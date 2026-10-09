# browser/extensions/webcompat/shims/spotify-embed.js

source: browser/extensions/webcompat/shims/spotify-embed.js
source-hash: 2c41d216f76007915cafeafcfba4fcb9e9275cb0
lines: 136

## <module>
- 役割: (未記入)
- 呼び出し先: `console.warn()`, `document.documentElement.addEventListener()`, `sessionStorage.getItem()`

## waitForDOMContentLoaded()
- 位置: L26-30
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.addEventListener()`

## previewPlayButtonListener()
- 位置: L36-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.click()`, `button.matches()`, `console.debug()`, `document .requestStorageAccess()`, `event.preventDefault()`, `event.stopPropagation()`, `location.reload()`, `sessionStorage.setItem()`, `target.closest()`
- 参照: `button.style.opacity`, `location.origin`

## startFullPlayback()
- 位置: async L88-108
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clearInterval()`, `console.debug()`, `document.querySelector()`, `document.querySelector(SELECTOR_FULL_PLAY).click()`, `document.requestStorageAccess()`, `setInterval()`, `waitForDOMContentLoaded()`
- 条件付き依存: `if (numTries >= 50)` → `console.debug()`
- 条件付き依存: `if (numTries >= 50)` → `clearInterval()`
