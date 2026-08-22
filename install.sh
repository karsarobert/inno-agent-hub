#!/bin/sh
#
# Inno Agent Installer
#
# One-line usage (Linux/macOS):
#   curl -fsSL https://<host>/install.sh | sh
#
# A piped install takes options as environment variables after the pipe
# (INNO_HOME, INNO_REPO_URL, INNO_PORT, ...) because a bare flag after the
# pipe would be read as an option to sh itself; a local run accepts the same
# variables. Install dir priority: INNO_HOME > ~/.local/opt/inno-agent.
#
# The content hub defaults to the teacher's GitHub hub (karsarobert/
# inno-agent-hub, branch main) so skills and preset cards are available
# right after install. Set INNO_HUB_TYPE=none for a fully offline install
# (no skills, no preset cards), or INNO_HUB_TYPE=bundle + INNO_HUB_URL for
# a self-hosted hub.
#
# SPDX-License-Identifier: MIT
set -e

# ── Why the installer lives in a function ──
# Under a piped web install, sh is the pipe READER. Wrapping the body forces
# sh to parse to the closing brace first, so the pipe always drains.
# `exit` still exits the shell from inside a function.
_inno_main() {

# ── Output style ──
RULE=""
_i=0
while [ "$_i" -lt 52 ]; do
    RULE="${RULE}─"
    _i=$((_i + 1))
done
if [ -n "${NO_COLOR:-}" ]; then
    C_TITLE= C_DIM= C_OK= C_WARN= C_ERR= C_RST=
elif [ -t 1 ] || [ -n "${FORCE_COLOR:-}" ]; then
    _ESC="$(printf '\033')"
    C_TITLE="${_ESC}[38;5;150m"
    C_DIM="${_ESC}[38;5;245m"
    C_OK="${_ESC}[38;5;108m"
    C_WARN="${_ESC}[38;5;136m"
    C_ERR="${_ESC}[91m"
    C_RST="${_ESC}[0m"
else
    C_TITLE= C_DIM= C_OK= C_WARN= C_ERR= C_RST=
fi

step()    { printf "  ${C_DIM}%-15.15s${C_RST}${3:-$C_OK}%s${C_RST}\n" "$1" "$2"; }
substep() { printf "  ${C_DIM}%-15s${2:-$C_DIM}%s${C_RST}\n" "" "$1"; }
die()     { printf "${C_ERR}ERROR: %s${C_RST}\n" "$1" >&2; exit 1; }

# ── Options (env vars; defaults for a clean install) ──
INNO_HOME="${INNO_HOME:-$HOME/.local/opt/inno-agent}"
INNO_REPO_URL="${INNO_REPO_URL:-https://github.com/karsarobert/inno-agent.git}"
INNO_BRANCH="${INNO_BRANCH:-main}"
INNO_PORT="${INNO_PORT:-3000}"
INNO_SKIP_BUILD="${INNO_SKIP_BUILD:-0}"
INNO_SKIP_START="${INNO_SKIP_START:-0}"
INNO_NODE_VER="${INNO_NODE_VER:-22}"
# Default provider/model stay EMPTY: the user configures them in the
# Settings UI after install. The content hub defaults to GitHub
# (karsarobert/inno-agent-hub); set INNO_HUB_TYPE=none to disable it, or
# INNO_HUB_TYPE=bundle and INNO_HUB_URL for a self-hosted content hub
# (e.g. an inno-hub on the local network).
INNO_HUB_TYPE="${INNO_HUB_TYPE:-github}"
INNO_HUB_URL="${INNO_HUB_URL:-}"
INNO_PROVIDER_BASE_URL="${INNO_PROVIDER_BASE_URL:-}"
INNO_PROVIDER_API_KEY="${INNO_PROVIDER_API_KEY:-}"
INNO_PROVIDER_MODEL="${INNO_PROVIDER_MODEL:-}"

echo ""
echo "${C_TITLE}${RULE}${C_RST}"
echo "${C_TITLE}  Inno Agent installer${C_RST}"
echo "${C_TITLE}${RULE}${C_RST}"
echo ""

# ── 1. OS / arch detection ──
step "System" "detecting OS and architecture..."
OS="$(uname -s 2>/dev/null || echo unknown)"
ARCH="$(uname -m 2>/dev/null || echo unknown)"
case "$OS" in
    Linux*)  OS="linux" ;;
    Darwin*) OS="macos" ;;
    *)       die "unsupported OS: $OS (Windows? use install.ps1)" ;;
