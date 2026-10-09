# browser/components/aiwindow/ui/modules/UrlTokenizer.sys.mjs

source: browser/components/aiwindow/ui/modules/UrlTokenizer.sys.mjs
source-hash: 09b1c3437aa6203470878283bb541be8c39e5ab1
lines: 227

## <module>
- 役割: LLM へ送る URL を §url_token§ 形式の短いトークンに置き換え、応答から元の URL に戻す仕組み。

## UrlTokenizer.constructor()
- 位置: L64-67
- 役割: URL からトークン、トークンから URL への双方向マップを空で初期化する。
- 触るとき: トークンの保持構造を変えるとき、または新しいトークナイザを作る箇所で初期状態を調べるとき。
- 参照: `this.tokenToUrl`, `this.urlToToken`

## UrlTokenizer.encodeToken()
- 位置: L81-139
- 役割: URL からホスト名とパスを連結した基底トークンを作り、同じ基底の出現回数を付けて一意にする。
- 触るとき: トークン名の形式(ホスト名の変換、長さ上限 100 字など)を変えるとき、またはトークン名が衝突すると疑われるとき。
- 呼び出し先: `URL.parse()`, `this.#baseTokenCounts.get()`, `this.#baseTokenCounts.set()`, `this.tokenToUrl.set()`, `this.urlToToken.get()`, `this.urlToToken.set()`
- 条件付き依存: `if (parsedUrl.protocol !== "http:" && parsedUrl.protocol !== "https:")` → `parsedUrl.protocol.toUpperCase().replace()`
- 条件付き依存: `if (parsedUrl.protocol !== "http:" && parsedUrl.protocol !== "https:")` → `parsedUrl.protocol.toUpperCase()`
- 条件付き依存: `if (parsedUrl)` → `parsedUrl.hostname .replace(/^www\./, "") .toUpperCase() .replace(/[.\-]/g, "_") .substring()`
- 条件付き依存: `if (parsedUrl)` → `parsedUrl.hostname .replace(/^www\./, "") .toUpperCase() .replace()`
- 条件付き依存: `if (parsedUrl)` → `parsedUrl.hostname .replace(/^www\./, "") .toUpperCase()`
- 条件付き依存: `if (parsedUrl)` → `parsedUrl.hostname .replace()`
- 条件付き依存: `if (parsedUrl)` → `parsedUrl.pathname.split()`
- 条件付き依存: `if (parsedUrl)` → `part.toUpperCase().replace()`
- 条件付き依存: `if (parsedUrl)` → `part.toUpperCase()`
- 参照: `nextToken.length`, `parsedUrl.protocol`

## UrlTokenizer.formatToken()
- 位置: L147-149
- 役割: encodeToken の結果を §url_token: …§ の区切りで包んだ文字列を返す。
- 触るとき: モデルに見せるトークンの区切り記号を変えるとき。
- 呼び出し先: `this.encodeToken()`

## UrlTokenizer.tokenizeText()
- 位置: L159-184
- 役割: テキスト中の http(s) URL を末尾の句読点を除いて正規表現で拾い、トークンに置換する。解析できない URL はスキームを落とす。
- 触るとき: モデル出力に生の URL が残る、または文末の句読点が URL に含まれてしまうといった問題を調べるとき。
- 呼び出し先: `URL.parse()`, `match.indexOf()`, `match.replace()`, `match.slice()`, `text.replace()`, `this.formatToken()`, `url.split()`
- 参照: `url.length`, `url.split("(").length`, `url.split(")").length`

## UrlTokenizer.resolveExactToken()
- 位置: L194-200
- 役割: 値全体がちょうど一つの既知トークンである場合だけ元の URL を返し、それ以外は null を返す。
- 触るとき: 構造化出力のリンク先を解決する処理で、モデルが作った偽のトークンを弾く挙動を変えるとき。
- 呼び出し先: `this.tokenToUrl.get()`, `value.trim()`, `value.trim().match()`

## expandUrlTokens()
- 位置: L211-215
- 役割: テキスト中のトークンを tokenToUrl のマップで元の URL に展開し、未知のトークンはそのまま残す。
- 触るとき: ツール呼び出しや表示の前にトークンを展開する箇所で、展開されない URL があると調べるとき。
- 呼び出し先: `text.replace()`, `tokenToUrl.get()`

## stripUnresolvedUrlTokens()
- 位置: L224-226
- 役割: 展開後に残ったトークンを空文字に置換して取り除く。
- 触るとき: 最終表示にトークンの残骸が出る問題を直すとき、または削除の対象範囲を変えるとき。
- 呼び出し先: `text.replace()`
