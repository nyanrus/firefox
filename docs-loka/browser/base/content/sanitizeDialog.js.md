# browser/base/content/sanitizeDialog.js

source: browser/base/content/sanitizeDialog.js
source-hash: 04d2253bb998827f1bb2f2201b4e9b178c39fe10
lines: 578

## <module>
- 役割: 履歴消去ダイアログ(sanitizeDialog)の画面処理を行う。消去期間やチェックボックスの状態を管理し、Sanitizer で消去を実行する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `Preferences.addAll()`, `gSanitizePromptDialog.init()`, `gSanitizePromptDialog.init().then()`, `window.addEventListener()`

## selectedTimespan()
- 位置: L64-67
- 役割: 消去期間のメニュー(sanitizeDurationChoice)の値を整数で返す。
- 触るとき: 消去期間の値の対応や、期間に応じた処理が食い違うときに見る。
- 呼び出し先: `document.getElementById()`, `parseInt()`
- 参照: `durList.value`

## warningBox()
- 位置: L69-71
- 役割: 「すべて消去」の警告ボックス要素(sanitizeEverythingWarningBox)を返す。
- 触るとき: 警告が出ない、または消えないと報告されたときに見る。
- 呼び出し先: `document.getElementById()`

## init()
- 位置: async L73-230
- 役割: ダイアログの開かれ方を判定して不要なグループを消し、OK ボタンの文言を決め、サイズ取得と警告表示を始める。
- 触るとき: 設定画面やシャットダウン時消去など開き方ごとに表示が違うとき、または初期化時の順序を変えるときに見る。
- 呼び出し先: `Intl.DateTimeFormat()`, `Intl.DateTimeFormat(navigator.language, { hour: "numeric", minute: "numeric", }).format()`, `document .getElementById()`, `document .getElementById("sanitizeDurationChoice") .addEventListener()`, `document.addEventListener()`, `document.getElementById()`, `document.l10n.setAttributes()`, `document.querySelector()`, `document.querySelectorAll()`, `new Date().setHours()`, `this._dialog.getButton()`, `this.getAndUpdateDataSizes()`, `this.registerSyncFromPrefListeners()`, `this.selectByTimespan()`, `this.showLoadingSpinners()`
- 条件付き依存: `if (arg.inBrowserWindow)` → `this._dialog.setAttribute()`
- 条件付き依存: `if (arg.inBrowserWindow)` → `this._observeTitleForChanges()`
- 条件付き依存: `if (arg.wrappedJSObject?.needNativeUI)` → `document .getElementById("sanitizeDurationChoice") .setAttribute()`
- 条件付き依存: `if (arg.wrappedJSObject?.needNativeUI)` → `document .getElementById()`
- 条件付き依存: `if (arg.wrappedJSObject?.needNativeUI)` → `document.querySelectorAll()`
- 条件付き依存: `if (arg.wrappedJSObject?.needNativeUI)` → `cb.setAttribute()`
- 条件付き依存: `if (this._inClearOnShutdownNewDialog)` → `this._dialog.setAttribute()`
- 条件付き依存: `if (this._inClearOnShutdownNewDialog)` → `clearPrivateDataGroupbox.remove()`
- 条件付き依存: `if (this._inClearOnShutdownNewDialog)` → `clearSiteDataGroupbox.remove()`
- 条件付き依存: `if (this._inClearOnShutdownNewDialog)` → `Sanitizer.maybeMigratePrefs()`
- 条件付き依存: `if (!(this._inClearOnShutdownNewDialog))` → `clearOnShutdownGroupbox.remove()`
- 条件付き依存: `if (this._inClearSiteDataNewDialog)` → `clearPrivateDataGroupbox.remove()`
- 条件付き依存: `if (!(this._inClearSiteDataNewDialog))` → `clearSiteDataGroupbox.remove()`
- 条件付き依存: `if (!(this._inClearSiteDataNewDialog))` → `Sanitizer.maybeMigratePrefs()`
- 条件付き依存: `if (lazy.AIWindow.isEnabled)` → `document.querySelectorAll()`
- 条件付き依存: `if (lazy.AIWindow.isEnabled)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (this._inClearOnShutdownNewDialog)` → `this.updatePrefs()`
- 条件付き依存: `if (!(this._inClearOnShutdownNewDialog))` → `this.sanitize()`
- 条件付き依存: `if (typeof onAccept === "function")` → `document.addEventListener()`
- 条件付き依存: `if (typeof onCancel === "function")` → `document.addEventListener()`
- 条件付き依存: `if ( this.selectedTimespan === Sanitizer.TIMESPAN_EVERYTHING && !this._inClearOnShutdownNewDialog )` → `this.prepareWarning()`
- 条件付き依存: `if ( this.selectedTimespan === Sanitizer.TIMESPAN_EVERYTHING && !this._inClearOnShutdownNewDialog )` → `document.getElementById()`
- 条件付き依存: `if ( this.selectedTimespan === Sanitizer.TIMESPAN_EVERYTHING && !this._inClearOnShutdownNewDialog )` → `document.l10n.translateFragment()`
- 条件付き依存: `if ( this.selectedTimespan === Sanitizer.TIMESPAN_EVERYTHING && !this._inClearOnShutdownNewDialog )` → `rootWin.promiseDocumentFlushed()`
- 参照: `Sanitizer.TIMESPAN_EVERYTHING`, `arg.inBrowserWindow`, `arg.mode`, `arg.wrappedJSObject`, `arg.wrappedJSObject?.needNativeUI`, `lazy.AIWindow.isEnabled`, `navigator.language`, `this._allCheckboxes`, `this._cacheCheckbox`, `this._cacheLoading`, `this._cookiesAndSiteDataCheckbox`, `this._cookiesLoading`, `this._dataSizesUpdated`, `this._dialog`, `this._inBrowserWindow`, `this._inClearOnShutdownNewDialog`, `this._inClearSiteDataNewDialog`, `this._inited`, `this._sinceMidnightSanitizeDurationOption`, `this.cacheSize`, `this.dataSizesFinishedUpdatingPromise`, `this.selectedTimespan`, `this.siteDataSizes`, `this.warningBox.hidden`, `window.arguments`, `window.browsingContext.topChromeWindow`

