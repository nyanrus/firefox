# browser/components/aboutwelcome/modules/AWToolbarUtils.sys.mjs

source: browser/components/aboutwelcome/modules/AWToolbarUtils.sys.mjs
source-hash: 6128bdb4ffdb8bbe09930c4383c702f33be2fc95
lines: 95

## <module>
- 役割: (未記入)
- 呼び出し先: `AWToolbarButton.removeSetupButtonIfOnboardingComplete()`, `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## maybeAddSetupButton()
- 位置: async L17-51
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (AWToolbarButton.didSeeFinalScreen)` → `AWToolbarButton.removeSetupButtonIfOnboardingComplete()`
- 条件付き依存: `if (AWToolbarButton.hasToolbarButtonEnabled)` → `lazy.CustomizableUI.createWidget()`
- 参照: `AWToolbarButton.didSeeFinalScreen`, `AWToolbarButton.hasToolbarButtonEnabled`, `lazy.CustomizableUI.AREA_BOOKMARKS`

## onCreated()
- 位置: L31-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserUsageTelemetry.recordWidgetChange()`
- 参照: `aNode.className`, `lazy.CustomizableUI.AREA_BOOKMARKS`

## onCommand()
- 位置: L39-41
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AWToolbarButton.openWelcome()`
- 参照: `aEvent.view`

## onDestroyed()
- 位置: L42-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserUsageTelemetry.recordWidgetChange()`

## removeSetupButtonIfOnboardingComplete()
- 位置: L53-62
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( AWToolbarButton.didSeeFinalScreen || !AWToolbarButton.hasToolbarButtonEnabled )` → `lazy.CustomizableUI.destroyWidget()`
- 参照: `AWToolbarButton.didSeeFinalScreen`, `AWToolbarButton.hasToolbarButtonEnabled`

## openWelcome()
- 位置: L64-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setStringPref()`, `win.gBrowser.addTrustedTab()`
- XPCOM: `Services.prefs`
