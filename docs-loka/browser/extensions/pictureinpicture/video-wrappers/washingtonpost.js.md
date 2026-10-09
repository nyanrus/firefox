# browser/extensions/pictureinpicture/video-wrappers/washingtonpost.js

source: browser/extensions/pictureinpicture/video-wrappers/washingtonpost.js
source-hash: 7239b0c7884697e84373ada3b8ac58b33fed5469
lines: 47

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L8-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L13-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.querySelector()`, `element.replaceWith()`, `subtitleElement.cloneNode()`, `subtitleElementClone.getElementsByTagName()`, `updateCaptionsFunction()`
- 条件付き依存: `if (!subtitleElement?.innerText)` → `updateCaptionsFunction()`
- 参照: `subtitleElement?.innerText`, `subtitleElementClone.innerText`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L41-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
