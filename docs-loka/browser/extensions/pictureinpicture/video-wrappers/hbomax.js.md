# browser/extensions/pictureinpicture/video-wrappers/hbomax.js

source: browser/extensions/pictureinpicture/video-wrappers/hbomax.js
source-hash: d4b8abfd070285a22f0c57583c83156d4933e611
lines: 56

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.setVolume()
- 位置: L8-10
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `video.volume`

## PictureInPictureVideoWrapper.isMuted()
- 位置: L12-14
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `video.volume`

## PictureInPictureVideoWrapper.setMuted()
- 位置: L16-22
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (shouldMute)` → `this.setVolume()`
- 条件付き依存: `if (!(shouldMute))` → `this.setVolume()`

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L24-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `document.querySelector( '[data-testid="CueBoxContainer"]' ).parentElement`, `this.captionsObserver`

## callback()
- 位置: L31-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.querySelector()`, `updateCaptionsFunction()`
- 参照: `container.querySelector( '[data-testid="CueBoxContainer"]' )?.innerText`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L50-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
