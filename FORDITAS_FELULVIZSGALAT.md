# Inno Agent backend – kínai → magyar fordítási felülvizsgálat

Összesen 257 string-cserélés, 28 fájlban. A táblázat az eredeti (kínai) és a magyar szöveget mutatja; a kódban a cserék már alkalmazva vannak.

## `apps/inno-agent/src/agent/document-tools.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| 解析文档 | Dokumentum feldolgozása |
| 解析 PDF、Word、Excel、PPT 或图片文件，提取文本内容。 | PDF, Word, Excel, PPT vagy képfájlok feldolgozása szöveg kinyeréséhez. |
| 用户想查看文件内容、提取文本、或需要先预览再决定是否归档时调用。 | Akkor hívd, ha a felhasználó meg szeretné nézni egy fájl tartalmát, szöveget szeretne kinyerni, vagy előbb előnézetet szeretne, mielőtt eldönti, archiválja-e. |
| 支持格式：.pdf, .docx, .xlsx, .pptx, .png, .jpg, .jpeg, .gif, .webp, .tiff | Támogatott formátumok: .pdf, .docx, .xlsx, .pptx, .png, .jpg, .jpeg, .gif, .webp, .tiff |
| 文件路径（绝对路径或相对于工作目录的路径） | Fájl elérési út (abszolút vagy a munkakönyvtárhoz viszonyított) |
| 为 true 时返回每页的文本，默认只返回合并后的全文 | true esetén oldalanként adja vissza a szöveget; alapértelmezés szerint csak az összefűzött teljes szöveget |
| 为 true 时返回每页的 PNG 截图（仅 PDF 支持），默认 false | true esetén oldalanként PNG-képernyőképet ad vissza (csak PDF-nél); alapértelmezés szerint false |
| --- 提取文本 --- | --- Kinyert szöveg --- |
| --- 逐页文本 --- | --- Oldalankénti szöveg --- |
| \n[截图生成失败，可能不支持该文件格式的截图] | \n[A képernyőkép generálása sikertelen; a fájlformátum valószínűleg nem támogatja] |

## `apps/inno-agent/src/agent/inno-extension.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| # 当前会话文件工作区 | # Az aktuális munkamenet fájlmunkaterülete |
| 调用 write 或 edit 时必须使用相对于该目录的路径，例如 `notes.md` 或 `src/main.py`。 | A write vagy edit hívásakor ehhez a könyvtárhoz viszonyított elérési utat használj, például `notes.md` vagy `src/main.py`. |
| 不要使用该目录之外的绝对路径，也不要通过 `..` 或符号链接越过该目录；越界修改会被拒绝。 | Ne használj a könyvtáron kívüli abszolút elérési utat, és ne lépj ki belőle `..`-val vagy szimbolikus hivatkozással; a kívülre irányuló módosítás elutasításra kerül. |
| 文件路径无效，请使用当前工作区内的相对路径。 | Érvénytelen fájl elérési út; használj az aktuális munkaterületen belüli relatív elérési utat. |
| 不要使用 open/xdg-open 命令打开文件。文件生成后用户会在浏览器右侧的文件预览面板自动看到结果；如需引导用户查看，在回复里说明文件路径即可。 | Ne használd az open/xdg-open parancsokat fájl megnyitásához. A fájl létrehozása után a felhasználó automatikusan látja az eredményt a böngésző jobb oldali fájl-előnézeti paneljén; ha szeretnéd vezetni a felhasználót, a válaszban írd le a fájl elérési útját. |
| [最近一次代码运行] | [A legutóbbi kódfuttatás] |
| 结束: (运行中或异常退出) | Vége: (fut vagy rendellenesen kilépett) |
| 输出 (tail 80 行): | Kimenet (utolsó 80 sor): |
| (空) | (üres) |