esac
case "$ARCH" in
    x86_64|amd64) ARCH="x64" ;;
    arm64|aarch64) ARCH="arm64" ;;
    *) die "unsupported architecture: $ARCH" ;;
esac
step "System" "${OS}/${ARCH}"

# ── 2. Prerequisites: git ──
step "Prereq" "checking git..."
command -v git >/dev/null 2>&1 || die "git is required but not installed."
step "Prereq" "git $(git --version | awk '{print $3}')"

# ── 3. Node.js >= 20.6 (nvm fallback) ──
step "Prereq" "checking Node.js (>=20.6)..."
NODE_BIN="$(command -v node || true)"
NODE_OK=0
if [ -n "$NODE_BIN" ]; then
    NODE_MAJOR="$(node --version 2>/dev/null | sed 's/^v//' | cut -d. -f1)"
    NODE_MINOR="$(node --version 2>/dev/null | sed 's/^v//' | cut -d. -f2)"
    if [ "${NODE_MAJOR:-0}" -gt 20 ] || { [ "${NODE_MAJOR:-0}" -eq 20 ] && [ "${NODE_MINOR:-0}" -ge 6 ]; }; then
        NODE_OK=1
    fi
fi
if [ "$NODE_OK" -ne 1 ]; then
    # Try nvm as a user-level fallback (no sudo needed).
    if [ -s "$HOME/.nvm/nvm.sh" ]; then
        step "Prereq" "installing Node.js $INNO_NODE_VER via nvm..."
        # shellcheck disable=SC1091
        . "$HOME/.nvm/nvm.sh"
        nvm install "$INNO_NODE_VER" >/dev/null 2>&1
        nvm use "$INNO_NODE_VER" >/dev/null 2>&1
        NODE_BIN="$(command -v node)"
        step "Prereq" "node $(node --version) via nvm"
    else
        die "Node.js >= 20.6 is required but not found (got: ${NODE_BIN:+$(node --version 2>/dev/null)}). \
Install it (e.g. 'curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | sh') and re-run, \
or set INNO_SKIP_NODE_CHECK=1 if a suitable node is already on PATH."
    fi
fi
[ "$INNO_SKIP_NODE_CHECK" = "1" ] || { command -v node >/dev/null 2>&1 || die "node not found"; }
step "Prereq" "node $(node --version)"
command -v npm >/dev/null 2>&1 || die "npm is required but not installed."
step "Prereq" "npm $(npm --version)"

# ── 4. Clone / update the repo ──
step "Install" "preparing $INNO_HOME..."
if [ -d "$INNO_HOME/.git" ]; then
    step "Install" "updating existing checkout..."
    ( cd "$INNO_HOME" && git fetch origin "$INNO_BRANCH" >/dev/null 2>&1 && git checkout -q "$INNO_BRANCH" && git pull -q --ff-only )
else
    mkdir -p "$(dirname "$INNO_HOME")"
    git clone -q --depth 1 --branch "$INNO_BRANCH" "$INNO_REPO_URL" "$INNO_HOME" || die "git clone failed: $INNO_REPO_URL"
fi
step "Install" "repo ready"

# The inno-agent repo root IS the app (npm monorepo: package.json at root).
APP_DIR="$INNO_HOME"

# ── 5. Dependencies + build ──
if [ "$INNO_SKIP_BUILD" = "1" ]; then
    step "Build" "skipped (INNO_SKIP_BUILD=1)"
else
    step "Build" "npm install (this can take a while)..."
    ( cd "$APP_DIR" && npm ci >/dev/null 2>&1 ) || ( cd "$APP_DIR" && npm install )
    step "Build" "npm run build..."
    ( cd "$APP_DIR" && npm run build >/dev/null 2>&1 ) || die "build failed; re-run with INNO_SKIP_BUILD=1 to skip"
    step "Build" "built"
fi

