# browser/extensions/pictureinpicture/video-wrappers/airmozilla.js

source: browser/extensions/pictureinpicture/video-wrappers/airmozilla.js
source-hash: 6416f2df0b4d2b43c1f559c1aff6bd0afede0205
lines: 68

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.play()
- 位置: L8-15
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (video.paused)` → `playPauseButton?.click()`
- 参照: `video.paused`

## PictureInPictureVideoWrapper.pause()
- 位置: L17-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (!video.paused)` → `playPauseButton?.click()`
- 参照: `video.paused`

## PictureInPictureVideoWrapper.setMuted()
- 位置: L26-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (video.muted !== shouldMute && muteButton)` → `muteButton.click()`
- 参照: `video.muted`

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L33-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L38-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container?.querySelector()`, `updateCaptionsFunction()`
- 条件付き依存: `if (!text)` → `updateCaptionsFunction()`
- 参照: `container?.querySelector("#overlayCaption").innerText`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L62-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