## `apps/inno-agent/src/agent/ocr-tools.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| 图片文字识别 (OCR) | Képszöveg-felismerés (OCR) |
| 调用百度 vl-ocr（PaddleOCR-VL）API 提取图片中的文字，返回 markdown 文本。 | A Baidu vl-ocr (PaddleOCR-VL) API meghívása a képek szövegének kinyeréséhez; markdown szöveget ad vissza. |
| 当当前接入的模型不支持图片识别，或图片识别失败时调用。 | Akkor hívd, ha a jelenlegi modell nem támogatja a képfelismerést, vagy a képfelismerés sikertelen. |
| filePath 可以是工作区相对路径，也可以是 http(s) URL。 | A filePath lehet munkaterület-relative elérési út vagy http(s) URL is. |
| 支持 PNG / JPG / JPEG / GIF / WEBP / TIFF / PDF 等常见格式。 | Gyakori formátumok támogatottak: PNG / JPG / JPEG / GIF / WEBP / TIFF / PDF. |
| 要识别的图片路径（工作区相对路径、绝对路径或 http(s) URL） | A felismerendő kép elérési útja (munkaterület-relative, abszolút vagy http(s) URL) |
| 请提供 filePath（图片路径或 URL）。 | Adj meg filePath értéket (kép elérési út vagy URL). |
| 尚未配置 OCR API token。请在设置面板的「OCR API」卡片填入 token 后重试。 | Az OCR API token nincs beállítva. Töltsd ki a tokent a Beállítások „OCR API" kártyáján, majd próbáld újra. |
| OCR 轮询被中断（超时或取消） | Az OCR lekérdezés megszakadt (időtúllépés vagy törlés) |
| OCR 任务失败（未提供错误详情） | Az OCR feladat sikertelen (nincs hibarészlet) |
| OCR 任务完成但未返回结果 URL。 | Az OCR feladat befejeződött, de nem adott vissza eredmény-URL-t. |
| OCR 完成，但未从图片中提取到任何文字。 | Az OCR elkészült, de nem nyert ki szöveget a képből. |

## `apps/inno-agent/src/agent/pi-runner.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| [消息来源渠道: feishu] | [Üzenet forráscsatornája: feishu] |
| [消息来源渠道: wechat] | [Üzenet forráscsatornája: wechat] |
| [消息来源渠道: qq] | [Üzenet forráscsatornája: qq] |
| [消息来源渠道: web] | [Üzenet forráscsatornája: web] |
| 附件已下载到 | A melléklet letöltve ide: |
| [已中断,未完成回复] | [Megszakítva, befejezetlen válasz] |

## `apps/inno-agent/src/agent/practice-tools.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| 在当前会话绑定的工作区里创建一组学习实践文件(代码、数据、说明)。返回的结构化结果包含 mainFile 与 suggestedCommand,前端会自动打开 mainFile 并显示 Run 按钮。用户点 Run 才会真正运行,不要自己跑 bash。 | Hozz létre egy gyakorlófájl-készletet (kód, adat, leírás) az aktuális munkamenethez kötött munkaterületen. A visszaadott strukturált eredmény tartalmazza a mainFile-t és a suggestedCommand-ot; az előtér automatikusan megnyitja a mainFile-t, és megjeleníti a Run gombot. A kód csak akkor fut, ha a felhasználó a Run gombra kattint; ne futtass bash-t magad. |

## `apps/inno-agent/src/agent/system-prompt.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| 归档 | Archiválás |
| 保存到知识库 | Mentés a tudásbázisba |
| 帮我记下来 | Jegyezd meg nekem |
| 通过飞书提醒我 | Emlékeztess Feishun keresztül |
| 你好 | Szia |
| 有什么可以帮你 | Miben segíthetek |
| 跳过 | Kihagyás |
| 不用了 | Nem, köszönöm |
| 不想要引导 | Nem kérek útmutatást |
| 先看看再说 | Előbb megnézem |
| 下次 | Később |
| 好的，画像暂未建立。需要引导时随时叫我。 | Rendben, a profil még nem készült el. Ha útmutatásra van szükséged, szólj bármikor. |
| 你想学什么？选一个最接近的方向 | Mit szeretnél tanulni? Válaszd a hozzád legközelebb álló irányt |
| 在这个方向你目前是什么水平？ | Milyen szinten állsz jelenleg ezen a területen? |
| 你喜欢怎么学？可以多选 | Hogyan szeretsz tanulni? Többet is választhatsz |
| 你大概每周能投入多少时间学习？ | Körülbelül mennyi időt tudsz hetente tanulásra fordítani? |
| 学习节奏 | Tanulási ritmus |
| 画像已建立，现在我们开始吧！ | A profil elkészült, kezdjük is! |

