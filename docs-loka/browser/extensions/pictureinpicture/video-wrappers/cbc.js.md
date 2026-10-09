# browser/extensions/pictureinpicture/video-wrappers/cbc.js

source: browser/extensions/pictureinpicture/video-wrappers/cbc.js
source-hash: 2c45708c8743b4f90a692af3f1b7ecf8e64ab1c0
lines: 31

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.play()
- 位置: L8-13
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (video.paused)` → `playButton?.click()`
- 参照: `video.paused`

## PictureInPictureVideoWrapper.pause()
- 位置: L15-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (!video.paused)` → `pauseButton?.click()`
- 参照: `video.paused`

## PictureInPictureVideoWrapper.setMuted()
- 位置: L22-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (video.muted !== shouldMute)` → `muteButton?.click()`
- 参照: `video.muted`
