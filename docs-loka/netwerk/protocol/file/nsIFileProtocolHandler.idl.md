# nsIFileProtocolHandler (netwerk/protocol/file/nsIFileProtocolHandler.idl)

source: netwerk/protocol/file/nsIFileProtocolHandler.idl
source-hash: 1fdc49696c522b94d2c0446e2e7e8aa251596ff3

- 継承: nsIProtocolHandler
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/migration/MSMigrationUtils.sys.mjs`](../../../browser/components/migration/MSMigrationUtils.sys.mjs.md), [`browser/components/preferences/config/downloads.mjs`](../../../browser/components/preferences/config/downloads.mjs.md)

## メソッド / 属性
- `nsIURI newFileURI(nsIFile aFile)`: This method constructs a new file URI
- `nsIURIMutator newFileURIMutator(nsIFile file)`: This method constructs a new file URI, and returns a URI mutator
- `AUTF8String getURLSpecFromFile(nsIFile file)`: DEPRECATED, AVOID IF AT ALL POSSIBLE.
- `AUTF8String getURLSpecFromActualFile(nsIFile file)`: Converts a non-directory nsIFile to the corresponding URL string.
- `AUTF8String getURLSpecFromDir(nsIFile file)`: Converts a directory nsIFile to the corresponding URL string.
- `nsIFile getFileFromURLSpec(AUTF8String url)`: Converts the URL string into the corresponding nsIFile if possible.
- `nsIURI readURLFile(nsIFile file)`: Takes a local file and tries to interpret it as an internet shortcut
- `nsIURI readShellLink(nsIFile file)`: Takes a local file and tries to interpret it as a shell link file