# ── 6. Clean runtime config ──
step "Config" "writing clean runtime config..."
mkdir -p "$APP_DIR/runtime/config" "$APP_DIR/runtime/data" "$APP_DIR/runtime/skills" "$APP_DIR/workspace"
# The app requires at least one provider with a baseUrl and a model; the
# apiKey may be empty. Without INNO_PROVIDER_* we ship a placeholder
# provider that the user completes in the Settings UI.
if [ -n "$INNO_PROVIDER_BASE_URL" ]; then
    PROVIDER_ID="default"
    PROVIDER_BASE_URL="$INNO_PROVIDER_BASE_URL"
    PROVIDER_API_KEY="${INNO_PROVIDER_API_KEY:-}"
    PROVIDER_MODEL="${INNO_PROVIDER_MODEL:-placeholder-model}"
    PROVIDER_JSON="{\"id\":\"$PROVIDER_ID\",\"baseUrl\":\"$PROVIDER_BASE_URL\",\"api\":\"openai-completions\",\"apiKey\":\"$PROVIDER_API_KEY\",\"models\":[{\"id\":\"$PROVIDER_MODEL\",\"name\":\"$PROVIDER_MODEL\",\"input\":[\"text\"],\"contextWindow\":128000,\"maxTokens\":8192}]}"
    PROVIDERS_JSON="{\"$PROVIDER_ID\":$PROVIDER_JSON}"
    DEFAULT_PROVIDER="\"$PROVIDER_ID\""
    DEFAULT_MODEL="\"$PROVIDER_MODEL\""
    step "Config" "provider configured via INNO_PROVIDER_*"
else
    PROVIDERS_JSON="{\"default\":{\"id\":\"default\",\"baseUrl\":\"http://127.0.0.1:8000/v1\",\"api\":\"openai-completions\",\"apiKey\":\"\",\"models\":[{\"id\":\"placeholder-model\",\"name\":\"Placeholder model - set up in Settings\",\"input\":[\"text\"],\"contextWindow\":128000,\"maxTokens\":8192}]}}"
    DEFAULT_PROVIDER="\"default\""
    DEFAULT_MODEL="\"placeholder-model\""
    step "Config" "placeholder provider written; set the real one in Settings UI"
fi
if [ -n "$INNO_HUB_URL" ]; then
    # Self-hosted hub: force bundle type and carry the base URL.
    INNO_HUB_TYPE="bundle"
    HUB_BASE_URL_JSON="\"$INNO_HUB_URL\""
    step "Config" "content hub: bundle @ $INNO_HUB_URL"
else
    HUB_BASE_URL_JSON="\"\""
fi
if [ "$INNO_HUB_TYPE" = "github" ]; then
    # Default: the teacher's GitHub hub (karsarobert/inno-agent-hub, main).
    CONTENT_HUB_JSON="{ \"type\": \"github\", \"owner\": \"karsarobert\", \"repo\": \"inno-agent-hub\", \"ref\": \"main\", \"skillsPath\": \"skill-library\", \"presetsPath\": \"workspace-templates\", \"baseUrl\": \"\", \"token\": \"\" }"
else
    CONTENT_HUB_JSON="{ \"type\": \"$INNO_HUB_TYPE\", \"baseUrl\": $HUB_BASE_URL_JSON }"
fi
cat > "$APP_DIR/runtime/config/config.json" <<EOF
{
    "defaultProvider": $DEFAULT_PROVIDER,
    "defaultModel": $DEFAULT_MODEL,
    "providers": $PROVIDERS_JSON,
    "server": { "port": $INNO_PORT },
    "contentHub": $CONTENT_HUB_JSON,
    "subagents": { "enabled": false },
    "memory": { "l1Enabled": true, "l2Enabled": true, "l3Enabled": true }
}
EOF
step "Config" "contentHub: $INNO_HUB_TYPE"

# ── 8. Desktop launcher + app-menu icon ──
step "Menu" "installing desktop launcher + icon..."
XDG_ICON_DIR="$HOME/.local/share/icons"
XDG_APP_DIR="$HOME/.local/share/applications"
mkdir -p "$XDG_ICON_DIR" "$XDG_APP_DIR"
cp "$APP_DIR/build/icon.png" "$XDG_ICON_DIR/inno-agent.png" 2>/dev/null || true

# Launcher: start the server when needed, then open the web UI. Used by the
# .desktop entry so the app can be started from the menu at any time.
LAUNCHER="$INNO_HOME/inno-agent.sh"
cat > "$LAUNCHER" <<EOF
#!/bin/sh
# Inno Agent launcher — start the server if needed, then open the web UI.
PORT=$INNO_PORT
APP_DIR="$INNO_HOME"
LOG="\$APP_DIR/inno-agent.log"
# Desktop launchers start with a minimal PATH; re-source nvm when present so
# a user-level Node install is found.
if [ -s "\$HOME/.nvm/nvm.sh" ]; then
    export NVM_DIR="\$HOME/.nvm"
    # shellcheck disable=SC1091
    . "\$HOME/.nvm/nvm.sh"
