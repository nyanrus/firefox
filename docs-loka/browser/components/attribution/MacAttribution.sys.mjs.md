# browser/components/attribution/MacAttribution.sys.mjs

source: browser/components/attribution/MacAttribution.sys.mjs
source-hash: 09ec083a44a9761c5deee8995c48419701406d9f
lines: 50

## <module>
- 役割: (未記入)

## applicationPath()
- 位置: L12-15
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.dirsvc.get()`
- 参照: `Ci.nsIFile`, `Services.dirsvc.get("GreD", Ci.nsIFile).parent.parent.path`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `Services.dirsvc`

## setAttributionString()
- 位置: async L17-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.setMacXAttr()`, `new TextEncoder().encode()`
- 参照: `this.applicationPath`

## getAttributionString()
- 位置: async L25-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.getMacXAttr()`, `attrStr.startsWith()`, `bytes.filter()`, `new TextDecoder().decode()`, `promise.then()`
- 条件付き依存: `if (attrStr.startsWith("__MOZCUSTOM__"))` → `attrStr.slice()`
- 参照: `this.applicationPath`

## delAttributionString()
- 位置: async L46-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.delMacXAttr()`
- 参照: `this.applicationPath`
