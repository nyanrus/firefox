# browser/base/content/browser-thumbnails.js

source: browser/base/content/browser-thumbnails.js
source-hash: 6dd7c20dc24d75d56de96c6381e161f03110a67a
lines: 227

## <module>
- 役割: トップサイトのサムネイルを、読み込み完了・タブ選択時に遅延撮影して PageThumbs に保存する仕組み。
- 呼び出し先: `ChromeUtils.defineLazyGetter()`

## Thumbnails_init()
- 位置: L36-49
- 役割: タブ進捗リスナーと disk_cache_ssl pref のオブザーバー、TabClose/TabSelect の購読を登録し、撮影予約用の WeakMap を作る。
- 触るとき: 撮影の開始条件になるイベントや pref を追加・変更するとき、初期化の順序に依存する処理を足すとき。
- 呼び出し先: `Services.prefs.addObserver()`, `Services.prefs.getBoolPref()`, `gBrowser.addTabsProgressListener()`, `gBrowser.tabContainer.addEventListener()`, `this._tabEvents.forEach()`
- 参照: `this.PREF_DISK_CACHE_SSL`, `this._sslDiskCacheEnabled`, `this._timeouts`
- XPCOM: `Services.prefs`

## Thumbnails_uninit()
- 位置: L51-63
- 役割: init で登録したリスナーと pref オブザーバーを外し、トップサイト URL 更新タイマーを止める。
- 触るとき: ウィンドウ終了時の後始末に残りがないか確かめるとき、init に新しいリスナーを足したとき。
- 呼び出し先: `Services.prefs.removeObserver()`, `gBrowser.removeTabsProgressListener()`, `gBrowser.tabContainer.removeEventListener()`, `this._tabEvents.forEach()`
- 条件付き依存: `if (this._topSiteURLsRefreshTimer)` → `this._topSiteURLsRefreshTimer.cancel()`
- 参照: `this.PREF_DISK_CACHE_SSL`, `this._topSiteURLsRefreshTimer`
- XPCOM: `Services.prefs`

## Thumbnails_handleEvent()
- 位置: L65-82
- 役割: scroll で予約済みのブラウザに遅延撮影を張り直し、TabSelect で予約、TabClose で予約の取り消しを行う。
- 触るとき: タブ切り替えや閉じた時に撮影が走る・走らないという挙動を調べるとき、scroll による再予約を変えるとき。
- 呼び出し先: `this._cancelDelayedCapture()`, `this._delayedCapture()`, `this._timeouts.has()`
- 条件付き依存: `if (this._timeouts.has(browser))` → `this._delayedCapture()`
- 参照: `aEvent.currentTarget`, `aEvent.target.linkedBrowser`, `aEvent.type`

## Thumbnails_observe()
- 位置: L84-92
- 役割: disk_cache_ssl pref の変更を受け、_sslDiskCacheEnabled の値を読み直す。
- 触るとき: SSL コンテンツのディスクキャッシュ設定が撮影に反映されないと感じたとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `this.PREF_DISK_CACHE_SSL`, `this._sslDiskCacheEnabled`
- XPCOM: `Services.prefs`

## Thumbnails_clearTopSiteURLCache()
- 位置: L94-102
- 役割: トップサイト URL 用のタイマーを止め、_topSiteURLs の lazy getter を作り直して次回参照時に再取得させる。
- 触るとき: トップサイトの追加や削除が撮影対象に反映されないとき。
- 呼び出し先: `ChromeUtils.defineLazyGetter()`
- 条件付き依存: `if (this._topSiteURLsRefreshTimer)` → `this._topSiteURLsRefreshTimer.cancel()`
- 参照: `this._topSiteURLs`, `this._topSiteURLsRefreshTimer`

## Thumbnails_notify()
- 位置: L104-107
- 役割: 60 秒のタイマー満了で呼ばれ、タイマー参照を null にしてトップサイト URL のキャッシュを消す。
- 触るとき: トップサイト URL のキャッシュがいつ更新されるかを追うとき。
- 呼び出し先: `gBrowserThumbnails.clearTopSiteURLCache()`
- 参照: `gBrowserThumbnails._topSiteURLsRefreshTimer`

