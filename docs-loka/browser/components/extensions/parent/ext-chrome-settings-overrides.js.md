# browser/components/extensions/parent/ext-chrome-settings-overrides.js

source: browser/components/extensions/parent/ext-chrome-settings-overrides.js
source-hash: b144aca5259106767393bd1e4f140abfa9623ac0
lines: 573

## <module>
- 役割: chrome_settings_overrides API を実装し、拡張の homepage と search_provider の設定を設定ストア・検索サービス・ホームページ設定へ反映する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `ExtensionPreferencesManager.addSetting()`

## beforeDisableAddon()
- 位置: async L48-71
- 役割: ホームページ確認ポップアップで、アドオン無効化前に現在タブを about:blank に逃がし、無効化後にホームページを開き直す。
- 触るとき: 拡張を無効化したときにホームページのタブが閉じられて開き直しに失敗する問題を調べるとき。
- 呼び出し先: `Services.io.newURI()`, `Services.prefs.addObserver()`, `replaceUrlInTab()`
- 参照: `gBrowser.selectedTab`, `win.gBrowser`
- XPCOM: `Services.io` / `Services.prefs`

## prefObserver()
- 位置: async L59-69
- 役割: browser.startup.homepage の変更通知を一度だけ受け、ホームページ読み込み完了後にポップアップを開き直す。
- 触るとき: 無効化後にホームページが開かない、またはポップアップが出ないときに確認する。
- 呼び出し先: `Services.prefs.removeObserver()`, `popup.open()`, `waitForTabLoaded()`, `win.BrowserCommands.home()`
- XPCOM: `Services.prefs`

## handleInitialHomepagePopup()
- 位置: async L79-103
- 役割: 起動時に startup.page が 1 なら読み込み完了を待ち、現在の URL がホームページならポップアップを開き、そうでなければ observer を登録する。
- 触るとき: 起動直後にホームページ確認ポップアップが出ない、または余計に出るときに調べる。
- 呼び出し先: `Services.prefs.getIntPref()`, `homepagePopup.addObserver()`
- 条件付き依存: `if (currentUrl != homepageUrl && currentUrl == "about:blank")` → `waitForTabLoaded()`
- 条件付き依存: `if (currentUrl == homepageUrl && gBrowser.selectedTab == tab)` → `homepagePopup.open()`
- 参照: `gBrowser.currentURI.spec`, `gBrowser.selectedTab`, `windowTracker.topWindow`
- XPCOM: `Services.prefs`

## handleHomepageUrl()
- 位置: async L113-163
- 役割: homepage_override 設定を書き込み、制御下なら非公開ウィンドウ許可と制御フラグを立て、add/remove-permissions の監視を登録する。
- 触るとき: 拡張が homepage を設定したときや、非公開ウィンドウ許可の反映を変えるとき。
- 呼び出し先: `ExtensionPreferencesManager.setSetting()`, `extension.on()`, `permissions.permissions.includes()`
- 条件付き依存: `if (inControl)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (extension.startupReason == "APP_STARTUP")` → `handleInitialHomepagePopup()`
- 条件付き依存: `if (!(extension.startupReason == "APP_STARTUP"))` → `homepagePopup.addObserver()`
- 条件付き依存: `if (permissions.permissions.includes("internal:privateBrowsingAllowed"))` → `ExtensionPreferencesManager.getSetting()`
- 条件付き依存: `if (item && item.id == extension.id)` → `Services.prefs.setBoolPref()`
- 参照: `extension.id`, `extension.privateBrowsingAllowed`, `extension.startupReason`, `item.id`
- XPCOM: `Services.prefs`

## processDefaultSearchSetting()
- 位置: async L173-210
- 役割: 既定検索の設定ストアに対して指定アクション(enable・disable・removeSetting など)を実行し、制御中なら対応する検索エンジンを既定に設定する。
- 触るとき: 拡張のインストール・無効化・削除で既定検索が戻らない、または切り替わらないときに見る。
- 呼び出し先: `ExtensionSettingsStore.getLevelOfControl()`, `ExtensionSettingsStore.getSetting()`, `ExtensionSettingsStore.initialize()`, `ExtensionSettingsStore[action]()`
- 条件付き依存: `if (item && control == "controlled_by_this_extension")` → `SearchService.getEngineByName()`
- 条件付き依存: `if (engine)` → `SearchService.setDefault()`
- 条件付き依存: `if (item && control == "controlled_by_this_extension")` → `Cu.reportError()`
- 参照: `SearchService.CHANGE_REASON.ADDON_INSTALL`, `SearchService.CHANGE_REASON.ADDON_UNINSTALL`, `item.initialValue`, `item.value`

