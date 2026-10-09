# browser/base/content/nonbrowser-mac.js

source: browser/base/content/nonbrowser-mac.js
source-hash: 57cabf79c16656b32e2e974f9350139523395560
lines: 177

## <module>
- 役割: macOS の非ブラウザウィンドウ(隠しウィンドウ等)用のメニュー・Dock 制御を担う NonBrowserWindow オブジェクトを定義し、load/unload を配線する。
- 呼び出し先: `XPCOMUtils.defineLazyServiceGetter()`, `addEventListener()`

## openBrowserWindowFromDockMenu()
- 位置: L9-20
- 役割: Dock メニューの新規ウィンドウ項目から、既存の最前面ブラウザウィンドウを opener にして新しいブラウザウィンドウを開き、読み込み後にアプリを前面化する。
- 触るとき: Dock メニューの『新規ウィンドウ』『新規プライベートウィンドウ』の挙動を変えるとき、または最前面ウィンドウがない状態で開く経路を調べるとき。
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`, `OpenBrowserWindow()`, `this.dockSupport.activateApplication()`, `win.addEventListener()`
- 参照: `options.openerWindow`

## startup()
- 位置: L22-118
- 役割: load 時に、非ブラウザ用に無効化すべきメニュー項目を disabled にし、menu_openLocation を表示する。隠しウィンドウなら閉じる系を無効化し Dock メニューを native 化し、プライベートブラウジング設定に応じて項目を隠す/削除する。最後に delayedStartup を setTimeout 0 で予約する。
- 触るとき: 隠しウィンドウのメニューや Dock メニューの項目を追加・削除するとき、またはプライベートブラウジングや終了ショートカットの有効無効条件を変えるとき。
- 呼び出し先: `document.getElementById()`, `setTimeout()`, `this.delayedStartup()`
- 条件付き依存: `if (element)` → `element.setAttribute()`
- 条件付き依存: `if (element)` → `element.removeAttribute()`
- 条件付き依存: `if (window.location.href == this.MAC_HIDDEN_WINDOW)` → `document.getElementById()`
- 条件付き依存: `if (dockMenuElement != null)` → `Cc[ "@mozilla.org/widget/standalonenativemenu;1" ].createInstance()`
- 条件付き依存: `if (dockMenuElement != null)` → `nativeMenu.init()`
- 条件付き依存: `if (window.location.href == this.MAC_HIDDEN_WINDOW)` → `dockMenuElement.addEventListener()`
- 条件付き依存: `if (PrivateBrowsingUtils.permanentPrivateBrowsing)` → `document.getElementById()`
- 条件付き依存: `if (!PrivateBrowsingUtils.enabled)` → `document.getElementById()`
- 条件付き依存: `if (!PrivateBrowsingUtils.enabled)` → `document.getElementById("key_privatebrowsing").remove()`
- 条件付き依存: `if (BrowserUIUtils.quitShortcutDisabled)` → `document.getElementById("key_quitApplication").remove()`
- 条件付き依存: `if (BrowserUIUtils.quitShortcutDisabled)` → `document.getElementById()`
- 条件付き依存: `if (BrowserUIUtils.quitShortcutDisabled)` → `document.getElementById("menu_FileQuitItem").removeAttribute()`
- 参照: `BrowserUIUtils.quitShortcutDisabled`, `Ci.nsIStandaloneNativeMenu`, `PrivateBrowsingUtils.enabled`, `PrivateBrowsingUtils.permanentPrivateBrowsing`, `document.getElementById("Tools:PrivateBrowsing").hidden`, `document.getElementById("macDockMenuNewPrivateWindow").hidden`, `document.getElementById("macDockMenuNewWindow").hidden`, `document.getElementById("menu_newPrivateWindow").hidden`, `element.hidden`, `this.MAC_HIDDEN_WINDOW`, `this.delayedStartupTimeoutId`, `this.dockSupport.dockMenu`, `window.location.href`
- XPCOM: `nsIStandaloneNativeMenu` / `@mozilla.org/widget/standalonenativemenu;1`

## delayedStartup()
- 位置: L120-130
- 役割: 予約された遅延初期化として、BrowserOffline を初期化し、プライベートウィンドウなら PrivateBrowsingUI を初期化する。
- 触るとき: オフライン表示や非ブラウザウィンドウのプライベートブラウジング UI の初期化順序を変えるとき。
- 呼び出し先: `BrowserOffline.init()`, `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (PrivateBrowsingUtils.isWindowPrivate(window))` → `PrivateBrowsingUI.init()`
- 参照: `this.delayedStartupTimeoutId`

## shutdown()
- 位置: L132-147
- 役割: unload 時に、隠しウィンドウなら Dock メニュー参照を解放する。遅延初期化がまだなら予約をキャンセルして戻り、済んでいれば BrowserOffline を解除する。
- 触るとき: ウィンドウ終了時のリーク防止や、オフライン監視の後始末を変更するとき。
- 呼び出し先: `BrowserOffline.uninit()`
- 条件付き依存: `if (this.delayedStartupTimeoutId)` → `clearTimeout()`
- 参照: `this.MAC_HIDDEN_WINDOW`, `this.delayedStartupTimeoutId`, `this.dockSupport.dockMenu`, `window.location.href`

## handleEvent()
- 位置: L149-166
- 役割: load/unload/command のイベントを startup、shutdown、Dock メニュー項目の新規ウィンドウ起動へ振り分ける。
- 触るとき: Dock メニューに新しい項目を足すとき、またはウィンドウのライフサイクルイベントの配線を調べるとき。
- 呼び出し先: `event.target.id.startsWith()`, `this.shutdown()`, `this.startup()`
- 条件付き依存: `if (event.target.id.startsWith("macDockMenuNew"))` → `this.openBrowserWindowFromDockMenu()`
- 参照: `event.target.id`, `event.type`
