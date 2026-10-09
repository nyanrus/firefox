# browser/components/genai/LinkPreviewChild.sys.mjs

source: browser/components/genai/LinkPreviewChild.sys.mjs
source-hash: b81f09eec612421a783e3cb526909e1390e8a148
lines: 427

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## LinkPreviewChild.receiveMessage()
- 位置: async L29-35
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (name === "LinkPreview:FetchPageData")` → `this.fetchPageData()`
- 参照: `data.url`

## LinkPreviewChild.fetchHTML()
- 位置: L44-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.withResolvers()`, `Services.scriptSecurityManager.createNullPrincipal()`, `channel.asyncOpen()`, `channel.setRequestHeader()`, `lazy.NetUtil.newChannel()`, `lazy.NetUtil.newURI()`, `uri.schemeIs()`
- 条件付き依存: `if (!uri.schemeIs("https"))` → `Components.Exception()`
- 参照: `Ci.nsIContentPolicy.TYPE_DOCUMENT`, `Ci.nsIHttpChannel`, `Ci.nsILoadInfo.SEC_ALLOW_CROSS_ORIGIN_INHERITS_SEC_CONTEXT`, `Ci.nsIRequest.LOAD_ANONYMOUS`, `Cr.NS_ERROR_UNKNOWN_PROTOCOL`, `channel.loadFlags`
- XPCOM: [`nsIContentPolicy`](../../../dom/base/nsIContentPolicy.idl.md) / [`nsIHttpChannel`](../../../netwerk/protocol/http/nsIHttpChannel.idl.md) / [`nsILoadInfo`](../../../dom/base/nsIContentPolicy.idl.md) / [`nsIRequest`](../../../docshell/base/nsIDocShell.idl.md) / `Services.scriptSecurityManager`

## onDataAvailable()
- 位置: L76-83
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (totalLength > MAX_CONTENT_LENGTH)` → `request.cancel()`
- 条件付き依存: `if (!(totalLength > MAX_CONTENT_LENGTH))` → `byteChunks.push()`
- 条件付き依存: `if (!(totalLength > MAX_CONTENT_LENGTH))` → `lazy.NetUtil.readInputStream()`
- 参照: `Cr.NS_ERROR_FILE_TOO_BIG`

## onStartRequest()
- 位置: L84-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `contentType.match()`, `contentType.startsWith()`, `http.getResponseHeader()`, `request.QueryInterface()`
- 条件付き依存: `if (contentType && !contentType.startsWith("text/html"))` → `request.cancel()`
- 条件付き依存: `if (http.getResponseHeader("content-length") > MAX_CONTENT_LENGTH)` → `request.cancel()`
- 参照: `Ci.nsIHttpChannel`, `Cr.NS_ERROR_FILE_TOO_BIG`, `Cr.NS_ERROR_FILE_UNKNOWN_TYPE`
- XPCOM: [`nsIHttpChannel`](../../../netwerk/protocol/http/nsIHttpChannel.idl.md)

## onStopRequest()
- 位置: L109-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Components.isSuccessCode()`
- 条件付き依存: `if (Components.isSuccessCode(status))` → `bytes.set()`
- 条件付き依存: `if (Components.isSuccessCode(status))` → `this.sniffCharset()`
- 条件付き依存: `if (Components.isSuccessCode(status))` → `new TextDecoder(effectiveCharset).decode()`
- 条件付き依存: `if (Components.isSuccessCode(status))` → `new TextDecoder("utf-8").decode()`
- 条件付き依存: `if (Components.isSuccessCode(status))` → `resolve()`
- 条件付き依存: `if (!(Components.isSuccessCode(status)))` → `reject()`
- 条件付き依存: `if (!(Components.isSuccessCode(status)))` → `Components.Exception()`
- 参照: `chunk.byteLength`

## LinkPreviewChild.sniffCharset()
- 位置: L147-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `bytes.subarray()`, `head.match()`, `new TextDecoder("windows-1252").decode()`
- 条件付き依存: `if (!match)` → `head.match()`
- 条件付き依存: `if (match && match[1])` → `this.normalizeAndValidateEncodingLabel()`
- 条件付き依存: `if (headerCharset)` → `this.normalizeAndValidateEncodingLabel()`
- 参照: `bytes.length`

## LinkPreviewChild.normalizeAndValidateEncodingLabel()
- 位置: L212-224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(label || "").trim()`
- 参照: `new TextDecoder(l).encoding`

## LinkPreviewChild.fetchPageData()
- 位置: async L232-265
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.NetUtil.newURI()`, `lazy.Readerable.shouldCheckUri()`, `lazy.isProbablyReaderable()`, `parser.parseFromString()`, `this.extractNormalizedMetadata()`, `this.extractUrlComponents()`, `this.fetchHTML()`, `this.getArticleDataFromDoc()`, `this.parseMetaTagsFromDoc()`
- 条件付き依存: `if ( !lazy.Readerable.shouldCheckUri(lazy.NetUtil.newURI(url)) || !lazy.isProbablyReaderable(doc) )` → `this.extractNormalizedMetadata()`
- 参照: `error.message`, `error.result`, `ret.article`, `ret.error`, `ret.meta`, `ret.rawMetaInfo`, `ret.urlComponents`

## LinkPreviewChild.extractNormalizedMetadata()
- 位置: L278-303
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `imageUrl.startsWith()`
- 参照: `articleData.excerpt`, `metaData.description`

## LinkPreviewChild.extractUrlComponents()
- 位置: L311-332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `pathname.endsWith()`, `pathname.split()`
- 条件付き依存: `if (pathname.endsWith("/"))` → `pathname.slice()`
- 参照: `pathParts.length`, `urlObj.hostname`, `urlObj.pathname`

## LinkPreviewChild.parseMetaTagsFromDoc()
- 位置: L341-374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `doc.querySelector()`, `doc.querySelectorAll()`, `metaTags.forEach()`, `rawName.toLowerCase()`, `tag.getAttribute()`
- 条件付き依存: `if (key && content)` → `desiredMetaNames.includes()`
- 参照: `doc.querySelector("title")?.textContent`

## LinkPreviewChild.getArticleDataFromDoc()
- 位置: async L382-425
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.ReaderMode.parseDocument()`
- 条件付き依存: `if (article)` → `Cc["@mozilla.org/parserutils;1"] .getService(Ci.nsIParserUtils) .convertToPlainText()`
- 条件付き依存: `if (article)` → `Cc["@mozilla.org/parserutils;1"] .getService()`
- 参照: `Ci.nsIParserUtils`
- XPCOM: `nsIParserUtils` / `@mozilla.org/parserutils;1`
