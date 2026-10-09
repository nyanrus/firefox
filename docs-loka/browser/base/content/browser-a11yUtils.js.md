# browser/base/content/browser-a11yUtils.js

source: browser/base/content/browser-a11yUtils.js
source-hash: d9ebd3727fa1bea144e396577c28027eb5c6703d
lines: 75

## <module>
- 役割: UI のアクセシビリティ補助。画面読み上げ向けに、非フォーカスの重要な通知を announce で読ませる。

## announce()
- 位置: async L31-73
- 役割: Fluent ID または生の文字列を読み上げ用の要素に入れる。翻訳待ちの間に新しい通知が来た場合は古い方を取り消す。
- 触るとき: 読み上げ通知を新たに出す、または通知の仕組みを変えるとき。
- 呼び出し先: `document.createElement()`, `document.getElementById()`, `label.setAttribute()`, `live.appendChild()`
- 条件付き依存: `if (this._cancelAnnounce)` → `this._cancelAnnounce()`
- 条件付き依存: `if (id)` → `document.l10n.formatValue()`
- 条件付き依存: `if (live.firstChild)` → `live.firstChild.remove()`
- 参照: `live.firstChild`, `this._cancelAnnounce`

## this._cancelAnnounce()
- 位置: L45-45
- 役割: 翻訳待ちの announce を取り消すフラグを立てる関数。
- 触るとき: 連続した通知で古い方が出てしまう問題を調べるとき。
