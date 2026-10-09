# browser/tools/mozscreenshots/mozscreenshots/extension/TestRunner.sys.mjs

source: browser/tools/mozscreenshots/mozscreenshots/extension/TestRunner.sys.mjs
source-hash: 94cdd31c17ea6a227af2a472ec0943b34e47e136
lines: 663

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## init()
- 位置: L29-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setupOS()`
- 参照: `this._extensionPath`

## initTest()
- 位置: L40-42
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.mochitestScope`

## setupOS()
- 位置: L44-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.disableNotificationCenter()`
- 参照: `AppConstants.platform`

## disableNotificationCenter()
- 位置: L53-69
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/file/local;1"].createInstance()`, `Cc["@mozilla.org/process/util;1"].createInstance()`, `killall.initWithPath()`, `killallP.init()`, `killallP.run()`
- 参照: `Ci.nsIFile`, `Ci.nsIProcess`, `killallArgs.length`
- XPCOM: [`nsIFile`](../../../../components/shell/nsIShellService.idl.md) / [`nsIProcess`](../../../../../xpcom/threads/nsIProcess.idl.md) / `@mozilla.org/file/local;1` / `@mozilla.org/process/util;1`

## start()
- 位置: async L74-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`, `Services.env.get()`, `Services.prefs.setCharPref()`, `Services.prefs.setIntPref()`, `Services.wm.getMostRecentWindow()`, `browserWindow.document .getElementById()`, `browserWindow.document .getElementById("main-window") .removeAttribute()`, `browserWindow.windowUtils.disableNonTestMouseEvents()`, `lazy.BrowserTestUtils.browserLoaded()`, `lazy.BrowserTestUtils.startLoadingURIString()`, `lazy.Screenshot.init()`, `new Date().toISOString()`, `new Date().toISOString().replace()`, `this._extensionPath .QueryInterface()`, `this._extensionPath .QueryInterface(Ci.nsIFileURL) .file.clone()`, `this._libDir.append()`, `this._performCombo()`, `this.cleanup()`, `this.combos.item()`, `this.loadSets()`, `this.mochitestScope.info()`
- 参照: `Ci.nsIFileURL`, `PathUtils.tempDir`, `Services.appinfo.OS`, `Services.appinfo.appBuildID`, `browserWindow.gBrowser.selectedBrowser`, `sets.length`, `this._extensionPath`, `this._lastCombo`, `this._libDir`, `this.combos`, `this.combos.length`, `this.completedCombos`, `this.currentComboIndex`
- XPCOM: [`nsIFileURL`](../../../../../netwerk/base/nsIFileURL.idl.md) / `Services.appinfo` / `Services.env` / `Services.prefs` / `Services.wm`

## filterRestrictions()
- 位置: L160-172
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/\[([^\]]+)\]$/.exec()`, `match[1] .split()`, `match[1] .split(",") .reduce()`, `name.trim()`, `set.add()`, `setName.slice()`
- 参照: `match.index`

## loadSets()
- 位置: L180-221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `Object.keys()`, `imported[setName].init()`, `restrictions.has()`, `setName.includes()`, `sets.push()`
- 条件付き依存: `if (setName.includes("["))` → `this.filterRestrictions()`
- 条件付き依存: `if (restrictions)` → `[...restrictions].filter()`
- 条件付き依存: `if (restrictions)` → `configurationNames.includes()`
- 参照: `configurationNames.length`, `filteredData.restrictions`, `filteredData.trimmedSetName`, `imported[setName].configurations`, `imported[setName].configurations[config].name`, `incorrectConfigs.length`, `this._libDir`

## cleanup()
- 位置: L223-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`, `Services.wm.getMostRecentWindow()`, `browserWindow.restore()`, `browserWindow.windowUtils.disableNonTestMouseEvents()`, `gBrowser.removeTab()`, `gBrowser.unpinTab()`, `lazy.BrowserTestUtils.startLoadingURIString()`
- 参照: `browserWindow.gBrowser`, `gBrowser.selectedBrowser`, `gBrowser.selectedTab`, `gBrowser.tabs.length`
- XPCOM: `Services.prefs` / `Services.wm`

## _findBoundingBox()
- 位置: L249-325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/gfx/screenmanager;1"] .getService()`, `Cc["@mozilla.org/gfx/screenmanager;1"] .getService(Ci.nsIScreenManager) .screenForRect()`, `Math.max()`, `Math.min()`, `Services.wm.getMostRecentWindow()`, `element.getBoundingClientRect()`, `rect.inflateFixed()`, `rects.push()`
- 条件付き依存: `if (typeof selector == "function")` → `selector()`
- 条件付き依存: `if (!(typeof selector == "function"))` → `browserWindow.document.querySelectorAll()`
- 条件付き依存: `if (rect.width === 0 && rect.height === 0)` → `this.mochitestScope.todo()`
- 条件付き依存: `if (!(!bounds))` → `bounds.union()`
- 参照: `Ci.nsIScreenManager`, `browserWindow.outerHeight`, `browserWindow.outerWidth`, `browserWindow.screenX`, `browserWindow.screenY`, `element.ownerDocument.defaultView`, `elementRect.height`, `elementRect.left`, `elementRect.top`, `elementRect.width`, `elements.length`, `rect.bottom`, `rect.height`, `rect.left`, `rect.right`, `rect.top`, `rect.width`, `selectors.length`, `this.croppingPadding`, `win.mozInnerScreenX`, `win.mozInnerScreenY`
- XPCOM: `nsIScreenManager` / `@mozilla.org/gfx/screenmanager;1` / `Services.wm`

