# browser/components/storybook/.storybook/moz-uri-utils.js

source: browser/components/storybook/.storybook/moz-uri-utils.js
source-hash: c95a00166bbe1370f72f8c3d705d23a3c19a8b9e
lines: 47

## <module>
- 役割: (未記入)
- 呼び出し先: `path.resolve()`, `require()`

## rewriteChromeUri()
- 位置: L9-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `uri.startsWith()`
- 条件付き依存: `if (uri in aliasMap)` → `rewriteChromeUri()`
- 条件付き依存: `if (uri.startsWith(prefix))` → `bundlePath.endsWith()`
- 条件付き依存: `if (uri.startsWith(prefix))` → `uri.slice()`
- 条件付き依存: `if (uri.startsWith(prefix))` → `Object.entries()`
- 参照: `prefix.length`

## rewriteMozSrcUri()
- 位置: L31-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `path.resolve()`, `resolvedPath.startsWith()`, `uri.replace()`, `uri.startsWith()`
