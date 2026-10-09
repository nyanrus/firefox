# browser/components/preferences/dialogs/fonts.js

source: browser/components/preferences/dialogs/fonts.js
source-hash: 77398275d1fa9bb9a4aceb08b628fb30e2d13969
lines: 179

## <module>
- 役割: (未記入)
- 呼び出し先: `Preferences.addAll()`, `Promise.resolve()`, `gFontsDialog.onLoad()`, `window.addEventListener()`

## onLoad()
- 位置: L31-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FontBuilder.readFontSelection()`, `Preferences.addSyncFromPrefListener()`, `Preferences.addSyncToPrefListener()`, `Preferences.close()`, `document .getElementById()`, `document .getElementById("key_close") .addEventListener()`, `document.getElementById()`, `this.readFontLanguageGroup()`, `this.readUseDocumentFonts()`, `this.writeUseDocumentFonts()`

## _selectLanguageGroup()
- 位置: L56-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `document.getElementById()`, `prefs[i].format.replace()`
- 条件付き依存: `if (!preference)` → `Preferences.add()`
- 条件付き依存: `if (element)` → `element.setAttribute()`
- 条件付き依存: `if (prefs[i].fonttype)` → `FontBuilder.buildFontList()`
- 条件付き依存: `if (element)` → `preference.setElementValue()`
- 参照: `console.error`, `preference.id`, `prefs.length`, `prefs[i].element`, `prefs[i].fonttype`, `prefs[i].type`, `this._selectLanguageGroupPromise`

## readFontLanguageGroup()
- 位置: L158-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`, `this._selectLanguageGroup()`
- 参照: `Preferences.get("font.language.group").value`, `Services.locale.fontLanguageGroup`
- XPCOM: `Services.locale`

## readUseDocumentFonts()
- 位置: L169-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Preferences.get()`
- 参照: `preference.value`

## writeUseDocumentFonts()
- 位置: L174-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 参照: `useDocumentFonts.checked`
