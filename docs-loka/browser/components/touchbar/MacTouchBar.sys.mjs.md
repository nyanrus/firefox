# browser/components/touchbar/MacTouchBar.sys.mjs

source: browser/components/touchbar/MacTouchBar.sys.mjs
source-hash: 898e37191b058d89435ed3aba2bc5a0e5e14fadf
lines: 684

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `XPCOMUtils.defineLazyServiceGetter()`

## execCommand()
- 位置: L36-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TouchBarHelper.window.document.getElementById()`
- 条件付き依存: `if (command)` → `command.doCommand()`
- 参照: `TouchBarHelper.window`

## hexToInt()
- 位置: L53-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `hexString.charAt()`, `isNaN()`, `parseInt()`
- 条件付き依存: `if (hexString.charAt(0) == "#")` → `hexString.slice()`

## callback()
- 位置: L81-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `execCommand()`, `lazy.touchBarHelper.unfocusUrlbar()`

## callback()
- 位置: L90-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `execCommand()`, `lazy.touchBarHelper.unfocusUrlbar()`

## callback()
- 位置: L99-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `execCommand()`, `lazy.touchBarHelper.unfocusUrlbar()`

## callback()
- 位置: L108-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `win.BrowserCommands.home()`

## callback()
- 位置: L117-117
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `execCommand()`

## callback()
- 位置: L123-123
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `execCommand()`

## callback()
- 位置: L129-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `execCommand()`

## callback()
- 位置: L135-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `win.SidebarController.toggle()`

## callback()
- 位置: L144-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `execCommand()`

## callback()
- 位置: L150-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `execCommand()`

## callback()
- 位置: L158-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.touchBarHelper.toggleFocusUrlbar()`

## callback()
- 位置: L167-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `execCommand()`

## callback()
- 位置: L185-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.touchBarHelper.insertRestrictionInUrlbar()`
- 参照: `lazy.UrlbarShared.RESTRICT_TOKENS.BOOKMARK`

## callback()
- 位置: L193-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.touchBarHelper.insertRestrictionInUrlbar()`
- 参照: `lazy.UrlbarShared.RESTRICT_TOKENS.OPENPAGE`

## callback()
- 位置: L201-204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.touchBarHelper.insertRestrictionInUrlbar()`
- 参照: `lazy.UrlbarShared.RESTRICT_TOKENS.HISTORY`

## callback()
- 位置: L209-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.touchBarHelper.insertRestrictionInUrlbar()`
- 参照: `lazy.UrlbarShared.RESTRICT_TOKENS.TAG`

## TouchBarHelper.constructor()
- 位置: L241-250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `this.getTouchBarInput()`
- 参照: `this._inputsNotUpdated`, `this._searchPopover`
- XPCOM: `Services.obs`

## TouchBarHelper.destructor()
- 位置: L252-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.removeObserver()`
- 参照: `this._searchPopover`
- XPCOM: `Services.obs`

## TouchBarHelper.activeUrl()
- 位置: L259-268
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `TouchBarHelper.window`, `TouchBarHelper.window.gBrowser`, `tabbrowser.selectedBrowser.currentURI.spec`

## TouchBarHelper.activeTitle()
- 位置: L270-279
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `TouchBarHelper.window`, `TouchBarHelper.window.gBrowser`, `tabbrowser.selectedBrowser.contentTitle`

## TouchBarHelper.allItems()
- 位置: L281-311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/array;1"].createInstance()`, `Object.keys()`, `layoutItems.appendElement()`, `this._inputsNotUpdated.add()`, `this._inputsNotUpdated.clear()`, `this.getTouchBarInput()`, `window.document.documentElement.getAttribute()`
- 参照: `Ci.nsIMutableArray`, `TouchBarHelper.window`, `window.isChromeWindow`
- XPCOM: [`nsIMutableArray`](../../../docshell/shistory/nsISHEntry.idl.md) / `@mozilla.org/array;1`

