# browser/base/content/browser-captivePortal.js

source: browser/base/content/browser-captivePortal.js
source-hash: 4f332f0beb3507c82f5bc64d3f02f871023fcbe3
lines: 407

## <module>
- 役割: キャプティブポータル検出時のバナー表示、ログイン用タブの管理、解消時の後始末を担う CaptivePortalWatcher を定義する。
- 呼び出し先: `Date.now()`

## _captivePortalNotification()
- 位置: L32-36
- 役割: ポータル通知バナーを値で検索し、表示中なら返す。
- 触るとき: バナーの重複表示や表示状態の判定を変えるとき。
- 呼び出し先: `gNotificationBox.getNotificationWithValue()`
- 参照: `this.PORTAL_NOTIFICATION_VALUE`

## canonicalURL()
- 位置: L38-40
- 役割: キャプティブポータル判定用の正規 URL を pref から読む。
- 触るとき: ログイン後にリダイレクト先として扱う URL の判定を変えるとき。
- 呼び出し先: `Services.prefs.getCharPref()`
- XPCOM: `Services.prefs`

## _browserBundle()
- 位置: L42-47
- 役割: browser.properties の文字列バンドルを初回アクセス時に生成してキャッシュする。
- 触るとき: バナーやボタンの文言を変えるとき、または文字列の読み込み先を変えるとき。
- 呼び出し先: `Services.strings.createBundle()`
- 参照: `this._browserBundle`
- XPCOM: `Services.strings`

## init()
- 位置: L49-81
- 役割: オブザーバーを登録し、起動時点のポータル状態に応じて検出や再チェックを開始する。
- 触るとき: 起動時の検出タイミングや、ポータル関連の通知トピックを追加・変更するとき。
- 呼び出し先: `Cc["@mozilla.org/network/captive-portal-service;1"].getService()`, `Services.obs.addObserver()`, `XPCOMUtils.defineLazyPreferenceGetter()`
- 条件付き依存: `if (this._cps.state == this._cps.LOCKED_PORTAL)` → `this._captivePortalDetected()`
- 条件付き依存: `if (BrowserWindowTracker.windowCount == 1)` → `this.ensureCaptivePortalTab()`
- 参照: `BrowserWindowTracker.windowCount`, `Ci.nsICaptivePortalService`, `this._cps`, `this._cps.LOCKED_PORTAL`, `this._cps.UNKNOWN`, `this._cps.state`, `this._delayedRecheckPending`
- XPCOM: [`nsICaptivePortalService`](../../../netwerk/base/nsICaptivePortalService.idl.md) / `@mozilla.org/network/captive-portal-service;1` / `Services.obs`

## uninit()
- 位置: L83-89
- 役割: init で登録したオブザーバーを外し、保留中の遅延検出を取り消す。
- 触るとき: ウィンドウ終了時の後始末を変えるとき。
- 呼び出し先: `Services.obs.removeObserver()`, `this._cancelDelayedCaptivePortal()`
- XPCOM: `Services.obs`

## delayedStartup()
- 位置: L91-96
- 役割: 初回描画後に保留されていたポータル再チェックを実行する。
- 触るとき: 起動直後のネットワーク要求のタイミングを変えるとき。
- 条件付き依存: `if (this._delayedRecheckPending)` → `this._cps.recheckCaptivePortal()`
- 参照: `this._delayedRecheckPending`

## observe()
- 位置: L98-113
- 役割: ポータルのログイン・中断・成功・遅延処理完了の各トピックを対応する処理に振り分ける。
- 触るとき: ポータル関連のオブザーバートピックの扱いを変えるとき。
- 呼び出し先: `this._cancelDelayedCaptivePortal()`, `this._captivePortalDetected()`, `this._captivePortalGone()`

## onLocationChange()
- 位置: L115-153
- 役割: ログイン用タブが正規 URL に遷移したとき、次のティックでそのタブを閉じる。
- 触るとき: ログイン完了後のタブの自動クローズ条件を調べたり変えたりするとき。
- 呼び出し先: `Services.io.newURI()`, `Services.tm.dispatchToMainThread()`, `tab.linkedBrowser.currentURI.equalsExceptRef()`, `this._previousCaptivePortalTab.get()`
- 条件付き依存: `if ( tab && (tab.linkedBrowser.currentURI.equalsExceptRef(canonicalURI) || tab.linkedBrowser.currentURI.host == "support.mozilla.org") && (this._cps.state == thi...)` → `gBrowser.removeTab()`
- 参照: `tab.linkedBrowser`, `tab.linkedBrowser.currentURI.host`, `this._cps.UNKNOWN`, `this._cps.UNLOCKED_PORTAL`, `this._cps.state`, `this._previousCaptivePortalTab`, `this.canonicalURL`
- XPCOM: `Services.io` / `Services.tm`

