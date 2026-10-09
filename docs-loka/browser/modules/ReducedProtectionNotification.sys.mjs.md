# browser/modules/ReducedProtectionNotification.sys.mjs

source: browser/modules/ReducedProtectionNotification.sys.mjs
source-hash: 7bc93bfa4c28751054d6dcd94e4f019ccded11ca
lines: 201

## <module>
- 役割: プライベートブラウズでトラッカーを止めたタブを再読み込みしたとき、保護を弱めて再読み込みすることを勧める案内バーを出す。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## observePref()
- 位置: L28-43
- 役割: 専用 pref の変化を監視し、有効になれば init、無効になれば uninit を呼ぶ。起動時に有効なら init を呼ぶ。
- 触るとき: pref を切り替えても案内の有効・無効が追随しない問題を調べるとき。
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.getBoolPref(PREF, false))` → `this.init()`
- 条件付き依存: `if (!(Services.prefs.getBoolPref(PREF, false)))` → `this.uninit()`
- 参照: `this._prefObserved`
- XPCOM: `Services.prefs`

## init()
- 位置: L45-69
- 役割: 永続でないプライベートウィンドウに進捗リスナーを付けるコールバックを EveryWindow に登録する。
- 触るとき: 新しく開いたプライベートウィンドウで案内が出ない問題を調べるとき。
- 呼び出し先: `lazy.EveryWindow.registerCallback()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if ( lazy.PrivateBrowsingUtils.isWindowPrivate(win) && !lazy.PrivateBrowsingUtils.permanentPrivateBrowsing )` → `win.gBrowser?.addTabsProgressListener()`
- 条件付き依存: `if ( lazy.PrivateBrowsingUtils.isWindowPrivate(win) && !lazy.PrivateBrowsingUtils.permanentPrivateBrowsing )` → `win.gBrowser?.removeTabsProgressListener()`
- 参照: `lazy.PrivateBrowsingUtils.permanentPrivateBrowsing`, `this._initialized`

## uninit()
- 位置: L71-80
- 役割: EveryWindow の登録を解除し、ブロック記録・保留中のタブ・表示済みホストの記録を空にする。
- 触るとき: 機能を無効にした後に古い状態が残る問題を調べるとき。
- 呼び出し先: `lazy.EveryWindow.unregisterCallback()`
- 参照: `this._blockedTrackers`, `this._initialized`, `this._pendingNotification`, `this._shownHosts`

## markUserReload()
- 位置: L82-89
- 役割: ブロックされたトラッカーがあり、そのホストで未表示なら、そのブラウザーを保留にする。
- 触るとき: ユーザーの再読み込みで案内を出す条件を変えるとき。
- 呼び出し先: `this._blockedTrackers.has()`
- 条件付き依存: `if (this._blockedTrackers.has(aBrowser))` → `this._shownHosts.get(aBrowser)?.has()`
- 条件付き依存: `if (this._blockedTrackers.has(aBrowser))` → `this._shownHosts.get()`
- 条件付き依存: `if (host && !this._shownHosts.get(aBrowser)?.has(host))` → `this._pendingNotification.add()`
- 参照: `aBrowser.currentURI?.host`

## onContentBlockingEvent()
- 位置: L91-98
- 役割: トップレベルでトラッカーのブロックを示す状態が来たら、そのブラウザーをブロック済みとして記録する。
- 触るとき: トラッカーをブロックしたと判定する条件を変えるとき。
- 条件付き依存: `if (aEvent & Ci.nsIWebProgressListener.STATE_BLOCKED_TRACKING_CONTENT)` → `this._blockedTrackers.add()`
- 参照: `Ci.nsIWebProgressListener.STATE_BLOCKED_TRACKING_CONTENT`, `aWebProgress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## onLocationChange()
- 位置: L100-120
- 役割: トップレベルの遷移で同一ドキュメント内の移動は無視し、再読み込みかつ保留とブロック記録が両方あれば showNotification を呼ぶ。
- 触るとき: 再読み込み後に案内が出ない、または余分に出る問題を調べるとき。
- 呼び出し先: `this._blockedTrackers.delete()`, `this._pendingNotification.delete()`
- 条件付き依存: `if ( aFlags & Ci.nsIWebProgressListener.LOCATION_CHANGE_RELOAD && isPending && blockedTrackers )` → `this.showNotification(aBrowser).catch()`
- 条件付き依存: `if ( aFlags & Ci.nsIWebProgressListener.LOCATION_CHANGE_RELOAD && isPending && blockedTrackers )` → `this.showNotification()`
- 条件付き依存: `if ( aFlags & Ci.nsIWebProgressListener.LOCATION_CHANGE_RELOAD && isPending && blockedTrackers )` → `console.error()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_RELOAD`, `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `aWebProgress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## showNotification()
- 位置: async L122-199
- 役割: 同じホストで未表示なら、タブの通知枠に案内を追加し、表示したホストを記録する。
- 触るとき: 案内の文言やボタン、表示回数の制限(ホストごとに1回)を変えるとき。
- 呼び出し先: `Glean.privacyReducedPageProtection.bannerShown.add()`, `aBrowser.getTabBrowser()`, `notificationBox.appendNotification()`, `notificationBox.getNotificationWithValue()`, `tabbrowser.getNotificationBox()`, `this._shownHosts.get()`, `this._shownHosts.get(aBrowser).add()`, `this._shownHosts.get(aBrowser)?.has()`, `this._shownHosts.has()`
- 条件付き依存: `if (!this._shownHosts.has(aBrowser))` → `this._shownHosts.set()`
- 参照: `aBrowser.currentURI`, `currentURI.host`, `notificationBox.PRIORITY_INFO_LOW`

