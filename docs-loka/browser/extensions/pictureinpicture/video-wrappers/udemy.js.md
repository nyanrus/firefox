# browser/extensions/pictureinpicture/video-wrappers/udemy.js

source: browser/extensions/pictureinpicture/video-wrappers/udemy.js
source-hash: 65d0f40a777f853b5c9283f61e64b3d842891549
lines: 52

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.setMuted()
- 位置: L8-15
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (video.muted !== shouldMute && muteButton)` → `muteButton.click()`
- 参照: `video.muted`

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L17-45
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`, `video.parentElement`

## callback()
- 位置: L22-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.querySelector()`, `updateCaptionsFunction()`
- 条件付き依存: `if (!text)` → `updateCaptionsFunction()`
- 参照: `container.querySelector( `[data-purpose="captions-cue-text"]` )?.innerText`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L46-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
