# browser/components/genai/PageAssistChild.sys.mjs

source: browser/components/genai/PageAssistChild.sys.mjs
source-hash: 5b4d83d383cf3d6b5b9ef0aec6c34665c71a9083
lines: 70

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## PageAssistChild.receiveMessage()
- 位置: async L15-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getPageData()`
- 参照: `message.name`

## PageAssistChild.getPageData()
- 位置: async L37-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.ReaderMode.parseDocument()`, `lazy.Readerable.isProbablyReaderable()`, `lazy.Readerable.shouldCheckUri()`
- 参照: `article?.content`, `article?.excerpt`, `article?.textContent`, `article?.title`, `doc.body?.innerText`, `doc.documentURIObject`, `doc.title`, `this.contentWindow.document`, `this.contentWindow.location.href`