## removeEngine()
- 位置: async L212-218
- 役割: 拡張由来の検索エンジンを SearchService から削除し、失敗時は Cu.reportError で報告するだけにする。
- 触るとき: 拡張削除後に検索エンジンが残るとき、またはエンジン削除の失敗扱いを変えるとき。
- 呼び出し先: `Cu.reportError()`, `SearchService.removeWebExtensionEngine()`

## removeSearchSettings()
- 位置: L220-225
- 役割: 既定検索設定の削除とエンジン削除を並行して実行し、両方の完了を待つ。
- 触るとき: 拡張削除時に検索まわりの後片付けが漏れていないか確認するとき。
- 呼び出し先: `Promise.all()`, `this.processDefaultSearchSetting()`, `this.removeEngine()`

## onUninstall()
- 位置: async L227-238
- 役割: 検索エンジンの登録処理が残っていれば完了を待ってから、検索設定の削除とホームページ確認の取り消しを行う。
- 触るとき: アンインストール時に登録処理と削除が競合する問題を調べるとき。
- 呼び出し先: `Promise.all()`, `homepagePopup.clearConfirmation()`, `pendingSearchSetupTasks.get()`, `this.removeSearchSettings()`
- 条件付き依存: `if (searchStartupPromise)` → `searchStartupPromise.catch()`
- 参照: `Cu.reportError`

## onUpdate()
- 位置: async L240-258
- 役割: 更新後のマニフェストを見て、homepage が無くなれば設定を消し、search_provider が無ければ検索設定を削除し、既定でなければ既定設定だけ外す。
- 触るとき: 拡張の更新後に検索やホームページの設定が残る、または消えすぎるときに確認する。
- 条件付き依存: `if (!manifest?.chrome_settings_overrides?.homepage)` → `ExtensionPreferencesManager.removeSetting()`
- 条件付き依存: `if (!search_provider)` → `this.removeSearchSettings()`
- 条件付き依存: `if (!search_provider.is_default)` → `chrome_settings_overrides.processDefaultSearchSetting()`
- 参照: `manifest?.chrome_settings_overrides?.homepage`, `manifest?.chrome_settings_overrides?.search_provider`, `search_provider.is_default`

## onDisable()
- 位置: async L260-265
- 役割: 無効化時にホームページ確認を取り消し、既定検索設定を disable にしてから検索エンジンを削除する。
- 触るとき: 拡張を無効化した後も検索エンジンや既定検索が残る不具合を調べるとき。
- 呼び出し先: `chrome_settings_overrides.processDefaultSearchSetting()`, `chrome_settings_overrides.removeEngine()`, `homepagePopup.clearConfirmation()`

## onManifestEntry()
- 位置: async L267-305
- 役割: マニフェストの homepage を、無視対象でなければ設定し、search_provider があればエンジン登録を待たずに開始して完了を Map に保持する。
- 触るとき: homepage や search_provider を持つ拡張のインストール・起動時の処理順を変えるとき。
- 条件付き依存: `if (homepageUrl)` → `HomePage.shouldIgnore()`
- 条件付き依存: `if (ignoreHomePageUrl)` → `Glean.homepage.preferenceIgnore.record()`
- 条件付き依存: `if (!(ignoreHomePageUrl))` → `handleHomepageUrl()`
- 条件付き依存: `if (manifest.chrome_settings_overrides.search_provider)` → `this.processSearchProviderManifestEntry().finally()`
- 条件付き依存: `if (manifest.chrome_settings_overrides.search_provider)` → `this.processSearchProviderManifestEntry()`
- 条件付き依存: `if (manifest.chrome_settings_overrides.search_provider)` → `pendingSearchSetupTasks.get()`
- 条件付き依存: `if ( pendingSearchSetupTasks.get(extension.id) === searchStartupPromise )` → `pendingSearchSetupTasks.delete()`
- 条件付き依存: `if ( pendingSearchSetupTasks.get(extension.id) === searchStartupPromise )` → `ExtensionParent.apiManager.emit()`
- 条件付き依存: `if (manifest.chrome_settings_overrides.search_provider)` → `pendingSearchSetupTasks.set()`
- 参照: `extension.id`, `manifest.chrome_settings_overrides.homepage`, `manifest.chrome_settings_overrides.search_provider`