## TouchBarHelper.window()
- 位置: L313-315
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`

## TouchBarHelper.document()
- 位置: L317-322
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `TouchBarHelper.window`, `TouchBarHelper.window.document`

## TouchBarHelper.isUrlbarFocused()
- 位置: L324-329
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `TouchBarHelper.window`, `TouchBarHelper.window.gURLBar`, `TouchBarHelper.window.gURLBar.focused`

## TouchBarHelper.toggleFocusUrlbar()
- 位置: L331-337
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.isUrlbarFocused)` → `this.unfocusUrlbar()`
- 条件付き依存: `if (!(this.isUrlbarFocused))` → `execCommand()`
- 参照: `this.isUrlbarFocused`

## TouchBarHelper.unfocusUrlbar()
- 位置: L339-344
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TouchBarHelper.window.gURLBar.blur()`
- 参照: `this.isUrlbarFocused`

## TouchBarHelper.baseWindow()
- 位置: L346-352
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TouchBarHelper.window.docShell.treeOwner.QueryInterface()`
- 参照: `Ci.nsIBaseWindow`, `TouchBarHelper.window`
- XPCOM: `nsIBaseWindow`

## TouchBarHelper.getTouchBarInput()
- 位置: L354-392
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `gBuiltInInputs.hasOwnProperty()`, `inputData.hasOwnProperty()`, `this._l10n.formatValue()`, `this._l10n.formatValue(inputData.title).then()`
- 条件付き依存: `if (this._inputsNotUpdated)` → `this._inputsNotUpdated.delete()`
- 条件付き依存: `if (TouchBarHelper.window)` → `lazy.touchBarUpdater.updateTouchBarInputs()`
- 参照: `TouchBarHelper.baseWindow`, `TouchBarHelper.window`, `inputData.title`, `item.title`, `this._inputsNotUpdated`, `this._searchPopover`

## TouchBarHelper._updateTouchBarInputs()
- 位置: L400-420
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `inputs.push()`, `lazy.touchBarUpdater.updateTouchBarInputs()`, `this._inputsNotUpdated.delete()`, `this.getTouchBarInput()`
- 参照: `TouchBarHelper.baseWindow`, `TouchBarHelper.window`, `inputNames.length`, `this._inputsNotUpdated`

## TouchBarHelper.insertRestrictionInUrlbar()
- 位置: L430-452
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TouchBarHelper.window.gURLBar.getAttribute()`, `TouchBarHelper.window.gURLBar.search()`
- 条件付き依存: `if ( TouchBarHelper.window.gURLBar.getAttribute("pageproxystate") != "valid" )` → `TouchBarHelper.window.gURLBar.lastSearchString.trimStart()`
- 条件付き依存: `if ( TouchBarHelper.window.gURLBar.getAttribute("pageproxystate") != "valid" )` → `Object.values(lazy.UrlbarShared.RESTRICT_TOKENS).includes()`
- 条件付き依存: `if ( TouchBarHelper.window.gURLBar.getAttribute("pageproxystate") != "valid" )` → `Object.values()`
- 条件付き依存: `if ( Object.values(lazy.UrlbarShared.RESTRICT_TOKENS).includes( searchString[0] ) )` → `searchString.substring(1).trimStart()`
- 条件付き依存: `if ( Object.values(lazy.UrlbarShared.RESTRICT_TOKENS).includes( searchString[0] ) )` → `searchString.substring()`
- 参照: `TouchBarHelper.window`, `lazy.UrlbarShared.RESTRICT_TOKENS`

## TouchBarHelper.observe()
- 位置: L454-536
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `lazy.touchBarUpdater.showPopover()`, `subject.QueryInterface()`, `this._updateTouchBarInputs()`, `this.destructor()`
- 条件付き依存: `if (subject.QueryInterface(Ci.nsIWebProgress)?.isTopLevel)` → `updatedInputs.push()`
- 条件付き依存: `if (subject.QueryInterface(Ci.nsIWebProgress)?.isTopLevel)` → `data.startsWith()`
- 条件付き依存: `if (!this._searchPopover)` → `this.getTouchBarInput()`
- 参照: `Ci.nsIWebProgress`, `TouchBarHelper.baseWindow`, `TouchBarHelper.window.document.fullscreenElement`, `TouchBarHelper.window.gBrowser.canGoBack`, `TouchBarHelper.window.gBrowser.canGoForward`, `gBuiltInInputs.AddBookmark.image`, `gBuiltInInputs.Back.disabled`, `gBuiltInInputs.Forward.disabled`, `gBuiltInInputs.OpenLocation.callback`, `gBuiltInInputs.OpenLocation.image`, `gBuiltInInputs.OpenLocation.title`, `gBuiltInInputs.ReaderView.disabled`, `helperProto._l10n`, `subject.QueryInterface(Ci.nsIWebProgress)?.isTopLevel`, `this._l10n`, `this._searchPopover`
- XPCOM: [`nsIWebProgress`](../../../dom/interfaces/base/nsIBrowser.idl.md)

## gBuiltInInputs.OpenLocation.callback()
- 位置: L477-479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TouchBarHelper.window.windowUtils.exitFullscreen()`

