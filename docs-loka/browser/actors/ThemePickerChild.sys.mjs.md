# browser/actors/ThemePickerChild.sys.mjs

source: browser/actors/ThemePickerChild.sys.mjs
source-hash: bad3e0fe5e49e0d7cb15114a3a90cb4cff9d5ed2
lines: 128

## <module>
- 役割: (未記入)

## ThemePickerChild.actorCreated()
- 位置: L16-21
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.addObserver()`
- 参照: `this.lookAndFeelChanged`, `this.prefChanged`
- XPCOM: `Services.obs` / `Services.prefs`

## ThemePickerChild.didDestroy()
- 位置: L23-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`, `Services.prefs.removeObserver()`
- 参照: `this.lookAndFeelChanged`, `this.prefChanged`
- XPCOM: `Services.obs` / `Services.prefs`

## ThemePickerChild.lookAndFeelChanged()
- 位置: L33-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `this.contentWindow.dispatchEvent()`
- 参照: `Services.appinfo .contentThemeDerivedColorSchemeIsDark`, `this.contentWindow`, `this.contentWindow.CustomEvent`
- XPCOM: `Services.appinfo`

## ThemePickerChild.prefChanged()
- 位置: async L46-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchToWindow()`, `this.sendQuery()`

## ThemePickerChild.handleEvent()
- 位置: async L66-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.themePicker.shown.record()`, `this.dispatchToWidget()`, `this.dispatchToWindow()`, `this.sendQuery()`
- 参照: `event.composedTarget`, `event.detail`, `event.type`

## ThemePickerChild.dispatchToWidget()
- 位置: L109-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `target.dispatchEvent()`
- 参照: `target.documentGlobal`, `win.CustomEvent`

## ThemePickerChild.dispatchToWindow()
- 位置: L120-126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `this.contentWindow.dispatchEvent()`
- 参照: `this.contentWindow`, `this.contentWindow.CustomEvent`
