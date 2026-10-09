# browser/components/aiwindow/models/TokenStreamParser.sys.mjs

source: browser/components/aiwindow/models/TokenStreamParser.sys.mjs
source-hash: d9112ddf5507571fe3ecbf3b526758e4d5454b4e
lines: 316

## <module>
- 役割: モデルのストリーム出力から §search:§ や §url_token:§ などの印を切り出し、URL トークンを実 URL に戻す、ストリーム逐次処理のパーサーを定義する。
- 呼び出し先: `ALLOWED_TOKEN_STARTS.map()`, `Math.max()`

## encodeForLink()
- 位置: L35-37
- 役割: 文字 1 つを、丸括弧だけ %28 %29 に、それ以外は encodeURIComponent で変換する。
- 触るとき: markdown リンクの URL を壊す文字の扱いを変えるとき。
- 呼び出し先: `encodeURIComponent()`

## isAllowedPrefix()
- 位置: L39-41
- 役割: 文字列が許可された印の先頭のいずれかの接頭辞かを判定する。
- 触るとき: 新しい印の種類を追加して、§ の後の判定が通るか確かめるとき。
- 呼び出し先: `ALLOWED_TOKEN_STARTS.some()`, `start.startsWith()`

## isExactAllowedStart()
- 位置: L43-45
- 役割: 文字列が許可された印の開始語と完全一致するかを判定し、一致すれば候補を確定させる。
- 触るとき: 印の確定条件を変えるとき。
- 呼び出し先: `ALLOWED_TOKEN_STARTS.includes()`

## pushPlain()
- 位置: L47-52
- 役割: 平文の断片を出力配列に積み、直近の平文の末尾を URL 文脈用に 16 文字だけ保持する。
- 触るとき: 直近の平文の保持長や、印として確定しなかった文字の扱いを変えるとき。
- 呼び出し先: `(state.recentPlain + str).slice()`, `plain.push()`
- 参照: `state.recentPlain`

## hasUnbalancedParens()
- 位置: L54-67
- 役割: URL の丸括弧の対応が崩れていれば true を返す。
- 触るとき: markdown リンクに入れる URL の括弧の扱いを調べるとき。

## expandUrlToken()
- 位置: L93-102
- 役割: url_token を実 URL に展開する。直前が markdown リンクの「](」なら括弧などを必要分だけ encode して直接入れ、そうでなければ <URL> で囲む。
- 触るとき: URL トークンが表示でリンクにならない、またはリンクの括弧が壊れるとき。
- 呼び出し先: `AT_MARKDOWN_LINK_URL_RE.test()`, `url.replace()`
- 条件付き依存: `if (isMarkdownLink)` → `hasUnbalancedParens()`
- 条件付き依存: `if (isMarkdownLink)` → `url.replace()`

## createParserState()
- 位置: L115-130
- 役割: パーサーの状態(印の途中か、候補か、保留中の §、直近の平文)の初期値を作る。
- 触るとき: パーサーの状態項目を増やすとき。

## parseToken()
- 位置: L138-158
- 役割: § の間の文字列を最初のコロンで key と value に分け、key が空や区切り無しなら null を返す。
- 触るとき: 印の書式(key:value の形)を変えるとき。
- 呼び出し先: `String()`, `String(raw ?? "").trim()`, `text.indexOf()`, `text.slice()`, `text.slice(0, colonIndex).trim()`, `text.slice(colonIndex + 1).trim()`

## consumeStreamChunk()
- 位置: L181-285
- 役割: チャンクを 1 文字ずつ読み、§ で始まる許可された印を検出して tokens に積み、url_token は tokenToUrl で URL に戻す。確定しない印は文字として出力し、チャンク末尾の § は次のチャンクまで保留する。
- 触るとき: ストリーム中に印をどう扱うか(保留、確定、文字扱い)を変えるとき。印が途中で消えたり漏れたりする問題を調べるとき。
- 呼び出し先: `String()`, `plain.join()`
- 条件付き依存: `if (!state.inToken)` → `pushPlain()`
- 条件付き依存: `if (!isTokenChar)` → `isAllowedPrefix()`
- 条件付き依存: `if ( state.tokenBuffer.length > MAX_START_LEN || !isAllowedPrefix(state.tokenBuffer) )` → `pushPlain()`
- 条件付き依存: `if (!isTokenChar)` → `isExactAllowedStart()`
- 条件付き依存: `if (state.tokenCandidate)` → `pushPlain()`
- 条件付き依存: `if (!(state.tokenCandidate))` → `parseToken()`
- 条件付き依存: `if (parsed?.key == "url_token")` → `tokenToUrl.get()`
- 条件付き依存: `if (url)` → `pushPlain()`
- 条件付き依存: `if (url)` → `expandUrlToken()`
- 条件付き依存: `if (parsed)` → `tokens.push()`
- 参照: `chunkString.length`, `parsed.value`, `parsed?.key`, `state.inToken`, `state.pendingOpen`, `state.recentPlain`, `state.tokenBuffer`, `state.tokenBuffer.length`, `state.tokenCandidate`

## flushTokenRemainder()
- 位置: L299-315
- 役割: ストリーム終了時に、保留中の § や閉じられなかった印の残りを文字として返し、状態を初期化する。
- 触るとき: 応答の末尾で印の残骸が消える・残る問題を調べるとき。
- 参照: `state.inToken`, `state.pendingOpen`, `state.tokenBuffer`, `state.tokenCandidate`
