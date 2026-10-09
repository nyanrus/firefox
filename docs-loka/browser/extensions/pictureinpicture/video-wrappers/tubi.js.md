# browser/extensions/pictureinpicture/video-wrappers/tubi.js

source: browser/extensions/pictureinpicture/video-wrappers/tubi.js
source-hash: 12ceddd17030fa07ad05a1dc40ba124719ef5044
lines: 40

## <module>
- 役割: (未記入)

## PictureInPictureVideoWrapper.setCaptionContainerObserver()
- 位置: L8-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 条件付き依存: `if (container)` → `updateCaptionsFunction()`
- 条件付き依存: `if (container)` → `callback()`
- 条件付き依存: `if (container)` → `this.captionsObserver.observe()`
- 参照: `this.captionsObserver`

## callback()
- 位置: L13-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container?.querySelector()`, `updateCaptionsFunction()`
- 参照: `container?.querySelector( `[data-id="captionsComponent"]:not([style="display: none;"])` )?.innerText`

## PictureInPictureVideoWrapper.removeCaptionContainerObserver()
- 位置: L34-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.captionsObserver?.disconnect()`
