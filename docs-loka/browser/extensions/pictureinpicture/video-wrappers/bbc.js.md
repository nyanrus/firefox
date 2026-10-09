# browser/extensions/pictureinpicture/video-wrappers/bbc.js

source: browser/extensions/pictureinpicture/video-wrappers/bbc.js
source-hash: c527aea63fb107e1da17e03b89b8417997beb60e
lines: 36

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L8-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L13-16
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.querySelector()`, `updateCaptionsFunction()`
- 参照: `container.querySelector(".p_cueDirUniWrapper")?.innerText`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L30-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
