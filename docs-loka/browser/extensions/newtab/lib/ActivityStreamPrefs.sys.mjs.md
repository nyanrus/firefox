# browser/extensions/newtab/lib/ActivityStreamPrefs.sys.mjs

source: browser/extensions/newtab/lib/ActivityStreamPrefs.sys.mjs
source-hash: 2a52708d4ffe255f1bc2e0eb5a791c4985ae7d15
lines: 109

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`

## Prefs.constructor()
- 位置: L35-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._branchObservers`

## Prefs.ignoreBranch()
- 位置: L40-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._branchObservers.delete()`, `this._branchObservers.get()`, `this._prefBranch.removeObserver()`

## Prefs.observeBranch()
- 位置: L46-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._branchObservers.set()`, `this._prefBranch.addObserver()`

## observer()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `listener.onPrefChanged()`, `this.get()`

## DefaultPrefs.constructor()
- 位置: L65-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this._config`

## DefaultPrefs.init()
- 位置: L76-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._config.get()`, `this._config.keys()`, `this.get()`, `this.set()`
- 参照: `AppConstants.MOZILLA_OFFICIAL`, `prefConfig.value`, `prefConfig.value_local_dev`
