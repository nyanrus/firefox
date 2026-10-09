# browser/components/taskbartabs/TaskbarTabsChrome.sys.mjs

source: browser/components/taskbartabs/TaskbarTabsChrome.sys.mjs
source-hash: 2f876c6acbc0748fcf0f3ecd148ee4a6649b3122
lines: 112

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.defineLazyServiceGetters()`

## init()
- 位置: L20-40
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.TabBarVisibility.update()`, `document.documentElement.hasAttribute()`, `document.documentElement.setAttribute()`, `document.getElementById()`, `initAudioButton()`, `initCornerIcon()`
- 参照: `aWindow.document`, `document.getElementById("star-button-box").style.display`

## initCornerIcon()
- 位置: L43-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.document.getElementById()`, `e.detail.changed.includes()`, `tab.addEventListener()`, `tab.hasAttribute()`, `updateCornerIcon()`
- 参照: `aWindow.gBrowser.tabs`

## updateCornerIcon()
- 位置: L47-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.gBrowser.getIcon()`, `tab.hasAttribute()`
- 条件付き依存: `if (tab.hasAttribute("triggeringprincipal"))` → `favicon.setAttribute()`
- 条件付き依存: `if (tab.hasAttribute("triggeringprincipal"))` → `tab.getAttribute()`
- 条件付き依存: `if (!(tab.hasAttribute("triggeringprincipal")))` → `favicon.removeAttribute()`
- 参照: `favicon.src`, `lazy.Favicons.defaultFavicon.spec`

## initAudioButton()
- 位置: L89-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `aWindow.document.getElementById()`, `audioButton.addEventListener()`, `audioButton.setAttribute()`, `audioButton.toggleAttribute()`, `tab.addEventListener()`, `tab.hasAttribute()`, `tab.toggleMuteAudio()`
- 参照: `aWindow.gBrowser.tabs`
