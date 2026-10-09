# browser/base/content/aboutRobots.js

source: browser/base/content/aboutRobots.js
source-hash: ce82722c4230971a9673e6fe08bbe04165c9c736
lines: 16

## <module>
- 役割: about:robots の補助スクリプト。エラー再試行ボタンの 1 回目と 2 回目の挙動を設定する。
- 呼び出し先: `document.getElementById()`

## button.onclick()
- 位置: L7-15
- 役割: 1 回目のクリックでボタンのラベルを label2 に変え、2 回目で非表示にする。
- 触るとき: about:robots の再試行ボタンの挙動を変えるとき。
- 条件付き依存: `if (!(buttonClicked))` → `button.getAttribute()`
- 参照: `button.style.visibility`, `button.textContent`
