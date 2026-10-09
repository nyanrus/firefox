# browser/modules/TransientPrefs.sys.mjs

source: browser/modules/TransientPrefs.sys.mjs
source-hash: b9a66ca5cd008eb13bd2c6bb723a849bde1cee11
lines: 20

## <module>
- 役割: (未記入)

## prefShouldBeVisible()
- 位置: L12-18
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefHasUserValue()`, `prefVisibility.get()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(prefName))` → `prefVisibility.set()`
- XPCOM: `Services.prefs`
