# browser/extensions/pictureinpicture/video-wrappers/hotstar.js

source: browser/extensions/pictureinpicture/video-wrappers/hotstar.js
source-hash: 3fa81c52017dce08a6a667c9bccac8216a1f9a1b
lines: 44

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L8-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L13-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(textNodeList, x => x.textContent).join()`, `container?.querySelectorAll()`, `updateCaptionsFunction()`
- 条件付き依存: `if (!textNodeList)` → `updateCaptionsFunction()`
- 参照: `x.textContent`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L38-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