## `apps/inno-agent/src/agent/tavily-tools.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| 未找到相关结果。 | Nem található releváns eredmény. |
| 联网搜索 (Tavily) | Internetes keresés (Tavily) |
| 通过 Tavily 搜索引擎联网检索最新信息，返回结果标题、URL、内容摘要和可选的综合答案。 | A Tavily keresőmotorral friss információkat keres az interneten; visszaadja az eredmények címét, URL-jét, tartalmi kivonatát és opcionálisan az összesített választ. |
| 当用户的问题涉及时事、最新资讯、超出知识截止日期的事实，或明确要求联网查询时使用。 | Akkor használd, ha a felhasználó kérdése aktuális eseményekre, friss hírekre, a tudáshatáridőn túli tényekre vonatkozik, vagy kifejezetten internetes keresést kér. |
| 优先用用户的语言构造 query；复杂或时效性强的查询可将 searchDepth 设为 advanced。 | A query-t lehetőleg a felhasználó nyelvén fogalmazd meg; bonyolult vagy időérzékeny lekérdezéseknél a searchDepth advanced értéket is kaphat. |
| 搜索查询词 | Keresőkifejezés |
| 检索深度：basic 快速（默认），advanced 更全但更慢更贵 | Keresési mélység: basic gyors (alapértelmezett), advanced alaposabb, de lassabb és drágább |
| 搜索主题：general（默认）/ news / finance | Keresési téma: general (alapértelmezett) / news / finance |
| 是否返回 Tavily 综合摘要答案（默认 true） | Visszaadja-e a Tavily összesített válaszát (alapértelmezés szerint true) |
| 请提供 query（搜索查询词）。 | Adj meg egy query értéket (keresőkifejezést). |
| 尚未配置 Tavily API Key。请在设置面板的「联网搜索 (Tavily)」卡片填入 API Key 后重试。 | A Tavily API-kulcs nincs beállítva. Töltsd ki az API-kulcsot a Beállítások „Internetes keresés (Tavily)" kártyáján, majd próbáld újra. |

## `apps/inno-agent/src/channels/channel-tools.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| 发送文件到渠道 | Fájl küldése csatornára |
| 把工作区里的某个文件发送到聊天渠道（如飞书）。 | Egy munkaterületi fájl elküldése csevegőcsatornára (pl. Feishu). |
| 当用户说「把 xxx 文件发给我」「发送到飞书/微信」「整理好后推给我」时调用。 | Akkor hívd, ha a felhasználó azt mondja: „küldd el nekem a xxx fájlt", „küldd el Feishu-ra/WeChatre" vagy „amikor kész, küldd el nekem". |
| filePath 是相对于当前工作区的路径。channel 可选，缺省时使用消息来源渠道的默认推送目标。 | A filePath a munkaterülethez viszonyított elérési út. A channel opcionális; ha nincs megadva, az üzenet forráscsatornájának alapértelmezett célját használja. |
| 注意：微信(iLink) 渠道暂不支持发送文件；如果用户未配置任何渠道，会返回提示让用户去配置。 | Megjegyzés: a WeChat (iLink) csatorna jelenleg nem támogatja a fájlküldést; ha a felhasználó nem konfigurált csatornát, a rendszer jelzi, hogy állítson be. |
| 要发送的文件路径（相对于当前工作区） | A küldendő fájl elérési útja (a munkaterülethez viszonyítva) |
| 目标渠道（可选）。缺省时使用已注册渠道的默认推送目标。 | Célcsatorna (opcionális). Alapértelmezésben a regisztrált csatorna alapértelmezett célját használja. |
| 推送目标 chat_id（可选）。缺省时使用该渠道的默认目标。 | Cél chat_id (opcionális). Alapértelmezésben az adott csatorna alapértelmezett célját használja. |
| 发送时显示的文件名（可选），默认用文件本身的名字。 | A küldéskor megjelenő fájlnév (opcionális); alapértelmezésben a fájl saját neve. |
| 你还没有配置任何消息渠道，无法发送文件。请先在设置里启用并配置飞书或微信等渠道后重试。 | Nincs beállítva üzenetcsatorna, ezért a fájl nem küldhető el. Előbb engedélyezz és konfigurálj egy csatornát (pl. Feishu vagy WeChat) a Beállításokban, majd próbáld újra. |

## `apps/inno-agent/src/channels/feishu/feishu-api.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| 💭 思考过程 | 💭 Gondolkodási folyamat |
| 等待回复中... | Válaszra vár… |
| 思考中... | Gondolkodás… |
| ✓ 回复完成 | ✓ Válasz elkészült |
| \n\n... *(内容过长已截断)* | \n\n... *(a tartalom túl hosszú, csonkolva)* |

## `apps/inno-agent/src/channels/feishu/feishu-channel.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| [用户发送了一张图片] | [A felhasználó egy képet küldött] |

## `apps/inno-agent/src/channels/personal-dispatcher.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| 新建对话 | Új beszélgetés |
| 新建会话 | Új munkamenet |
| 新建会话失败，请稍后重试。 | Az új munkamenet létrehozása sikertelen; próbáld újra később. |
| 消息过长，已截断处理。 | Az üzenet túl hosszú; csonkolva lett. |
| 这次处理失败了，请稍后重试。 | A feldolgozás sikertelen; próbáld újra később. |

