# nsIInputStreamChannel (netwerk/base/nsIInputStreamChannel.idl)

source: netwerk/base/nsIInputStreamChannel.idl
source-hash: 9172a2b283e635ccdee5b4f3c55783528445dcce

- 継承: nsISupports
- 役割: nsIInputStreamChannel
- 実装: (未記入)
- 使っているJS: [`browser/components/backup/BackupService.sys.mjs`](../../browser/components/backup/BackupService.sys.mjs.md), [`browser/components/newtab/AboutNewTabRedirector.sys.mjs`](../../browser/components/newtab/AboutNewTabRedirector.sys.mjs.md), [`browser/components/newtab/MozNewTabRemoteRendererProtocolHandler.sys.mjs`](../../browser/components/newtab/MozNewTabRemoteRendererProtocolHandler.sys.mjs.md)

## メソッド / 属性
- `void setURI(nsIURI aURI)`: Sets the URI for this channel.  This must be called before the
- `attribute nsIInputStream contentStream`: Get/set the content stream
- `attribute AString srcdocData`: Get/set the srcdoc data string.  When the input stream channel is
- `readonly attribute boolean isSrcdocChannel`: Returns true if srcdocData has been set within the channel.
- `attribute nsIURI baseURI`: The base URI to be used for the channel.  Used when the base URI cannot
