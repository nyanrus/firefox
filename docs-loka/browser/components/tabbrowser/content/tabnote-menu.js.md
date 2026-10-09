# browser/components/tabbrowser/content/tabnote-menu.js

source: browser/components/tabbrowser/content/tabnote-menu.js
source-hash: 3466f21a4e060ed9a43b62f64b3f9eb0cc5fd689
lines: 312

## <module>
- 役割: タブのメモを作成・編集・削除するパネル要素 tabnote-menu を定義する。
- 呼び出し先: `ChromeUtils.importESModule()`, `customElements.define()`

## MozTabbrowserTabNoteMenu.connectedCallback()
- 位置: L100-135
- 役割: 初回接続時にマークアップを挿入し、パネルや各ボタンを取得してイベントを登録する。
- 触るとき: メモパネルの構造や初期化、ボタンの結び付けを変えるとき。
- 呼び出し先: `document.getElementById()`, `this.#cancelButton.addEventListener()`, `this.#deleteButton.addEventListener()`, `this.#deleteNote()`, `this.#noteField.addEventListener()`, `this.#panel.addEventListener()`, `this.#panel.hidePopup()`, `this.#saveButton.addEventListener()`, `this.appendChild()`, `this.initializeAttributeInheritance()`, `this.querySelector()`, `this.saveNote()`

## MozTabbrowserTabNoteMenu.on_keypress()
- 位置: L137-153
- 役割: Esc でパネルを閉じ、メモ欄で Shift なしの Enter を押すと保存する。
- 触るとき: メモパネルのキー操作を変えるとき。
- 呼び出し先: `this.#panel.hidePopup()`
- 条件付き依存: `if (!event.shiftKey && event.target === this.#noteField)` → `this.saveNote()`

## MozTabbrowserTabNoteMenu.on_input()
- 位置: L155-157
- 役割: 入力のたびにパネルの状態(文字数警告や保存可否)を更新する。
- 触るとき: 入力時の保存ボタンの有効化や文字数表示を調べるとき。
- 呼び出し先: `this.#updatePanel()`

## MozTabbrowserTabNoteMenu.on_popuphidden()
- 位置: L159-163
- 役割: パネルが閉じたとき、対象タブ・入力値・telemetry 元を初期化する。
- 触るとき: パネルを閉じた後に状態が残る問題を調べるとき。

## MozTabbrowserTabNoteMenu.createMode()
- 位置: L165-167
- 役割: 現在が新規作成モードかを返す。
- 触るとき: 作成と編集のモード判定を調べるとき。

## MozTabbrowserTabNoteMenu.createMode()
- 位置: L169-187
- 役割: 作成・編集モードに応じて見出し、区切り、削除ボタン、aria-label を切り替える。
- 触るとき: 作成時と編集時で表示を変えたいとき。
- 呼び出し先: `gBrowser.tabLocalization.formatValueSync()`, `this.#panel.setAttribute()`

## MozTabbrowserTabNoteMenu.#panelPosition()
- 位置: L189-196
- 役割: 縦タブか横タブか、サイドバーの位置に応じてパネルの開く位置を返す。
- 触るとき: メモパネルの表示位置がずれるとき。

## MozTabbrowserTabNoteMenu.#updatePanel()
- 位置: L198-239
- 役割: 文字数から警告状態と保存可否を決め、入力量に合わせてメモ欄の高さを調整する。
- 触るとき: 文字数の上限や警告表示、入力欄の高さ調整を変えるとき。
- 呼び出し先: `getComputedStyle()`, `parseFloat()`, `this.#noteField.value.trim()`
- 条件付き依存: `if (overflow != OverflowState.NONE)` → `this.#panel.setAttribute()`
- 条件付き依存: `if (overflow != OverflowState.NONE)` → `gBrowser.tabLocalization.formatValueSync()`
- 条件付き依存: `if (!(overflow != OverflowState.NONE))` → `this.#panel.removeAttribute()`

## MozTabbrowserTabNoteMenu.openPanel()
- 位置: L248-282
- 役割: 対象タブが対象なら既存メモを読み込んで作成か編集のモードで開き、入力欄にフォーカスする。
- 触るとき: メモパネルを開く流れや telemetry 元の受け渡しを調べるとき。
- 呼び出し先: `TabNotes.get()`, `TabNotes.get(tab).then()`, `TabNotes.isEligible()`, `this.#noteField.focus()`, `this.#panel.addEventListener()`, `this.#panel.openPopup()`, `this.#updatePanel()`

## MozTabbrowserTabNoteMenu.saveNote()
- 位置: L284-298
- 役割: 有効なメモ(空でなく上限以内)を保存してパネルを閉じる。
- 触るとき: メモ保存の条件や保存先の呼び出しを変えるとき。
- 呼び出し先: `TabNotes.isEligible()`, `note.trim()`, `this.#panel.hidePopup()`
- 条件付き依存: `if ( TabNotes.isEligible(this.#currentTab) && note.trim().length && note.length <= OVERFLOW_MAX_THRESHOLD )` → `TabNotes.set()`

## MozTabbrowserTabNoteMenu.#deleteNote()
- 位置: L300-307
- 役割: 対象タブのメモを削除してパネルを閉じる。
- 触るとき: メモ削除の動作を調べるとき。
- 呼び出し先: `TabNotes.isEligible()`, `this.#panel.hidePopup()`
- 条件付き依存: `if (TabNotes.isEligible(this.#currentTab))` → `TabNotes.delete()`