## `apps/inno-agent/src/memory/l2/document-parser.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| 文件解析结果为空。可能是扫描件（需要 OCR）或文件内容为空。 | A fájl feldolgozásának eredménye üres. Lehet, hogy szkennelt dokumentum (OCR szükséges), vagy a fájl tartalma üres. |

## `apps/inno-agent/src/memory/l2/l2-tools.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| L2 Wiki 知识库已在设置中关闭，当前不归档也不检索知识库内容。 | Az L2 Wiki tudásbázis ki van kapcsolva a beállításokban; jelenleg sem archiválás, sem keresés nem történik benne. |
| 归档到 L2 Wiki | Archiválás az L2 Wiki-be |
| 将学习资料归档到 L2 Wiki 知识库。用户说「归档」「保存到知识库」「帮我记下来」或上传资料要求学习/总结时调用。 | Tananyag archiválása az L2 Wiki tudásbázisba. Akkor hívd, ha a felhasználó azt mondja: „archiválás", „mentés a tudásbázisba", „jegyezd meg nekem", vagy tananyagot tölt fel tanulás/összefoglalás céljából. |
| 支持文本(text)、Markdown(markdown)、对话片段(conversation)、PDF(pdf)、Word 文档(word)、图片(image)。 | Támogatott: szöveg (text), Markdown (markdown), beszélgetésrészlet (conversation), PDF (pdf), Word-dokumentum (word), kép (image). |
| 文本类内容传 content 参数；文件类内容传 filePath 参数。 | Szöveges tartalom esetén a content paramétert add meg; fájl esetén a filePath paramétert. |
| 资料标题 | Anyag címe |
| 要归档的文本内容（与 filePath 二选一） | Az archiválandó szöveges tartalom (a filePath helyett) |
| 要归档的文件路径（PDF/Word/Image），与 content 二选一 | Az archiválandó fájl elérési útja (PDF/Word/kép); a content helyett |
| 资料类型：text（纯文本）、markdown、conversation（对话片段）、pdf、word、image | Anyagtípus: text (sima szöveg), markdown, conversation (beszélgetésrészlet), pdf, word, image |
| 标签列表，如 ['python', 'async'] | Címkelista, pl. ['python', 'async'] |
| 来源类型，默认根据 sourceType 自动推断 | Forrástípus; alapértelmezésben a sourceType alapján automatikusan következtet |
| 来源 URL（网页、论文链接等） | Forrás URL (weboldal, tanulmányhivatkozás stb.) |
| 关联的会话 ID | Kapcsolódó munkamenet-azonosító |
| 为 true 时跳过重复检查，强制归档 | true esetén kihagyja az ismétlődés-ellenőrzést, és kényszerített archiválást végez |
| 参数错误：必须提供 content（文本内容）或 filePath（文件路径）。 | Paraméterhiba: meg kell adni content (szöveges tartalom) vagy filePath (fájl elérési út) értéket. |
| 无 | Nincs |
| 查询 L2 Wiki | L2 Wiki lekérdezése |
| 查询 L2 Wiki 知识库。当需要回答与已归档学习资料相关的问题时调用。 | Az L2 Wiki tudásbázis lekérdezése. Akkor hívd, ha az archivált tananyaggal kapcsolatos kérdésre kell válaszolni. |
| 先读取索引，再定位和读取相关页面，综合回答。 | Először olvasd be az indexet, majd keresd meg és olvasd be a releváns oldalakat, és összesítve válaszolj. |
| 参数 query 可省略或留空字符串，此时返回 Wiki 索引概览（用于查看有哪些内容）。 | A query paraméter elhagyható vagy üres lehet; ekkor a Wiki-index áttekintése tér vissza (a tartalom megtekintéséhez). |
| 查询关键词或问题，如「Python async」「上次读的论文」。留空或省略则返回 Wiki 索引概览。 | Keresés kulcsszó vagy kérdés alapján, pl. „Python async", „a legutóbb olvasott tanulmány". Ha üres vagy elmarad, a Wiki-index áttekintése tér vissza. |

## `apps/inno-agent/src/memory/l2/overview.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| 知识库总览 | Tudásbázis-áttekintés |
| 资料摘要 | Anyagkivonat |
| 实体 | Entitások |
| 概念 | Fogalmak |
| 分析 | Elemzés |
| ## 概况 | ## Áttekintés |
| ## 主题社区 | ## Témaközösség |
| ## 核心节点（按关联度） | ## Központi csomópontok (relevancia szerint) |
| <!-- 暂无足够的双链关联 --> | <!-- Nincs elég kétirányú hivatkozás --> |
| ## 维护建议 | ## Karbantartási javaslatok |

