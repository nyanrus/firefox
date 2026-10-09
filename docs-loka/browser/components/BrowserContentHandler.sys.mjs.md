# browser/components/BrowserContentHandler.sys.mjs

source: browser/components/BrowserContentHandler.sys.mjs
source-hash: f4a0e1e566c363d5eb1d77e0c021df250d96b3f3
lines: 1793

## <module>
- 役割: コマンドラインや外部からの URL を受けて、ブラウザウィンドウを開く・既存ウィンドウに渡す処理を行う。初回起動時のホームページ上書き(WNP)もここで決める。
- 呼び出し先: `Cc["@mozilla.org/system-alerts-service;1"] ?.getService()`, `Cc["@mozilla.org/system-alerts-service;1"] ?.getService(Ci.nsIAlertsService) ?.QueryInterface()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `XPCOMUtils.defineLazyServiceGetters()`

## canOpenAsSmartWindow()
- 位置: L47-53
- 役割: forcePrivate でなく、スマートウィンドウが既定で開く設定で、かつ利用規約への同意がある場合に true を返す。
- 触るとき: 新規ウィンドウがスマートウィンドウで開くかどうかの条件を変えるとき、またはサインイン済みなのに通常ウィンドウで開くと報告されたときに見る。
- 呼び出し先: `lazy.AIWindow.shouldOpenAsSmartWindow()`
- 参照: `lazy.AIWindowAccountAuth.hasToSConsent`

## shouldLoadURI()
- 位置: L83-91
- 役割: chrome: スキームの URI は外部からのロードを拒否し、それ以外は true を返す。
- 触るとき: 外部から chrome URL を開こうとして拒否される、または逆に通ってしまう問題を調べるときに見る。
- 呼び出し先: `aURI.schemeIs()`, `dump()`

## resolveURIInternal()
- 位置: L93-124
- 役割: 引数をファイル URI として解決し、存在すればそのまま返す。存在しなければ URI の修正(fixup)ヒューリスティックで URI を作り直す。
- 触るとき: コマンドライン引数の解釈が想定と違う、ファイル名が検索語として扱われるときに見る。
- 呼び出し先: `Services.uriFixup.getFixupURIInfo()`, `aCmdLine.resolveURI()`, `console.error()`, `uri.file.exists()`
- 条件付き依存: `if (!(uri instanceof Ci.nsIFileURL))` → `Services.uriFixup.getFixupURIInfo()`
- 参照: `Ci.nsIFileURL`, `Services.uriFixup`, `Services.uriFixup.getFixupURIInfo( aArgument, uriFixup.FIXUP_FLAG_FIX_SCHEME_TYPOS ).preferredURI`, `Services.uriFixup.getFixupURIInfo(aArgument).preferredURI`, `lazy.gSystemPrincipal`, `uriFixup.FIXUP_FLAG_FIX_SCHEME_TYPOS`
- XPCOM: [`nsIFileURL`](../../netwerk/base/nsIFileURL.idl.md) / `Services.uriFixup`

## needHomepageOverride()
- 位置: L157-212
- 役割: 保存された mstone と buildID を現在の値と比べ、新規プロファイル、メジャー更新、同一メジャーのビルド更新のどれかを返す。updateMilestones が真なら記録も更新する。
- 触るとき: 初回起動や更新後にホームページの上書きが出る・出ないを調べるとき、または判定の条件を変えるときに見る。
- 呼び出し先: `Services.prefs.getCharPref()`
- 条件付き依存: `if (savedmstone)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (updateMilestones)` → `Services.prefs.setCharPref()`
- 参照: `Services.appinfo.platformBuildID`, `Services.appinfo.platformVersion`
- XPCOM: `Services.appinfo` / `Services.prefs`

## getPostUpdateOverridePage()
- 位置: L228-263
- 役割: 更新情報の actions に応じて、更新後に開くページを決める。silent や showURL の欠如、ポリシー、Nimbus の URL、update の openURL の順に判定する。
- 触るとき: 更新後の What's New ページが出ない、または想定外の URL が出るときに見る。
- 呼び出し先: `Services.policies.isAllowed()`, `actions.includes()`, `update.QueryInterface()`, `update.getProperty()`
- 参照: `Ci.nsIWritablePropertyBag`
- XPCOM: [`nsIWritablePropertyBag`](../../xpcom/ds/nsIWritablePropertyBag.idl.md) / `Services.policies`

## openBrowserWindow()
- 位置: L294-410
- 役割: 初回起動なら起動用の空ウィンドウを置き換え、そうでなければ新規ウィンドウを作る。URL の指定形式に応じて引数を組み、BrowserWindowTracker.openWindow に渡す。
- 触るとき: 新しいウィンドウを開く経路(ホームページ、URL、スマートウィンドウ、プライベート)の引数を変えるときに見る。
- 呼び出し先: `canOpenAsSmartWindow()`, `gBrowserContentHandler.getFeatures()`, `lazy.BrowserWindowTracker.openWindow()`
- 条件付き依存: `if (isStartup)` → `gBrowserContentHandler.getFirstWindowArgs()`
- 条件付き依存: `if (!(isStartup))` → `gBrowserContentHandler.getNewWindowArgs()`
- 条件付き依存: `if (!(!urlOrUrlList))` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(urlOrUrlList))` → `triggeringPrincipal.equals()`
- 条件付き依存: `if (Array.isArray(urlOrUrlList))` → `Cc["@mozilla.org/array;1"].createInstance()`
- 条件付き依存: `if (Array.isArray(urlOrUrlList))` → `urlOrUrlList.forEach()`
- 条件付き依存: `if (Array.isArray(urlOrUrlList))` → `Cc["@mozilla.org/supports-string;1"].createInstance()`
- 条件付き依存: `if (Array.isArray(urlOrUrlList))` → `uriArray.appendElement()`
- 条件付き依存: `if (!(Array.isArray(urlOrUrlList)))` → `Cc["@mozilla.org/hash-property-bag;1"].createInstance()`
- 条件付き依存: `if (!(Array.isArray(urlOrUrlList)))` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (forceAllowDataURI)` → `extraOptions.setPropertyAsBool()`
- 条件付き依存: `if (isStartup)` → `gBrowserContentHandler.replaceStartupWindow()`
- 条件付き依存: `if (!urlOrUrlList)` → `Cc["@mozilla.org/supports-string;1"].createInstance()`
- 条件付き依存: `if (openAsSmart)` → `Cc["@mozilla.org/array;1"].createInstance()`
- 条件付き依存: `if (openAsSmart)` → `array.appendElement()`
- 条件付き依存: `if (args.length > 1)` → `Cc["@mozilla.org/supports-string;1"].createInstance()`
- 条件付き依存: `if (!(!urlOrUrlList))` → `Cc["@mozilla.org/array;1"].createInstance()`
- 条件付き依存: `if (!(!urlOrUrlList))` → `args.forEach()`
- 条件付き依存: `if (!(!urlOrUrlList))` → `array.appendElement()`
- 参照: `Ci.nsICommandLine.STATE_INITIAL_LAUNCH`, `Ci.nsIMutableArray`, `Ci.nsISupportsString`, `Ci.nsIWritablePropertyBag2`, `args.length`, `cmdLine.state`, `lazy.gSystemPrincipal`, `sstring.data`, `string.data`
- XPCOM: [`nsICommandLine`](nsIBrowserHandler.idl.md) / [`nsIMutableArray`](../../docshell/shistory/nsISHEntry.idl.md) / [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md) / [`nsIWritablePropertyBag2`](../../xpcom/ds/nsIWritablePropertyBag2.idl.md) / `@mozilla.org/array;1` / `@mozilla.org/hash-property-bag;1` / `@mozilla.org/supports-string;1`

## openPreferences()
- 位置: L412-414
- 役割: about:preferences を開くウィンドウを openBrowserWindow で作る。
- 触るとき: --preferences や旧 chrome 引数で設定画面が開かないときに見る。
- 呼び出し先: `openBrowserWindow()`
- 参照: `lazy.gSystemPrincipal`

## doSearch()
- 位置: async L416-438
- 役割: 空のウィンドウを開き、起動完了を待ってから SearchUIUtils.loadSearch で検索を実行する。
- 触るとき: --search の検索結果が開かない、またはプライベートで検索されてしまうときに見る。
- 呼び出し先: `lazy.BrowserUtils.promiseObserved()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.SearchUIUtils.loadSearch()`, `openBrowserWindow()`
- 参照: `console.error`, `lazy.PrivateBrowsingUtils.isInTemporaryAutoStartMode`, `lazy.gSystemPrincipal`, `win.gBrowser.selectedBrowser.policyContainer`

## spinForLastUpdateInstalled()
- 位置: L440-442
- 役割: UpdateManager.lastUpdateInstalled() の結果をイベントループを回して同期的に取り出す。
- 触るとき: 更新情報の取得が同期で必要な箇所で値が取れないときに見る。
- 呼び出し先: `lazy.UpdateManager.lastUpdateInstalled()`, `spinResolve()`

## spinForUpdateInstalledAtStartup()
- 位置: L444-446
- 役割: UpdateManager.updateInstalledAtStartup() の結果を spinResolve で同期的に取り出す。
- 触るとき: 起動時に更新が適用されたかの判定を変えるとき、または結果が遅れて得られないときに見る。
- 呼び出し先: `lazy.UpdateManager.updateInstalledAtStartup()`, `spinResolve()`

## spinResolve()
- 位置: L448-475
- 役割: Promise でなければ値をそのまま返し、Promise なら完了まで spinEventLoopUntil で待って結果か例外を返す。
- 触るとき: 同期呼び出しが固まる、または Forcefully exited の例外が出るときに見る。
- 呼び出し先: `Services.tm.spinEventLoopUntil()`, `promise .catch()`, `promise .catch(e => { error = e; }) .then()`
- XPCOM: `Services.tm`

## nsBrowserContentHandler()
- 位置: L477-482
- 役割: グローバルの BrowserContentHandler を一つだけ作る。最初に作られた this を返すコンストラクター。
- 触るとき: ハンドラーが二重に作られる、またはシングルトンの前提を崩すときに見る。

## bch_handle()
- 位置: L494-736
- 役割: コマンドラインのフラグ(kiosk、browser、new-window、new-tab、data、chrome、preferences、private-window、search、private、setDefaultBrowser、first-startup、file など)を順に処理し、対応するウィンドウを開く。
- 触るとき: 起動オプションを追加・変更するとき、または特定のフラグが効かないと報告されたときに見る。
- 呼び出し先: `cmdLine.handleFlag()`, `cmdLine.handleFlagWithParam()`, `console.error()`, `handURIToExistingBrowser()`, `openBrowserWindow()`, `resolveURIInternal()`, `shouldLoadURI()`, `uri.schemeIs()`
- 条件付き依存: `if ( cmdLine.handleFlag("kiosk", false) || cmdLine.handleFlagWithParam("kiosk-monitor", false) )` → `Glean.browserStartup.kioskMode.set()`
- 条件付き依存: `if (cmdLine.handleFlag("disable-pinch", false))` → `Services.prefs.getDefaultBranch()`
- 条件付き依存: `if (cmdLine.handleFlag("disable-pinch", false))` → `defaults.setBoolPref()`
- 条件付き依存: `if (cmdLine.handleFlag("disable-pinch", false))` → `Services.prefs.lockPref()`
- 条件付き依存: `if (cmdLine.handleFlag("disable-pinch", false))` → `defaults.setCharPref()`
- 条件付き依存: `if (cmdLine.handleFlag("browser", false))` → `openBrowserWindow()`
- 条件付き依存: `if (!uri.schemeIs("data"))` → `console.error()`
- 条件付き依存: `if (cmdLine.state == Ci.nsICommandLine.STATE_INITIAL_LAUNCH)` → `openBrowserWindow()`
- 条件付き依存: `if (!(cmdLine.state == Ci.nsICommandLine.STATE_INITIAL_LAUNCH))` → `handURIToExistingBrowser()`
- 条件付き依存: `if ( chromeParam == "chrome://browser/content/pref/pref.xul" || chromeParam == "chrome://browser/content/preferences/preferences.xul" )` → `openPreferences()`
- 条件付き依存: `if (!( chromeParam == "chrome://browser/content/pref/pref.xul" || chromeParam == "chrome://browser/content/preferences/preferences.xul" ))` → `resolveURIInternal()`
- 条件付き依存: `if (!( chromeParam == "chrome://browser/content/pref/pref.xul" || chromeParam == "chrome://browser/content/preferences/preferences.xul" ))` → `isLocal()`
- 条件付き依存: `if (isLocal(resolvedURI))` → `this.getFeatures()`
- 条件付き依存: `if (isLocal(resolvedURI))` → `Cc["@mozilla.org/array;1"].createInstance()`
- 条件付き依存: `if (isLocal(resolvedURI))` → `argArray.appendElement()`
- 条件付き依存: `if (isLocal(resolvedURI))` → `Services.ww.openWindow()`
- 条件付き依存: `if (!(isLocal(resolvedURI)))` → `dump()`
- 条件付き依存: `if (!( chromeParam == "chrome://browser/content/pref/pref.xul" || chromeParam == "chrome://browser/content/preferences/preferences.xul" ))` → `console.error()`
- 条件付き依存: `if (cmdLine.handleFlag("preferences", false))` → `openPreferences()`
- 条件付き依存: `if (!lazy.PrivateBrowsingUtils.enabled)` → `Services.io.newURI()`
- 条件付き依存: `if (!(!lazy.PrivateBrowsingUtils.enabled))` → `resolveURIInternal()`
- 条件付き依存: `if (privateWindowParam)` → `handURIToExistingBrowser()`
- 条件付き依存: `if (cmdLine.handleFlag("private-window", false))` → `openBrowserWindow()`
- 条件付き依存: `if (searchParam)` → `doSearch()`
- 条件付き依存: `if ( cmdLine.handleFlag("private", false) && lazy.PrivateBrowsingUtils.enabled )` → `lazy.PrivateBrowsingUtils.enterTemporaryAutoStartMode()`
- 条件付き依存: `if (cmdLine.state == Ci.nsICommandLine.STATE_INITIAL_LAUNCH)` → `Services.wm.getMostRecentWindow()`
- 条件付き依存: `if (win)` → `win.docShell.QueryInterface()`
- 条件付き依存: `if (cmdLine.handleFlag("setDefaultBrowser", false))` → `lazy.ShellService.setDefaultBrowser(true).catch()`
- 条件付き依存: `if (cmdLine.handleFlag("setDefaultBrowser", false))` → `lazy.ShellService.setDefaultBrowser()`
- 条件付き依存: `if (cmdLine.handleFlag("setDefaultBrowser", false))` → `console.error()`
- 条件付き依存: `if (cmdLine.handleFlag("first-startup", false))` → `needHomepageOverride()`
- 条件付き依存: `if (cmdLine.handleFlag("first-startup", false))` → `lazy.FirstStartup.init()`
- 条件付き依存: `if (fileParam)` → `cmdLine.resolveFile()`
- 条件付き依存: `if (fileParam)` → `Services.io.newFileURI()`
- 条件付き依存: `if (fileParam)` → `openBrowserWindow()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `cmdLine.getArgument()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `param.match()`
- 条件付き依存: `if (param.match(/^\? /))` → `cmdLine.removeArguments()`
- 条件付き依存: `if (param.match(/^\? /))` → `param.substr()`
- 条件付き依存: `if (param.match(/^\? /))` → `doSearch()`
- 参照: `AppConstants.platform`, `Ci.nsIBrowserDOMWindow.OPEN_DEFAULTWINDOW`, `Ci.nsIBrowserDOMWindow.OPEN_NEWTAB`, `Ci.nsICommandLine.STATE_INITIAL_LAUNCH`, `Ci.nsILoadContext`, `Ci.nsIMutableArray`, `Cr.NS_ERROR_INVALID_ARG`, `cmdLine.length`, `cmdLine.preventDefault`, `cmdLine.state`, `e.result`, `fileURI.spec`, `lazy.PrivateBrowsingUtils.enabled`, `lazy.gSystemPrincipal`, `resolvedInfo.principal`, `resolvedInfo.uri`, `resolvedURI.spec`, `uri.spec`, `win.docShell.QueryInterface(Ci.nsILoadContext).usePrivateBrowsing`
- XPCOM: [`nsIBrowserDOMWindow`](../../dom/interfaces/base/nsIBrowserDOMWindow.idl.md) / [`nsICommandLine`](nsIBrowserHandler.idl.md) / [`nsILoadContext`](../../docshell/base/nsILoadContext.idl.md) / [`nsIMutableArray`](../../docshell/shistory/nsISHEntry.idl.md) / `@mozilla.org/array;1` / `Services.io` / `Services.prefs` / `Services.wm` / `Services.ww`

## isLocal()
- 位置: L587-593
- 役割: --chrome で渡された URI の最内 URI のスキームが chrome、file、resource のいずれかなら true を返す。
- 触るとき: --chrome で開けるローカル URL の範囲を変えるときに見る。
- 呼び出し先: `localSchemes.has()`
- 条件付き依存: `if (uri instanceof Ci.nsINestedURI)` → `uri.QueryInterface()`
- 参照: `Ci.nsINestedURI`, `uri.QueryInterface(Ci.nsINestedURI).innerMostURI`, `uri.scheme`
- XPCOM: [`nsINestedURI`](../../netwerk/base/nsINestedURI.idl.md)

## helpInfo()
- 位置: L738-765
- 役割: コマンドライン用のヘルプ文字列を、プラットフォームに応じた設定画面のフラグ名を含めて返す。
- 触るとき: 新しいフラグを追加したとき、ヘルプの表示を揃えるときに見る。
- 参照: `AppConstants.platform`

## defaultArgs()
- 位置: L769-771
- 役割: getNewWindowArgs() の結果を返す。nsIBrowserHandler の既定引数。
- 触るとき: 既定の起動引数が browser-init 側の判定と食い違うときに見る。
- 呼び出し先: `this.getNewWindowArgs()`

## getNewWindowArgs()
- 位置: L778-820
- 役割: LaterRun の URL、browser.startup.page で選んだホームページ、about:home の代わりのスマートウィンドウ URL を '|' で連結し、空なら about:blank を返す。
- 触るとき: 新規ウィンドウで開く URL の組み立てを変えるとき、またはスマートウィンドウ時の URL 置換を調べるときに見る。
- 呼び出し先: `canOpenAsSmartWindow()`, `console.error()`, `lazy.LaterRun.getURL()`, `prefb.getIntPref()`
- 条件付き依存: `if (choice == 1 || choice == 3)` → `lazy.HomePage.get()`
- 参照: `Services.prefs`, `lazy.AIWindow.initialStartupURL`
- XPCOM: `Services.prefs`

## getFirstWindowArgs()
- 位置: L826-1142
- 役割: 初回起動時の最初のウィンドウで開く URL を決める。一時的なプライベートモードならプライベートの空白ページ、更新後や新規プロファイルなら上書きページを、通常のページより前に並べる。
- 触るとき: 起動時に最初に出るページ(WNP、ようこそ、ホーム)が想定と違うとき、または上書きの条件を変えるときに見る。
- 呼び出し先: `Services.prefs.getCharPref()`, `needHomepageOverride()`, `prefb.getBoolPref()`, `prefb.prefHasUserValue()`, `this.getNewWindowArgs()`
- 条件付き依存: `if (override != OVERRIDE_NONE)` → `Services.urlFormatter.formatURLPref()`
- 条件付き依存: `if (override != OVERRIDE_NONE)` → `lazy.LaterRun.enable()`
- 条件付き依存: `if (override != OVERRIDE_NONE)` → `lazy.SessionStartup.isAutomaticRestoreEnabled()`
- 条件付き依存: `if (override != OVERRIDE_NONE)` → `spinForLastUpdateInstalled()`
- 条件付き依存: `if (override != OVERRIDE_NONE)` → `Services.vc.compare()`
- 条件付き依存: `if (override != OVERRIDE_NONE)` → `Services.prefs.getCharPref()`
- 条件付き依存: `if (override != OVERRIDE_NONE)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (nimbusOverrideUrl && versionMatch)` → `Services.io.newURI()`
- 条件付き依存: `if (nimbusOverrideUrl && versionMatch)` → `nimbusOverrideUrl.split("|")[0].trim()`
- 条件付き依存: `if (nimbusOverrideUrl && versionMatch)` → `nimbusOverrideUrl.split()`
- 条件付き依存: `if (nimbusOverrideUrl && versionMatch)` → `[ "www.mozilla.org", "www.mozilla.com", "www.firefox.com", ].includes()`
- 条件付き依存: `if (nimbusOverrideUrl && versionMatch)` → `console.error()`
- 条件付き依存: `if ( update && Services.vc.compare(update.appVersion, old_mstone) > 0 )` → `getPostUpdateOverridePage()`
- 条件付き依存: `if (overridePage || (versionMatch && disableWNP))` → `nimbusWNPFeature .ready() .then()`
- 条件付き依存: `if (overridePage || (versionMatch && disableWNP))` → `nimbusWNPFeature .ready()`
- 条件付き依存: `if (overridePage || (versionMatch && disableWNP))` → `nimbusWNPFeature.recordExposureEvent()`
- 条件付き依存: `if ( update && Services.vc.compare(update.appVersion, old_mstone) > 0 )` → `lazy.LaterRun.enable()`
- 条件付き依存: `if (override != OVERRIDE_NONE)` → `lazy.UpdateManager.updateInstalledAtStartup().then()`
- 条件付き依存: `if (override != OVERRIDE_NONE)` → `lazy.UpdateManager.updateInstalledAtStartup()`
- 条件付き依存: `if (updateInstalledAtStartup)` → `Glean.update.previousChannel.set()`
- 条件付き依存: `if (updateInstalledAtStartup)` → `Glean.update.previousVersion.set()`
- 条件付き依存: `if (updateInstalledAtStartup)` → `Glean.update.previousBuildId.set()`
- 条件付き依存: `if (updateInstalledAtStartup)` → `GleanPings.update.submit()`
- 条件付き依存: `if (override != OVERRIDE_NONE)` → `lazy.AsyncShutdown.profileBeforeChange.addBlocker()`
- 条件付き依存: `if (override != OVERRIDE_NONE)` → `overridePage.replace()`
- 条件付き依存: `if (override != OVERRIDE_NONE)` → `spinForUpdateInstalledAtStartup()`
- 条件付き依存: `if (updateInstalledAtStartup)` → `lazy.LaterRun.enable()`
- 条件付き依存: `if (overridePage == "" && prefb.prefHasUserValue(ONCE_PREF))` → `JSON.parse()`
- 条件付き依存: `if (overridePage == "" && prefb.prefHasUserValue(ONCE_PREF))` → `prefb.getStringPref()`
- 条件付き依存: `if (overridePage == "" && prefb.prefHasUserValue(ONCE_PREF))` → `Services.urlFormatter.formatURL()`
- 条件付き依存: `if (overridePage == "" && prefb.prefHasUserValue(ONCE_PREF))` → `Date.now()`
- 条件付き依存: `if (!(Date.now() > expire))` → `url .split("|") .map()`
- 条件付き依存: `if (!(Date.now() > expire))` → `url .split()`
- 条件付き依存: `if (!(Date.now() > expire))` → `URL.parse()`
- 条件付き依存: `if (!parsed)` → `console.error()`
- 条件付き依存: `if (!(Date.now() > expire))` → `ONCE_DOMAINS.has()`
- 条件付き依存: `if (!(Date.now() > expire))` → `Services.eTLD.getBaseDomainFromHost()`
- 条件付き依存: `if (feature_id && slug)` → `lazy.NimbusFeatures[feature_id]?.recordExposureEvent()`
- 条件付き依存: `if (overridePage != url)` → `console.error()`
- 条件付き依存: `if (overridePage == "" && prefb.prefHasUserValue(ONCE_PREF))` → `console.error()`
- 条件付き依存: `if (overridePage == "" && prefb.prefHasUserValue(ONCE_PREF))` → `prefb.clearUserPref()`
- 条件付き依存: `if (!additionalPage)` → `lazy.LaterRun.getURL()`
- 参照: `Services.appinfo.version`, `Services.prefs`, `lazy.LaterRun.ENABLE_REASON_NEW_PROFILE`, `lazy.LaterRun.ENABLE_REASON_UPDATE_APPLIED`, `lazy.NimbusFeatures`, `lazy.NimbusFeatures.whatsNewPage`, `lazy.PrivateBrowsingUtils.isInTemporaryAutoStartMode`, `parsed.host`, `parsed?.protocol`, `progress.payloadCreated`, `progress.updateFetched`, `update.appVersion`, `update.platformVersion`, `updateInstalledAtStartup.channel`, `uri.host`, `uri.scheme`
- XPCOM: `Services.appinfo` / `Services.eTLD` / `Services.io` / `Services.prefs` / `Services.urlFormatter` / `Services.vc`

## fetchState()
- 位置: L1034-1034
- 役割: AsyncShutdown の blocker が終了時に状態として送る progress を返す。
- 触るとき: 更新 ping の送信が終了時に止まったとき、どこまで進んだかを確かめるときに見る。

## bch_features()
- 位置: L1146-1187
- 役割: --width、--height、--left、--top と一時的なプライベートモードに応じたウィンドウの feature 文字列を作り、キャッシュする。最初のウィンドウでは suppressanimation を足す。
- 触るとき: 新しいウィンドウの大きさや位置の指定が効かないとき、またはプライベートの feature を変えるときに見る。
- 条件付き依存: `if (cmdLine)` → `cmdLine.handleFlagWithParam()`
- 条件付き依存: `if (this.mFeatures === null)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (this.mFeatures === null)` → `Services.wm.getMostRecentWindow()`
- 参照: `lazy.PrivateBrowsingUtils.isInTemporaryAutoStartMode`, `this.mFeatures`
- XPCOM: `Services.prefs` / `Services.wm`

## kiosk()
- 位置: L1189-1191
- 役割: キオスクモードで起動したかを返す。
- 触るとき: キオスク判定を参照する箇所の挙動を確かめるときに見る。

## majorUpgrade()
- 位置: L1193-1195
- 役割: メジャーバージョンの更新があったかを返す getter。
- 触るとき: メジャー更新後の処理が呼ばれる条件を確かめるときに見る。

## majorUpgrade()
- 位置: L1197-1199
- 役割: メジャーバージョン更新のフラグを設定する setter。
- 触るとき: メジャー更新の判定を外部から書き換える箇所を調べるときに見る。

## firstRunProfile()
- 位置: L1201-1203
- 役割: 新規プロファイルの初回起動かを返す getter。
- 触るとき: 新規プロファイル向けの処理が走るかを確かめるときに見る。

## firstRunProfile()
- 位置: L1205-1207
- 役割: 新規プロファイルの初回起動フラグを設定する setter。
- 触るとき: 新規プロファイルの判定を外部から書き換える箇所を調べるときに見る。

## bch_handleContent()
- 位置: L1211-1232
- 役割: Web ナビゲーションで扱えない種類の内容なら例外を投げ、扱える場合は既存のブラウザでその URI を開いてロードを取り消す。
- 触るとき: 外部から開かれたコンテンツの種類ごとの扱いを変えるとき、または特定のファイルを開けないときに見る。
- 呼び出し先: `Cc["@mozilla.org/webnavigation-info;1"].getService()`, `handURIToExistingBrowser()`, `request.QueryInterface()`, `request.cancel()`, `webNavInfo.isTypeSupported()`
- 参照: `Ci.nsIBrowserDOMWindow.OPEN_DEFAULTWINDOW`, `Ci.nsIChannel`, `Ci.nsIWebNavigationInfo`, `Components.Exception`, `Cr.NS_BINDING_ABORTED`, `Cr.NS_ERROR_WONT_HANDLE_CONTENT`, `request.URI`, `request.loadInfo.triggeringPrincipal`
- XPCOM: [`nsIBrowserDOMWindow`](../../dom/interfaces/base/nsIBrowserDOMWindow.idl.md) / [`nsIChannel`](../../docshell/base/nsIDocShell.idl.md) / [`nsIWebNavigationInfo`](../../docshell/base/nsIWebNavigationInfo.idl.md) / `@mozilla.org/webnavigation-info;1`

## replaceStartupWindow()
- 位置: L1237-1278
- 役割: 起動時に BrowserGlue が作った空白ウィンドウを、プライベート設定と Windows のタスクバー情報を反映して本来のブラウザウィンドウに置き換える。
- 触るとき: 起動時の空白ウィンドウが残る、またはプライベートの表示が違うときに見る。
- 呼び出し先: `Services.wm.getMostRecentWindow()`
- 条件付き依存: `if (win)` → `win.document.documentElement.removeAttribute()`
- 条件付き依存: `if (forcePrivate)` → `win.docShell.QueryInterface()`
- 条件付き依存: `if (forcePrivate)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( AppConstants.platform == "win" && Services.prefs.getBoolPref( "browser.privateWindowSeparation.enabled", true ) )` → `lazy.WinTaskbar.setGroupIdForWindow()`
- 条件付き依存: `if ( AppConstants.platform == "win" && Services.prefs.getBoolPref( "browser.privateWindowSeparation.enabled", true ) )` → `lazy.WindowsUIUtils.setWindowIconFromExe()`
- 条件付き依存: `if ( AppConstants.platform == "win" && Services.prefs.getBoolPref( "browser.privateWindowSeparation.enabled", true ) )` → `Services.dirsvc.get()`
- 条件付き依存: `if (win)` → `ChromeUtils.addProfilerMarker()`
- 条件付き依存: `if (win)` → `lazy.BrowserWindowTracker.registerOpeningWindow()`
- 参照: `AppConstants.BROWSER_CHROME_URL`, `AppConstants.platform`, `Ci.nsIFile`, `Ci.nsILoadContext`, `Services.dirsvc.get("XREExeF", Ci.nsIFile).path`, `lazy.WinTaskbar.defaultPrivateGroupId`, `win.arguments`, `win.docShell.QueryInterface(Ci.nsILoadContext).usePrivateBrowsing`, `win.location`, `win.openTime`
- XPCOM: [`nsIFile`](shell/nsIShellService.idl.md) / [`nsILoadContext`](../../docshell/base/nsILoadContext.idl.md) / `Services.dirsvc` / `Services.prefs` / `Services.wm`

## bch_validate()
- 位置: L1281-1295
- 役割: リモートからの --url 指定に余計な引数があるか、firefoxurl: スキームを含むときは中断させる。
- 触るとき: リモート起動の URL 指定が拒否されるときに、その条件を確かめるときに見る。
- 呼び出し先: `cmdLine.findFlag()`
- 条件付き依存: `if ( urlFlagIdx > -1 && cmdLine.state == Ci.nsICommandLine.STATE_REMOTE_EXPLICIT )` → `cmdLine.getArgument()`
- 条件付き依存: `if ( urlFlagIdx > -1 && cmdLine.state == Ci.nsICommandLine.STATE_REMOTE_EXPLICIT )` → `/firefoxurl(-[a-f0-9]+)?:/i.test()`
- 条件付き依存: `if ( cmdLine.length != urlFlagIdx + 2 || /firefoxurl(-[a-f0-9]+)?:/i.test(urlParam) )` → `Components.Exception()`
- 参照: `Ci.nsICommandLine.STATE_REMOTE_EXPLICIT`, `Cr.NS_ERROR_ABORT`, `cmdLine.length`, `cmdLine.state`
- XPCOM: [`nsICommandLine`](nsIBrowserHandler.idl.md)

## handURIToExistingBrowser()
- 位置: L1299-1357
- 役割: 既存のブラウザウィンドウに URI を渡し、無ければ保留中のウィンドウを待つ、それも無ければ新規ウィンドウを開く。
- 触るとき: 外部リンクがどのウィンドウで開くかを変えるとき、または既存ウィンドウに渡らないと報告されたときに見る。
- 呼び出し先: `lazy.BrowserWindowTracker.getPendingWindow()`, `lazy.BrowserWindowTracker.getTopWindow()`, `openBrowserWindow()`, `shouldLoadURI()`
- 条件付き依存: `if (navWin)` → `openInWindow()`
- 条件付き依存: `if (pending)` → `pending.then()`
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `uri.spec`

## openInWindow()
- 位置: L1311-1322
- 役割: 渡されたウィンドウの browserDOMWindow.openURI を外部からの読み込みとして呼び出す。
- 触るとき: 既存ウィンドウへの URI 受け渡しの引数を変えるときに見る。
- 呼び出し先: `browserDOMWindow.openURI()`
- 参照: `Ci.nsIBrowserDOMWindow.OPEN_EXTERNAL`, `Ci.nsIBrowserDOMWindow.OPEN_FORCE_ALLOW_DATA_URI`
- XPCOM: [`nsIBrowserDOMWindow`](../../dom/interfaces/base/nsIBrowserDOMWindow.idl.md)

## maybeRecordToHandleTelemetry()
- 位置: L1370-1404
- 役割: 渡された URI が登録済みのファイル拡張子かスキームなら、その種類を、そうでなければ <other> として、起動または呼び出しの計測を増やす。
- 触るとき: ファイルやプロトコルの telemetry 分類を変えるとき、または計測値が想定と違うときに見る。
- 条件付き依存: `if (uri instanceof Ci.nsIFileURL)` → `uri.fileExtension.toLowerCase()`
- 条件付き依存: `if (uri instanceof Ci.nsIFileURL)` → `registeredExtensions.has()`
- 条件付き依存: `if (registeredExtensions.has(extension))` → `counter[extension].add()`
- 条件付き依存: `if (!(registeredExtensions.has(extension)))` → `counter[".<other extension>"].add()`
- 条件付き依存: `if (uri)` → `uri.scheme.toLowerCase()`
- 条件付き依存: `if (uri)` → `registeredSchemes.has()`
- 条件付き依存: `if (registeredSchemes.has(scheme))` → `counter[scheme].add()`
- 条件付き依存: `if (!(registeredSchemes.has(scheme)))` → `counter["<other protocol>"].add()`
- 参照: `Ci.nsIFileURL`, `Glean.osEnvironment.invokedToHandle`, `Glean.osEnvironment.launchedToHandle`
- XPCOM: [`nsIFileURL`](../../netwerk/base/nsIFileURL.idl.md)

## maybeRecordSearchActivationTelemetry()
- 位置: L1416-1433
- 役割: Windows で bing.com の /search を開いたとき、起動か新規タブかの別に検索の活性化を計測する。
- 触るとき: Windows の検索活性化の計測条件を変えるとき、または値が増えないときに見る。
- 呼び出し先: `Services.eTLD.getBaseDomain()`
- 条件付き依存: `if ( Services.eTLD.getBaseDomain(uri) == "bing.com" && uri.filePath == "/search" )` → `Glean.browserEngagement.windowsStartSearchActivationCount[ isLaunch ? "startup" : "new_tab" ].add()`
- 参照: `AppConstants.platform`, `Glean.browserEngagement.windowsStartSearchActivationCount`, `uri.filePath`
- XPCOM: `Services.eTLD`

## nsDefaultCommandLineHandler()
- 位置: L1435-1435
- 役割: 既定のコマンドライン処理ハンドラー。通常の URL 引数、通知、既定ウィンドウを扱う。
- 触るとき: 引数なし起動や URL 引数の処理がどのハンドラーで行われるかを確かめるときに見る。

## handleNotification()
- 位置: L1447-1503
- 役割: Windows のトーストから来た通知起動だけを扱う。通知の ID を取り、非同期の処理に渡して、扱ったかを返す。
- 触るとき: Windows の通知クリックから起動したときの処理を変えるときに見る。
- 呼び出し先: `cmdLine.handleFlagWithParam()`, `console.error()`, `this.handleNotificationImpl()`, `this.handleNotificationImpl(cmdLine, tag, notificationData, alertService) .catch()`
- 条件付き依存: `if (!alertService)` → `console.error()`
- 条件付き依存: `if (cmdLine.state == Ci.nsICommandLine.STATE_INITIAL_LAUNCH)` → `Services.startup.enterLastWindowClosingSurvivalArea()`
- 条件付き依存: `if (cmdLine.state == Ci.nsICommandLine.STATE_INITIAL_LAUNCH)` → `Services.startup.exitLastWindowClosingSurvivalArea()`
- 参照: `AppConstants.platform`, `Ci.nsICommandLine.STATE_INITIAL_LAUNCH`, `cmdLine.state`, `lazy.gWindowsAlertsService`
- XPCOM: [`nsICommandLine`](nsIBrowserHandler.idl.md) / `Services.startup`

## handleNotificationImpl()
- 位置: async L1515-1618
- 役割: 通知を Windows のアラートサービスで処理し、Web 通知なら origin のハンドラーに返す。Messaging System の通知なら SpecialMessageActions でアクションを実行する。
- 触るとき: 通知のクリックで正しいページやアクションが開かないときに見る。
- 呼び出し先: `JSON.parse()`, `alertService.handleWindowsTag()`, `console.error()`, `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (notificationData?.opaqueRelaunchData)` → `JSON.parse()`
- 条件付き依存: `if (notificationData?.opaqueRelaunchData)` → `console.error()`
- 条件付き依存: `if (notificationData?.privilegedName)` → `Glean.browserLaunchedToHandle.systemNotification.record()`
- 条件付き依存: `if (cmdLine.state == Ci.nsICommandLine.STATE_INITIAL_LAUNCH)` → `openBrowserWindow()`
- 条件付き依存: `if (cmdLine.state == Ci.nsICommandLine.STATE_INITIAL_LAUNCH)` → `lazy.BrowserUtils.promiseObserved()`
- 条件付き依存: `if (!tagWasHandled && origin && !opaqueRelaunchData)` → `Services.scriptSecurityManager.createContentPrincipalFromOrigin()`
- 条件付き依存: `if (!tagWasHandled && origin && !opaqueRelaunchData)` → `Cc["@mozilla.org/notification-handler;1"].getService()`
- 条件付き依存: `if (!tagWasHandled && origin && !opaqueRelaunchData)` → `handler.respondOnClick()`
- 条件付き依存: `if (opaqueRelaunchData && winForAction)` → `Services.tm.dispatchToMainThread()`
- 条件付き依存: `if (opaqueRelaunchData && winForAction)` → `lazy.SpecialMessageActions.handleAction()`
- 参照: `Ci.nsICommandLine.STATE_INITIAL_LAUNCH`, `Ci.nsINotificationHandler`, `cmdLine.state`, `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `lazy.gSystemPrincipal`, `notificationData.opaqueRelaunchData`, `notificationData.privilegedName`, `notificationData?.action`, `notificationData?.launchUrl`, `notificationData?.opaqueRelaunchData`, `notificationData?.origin`, `notificationData?.privilegedName`, `winForAction.gBrowser`
- XPCOM: [`nsICommandLine`](nsIBrowserHandler.idl.md) / [`nsINotificationHandler`](../../dom/notification/nsINotificationHandler.idl.md) / `@mozilla.org/notification-handler;1` → `mozilla::dom::notification::NotificationHandler` (dom/notification/components.conf) / `Services.scriptSecurityManager` / `Services.tm`

