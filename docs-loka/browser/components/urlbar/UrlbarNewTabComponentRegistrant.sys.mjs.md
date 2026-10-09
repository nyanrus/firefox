# browser/components/urlbar/UrlbarNewTabComponentRegistrant.sys.mjs

source: browser/components/urlbar/UrlbarNewTabComponentRegistrant.sys.mjs
source-hash: a60c6e5fc8f3bd39fba3b1ffd72a6010c4e426ad
lines: 86

## <module>
- 役割: (未記入)

## UrlbarNewTabComponentRegistrant.constructor()
- 位置: L22-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.addObserver()`, `super()`

## UrlbarNewTabComponentRegistrant.destroy()
- 位置: L29-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.removeObserver()`

## UrlbarNewTabComponentRegistrant.onNimbusChanged()
- 位置: L33-41
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( variable == FEATURE_GATE || variable == VARIANT_A || variable == VARIANT_B )` → `this.updated()`

## UrlbarNewTabComponentRegistrant.onPrefChanged()
- 位置: L43-47
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (pref == NOVA_PREF)` → `this.updated()`

## UrlbarNewTabComponentRegistrant.getComponents()
- 位置: L49-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (!(UrlbarPrefs.get(VARIANT_B)))` → `UrlbarPrefs.get()`
- 参照: `AboutNewTabComponentRegistry.TYPES.SEARCH`