## _captivePortalDetected()
- 位置: L155-197
- 役割: ポータル検出時に正規 URL へ https-only の例外権限を付与し、必要ならフォーカス待ちにしてバナーを出す。
- 触るとき: 検出時の権限付与や、ウィンドウが非アクティブな時の扱いを変えるとき。
- 呼び出し先: `BrowserWindowTracker.getTopWindow()`, `PrivateBrowsingUtils.isWindowPrivate()`, `Services.io.newURI()`, `Services.perms.addFromPrincipal()`, `Services.scriptSecurityManager.createContentPrincipal()`, `this._showNotification()`, `win?.document.documentElement.getAttribute()`
- 条件付き依存: `if (win != Services.focus.activeWindow)` → `window.addEventListener()`
- 条件付き依存: `if (win != Services.focus.activeWindow)` → `Services.obs.addObserver()`
- 参照: `Ci.nsIPermissionManager.ALLOW_ACTION`, `Ci.nsIPermissionManager.EXPIRE_SESSION`, `Services.focus.activeWindow`, `gBrowser.contentPrincipal.userContextId`, `this._delayedCaptivePortalDetectedInProgress`, `this.canonicalURL`
- XPCOM: [`nsIPermissionManager`](../../../netwerk/base/nsIPermissionManager.idl.md) / `Services.focus` / `Services.io` / `Services.obs` / `Services.perms` / `Services.scriptSecurityManager`

## _delayedCaptivePortalDetected()
- 位置: L204-240
- 役割: ウィンドウ活性化後に再チェックを要求し、短時間内にまだポータルなら login タブを開く。
- 触るとき: フォーカス復帰時のポータル再確認とタブ自動表示の条件を変えるとき。
- 呼び出し先: `Date.now()`, `Services.obs.addObserver()`, `Services.obs.notifyObservers()`, `this._cps.recheckCaptivePortal()`, `window.document.documentElement.getAttribute()`
- 参照: `this._delayedCaptivePortalDetectedInProgress`, `this._waitingForRecheck`
- XPCOM: `Services.obs`

## observer()
- 位置: L223-238
- 役割: 再チェック完了通知を受けて、遅延検出時間内ならログイン用タブを開く。
- 触るとき: 再チェック完了後にタブを開くかどうかの判定を変えるとき。
- 呼び出し先: `Date.now()`, `Services.obs.removeObserver()`
- 条件付き依存: `if (time <= this.PORTAL_RECHECK_DELAY_MS)` → `this.ensureCaptivePortalTab()`
- 参照: `this.PORTAL_RECHECK_DELAY_MS`, `this._cps.LOCKED_PORTAL`, `this._cps.state`, `this._waitingForRecheck`
- XPCOM: `Services.obs`

## _captivePortalGone()
- 位置: L242-276
- 役割: ポータル解消時にバナーを消し、表示時間を Glean に記録し、ログイン用タブを閉じる。
- 触るとき: ポータル解消時の計測項目やタブの後始末を変えるとき。
- 呼び出し先: `Date.now()`, `Math.round()`, `Services.io.newURI()`, `tab.linkedBrowser.currentURI.equalsExceptRef()`, `this._cancelDelayedCaptivePortal()`, `this._captivePortalTab.get()`, `this._removeNotification()`
- 条件付き依存: `if (aSuccess)` → `Glean.networking.captivePortalBannerDisplayTime.success.add()`
- 条件付き依存: `if (!(aSuccess))` → `Glean.networking.captivePortalBannerDisplayTime.abort.add()`
- 条件付き依存: `if ( tab && tab.linkedBrowser && (tab.linkedBrowser.currentURI.equalsExceptRef(canonicalURI) || tab.linkedBrowser.currentURI.host == "support.mozilla.org") )` → `gBrowser.removeTab()`
- 参照: `tab.linkedBrowser`, `tab.linkedBrowser.currentURI.host`, `this._bannerDisplayTime`, `this._captivePortalTab`, `this._previousCaptivePortalTab`, `this.canonicalURL`
- XPCOM: `Services.io`

