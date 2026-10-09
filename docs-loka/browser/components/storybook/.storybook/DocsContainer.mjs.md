# browser/components/storybook/.storybook/DocsContainer.mjs

source: browser/components/storybook/.storybook/DocsContainer.mjs
source-hash: 8d9896fade86c7a7f0619c34d3f33a74eb0337d6
lines: 125

## <module>
- 役割: (未記入)

## getSelectedFromUrl()
- 位置: L19-22
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `g?.match()`, `new URLSearchParams(location.search).get()`
- 参照: `location.search`

## getOsDark()
- 位置: L23-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.matchMedia()`
- 参照: `window.matchMedia("(prefers-color-scheme: dark)").matches`

## mergeGlobalsParam()
- 位置: L26-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(existing || "").split()`, `(existing || "").split(",").filter()`, `[...map.entries()].map()`, `[...map.entries()].map(([k, v]) => `${k}:${v}`).join()`, `map.entries()`, `map.set()`, `parts.map()`, `s.split()`

## syncGlobalsUrl()
- 位置: L32-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `mergeGlobalsParam()`, `u.searchParams.get()`, `u2.searchParams.get()`
- 条件付き依存: `if (merged !== prev)` → `u.searchParams.set()`
- 条件付き依存: `if (merged !== prev)` → `window.history.replaceState()`
- 条件付き依存: `if (merged !== prev)` → `u.toString()`
- 条件付き依存: `if (merged2 !== prev2)` → `u2.searchParams.set()`
- 条件付き依存: `if (merged2 !== prev2)` → `topWin.history.replaceState()`
- 条件付き依存: `if (merged2 !== prev2)` → `u2.toString()`
- 参照: `topWin.location.href`, `window.location.href`, `window.parent`, `window.top`

## applyDocsDomTheme()
- 位置: L55-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `html.classList.toggle()`
- 条件付き依存: `if (root)` → `root.classList.toggle()`
- 参照: `document.documentElement`, `html.style.colorScheme`

## DocsContainer()
- 位置: L67-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addons.getChannel()`, `applyDocsDomTheme()`, `channel.off()`, `channel.on()`, `getOsDark()`, `getSelectedFromUrl()`, `mql.addEventListener()`, `mql.addListener()`, `mql.removeEventListener()`, `mql.removeListener()`, `useEffect()`, `useLayoutEffect()`, `useState()`, `window.matchMedia()`

## onChange()
- 位置: L83-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setOsDark()`
- 参照: `e.matches`

## onUpdate()
- 位置: L94-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `applyDocsDomTheme()`, `getOsDark()`, `setSelected()`, `syncGlobalsUrl()`
- 参照: `payload?.globals?.theme`
