# browser/extensions/pictureinpicture/video-wrappers/voot.js

source: browser/extensions/pictureinpicture/video-wrappers/voot.js
source-hash: 91209cf3f752669b7d3cf0c8e6ea44ad1944e472
lines: 41

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L8-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L13-21
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.querySelector()`, `updateCaptionsFunction()`
- 条件付き依存: `if (!text)` → `updateCaptionsFunction()`
- 参照: `container.querySelector(".playkit-subtitles").innerText`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L35-37
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
