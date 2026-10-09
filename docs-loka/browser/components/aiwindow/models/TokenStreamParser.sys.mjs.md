# browser/components/aiwindow/models/TokenStreamParser.sys.mjs

source: browser/components/aiwindow/models/TokenStreamParser.sys.mjs
source-hash: d9112ddf5507571fe3ecbf3b526758e4d5454b4e
lines: 316

## <module>
- 役割: (未記入)
- 呼び出し先: `ALLOWED_TOKEN_STARTS.map()`, `Math.max()`

## encodeForLink()
- 位置: L35-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `encodeURIComponent()`

## isAllowedPrefix()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ALLOWED_TOKEN_STARTS.some()`, `start.startsWith()`

## isExactAllowedStart()
- 位置: L43-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ALLOWED_TOKEN_STARTS.includes()`

## pushPlain()
- 位置: L47-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(state.recentPlain + str).slice()`, `plain.push()`
- 参照: `state.recentPlain`

## hasUnbalancedParens()
- 位置: L54-67
- 役割: (未記入)
- 触るとき: (未記入)

## expandUrlToken()
- 位置: L93-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AT_MARKDOWN_LINK_URL_RE.test()`, `url.replace()`
- 条件付き依存: `if (isMarkdownLink)` → `hasUnbalancedParens()`
- 条件付き依存: `if (isMarkdownLink)` → `url.replace()`

## createParserState()
- 位置: L115-130
- 役割: (未記入)
- 触るとき: (未記入)

## parseToken()
- 位置: L138-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `String(raw ?? "").trim()`, `text.indexOf()`, `text.slice()`, `text.slice(0, colonIndex).trim()`, `text.slice(colonIndex + 1).trim()`

## consumeStreamChunk()
- 位置: L181-285
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `state.inToken`, `state.pendingOpen`, `state.tokenBuffer`, `state.tokenCandidate`
