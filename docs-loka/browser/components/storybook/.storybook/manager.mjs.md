# browser/components/storybook/.storybook/manager.mjs

source: browser/components/storybook/.storybook/manager.mjs
source-hash: b3615681a6499b6deb26b3eea7ca044b59d44370
lines: 61

## <module>
- 役割: (未記入)
- 呼び出し先: `addons.getChannel()`, `apply()`, `channel.on()`, `document.createElement()`, `document.head.appendChild()`, `getToolbarTheme()`, `link.setAttribute()`, `mql.addEventListener()`, `mql.addListener()`, `window.matchMedia()`

## getToolbarTheme()
- 位置: L21-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `g?.match()`, `new URLSearchParams(location.search).get()`
- 参照: `location.search`

## pickTheme()
- 位置: L28-36
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `mql.matches`

## apply()
- 位置: L38-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addons.setConfig()`, `pickTheme()`

## onOsChange()
- 位置: L42-46
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (selected === "system")` → `apply()`

## onGlobals()
- 位置: L51-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `apply()`
- 参照: `globals.theme`, `globals?.theme`
