# browser/extensions/pictureinpicture/video-wrappers/mock-wrapper.js

source: browser/extensions/pictureinpicture/video-wrappers/mock-wrapper.js
source-hash: 19c49d1f951e8139cf421559f0cdad4294cad527
lines: 56

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L8-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L14-14
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `updateCaptionsFunction()`
- 参照: `container.textContent`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L25-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`

## PictureInPictureVideoWrapper.play()
- 位置: L29-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`, `playPauseButton.click()`

## PictureInPictureVideoWrapper.pause()
- 位置: L34-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`, `playPauseButton.click()`

## PictureInPictureVideoWrapper.setMuted()
- 位置: L40-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (video.muted !== shouldMute && muteButton)` → `muteButton.click()`
- 参照: `video.muted`

## PictureInPictureVideoWrapper.shouldHideToggle()
- 位置: L49-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `video.classList.contains()`
