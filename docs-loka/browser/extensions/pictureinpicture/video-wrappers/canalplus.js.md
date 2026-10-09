# browser/extensions/pictureinpicture/video-wrappers/canalplus.js

source: browser/extensions/pictureinpicture/video-wrappers/canalplus.js
source-hash: 210fabc247d7e65eed9e8addc67e65c9df23d766
lines: 61

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.isLive()
- 位置: L8-11
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `documentURI.includes()`
- 参照: `document.documentURI`

## PictureInPictureVideoWrapper.getDuration()
- 位置: L13-18
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.isLive()`
- 参照: `video.duration`

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L20-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L27-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.querySelector()`, `updateCaptionsFunction()`
- 条件付き依存: `if (!text)` → `updateCaptionsFunction()`
- 参照: `container.querySelector( ".rxp-texttrack-region" )?.innerText`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L55-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
