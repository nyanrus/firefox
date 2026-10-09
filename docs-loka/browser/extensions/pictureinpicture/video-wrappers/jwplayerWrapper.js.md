# browser/extensions/pictureinpicture/video-wrappers/jwplayerWrapper.js

source: browser/extensions/pictureinpicture/video-wrappers/jwplayerWrapper.js
source-hash: b7261c9cc61efb724d962aef79675c23258d3651
lines: 44

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L9-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L15-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `updateCaptionsFunction()`
- 条件付き依存: `if (!text)` → `updateCaptionsFunction()`
- 参照: `container.innerText`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L38-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
