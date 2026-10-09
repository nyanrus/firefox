# browser/extensions/pictureinpicture/video-wrappers/videojsWrapper.js

source: browser/extensions/pictureinpicture/video-wrappers/videojsWrapper.js
source-hash: ceb9de4395073bcecf73d0cadccc78d8fec811c1
lines: 38

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L9-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L14-18
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `updateCaptionsFunction()`
- 参照: `container.textContent`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L32-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
