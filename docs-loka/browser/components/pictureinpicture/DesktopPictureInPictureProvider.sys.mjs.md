# browser/components/pictureinpicture/DesktopPictureInPictureProvider.sys.mjs

source: browser/components/pictureinpicture/DesktopPictureInPictureProvider.sys.mjs
source-hash: f5c74fa65e1aed29c49fe626464c8d1eeba3d678
lines: 112

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`

## PictureInPictureFunctionsImpl.#getActor()
- 位置: L24-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `windowGlobalChild.getActor()`
- 条件付き依存: `if (!videoElement)` → `Components.Exception()`
- 条件付き依存: `if (!windowGlobalChild)` → `Components.Exception()`
- 条件付き依存: `if (!actor)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_FAILURE`, `Cr.NS_ERROR_INVALID_ARG`, `docShell.domWindow.windowGlobalChild`, `videoElement.documentGlobal.docShell`

## PictureInPictureFunctionsImpl.openMediaPictureInPictureWindow()
- 位置: async L53-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.togglePictureInPicture()`, `this.#getActor()`
- 条件付き依存: `if (!pictureInPictureWindow)` → `Components.Exception()`
- 条件付き依存: `if (!videoElement.isCloningElementVisually)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_INVALID_ARG`, `videoElement.isCloningElementVisually`

## PictureInPictureFunctionsImpl.closeMediaPictureInPictureWindow()
- 位置: L85-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actor.closePictureInPicture()`, `getActorFor()`
- 条件付き依存: `if (!videoElement)` → `Components.Exception()`
- 条件付き依存: `if (!videoElement.isCloningElementVisually)` → `Promise.resolve()`
- 条件付き依存: `if (!actor)` → `Components.Exception()`
- 参照: `Cr.NS_ERROR_FAILURE`, `Cr.NS_ERROR_INVALID_ARG`, `videoElement.isCloningElementVisually`

## PictureInPictureProvider()
- 位置: L109-111
- 役割: (未記入)
- 触るとき: (未記入)