fi
if ! curl -fsS "http://127.0.0.1:\$PORT/health" >/dev/null 2>&1; then
    ( cd "\$APP_DIR" && nohup npm run server -- --home ./runtime --workspace ./workspace --port "\$PORT" >>"\$LOG" 2>&1 & echo \$! > "\$APP_DIR/inno-agent.pid" )
    _tries=0
    while [ "\$_tries" -lt 30 ]; do
        curl -fsS "http://127.0.0.1:\$PORT/health" >/dev/null 2>&1 && break
        _tries=\$((_tries + 1))
        sleep 1
    done
fi
# Open the web UI (xdg-open on Linux, open on macOS).
if command -v xdg-open >/dev/null 2>&1; then
    xdg-open "http://localhost:\$PORT" >/dev/null 2>&1 &
elif command -v open >/dev/null 2>&1; then
    open "http://localhost:\$PORT"
fi
EOF
chmod +x "$LAUNCHER"

cat > "$XDG_APP_DIR/inno-agent.desktop" <<EOF
[Desktop Entry]
Type=Application
Name=Inno Agent
Comment=Personal learning agent
Exec="$LAUNCHER"
Icon=$XDG_ICON_DIR/inno-agent.png
Terminal=false
Categories=Education;
StartupNotify=true
EOF
# Refresh the XDG application database when available (harmless if absent).
command -v update-desktop-database >/dev/null 2>&1 && update-desktop-database "$XDG_APP_DIR" >/dev/null 2>&1 || true
step "Menu" "launcher installed (Inno Agent in the app menu)"

# ── 9. Start + health check ──
if [ "$INNO_SKIP_START" = "1" ]; then
    step "Start" "skipped (INNO_SKIP_START=1)"
else
    step "Start" "starting Inno Agent on :$INNO_PORT..."
    ( cd "$APP_DIR" && nohup npm run server -- --home ./runtime --workspace ./workspace --port "$INNO_PORT" >"$INNO_HOME/inno-agent.log" 2>&1 & echo $! > "$INNO_HOME/inno-agent.pid" )
    _tries=0
    while [ "$_tries" -lt 30 ]; do
        if curl -fsS "http://127.0.0.1:$INNO_PORT/health" >/dev/null 2>&1; then
            break
        fi
        _tries=$((_tries + 1))
        sleep 1
    done
    if curl -fsS "http://127.0.0.1:$INNO_PORT/health" >/dev/null 2>&1; then
        step "Start" "healthy"
    else
        step "Start" "server did not become healthy; check $INNO_HOME/inno-agent.log" "${C_WARN}"
    fi
fi

# ── Summary ──
echo ""
echo "${C_TITLE}${RULE}${C_RST}"
echo "${C_TITLE}  Inno Agent installed${C_RST}"
echo "${C_TITLE}${RULE}${C_RST}"
echo ""
if [ "$INNO_SKIP_START" != "1" ]; then
    substep "Web UI:  http://localhost:$INNO_PORT"
fi
substep "Install: $INNO_HOME"
substep "Config:  $INNO_HOME/runtime/config/config.json"
substep "Log:     $INNO_HOME/inno-agent.log"
if [ "$INNO_SKIP_START" = "1" ]; then
    substep "Start:   $LAUNCHER (or from the app menu)"
fi
substep "Menu:    Inno Agent — start it anytime from the app menu"
substep "Update:  cd $INNO_HOME && git pull && npm ci && npm run build"
echo ""
if [ -n "$INNO_HUB_URL" ]; then
    substep "Content hub: enabled ($INNO_HUB_TYPE @ $INNO_HUB_URL)"
elif [ "$INNO_HUB_TYPE" = "none" ]; then
    substep "Content hub: DISABLED (no skills, no preset cards)."
    substep "To enable a hub later, use Settings > Content Hub in the UI."
else
    substep "Content hub: GitHub karsarobert/inno-agent-hub (main)"
    substep "To disable it, use Settings > Content Hub in the UI or INNO_HUB_TYPE=none."
fi
echo ""

}

# Every byte above is parsed before this line runs, which is the point.
_inno_main "$@"