## `apps/inno-agent/src/memory/l2/summarizer.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| \n\n...(内容已截断) | \n\n...(a tartalom csonkolva) |

## `apps/inno-agent/src/memory/l2/wiki-linker.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| \n\n...(内容已截断) | \n\n...(a tartalom csonkolva) |
| 方法 | Módszer |
| 系统 | Rendszer |
| 内容 | Tartalom |
| 条目名 | Szócikk neve |
| 一句话定义或说明 | Egymondatos meghatározás vagy leírás |
| 由 L2 自动从资料摘要中的双链识别，待进一步完善。 | Az L2 automatikusan azonosítja az anyagkivonat kétirányú hivatkozásaiból; további finomításra vár. |
| 由 L2 自动识别，待进一步完善。 | Az L2 automatikusan azonosítja; további finomításra vár. |
| \n## 相关资料 | \n## Kapcsolódó anyagok |
| 是什么 | Mi ez |
| 融合后的完整定义 | Az egyesített teljes meghatározás |
| ## 定义 | ## Meghatározás |
| \n## 争议 | \n## Vita |

## `apps/inno-agent/src/memory/l2/wiki-maintainer.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| ## 资料摘要 (Sources) | ## Anyagkivonat (Sources) |
| ## 实体 (Entities) | ## Entitások (Entities) |
| ## 概念 (Concepts) | ## Fogalmak (Concepts) |
| ## 分析 (Analysis) | ## Elemzés (Analysis) |
| # L2 Wiki 索引 | # L2 Wiki-index |

## `apps/inno-agent/src/memory/l2/wiki-query.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| L2 Wiki 尚未初始化，暂无索引。 | Az L2 Wiki még nincs inicializálva; egyelőre nincs index. |

## `apps/inno-agent/src/memory/l3/l3-tools.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| 回忆历史对话 | Korábbi beszélgetések felidézése |
| 在过往会话记录（L3）中按语义/关键词检索，召回与当前问题相关的历史对话片段。 | Keresés a korábbi munkamenetekben (L3) szemantikus/kulcsszó alapján, és a jelenlegi kérdéshez kapcsolódó történeti beszélgetésrészletek visszakeresése. |
| 当用户提到「上次」「之前聊过」「我们讨论过」「你还记得吗」等指向过去对话的线索， | Akkor hívd, ha a felhasználó utal a korábbi beszélgetésekre („legutóbb", „korábban beszéltünk", „megbeszéltük", „emlékszel rá"), |
| 或你需要跨对话的上下文来连续地帮助用户时调用。结果带相关度，仅返回足够相关的片段。 | vagy ha a folyamatos segítséghez szükséged van a korábbi beszélgetések kontextusára. Az eredmény relevancia-értékkel érkezik; csak a kellően releváns részletek kerülnek visszaadásra. |
| 检索关键词或问题，如「上次说的学习计划」「之前的 Python 报错」。 | Keresés kulcsszó vagy kérdés alapján, pl. „a legutóbb említett tanulási terv", „a korábbi Python-hiba". |
| 最多返回片段数，默认 4。 | A visszaadott részletek maximális száma; alapértelmezés szerint 4. |
| 跨对话历史检索（L3）已在设置中关闭，当前仅使用本工作区与当前对话上下文。 | A munkameneteken átívelő keresés (L3) ki van kapcsolva a beállításokban; jelenleg csak az aktuális munkaterület és beszélgetés kontextusa használatos. |
| 请提供检索关键词或问题。 | Adj meg keresési kulcsszót vagy kérdést. |

## `apps/inno-agent/src/memory/l3/recall.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| # 相关历史对话（来自过往会话，仅供参考） | # Kapcsolódó korábbi beszélgetések (korábbi munkamenetekből, tájékoztatásul) |
| 以下片段来自你与该用户的早期对话，按相关度排序。若与当前问题相关可参考，不相关请忽略： | Az alábbi részletek a felhasználóval folytatott korábbi beszélgetésekből származnak, relevancia szerint rendezve. Ha kapcsolódnak az aktuális kérdéshez, használd őket; ha nem, hagyd figyelmen kívül: |
| 用户 | Felhasználó |
| 你 | Te |

