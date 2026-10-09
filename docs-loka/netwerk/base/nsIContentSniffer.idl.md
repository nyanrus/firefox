# nsIContentSniffer (netwerk/base/nsIContentSniffer.idl)

source: netwerk/base/nsIContentSniffer.idl
source-hash: f9052b8e606b8c9f9b9cb7ab211e321d93d965f0

- 継承: nsISupports
- 役割: Content sniffer interface. Components implementing this interface can
- 実装: (未記入)
- 使っているJS: [`browser/components/migration/MigrationUtils.sys.mjs`](../../browser/components/migration/MigrationUtils.sys.mjs.md), [`browser/modules/FaviconLoader.sys.mjs`](../../browser/modules/FaviconLoader.sys.mjs.md)

## メソッド / 属性
- `ACString getMIMETypeFromContent(nsIRequest aRequest, octet aData, unsigned long aLength)`: Given a chunk of data, determines a MIME type. Information from the given