## _cancelDelayedCaptivePortal()
- 位置: L278-284
- 役割: 保留中の遅延検出を解除し、オブザーバーと activate リスナーを外す。
- 触るとき: 遅延検出の取り消し処理を調べるとき。
- 条件付き依存: `if (this._delayedCaptivePortalDetectedInProgress)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (this._delayedCaptivePortalDetectedInProgress)` → `window.removeEventListener()`
- 参照: `this._delayedCaptivePortalDetectedInProgress`
- XPCOM: `Services.obs`

## handleEvent()
- 位置: async L286-317
- 役割: activate で遅延検出を進め、TabSelect でログインタブ選択時にバナーのボタンの表示を切り替える。
- 触るとき: ウィンドウのフォーカスやタブ切り替えとバナー表示の連動を変えるとき。
- 呼び出し先: `n.buttonContainer.querySelector()`, `this._captivePortalTab.get()`, `this._delayedCaptivePortalDetected()`
- 参照: `aEvent.type`, `button.style.visibility`, `doc.defaultView.gBrowser.selectedTab`, `tab.ownerDocument`, `this._captivePortalNotification`, `this._captivePortalTab`, `this._notificationPromise`

## _showNotification()
- 位置: L319-373
- 役割: ポータル用の情報バナーとログインページボタンを追加し、閉じ方を計測する。
- 触るとき: バナーの文言、ボタン、優先度、計測を変えるとき。
- 呼び出し先: `Date.now()`, `Glean.networking.captivePortalBannerDisplayed.add()`, `gBrowser.tabContainer.addEventListener()`, `gNotificationBox.appendNotification()`, `this._browserBundle.GetStringFromName()`
- 参照: `gNotificationBox.PRIORITY_INFO_MEDIUM`, `this.PORTAL_NOTIFICATION_VALUE`, `this._bannerDisplayTime`, `this._captivePortalNotification`, `this._notificationPromise`

## callback()
- 位置: L332-337
- 役割: バナーのボタン押下時にログイン用タブを開き、通知を閉じないよう true を返す。
- 触るとき: バナーのボタン動作を変えるとき。
- 呼び出し先: `this.ensureCaptivePortalTab()`

## closeHandler()
- 位置: L345-360
- 役割: バナーが閉じられた時に表示時間を記録し、removed 時に TabSelect リスナーを外す。
- 触るとき: バナーの閉じる操作の計測や後始末を変えるとき。
- 呼び出し先: `gBrowser.tabContainer.removeEventListener()`
- 条件付き依存: `if (aEventName == "dismissed")` → `Math.round()`
- 条件付き依存: `if (aEventName == "dismissed")` → `Date.now()`
- 条件付き依存: `if (aEventName == "dismissed")` → `Glean.networking.captivePortalBannerDisplayTime.dismiss.add()`
- 参照: `this._bannerDisplayTime`

## _removeNotification()
- 位置: L375-381
- 役割: 表示中のポータルバナーがあれば閉じる。
- 触るとき: バナーを閉じる条件を変えるとき。
- 呼び出し先: `n.close()`
- 参照: `n.parentNode`, `this._captivePortalNotification`

## ensureCaptivePortalTab()
- 位置: L383-405
- 役割: 既存のログインタブがなければ正規 URL を新規タブで開き、そのタブを選択する。
- 触るとき: ログイン用タブの生成や再利用の条件を変えるとき。
- 条件付き依存: `if (this._captivePortalTab)` → `this._captivePortalTab.get()`
- 条件付き依存: `if (!tab || tab.closing || !tab.parentNode)` → `gBrowser.addWebTab()`
- 条件付き依存: `if (!tab || tab.closing || !tab.parentNode)` → `Services.scriptSecurityManager.createNullPrincipal()`
- 条件付き依存: `if (!tab || tab.closing || !tab.parentNode)` → `Cu.getWeakReference()`
- 参照: `gBrowser.contentPrincipal.userContextId`, `gBrowser.selectedTab`, `tab.closing`, `tab.parentNode`, `this._captivePortalTab`, `this._previousCaptivePortalTab`, `this.canonicalURL`
- XPCOM: `Services.scriptSecurityManager`