## `apps/inno-agent/src/memory/learner/auto-profile.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| 相关学习目标已归档；除非用户重新提出该方向，否则不再主动安排该概念学习。 | A kapcsolódó tanulási cél archiválva lett; amíg a felhasználó újra nem hozza ezt az irányt, a fogalom tanulása nem kerül aktívan ütemezésre. |
| 避免 | Kerülendő |
| 代码 | Kód |
| 例子 | Példa |
| 示例 | Példák |
| 理论 | Elmélet |
| 小步 | Kis lépések |
| 即时 | Azonnali |
| 反馈 | Visszajelzés |
| 鼓励 | Bátorítás |
| 苏格拉底 | Szókratészi |
| 有学习接触记录，尚未形成稳定掌握度判断。 | Van tanulási érintkezési rekord, de még nem alakult ki stabil elsajátítottsági ítélet. |
| 继续通过讲解、练习或复盘补充证据。 | Folytasd a bizonyítékgyűjtést magyarázattal, gyakorlással vagy visszatekintéssel. |

## `apps/inno-agent/src/memory/learner/context-pack.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| 暂无诊断 | Nincs diagnózis |
| 例子优先 | Példa először |
| 代码优先 | Kód először |
| 理论优先 | Elmélet először |
| 图示优先 | Ábra először |
| 小步练习 | Kis lépéses gyakorlás |
| 即时反馈 | Azonnali visszajelzés |
| 间隔复习 | Térközös ismétlés |
| 直接 | Közvetlen |
| 鼓励性 | Bátorító |
| 苏格拉底式提问 | Szókratészi kérdezés |
| ## 学习者上下文 | ## Tanulói kontextus |
| \n当前目标：暂未设定 | \nAktuális cél: még nincs beállítva |
| \n相关概念： | \nKapcsolódó fogalmak: |
| \n活跃误区： | \nAktív tévhitek: |
| \n教学提示： | \nTanítási tippek: |
| \n到期复习： | \nEsedékes ismétlés: |
| \n最近学习事件： | \nLegutóbbi tanulási események: |

## `apps/inno-agent/src/memory/learner/learner-tools.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| L1 学习者画像已在设置中关闭，当前不读取也不更新学习者画像。 | Az L1 tanulói profil ki van kapcsolva a beállításokban; jelenleg sem olvasás, sem frissítés nem történik. |
| 读取当前学习者上下文包，包含活跃目标、相关概念掌握度、活跃误区和教学提示。在开始新对话或需要了解学习者状态时调用。 | Az aktuális tanulói kontextuscsomag beolvasása: aktív célok, kapcsolódó fogalmak elsajátítottsága, aktív tévhitek és tanítási tippek. Akkor hívd, ha új beszélgetés kezdődik, vagy ha ismerni kell a tanuló állapotát. |
| 记录一个结构化的学习事件，并自动把确定性信号合入 L1 学习者画像。当观察到学习者声明/停止/切换目标、完成练习、接受讲解、自我评估、表达偏好、接收反馈或达到里程碑时调用。 | Strukturált tanulási esemény naplózása, és a határozott jelek automatikus beépítése az L1 tanulói profilba. Akkor hívd, ha a tanuló célt tűz ki/állít le/vált, gyakorlatot végez, magyarázatot fogad el, önértékelést ad, preferenciát fejez ki, visszajelzést kap, vagy mérföldkőhöz ér. |
| Event-specific data. For stopping a goal, include goal_description/action/reason such as { goal_description: '不再学习 Rust', action: 'archived' }. For switching goals, include previous_goal and goal. | Eseményspecifikus adatok. Cél leállításához add meg a goal_description/action/reason értékeket, pl. { goal_description: 'nem tanulok többé Rustot', action: 'archived' }. Célváltáshoz add meg a previous_goal és a goal értékeket. |
| Observed learner preferences, e.g. ['prefers code-first explanations', '避免长篇理论'] | Megfigyelt tanulói preferenciák, pl. ['prefers code-first explanations', 'elkerüli a hosszú elméleti magyarázatokat'] |
| 低成本局部更新 L1 学习者画像。用于在一次学习互动后调整某个概念的掌握度/诊断/复习时间，追加偏好或画像摘要；不需要提交完整知识状态对象。 | Költséghatékony, részleges L1 tanulói profil-frissítés. Egy tanulási interakció után egy fogalom elsajátítottságának/diagnózisának/ismétlési idejének módosítására, preferencia vagy profilkivonat hozzáfűzésére szolgál; nem igényel teljes tudásállapot-objektumot. |
| 更新学习者画像的特定字段。可以更新目标、知识状态、误区、偏好和画像摘要。数组字段按 ID 合并（已存在则替换，不存在则新增）。 | A tanulói profil egyes mezőinek frissítése. Frissíthető a cél, a tudásállapot, a tévhitek, a preferenciák és a profilkivonat. A tömbmezők azonosító alapján egyesülnek (a meglévő felülíródik, az új hozzáadódik). |
| 展示完整的学习者画像，供用户查看、修正或删除。当用户请求查看自己的学习状态时调用。 | A teljes tanulói profil megjelenítése megtekintéshez, javításhoz vagy törléshez. Akkor hívd, ha a felhasználó meg szeretné nézni a tanulási állapotát. |
| 未设定 | Nincs beállítva |
| 暂无摘要 | Nincs kivonat |

