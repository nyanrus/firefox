# browser/extensions/pictureinpicture/video-wrappers/primeVideo.js

source: browser/extensions/pictureinpicture/video-wrappers/primeVideo.js
source-hash: e97999391ad206c5dcd5bc5fee1871ef315c0bbb
lines: 110

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.play()
- 位置: L16-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `video.play()`, `video.play().catch()`

## PictureInPictureVideoWrapper.setCurrentTime()
- 位置: L36-55
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (video.readyState < video.HAVE_CURRENT_DATA)` → `video .play() .then(() => { if (!wasPlaying) { video.pause(); } }) .catch()`
- 条件付き依存: `if (video.readyState < video.HAVE_CURRENT_DATA)` → `video .play() .then()`
- 条件付き依存: `if (video.readyState < video.HAVE_CURRENT_DATA)` → `video .play()`
- 条件付き依存: `if (!wasPlaying)` → `video.pause()`
- 条件付き依存: `if (wasPlaying)` → `this.play()`
- 参照: `this.wasPlaying`, `video.HAVE_CURRENT_DATA`, `video.currentTime`, `video.paused`, `video.readyState`

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L57-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document?.querySelector()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L62-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container?.querySelector()`, `updateCaptionsFunction()`
- 条件付き依存: `if (container?.querySelector(".atvwebplayersdk-player-container"))` → `container ?.querySelector(".f35bt6a") ?.querySelector()`
- 条件付き依存: `if (container?.querySelector(".atvwebplayersdk-player-container"))` → `container ?.querySelector()`
- 条件付き依存: `if (!(container?.querySelector(".atvwebplayersdk-player-container")))` → `container ?.querySelector(".persistentPanel") ?.querySelector()`
- 条件付き依存: `if (!(container?.querySelector(".atvwebplayersdk-player-container")))` → `container ?.querySelector()`
- 条件付き依存: `if (!text)` → `updateCaptionsFunction()`
- 参照: `container ?.querySelector(".f35bt6a") ?.querySelector(".atvwebplayersdk-captions-text")?.innerText`, `container ?.querySelector(".persistentPanel") ?.querySelector("span")?.innerText`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L100-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`

## PictureInPictureVideoWrapper.shouldHideToggle()
- 位置: L104-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `video.classList.contains()`
