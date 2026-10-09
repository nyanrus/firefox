# browser/actors/PageInfoChild.sys.mjs

source: browser/actors/PageInfoChild.sys.mjs
source-hash: 18060c54d7b89a00da3cc072b858c77ea281acb5
lines: 399

## <module>
- 役割: ページ情報ダイアログのために、ページのメタ情報・文書情報・メディア(画像や動画など)を集めて親へ返す子側アクター。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## PageInfoChild.receiveMessage()
- 位置: async L14-41
- 役割: getData、getMediaData、getPartitionKey の要求に応じて、必要な情報を集めて返す。
- 触るとき: ページ情報の要求の種類を増やすとき。
- 呼び出し先: `Promise.resolve()`, `this.getDocumentInfo()`, `this.getDocumentMedia()`, `this.getMetaInfo()`, `this.getPartitionKey()`, `this.getWindowInfo()`
- 参照: `message.name`, `this.contentWindow`, `window.document`

## PageInfoChild.getPartitionKey()
- 位置: L43-46
- 役割: 文書の Cookie の partitionKey を返す。
- 触るとき: パーティションキーの取得を変えるとき。
- 参照: `document.cookieJarSettings.partitionKey`

## PageInfoChild.getMetaInfo()
- 位置: L48-64
- 役割: meta 要素の名前、http-equiv、property のいずれかと内容の組の一覧を作る。
- 触るとき: メタ情報の表示内容を変えるとき。
- 呼び出し先: `document.getElementsByTagName()`, `metaNode.getAttribute()`, `metaViewRows.push()`
- 参照: `metaNode.content`, `metaNode.httpEquiv`, `metaNode.name`

## PageInfoChild.getWindowInfo()
- 位置: L66-77
- 役割: 最上位のウィンドウかどうかと、表示用のホスト名を返す。
- 触るとき: ウィンドウ情報の項目を変えるとき。
- 呼び出し先: `Services.io.newURI()`
- 参照: `Services.io.newURI(window.location.href).displayHost`, `window.location.href`, `window.top`, `windowInfo.hostName`, `windowInfo.isTopWindow`
- XPCOM: `Services.io`

## PageInfoChild.getDocumentInfo()
- 位置: L79-111
- 役割: タイトル、URL、リファラー(表示用に変換)、文字コード、更新日時、プリンシパル、Cookie 設定などをまとめる。
- 触るとき: 文書の基本情報の項目や形式を変えるとき。
- 呼び出し先: `Services.io.newURI()`, `document.location.toString()`, `lazy.E10SUtils.serializeCookieJarSettings()`, `lazy.PrivateBrowsingUtils.isContentWindowPrivate()`
- 条件付き依存: `if (document.referrer)` → `Services.io.newURI()`
- 参照: `Services.io.newURI( document.location.toString() ).displaySpec`, `Services.io.newURI(document.referrer).displaySpec`, `docInfo.characterSet`, `docInfo.compatMode`, `docInfo.contentType`, `docInfo.cookieJarSettings`, `docInfo.documentURIObject`, `docInfo.isContentWindowPrivate`, `docInfo.lastModified`, `docInfo.location`, `docInfo.principal`, `docInfo.referrer`, `docInfo.title`, `document.characterSet`, `document.compatMode`, `document.contentType`, `document.cookieJarSettings`, `document.documentGlobal`, `document.documentURIObject.spec`, `document.lastModified`, `document.nodePrincipal`, `document.referrer`, `document.title`, `documentURIObject.spec`
- XPCOM: `Services.io`

## PageInfoChild.getDocumentMedia()
- 位置: async L118-139
- 役割: 文書内の要素を順に走査して getMediaItems で画像などを集める。500 要素ごとに 10 ms 譲って処理を止めすぎないようにする。
- 触るとき: メディア一覧の収集範囲や性能を変えるとき。
- 呼び出し先: `document.createTreeWalker()`, `iterator.nextNode()`, `this.getMediaItems()`, `totalMediaItems.push()`
- 条件付き依存: `if (++nodeCount % 500 == 0)` → `lazy.setTimeout()`
- 参照: `content.NodeFilter.SHOW_ELEMENT`, `document.documentGlobal`, `iterator.currentNode`