## `apps/inno-agent/src/memory/learner/profile-updater.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| 有学习接触记录，尚未形成稳定掌握度判断。 | Van tanulási érintkezési rekord, de még nem alakult ki stabil elsajátítottsági ítélet. |

## `apps/inno-agent/src/scheduler/job-runner.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| 提醒时间到了。 | Itt az emlékeztető ideje. |

## `apps/inno-agent/src/scheduler/scheduler-tools.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| 创建一个定时任务。用户说「每天晚上9点提醒我复习」或「设置一个每周总结」时调用。cron 表达式示例：'0 21 * * *' 表示每天21:00，'0 9 * * 1' 表示每周一9:00。 | Ütemezett feladat létrehozása. Akkor hívd, ha a felhasználó azt mondja: „minden este 9-kor emlékeztess a tanulásra" vagy „állíts be heti összefoglalót". Cron-példa: '0 21 * * *' = minden nap 21:00, '0 9 * * 1' = minden hétfő 9:00. |
| 任务名称 | Feladat neve |
| Cron 表达式，如 '0 21 * * *' | Cron kifejezés, pl. '0 21 * * *' |
| 任务类型 | Feladat típusa |
| 执行时发送给 agent 的提示词 | A feladat futtatásakor az agentnek küldött utasítás |
| 结果推送的频道（可选） | Az eredmény célcsatornája (opcionális) |
| 推送目标的 chat_id（可选） | A cél chat_id (opcionális) |
| 无法计算，请检查 cron 表达式 | Nem számítható; ellenőrizd a cron kifejezést |
| 列出所有定时任务。用户问「我有哪些定时任务」或「查看定时任务」时调用。 | Az összes ütemezett feladat listázása. Akkor hívd, ha a felhasználó megkérdezi: „milyen ütemezett feladataim vannak" vagy „mutasd az ütemezett feladatokat". |
| 当前没有定时任务。 | Jelenleg nincs ütemezett feladat. |
| 启用 | Engedélyezve |
| 禁用 | Letiltva |
| 未运行 | Nem futott |
| 从未 | Soha |
| 未计算 | Nem számított |
| 更新或禁用一个定时任务。可以修改名称、cron、启用状态、提示词等。 | Ütemezett feladat frissítése vagy letiltása. Módosítható a név, a cron, az engedélyezettség és az utasítás. |
| 任务 ID | Feladat azonosító |
| 新名称 | Új név |
| 新 Cron 表达式 | Új cron kifejezés |
| 是否启用 | Engedélyezve van-e |
| 新提示词 | Új utasítás |
| 删除一个定时任务。 | Ütemezett feladat törlése. |
| 要删除的任务 ID | A törlendő feladat azonosítója |
| 立即执行一个定时任务。当用户说「执行那个复习任务」或「现在就运行每日总结」时调用。执行 job 中定义的 prompt 并返回结果。 | Ütemezett feladat azonnali futtatása. Akkor hívd, ha a felhasználó azt mondja: „futtasd azt az ismétlő feladatot" vagy „futtasd most a napi összefoglalót". A feladatban definiált utasítás fut le, és az eredmény visszaadásra kerül. |
| 要执行的任务 ID | A futtatandó feladat azonosítója |
| 当前运行环境没有可用的后台 ChannelRegistry，无法真正执行任务。 | A jelenlegi futási környezetben nincs elérhető háttér-ChannelRegistry, így a feladat ténylegesen nem hajtható végre. |
| 任务「${job.name}」已执行完成。\nRun: ${result.runId}\n${result.pushedToChannel ? `已推送到: ${result.pushedToChannel}\n` : ""}\n输出：\n${result.output ?? ""} | A(z) „${job.name}" feladat végrehajtása kész.\nRun: ${result.runId}\n${result.pushedToChannel ? `Küldve ide: ${result.pushedToChannel}\n` : ""}\nKimenet:\n${result.output ?? ""} |
| 任务「${job.name}」执行失败。\nRun: ${result.runId}\n错误：${result.error} | A(z) „${job.name}" feladat végrehajtása sikertelen.\nRun: ${result.runId}\nHiba: ${result.error} |

