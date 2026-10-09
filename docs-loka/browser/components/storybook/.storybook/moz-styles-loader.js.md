# browser/components/storybook/.storybook/moz-styles-loader.js

source: browser/components/storybook/.storybook/moz-styles-loader.js
source-hash: 683ace21a3d001fdd7da47d7eb91b8690bd0d1d0
lines: 273

## <module>
- 役割: (未記入)
- 呼び出し先: `path.resolve()`, `require()`

## getReferencedCssUris()
- 位置: L109-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `matches.add()`, `source.matchAll()`

## resolveCssUri()
- 位置: L128-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cssUri.startsWith()`
- 条件付き依存: `if (cssUri.startsWith("chrome://"))` → `rewriteChromeUri()`
- 条件付き依存: `if (localPath)` → `path.join()`
- 条件付き依存: `if (cssUri.startsWith("moz-src:///"))` → `rewriteMozSrcUri()`
- 条件付き依存: `if (absolutePath)` → `path.relative()`
- 条件付き依存: `if (absolutePath)` → `path.dirname()`
- 条件付き依存: `if (absolutePath)` → `localPath.startsWith()`

## rewriteCssModuleScriptImports()
- 位置: L173-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handledUris.add()`, `resolveCssUri()`, `source.replace()`, `statement .replace()`, `statement .replace(cssUri, `${localPath}?css-module`) .replace()`, `this.addMissingDependency()`
- 参照: `this.resourcePath`

## rewriteCssUris()
- 位置: async L203-255
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["moz-label.mjs", "panel-list.mjs"].includes()`, `cssUriToLocalPath.entries()`, `getReferencedCssUris()`, `getReferencedCssUris(sourceAfterModuleScripts).filter()`, `handledUris.has()`, `path .basename()`, `path .basename(localPath, ".css") .replaceAll()`, `path.basename()`, `resolveCssUri()`, `rewriteCssModuleScriptImports.call()`, `this.resourcePath.endsWith()`
- 条件付き依存: `if (localPath)` → `cssUriToLocalPath.set()`
- 条件付き依存: `if (localPath)` → `this.addMissingDependency()`
- 条件付き依存: `if ( ["moz-label.mjs", "panel-list.mjs"].includes( path.basename(this.resourcePath) ) || this.resourcePath.endsWith(".js") )` → `rewrittenSource.replaceAll()`
- 条件付き依存: `if (!( ["moz-label.mjs", "panel-list.mjs"].includes( path.basename(this.resourcePath) ) || this.resourcePath.endsWith(".js") ))` → `rewrittenSource.replaceAll()`
- 参照: `this.resourcePath`

## mozUriLoader()
- 位置: async L264-272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `callback()`, `rewriteCssUris.call()`, `this.async()`
