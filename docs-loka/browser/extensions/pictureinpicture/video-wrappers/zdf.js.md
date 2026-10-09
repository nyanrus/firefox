# browser/extensions/pictureinpicture/video-wrappers/zdf.js

source: browser/extensions/pictureinpicture/video-wrappers/zdf.js
source-hash: 1eb8c6fd7afe2facbcbd955be72a15a79ec06331
lines: 43

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L8-35
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
- 呼び出し先: `Array.from()`, `Array.from(textNodeList, x => x.textContent).join()`, `container.querySelectorAll()`, `updateCaptionsFunction()`
- 条件付き依存: `if (!textNodeList.length)` → `updateCaptionsFunction()`
- 参照: `textNodeList.length`, `x.textContent`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L37-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
