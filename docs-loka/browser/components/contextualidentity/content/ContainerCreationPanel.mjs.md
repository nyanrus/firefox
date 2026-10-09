# browser/components/contextualidentity/content/ContainerCreationPanel.mjs

source: browser/components/contextualidentity/content/ContainerCreationPanel.mjs
source-hash: 9868c288653b83717afb0403901c8adc0058bd4d
lines: 105

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## unpinAnchor()
- 位置: L16-22
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `anchor.classList.contains()`, `anchor.classList.remove()`
- 参照: `anchor.hidden`

## open()
- 位置: async L42-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.containers.addContainerClicked.record()`, `body.replaceChildren()`, `cancelButton.addEventListener()`, `cancelButton.removeEventListener()`, `createButton.addEventListener()`, `createButton.removeEventListener()`, `doc.getElementById()`, `editor.focus()`, `editor.form.addEventListener()`, `editor.render()`, `lazy.BrowserWindowTracker.getTopWindow()`, `lazy.BrowserWindowTracker.promiseOpenWindow()`, `panel.addEventListener()`, `panel.openPopup()`, `unpinAnchor()`, `updateValidity()`
- 条件付き依存: `if (win != source)` → `win.focus()`
- 条件付き依存: `if (anchor.hidden)` → `anchor.classList.add()`
- 参照: `anchor.hidden`, `panel.state`, `source.gBrowser`, `sourceWin.top`, `win.document`

## updateValidity()
- 位置: L69-71
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `createButton.disabled`, `editor.isValid`

## onCreate()
- 位置: L75-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `editor.commit()`, `panel.hidePopup()`

## onCancel()
- 位置: L79-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panel.hidePopup()`
