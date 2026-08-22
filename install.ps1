# Inno Agent Installer for Windows PowerShell
#
# One-line usage:
#   irm https://<host>/install.ps1 | iex
#
# A piped install takes options as environment variables set beforehand
# (INNO_HOME, INNO_REPO_URL, INNO_PORT, ...) because the web entry point
# cannot forward arguments; a local run accepts the same variables.
# Install dir priority: INNO_HOME > $USERPROFILE\.local\opt\inno-agent
#
# The content hub defaults to the teacher's GitHub hub (karsarobert/
# inno-agent-hub, branch main) so skills and preset cards are available
# right after install. Set INNO_HUB_TYPE=none for a fully offline install
# (no skills, no preset cards), or INNO_HUB_TYPE=bundle + INNO_HUB_URL for
# a self-hosted hub.
#
# SPDX-License-Identifier: MIT
function Install-InnoAgent {
    $ErrorActionPreference = "Stop"
    # PowerShell 7.3+ treats native stderr output as an error record when
    # $ErrorActionPreference=Stop, so harmless npm/node warnings (e.g.
    # "npm warn deprecated ...") would abort the installer. Disable that
    # so only $LASTEXITCODE decides success. No-op on Windows PowerShell 5.1.
    $PSNativeCommandUseErrorActionPreference = $false
    # A profile that sets 'None' for $PSModuleAutoLoadingPreference makes
    # ConvertTo-Json / Invoke-WebRequest stop resolving on PowerShell 7.
    $PSModuleAutoLoadingPreference = 'All'
    # 5.1 redraws the IWR progress bar on every read; that redraw sets the
    # download rate. Kill it before any download in this script.
    $ProgressPreference = 'SilentlyContinue'

    function Write-Step([string]$Label, [string]$Message, [string]$Color = 'Green') {
        Write-Host ("  {0,-15} {1}" -f $Label, $Message) -ForegroundColor $Color
    }
    function Write-SubStep([string]$Message) {
        Write-Host ("  {0,-15} {1}" -f '', $Message) -ForegroundColor 'DarkGray'
    }
    function Write-Err([string]$Message) {
        Write-Host "ERROR: $Message" -ForegroundColor 'Red'
        exit 1
    }
    # Run a native command (git/node/npm) and return $LASTEXITCODE.
    # With $ErrorActionPreference=Stop, PowerShell 5.1/7.x wraps native
    # stderr lines in ErrorRecords and can abort the script on harmless
    # warnings ("npm warn deprecated ...", "From https://..."). We lower
    # the preference to Continue for the native call only, so stderr is
    # swallowed and only the exit code decides success. Works on every
    # PowerShell version (the $PSNativeCommandUseErrorActionPreference
    # variable only exists in 7.3+).
    function Invoke-Native {
        param([string]$FilePath, [string[]]$Arguments)
        $oldEap = $ErrorActionPreference
        $ErrorActionPreference = 'Continue'
        try {
            & $FilePath @Arguments 2>&1 | Out-Null
            return $LASTEXITCODE
        } finally {
            $ErrorActionPreference = $oldEap
        }
    }

    # Write a text file as UTF-8 WITHOUT a BOM. PowerShell 5.1's
    # Set-Content -Encoding UTF8 prepends a BOM that Node's JSON.parse
    # rejects, so all config/launcher files go through this helper.
    function Write-Utf8NoBom([string]$Path, [string]$Content) {
        [System.IO.File]::WriteAllText($Path, $Content, (New-Object System.Text.UTF8Encoding($false)))
    }

    # ── Options (env vars; defaults for a clean install) ──
    $InnoHome = if ($env:INNO_HOME) { $env:INNO_HOME } else { Join-Path $env:USERPROFILE '.local\opt\inno-agent' }
    $InnoRepoUrl = if ($env:INNO_REPO_URL) { $env:INNO_REPO_URL } else { 'https://github.com/karsarobert/inno-agent.git' }
    $InnoBranch = if ($env:INNO_BRANCH) { $env:INNO_BRANCH } else { 'main' }
    $InnoPort = if ($env:INNO_PORT) { $env:INNO_PORT } else { '3000' }
    $InnoSkipBuild = $env:INNO_SKIP_BUILD -eq '1'
    $InnoSkipStart = $env:INNO_SKIP_START -eq '1'
    $InnoHubType = if ($env:INNO_HUB_TYPE) { $env:INNO_HUB_TYPE } else { 'github' }
    $InnoHubUrl = if ($env:INNO_HUB_URL) { $env:INNO_HUB_URL } else { '' }
    $InnoProviderBaseUrl = if ($env:INNO_PROVIDER_BASE_URL) { $env:INNO_PROVIDER_BASE_URL } else { '' }
    $InnoProviderApiKey = if ($env:INNO_PROVIDER_API_KEY) { $env:INNO_PROVIDER_API_KEY } else { '' }
    $InnoProviderModel = if ($env:INNO_PROVIDER_MODEL) { $env:INNO_PROVIDER_MODEL } else { '' }

    $Rule = '─' * 52
    Write-Host ""
    Write-Host $Rule -ForegroundColor 'DarkCyan'
    Write-Host "  Inno Agent installer" -ForegroundColor 'DarkCyan'
    Write-Host $Rule -ForegroundColor 'DarkCyan'
    Write-Host ""

    # ── 1. Prerequisites: git ──
    Write-Step 'Prereq' 'checking git...'
    $Git = Get-Command git -ErrorAction SilentlyContinue
    if (-not $Git) { Write-Err 'git is required but not installed. Install Git for Windows (https://git-scm.com/download/win) and re-run.' }
    Write-Step 'Prereq' ("git {0}" -f (& git --version))

    # ── 2. Node.js >= 20.6 ──
    Write-Step 'Prereq' 'checking Node.js (>=20.6)...'
    $Node = Get-Command node -ErrorAction SilentlyContinue
    $NodeOk = $false
    if ($Node) {
        $NodeVer = (& node --version) -replace '^v', ''
        $NodeMajor = [int]($NodeVer.Split('.')[0])
        $NodeMinor = [int]($NodeVer.Split('.')[1])
        if ($NodeMajor -gt 20 -or ($NodeMajor -eq 20 -and $NodeMinor -ge 6)) { $NodeOk = $true }
    }
    if (-not $NodeOk) {
        Write-Err "Node.js >= 20.6 is required but not found (got: $(if ($Node) { & node --version } else { 'none' })). Install it from https://nodejs.org (LTS 22+) and re-run, or set INNO_SKIP_NODE_CHECK=1 if a suitable node is already on PATH."
    }
    Write-Step 'Prereq' ("node {0}" -f (& node --version))
    $Npm = Get-Command npm -ErrorAction SilentlyContinue
    if (-not $Npm) { Write-Err 'npm is required but not installed.' }
    Write-Step 'Prereq' ("npm {0}" -f (& npm --version))

    # ── 3. Clone / update the repo ──
    Write-Step 'Install' "preparing $InnoHome..."
    if (Test-Path (Join-Path $InnoHome '.git')) {
        Write-Step 'Install' 'updating existing checkout...'
        Push-Location $InnoHome
        try {
            Invoke-Native 'git' @('fetch', 'origin', $InnoBranch) | Out-Null
            Invoke-Native 'git' @('checkout', '-q', $InnoBranch) | Out-Null
            $pullCode = Invoke-Native 'git' @('pull', '-q', '--ff-only')
            if ($pullCode -ne 0) { Write-Err 'git pull failed.' }
        } finally { Pop-Location }
    } else {
        New-Item -ItemType Directory -Force -Path (Split-Path $InnoHome) | Out-Null
        $cloneCode = Invoke-Native 'git' @('clone', '-q', '--depth', '1', '--branch', $InnoBranch, $InnoRepoUrl, $InnoHome)
        if ($cloneCode -ne 0) { Write-Err "git clone failed: $InnoRepoUrl" }
    }
    Write-Step 'Install' 'repo ready'

    # The inno-agent repo root IS the app (npm monorepo: package.json at root).
    $AppDir = $InnoHome

    # ── 4. Dependencies + build ──
    if ($InnoSkipBuild) {
        Write-Step 'Build' 'skipped (INNO_SKIP_BUILD=1)'
    } else {
        Write-Step 'Build' 'npm install (this can take a while)...'
        Push-Location $AppDir
        try {
            $ciCode = Invoke-Native 'npm' @('ci')
            if ($ciCode -ne 0) { $ciCode = Invoke-Native 'npm' @('install') }
            if ($ciCode -ne 0) { Write-Err 'npm install failed.' }
            Write-Step 'Build' 'npm run build...'
            $buildCode = Invoke-Native 'npm' @('run', 'build')
            if ($buildCode -ne 0) { Write-Err 'build failed; re-run with INNO_SKIP_BUILD=1 to skip' }
        } finally { Pop-Location }
        Write-Step 'Build' 'built'
    }

    # ── 5. Clean runtime config ──
    Write-Step 'Config' 'writing clean runtime config...'
    $RuntimeDir = Join-Path $AppDir 'runtime'
    New-Item -ItemType Directory -Force -Path (Join-Path $RuntimeDir 'config'), (Join-Path $RuntimeDir 'data'), (Join-Path $RuntimeDir 'skills'), (Join-Path $AppDir 'workspace') | Out-Null

    $DefaultProvider = 'default'
    $DefaultModel = ''
    $Providers = @{}
    if ($InnoProviderBaseUrl) {
        $ModelId = if ($InnoProviderModel) { $InnoProviderModel } else { 'placeholder-model' }
        $Providers['default'] = @{
            id = 'default'
            baseUrl = $InnoProviderBaseUrl
            api = 'openai-completions'
            apiKey = $InnoProviderApiKey
            models = @(@{ id = $ModelId; name = $ModelId; input = @('text'); contextWindow = 128000; maxTokens = 8192 })
        }
        $DefaultModel = $ModelId
        Write-Step 'Config' 'provider configured via INNO_PROVIDER_*'
    } else {
        # The app requires at least one provider (baseUrl + model); apiKey may
        # be empty. Ship a placeholder the user completes in the Settings UI.
        $Providers['default'] = @{
            id = 'default'
            baseUrl = 'http://127.0.0.1:8000/v1'
            api = 'openai-completions'
            apiKey = ''
            models = @(@{ id = 'placeholder-model'; name = 'Placeholder model - set up in Settings'; input = @('text'); contextWindow = 128000; maxTokens = 8192 })
        }
        $DefaultModel = 'placeholder-model'
        Write-Step 'Config' 'placeholder provider written; set the real one in Settings UI'
    }

    # A self-hosted hub URL forces bundle type and carries the base URL.
    if ($InnoHubUrl) {
        $InnoHubType = 'bundle'
        Write-Step 'Config' "content hub: bundle @ $InnoHubUrl"
    }
    if ($InnoHubType -eq 'github') {
        # Default: the teacher's GitHub hub (karsarobert/inno-agent-hub, main).
        $ContentHub = @{
            type = 'github'; owner = 'karsarobert'; repo = 'inno-agent-hub'; ref = 'main'
            skillsPath = 'skill-library'; presetsPath = 'workspace-templates'
            baseUrl = ''; token = ''
        }
    } else {
        $ContentHub = @{ type = $InnoHubType; baseUrl = $InnoHubUrl }
    }
    $Config = [ordered]@{
        defaultProvider = $DefaultProvider
        defaultModel = $DefaultModel
        providers = $Providers
        server = @{ port = [int]$InnoPort }
        contentHub = $ContentHub
        subagents = @{ enabled = $false }
        memory = @{ l1Enabled = $true; l2Enabled = $true; l3Enabled = $true }
    }
    $ConfigJson = $Config | ConvertTo-Json -Depth 8
    Write-Utf8NoBom (Join-Path $RuntimeDir 'config\config.json') $ConfigJson
    Write-Step 'Config' "contentHub: $InnoHubType"

    # ── 6. Start Menu shortcut + desktop icon ──
    Write-Step 'Menu' 'installing Start Menu shortcut...'
    $LauncherPath = Join-Path $InnoHome 'inno-agent.ps1'
    $LauncherContent = @"
# Inno Agent launcher - start the server if needed, then open the web UI.
`$Port = $InnoPort
`$AppDir = "$InnoHome"
`$LogFile = Join-Path `$AppDir 'inno-agent.log'
`$Healthy = `$false
try {
    `$Resp = Invoke-WebRequest -UseBasicParsing -Uri "http://127.0.0.1:`$Port/health" -TimeoutSec 2
    if (`$Resp.StatusCode -eq 200) { `$Healthy = `$true }
} catch { }
if (-not `$Healthy) {
    `$ErrFile = Join-Path `$AppDir 'inno-agent.err.log'
    `$Proc = Start-Process -FilePath 'npm.cmd' -ArgumentList @('run', 'server', '--', '--home', './runtime', '--workspace', './workspace', '--port', "`$Port") -WorkingDirectory `$AppDir -RedirectStandardOutput `$LogFile -RedirectStandardError `$ErrFile -PassThru -WindowStyle Hidden
    for (`$i = 0; `$i -lt 30; `$i++) {
        Start-Sleep -Seconds 1
        try {
            `$Resp = Invoke-WebRequest -UseBasicParsing -Uri "http://127.0.0.1:`$Port/health" -TimeoutSec 2
            if (`$Resp.StatusCode -eq 200) { break }
        } catch { }
    }
}
Start-Process "http://localhost:`$Port"
"@
    Write-Utf8NoBom $LauncherPath $LauncherContent

    $StartMenuDir = Join-Path $env:APPDATA 'Microsoft\Windows\Start Menu\Programs'
    $ShortcutPath = Join-Path $StartMenuDir 'Inno Agent.lnk'
    $WshShell = New-Object -ComObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut($ShortcutPath)
    $Shortcut.TargetPath = 'powershell.exe'
    $Shortcut.Arguments = "-NoProfile -ExecutionPolicy Bypass -File `"$LauncherPath`""
    $Shortcut.WorkingDirectory = $InnoHome
    $Shortcut.IconLocation = (Join-Path $InnoHome 'build\icon.png')
    $Shortcut.Description = 'Inno Agent - personal learning agent'
    $Shortcut.Save()
    Write-Step 'Menu' 'Start Menu shortcut created (Inno Agent)'

    # ── 7. Start + health check ──
    if ($InnoSkipStart) {
        Write-Step 'Start' 'skipped (INNO_SKIP_START=1)'
    } else {
        Write-Step 'Start' "starting Inno Agent on :$InnoPort..."
        $LogFile = Join-Path $InnoHome 'inno-agent.log'
        $ErrFile = Join-Path $InnoHome 'inno-agent.err.log'
        $Proc = Start-Process -FilePath 'npm.cmd' -ArgumentList @('run', 'server', '--', '--home', './runtime', '--workspace', './workspace', '--port', $InnoPort) -WorkingDirectory $AppDir -RedirectStandardOutput $LogFile -RedirectStandardError $ErrFile -PassThru -WindowStyle Hidden
        $Healthy = $false
        for ($i = 0; $i -lt 30; $i++) {
            Start-Sleep -Seconds 1
            try {
                $Resp = Invoke-WebRequest -UseBasicParsing -Uri "http://127.0.0.1:$InnoPort/health" -TimeoutSec 2
                if ($Resp.StatusCode -eq 200) { $Healthy = $true; break }
            } catch { }
        }
        if ($Healthy) {
            Write-Step 'Start' 'healthy'
        } else {
            Write-Step 'Start' "server did not become healthy; check $LogFile" 'Yellow'
        }
    }

    # ── Summary ──
    Write-Host ""
    Write-Host $Rule -ForegroundColor 'DarkCyan'
    Write-Host "  Inno Agent installed" -ForegroundColor 'DarkCyan'
    Write-Host $Rule -ForegroundColor 'DarkCyan'
    Write-Host ""
    if (-not $InnoSkipStart) {
        Write-SubStep "Web UI:  http://localhost:$InnoPort"
    }
    Write-SubStep "Install: $InnoHome"
    Write-SubStep "Config:  $RuntimeDir\config\config.json"
    Write-SubStep "Log:     $LogFile"
    Write-SubStep 'Menu:    Inno Agent - Start Menu shortcut created'
    if ($InnoSkipStart) {
        Write-SubStep "Start:   $LauncherPath (or from the Start Menu)"
    }
    Write-SubStep 'Update:  git pull; cd app; npm ci; npm run build'
    Write-Host ""
    if ($InnoHubType -eq 'none') {
        Write-SubStep 'Content hub: DISABLED (no skills, no preset cards).'
        Write-SubStep 'To enable a hub later, use Settings > Content Hub in the UI.'
    } else {
        Write-SubStep 'Content hub: GitHub karsarobert/inno-agent-hub (main)'
        Write-SubStep 'To disable it, use Settings > Content Hub in the UI or INNO_HUB_TYPE=none.'
    }
    Write-Host ""
}

Install-InnoAgent @args
