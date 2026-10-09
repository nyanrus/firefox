# browser/extensions/pictureinpicture/video-wrappers/iq.js

source: browser/extensions/pictureinpicture/video-wrappers/iq.js
source-hash: 7d94b934f35809b07ef495930c5365dd5f2b88e0
lines: 97

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.constructor()
- 位置: L8-10
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.player`, `window.wrappedJSObject.playerObject`

## PictureInPictureVideoWrapper.play()
- 位置: L12-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (video.paused)` → `playPauseButton?.click()`
- 参照: `video.paused`

## PictureInPictureVideoWrapper.pause()
- 位置: L21-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (!video.paused)` → `playPauseButton?.click()`
- 参照: `video.paused`

## PictureInPictureVideoWrapper.setCurrentTime()
- 位置: L30-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.player.seek()`

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L34-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[ `[data-player-hook="subtitleelem"]`, ".subtitle_text", ].join()`, `document.querySelector()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L44-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(subtitles, x => x.innerText.trim()) .filter()`, `Array.from(subtitles, x => x.innerText.trim()) .filter(String) .join()`, `container.querySelectorAll()`, `updateCaptionsFunction()`, `x.innerText.trim()`
- 条件付き依存: `if (mutationList)` → `mutation.target.matches()`
- 条件付き依存: `if (!subtitles.length)` → `updateCaptionsFunction()`
- 条件付き依存: `if (subtitles.length > 1)` → `Array.from(subtitles).sort()`
- 条件付き依存: `if (subtitles.length > 1)` → `Array.from()`
- 参照: `a.offsetTop`, `b.offsetTop`, `subtitles.length`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L91-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
