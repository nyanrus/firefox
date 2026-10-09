# browser/extensions/newtab/content-src/lib/screenshot-utils.mjs

source: browser/extensions/newtab/content-src/lib/screenshot-utils.mjs
source-hash: 2d1342be4f7cea963f107d592c95661effdffd2f
lines: 62

## <module>
- 役割: (未記入)

## isBlob()
- 位置: L18-24
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `image.data`, `image.path`, `image.url`

## createLocalImageObject()
- 位置: L27-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isBlob()`
- 条件付き依存: `if (this.isBlob(false, remoteImage))` → `globalThis.URL.createObjectURL()`
- 参照: `remoteImage.data`, `remoteImage.path`

## maybeRevokeBlobObjectURL()
- 位置: L42-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isBlob()`
- 条件付き依存: `if (this.isBlob(true, localImage))` → `globalThis.URL.revokeObjectURL()`
- 参照: `localImage.url`

## isRemoteImageLocal()
- 位置: L49-60
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (remoteImage && localImage)` → `this.isBlob()`
- 参照: `localImage.path`, `localImage.url`, `remoteImage.path`
