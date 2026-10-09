# browser/components/extensions/parent/ext-url-overrides.js

source: browser/components/extensions/parent/ext-url-overrides.js
source-hash: 5be610a63750e9444cca4a2005ecb9d09df220e8
lines: 206

## <module>
- 役割: 拡張機能が新規タブ URL を上書きする設定を、ExtensionSettingsStore と新規タブ用の pref に同期させる。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `ExtensionParent.apiManager.on()`

## onObserverAdded()
- 位置: L37-39
- 役割: 新規タブ通知の監視が始まったとき、AboutNewTab.willNotifyUser を真にする。
- 触るとき: 新規タブ通知をいつ出すかを変えるとき。
- 参照: `AboutNewTab.willNotifyUser`

## onObserverRemoved()
- 位置: L40-42
- 役割: 新規タブ通知の監視が終わったとき、AboutNewTab.willNotifyUser を偽にする。
- 触るとき: 通知の監視の終了条件を変えるとき。
- 参照: `AboutNewTab.willNotifyUser`

## beforeDisableAddon()
- 位置: async L43-69
- 役割: 拡張を無効化する前に現在のタブを about:blank へ移し、新規タブ URL が変わった後に元の新規タブ URL を開き直す準備をする。
- 触るとき: 拡張の無効化で現在のタブが閉じられてしまう問題や、無効化後の通知の再表示を調べるとき。
- 呼び出し先: `Services.io.newURI()`, `Services.obs.addObserver()`, `replaceUrlInTab()`
- 参照: `gBrowser.selectedTab`, `win.gBrowser`
- XPCOM: `Services.io` / `Services.obs`

## observe()
- 位置: async L55-65
- 役割: newtab-url-changed を受けてタブを新しい新規タブ URL へ移し、ポップアップを開き直して監視を外す。
- 触るとき: 無効化の後にタブが新規タブへ戻らない問題を調べるとき。
- 呼び出し先: `Services.io.newURI()`, `Services.obs.removeObserver()`, `popup.open()`, `replaceUrlInTab()`
- 参照: `AboutNewTab.newTabURL`
- XPCOM: `Services.io` / `Services.obs`

## setNewTabURL()
- 位置: L73-90
- 役割: 拡張 ID があれば通知を監視し、プライベートブラウジングの可否と拡張制御の pref を設定する。ID が無ければ監視を外して pref を消し、URL があれば AboutNewTab.newTabURL を更新する。
- 触るとき: 新規タブ URL の反映や privateAllowed の扱いを変えるとき、設定変更後に pref がずれる問題を調べるとき。
- 条件付き依存: `if (extensionId)` → `newTabPopup.addObserver()`
- 条件付き依存: `if (extensionId)` → `ExtensionParent.WebExtensionPolicy.getByID()`
- 条件付き依存: `if (extensionId)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!(extensionId))` → `newTabPopup.removeObserver()`
- 条件付き依存: `if (!(extensionId))` → `Services.prefs.clearUserPref()`
- 参照: `AboutNewTab.newTabURL`, `policy.privateBrowsingAllowed`
- XPCOM: `Services.prefs`

## processSettings()
- 位置: async L112-117
- 役割: ExtensionSettingsStore を初期化し、その拡張 ID が新規タブ設定を持っていれば指定の操作(enable, disable, removeSetting)を行う。
- 触るとき: 拡張の無効化、有効化、削除で新規タブ設定が追随しない問題を調べるとき。
- 呼び出し先: `ExtensionSettingsStore.hasSetting()`, `ExtensionSettingsStore.initialize()`
- 条件付き依存: `if (ExtensionSettingsStore.hasSetting(id, STORE_TYPE, NEW_TAB_SETTING_NAME))` → `ExtensionSettingsStore[action]()`

## onDisable()
- 位置: async L120-123
- 役割: 新規タブの通知確認状態を消し、新規タブ設定を無効にする。
- 触るとき: 無効化時に確認済みの通知がどう扱われるかを変えるとき。
- 呼び出し先: `newTabPopup.clearConfirmation()`, `processSettings()`

## onEnabling()
- 位置: async L125-127
- 役割: 新規タブ設定を有効に戻す。
- 触るとき: 拡張を再度有効にしたときに新規タブ URL が戻らない問題を調べるとき。
- 呼び出し先: `processSettings()`

## onUninstall()
- 位置: async L129-133
- 役割: 新規タブの通知確認状態を消し、新規タブ設定を削除する。
- 触るとき: アンインストール時のデータ掃除を変えるとき。TODO にある bug 1438364 の後始末に関わる。
- 呼び出し先: `newTabPopup.clearConfirmation()`, `processSettings()`

## onUpdate()
- 位置: async L135-151
- 役割: 新しいマニフェストに chrome_url_overrides.newtab が無ければ、既存の新規タブ設定を削除する。
- 触るとき: アップデートで新規タブ指定を外した拡張の設定が残る問題を調べるとき。
- 条件付き依存: `if ( !manifest.chrome_url_overrides || !manifest.chrome_url_overrides.newtab )` → `ExtensionSettingsStore.initialize()`
- 条件付き依存: `if ( !manifest.chrome_url_overrides || !manifest.chrome_url_overrides.newtab )` → `ExtensionSettingsStore.hasSetting()`
- 条件付き依存: `if ( ExtensionSettingsStore.hasSetting(id, STORE_TYPE, NEW_TAB_SETTING_NAME) )` → `ExtensionSettingsStore.removeSetting()`
- 参照: `manifest.chrome_url_overrides`, `manifest.chrome_url_overrides.newtab`

## onManifestEntry()
- 位置: async L153-204
- 役割: マニフェストの newtab の URL を解決して設定に追加し、現在値を反映する。プライベートブラウジング許可の追加と削除を監視して pref を更新する。
- 触るとき: 拡張の読み込み時に新規タブ URL がどう決まるかを変えるとき、プライベート許可の pref が権限の変更に追随しない問題を調べるとき。
- 条件付き依存: `if (manifest.chrome_url_overrides.newtab)` → `extension.baseURI.resolve()`
- 条件付き依存: `if (manifest.chrome_url_overrides.newtab)` → `ExtensionSettingsStore.initialize()`
- 条件付き依存: `if (manifest.chrome_url_overrides.newtab)` → `ExtensionSettingsStore.addSetting()`
- 条件付き依存: `if (item)` → `setNewTabURL()`
- 条件付き依存: `if (manifest.chrome_url_overrides.newtab)` → `extension.on()`
- 条件付き依存: `if (manifest.chrome_url_overrides.newtab)` → `permissions.permissions.includes()`
- 条件付き依存: `if ( permissions.permissions.includes("internal:privateBrowsingAllowed") )` → `ExtensionSettingsStore.getSetting()`
- 条件付き依存: `if (item && item.id == extension.id)` → `Services.prefs.setBoolPref()`
- 参照: `AboutNewTab.newTabURL`, `extension.id`, `item.id`, `item.initialValue`, `item.value`, `manifest.chrome_url_overrides.newtab`
- XPCOM: `Services.prefs`