## gBuiltInInputs.OpenLocation.callback()
- 位置: L484-485
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `execCommand()`

## TouchBarInput.constructor()
- 位置: L569-598
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `hexToInt()`, `input.hasOwnProperty()`
- 条件付き依存: `if (input.children)` → `Object.values()`
- 条件付き依存: `if (input.children)` → `this._children.push()`
- 条件付き依存: `if (childData.title && !localizedStrings[childData.title])` → `toLocalize.push()`
- 条件付き依存: `if (input.children)` → `this._localizeChildren()`
- 参照: `childData.title`, `initializedChild.type`, `input.callback`, `input.children`, `input.color`, `input.disabled`, `input.image`, `input.key`, `input.title`, `input.type`, `this._callback`, `this._children`, `this._color`, `this._disabled`, `this._image`, `this._key`, `this._title`, `this._type`

## TouchBarInput.key()
- 位置: L600-602
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._key`

## TouchBarInput.title()
- 位置: L603-605
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._title`

## TouchBarInput.title()
- 位置: L606-608
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._title`

## TouchBarInput.image()
- 位置: L609-611
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`
- 参照: `this._image`
- XPCOM: `Services.io`

## TouchBarInput.image()
- 位置: L612-614
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._image`

## TouchBarInput.type()
- 位置: L615-617
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._type`

## TouchBarInput.type()
- 位置: L618-620
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._type`

## TouchBarInput.callback()
- 位置: L621-623
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._callback`

## TouchBarInput.callback()
- 位置: L624-626
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._callback`

## TouchBarInput.color()
- 位置: L627-629
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._color`

## TouchBarInput.color()
- 位置: L630-632
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hexToInt()`
- 参照: `this._color`

## TouchBarInput.disabled()
- 位置: L633-635
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._disabled`

## TouchBarInput.disabled()
- 位置: L636-638
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._disabled`

## TouchBarInput.children()
- 位置: L639-650
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/array;1"].createInstance()`, `children.appendElement()`
- 参照: `Ci.nsIMutableArray`, `this._children`
- XPCOM: [`nsIMutableArray`](../../../docshell/shistory/nsISHEntry.idl.md) / `@mozilla.org/array;1`

## TouchBarInput._localizeChildren()
- 位置: async L658-678
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `children.forEach()`, `children.map()`, `helperProto._l10n.formatValues()`, `lazy.touchBarUpdater.updateTouchBarInputs()`
- 参照: `TouchBarHelper.baseWindow`, `child.key`, `child.title`, `children.length`