## PageInfoChild.getMediaItems()
- 位置: L141-229
- 役割: 1 つの要素から、CSS の背景や枠の画像、img、SVG、動画、音声、アイコン link、画像ボタン、object、embed を取り出す。
- 触るとき: メディアとして拾う要素の種類を増やすとき。
- 呼び出し先: `content.HTMLImageElement.isInstance()`, `elem.documentGlobal.getComputedStyle()`
- 条件付き依存: `if (computedStyle)` → `addImgFunc()`
- 条件付き依存: `if (computedStyle)` → `computedStyle.getCSSImageURLs()`
- 条件付き依存: `if (content.HTMLImageElement.isInstance(elem))` → `addMedia()`
- 条件付き依存: `if (content.HTMLImageElement.isInstance(elem))` → `elem.getAttribute()`
- 条件付き依存: `if (content.HTMLImageElement.isInstance(elem))` → `elem.hasAttribute()`
- 条件付き依存: `if (!(content.HTMLImageElement.isInstance(elem)))` → `content.SVGImageElement.isInstance()`
- 条件付き依存: `if (elem.href.baseVal)` → `URL.parse()`
- 条件付き依存: `if (href)` → `addMedia()`
- 条件付き依存: `if (!(content.SVGImageElement.isInstance(elem)))` → `content.HTMLVideoElement.isInstance()`
- 条件付き依存: `if (content.HTMLVideoElement.isInstance(elem))` → `addMedia()`
- 条件付き依存: `if (!(content.HTMLVideoElement.isInstance(elem)))` → `content.HTMLAudioElement.isInstance()`
- 条件付き依存: `if (content.HTMLAudioElement.isInstance(elem))` → `addMedia()`
- 条件付き依存: `if (!(content.HTMLAudioElement.isInstance(elem)))` → `content.HTMLLinkElement.isInstance()`
- 条件付き依存: `if (content.HTMLLinkElement.isInstance(elem))` → `/\bicon\b/i.test()`
- 条件付き依存: `if (elem.rel && /\bicon\b/i.test(elem.rel))` → `addMedia()`
- 条件付き依存: `if (!(content.HTMLLinkElement.isInstance(elem)))` → `content.HTMLInputElement.isInstance()`
- 条件付き依存: `if (!(content.HTMLLinkElement.isInstance(elem)))` → `content.HTMLButtonElement.isInstance()`
- 条件付き依存: `if ( content.HTMLInputElement.isInstance(elem) || content.HTMLButtonElement.isInstance(elem) )` → `elem.type.toLowerCase()`
- 条件付き依存: `if (elem.type.toLowerCase() == "image")` → `addMedia()`
- 条件付き依存: `if (elem.type.toLowerCase() == "image")` → `elem.getAttribute()`
- 条件付き依存: `if (elem.type.toLowerCase() == "image")` → `elem.hasAttribute()`
- 条件付き依存: `if (!( content.HTMLInputElement.isInstance(elem) || content.HTMLButtonElement.isInstance(elem) ))` → `content.HTMLObjectElement.isInstance()`
- 条件付き依存: `if (content.HTMLObjectElement.isInstance(elem))` → `addMedia()`
- 条件付き依存: `if (content.HTMLObjectElement.isInstance(elem))` → `this.getValueText()`
- 条件付き依存: `if (!(content.HTMLObjectElement.isInstance(elem)))` → `content.HTMLEmbedElement.isInstance()`
- 条件付き依存: `if (content.HTMLEmbedElement.isInstance(elem))` → `addMedia()`
- 参照: `URL.parse(elem.href.baseVal, elem.baseURI)?.href`, `document.documentGlobal`, `elem.baseURI`, `elem.currentSrc`, `elem.data`, `elem.href`, `elem.href.baseVal`, `elem.rel`, `elem.src`

## addMedia()
- 位置: L149-159
- 役割: URL、種類、代替テキスト、要素の情報を 1 件のメディア項目にまとめて追加する。
- 触るとき: メディア項目の形を変えるとき。
- 呼び出し先: `mediaItems.push()`, `this.serializeElementInfo()`

## addImgFunc()
- 位置: L162-166
- 役割: CSS の画像 URL の一覧を、bg-img などの種類を付けて 1 件ずつ追加する。
- 触るとき: CSS 由来の画像の分類を変えるとき。
- 呼び出し先: `addMedia()`

