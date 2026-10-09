# nsIPipe (xpcom/io/nsIPipe.idl)

source: xpcom/io/nsIPipe.idl
source-hash: cf9d4562fb4c22860c992009d91e8b86e269e572

- 継承: nsISupports
- 役割: nsIPipe represents an in-process buffer that can be read using nsIInputStream
- 実装: (未記入)
- 使っているJS: [`browser/components/mozcachedohttp/MozCachedOHTTPProtocolHandler.sys.mjs`](../../browser/components/mozcachedohttp/MozCachedOHTTPProtocolHandler.sys.mjs.md), [`browser/components/newtab/AboutHomeStartupCache.sys.mjs`](../../browser/components/newtab/AboutHomeStartupCache.sys.mjs.md)

## メソッド / 属性
- `void init(boolean nonBlockingInput, boolean nonBlockingOutput, unsigned long segmentSize, unsigned long segmentCount)`: initialize this pipe
- `readonly attribute nsIAsyncInputStream inputStream`: The pipe's input end. Getting fails if the pipe hasn't been
- `readonly attribute nsIAsyncOutputStream outputStream`: The pipe's output end. Getting fails if the pipe hasn't been
