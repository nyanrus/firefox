# browser/extensions/pictureinpicture/video-wrappers/apple.js

source: browser/extensions/pictureinpicture/video-wrappers/apple.js
source-hash: b89255b7e080ff775c27f5fe9d076659b9a23fd9
lines: 26

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.play()
- 位置: L8-14
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container?.querySelector()`
- 条件付き依存: `if (video.paused && playButton)` → `playButton?.click()`
- 参照: `video.parentNode`, `video.paused`

## PictureInPictureVideoWrapper.pause()
- 位置: L16-22
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container?.querySelector()`
- 条件付き依存: `if (!video.paused && pauseButton)` → `pauseButton?.click()`
- 参照: `video.parentNode`, `video.paused`
