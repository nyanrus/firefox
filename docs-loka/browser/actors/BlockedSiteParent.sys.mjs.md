# browser/actors/BlockedSiteParent.sys.mjs

source: browser/actors/BlockedSiteParent.sys.mjs
source-hash: 7f348199bc402fdc016d9bc47d967daf2953e8e0
lines: 299

## <module>
- 役割: セーフブラウジングでブロックされたページの親側アクター。警告バーの表示、理由別の文言と報告リンク、警告を無視して進む処理を担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `Services.strings.createBundle()`

## SafeBrowsingNotificationBox.constructor()
- 位置: L25-35
- 役割: タブの現在ドメインを記録し、進行リスナーを登録して警告バーを表示する。
- 触るとき: 警告バーを出すタイミングや、ドメイン移動時の後始末を変えるときに見る。
- 呼び出し先: `browser.addProgressListener()`, `this.#getDomainForComparison()`, `this.show()`
- 参照: `Ci.nsIWebProgress.NOTIFY_LOCATION`, `browser.currentURI`, `this._currentURIBaseDomain`, `this.browser`
- XPCOM: [`nsIWebProgress`](../../dom/interfaces/base/nsIBrowser.idl.md)

## SafeBrowsingNotificationBox.show()
- 位置: async L37-59
- 役割: 同じ値の既存通知を消してから、重大度の高い警告通知を表示し、リダイレクトでも残るよう永続化する。
- 触るとき: 警告バーの見た目、ボタン、重複表示の扱いを変えるときに見る。
- 呼び出し先: `gBrowser.getNotificationBox()`, `notificationBox.appendNotification()`, `notificationBox.getNotificationWithValue()`, `this.browser.getTabBrowser()`
- 条件付き依存: `if (previousNotification)` → `notificationBox.removeNotification()`
- 参照: `notification.persistence`, `notificationBox.PRIORITY_CRITICAL_HIGH`, `this.browser`

## SafeBrowsingNotificationBox.onLocationChange()
- 位置: L61-73
- 役割: トップレベルのドメインが変わったら cleanup を呼び、警告バーを外す。
- 触るとき: 別サイトへ移動したときに警告バーが残る、または早く消える問題を調べるときに見る。
- 呼び出し先: `this.#getDomainForComparison()`
- 条件付き依存: `if ( !this._currentURIBaseDomain || newURIBaseDomain !== this._currentURIBaseDomain )` → `this.cleanup()`
- 参照: `this._currentURIBaseDomain`, `webProgress.isTopLevel`

## SafeBrowsingNotificationBox.cleanup()
- 位置: L75-93
- 役割: 警告通知を外し、進行リスナーと参照を解除して状態を初期化する。
- 触るとき: 警告バーの解放漏れや二重解除を調べるときに見る。
- 条件付き依存: `if (this.browser)` → `this.browser.getTabBrowser()`
- 条件付き依存: `if (this.browser)` → `gBrowser.getNotificationBox()`
- 条件付き依存: `if (this.browser)` → `notificationBox.getNotificationWithValue()`
- 条件付き依存: `if (notification)` → `notificationBox.removeNotification()`
- 条件付き依存: `if (this.browser)` → `this.browser.removeProgressListener()`
- 参照: `Ci.nsIWebProgress.NOTIFY_LOCATION`, `this._currentURIBaseDomain`, `this.browser`, `this.browser.safeBrowsingNotification`
- XPCOM: [`nsIWebProgress`](../../dom/interfaces/base/nsIBrowser.idl.md)

## SafeBrowsingNotificationBox.#getDomainForComparison()
- 位置: L95-104
- 役割: URI の eTLD+1 を比較用に返し、取れなければ host か spec を代わりに使う。
- 触るとき: 同一サイト判定の粒度を変えるときに見る。
- 呼び出し先: `Services.eTLD.getBaseDomain()`
- 参照: `uri.asciiHost`, `uri.asciiSpec`
- XPCOM: `Services.eTLD`

## BlockedSiteParent.receiveMessage()
- 位置: L113-124
- 役割: 子からの Browser:SiteBlockedError を受け、トップフレームかどうかを添えて _onAboutBlocked に渡す。
- 触るとき: ブロックページのクリックが親の処理に届く経路を追うときに見る。
- 呼び出し先: `this._onAboutBlocked()`
- 参照: `msg.data.blockedInfo`, `msg.data.elementId`, `msg.data.reason`, `msg.name`, `this.browsingContext`, `this.browsingContext.top`

