# browser/actors/AboutPrivateBrowsingParent.sys.mjs

source: browser/actors/AboutPrivateBrowsingParent.sys.mjs
source-hash: 0ad1a4eb3854b401eed69fb547dec53743f2cddb
lines: 187

## <module>
- 役割: about:privatebrowsing の親側アクター。ページからのメッセージを受け、新規ウィンドウ、検索への引き継ぎ、検索バナーとプロモの表示判定、Spotlight 表示を行う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## AboutPrivateBrowsingParent.setShownThisSession()
- 位置: L37-39
- 役割: セッション中に検索バナーを表示済みかを示すフラグを外から設定する（テスト用）。
- 触るとき: 検索バナーの一セッション一回の制御をテストで切り替えるときに見る。

## AboutPrivateBrowsingParent.receiveMessage()
- 位置: L41-185
- 役割: ページからの OpenPrivateWindow、SearchHandoff、ShouldShowSearchBanner などのメッセージを種類ごとに処理し、結果を返す。
- 触るとき: about:privatebrowsing の機能を追加・変更するとき、どのメッセージがどの処理に届くかを確かめるときに見る。
- 呼び出し先: `ASRouter.handleMessageRequest()`, `ASRouter.isUnblockedMessage()`, `BrowserUtils.shouldShowPromo()`, `Services.prefs.getIntPref()`, `Services.prefs.setIntPref()`, `browser.getAttribute()`, `lazy.SearchService.getDefaultPrivate()`, `lazy.SearchService.getDefaultPrivate().then()`, `lazy.SpecialMessageActions.handleAction()`, `resolve()`, `urlBar.inputField.addEventListener()`, `win.OpenBrowserWindow()`, `win.openPreferences()`
- 条件付き依存: `if (!aMessage.data || !aMessage.data.text)` → `urlBar.setHiddenFocus()`
- 条件付き依存: `if (!(!aMessage.data || !aMessage.data.text))` → `urlBar.handoff()`
- 条件付き依存: `if (message)` → `Glean.aboutprivatebrowsing.basicsModalShown.record()`
- 条件付き依存: `if (message)` → `lazy.Spotlight.showSpotlightDialog()`
- 参照: `ASRouter.waitForInitialized`, `BrowserUtils.PromoType`, `aMessage.data`, `aMessage.data.id`, `aMessage.data.text`, `aMessage.data.type`, `aMessage.name`, `browser.documentGlobal`, `engine.name`, `lazy.MAX_SEARCH_BANNER_SHOW_COUNT`, `lazy.SearchService.defaultPrivateEngine`, `lazy.isPrivateSearchUIEnabled`, `this.browsingContext.top.embedderElement`, `win.gURLBar`
- XPCOM: `Services.prefs`

## checkFirstChange()
- 位置: L71-83
- 役割: 検索ハンドオフで最初の文字入力や貼り付けを検知し、非表示フォーカスを解除してページ内検索を隠す。
- 触るとき: 検索ハンドオフ時にアドレスバーの見た目や入力が正しく切り替わらないときに見る。
- 条件付き依存: `if (isFirstChange)` → `urlBar.removeHiddenFocus()`
- 条件付き依存: `if (isFirstChange)` → `urlBar.handoff()`
- 条件付き依存: `if (isFirstChange)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (isFirstChange)` → `urlBar.removeEventListener()`

## onKeydown()
- 位置: L85-94
- 役割: アドレスバーの keydown を監視し、値が変わる入力なら checkFirstChange を呼び、Escape なら onDone で終える。
- 触るとき: ページ内検索からの入力や Escape の挙動を変えるときに見る。
- 条件付き依存: `if (ev.key.length === 1 && !ev.altKey && !ev.ctrlKey && !ev.metaKey)` → `checkFirstChange()`
- 条件付き依存: `if (ev.key === "Escape")` → `onDone()`
- 参照: `ev.altKey`, `ev.ctrlKey`, `ev.key`, `ev.key.length`, `ev.metaKey`

## onDone()
- 位置: L96-111
- 役割: 検索ハンドオフを終了し、ページ内検索を再表示してアドレスバーのリスナーを外す。
- 触るとき: 検索ハンドオフ終了後にフォーカスやリスナーが残る問題を調べるときに見る。
- 呼び出し先: `this.sendAsyncMessage()`, `urlBar.inputField.removeEventListener()`, `urlBar.removeHiddenFocus()`
- 参照: `ev?.type`
