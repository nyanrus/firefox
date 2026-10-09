# browser/modules/UIDensityTelemetry.sys.mjs

source: browser/modules/UIDensityTelemetry.sys.mjs
source-hash: 64e42398c45e6841fc9145a5cf2c1475b2ac09fa
lines: 237

## <module>
- 役割: ウィンドウ密度の設定と実際に解決された密度を ui_density.mode テレメトリとして記録する。
- 呼び出し先: `Cc["@mozilla.org/windows-ui-utils;1"].getService()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`

## currentSetting()
- 位置: L31-49
- 役割: about:preferences に表示される密度設定を automatic / compact / touch / standard 系の文字列で返す。
- 触るとき: 密度設定の種類を増やしたり名前を変えたりするとき、current の値の意味を確認するとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`, `Services.prefs.prefHasUserValue()`
- 参照: `gUIDensity.MODE_COMPACT`, `gUIDensity.MODE_NORMAL`, `gUIDensity.MODE_TOUCH`
- XPCOM: `Services.prefs`

## effectiveDensity()
- 位置: L59-69
- 役割: gUIDensity の現在の密度からウィンドウが実際に解決した密度を compact / touch / standard で返す。
- 触るとき: 自動調整で実効密度が変わった理由を調べるとき、effective の値を変えるとき。
- 呼び出し先: `gUIDensity.getCurrentDensity()`
- 参照: `gUIDensity.MODE_COMPACT`, `gUIDensity.MODE_TOUCH`, `gUIDensity.getCurrentDensity().mode`

## touchCapable()
- 位置: L74-84
- 役割: macOS は no、Windows はタブレット対応判定で yes / no、それ以外は unknown を返す。
- 触るとき: touch_capable の判定方法を変えるとき、Linux で unknown になる理由を確認するとき。
- 参照: `AppConstants.platform`, `lazy.WindowsUIUtils.isTabletCapable`

## init()
- 位置: async L121-145
- 役割: 各ウィンドウの gUIDensity.init から呼ばれ、実効密度を記録して、最初の条件を満たす最上位ウィンドウで監視を始め起動時イベントを記録する。
- 触るとき: 起動時の ui_density イベントが出ない、または重複する問題を調べるとき。
- 呼び出し先: `Services.prefs.addObserver()`, `effectiveDensity()`, `lazy.BrowserWindowTracker.getTopWindow()`, `this._lastEffective.set()`, `this._record()`
- 参照: `lazy.SessionStore.promiseAllWindowsRestored`, `this._initialized`, `win.toolbar.visible`
- XPCOM: `Services.prefs`

## uninit()
- 位置: L152-162
- 役割: テスト専用で、オブザーバーを外し記録の状態を初期化する。
- 触るとき: テストで UIDensityTelemetry の状態をリセットする仕組みを変えるとき。
- 呼び出し先: `Services.prefs.removeObserver()`
- 参照: `this._autoAdjustments`, `this._current`, `this._initialized`, `this._lastEffective`
- XPCOM: `Services.prefs`

## observe()
- 位置: L164-169
- 役割: 密度や自動タッチモードの pref が変わったとき、最上位ウィンドウで記録処理を呼ぶ。
- 触るとき: 設定画面で密度を変えたのにイベントが出ない問題を調べるとき。
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (win)` → `this._record()`

## onDensityChanged()
- 位置: L179-184
- 役割: gUIDensity から密度の変化を受け、初期化済みで最上位ウィンドウの場合に記録処理を呼ぶ。
- 触るとき: リサイズやタブレットモードなど自動的に密度が変わったときに記録されない問題を調べるとき。
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `this._record()`
- 参照: `this._initialized`

## _record()
- 位置: L194-235
- 役割: 現在の設定と実効密度を読み、前回と違うときだけ ui_density.mode を Glean で記録する。設定が変わったら自動調整の回数を 0 に戻す。
- 触るとき: イベントの項目(current, effective, auto_adjustments_prior など)を変えるとき、記録の重複や取りこぼしを調べるとき。
- 呼び出し先: `Glean.uiDensity.mode.record()`, `String()`, `currentSetting()`, `effectiveDensity()`, `this._lastEffective.get()`, `this._lastEffective.set()`, `touchCapable()`
- 参照: `extra.previous`, `this._autoAdjustments`, `this._current`, `win.devicePixelRatio`, `win.outerHeight`, `win.outerWidth`