## BlockedSiteParent._onAboutBlocked()
- 位置: L126-171
- 役割: 理由別にテレメトリを記録し、「戻る」は前のページへ戻し、「警告を無視」は許可ボタン付きで ignoreWarningLink を呼ぶ。
- 触るとき: ブロックページのボタンごとの動作やテレメトリの計測名を変えるときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`, `this.leaveErrorPage()`
- 条件付き依存: `if (sendTelemetry)` → `Glean.urlclassifier.uiEvents.accumulateSingleSample()`
- 条件付き依存: `if (Services.prefs.getBoolPref("browser.safebrowsing.allowOverride"))` → `this.ignoreWarningLink()`
- 参照: `Ci.IUrlClassifierUITelemetry`, `this.browsingContext.top.embedderElement`
- XPCOM: `Services.prefs`

## BlockedSiteParent.ignoreWarningLink()
- 位置: L173-297
- 役割: 一時的な safe-browsing 許可を付与し、理由別の警告文とボタンを作ってバイパス読み込みで元の URL を開く。
- 触るとき: 警告を無視して進む動作、報告リンクの有無、許可の有効期間を変えるときに見る。
- 呼び出し先: `Services.perms.addFromPrincipal()`, `Services.scriptSecurityManager.createContentPrincipal()`, `browser.safeBrowsingNotification?.cleanup()`, `browsingContext.currentURI.mutate()`, `browsingContext.currentURI.mutate().setQuery()`, `browsingContext.currentURI.mutate().setQuery("").finalize()`, `browsingContext.loadURI()`, `lazy.browserBundle.GetStringFromName()`
- 条件付き依存: `if (reason === "malware")` → `lazy.SafeBrowsing.getReportURL()`
- 条件付き依存: `if (reason === "malware")` → `lazy.browserBundle.GetStringFromName()`
- 条件付き依存: `if (reportUrl)` → `lazy.browserBundle.GetStringFromName()`
- 条件付き依存: `if (reason === "phishing")` → `lazy.SafeBrowsing.getReportURL()`
- 条件付き依存: `if (reason === "phishing")` → `lazy.browserBundle.GetStringFromName()`
- 条件付き依存: `if (reason === "unwanted")` → `lazy.browserBundle.GetStringFromName()`
- 条件付き依存: `if (reason === "harmful")` → `lazy.browserBundle.GetStringFromName()`
- 条件付き依存: `if (!activeSHEntry)` → `console.error()`
- 参照: `Ci.nsIPermissionManager.ALLOW_ACTION`, `Ci.nsIPermissionManager.EXPIRE_SESSION`, `Ci.nsIWebNavigation.LOAD_FLAGS_BYPASS_CLASSIFIER`, `activeSHEntry.triggeringPrincipal`, `browser.safeBrowsingNotification`, `browsingContext.activeSessionHistoryEntry`, `browsingContext.currentWindowGlobal.documentPrincipal.originAttributes`, `browsingContext.top.embedderElement`, `browsingContext.topChromeWindow`, `uri.asciiSpec`
- XPCOM: [`nsIPermissionManager`](../../netwerk/base/nsIPermissionManager.idl.md) / [`nsIWebNavigation`](../../docshell/base/nsIWebNavigation.idl.md) / `Services.perms` / `Services.scriptSecurityManager`

## callback()
- 位置: L201-204
- 役割: 警告バーの「ここから離れる」ボタンで、エラーページから戻る処理を行う。
- 触るとき: 警告バーの離脱ボタンの挙動を変えるときに見る。
- 呼び出し先: `this.leaveErrorPage()`
- 参照: `browsingContext.top.embedderElement`

## BlockedSiteParent.callback()
- 位置: L228-234
- 役割: マルウェア警告の「攻撃サイトではない」ボタンから、報告 URL を新しいタブで開く。
- 触るとき: マルウェアの誤検知報告リンクの動作を変えるときに見る。
- 呼び出し先: `lazy.URILoadingHelper.openTrustedLinkIn()`

## BlockedSiteParent.callback()
- 位置: L255-261
- 役割: フィッシング警告の「詐欺サイトではない」ボタンから、報告 URL を新しいタブで開く。
- 触るとき: フィッシングの誤検知報告リンクの動作を変えるときに見る。
- 呼び出し先: `lazy.URILoadingHelper.openTrustedLinkIn()`
