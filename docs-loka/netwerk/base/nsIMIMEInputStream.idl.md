# nsIMIMEInputStream (netwerk/base/nsIMIMEInputStream.idl)

source: netwerk/base/nsIMIMEInputStream.idl
source-hash: 060554c7c09f852f050485f38bd25f2a43e484f4

- 継承: nsIInputStream
- 役割: The MIME stream separates headers and a datastream. It also allows
- 実装: (未記入)
- 使っているJS: [`browser/components/urlbar/UrlbarUtils.sys.mjs`](../../browser/components/urlbar/UrlbarUtils.sys.mjs.md)

## メソッド / 属性
- `void addHeader(string name, string value)`: Adds an additional header to the stream on the form "name: value". May
- `void visitHeaders(nsIHttpHeaderVisitor visitor)`: Visits all headers which have been added via addHeader.  Calling
- `void setData(nsIInputStream stream)`: Sets data-stream. May not be called once the stream has been started
- `readonly attribute nsIInputStream data`: Get the wrapped data stream