## _do_skip()
- 位置: L327-343
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (todo)` → `this.mochitestScope.todo()`
- 条件付き依存: `if (todo)` → `combo.map(e => e.name).join()`
- 条件付き依存: `if (todo)` → `combo.map()`
- 条件付き依存: `if (!(todo))` → `this.mochitestScope.info()`
- 条件付き依存: `if (!(todo))` → `combo.map(e => e.name).join()`
- 条件付き依存: `if (!(todo))` → `combo.map()`
- 参照: `config.name`, `e.name`

## _performCombo()
- 位置: async L345-459
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `combo .map()`, `combo .map(({ name }) => name) .join()`, `ex.toString()`, `finalSelectors.push()`, `padLeft()`, `this._comboName()`, `this._comboName( combo ).substring()`, `this._findBoundingBox()`, `this._onConfigurationReady()`, `this.mochitestScope.info()`, `this.mochitestScope.ok()`
- 条件付き依存: `if (!this._lastCombo || config !== this._lastCombo[i])` → `this.mochitestScope.info()`
- 条件付き依存: `if (!this._lastCombo || config !== this._lastCombo[i])` → `changeConfig()`
- 条件付き依存: `if (reason)` → `this._do_skip()`
- 条件付き依存: `if (config.verifyConfig)` → `this.mochitestScope.info()`
- 条件付き依存: `if (config.verifyConfig)` → `config.verifyConfig()`
- 条件付き依存: `if (ex.stack)` → `this.mochitestScope.info()`
- 条件付き依存: `if (windowType !== obj.windowType)` → `this.mochitestScope.ok()`
- 参照: `String(this.combos.length).length`, `combo.length`, `config.name`, `config.verifyConfig`, `ex.stack`, `obj.selectors`, `obj.windowType`, `this._lastCombo`, `this.combos.length`, `this.currentComboIndex`

## changeConfig()
- 位置: L358-374
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.race()`, `Promise.race([applyPromise, timeoutPromise]).then()`, `Promise.resolve()`, `config.applyConfig()`, `resolve()`, `setTimeout()`, `this.mochitestScope.info()`
- 参照: `config.name`

## _onConfigurationReady()
- 位置: async L461-481
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.toFileURI()`, `Services.wm.getMostRecentWindow()`, `String()`, `combo.map()`, `combo.map(e => e.name).join()`, `lazy.Screenshot.captureExternal()`, `padLeft()`, `this._comboName()`, `this._cropImage()`, `this._cropImage( browserWindow, PathUtils.toFileURI(imagePath), bounds, rects, imagePath ).catch()`, `this.mochitestScope.info()`
- 参照: `String(this.combos.length).length`, `e.name`, `this.combos.length`, `this.completedCombos`, `this.currentComboIndex`
- XPCOM: `Services.wm`

## _comboName()
- 位置: L483-487
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `combo.reduce()`
- 参照: `b.name`

## _cropImage()
- 位置: async L500-573
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `canvas.getContext()`, `canvas.toBlob()`, `ctx.drawImage()`, `ctx.fillRect()`, `document.createElementNS()`, `fetch()`, `fetch(imageFileURIString).then()`, `fr.readAsArrayBuffer()`, `r.blob()`, `window.createImageBitmap()`
- 参照: `bounds.bottom`, `bounds.height`, `bounds.left`, `bounds.right`, `bounds.top`, `bounds.width`, `canvas.height`, `canvas.width`, `ctx.fillStyle`, `ctx.imageSmoothingEnabled`, `fr.onerror`, `fr.onload`, `img.height`, `img.width`, `rect.bottom`, `rect.height`, `rect.left`, `rect.right`, `rect.top`, `rect.width`

## fr.onload()
- 位置: L564-568
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.write()`, `IOUtils.write(targetPath, new Uint8Array(e.target.result)).then()`
- 参照: `e.target.result`

## findComma()
- 位置: L581-594
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `envVar.length`

## splitEnv()
- 位置: L603-614
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `envVar.slice()`, `envVar.slice(0, commaIndex).trim()`, `envVar.trim()`, `result.push()`, `this.findComma()`

## LazyProduct()
- 位置: L620-635
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`
- 参照: `Object.keys(set).length`, `this.lookupTable`, `this.sets`, `this.sets.length`

## length()
- 位置: L637-643
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.lookupTable`

## item()
- 位置: L645-657
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Object.keys()`
- 参照: `this.lookupTable`, `this.sets`, `this.sets.length`

## padLeft()
- 位置: L660-662
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `String()`, `padding.repeat()`
- 参照: `String(number).length`
