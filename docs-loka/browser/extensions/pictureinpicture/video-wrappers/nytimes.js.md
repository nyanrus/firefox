# browser/extensions/pictureinpicture/video-wrappers/nytimes.js

source: browser/extensions/pictureinpicture/video-wrappers/nytimes.js
source-hash: 44de05d60c3833ef36246e0f471f85b7548b54db
lines: 42

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
- 参照: `container.querySelector(".cueWrap-2P4Ue4VQ")?.innerText`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L36-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
