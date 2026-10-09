# browser/tools/resourceUriPlugin.js

source: browser/tools/resourceUriPlugin.js
source-hash: 7d8ab9cd5444b566bbc0d54e17d2cf5b8f428ea6
lines: 74

## <module>
- 役割: (未記入)
- 呼び出し先: `require()`

## ResourceUriPlugin.constructor()
- 位置: L37-39
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#resourcePathRegExes`

## ResourceUriPlugin.apply()
- 位置: L41-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `compiler.hooks.compilation.tap()`, `normalModuleFactory.hooks.resolveForScheme .for()`, `normalModuleFactory.hooks.resolveForScheme .for("resource") .tap()`, `path.join()`, `url.href.match()`, `url.href.replace()`
- 参照: `resourceData.fragment`, `resourceData.path`, `resourceData.query`, `resourceData.resource`, `this.#resourcePathRegExes`, `url.hash`, `url.search`
