# browser/extensions/pictureinpicture/video-wrappers/edx.js

source: browser/extensions/pictureinpicture/video-wrappers/edx.js
source-hash: e660d709b2ff2bfbcdbfb94323170aa237df63bd
lines: 38

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L8-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L13-18
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.querySelector()`, `updateCaptionsFunction()`
- 参照: `container.querySelector( ".closed-captions.is-visible" )?.innerText`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L32-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
