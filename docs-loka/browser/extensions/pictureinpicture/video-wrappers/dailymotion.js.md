# browser/extensions/pictureinpicture/video-wrappers/dailymotion.js

source: browser/extensions/pictureinpicture/video-wrappers/dailymotion.js
source-hash: e75712a1638137dedfebeaf644dfd0303ce98a54
lines: 56

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L8-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `video.closest()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L13-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.querySelector()`, `updateCaptionsFunction()`
- 条件付き依存: `if (mutationList.length)` → `mutation.target.matches()`
- 条件付き依存: `if (!text)` → `updateCaptionsFunction()`
- 参照: `container.querySelector(".subtitles_placeholder")?.innerText`, `mutationList.length`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L50-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