## dch_handle()
- 位置: L1621-1789
- 役割: 既定のハンドラー。Windows と macOS のプロファイル未選択の扱い、--url、--screenshot、URI の引数、ウィンドウが無いときの新規ウィンドウや Windows のタブレットモードを処理する。
- 触るとき: ファイルや URL を渡したときに開く先が違う、または何も開かないときに見る。
- 呼び出し先: `cmdLine.findFlag()`, `cmdLine.getArgument()`, `cmdLine.handleFlagWithParam()`, `console.error()`, `curarg.match()`, `principalList.push()`, `resolveURIInternal()`, `this.handleNotification()`, `urilist.push()`
- 条件付き依存: `if ( cmdLine.state == Ci.nsICommandLine.STATE_INITIAL_LAUNCH && Services.startup.wasSilentlyStarted )` → `Services.startup.enterLastWindowClosingSurvivalArea()`
- 条件付き依存: `if ( cmdLine.state == Ci.nsICommandLine.STATE_INITIAL_LAUNCH && Services.startup.wasSilentlyStarted )` → `Services.obs.addObserver()`
- 条件付き依存: `if (!this._haveProfile)` → `Services.dirsvc.get()`
- 条件付き依存: `if (!this._haveProfile)` → `cmdLine.handleFlagWithParam()`
- 条件付き依存: `if (launchedWithArg_osint)` → `cmdLine.handleFlag()`
- 条件付き依存: `if (launchedWithArg_osint)` → `maybeRecordSearchActivationTelemetry()`
- 条件付き依存: `if (launchedWithArg_osint)` → `maybeRecordToHandleTelemetry()`
- 条件付き依存: `if (cmdLine.findFlag("screenshot", true) != -1)` → `lazy.HeadlessShell.handleCmdLineArgs()`
- 条件付き依存: `if (cmdLine.findFlag("screenshot", true) != -1)` → `urilist.filter(shouldLoadURI).map()`
- 条件付き依存: `if (cmdLine.findFlag("screenshot", true) != -1)` → `urilist.filter()`
- 条件付き依存: `if (curarg.match(/^-/))` → `console.error()`
- 条件付き依存: `if (!(curarg.match(/^-/)))` → `resolveURIInternal()`
- 条件付き依存: `if (!(curarg.match(/^-/)))` → `urilist.push()`
- 条件付き依存: `if (!(curarg.match(/^-/)))` → `principalList.push()`
- 条件付き依存: `if (!(curarg.match(/^-/)))` → `console.error()`
- 条件付き依存: `if ( cmdLine.state != Ci.nsICommandLine.STATE_INITIAL_LAUNCH && urilist.length == 1 )` → `handURIToExistingBrowser()`
- 条件付き依存: `if (urilist.length)` → `urilist.filter(shouldLoadURI).map()`
- 条件付き依存: `if (urilist.length)` → `urilist.filter()`
- 条件付き依存: `if (URLlist.length)` → `openBrowserWindow()`
- 条件付き依存: `if ( AppConstants.platform == "win" && cmdLine.state != Ci.nsICommandLine.STATE_INITIAL_LAUNCH && lazy.WindowsUIUtils.inWin10TabletMode )` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (win)` → `win.focus()`
- 条件付き依存: `if (!cmdLine.preventDefault)` → `openBrowserWindow()`
- 条件付き依存: `if (!(!cmdLine.preventDefault))` → `Services.wm.getMostRecentWindow()`
- 条件付き依存: `if (win)` → `win.close()`
- 参照: `AppConstants.platform`, `Ci.nsIBrowserDOMWindow.OPEN_DEFAULTWINDOW`, `Ci.nsICommandLine.STATE_INITIAL_LAUNCH`, `Ci.nsIFile`, `Services.startup.wasSilentlyStarted`, `URLlist.length`, `cmdLine.length`, `cmdLine.preventDefault`, `cmdLine.state`, `lazy.WindowsUIUtils.inWin10TabletMode`, `lazy.gSystemPrincipal`, `this._haveProfile`, `u.spec`, `urilist.length`
- XPCOM: [`nsIBrowserDOMWindow`](../../dom/interfaces/base/nsIBrowserDOMWindow.idl.md) / [`nsICommandLine`](nsIBrowserHandler.idl.md) / [`nsIFile`](shell/nsIShellService.idl.md) / `Services.dirsvc` / `Services.obs` / `Services.startup` / `Services.wm`

## windowOpenObserver()
- 位置: L1646-1649
- 役割: silent 起動で最初のウィンドウが開いたら、生存領域を抜ける1回限りのオブザーバー。
- 触るとき: サイレント起動で終了してしまう、またはウィンドウが開いても残り続けるときに見る。
- 呼び出し先: `Services.obs.removeObserver()`, `Services.startup.exitLastWindowClosingSurvivalArea()`
- XPCOM: `Services.obs` / `Services.startup`
