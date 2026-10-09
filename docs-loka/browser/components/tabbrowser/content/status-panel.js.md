# browser/components/tabbrowser/content/status-panel.js

source: browser/components/tabbrowser/content/status-panel.js
source-hash: 1200576f64defa343cbd9cf8b365797023d40908
lines: 155

## <module>
- 役割: リンクのホバーや読み込み状況を表示するステータスパネルの制御を行う StatusPanel オブジェクトを定義する。

## panel()
- 位置: L10-22
- 役割: ステータスパネル要素を初回に取得して transition 終了の監視を付け、以後はその要素を返す。
- 触るとき: パネル要素の取得や transition 後の処理を調べるとき。
- 呼び出し先: `document.getElementById()`, `this._onTransitionEnd.bind()`, `this.panel.addEventListener()`

## isVisible()
- 位置: L24-26
- 役割: パネルに inactive 属性がなければ表示中と判定する。
- 触るとき: パネルの表示状態の判定を調べるとき。
- 呼び出し先: `this.panel.hasAttribute()`

## update()
- 位置: L28-67
- 役割: リンク上・読み込み状況・既定の順で表示文言を選び、長い base64 data URI は切り詰めて、パネルの種類とラベルを更新する。
- 触るとき: ステータス文言の優先順位や省略表示の規則を変えるとき。
- 呼び出し先: `text.match()`, `types.push()`
- 条件付き依存: `if (XULBrowserWindow.busyUI)` → `types.push()`
- 条件付き依存: `if (text.length > 500 && text.match(/^data:[^,]+;base64,/))` → `text.substring()`
- 条件付き依存: `if (this._labelElement.value != text || (text && !this.isVisible))` → `this.panel.setAttribute()`
- 条件付き依存: `if (this._labelElement.value != text || (text && !this.isVisible))` → `this.panel.getAttribute()`
- 条件付き依存: `if (this._labelElement.value != text || (text && !this.isVisible))` → `this._labelElement.setAttribute()`

## _labelElement()
- 位置: L69-72
- 役割: ラベル要素を初回に取得し、以後は同じ要素を返す。
- 触るとき: ラベル要素の取得元を調べるとき。
- 呼び出し先: `document.getElementById()`

## _label()
- 位置: L74-109
- 役割: ラベル文字列を設定してパネルを表示または非表示にし、マウス位置の追跡を付け外しする。
- 触るとき: パネルの出現・消去や幅の固定によるちらつき対策を調べるとき。
- 呼び出し先: `this.panel.getAttribute()`
- 条件付き依存: `if (!this.isVisible)` → `this.panel.removeAttribute()`
- 条件付き依存: `if ( this.panel.getAttribute("type") == "status" && this.panel.getAttribute("previoustype") == "status" )` → `window.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (this.panel.hidden)` → `getComputedStyle()`
- 条件付き依存: `if (val)` → `this.panel.removeAttribute()`
- 条件付き依存: `if (val)` → `MousePosTracker.addListener()`
- 条件付き依存: `if (!(val))` → `this.panel.setAttribute()`
- 条件付き依存: `if (!(val))` → `MousePosTracker.removeListener()`

## _onTransitionEnd()
- 位置: L111-115
- 役割: transition 終了時に非表示状態ならパネルを hidden にする。
- 触るとき: フェードアウト後にパネルが残る問題を調べるとき。

## getMouseTargetRect()
- 位置: L117-130
- 役割: RTL を考慮したパネルの矩形をマウス追跡用に返す。
- 触るとき: マウスがパネルに近づいたときの反応範囲を変えるとき。
- 呼び出し先: `window.windowUtils.getBoundsWithoutFlushing()`

## onMouseEnter()
- 位置: L132-134
- 役割: マウスが入ったときパネルの mirror 状態を切り替える。
- 触るとき: ホバー時にパネルが反対側へ移る動作を調べるとき。
- 呼び出し先: `this._mirror()`

## onMouseLeave()
- 位置: L136-138
- 役割: マウスが出たときパネルの mirror 状態を切り替える。
- 触るとき: ホバー時にパネルが反対側へ移る動作を調べるとき。
- 呼び出し先: `this._mirror()`

## _mirror()
- 位置: L140-153
- 役割: mirror 属性を切り替え、sizelimit 属性を付けて、パネルを反対側の隅に動かす。
- 触るとき: ステータスパネルの左右の位置切り替えを変えるとき。
- 呼び出し先: `this.panel.hasAttribute()`
- 条件付き依存: `if (this.panel.hasAttribute("mirror"))` → `this.panel.removeAttribute()`
- 条件付き依存: `if (!(this.panel.hasAttribute("mirror")))` → `this.panel.setAttribute()`
- 条件付き依存: `if (!this.panel.hasAttribute("sizelimit"))` → `this.panel.setAttribute()`
