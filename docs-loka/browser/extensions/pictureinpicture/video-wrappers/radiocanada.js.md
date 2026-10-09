# browser/extensions/pictureinpicture/video-wrappers/radiocanada.js

source: browser/extensions/pictureinpicture/video-wrappers/radiocanada.js
source-hash: d6324247ebec415c1a324d8f3aa7be54bd3fbcec
lines: 37

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
- 位置: L26-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (video.muted !== shouldMute)` → `muteButton?.click()`
- 参照: `video.muted`