## ensureSetting()
- 位置: async L307-344
- 役割: 既定検索設定が無ければ現在の既定エンジン名で作成し、更新・降格・有効化の起動理由や disable 指定の場合は設定を無効化する。
- 触るとき: 初回インストールや更新で既定検索の設定が意図せず有効になる、または無効にならないときに調べる。
- 呼び出し先: `ExtensionSettingsStore.getSetting()`, `ExtensionSettingsStore.initialize()`
- 条件付き依存: `if (!item)` → `SearchService.getDefault()`
- 条件付き依存: `if (!item)` → `ExtensionSettingsStore.addSetting()`
- 条件付き依存: `if (!item)` → `["ADDON_UPGRADE", "ADDON_DOWNGRADE", "ADDON_ENABLE"].includes()`
- 条件付き依存: `if (disable)` → `ExtensionSettingsStore.disable()`
- 参照: `defaultEngine.name`, `extension.id`, `extension.startupReason`

## promptDefaultSearch()
- 位置: async L346-392
- 役割: 既定エンジンと異なる場合は設定を無効化したうえで、既定変更の確認ポップアップ用に webextension-defaultsearch-prompt 通知を発行する。
- 触るとき: インストール時の既定検索確認の内容や通知の渡し方を変えるとき。
- 呼び出し先: `SearchService.getDefault()`, `SearchService.getEngineByName()`, `Services.obs.notifyObservers()`, `extension.getPreferredIcon()`, `this.ensureSetting()`
- 参照: `defaultEngine.name`, `engine.name`, `extension.id`, `extension.name`, `windowTracker.topWindow?.gBrowser.selectedBrowser`
- XPCOM: `Services.obs`

## respond()
- 位置: async L372-388
- 役割: 確認ポップアップの応答を受け、許可なら既定検索を有効化して既定エンジンを設定し、テスト用の応答通知を発行する。
- 触るとき: 既定検索の確認で許可や拒否を押したときの動作を調べるとき。
- 呼び出し先: `Services.obs.notifyObservers()`
- 条件付き依存: `if (allow)` → `chrome_settings_overrides.processDefaultSearchSetting()`
- 条件付き依存: `if (allow)` → `SearchService.setDefault()`
- 条件付き依存: `if (allow)` → `SearchService.getEngineByName()`
- 参照: `SearchService.CHANGE_REASON.ADDON_INSTALL`, `extension.id`
- XPCOM: `Services.obs`

## processSearchProviderManifestEntry()
- 位置: async L394-437
- 役割: search_provider を処理する。非既定ならエンジン追加のみ、既定なら SearchService 初期化後に上書き可否を判定し、必要に応じて既定設定・エンジン追加・確認を行う。
- 触るとき: search_provider を持つ拡張が既定エンジンを上書きできるかどうか、または確認の出し方を変えるとき。
- 呼び出し先: `SearchService.maybeSetAndOverrideDefault()`, `searchProvider.name.trim()`, `this.addSearchEngine()`
- 条件付き依存: `if (!searchProvider.is_default)` → `this.addSearchEngine()`
- 条件付き依存: `if (!this.extension)` → `Cu.reportError()`
- 条件付き依存: `if (result.canChangeToConfigEngine)` → `this.setDefault()`
- 条件付き依存: `if (extension.startupReason === "ADDON_INSTALL")` → `this.promptDefaultSearch()`
- 条件付き依存: `if (!(extension.startupReason === "ADDON_INSTALL"))` → `this.setDefault()`
- 参照: `SearchService.promiseInitialized`, `extension.startupReason`, `manifest.chrome_settings_overrides.search_provider`, `result.canChangeToConfigEngine`, `result.canInstallEngine`, `searchProvider.is_default`, `this.extension`

