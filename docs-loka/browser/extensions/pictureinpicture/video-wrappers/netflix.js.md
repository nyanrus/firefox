# browser/extensions/pictureinpicture/video-wrappers/netflix.js

source: browser/extensions/pictureinpicture/video-wrappers/netflix.js
source-hash: 6f13c759a618baf5b8546f0e59cd00098f757257
lines: 105

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.constructor()
- 位置: L8-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `id.startsWith()`, `netflixPlayerAPI.getAllPlayerSessionIds()`, `netflixPlayerAPI.getVideoPlayerBySessionId()`, `window.wrappedJSObject.netflix.appContext.state.playerApp.getAPI()`
- 参照: `this.player`, `window.wrappedJSObject.netflix.appContext.state.playerApp.getAPI() .videoPlayer`

## PictureInPictureVideoWrapper.getCurrentTime()
- 位置: L28-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.player.getCurrentTime()`

## PictureInPictureVideoWrapper.getDuration()
- 位置: L38-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.player.getDuration()`

## PictureInPictureVideoWrapper.play()
- 位置: L42-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.player.play()`

## PictureInPictureVideoWrapper.pause()
- 位置: L46-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.player.pause()`

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L50-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L55-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.querySelector()`, `updateCaptionsFunction()`
- 参照: `container.querySelector(".player-timedtext").innerText`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L73-75
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`

## PictureInPictureVideoWrapper.setCurrentTime()
- 位置: L83-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.player.seek()`

## PictureInPictureVideoWrapper.setVolume()
- 位置: L87-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.player.setVolume()`

## PictureInPictureVideoWrapper.getVolume()
- 位置: L91-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.player.getVolume()`

## PictureInPictureVideoWrapper.setMuted()
- 位置: L95-97
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.player.setMuted()`

## PictureInPictureVideoWrapper.isMuted()
- 位置: L99-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.player.isMuted()`