## `apps/inno-agent/src/server.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| 未命名对话 | Névtelen beszélgetés |
| <details><summary>💭 思考过程</summary> | <details><summary>💭 Gondolkodási folyamat</summary> |
| **参数：** | **Paraméterek:** |
| **结果：** | **Eredmény:** |
| Inno Agent 飞书主动推送测试。 | Inno Agent Feishu-aktívküldés-teszt. |
| 新目标 | Új cél |
| 成功 | Sikeres |
| 失败 | Sikertelen |
| 未完成 | Befejezetlen |
| ## 元信息 | ## Metaadatok |
| ## 输出 | ## Kimenet |
| (无输出) | (nincs kimenet) |
| ## 备注 | ## Megjegyzések |
| 飞书 | Feishu |

## `apps/inno-agent/src/workspace/workspace-registry.ts`

| Eredeti (kínai) | Magyar |
|---|---|
| 飞书 | Feishu |
| 微信 | WeChat |
| 公共空间 | Közös tér |
| 默认工作区 | Alapértelmezett munkaterület |


---

## Kiegészítés (2. kör + rendszerprompt)

A második körben a template-literal szövegek (backtick-es), a hosszú modell-promptok
(INNO_SYSTEM_PROMPT, ONBOARDING_GUIDE, SUMMARIZE_PROMPT, LINK_MAINTAIN_PROMPT,
STAGE1_PLAN_PROMPT, NARRATIVE_PROMPT) és a további felhasználónak látható üzenetek
is magyarra lettek fordítva (kb. 170 további csere). A részletes párlistát a
`git diff` mutatja; a főbb csoportok:

- dokumentum-feldolgozás (parse_document): fájl/oldalszám/szöveghossz feliratok, hibaüzenetek
- OCR (ocr_image): token-hiány, feladat- és feldolgozási hibák
- internetes keresés (web_search): „## Összegzés", „## Keresési eredmények", hibák
- csatornák (send_file_to_channel): csatorna-kiválasztás, fájlhibák, sikeres küldés
- L2 Wiki: kivonat-, index-, karbantartási és lekérdezési szövegek
- L3 keresés: találat-hiány, paraméterhibák
- tanulói profil (L1): eseményrögzítés, profilfrissítés, profil-megjelenítés feliratai
- ütemezett feladatok: létrehozás/frissítés/törlés/futtatás visszajelzései
- beszélgetés-export (server.ts): exportálás fejlécei és formátuma

### Funkcionális regex-minták (már lefordítva)

A kínai bemenetet kereső regex-minták is magyarra lettek cserélve (commit
7d089cf): a hasArchiveIntent magyar kifejezéseket ismer fel (nem tanul,
abbahagy, felad, leállít, archivál), a „Kerülendő"/„Emlékeztess" prefixek
levágása magyar, a generált címeknél a „Cím:" prefix tisztítása. Az angol
örökölt minták (archive, stop learning, quit) megmaradtak.

- `apps/inno-agent/src/memory/l2/source-converter.ts:40: // 文本已由 LiteParse 在上游提取，此处直接透传`
- `apps/inno-agent/src/memory/l3/sqlite-store.ts:62: * more discriminative than single CJK characters — unigram tokens like 的/我/学`
- `apps/inno-agent/src/memory/learner/auto-profile.ts:46: return /不学|不学习|不再学习|放弃|停止学习|取消.*目标|归档|archive|archived|stop learning|quit/i.test(text);`
- `apps/inno-agent/src/memory/learner/auto-profile.ts:123: return { avoid: [text.replace(/^避免[:：]?\s*/, "")] };`
- `apps/inno-agent/src/scheduler/job-runner.ts:166: .replace(/^提醒学习者[：:]\s*/, "")`
- `apps/inno-agent/src/scheduler/job-runner.ts:167: .replace(/^提醒我[：:]\s*/, "")`
- `apps/inno-agent/src/scheduler/scheduler-tools.ts:96: `- [${j.enabled ? "Engedélyezve" : "Letiltva"}] ${j.name} (${j.id})\n  Cron: ${j.cron} | 类`
- `apps/inno-agent/src/server.ts:878: if (kv[1] in fm) continue; // 保留第一个值（标准YAML行为）`
- `apps/inno-agent/src/server.ts:1964: // Verified on unmodified code: a learner asking "飞书的英文名?" (user text)`
- `apps/inno-agent/src/server.ts:2192: .replace(/^标题[:：]\s*/i, "")`
