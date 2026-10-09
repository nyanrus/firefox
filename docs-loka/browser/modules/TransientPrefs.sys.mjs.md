# browser/modules/TransientPrefs.sys.mjs

source: browser/modules/TransientPrefs.sys.mjs
source-hash: b9a66ca5cd008eb13bd2c6bb723a849bde1cee11
lines: 20

## <module>
- 役割: 既定値に戻した設定を、アプリ終了まで表示し続けるための可視性の記録を持つ。

## prefShouldBeVisible()
- 位置: L12-18
- 役割: 設定にユーザー値があれば表示対象として記録し、その記録の有無を返す。
- 触るとき: ユーザーが変えて既定値に戻した設定が、設定画面から即座に消えてしまう、または再起動後も残り続ける問題を調べるとき。
- 呼び出し先: `Services.prefs.prefHasUserValue()`, `prefVisibility.get()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(prefName))` → `prefVisibility.set()`
- XPCOM: `Services.prefs`