## Thumbnails_onStateChange()
- 位置: L112-125
- 役割: 全タブの進捗リスナーとして、ネットワーク由来の STATE_STOP を受けたら遅延撮影を予約する。
- 触るとき: ページの読み込み完了後にサムネイルを撮るタイミングを変えるとき。
- 条件付き依存: `if ( aStateFlags & Ci.nsIWebProgressListener.STATE_STOP && aStateFlags & Ci.nsIWebProgressListener.STATE_IS_NETWORK )` → `this._delayedCapture()`
- 参照: `Ci.nsIWebProgressListener.STATE_IS_NETWORK`, `Ci.nsIWebProgressListener.STATE_STOP`
- XPCOM: [`nsIWebProgressListener`](../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## _capture()
- 位置: async L127-136
- 役割: URI がトップサイトに含まれ、_shouldCapture も真のとき、PageThumbs.captureAndStoreIfStale で撮影して保存する。
- 触るとき: どのページを撮影対象にするか、撮影条件を広げたり絞ったりするとき。
- 呼び出し先: `this._shouldCapture()`, `topSites.includes()`
- 条件付き依存: `if (await this._shouldCapture(aBrowser))` → `PageThumbs.captureAndStoreIfStale()`
- 参照: `aBrowser.currentURI`, `aBrowser.currentURI.spec`, `this._topSiteURLs`

## Thumbnails_delayedCapture()
- 位置: L138-160
- 役割: 既存の予約を取り消したうえで、1 秒後に requestIdleCallback(上限は 30 秒)で _capture を予約し、予約 ID を _timeouts に記録する。
- 触るとき: スクロールや連続読み込みで撮影が重複したり遅れすぎたりするのを直すとき。
- 呼び出し先: `requestIdleCallback()`, `setTimeout()`, `this._timeouts.has()`, `this._timeouts.set()`
- 条件付き依存: `if (this._timeouts.has(aBrowser))` → `this._cancelDelayedCallbacks()`
- 条件付き依存: `if (!(this._timeouts.has(aBrowser)))` → `aBrowser.addEventListener()`
- 参照: `this._captureDelayMS`

## idleCallback()
- 位置: L145-148
- 役割: requestIdleCallback に渡される無名関数で、遅延予約を解除してから _capture を実行する。
- 触るとき: アイドル時の撮影実行の順序やキャンセル処理を変えるとき。
- 呼び出し先: `this._cancelDelayedCapture()`, `this._capture()`

## Thumbnails_shouldCapture()
- 位置: async L162-171
- 役割: 選択中のブラウザで、about: ページでなければ PageThumbs.shouldStoreThumbnail に判定を任せる。
- 触るとき: どの状況でサムネイルを保存しないかという条件を変えるとき。
- 呼び出し先: `PageThumbs.shouldStoreThumbnail()`, `gBrowser.currentURI.schemeIs()`
- 参照: `gBrowser.selectedBrowser`

## Thumbnails_cancelDelayedCapture()
- 位置: L173-179
- 役割: 予約が残るブラウザから scroll リスナーを外し、予約を取り消して _timeouts から削除する。
- 触るとき: タブを閉じた後に撮影が走る、または予約が残る不具合を調べるとき。
- 呼び出し先: `this._timeouts.has()`
- 条件付き依存: `if (this._timeouts.has(aBrowser))` → `aBrowser.removeEventListener()`
- 条件付き依存: `if (this._timeouts.has(aBrowser))` → `this._cancelDelayedCallbacks()`
- 条件付き依存: `if (this._timeouts.has(aBrowser))` → `this._timeouts.delete()`

## Thumbnails_cancelDelayedCallbacks()
- 位置: L181-192
- 役割: 予約の種類に応じて、タイマーなら clearTimeout、idle 予約なら cancelIdleCallback で止める。
- 触るとき: タイマー予約と idle 予約の扱いを変えるとき。
- 呼び出し先: `this._timeouts.get()`
- 条件付き依存: `if (timeoutData.isTimeout)` → `clearTimeout()`
- 条件付き依存: `if (!(timeoutData.isTimeout))` → `window.cancelIdleCallback()`
- 参照: `timeoutData.id`, `timeoutData.isTimeout`

## getTopSiteURLs()
- 位置: async L195-220
- 役割: 60 秒のタイマーを張り、faviconSize が 96 未満のトップサイトとピン留めサイトの URL を集めて返す。
- 触るとき: 撮影対象になるトップサイトの範囲を変えるとき、特に favicon サイズによる絞り込みを見直すとき。
- 呼び出し先: `Cc[ "@mozilla.org/timer;1" ].createInstance()`, `NewTabUtils.activityStreamLinks.getTopSites()`, `gBrowserThumbnails._topSiteURLsRefreshTimer.initWithCallback()`, `sites.push()`, `sites.reduce()`, `topSites.filter()`
- 条件付き依存: `if (link)` → `urls.push()`
- 参照: `Ci.nsITimer`, `Ci.nsITimer.TYPE_ONE_SHOT`, `NewTabUtils.pinnedLinks.links`, `gBrowserThumbnails._topSiteURLsRefreshTimer`, `link.faviconSize`, `link.url`
- XPCOM: [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1`