## callback()
- 位置: L152-155
- 役割: 「今後表示しない」ボタン: 計測を送り、専用 pref を false にする。
- 触るとき: 案内を恒久的に止める設定の動きを変えるとき。
- 呼び出し先: `Glean.privacyReducedPageProtection.disableClicked.add()`, `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## callback()
- 位置: L159-188
- 役割: 「再読み込み」ボタン: 計測を送り、ブラウジングコンテキストのトラッキング防止関連の scoped pref を全て false にしてから再読み込みする。
- 触るとき: 再読み込み時にどの保護を外すかを変えるとき。
- 呼び出し先: `Glean.privacyReducedPageProtection.reloadClicked.add()`, `aBrowser.reload()`
- 条件付き依存: `if (scopedPrefs)` → `scopedPrefs.setBoolPrefScoped()`
- 参照: `Ci.nsIScopedPrefs .PRIVACY_TRACKINGPROTECTION_CONTENT_CRYPTOMINING_ENABLED`, `Ci.nsIScopedPrefs .PRIVACY_TRACKINGPROTECTION_CONTENT_EMAILTRACKING_ENABLED`, `Ci.nsIScopedPrefs .PRIVACY_TRACKINGPROTECTION_CONTENT_FINGERPRINTING_ENABLED`, `Ci.nsIScopedPrefs .PRIVACY_TRACKINGPROTECTION_CONTENT_SOCIALTRACKING_ENABLED`, `Ci.nsIScopedPrefs .PRIVACY_TRACKINGPROTECTION_CRYPTOMINING_ENABLED`, `Ci.nsIScopedPrefs .PRIVACY_TRACKINGPROTECTION_EMAILTRACKING_ENABLED`, `Ci.nsIScopedPrefs .PRIVACY_TRACKINGPROTECTION_FINGERPRINTING_ENABLED`, `Ci.nsIScopedPrefs .PRIVACY_TRACKINGPROTECTION_SOCIALTRACKING_ENABLED`, `Ci.nsIScopedPrefs.PRIVACY_TRACKINGPROTECTION_CONTENT_ENABLED`, `Ci.nsIScopedPrefs.PRIVACY_TRACKINGPROTECTION_ENABLED`, `aBrowser.browsingContext`, `aBrowser.browsingContext.scopedPrefs`
- XPCOM: [`nsIScopedPrefs`](../../toolkit/components/antitracking/scopedprefs/nsIScopedPrefs.idl.md)
