# browser/actors/PluginParent.sys.mjs

source: browser/actors/PluginParent.sys.mjs
source-hash: 498e9622c8bde67f7fb8af7916eca114e44b0f46
lines: 204

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.strings.createBundle()`

## observe()
- 位置: L21-27
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._registerGMPCrash()`

## _registerGMPCrash()
- 位置: L29-60
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `propertyBag.getPropertyAsACString()`, `propertyBag.getPropertyAsAString()`, `propertyBag.getPropertyAsUint32()`, `propertyBag.hasKey()`
- 条件付き依存: `if ( !(propertyBag instanceof Ci.nsIWritablePropertyBag2) || !propertyBag.hasKey("pluginID") || !propertyBag.hasKey("pluginDumpID") || !propertyBag.hasKey("plugi...)` → `console.error()`
- 条件付き依存: `if (pluginDumpID)` → `this.gmpCrashes.set()`
- 条件付き依存: `if (Services.ppmm)` → `Services.ppmm.broadcastAsyncMessage()`
- 参照: `Ci.nsIWritablePropertyBag2`, `Services.ppmm`
- XPCOM: [`nsIWritablePropertyBag2`](../../xpcom/ds/nsIWritablePropertyBag2.idl.md) / `Services.ppmm`

## submitCrashReport()
- 位置: L73-94
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.CrashSubmit.submit()`, `this.getCrashReport()`, `this.gmpCrashes.delete()`
- 条件付き依存: `if (!report)` → `console.error()`
- 条件付き依存: `if (!report)` → `JSON.stringify()`
- 参照: `lazy.CrashSubmit.SUBMITTED_FROM_CRASH_TAB`, `pluginCrashID.pluginID`

## getCrashReport()
- 位置: L96-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.gmpCrashes.get()`
- 参照: `pluginCrashID.pluginID`

## PluginParent.receiveMessage()
- 位置: L102-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `this.showPluginCrashedNotification()`
- 参照: `msg.data.pluginCrashID`, `msg.name`, `this.manager.rootFrameLoader.ownerElement`

## PluginParent.showPluginCrashedNotification()
- 位置: L129-202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PluginManager.getCrashReport()`, `browser.getTabBrowser()`, `browser.getTabBrowser().getNotificationBox()`, `buttons.push()`, `lazy.gNavigatorBundle.GetStringFromName()`, `lazy.gNavigatorBundle.formatStringFromName()`, `notificationBox.appendNotification()`, `notificationBox.getNotificationWithValue()`
- 条件付き依存: `if (AppConstants.MOZ_CRASHREPORTER)` → `lazy.gNavigatorBundle.GetStringFromName()`
- 条件付き依存: `if (AppConstants.MOZ_CRASHREPORTER)` → `buttons.push()`
- 参照: `AppConstants.MOZ_CRASHREPORTER`, `notificationBox.PRIORITY_WARNING_MEDIUM`, `report.pluginName`

## PluginParent.callback()
- 位置: L155-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.reload()`

## callback()
- 位置: L172-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PluginManager.submitCrashReport()`
