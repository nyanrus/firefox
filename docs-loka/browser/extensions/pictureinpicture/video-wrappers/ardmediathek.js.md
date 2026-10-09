# browser/extensions/pictureinpicture/video-wrappers/ardmediathek.js

source: browser/extensions/pictureinpicture/video-wrappers/ardmediathek.js
source-hash: bbba778fce80ddeb08f442fbb49d6726f43f88c4
lines: 54

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L8-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `video.closest()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L13-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.querySelector()`, `updateCaptionsFunction()`
- 条件付き依存: `if (mutationList)` → `mutation.target.matches()`
- 条件付き依存: `if (!text)` → `updateCaptionsFunction()`
- 参照: `container.querySelector(".ardplayer-untertitel")?.innerText`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L48-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
