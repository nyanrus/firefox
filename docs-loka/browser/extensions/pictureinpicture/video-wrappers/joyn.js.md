# browser/extensions/pictureinpicture/video-wrappers/joyn.js

source: browser/extensions/pictureinpicture/video-wrappers/joyn.js
source-hash: bc8c15aa4fc742c04fb45bd454853e54c0b82aa8
lines: 42

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L8-34
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L14-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.querySelector()`, `updateCaptionsFunction()`
- 条件付き依存: `if (!text)` → `updateCaptionsFunction()`
- 参照: `container.querySelector( `:scope > div > div > div > div[role="cue"]` )?.innerText`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L36-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
