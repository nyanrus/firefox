# browser/extensions/newtab/webpack.system-addon.config.js

source: browser/extensions/newtab/webpack.system-addon.config.js
source-hash: 537d63d154d067ffa349f5a791678d574379e8d5
lines: 173

## <module>
- 役割: (未記入)
- 呼び出し先: `absolute()`, `path.resolve()`, `require()`, `vendored()`

## absolute()
- 位置: L7-7
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `path.join()`

## vendored()
- 位置: L12-12
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `name.split()`, `path.join()`

## baseConfig()
- 位置: L19-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `vendored()`
- 参照: `env.development`

## DependencyListPlugin.constructor()
- 位置: L50-52
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.outputPath`

## DependencyListPlugin.apply()
- 位置: L54-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...stats.compilation.fileDependencies].sort()`, `compiler.hooks.done.tap()`, `deps.join()`, `require()`, `require("fs").appendFileSync()`
- 参照: `stats.compilation.fileDependencies`, `this.outputPath`

## dependencyListPlugins()
- 位置: L62-65
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `process.env.MOZ_WEBPACK_DEPS`

## module.exports()
- 位置: L81-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Object.assign()`, `absolute()`, `baseConfig()`, `dependencyListPlugins()`, `path.basename()`, `path.join()`, `path.resolve()`
- 参照: `env.development`, `env.outputPath`, `webpack.BannerPlugin`, `webpack.DefinePlugin`, `webpack.optimize.ModuleConcatenationPlugin`