## updateAcceptButtonState()
- 位置: L232-238
- 役割: チェックボックスが一つも選ばれていなければ OK ボタンを無効にする。
- 触るとき: チェックを全部外したのに OK が押せる、または押せないといった挙動を調べるときに見る。
- 呼び出し先: `Array.from()`, `Array.from(this._allCheckboxes).every()`, `this._dialog.getButton()`
- 参照: `acceptButton.disabled`, `cb.checked`, `this._allCheckboxes`

## selectByTimespan()
- 位置: async L240-280
- 役割: 消去期間の選択変更時に呼ばれ、「すべて」なら警告を出してリサイズし、それ以外なら警告を隠す。どちらも最後にデータサイズを更新する。
- 触るとき: 期間を切り替えたときに警告やダイアログの高さがずれるとき、または期間の扱いを変えるときに見る。
- 呼び出し先: `document.l10n.setAttributes()`, `this.updateDataSizesInUI()`
- 条件付き依存: `if (this.selectedTimespan === Sanitizer.TIMESPAN_EVERYTHING)` → `this.prepareWarning()`
- 条件付き依存: `if (warningBox.hidden)` → `warningBox.nextElementSibling.getBoundingClientRect()`
- 条件付き依存: `if (warningBox.hidden)` → `warningBox.previousElementSibling.getBoundingClientRect()`
- 条件付き依存: `if (warningBox.hidden)` → `window.resizeBy()`
- 条件付き依存: `if (this.selectedTimespan === Sanitizer.TIMESPAN_EVERYTHING)` → `this.updateDataSizesInUI()`
- 条件付き依存: `if (!warningBox.hidden)` → `warningBox.nextElementSibling.getBoundingClientRect()`
- 条件付き依存: `if (!warningBox.hidden)` → `warningBox.previousElementSibling.getBoundingClientRect()`
- 条件付き依存: `if (!warningBox.hidden)` → `window.resizeBy()`
- 参照: `Sanitizer.TIMESPAN_EVERYTHING`, `document.documentElement`, `this._inited`, `this.selectedTimespan`, `this.warningBox`, `warningBox.hidden`, `warningBox.nextElementSibling.getBoundingClientRect().top`, `warningBox.previousElementSibling.getBoundingClientRect().bottom`

