# browser/components/sessionstore/TabAttributes.sys.mjs

source: browser/components/sessionstore/TabAttributes.sys.mjs
source-hash: ea53156d129cba5309702446a3994747af81c069
lines: 44

## <module>
- 役割: セッション復元で保存・再設定するタブ属性（現状は customizemode のみ）を扱う小さなユーティリティ。
- 呼び出し先: `Object.freeze()`

## get()
- 位置: L12-14
- 役割: TabAttributesInternal.get を呼ぶ公開 getter。タブから保存対象の属性を集める。
- 触るとき: 保存対象の属性を増やす、または復元時の属性の受け渡しを確かめるとき。
- 呼び出し先: `TabAttributesInternal.get()`

## set()
- 位置: L16-18
- 役割: TabAttributesInternal.set を呼ぶ公開 setter。保存済みデータをタブに戻す。
- 触るとき: 復元後にタブ属性が反映されない原因を追うとき。
- 呼び出し先: `TabAttributesInternal.set()`

## get()
- 位置: L22-32
- 役割: PERSISTED_ATTRIBUTES のうちタブが持つ属性だけを読み、オブジェクトにまとめる。
- 触るとき: customizemode などの属性がセッションに書き出されない問題を調べるとき。
- 呼び出し先: `tab.hasAttribute()`
- 条件付き依存: `if (tab.hasAttribute(name))` → `tab.getAttribute()`

## set()
- 位置: L34-42
- 役割: 各保存対象属性をいったん削除し、データに含まれていれば設定し直す。
- 触るとき: 復元時に古い属性が残る、または属性が消えてしまう問題を調べるとき。
- 呼び出し先: `tab.removeAttribute()`
- 条件付き依存: `if (name in data)` → `tab.setAttribute()`
