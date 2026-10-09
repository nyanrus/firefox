# browser/extensions/webcompat/shims/figshare.js

source: browser/extensions/webcompat/shims/figshare.js
source-hash: 4f7bb0058fd85b15826b158ba78cafc4225e5a1c
lines: 83

## <module>
- 役割: (未記入)
- 呼び出し先: `console.warn()`, `document.documentElement.addEventListener()`, `document.querySelector()`, `document.requestStorageAccessForOrigin()`, `document.requestStorageAccessForOrigin(STORAGE_ACCESS_ORIGIN).then()`, `e.preventDefault()`, `e.stopPropagation()`, `link.click()`, `target.closest()`

## watchFirefoxNotificationDialogAndHide()
- 位置: L52-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`, `observer.observe()`
- 条件付き依存: `if (element)` → `obs.disconnect()`
- 参照: `document.body`, `element.style.display`