## setDefault()
- 位置: async L439-517
- 役割: 起動理由ごとに既定検索の制御状態を確認し、制御中なら該当エンジンを既定にする。設定と実際の既定が食い違う場合は他の設定を無効化して直し、制御可能なら確認を出すか直接有効化する。
- 触るとき: 拡張の更新・有効化で既定検索が切り替わらない、または他の拡張の設定が残るときに確認する。
- 条件付き依存: `if (extension.startupReason === "ADDON_INSTALL")` → `this.ensureSetting()`
- 条件付き依存: `if (extension.startupReason === "ADDON_INSTALL")` → `SearchService.setDefault()`
- 条件付き依存: `if (extension.startupReason === "ADDON_INSTALL")` → `SearchService.getEngineByName()`
- 条件付き依存: `if (!(extension.startupReason === "ADDON_INSTALL"))` → `["ADDON_UPGRADE", "ADDON_DOWNGRADE", "ADDON_ENABLE"].includes()`
- 条件付き依存: `if ( ["ADDON_UPGRADE", "ADDON_DOWNGRADE", "ADDON_ENABLE"].includes( extension.startupReason ) )` → `ExtensionSettingsStore.getLevelOfControl()`
- 条件付き依存: `if ( control === "controlled_by_this_extension" && SearchService.defaultEngine.name !== engineName )` → `ExtensionSettingsStore.getAllSettings()`
- 条件付き依存: `if (setting.value !== SearchService.defaultEngine.name)` → `ExtensionSettingsStore.disable()`
- 条件付き依存: `if ( control === "controlled_by_this_extension" && SearchService.defaultEngine.name !== engineName )` → `ExtensionSettingsStore.getLevelOfControl()`
- 条件付き依存: `if (control === "controlled_by_this_extension")` → `SearchService.setDefault()`
- 条件付き依存: `if (control === "controlled_by_this_extension")` → `SearchService.getEngineByName()`
- 条件付き依存: `if (skipEnablePrompt)` → `chrome_settings_overrides.processDefaultSearchSetting()`
- 条件付き依存: `if (skipEnablePrompt)` → `SearchService.setDefault()`
- 条件付き依存: `if (skipEnablePrompt)` → `SearchService.getEngineByName()`
- 条件付き依存: `if (extension.startupReason == "ADDON_ENABLE")` → `this.promptDefaultSearch()`
- 参照: `SearchService.CHANGE_REASON.ADDON_INSTALL`, `SearchService.defaultEngine.name`, `extension.id`, `extension.startupReason`, `item.value`, `setting.id`, `setting.value`

## addSearchEngine()
- 位置: async L519-528
- 役割: 拡張の検索エンジンを SearchService に追加し、失敗時は報告して false を返す。
- 触るとき: 検索エンジン追加の失敗時の扱いや戻り値を使う呼び出し側を変えるとき。
- 呼び出し先: `Cu.reportError()`, `SearchService.addEngineFromExtension()`

## onPrefsChanged()
- 位置: async L542-561
- 役割: 設定の制御者が拡張になると、ホームページ監視・非公開許可・制御フラグを設定する。制御が戻ると監視を外し、関連 pref を消去する。
- 触るとき: ホームページの制御者が切り替わった際に非公開ウィンドウ許可の状態が合わないときに調べる。
- 条件付き依存: `if (item.id)` → `homepagePopup.addObserver()`
- 条件付き依存: `if (item.id)` → `ExtensionParent.WebExtensionPolicy.getByID()`
- 条件付き依存: `if (!policy)` → `ExtensionPermissions.get()`
- 条件付き依存: `if (!policy)` → `perms.permissions.includes()`
- 条件付き依存: `if (item.id)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!(item.id))` → `homepagePopup.removeObserver()`
- 条件付き依存: `if (!(item.id))` → `Services.prefs.clearUserPref()`
- 参照: `item.id`, `policy.privateBrowsingAllowed`
- XPCOM: `Services.prefs`

## setCallback()
- 位置: L562-571
- 役割: ホームページ値の設定時に一緒に書き込む pref の組(ホームページ、制御フラグ、非公開許可)を返す。非公開許可は常に false にする。
- 触るとき: 拡張がホームページを設定・解除したときに関連 pref の組が揃わない問題を調べるとき。
