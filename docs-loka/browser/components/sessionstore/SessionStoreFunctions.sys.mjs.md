# browser/components/sessionstore/SessionStoreFunctions.sys.mjs

source: browser/components/sessionstore/SessionStoreFunctions.sys.mjs
source-hash: 3b42523e4b96d09aedeace381229509ba7651242
lines: 93

## <module>
- 役割: 子プロセスからの sessionstore 更新要求を SessionStore 本体の updateSessionStoreFromChild に渡す XPCOM ラッパー。
- 呼び出し先: `ChromeUtils.generateQI()`

## SessionStoreFunctions.UpdateSessionStore()
- 位置: L7-23
- 役割: フォームデータ・スクロール等を含む通常のセッション更新を SessionStore に転送する公開メソッド。
- 触るとき: 子プロセスから届く tab 状態の更新経路を変えるとき、または epoch や sHistory 収集の扱いを調べるとき。
- 呼び出し先: `SessionStoreFuncInternal.updateSessionStore()`

## SessionStoreFunctions.UpdateSessionStoreForStorage()
- 位置: L25-39
- 役割: sessionStorage 等のストレージ情報だけを SessionStore に転送する公開メソッド。
- 触るとき: ストレージ（DOMStorage）の保存が遅れる・抜ける不具合を追うとき。
- 呼び出し先: `SessionStoreFuncInternal.updateSessionStoreForStorage()`

## SSF_updateSessionStore()
- 位置: L43-71
- 役割: formdata と scroll を JSON 化してから updateSessionStoreFromChild に data・epoch・sHistoryNeeded を渡す内部処理。
- 触るとき: フォーム入力やスクロール位置がセッションに保存されない問題を調べるとき。
- 呼び出し先: `SessionStore.updateSessionStoreFromChild()`
- 条件付き依存: `if (formdata)` → `formdata.toJSON()`
- 条件付き依存: `if (scroll)` → `scroll.toJSON()`
- 参照: `aData.formdata`, `aData.scroll`

## SSF_updateSessionStoreForStorage()
- 位置: L73-87
- 役割: ストレージデータを data.storage に包み、epoch を付けて updateSessionStoreFromChild を第5引数 true 付きで呼ぶ内部処理。
- 触るとき: ストレージ更新の epoch 判定や、保存先への反映順序を変えるときに見る。
- 呼び出し先: `SessionStore.updateSessionStoreFromChild()`
