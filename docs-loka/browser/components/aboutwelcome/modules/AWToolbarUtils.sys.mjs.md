# browser/components/aboutwelcome/modules/AWToolbarUtils.sys.mjs

source: browser/components/aboutwelcome/modules/AWToolbarUtils.sys.mjs
source-hash: 6128bdb4ffdb8bbe09930c4383c702f33be2fc95
lines: 95

## <module>
- 役割: about:welcome を開くツールバーボタン(aboutwelcome-button)の作成、撤去、起動を管理するモジュール
- 呼び出し先: `AWToolbarButton.removeSetupButtonIfOnboardingComplete()`, `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## maybeAddSetupButton()
- 位置: async L17-51
- 役割: オンボーディング完了済みなら撤去し、ツールバー表示の pref が有効なら Bookmarks 領域にボタンを作成する
- 触るとき: ツールバーボタンの出す条件(新規プロファイルの判定など)を変えるとき
- 条件付き依存: `if (AWToolbarButton.didSeeFinalScreen)` → `AWToolbarButton.removeSetupButtonIfOnboardingComplete()`
- 条件付き依存: `if (AWToolbarButton.hasToolbarButtonEnabled)` → `lazy.CustomizableUI.createWidget()`
- 参照: `AWToolbarButton.didSeeFinalScreen`, `AWToolbarButton.hasToolbarButtonEnabled`, `lazy.CustomizableUI.AREA_BOOKMARKS`

## onCreated()
- 位置: L31-38
- 役割: ボタンに CSS クラスを付け、作成を widget の変更テレメトリとして記録する
- 触るとき: ボタンの見た目や作成時の計測を変えるとき
- 呼び出し先: `lazy.BrowserUsageTelemetry.recordWidgetChange()`
- 参照: `aNode.className`, `lazy.CustomizableUI.AREA_BOOKMARKS`

## onCommand()
- 位置: L39-41
- 役割: ボタン押下で openWelcome を呼ぶ
- 触るとき: ボタン押下時の挙動を変えるとき
- 呼び出し先: `AWToolbarButton.openWelcome()`
- 参照: `aEvent.view`

## onDestroyed()
- 位置: L42-48
- 役割: ウィジェット破棄を変更テレメトリとして記録する
- 触るとき: 撤去時の計測を調べるとき
- 呼び出し先: `lazy.BrowserUsageTelemetry.recordWidgetChange()`

## removeSetupButtonIfOnboardingComplete()
- 位置: L53-62
- 役割: 完了済みか、ツールバーボタンが無効なら widget を破棄する
- 触るとき: ボタンを撤去する条件を変えるとき。pref の変化時にも呼ばれる
- 条件付き依存: `if ( AWToolbarButton.didSeeFinalScreen || !AWToolbarButton.hasToolbarButtonEnabled )` → `lazy.CustomizableUI.destroyWidget()`
- 参照: `AWToolbarButton.didSeeFinalScreen`, `AWToolbarButton.hasToolbarButtonEnabled`

## openWelcome()
- 位置: L64-73
- 役割: エントリポイントを toolbarButton に設定し、about:welcome を前面でないタブとして開く
- 触るとき: ボタン経由の起動時のエントリポイント値や開き方を変えるとき
- 呼び出し先: `Services.prefs.setStringPref()`, `win.gBrowser.addTrustedTab()`
- XPCOM: `Services.prefs`
