# browser/extensions/pictureinpicture/video-wrappers/tubilive.js

source: browser/extensions/pictureinpicture/video-wrappers/tubilive.js
source-hash: 821d2bb8919a7e19795458ac470891111b5b7a5a
lines: 40

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L8-32
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`, `video.parentElement`

## callback()
- 位置: L13-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.querySelector()`, `updateCaptionsFunction()`
- 参照: `container.querySelector(`.subtitleWindow`)?.innerText`, `container.querySelector(`.tubi-text-track-container`)?.innerText`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L34-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
