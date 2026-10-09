# browser/extensions/pictureinpicture/video-wrappers/piped.js

source: browser/extensions/pictureinpicture/video-wrappers/piped.js
source-hash: 8f1b1efa8481e51ca9f2c25c21d99219f6afac84
lines: 46

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L8-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L13-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(textNodeList, x => x.textContent).join()`, `container .querySelector()`, `container .querySelector(".shaka-text-wrapper") ?.querySelectorAll()`, `updateCaptionsFunction()`
- 条件付き依存: `if (!textNodeList)` → `updateCaptionsFunction()`
- 参照: `x.textContent`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L40-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