## PageInfoChild.serializeElementInfo()
- 位置: L236-329
- 役割: 要素の種類、代替テキスト、MIME 型、フレーム数、寸法をプレビュー用のオブジェクトにまとめる。背景画像は新しい img を作って自然サイズを取る。
- 触るとき: プレビューに渡す項目を変えるとき。
- 呼び出し先: `content.HTMLAudioElement.isInstance()`, `content.HTMLEmbedElement.isInstance()`, `content.HTMLImageElement.isInstance()`, `content.HTMLInputElement.isInstance()`, `content.HTMLLinkElement.isInstance()`, `content.HTMLObjectElement.isInstance()`, `content.HTMLVideoElement.isInstance()`, `content.ImageDocument.isInstance()`, `content.SVGImageElement.isInstance()`, `url.startsWith()`
- 条件付き依存: `if ( !isBG && !content.SVGImageElement.isInstance(item) && !content.ImageDocument.isInstance(document) )` → `content.HTMLImageElement.isInstance()`
- 条件付き依存: `if (!imageText && !content.HTMLImageElement.isInstance(item))` → `this.getValueText()`
- 条件付き依存: `if ( !result.mimeType && !isBG && item instanceof Ci.nsIImageLoadingContent )` → `item.getRequest()`
- 条件付き依存: `if (!result.mimeType && url.startsWith("data:"))` → `/^data:(image\/[^;,]+)/i.exec()`
- 条件付き依存: `if (dataMimeType)` → `dataMimeType[1].toLowerCase()`
- 条件付き依存: `if (isBG)` → `content.document.createElement()`
- 条件付き依存: `if (!(isBG))` → `content.SVGImageElement.isInstance()`
- 参照: `Ci.nsIImageLoadingContent`, `Ci.nsIImageLoadingContent.CURRENT_REQUEST`, `document.documentGlobal`, `image.numFrames`, `imageRequest.STATUS_ERROR`, `imageRequest.image`, `imageRequest.imageStatus`, `imageRequest.mimeType`, `img.naturalHeight`, `img.naturalWidth`, `img.src`, `item.alt`, `item.baseURI`, `item.height`, `item.height.baseVal.value`, `item.longDesc`, `item.title`, `item.type`, `item.width`, `item.width.baseVal.value`, `result.HTMLAudioElement`, `result.HTMLImageElement`, `result.HTMLInputElement`, `result.HTMLLinkElement`, `result.HTMLObjectElement`, `result.HTMLVideoElement`, `result.SVGImageElement`, `result.SVGImageElementHeight`, `result.SVGImageElementWidth`, `result.baseURI`, `result.height`, `result.imageText`, `result.longDesc`, `result.mimeType`, `result.naturalHeight`, `result.naturalWidth`, `result.numFrames`, `result.width`
- XPCOM: [`nsIImageLoadingContent`](../../dom/base/nsIImageLoadingContent.idl.md)

## PageInfoChild.getValueText()
- 位置: L334-369
- 役割: 要素の子のテキストを再帰的に連結して整形する。画像は alt を使い、入力欄や選択欄は除外する。
- 触るとき: object などの表示テキストの取り方を変えるとき。
- 呼び出し先: `content.HTMLInputElement.isInstance()`, `content.HTMLSelectElement.isInstance()`, `content.HTMLTextAreaElement.isInstance()`, `this.stripWS()`
- 条件付き依存: `if (nodeType == content.Node.ELEMENT_NODE)` → `content.HTMLImageElement.isInstance()`
- 条件付き依存: `if (content.HTMLImageElement.isInstance(childNode))` → `this.getAltText()`
- 条件付き依存: `if (!(content.HTMLImageElement.isInstance(childNode)))` → `this.getValueText()`
- 参照: `childNode.nodeType`, `childNode.nodeValue`, `content.Node.ELEMENT_NODE`, `content.Node.TEXT_NODE`, `node.childNodes`, `node.childNodes.length`, `node.documentGlobal`

## PageInfoChild.getAltText()
- 位置: L373-387
- 役割: 要素の alt を返し、無ければ子をたどって探す。 ソースの不具合の疑い: 代入と比較の括弧の位置により、子を持つ要素では alt ではなく真偽値 true が返る。
- 触るとき: 代替テキストが取れない、または値がおかしい不具合を調べるとき。
- 呼び出し先: `this.getAltText()`
- 参照: `node.alt`, `node.childNodes`, `node.childNodes.length`

## PageInfoChild.stripWS()
- 位置: L391-397
- 役割: 連続する空白を 1 つにまとめ、前後の空白を取り除く。
- 触るとき: 抽出テキストの整形を変えるとき。
- 呼び出し先: `text.replace()`