## sanitize()
- 位置: L282-320
- 役割: pref を更新し、ボタンを無効化したうえで、選ばれた項目を Sanitizer.sanitize で消去する。完了後に SiteDataManager を更新して閉じる。
- 触るとき: 履歴やデータの消去が実行されない、または途中で止まるといった問題を調べるときに見る。
- 呼び出し先: `Sanitizer.getClearRange()`, `Sanitizer.sanitize()`, `Sanitizer.sanitize(itemsToClear, options) .catch()`, `Sanitizer.sanitize(itemsToClear, options) .catch(console.error) .then()`, `console.error()`, `document.l10n.setAttributes()`, `event.preventDefault()`, `this._dialog.getButton()`, `this.getItemsToClear()`, `this.updatePrefs()`, `window.close()`
- 条件付き依存: `if (!this._inBrowserWindow)` → `lazy.SiteDataManager.updateSites()`
- 参照: `acceptButton.disabled`, `console.error`, `this._dialog.getButton("cancel").disabled`, `this._inBrowserWindow`, `this.selectedTimespan`

## prepareWarning()
- 位置: L326-337
- 役割: 選択中の項目が全部でなければ selected 用の警告文、全部なら everything 用の警告文を設定する。
- 触るとき: 警告文の出し分け条件を変えるとき、または警告の文面が状況と合わないときに見る。
- 呼び出し先: `document.getElementById()`, `this.hasNonSelectedItems()`
- 条件付き依存: `if (this.hasNonSelectedItems())` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(this.hasNonSelectedItems()))` → `document.l10n.setAttributes()`

## _getItemPrefs()
- 位置: L342-346
- 役割: チェックボックス要素の preference 属性を配列にして返す。
- 触るとき: 新しいチェックボックスを追加したとき、その pref が一覧に含まれるかを確認するときに見る。
- 呼び出し先: `Array.from()`, `Array.from(this._allCheckboxes).map()`, `checkbox.getAttribute()`
- 参照: `this._allCheckboxes`

## onReadGeneric()
- 位置: L352-369
- 役割: いずれかの項目の pref が true なら OK ボタンを有効にし、警告文も更新する。
- 触るとき: pref の同期で OK ボタンの有効状態がずれるとき、または判定に含める pref を変えるときに見る。
- 呼び出し先: `Preferences.get()`, `this._dialog.getButton()`, `this._getItemPrefs()`, `this._getItemPrefs().some()`, `this.prepareWarning()`
- 参照: `Preferences.get(pref).value`, `this._dialog.getButton("accept").disabled`

## showLoadingSpinners()
- 位置: L374-381
- 役割: Cookie とキャッシュのチェックボックス横の読み込み表示を出す。
- 触るとき: データサイズの読み込み中の表示がずれるときに見る。
- 参照: `this._cacheLoading`, `this._cacheLoading.hidden`, `this._cookiesLoading`, `this._cookiesLoading.hidden`

## hideLoadingSpinners()
- 位置: L386-393
- 役割: Cookie とキャッシュの読み込み表示を隠す。
- 触るとき: サイズ計算後も読み込み表示が残るときに見る。
- 参照: `this._cacheLoading`, `this._cacheLoading.hidden`, `this._cookiesLoading`, `this._cookiesLoading.hidden`

## getAndUpdateDataSizes()
- 位置: async L400-434
- 役割: ブラウザ内で開いた場合はサイトを更新し、5 つの期間の割当量とキャッシュサイズを取得して単位付きで保持し、UI を更新してから表示を隠す。
- 触るとき: 項目のサイズ表示が古い、または取得できないときに見る。取得対象の期間を変えるときも見る。
- 呼び出し先: `Promise.all()`, `lazy.DownloadUtils.convertByteUnits()`, `lazy.SiteDataManager.getCacheSize()`, `lazy.SiteDataManager.getQuotaUsageForTimeRanges()`, `this.hideLoadingSpinners()`, `this.updateDataSizesInUI()`
- 条件付き依存: `if (this._inBrowserWindow)` → `lazy.SiteDataManager.updateSites()`
- 参照: `this._dataSizesUpdated`, `this._inBrowserWindow`, `this.cacheSize`, `this.siteDataSizes`

## updatePrefs()
- 位置: L443-453
- 役割: 選ばれた期間の pref を書き、各チェックボックスの値を対応する bool pref に書き込む。
- 触るとき: 消去の前にダイアログの状態が pref に反映されないとき、またはシャットダウン時消去の設定が保存されないときに見る。
- 呼び出し先: `Preferences.get()`, `Services.prefs.setBoolPref()`, `Services.prefs.setIntPref()`, `this._getItemPrefs()`
- 参照: `Sanitizer.PREF_TIMESPAN`, `p.id`, `p.value`, `prefs.length`, `this.selectedTimespan`
- XPCOM: `Services.prefs`

## hasNonSelectedItems()
- 位置: L458-467
- 役割: チェックボックスのどれか一つでも pref が偽なら true を返す。
- 触るとき: 警告文が「すべて」か「選択中」かの判定がずれるときに見る。
- 呼び出し先: `Preferences.get()`, `checkboxes[i].getAttribute()`, `document.querySelectorAll()`
- 参照: `checkboxes.length`, `pref.value`

## registerSyncFromPrefListeners()
- 位置: L472-477
- 役割: 各チェックボックスに、pref が同期されたら onReadGeneric を呼ぶリスナーを登録する。
- 触るとき: pref を外から変えたときに OK ボタンの状態が追従しないときに見る。
- 呼び出し先: `Preferences.addSyncFromPrefListener()`, `document.querySelectorAll()`, `this.onReadGeneric()`

## _titleChanged()
- 位置: L479-484
- 役割: 文書の title 属性を titleText 要素の本文に反映する。
- 触るとき: ブラウザ内で開いたダイアログのタイトルが更新されないときに見る。
- 呼び出し先: `document.documentElement.getAttribute()`
- 条件付き依存: `if (title)` → `document.getElementById()`
- 参照: `document.getElementById("titleText").textContent`

## _observeTitleForChanges()
- 位置: L486-495
- 役割: 文書の title 属性の変化を MutationObserver で監視し、変わるたびに _titleChanged を呼ぶ。
- 触るとき: タイトルの追従を別の属性に広げたり、監視を止めたりするときに見る。
- 呼び出し先: `this._mutObs.observe()`, `this._titleChanged()`
- 参照: `document.documentElement`, `this._mutObs`

## updateDataSizesInUI()
- 位置: async L500-544
- 役割: 取得済みのサイズを選択期間に合わせてチェックボックスの表示に反映し、翻訳後にダイアログをリサイズする。
- 触るとき: 期間を変えても表示サイズが変わらない、またはボタンがはみ出すときに見る。期間の対応表(0 から 6)が取得対象と合っているかを確かめるときにも見る。(要確認: 5 と 6 の期間は getAndUpdateDataSizes で取得していないため、その期間を選ぶと siteDataSizes の参照が undefined になる。)
- 呼び出し先: `document.l10n.pauseObserving()`, `document.l10n.resumeObserving()`, `document.l10n.setAttributes()`, `document.l10n.translateElements()`, `window.resizeDialog()`
- 参照: `this._cacheCheckbox`, `this._cookiesAndSiteDataCheckbox`, `this._dataSizesUpdated`, `this._sinceMidnightSanitizeDurationOption`, `this.cacheSize`, `this.selectedTimespan`, `this.siteDataSizes`

## getItemsToClear()
- 位置: L551-559
- 役割: checked なチェックボックスの id を配列にして返す。
- 触るとき: 消去対象に含まれない項目がある、または余計に消えると報告されたときに見る。
- 条件付き依存: `if (cb.checked)` → `items.push()`
- 参照: `cb.checked`, `cb.id`, `this._allCheckboxes`
