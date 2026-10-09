# browser/extensions/pictureinpicture/video-wrappers/hulu.js

source: browser/extensions/pictureinpicture/video-wrappers/hulu.js
source-hash: 2b6b3a3da681fb208a798897e1c6d7c7c3c7dd70
lines: 83

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.constructor()
- 位置: L8-10
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.player`, `video.wrappedJSObject.__HuluDashPlayer__`

## PictureInPictureVideoWrapper.play()
- 位置: L12-14
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.player.play()`

## PictureInPictureVideoWrapper.pause()
- 位置: L16-18
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.player.pause()`

## PictureInPictureVideoWrapper.isMuted()
- 位置: L20-22
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `video.volume`

## PictureInPictureVideoWrapper.setMuted()
- 位置: L24-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`, `this.isMuted()`
- 条件付き依存: `if (this.isMuted(video) !== shouldMute)` → `muteButton.click()`

## PictureInPictureVideoWrapper.setCurrentTime()
- 位置: L32-34
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.player.currentTime`

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L36-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L41-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `container.querySelector()`, `container.querySelectorAll()`, `updateCaptionsFunction()`, `x.textContent.trim()`
- 参照: `container.querySelector(".CaptionBox").innerText`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L73-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`

## PictureInPictureVideoWrapper.getDuration()
- 位置: L77-79
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.player.duration`
