# browser/extensions/pictureinpicture/video-wrappers/youtube.js

source: browser/extensions/pictureinpicture/video-wrappers/youtube.js
source-hash: 7f7720e0bdd71cb2883e5e41c17c1e938b902dfd
lines: 120

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.constructor()
- 位置: L8-16
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `video.baseURI.includes()`, `video.closest()`
- 参照: `this.player`, `video.closest("#movie_player")?.wrappedJSObject`, `video.closest("#shorts-player")?.wrappedJSObject`

## PictureInPictureVideoWrapper.isLive()
- 位置: L18-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`

## PictureInPictureVideoWrapper.setMuted()
- 位置: L22-32
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (shouldMute)` → `this.player.mute()`
- 条件付き依存: `if (!(shouldMute))` → `this.player.unMute()`
- 参照: `this.player`, `video.muted`

## PictureInPictureVideoWrapper.getDuration()
- 位置: L34-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isLive()`
- 参照: `video.duration`

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L41-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L46-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(textNodeList, x => x.textContent).join()`, `container .querySelector()`, `container .querySelector(".captions-text") ?.querySelectorAll()`, `updateCaptionsFunction()`
- 条件付き依存: `if (!textNodeList)` → `updateCaptionsFunction()`
- 参照: `x.textContent`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L76-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`

## PictureInPictureVideoWrapper.shouldHideToggle()
- 位置: L80-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `video.closest()`

## PictureInPictureVideoWrapper.isUrlbarToggleEligible()
- 位置: L84-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `video.closest()`

## PictureInPictureVideoWrapper.setVolume()
- 位置: L88-94
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.player)` → `this.player.setVolume()`
- 参照: `this.player`, `video.volume`

## PictureInPictureVideoWrapper.getVolume()
- 位置: L96-101
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.player)` → `this.player.getVolume()`
- 参照: `this.player`, `video.volume`

## PictureInPictureVideoWrapper.setPlaybackRate()
- 位置: L103-109
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.player)` → `this.player.setPlaybackRate()`
- 参照: `this.player`, `video.playbackRate`

## PictureInPictureVideoWrapper.getPlaybackRate()
- 位置: L111-116
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.player)` → `this.player.getPlaybackRate()`
- 参照: `this.player`, `video.playbackRate`
