# browser/extensions/pictureinpicture/video-wrappers/disneyplus.js

source: browser/extensions/pictureinpicture/video-wrappers/disneyplus.js
source-hash: 6ae67b651f94373ca3cbcaca02b3c63900ea1870
lines: 136

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.constructor()
- 位置: L8-11
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `video.closest()`
- 参照: `this.player`, `video.closest("disney-web-player").wrappedJSObject.mediaPlayer`

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L13-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L18-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(textNodeList, x => x.textContent).join()`, `container.querySelectorAll()`, `updateCaptionsFunction()`
- 条件付き依存: `if (!textNodeList.length)` → `updateCaptionsFunction()`
- 参照: `textNodeList.length`, `x.textContent`

## callback()
- 位置: L49-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(textNodeList, x => x.textContent).join()`, `container?.querySelectorAll()`, `updateCaptionsFunction()`
- 条件付き依存: `if (!textNodeList)` → `updateCaptionsFunction()`
- 参照: `x.textContent`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L74-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`

## PictureInPictureVideoWrapper.play()
- 位置: L78-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.player.play()`

## PictureInPictureVideoWrapper.pause()
- 位置: L82-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.player.pause()`

## PictureInPictureVideoWrapper.getPaused()
- 位置: L86-88
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.player.playbackStatus.paused`

## PictureInPictureVideoWrapper.getEnded()
- 位置: L90-92
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.player.playbackStatus.ended`

## PictureInPictureVideoWrapper.getDuration()
- 位置: L94-96
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`
- 参照: `this.player.heartbeat.playbackDuration`

## PictureInPictureVideoWrapper.getCurrentTime()
- 位置: L98-100
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`
- 参照: `this.player.heartbeat.playheadPosition`

## PictureInPictureVideoWrapper.setCurrentTime()
- 位置: L102-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.player.seek()`

## PictureInPictureVideoWrapper.getVolume()
- 位置: L106-108
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.player.volume.level`

## PictureInPictureVideoWrapper.setVolume()
- 位置: L110-112
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.player.volume.level`

## PictureInPictureVideoWrapper.isMuted()
- 位置: L114-120
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.muteButton)` → `video.ownerDocument.querySelector()`
- 参照: `this.muteButton`, `this.muteButton.store.volume.muted`, `video.ownerDocument.querySelector("toggle-mute-button").wrappedJSObject`

## PictureInPictureVideoWrapper.setMuted()
- 位置: L122-128
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (shouldMute)` → `this.player.volume.mute()`
- 条件付き依存: `if (!(shouldMute))` → `this.player.volume.unmute()`

## PictureInPictureVideoWrapper.isLive()
- 位置: L130-132
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.player.isLive`
