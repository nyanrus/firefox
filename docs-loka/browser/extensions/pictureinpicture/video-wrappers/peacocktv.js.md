# browser/extensions/pictureinpicture/video-wrappers/peacocktv.js

source: browser/extensions/pictureinpicture/video-wrappers/peacocktv.js
source-hash: f65e78665fbf4a02e278a2d430f1b90e39d33b08
lines: 121

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.constructor()
- 位置: L15-17
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.video`, `video.wrappedJSObject`

## PictureInPictureVideoWrapper.hasCvsdkSession()
- 位置: L19-23
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.video.cvsdkSession`

## PictureInPictureVideoWrapper.play()
- 位置: L25-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasCvsdkSession()`, `this.video.cvsdkSession.play()`
- 条件付き依存: `if (!this.hasCvsdkSession())` → `this.video.play()`

## PictureInPictureVideoWrapper.pause()
- 位置: L33-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasCvsdkSession()`, `this.video.cvsdkSession.pause()`
- 条件付き依存: `if (!this.hasCvsdkSession())` → `this.video.pause()`

## PictureInPictureVideoWrapper.setCurrentTime()
- 位置: L41-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasCvsdkSession()`, `this.video.cvsdkSession.seek()`
- 参照: `this.video.currentTime`

## PictureInPictureVideoWrapper.setDefaultCaptionMutationObserver()
- 位置: L53-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getContainer()`, `this.captionsObserver.observe()`, `updateCaptionsFunction()`
- 参照: `getContainer().innerText`, `this.captionsObserver`, `video.parentElement`

## getContainer()
- 位置: L64-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `video.parentElement.querySelector()`

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L82-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasCvsdkSession()`, `this.video.cvsdkSession.setSimpleCueHandler()`
- 条件付き依存: `if (!this.hasCvsdkSession())` → `this.setDefaultCaptionMutationObserver()`

## PictureInPictureVideoWrapper.getDuration()
- 位置: L90-95
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasCvsdkSession()`, `this.video.cvsdkSession.getDuration()`
- 参照: `this.video.duration`

## PictureInPictureVideoWrapper.getCurrentTime()
- 位置: L97-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasCvsdkSession()`, `this.video.cvsdkSession.getCurrentTime()`
- 参照: `this.video.currentTime`

## PictureInPictureVideoWrapper.setMuted()
- 位置: L104-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasCvsdkSession()`, `this.video.cvsdkSession.setMute()`
- 参照: `this.video.muted`

## PictureInPictureVideoWrapper.getMuted()
- 位置: L112-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasCvsdkSession()`, `this.video.cvsdkSession.isMuted()`
- 参照: `this.video.muted`
