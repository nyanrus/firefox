# browser/extensions/formautofill/api.js

source: browser/extensions/formautofill/api.js
source-hash: 7237fdf669a38d13581e2418f6a5cdef6e0f89a4
lines: 214

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetter()`

## insertStyleSheet()
- 位置: L30-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CACHED_STYLESHEETS.has()`, `doc.createProcessingInstruction()`, `doc.insertBefore()`
- 条件付き依存: `if (CACHED_STYLESHEETS.has(domWindow))` → `CACHED_STYLESHEETS.get(domWindow).push()`
- 条件付き依存: `if (CACHED_STYLESHEETS.has(domWindow))` → `CACHED_STYLESHEETS.get()`
- 条件付き依存: `if (!(CACHED_STYLESHEETS.has(domWindow)))` → `CACHED_STYLESHEETS.set()`
- 参照: `doc.documentElement`, `domWindow.document`

## refreshNativeOnnxRuntimeAvailability()
- 位置: L54-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.idleDispatch()`, `EngineProcess.requestIsNativeOnnxRuntimeAvailable()`, `FormAutofillUtils.setNativeOnnxRuntimeAvailable()`
- 参照: `FormAutofillUtils.isMLAutofillEnabled`

## ensureCssLoaded()
- 位置: L70-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CACHED_STYLESHEETS.has()`, `insertStyleSheet()`

## adjustAndCheckFormAutofillPrefs()
- 位置: L83-135
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FormAutofill.isAutofillTypeAvailable()`, `Glean.formautofill.availability.set()`, `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!creditCardAutofillAvailable)` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (!addressAutofillAvailable)` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (!addressAutofillAvailable && !creditCardAutofillAvailable)` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (!addressAutofillAvailable && !creditCardAutofillAvailable)` → `Glean.formautofill.availability.set()`
- 条件付き依存: `if (addressAutofillAvailable)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!(addressAutofillAvailable))` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (creditCardAutofillAvailable)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!(creditCardAutofillAvailable))` → `Services.prefs.clearUserPref()`
- 参照: `AutofillDataTypes.ADDRESS`, `AutofillDataTypes.CREDIT_CARD`
- XPCOM: `Services.prefs`

## onStartup()
- 位置: L136-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AutoCompleteParent.addPopupStateListener()`, `Cc[ "@mozilla.org/addons/addon-manager-startup;1" ].getService()`, `ChromeUtils.registerWindowActor()`, `FormAutofillParent.addMessageObserver()`, `FormAutofillStatus.init()`, `Services.io.newURI()`, `aomStartup.registerChrome()`, `refreshNativeOnnxRuntimeAvailability()`, `resProto.setSubstitution()`, `this.adjustAndCheckFormAutofillPrefs()`
- 参照: `Ci.amIAddonManagerStartup`, `this.chromeHandle`, `this.extension.rootURI`, `this.onFormSubmitted`
- XPCOM: `@mozilla.org/addons/addon-manager-startup;1` / `Services.io`

## this.onFormSubmitted()
- 位置: L163-163
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ensureCssLoaded()`

## onShutdown()
- 位置: L186-212
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AutoCompleteParent.removePopupStateListener()`, `CACHED_STYLESHEETS.get()`, `ChromeUtils.unregisterWindowActor()`, `FormAutofillParent.removeMessageObserver()`, `Services.wm.getEnumerator()`, `cachedStyleSheets.pop()`, `cachedStyleSheets.pop().remove()`, `resProto.setSubstitution()`, `this.chromeHandle.destruct()`
- 参照: `cachedStyleSheets.length`, `this.chromeHandle`
- XPCOM: `Services.wm`
