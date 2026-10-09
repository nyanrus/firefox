# browser/base/content/nsContextMenu.sys.mjs

source: browser/base/content/nsContextMenu.sys.mjs
source-hash: af4633e94e3753ef4fd07f72c7bd4958127c4676
lines: 3102

## <module>
- 役割: 右クリックメニュー(contextmenu)の項目を文脈に合わせて表示・無効化し、リンク・画像・動画・音声・テキスト選択などの各操作を実行するクラス nsContextMenu を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Components.Constructor()`, `Promise.resolve()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetter()`

## nsContextMenu.constructor()
- 位置: L153-220
- 役割: メニューを開くたびに作られ、文脈を読み込んだうえで各項目を初期化する。表示対象外なら何もしない。Shift を押していなければ on-build-contextmenu を通知して拡張機能が項目を足せるようにする。
- 触るとき: メニューの初期化の流れや、拡張機能への通知のタイミングを変えるとき。
- 呼び出し先: `this.document.getElementById()`, `this.initItems()`, `this.setContext()`
- 条件付き依存: `if (!aIsShift)` → `gBrowser.getTabForBrowser()`
- 条件付き依存: `if (!aIsShift)` → `Services.obs.notifyObservers()`
- 参照: `aXulMenu.documentGlobal`, `aXulMenu.ownerDocument`, `gBrowser.getTabForBrowser`, `subject.wrappedJSObject`, `this.browser`, `this.browser.currentURI.spec`, `this.contentData`, `this.contentData.docLocation`, `this.contentData.webExtContextData`, `this.document`, `this.frameID`, `this.inFrame`, `this.isContentSelected`, `this.isTextSelected`, `this.linkTextStr`, `this.linkURI`, `this.linkURL`, `this.onAudio`, `this.onCanvas`, `this.onEditable`, `this.onImage`, `this.onLink`, `this.onPassword`, `this.onPlainTextLink`, `this.onSpellcheckable`, `this.onTextInput`, `this.onVideo`, `this.originalMediaURL`, `this.passwordRevealed`, `this.selectionInfo.docSelectionIsCollapsed`, `this.selectionInfo.fullText`, `this.shouldDisplay`, `this.timeStamp`, `this.viewFrameSourceElement`, `this.webExtBrowserType`, `this.window`
- XPCOM: `Services.obs`

## nsContextMenu.setContext()
- 位置: L222-365
- 役割: 子プロセスから届いた contentData(無ければ現在のブラウザ)から文脈を読み、リンク、メディア URL、principal、選択、スペルチェック情報、ContextMenu アクターを this に写し、PDF.js 用のメニューを作る。
- 触るとき: メニュー項目の判定に使う値を増やすとき、または値が空になる理由を調べるとき。
- 呼び出し先: `BrowsingContext.get()`, `Object.create()`, `gBrowser.getTabForBrowser()`, `lazy.E10SUtils.deserializePolicyContainer()`, `this.browser.getAttribute()`, `this.getLinkURI()`
- 条件付き依存: `if (!(this.contentData))` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (!(this.contentData))` → `SelectionUtils.getSelectionDetails()`
- 条件付き依存: `if (!(this.contentData))` → `this.browser.browsingContext.currentWindowGlobal.getActor()`
- 条件付き依存: `if (context.shouldInitInlineSpellCheckerUINoChildren)` → `InlineSpellCheckerUI.initFromRemote()`
- 条件付き依存: `if (context.shouldInitInlineSpellCheckerUIWithChildren)` → `InlineSpellCheckerUI.initFromRemote()`
- 条件付き依存: `if (context.shouldInitInlineSpellCheckerUIWithChildren)` → `this.showItem()`
- 参照: `InlineSpellCheckerUI.canSpellCheck`, `context.bgImageURL`, `context.canSpellCheck`, `context.frameBrowsingContextID`, `context.frameID`, `context.frameOuterWindowID`, `context.hasBGImage`, `context.hasMultipleBGImages`, `context.hasTextFragments`, `context.imageDescURL`, `context.imageInfo`, `context.inAboutDevtoolsToolbox`, `context.inFrame`, `context.inPDFViewer`, `context.inSrcdocFrame`, `context.inSyntheticDoc`, `context.inTabBrowser`, `context.inWebExtBrowser`, `context.isDesignMode`, `context.isSponsoredLink`, `context.link`, `context.linkDownload`, `context.linkProtocol`, `context.linkTextStr`, `context.linkURL`, `context.mediaURL`, `context.onAudio`, `context.onCanvas`, `context.onCompletedImage`, `context.onDRMMedia`, `context.onEditable`, `context.onImage`, `context.onLink`, `context.onLoadedImage`, `context.onMailtoLink`, `context.onMozExtLink`, `context.onNumeric`, `context.onPassword`, `context.onPiPVideo`, `context.onSaveableLink`, `context.onSearchField`, `context.onSpellcheckable`, `context.onTelLink`, `context.onTextInput`, `context.onVideo`, `context.originalMediaURL`, `context.passwordRevealed`, `context.policyContainer`, `context.principal`, `context.shouldDisplay`, `context.shouldInitInlineSpellCheckerUINoChildren`, `context.shouldInitInlineSpellCheckerUIWithChildren`, `context.storagePrincipal`, `context.target`, `context.targetIdentifier`, `context.timeStamp`, `context.webExtBrowserType`, `gBrowser.getTabForBrowser`, `nsContextMenu.contentData`, `this.actor`, `this.actor.manager`, `this.actor.manager.domProcess.remoteType`, `this.browser`, `this.browser.documentGlobal`, `this.canSpellCheck`, `this.contentData`, `this.contentData.actor`, `this.contentData.browser`, `this.contentData.context`, `this.contentData.selectionInfo`, `this.contentData.spellInfo`, `this.contentData.spellInfo.spellSuggestions`, `this.frameBrowsingContext`, `this.frameID`, `this.frameOuterWindowID`, `this.hasBGImage`, `this.hasMultipleBGImages`, `this.hasTextFragments`, `this.imageDescURL`, `this.imageInfo`, `this.inAboutDevtoolsToolbox`, `this.inFrame`, `this.inPDFViewer`, `this.inSrcdocFrame`, `this.inSyntheticDoc`, `this.inTabBrowser`, `this.inWebExtBrowser`, `this.isDesignMode`, `this.isSponsoredLink`, `this.isTextSelected`, `this.link`, `this.linkDownload`, `this.linkProtocol`, `this.linkTextStr`, `this.linkURI`, `this.linkURL`, `this.mediaURL`, `this.onAudio`, `this.onCanvas`, `this.onCompletedImage`, `this.onDRMMedia`, `this.onEditable`, `this.onImage`, `this.onLink`, `this.onLoadedImage`, `this.onMailtoLink`, `this.onMozExtLink`, `this.onNumeric`, `this.onPassword`, `this.onPiPVideo`, `this.onSaveableLink`, `this.onSearchField`, `this.onSpellcheckable`, `this.onTelLink`, `this.onTextInput`, `this.onVideo`, `this.originalMediaURL`, `this.ownerDoc`, `this.ownerDoc.defaultView.docShell.chromeEventHandler`, `this.passwordRevealed`, `this.pdfjsContextMenu`, `this.policyContainer`, `this.principal`, `this.remoteType`, `this.selectedText`, `this.selectedText.length`, `this.selectionInfo`, `this.selectionInfo.text`, `this.shouldDisplay`, `this.spellSuggestions`, `this.storagePrincipal`, `this.target`, `this.target.ownerDocument`, `this.targetIdentifier`, `this.textFragmentURL`, `this.timeStamp`, `this.webExtBrowserType`, `this.window`

## nsContextMenu.hiding()
- 位置: L367-391
- 役割: メニューが閉じるとき、アクターに通知し、ログイン候補の取得を打ち切り、スペルチェックの候補と辞書とログイン項目を消す。最後に _onPopupHiding が残っていれば実行する。
- 触るとき: 閉じた後にメニューの状態が残ってしまう不具合を調べるとき。
- 呼び出し先: `Cu.isESModuleLoaded()`, `this.#passwordItemsAbortController?.abort()`, `this.window.InlineSpellCheckerUI.clearDictionaryListFromMenu()`, `this.window.InlineSpellCheckerUI.clearSuggestionsFromMenu()`, `this.window.InlineSpellCheckerUI.uninit()`
- 条件付き依存: `if (this.actor)` → `this.actor.hiding()`
- 条件付き依存: `if ( Cu.isESModuleLoaded( "resource://gre/modules/LoginManagerContextMenu.sys.mjs" ) )` → `lazy.LoginManagerContextMenu.clearLoginsFromMenu()`
- 条件付き依存: `if (this._onPopupHiding)` → `this._onPopupHiding()`
- 参照: `aXulMenu.showHideSeparators`, `this._onPopupHiding`, `this.actor`, `this.contentData`, `this.document`

## nsContextMenu.initItems()
- 位置: L393-421
- 役割: 各 init 関数を決まった順に呼び、PDF.js の項目を初期化してセパレータを整える。拡張機能が後から呼べるよう aXulMenu に showHideSeparators を設定する。
- 触るとき: 項目の初期化順を変えるとき、または項目がどの init で扱われるかを探すとき。
- 呼び出し先: `this.initClipboardItems()`, `this.initImageItems()`, `this.initLeaveDOMFullScreenItems()`, `this.initMediaPlayerItems()`, `this.initMiscItems()`, `this.initNavigationItems()`, `this.initOpenItems()`, `this.initPasswordControlItems()`, `this.initPasswordManagerItems()`, `this.initSaveItems()`, `this.initScreenshotItem()`, `this.initSpellingItems()`, `this.initSyncItems()`, `this.initTextFragmentItems()`, `this.initViewItems()`, `this.initViewSourceItems()`, `this.pdfjsContextMenu.initItems()`, `this.showHideSeparators()`
- 参照: `aXulMenu.showHideSeparators`

## aXulMenu.showHideSeparators()
- 位置: L417-419
- 役割: メニューに付けられた関数で、中身は nsContextMenu の showHideSeparators を呼ぶ。拡張機能がメニューを書き換えたあとに呼んで、区切り線を整え直せるようにする。
- 触るとき: 拡張機能が項目を足したり消したりした後に区切り線の表示を直したいとき。
- 呼び出し先: `this.showHideSeparators()`

## nsContextMenu.initTextFragmentItems()
- 位置: L423-446
- 役割: ハイライトへのリンクをコピーする項目を表示するか決める。機能が有効で、PDF、フレーム、編集可能欄、view-source 以外で、ハイライトか選択があるときに出す。項目は最初は無効にし、ハイライト削除は既存のハイライトがあるときだけ出す。
- 触るとき: ハイライト関連の項目の表示条件を変えるとき。
- 呼び出し先: `this.browser.currentURI.schemeIs()`, `this.setItemAttr()`, `this.showItem()`
- 参照: `lazy.STRIP_ON_SHARE_ENABLED`, `lazy.TEXT_FRAGMENTS_ENABLED`, `this.hasTextFragments`, `this.inFrame`, `this.inPDFViewer`, `this.isContentSelected`, `this.onEditable`

## nsContextMenu.getTextDirective()
- 位置: async L448-465
- 役割: 機能が有効なら子プロセスからテキストフラグメントの URL を取り、作れた場合にコピー項目を有効にする。クリーンなリンクの項目は、パラメータを取り除ける URL のときだけ有効にする。
- 触るとき: ハイライトのコピー項目が無効のままになる条件を調べるとき。
- 呼び出し先: `this.actor.getTextDirective()`
- 条件付き依存: `if (this.textFragmentURL)` → `this.setItemAttr()`
- 条件付き依存: `if (this.textFragmentURL)` → `this.getLinkURI()`
- 条件付き依存: `if (this.textFragmentURL)` → `this.#canStripParams()`
- 参照: `lazy.TEXT_FRAGMENTS_ENABLED`, `this.textFragmentURL`

## nsContextMenu.removeAllTextFragments()
- 位置: async L467-469
- 役割: 子プロセスの removeAllTextFragments を呼んで、ページ上のハイライトをすべて消す。
- 触るとき: ハイライトの一括削除の動作を変えるとき。
- 呼び出し先: `this.actor.removeAllTextFragments()`

## nsContextMenu.copyLinkToHighlight()
- 位置: L471-480
- 役割: テキストフラグメントの URL があれば、stripSiteTracking が真ならトラッキング用パラメータを除いてコピーし、偽ならそのままコピーする。
- 触るとき: ハイライトのリンクをコピーするときの除去の有無を変えるとき。
- 条件付き依存: `if (stripSiteTracking)` → `this.getLinkURI()`
- 条件付き依存: `if (stripSiteTracking)` → `this.copyStrippedLink()`
- 条件付き依存: `if (!(stripSiteTracking))` → `this.copyLink()`
- 参照: `this.textFragmentURL`

## nsContextMenu.initOpenItems()
- 位置: L482-572
- 役割: リンクを開く系の項目(新しいタブ、プライベート、コンテナ、分割表示、スマートウィンドウ、プレビュー)の表示を決める。mailto の内部ハンドラの判定と、テキスト選択中のプレーンテキストリンクも扱う。
- 触るとき: リンクを開く項目の表示条件を変えるとき、またはコンテナや mailto で項目が出ない理由を調べるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.AIWindow.isAIWindowEnabled()`, `lazy.ContextualIdentityService.getPublicIdentities()`, `lazy.LinkPreview.shouldShowContextMenu()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.showItem()`, `window.gBrowser?.getTabForBrowser()`
- 条件付き依存: `if (this.onMailtoLink)` → `Cc[ "@mozilla.org/uriloader/external-protocol-service;1" ] .getService()`
- 条件付き依存: `if ( this.isTextSelected && !this.onLink && this.selectionInfo && this.selectionInfo.linkURL )` → `this.getLinkURI()`
- 条件付き依存: `if (this.contentData.userContextId)` → `document.getElementById()`
- 条件付き依存: `if (this.contentData.userContextId)` → `item.setAttribute()`
- 条件付き依存: `if (this.contentData.userContextId)` → `lazy.ContextualIdentityService.getUserContextLabel()`
- 条件付き依存: `if (this.contentData.userContextId)` → `document.l10n.setAttributes()`
- 参照: `Ci.nsIExternalProtocolService`, `Ci.nsIHandlerInfo.useHelperApp`, `Ci.nsIWebHandlerApp`, `lazy.ContextualIdentityService.getPublicIdentities().length`, `lazy.PrivateBrowsingUtils.enabled`, `mailtoHandler.alwaysAskBeforeHandling`, `mailtoHandler.preferredAction`, `mailtoHandler.preferredApplicationHandler`, `this.browser`, `this.contentData.userContextId`, `this.isTextSelected`, `this.linkTextStr`, `this.linkURI`, `this.linkURL`, `this.onLink`, `this.onMailtoLink`, `this.onPlainTextLink`, `this.onSaveableLink`, `this.selectionInfo`, `this.selectionInfo.linkText`, `this.selectionInfo.linkURL`, `window.gBrowser?.getTabForBrowser(this.browser)?.hidden`, `window.gBrowser?.getTabForBrowser(this.browser)?.pinned`, `window.gBrowser?.selectedTab?.splitview`
- XPCOM: [`nsIExternalProtocolService`](../../../uriloader/exthandler/nsIExternalProtocolService.idl.md) / [`nsIHandlerInfo`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIWebHandlerApp`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / `@mozilla.org/uriloader/external-protocol-service;1` / `Services.prefs`

## nsContextMenu.initNavigationItems()
- 位置: L574-643
- 役割: 戻る、進む、再読み込み、停止の表示を決める。選択や画像などがあるとき、またはタブ以外では出さない。戻る・進むの説明文に現在のショートカットを入れる。
- 触るとき: ナビゲーション項目の表示条件や、再読み込みと停止の切り替えを変えるとき。
- 呼び出し先: `initBackForwardMenuItemTooltip()`, `this.showItem()`, `this.window.XULBrowserWindow.stopCommand.getAttribute()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `this.showItem()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `this.showItem()`
- 参照: `AppConstants.platform`, `this.inTabBrowser`, `this.isContentSelected`, `this.onAudio`, `this.onCanvas`, `this.onImage`, `this.onLink`, `this.onTextInput`, `this.onVideo`, `this.window.browsingContext.isDocumentPiP`

## initBackForwardMenuItemTooltip()
- 位置: L613-630
- 役割: macOS 以外で、指定の項目の説明文にショートカットを整形して入れる。ショートカットの要素が無ければ空の値で整形する。
- 触るとき: 戻る・進むの説明文の表示を変えるとき。
- 呼び出し先: `document.getElementById()`, `document.l10n.setAttributes()`
- 条件付き依存: `if (shortcut)` → `lazy.ShortcutUtils.prettifyShortcut()`
- 参照: `AppConstants.platform`

## nsContextMenu.initLeaveDOMFullScreenItems()
- 位置: L645-649
- 役割: ドキュメントが DOM の全画面表示中のときだけ「全画面表示を終了」の項目を表示する。
- 触るとき: 全画面終了の項目の表示条件を変えるとき。
- 呼び出し先: `this.showItem()`
- 参照: `this.target.ownerDocument.fullscreen`

## nsContextMenu.initSaveItems()
- 位置: L651-717
- 役割: 保存系の項目を文脈に応じて表示する。ページ保存は選択やリンク、画像、動画、音声が無いときだけ出す。リンク保存は保存可能なリンクかプレーンテキストのリンクのときに出し、ポリシーで禁止されていれば無効にする。動画・音声の保存と送信は mediaURL が無いか blob: のとき無効にする。ポリシーでファイル選択が禁止なら保存系をすべて無効にする。
- 触るとき: 保存項目の表示条件を変えるとき、またはポリシーによる無効化の範囲を調べるとき。
- 呼び出し先: `Services.policies.isAllowed()`, `this.mediaURL.startsWith()`, `this.setItemAttr()`, `this.showItem()`
- 条件付き依存: `if ( (this.onSaveableLink || this.onPlainTextLink) && Services.policies.status === Services.policies.ACTIVE )` → `this.setItemAttr()`
- 条件付き依存: `if ( (this.onSaveableLink || this.onPlainTextLink) && Services.policies.status === Services.policies.ACTIVE )` → `lazy.WebsiteFilter.isAllowed()`
- 条件付き依存: `if ( Services.policies.status === Services.policies.ACTIVE && !Services.policies.isAllowed("filepickers") )` → `this.setItemAttr()`
- 参照: `Services.policies.ACTIVE`, `Services.policies.status`, `this.isContentSelected`, `this.linkURL`, `this.mediaURL`, `this.onAudio`, `this.onCanvas`, `this.onImage`, `this.onLink`, `this.onPlainTextLink`, `this.onSaveableLink`, `this.onTextInput`, `this.onVideo`
- XPCOM: `Services.policies`

## nsContextMenu.initImageItems()
- 位置: L719-837
- 役割: 画像関連の項目(再読み込み、画像を開く、保存、コピー、テキスト認識、デスクトップ背景の設定など)の表示を決める。背景画像は1枚のときだけ扱い、cached-favicon などの画像専用プロトコルは保存・表示の対象から外す。ポリシーでファイル選択が禁止なら保存を無効にする。
- 触るとき: 画像項目の表示条件を変えるとき、または画像の項目が出ない理由を調べるとき。
- 呼び出し先: `IMAGE_ONLY_PROTOCOLS.includes()`, `Services.policies.isAllowed()`, `Services.prefs.getBoolPref()`, `URL.parse()`, `this.setItemAttr()`, `this.showAndFormatVisualSearchContextItem()`, `this.showItem()`
- 条件付き依存: `if (Services.policies.status === Services.policies.ACTIVE)` → `this.setItemAttr()`
- 条件付き依存: `if (Services.policies.status === Services.policies.ACTIVE)` → `Services.policies.isAllowed()`
- 条件付き依存: `if ( AppConstants.HAVE_SHELL_SERVICE && Services.policies.isAllowed("setDesktopBackground") )` → `this.window.getShellService()`
- 条件付き依存: `if (canSetDesktopBackground)` → `this.document.getElementById()`
- 参照: `AppConstants.HAVE_SHELL_SERVICE`, `Services.appinfo.isTextRecognitionSupported`, `Services.policies.ACTIVE`, `Services.policies.status`, `lazy.TEXT_RECOGNITION_ENABLED`, `mediaURL.protocol`, `shell.canSetDesktopBackground`, `this.contentData.disableSetDesktopBackground`, `this.document.getElementById("context-setDesktopBackground").disabled`, `this.hasBGImage`, `this.hasMultipleBGImages`, `this.imageDescURL`, `this.inFrame`, `this.inPDFViewer`, `this.inSyntheticDoc`, `this.isContentSelected`, `this.mediaURL`, `this.onAudio`, `this.onCanvas`, `this.onCompletedImage`, `this.onImage`, `this.onLink`, `this.onLoadedImage`, `this.onTextInput`, `this.onVideo`, `this.webExtBrowserType`
- XPCOM: `Services.appinfo` / `Services.policies` / `Services.prefs`

## nsContextMenu.initViewItems()
- 位置: L839-894
- 役割: ページソース、選択範囲のソース、選択範囲の印刷、検証(Inspect)、アクセシビリティ検証、動画を表示の項目を決める。DevTools の設定値と既存の利用歴から検証項目の出し方を決める。
- 触るとき: 開発者ツール関連の項目の表示条件を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.DevToolsShim.isDevToolsUser()`, `this.setItemAttr()`, `this.showItem()`
- 参照: `lazy.gPrintEnabled`, `this.inAboutDevtoolsToolbox`, `this.inFrame`, `this.inSyntheticDoc`, `this.inTabBrowser`, `this.isContentSelected`, `this.mediaURL`, `this.onAudio`, `this.onCanvas`, `this.onImage`, `this.onLink`, `this.onTextInput`, `this.onVideo`, `this.selectionInfo.isDocumentLevelSelection`, `this.window.browsingContext.isDocumentPiP`
- XPCOM: `Services.prefs`

## nsContextMenu.initMiscItems()
- 位置: L896-978
- 役割: ブックマーク、リンクのブックマーク、検索エンジンの追加、フレーム関連、翻訳、AI チャット、AI タブなど雑多な項目の表示を決める。フレームでは OS の PID をラベルに入れ、テキスト入力の有無に応じて BiDi の方向切り替えを出す。
- 触るとき: 雑多な項目の表示条件を変えるとき、またはフレーム向けの項目を足すとき。
- 呼び出し先: `["http", "https"].includes()`, `document.getElementById()`, `lazy.AIWindow.isAIWindowActiveAndEnabled()`, `lazy.GenAI.buildAskChatMenu()`, `this.shouldShowAddEngine()`, `this.showAndFormatSearchContextItem()`, `this.showItem()`, `this.showItem.bind()`, `this.showTranslateSelectionItem()`
- 条件付き依存: `if (this.inFrame)` → `this.setItemAttr()`
- 条件付き依存: `if (this.inFrame)` → `lazy.BrowserUtils.mimeTypeIsTextBased()`
- 参照: `lazy.AITAB_ENABLED`, `lazy.gPrintEnabled`, `this.actor.manager.browsingContext.currentWindowGlobal.osPid`, `this.browser`, `this.browser.currentURI.scheme`, `this.inFrame`, `this.inSrcdocFrame`, `this.inWebExtBrowser`, `this.isContentSelected`, `this.onAudio`, `this.onCanvas`, `this.onImage`, `this.onLink`, `this.onMailtoLink`, `this.onMozExtLink`, `this.onNumeric`, `this.onPlainTextLink`, `this.onTelLink`, `this.onTextInput`, `this.onVideo`, `this.selectionInfo`, `this.target.ownerDocument.contentType`, `this.viewFrameSourceElement.hidden`, `this.window`, `this.window.browsingContext.isDocumentPiP`, `window.top.gBidiUI`

## nsContextMenu.initSpellingItems()
- 位置: L980-1028
- 役割: スペルチェックの項目を決める。誤りの上なら候補の一覧を作り、辞書の一覧を追加する。辞書が無くても辞書の入手項目を出せる場合は、その項目を出す。
- 触るとき: スペル候補や辞書の項目の表示を変えるとき。
- 呼び出し先: `InlineSpellCheckerUI.canUndo()`, `document .getElementById()`, `document .getElementById("spell-check-enabled") .toggleAttribute()`, `this.showItem()`
- 条件付き依存: `if (onMisspelling)` → `document.getElementById()`
- 条件付き依存: `if (onMisspelling)` → `InlineSpellCheckerUI.addSuggestionsToMenu()`
- 条件付き依存: `if (onMisspelling)` → `this.showItem()`
- 条件付き依存: `if (!(onMisspelling))` → `this.showItem()`
- 条件付き依存: `if (canSpell)` → `document.getElementById()`
- 条件付き依存: `if (canSpell)` → `InlineSpellCheckerUI.addDictionaryListToMenu()`
- 条件付き依存: `if (canSpell)` → `this.showItem()`
- 条件付き依存: `if (this.onSpellcheckable)` → `this.showItem()`
- 条件付き依存: `if (!(this.onSpellcheckable))` → `this.showItem()`
- 参照: `InlineSpellCheckerUI.canSpellCheck`, `InlineSpellCheckerUI.enabled`, `InlineSpellCheckerUI.initialSpellCheckPending`, `InlineSpellCheckerUI.overMisspelling`, `suggestionsSeparator.parentNode`, `this.canSpellCheck`, `this.onSpellcheckable`, `this.spellSuggestions`, `this.window`

## nsContextMenu.initClipboardItems()
- 位置: L1030-1096
- 役割: 元に戻す、切り取り、コピー、貼り付けなどの編集項目と、メール、電話、リンク、動画と音声の URL をコピーする項目の表示を決める。グローバルの編集コマンドの状態も更新する。クリーンなリンクのコピーは機能が有効で、リンクかプレーンテキストのリンクで、安全でない about ページでないときに出し、パラメータを除けないときは無効にする。
- 触るとき: 編集やコピーの項目の表示条件を変えるとき、またはクリーンなリンクが無効になる理由を調べるとき。
- 呼び出し先: `sendLinkSeparator.toggleAttribute()`, `this.#canStripParams()`, `this.document.getElementById()`, `this.isSecureAboutPage()`, `this.setItemAttr()`, `this.showItem()`, `this.window.goUpdateGlobalEditMenuItems()`
- 参照: `lazy.STRIP_ON_SHARE_ENABLED`, `this.inSyntheticDoc`, `this.isContentSelected`, `this.isDesignMode`, `this.mediaURL`, `this.onAudio`, `this.onImage`, `this.onLink`, `this.onMailtoLink`, `this.onMozExtLink`, `this.onPlainTextLink`, `this.onTelLink`, `this.onTextInput`, `this.onVideo`, `this.syncItemsShown`

## nsContextMenu.initMediaPlayerItems()
- 位置: L1098-1206
- 役割: 動画と音声の操作項目を決める。再生、一時停止、ミュート、ループ、コントロール表示、全画面、ピクチャーインピクチャー、再生速度の表示を決め、速度項目は現在の値に合わせて選択状態にする。読み込み失敗やソース無しでは操作項目を無効にする。
- 触るとき: メディアの操作項目の出し分けや、再生速度の選択状態を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `this.showItem()`
- 条件付き依存: `if (onMedia)` → `this.setItemAttr()`
- 条件付き依存: `if (this.onVideo)` → `this.setItemAttr()`
- 参照: `Number.POSITIVE_INFINITY`, `this.inSyntheticDoc`, `this.onAudio`, `this.onDRMMedia`, `this.onPiPVideo`, `this.onVideo`, `this.target.HAVE_CURRENT_DATA`, `this.target.NETWORK_NO_SOURCE`, `this.target.controls`, `this.target.duration`, `this.target.ended`, `this.target.error`, `this.target.loop`, `this.target.muted`, `this.target.networkState`, `this.target.ownerDocument.fullscreen`, `this.target.paused`, `this.target.playbackRate`, `this.target.readyState`
- XPCOM: `Services.prefs`

## nsContextMenu.initPasswordManagerItems()
- 位置: L1208-1290
- 役割: ログイン入力欄の上でだけ、保存済みログインの挿入、パスワードの生成、リレーのマスク、ログイン管理の項目を出す。主パスワードでロックされていれば挿入を無効にする。候補の取得は updatePasswordManagerSubMenuItems に任せ、finally で項目の表示と区切り線を必ず整える。
- 触るとき: パスワード関連の項目が出ない条件や、ロック時の挙動を変えるとき。
- 呼び出し先: `PASSWORD_FIELDNAME_HINTS.includes()`, `Services.logins.getLoginSavingEnabled()`, `document.getElementById()`, `document.l10n.setAttributes()`, `lazy.LoginHelper.getLoginOrigin()`, `this.isLoginForm()`, `this.setItemAttr()`, `this.showItem()`, `this.updatePasswordManagerSubMenuItems()`
- 参照: `Services.logins.isLoggedIn`, `documentURI?.spec`, `lazy.LoginHelper.generationAvailable`, `lazy.LoginHelper.generationEnabled`, `loginFillInfo.activeField.fieldNameHint`, `loginFillInfo?.activeField.disabled`, `loginFillInfo?.passwordField.disabled`, `this.#passwordItemsAbortController`, `this.#passwordItemsAbortController.signal`, `this.#passwordItemsReady`, `this.contentData?.context.showRelay`, `this.contentData?.documentURIObject`, `this.contentData?.loginFillInfo`
- XPCOM: `Services.logins`

## nsContextMenu.passwordItemsReady()
- 位置: L1299-1301
- 役割: 保存済みログインの候補の取得が終わるまで待てる Promise を返す。テストが候補の到着を待つために使う。
- 触るとき: 候補の非同期な表示を待つテストを書くとき。
- 参照: `this.#passwordItemsReady`

## nsContextMenu.updatePasswordManagerSubMenuItems()
- 位置: async L1311-1330
- 役割: LoginManagerContextMenu から候補の断片を取得し、メニューを閉じられていなければ fill-login-popup に追加して、保存済みログインの項目を表示する。
- 触るとき: 候補の追加先や、メニューが閉じた後の取り消しの条件を変えるとき。
- 呼び出し先: `document.getElementById()`, `lazy.LoginManagerContextMenu.addLoginsToMenu()`, `popup.appendChild()`, `this.setItemAttr()`, `this.showItem()`
- 参照: `signal.aborted`, `this.browser`, `this.targetIdentifier`

## nsContextMenu.initSyncItems()
- 位置: L1332-1334
- 役割: gSync に同期関連の項目を更新させ、その結果を syncItemsShown に保存する。
- 触るとき: 端末への送信など同期項目の表示を変えるとき。
- 呼び出し先: `this.window.gSync.updateContentContextMenu()`
- 参照: `this.syncItemsShown`

## nsContextMenu.initViewSourceItems()
- 位置: L1336-1372
- 役割: ソース表示ページ(view-source)のときだけ、行へ移動、折り返し、構文の強調の項目を出す。ラベルとアクセスキーは localize された文字列から入れ、チェック状態は設定値から決める。
- 触るとき: view-source の項目の並びや設定との対応を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `showViewSourceItem()`, `this.browser.browsingContext.currentWindowGlobal?.documentURI?.schemeIs()`
- XPCOM: `Services.prefs`

## getString()
- 位置: L1337-1342
- 役割: ページアクターのバンドルから、指定名の文字列を取り出す。
- 触るとき: view-source 用の文字列の取り出し方を変えるとき。
- 呼び出し先: `bundle.GetStringFromName()`, `this.window.gViewSourceUtils.getPageActor()`
- 参照: `this.browser`

## showViewSourceItem()
- 位置: L1343-1358
- 役割: view-source の項目1つを表示する。view-source ページでなければ隠し、そうでなければチェック状態、ラベル、アクセスキーを設定する。
- 触るとき: view-source の項目を追加するとき。
- 呼び出し先: `check()`, `getString()`, `this.setItemAttr()`, `this.showItem()`
- 条件付き依存: `if (accesskey)` → `this.setItemAttr()`
- 条件付き依存: `if (accesskey)` → `getString()`

## nsContextMenu.showHideSeparators()
- 位置: L1377-1415
- 役割: 表示中の項目を順にたどり、区切り線が連続したり先頭や末尾に残ったりしないように隠す。サブメニューは再帰的に処理し、ensureHidden の付いた区切り線は必ず隠す。
- 触るとき: 項目の表示が変わって区切り線が二重に出るとき、または区切り線の隠し方を変えるとき。
- 呼び出し先: `menuItem.hasAttribute()`
- 条件付き依存: `if (menuItem.localName == "menuseparator")` → `menuItem.hasAttribute()`
- 条件付き依存: `if (menuItem.localName == "menu" && menuItem.menupopup)` → `this.showHideSeparators()`
- 条件付き依存: `if (menuItem.localName == "menugroup")` → `this.showHideSeparators()`
- 参照: `aPopup.children`, `lastVisibleSeparator.hidden`, `menuItem.hidden`, `menuItem.localName`, `menuItem.menupopup`

## nsContextMenu.shouldShowTakeScreenshot()
- 位置: L1417-1429
- 役割: スクリーンショット機能が有効で、タブ内で、テキスト入力・リンク・音声・編集欄・パスワード欄ではないときに true を返す。
- 触るとき: スクリーンショット項目を出す条件を変えるとき。
- 参照: `lazy.ScreenshotsUtils.screenshotsEnabled`, `this.inTabBrowser`, `this.onAudio`, `this.onEditable`, `this.onLink`, `this.onPassword`, `this.onPlainTextLink`, `this.onTextInput`

## nsContextMenu.initScreenshotItem()
- 位置: L1431-1442
- 役割: スクリーンショットの区切り線と撮影項目を表示する。ミニウィンドウの項目は、設定が有効でまだミニウィンドウ表示でないときだけ出す。
- 触るとき: スクリーンショットやミニウィンドウの項目の表示条件を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `this.document.documentElement.hasAttribute()`, `this.shouldShowTakeScreenshot()`, `this.showItem()`
- XPCOM: `Services.prefs`

## nsContextMenu.initPasswordControlItems()
- 位置: L1444-1454
- 役割: パスワード欄の上で、ポリシーで許されていれば「パスワードを表示」の項目を出し、表示状態のチェックを現在値に合わせる。
- 触るとき: パスワード表示の項目の条件を変えるとき。
- 呼び出し先: `Services.policies.isAllowed()`, `this.showItem()`
- 条件付き依存: `if (shouldShow)` → `this.document.getElementById()`
- 条件付き依存: `if (shouldShow)` → `revealPassword.toggleAttribute()`
- 参照: `this.onPassword`, `this.passwordRevealed`
- XPCOM: `Services.policies`

## nsContextMenu.toggleRevealPassword()
- 位置: L1456-1458
- 役割: 対象のパスワード欄の表示状態を切り替えるように、アクターに依頼する。
- 触るとき: パスワードの表示切り替えの経路を変えるとき。
- 呼び出し先: `this.actor.toggleRevealPassword()`
- 参照: `this.targetIdentifier`

## nsContextMenu.openPasswordManager()
- 位置: L1460-1464
- 役割: パスワードマネージャを、入口を Contextmenu として開く。
- 触るとき: 右クリックからパスワード管理を開くときの入口の値を変えるとき。
- 呼び出し先: `lazy.LoginHelper.openPasswordManager()`
- 参照: `this.window`

## nsContextMenu.useRelayMask()
- 位置: L1466-1470
- 役割: 現在の文書のログイン用オリジンを求め、対象の欄に Relay のマスクメールを入れるようアクターに依頼する。
- 触るとき: Relay のマスクの使い方や対象のオリジンの決め方を変えるとき。
- 呼び出し先: `lazy.LoginHelper.getLoginOrigin()`, `this.actor.useRelayMask()`
- 参照: `documentURI?.spec`, `this.contentData?.documentURIObject`, `this.targetIdentifier`

## nsContextMenu.useGeneratedPassword()
- 位置: L1472-1474
- 役割: 対象の欄に生成したパスワードを入れるよう LoginManagerContextMenu に依頼する。
- 触るとき: 生成パスワードの入力経路を変えるとき。
- 呼び出し先: `lazy.LoginManagerContextMenu.useGeneratedPassword()`
- 参照: `this.targetIdentifier`

## nsContextMenu.isLoginForm()
- 位置: L1476-1488
- 役割: パスワード欄が見つかっているか、ユーザー名だけの欄であれば true を返す。about: ページと PDF.js ビューアーは除く。
- 触るとき: ログインフォームと判定する条件を変えるとき、またはパスワード項目が出ないページを調べるとき。
- 呼び出し先: `documentURI?.schemeIs()`
- 参照: `loginFillInfo?.activeField.fieldNameHint`, `loginFillInfo?.passwordField?.found`, `this.browser.contentPrincipal.spec`, `this.contentData?.documentURIObject`, `this.contentData?.loginFillInfo`

## nsContextMenu.inspectNode()
- 位置: L1490-1495
- 役割: 選択中のタブで、対象ノードを DevTools の検証で開くよう DevToolsShim に依頼する。
- 触るとき: 検証(Inspect)の起動経路を変えるとき。
- 呼び出し先: `lazy.DevToolsShim.inspectNode()`
- 参照: `this.targetIdentifier`, `this.window.gBrowser.selectedTab`

## nsContextMenu.inspectA11Y()
- 位置: L1497-1502
- 役割: 選択中のタブで、対象ノードをアクセシビリティ検証で開くよう DevToolsShim に依頼する。
- 触るとき: アクセシビリティ検証の起動経路を変えるとき。
- 呼び出し先: `lazy.DevToolsShim.inspectA11Y()`
- 参照: `this.targetIdentifier`, `this.window.gBrowser.selectedTab`

## nsContextMenu._openLinkInParameters()
- 位置: L1504-1539
- 役割: 開くリンクの共通パラメータを作る。文字コード、起点の principal、リファラーの情報、フレーム ID を入れ、引数 extra で上書きする。別のコンテナへ開く場合やプレーンテキストのリンクでは、リファラーを作り直して送らないようにする。
- 触るとき: リンクを開く全経路に渡す値を変えるとき、またはリファラーが送られない理由を調べるとき。
- 参照: `lazy.ReferrerInfo`, `params.referrerInfo`, `params.userContextId`, `referrerInfo.originalReferrer`, `referrerInfo.referrerPolicy`, `this.contentData.charSet`, `this.contentData.frameID`, `this.contentData.linkReferrerInfo`, `this.contentData.referrerInfo`, `this.contentData.userContextId`, `this.onLink`, `this.onPlainTextLink`, `this.policyContainer`, `this.principal`, `this.remoteType`, `this.storagePrincipal`

## nsContextMenu._getGlobalHistoryOptions()
- 位置: L1541-1563
- 役割: スポンサーリンクの起点情報を globalHistoryOptions にまとめる。ニュータブ由来のリンクか、ブラウザに付いた triggeringSponsoredURL があれば返し、無ければ空を返す。
- 触るとき: スポンサー付きリンクの履歴記録を変えるとき。
- 条件付き依存: `if (!(this.isSponsoredLink))` → `this.browser.hasAttribute()`
- 条件付き依存: `if (this.browser.hasAttribute("triggeringSponsoredURL"))` → `this.browser.getAttribute()`
- 参照: `this.isSponsoredLink`, `this.linkURL`

## nsContextMenu.openLink()
- 位置: L1566-1574
- 役割: リンク先を新しいウィンドウで開く。
- 触るとき: リンクを新しいウィンドウで開くときの挙動を変えるとき。
- 呼び出し先: `this._getGlobalHistoryOptions()`, `this._openLinkInParameters()`, `this.window.openLinkIn()`
- 参照: `this.linkURL`

## nsContextMenu.openLinkInPrivateWindow()
- 位置: L1577-1583
- 役割: リンク先をプライベートウィンドウで開く。
- 触るとき: プライベートウィンドウでの表示条件や挙動を変えるとき。
- 呼び出し先: `this._openLinkInParameters()`, `this.window.openLinkIn()`
- 参照: `this.linkURL`

## nsContextMenu.openLinkInSmartWindow()
- 位置: L1586-1593
- 役割: リンク先を AI ウィンドウで開く。aiWindow フラグを付けて、スポンサー情報も引き継ぐ。
- 触るとき: AI ウィンドウで開く動作を変えるとき。
- 呼び出し先: `this._getGlobalHistoryOptions()`, `this._openLinkInParameters()`, `this.window.openLinkIn()`
- 参照: `this.linkURL`

## nsContextMenu.openLinkInTab()
- 位置: L1596-1608
- 役割: リンク先を新しいタブで開く。コンテナのユーザーコンテキスト ID を右クリック項目の data-usercontextid から読み、スポンサー情報を付ける。
- 触るとき: 新しいタブで開くときのコンテナ指定や呼び出し元の情報を変えるとき。
- 呼び出し先: `event.target.getAttribute()`, `parseInt()`, `this._getGlobalHistoryOptions()`, `this._openLinkInParameters()`, `this.window.openLinkIn()`
- 参照: `this.linkURL`

## nsContextMenu.openLinkInSplitView()
- 位置: L1611-1631
- 役割: リンク先を新しいタブで開き、開いた後に現在のタブと分割表示にする。現在のタブを挿入位置にし、そのタブを選択する。
- 触るとき: 分割表示で開く並びや選択の挙動を変えるとき。
- 呼び出し先: `this._getGlobalHistoryOptions()`, `this._openLinkInParameters()`, `win.gBrowser.getTabForBrowser()`, `win.openLinkIn()`
- 参照: `currentTab.userContextId`, `this.browser`, `this.linkURL`, `this.window`

## resolveOnNewTabCreated()
- 位置: L1619-1627
- 役割: 新しいタブが作られたときに呼ばれる。リンク先のタブと現在のタブが両方あれば、分割表示のグループを作ってリンク先のタブを選択する。
- 触るとき: 分割表示のグループを作るタイミングを変えるとき。
- 呼び出し先: `win.gBrowser.getTabForBrowser()`
- 条件付き依存: `if (linkTab && currentTab)` → `win.gBrowser.addTabSplitView()`
- 参照: `win.gBrowser.selectedTab`

## nsContextMenu.openLinkInCurrent()
- 位置: L1634-1640
- 役割: リンク先を現在のタブで開く。プレーンテキストのリンク項目で使う。
- 触るとき: 現在のタブで開く条件を変えるとき。
- 呼び出し先: `this._openLinkInParameters()`, `this.window.openLinkIn()`
- 参照: `this.linkURL`

## nsContextMenu.openFrameInTab()
- 位置: L1643-1650
- 役割: クリックしたフレームの URL を新しいタブで開く。フレームのリファラーとブラウザの principal を使う。
- 触るとき: フレームを新しいタブで開く際のリファラーや principal を変えるとき。
- 呼び出し先: `this.window.openLinkIn()`
- 参照: `this.browser.contentPrincipal`, `this.browser.policyContainer`, `this.contentData.charSet`, `this.contentData.docLocation`, `this.contentData.frameReferrerInfo`

## nsContextMenu.reloadFrame()
- 位置: L1653-1656
- 役割: クリックしたフレームを再読み込みするよう依頼する。Shift を押していればキャッシュを使わず強制的に読み直す。
- 触るとき: フレーム再読み込みのキャッシュ扱いを変えるとき。
- 呼び出し先: `this.actor.reloadFrame()`
- 参照: `aEvent.shiftKey`, `this.targetIdentifier`

## nsContextMenu.openFrame()
- 位置: L1659-1666
- 役割: クリックしたフレームを別ウィンドウで開く。
- 触るとき: フレームを別ウィンドウで開く挙動を変えるとき。
- 呼び出し先: `this.window.openLinkIn()`
- 参照: `this.browser.contentPrincipal`, `this.browser.policyContainer`, `this.contentData.charSet`, `this.contentData.docLocation`, `this.contentData.frameReferrerInfo`

## nsContextMenu.showOnlyThisFrame()
- 位置: L1669-1679
- 役割: URL のセキュリティ検査をしたうえで、フレームの URL を現在のタブで開く。
- 触るとき: このフレームだけを表示する挙動や検査の条件を変えるとき。
- 呼び出し先: `this.window.openWebLinkIn()`, `this.window.urlSecurityCheck()`
- 参照: `Ci.nsIScriptSecurityManager.DISALLOW_SCRIPT`, `this.browser.contentPrincipal`, `this.contentData.docLocation`, `this.contentData.frameReferrerInfo`
- XPCOM: `nsIScriptSecurityManager`

## nsContextMenu.takeScreenshot()
- 位置: L1681-1687
- 役割: menuitem-screenshot の通知を出して、スクリーンショット機能を開始させる。
- 触るとき: スクリーンショットの起動経路を変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`
- 参照: `this.window`
- XPCOM: `Services.obs`

## nsContextMenu.useMiniWindow()
- 位置: L1689-1693
- 役割: ScreenshotsUtils の toggle を、ミニウィンドウの選択モードで呼ぶ。
- 触るとき: ミニウィンドウのスクリーンショットの起動条件を変えるとき。
- 呼び出し先: `lazy.ScreenshotsUtils.toggle()`
- 参照: `lazy.SELECTION_MODES.MINI_WINDOW`, `this.browser`

## nsContextMenu.viewPartialSource()
- 位置: L1696-1733
- 役割: 選択範囲のソースを表示する。ソースを開く先のタブを、現在のウィンドウか新しいウィンドウかの設定に応じて作り、ページのソース表示を依頼する。
- 触るとき: 選択範囲のソース表示先のウィンドウやタブの決め方を変えるとき。
- 呼び出し先: `this.window.gViewSourceUtils.viewPartialSourceInBrowser()`
- 参照: `this.actor.browsingContext`

## openSelectionFn()
- 位置: async L1698-1727
- 役割: viewPartialSource が使う関数。適切な tab browser を選んで about:blank のタブを作り、新しいウィンドウの設定ならタブを隠してウィンドウに置き換え、その browser を返す。
- 触るとき: 選択範囲のソースを開くタブの作り方を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `tabBrowser.addTab()`, `tabBrowser.getBrowserForTab()`
- 条件付き依存: `if (!tabBrowser || !tabBrowser.addTab || !this.window.toolbar.visible)` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (!tabBrowser || !tabBrowser.addTab || !this.window.toolbar.visible)` → `lazy.BrowserWindowTracker.promiseOpenWindow()`
- 条件付き依存: `if (inNewWindow)` → `tabBrowser.hideTab()`
- 条件付き依存: `if (inNewWindow)` → `tabBrowser.replaceTabsWithWindow()`
- 参照: `browserWindow.gBrowser`, `tabBrowser.addTab`, `tabBrowser?.selectedBrowser`, `this.window.gBrowser`, `this.window.toolbar.visible`
- XPCOM: `Services.prefs` / `Services.scriptSecurityManager`

## nsContextMenu.viewFrameSource()
- 位置: L1736-1742
- 役割: クリックしたフレームのソースを view-source で開く。
- 触るとき: フレームのソース表示の経路を変えるとき。
- 呼び出し先: `this.window.BrowserCommands.viewSourceOfDocument()`
- 参照: `this.browser`, `this.contentData.docLocation`, `this.frameOuterWindowID`

## nsContextMenu.viewInfo()
- 位置: L1744-1752
- 役割: フレームのページ情報を、既定のタブで開く。
- 触るとき: ページ情報を開く経路を変えるとき。
- 呼び出し先: `this.window.BrowserCommands.pageInfo()`
- 参照: `this.browser`, `this.contentData.docLocation`

## nsContextMenu.viewImageInfo()
- 位置: L1754-1762
- 役割: 画像の情報をページ情報のメディアタブで開き、クリックした画像の情報を渡す。
- 触るとき: 画像情報の表示経路や渡す値を変えるとき。
- 呼び出し先: `this.window.BrowserCommands.pageInfo()`
- 参照: `this.browser`, `this.contentData.docLocation`, `this.imageInfo`

## nsContextMenu.viewImageDesc()
- 位置: L1764-1776
- 役割: 画像の説明 URL をセキュリティ検査してから、openUILink で開く。
- 触るとき: 画像の説明リンクの開き方を変えるとき。
- 呼び出し先: `this.window.openUILink()`, `this.window.urlSecurityCheck()`
- 参照: `Ci.nsIScriptSecurityManager.DISALLOW_SCRIPT`, `this.contentData.referrerInfo`, `this.imageDescURL`, `this.policyContainer`, `this.principal`, `this.remoteType`
- XPCOM: `nsIScriptSecurityManager`

## nsContextMenu.viewFrameInfo()
- 位置: L1778-1786
- 役割: フレームのページ情報を、そのフレームのブラウジングコンテキストを指定して開く。
- 触るとき: フレームのページ情報の対象を変えるとき。
- 呼び出し先: `this.window.BrowserCommands.pageInfo()`
- 参照: `this.actor.browsingContext`, `this.browser`, `this.contentData.docLocation`

## nsContextMenu.reloadImage()
- 位置: L1788-1795
- 役割: 画像の URL をセキュリティ検査してから、画像の再読み込みをアクターに依頼する。
- 触るとき: 画像の再読み込みの経路を変えるとき。
- 呼び出し先: `this.actor.reloadImage()`, `this.window.urlSecurityCheck()`
- 参照: `Ci.nsIScriptSecurityManager.DISALLOW_SCRIPT`, `this.mediaURL`, `this.principal`, `this.targetIdentifier`
- XPCOM: `nsIScriptSecurityManager`

## nsContextMenu.#canvasToBlobURL()
- 位置: async L1797-1805
- 役割: キャンバスの内容を子プロセスで blob URL にしてもらい、その URL が現在の principal で有効かを確かめて返す。無効なら例外を投げる。
- 触るとき: キャンバス画像の blob URL の扱いを変えるとき。
- 呼び出し先: `ChromeUtils.isBlobURLValid()`, `this.actor.canvasToBlobURL()`
- 参照: `this.principal`

## nsContextMenu.copyCanvasImage()
- 位置: L1807-1814
- 役割: キャンバスを blob にして ArrayBuffer に変え、画像としてクリップボードへコピーする。
- 触るとき: キャンバス画像のコピー方法を変えるとき。
- 呼び出し先: `blob.arrayBuffer()`, `lazy.BrowserUtils.copyImageToClipboard()`, `this.actor .canvasToBlob()`, `this.actor .canvasToBlob(this.targetIdentifier) .then()`, `this.actor .canvasToBlob(this.targetIdentifier) .then(blob => blob.arrayBuffer()) .then()`
- 参照: `console.error`, `this.targetIdentifier`

## nsContextMenu.viewMedia()
- 位置: L1817-1850
- 役割: 画像、動画、音声の URL を開く。キャンバスは blob URL にしてから開く。その他は許可された chrome 画像なら system principal、そうでなければ現在の principal で検査して、新しいタブなどに開く。
- 触るとき: メディアを開く先や principal の判定を変えるとき。
- 呼び出し先: `Services.scriptSecurityManager.getSystemPrincipal()`, `lazy.BrowserUtils.whereToOpenLink()`
- 条件付き依存: `if (this.onCanvas)` → `this.#canvasToBlobURL(this.targetIdentifier).then()`
- 条件付き依存: `if (this.onCanvas)` → `this.#canvasToBlobURL()`
- 条件付き依存: `if (this.onCanvas)` → `this.window.openLinkIn()`
- 条件付き依存: `if (!(this.onCanvas))` → `ALLOWED_CHROME_IMAGE_URLS.has()`
- 条件付き依存: `if (!(this.onCanvas))` → `this.window.urlSecurityCheck()`
- 条件付き依存: `if (!(this.onCanvas))` → `this.window.openLinkIn()`
- 参照: `Ci.nsIScriptSecurityManager.DISALLOW_SCRIPT`, `console.error`, `this.contentData.referrerInfo`, `this.mediaURL`, `this.onCanvas`, `this.policyContainer`, `this.principal`, `this.remoteType`, `this.targetIdentifier`
- XPCOM: `nsIScriptSecurityManager` / `Services.scriptSecurityManager`

## nsContextMenu.saveVideoFrameAsImage()
- 位置: L1852-1894
- 役割: 動画の現在のフレームを子プロセスから JPEG として受け取り、URL のファイル名から作った名前で internalSave により保存する。ファイル名が無ければ snapshot.jpg にする。
- 触るとき: 動画のスナップショット保存の名前や保存方法を変えるとき。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isBrowserPrivate()`, `this.actor.saveVideoFrameAsImage()`, `this.actor.saveVideoFrameAsImage(this.targetIdentifier).then()`, `this.window.internalSave()`
- 条件付き依存: `if (this.mediaURL)` → `this.window.makeURI()`
- 条件付き依存: `if (this.mediaURL)` → `uri.QueryInterface()`
- 条件付き依存: `if (url.fileBaseName)` → `decodeURI()`
- 参照: `Ci.nsIURL`, `this.browser`, `this.contentData.cookieJarSettings`, `this.contentData.referrerInfo`, `this.mediaURL`, `this.principal`, `this.targetIdentifier`, `url.fileBaseName`
- XPCOM: [`nsIURL`](../../../netwerk/base/nsIURL.idl.md)

## nsContextMenu.leaveDOMFullScreen()
- 位置: L1896-1898
- 役割: ドキュメントの全画面表示を終了する。
- 触るとき: 全画面終了の挙動を変えるとき。
- 呼び出し先: `this.document.exitFullscreen()`

## nsContextMenu.viewBGImage()
- 位置: L1901-1915
- 役割: 背景画像の URL をセキュリティ検査し、openUILink で開く。現在のコードは this.bgImageURL を読むが、この名前は setContext で代入されない(要確認: 実際には mediaURL に入る値)。
- 触るとき: 背景画像を開く経路を直すとき、または背景画像の項目で URL が空になる理由を調べるとき。
- 呼び出し先: `this.window.openUILink()`, `this.window.urlSecurityCheck()`
- 参照: `Ci.nsIScriptSecurityManager.DISALLOW_SCRIPT`, `this.bgImageURL`, `this.contentData.referrerInfo`, `this.policyContainer`, `this.principal`, `this.remoteType`
- XPCOM: `nsIScriptSecurityManager`

## nsContextMenu.setDesktopBackground()
- 位置: L1917-1968
- 役割: ポリシーで許可されていれば、子プロセスで画像を取り出し、デスクトップ背景の設定ダイアログを開く。macOS では既存のダイアログがあれば再利用し、他の OS ではモーダルのダイアログを出す。
- 触るとき: デスクトップ背景の設定の流れや、ダイアログの開き方を変えるとき。
- 呼び出し先: `Services.policies.isAllowed()`, `this.actor .setAsDesktopBackground()`, `this.actor .setAsDesktopBackground(this.targetIdentifier) .then()`, `this.document.createElementNS()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `Services.wm.getMostRecentWindow()`
- 条件付き依存: `if (dbWin)` → `dbWin.gSetBackground.init()`
- 条件付き依存: `if (dbWin)` → `dbWin.focus()`
- 条件付き依存: `if (!(dbWin))` → `this.window.openDialog()`
- 条件付き依存: `if (!(AppConstants.platform == "macosx"))` → `this.window.openDialog()`
- 参照: `AppConstants.platform`, `image.src`, `this.targetIdentifier`
- XPCOM: `Services.policies` / `Services.wm`

## nsContextMenu.saveFrame()
- 位置: L1971-1973
- 役割: クリックしたフレームを saveBrowser で保存する。
- 触るとき: フレームの保存範囲を変えるとき。
- 呼び出し先: `this.window.saveBrowser()`
- 参照: `this.browser`, `this.frameBrowsingContext`

## nsContextMenu.saveHelper()
- 位置: L1977-2174
- 役割: リンクを「名前を付けて保存」するための共通処理。新しいチャンネルを作り、受け取ったヘッダーで保存ダイアログを出す。一定時間でヘッダーが来なければ従来の保存に切り替え、認証要求が来たら取り消す。
- 触るとき: リンク保存のタイムアウトや、保存に渡すリファラーや Cookie の扱いを変えるとき。
- 呼び出し先: `Cc["@mozilla.org/timer;1"].createInstance()`, `Services.prefs.getIntPref()`, `channel.asyncOpen()`, `lazy.NetUtil.newChannel()`, `this.window.makeURI()`, `timer.initWithCallback()`
- 条件付き依存: `if (channel instanceof Ci.nsIPrivateBrowsingChannel)` → `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- 条件付き依存: `if (channel instanceof Ci.nsIPrivateBrowsingChannel)` → `channel.setPrivate()`
- 参照: `Ci.nsICachingChannel`, `Ci.nsICachingChannel.LOAD_BYPASS_LOCAL_CACHE_IF_BUSY`, `Ci.nsIChannel.LOAD_CALL_CONTENT_SNIFFERS`, `Ci.nsIContentPolicy.TYPE_SAVEAS_DOWNLOAD`, `Ci.nsIHttpChannel`, `Ci.nsIHttpChannelInternal`, `Ci.nsILoadInfo.SEC_ALLOW_CROSS_ORIGIN_INHERITS_SEC_CONTEXT`, `Ci.nsIPrivateBrowsingChannel`, `Ci.nsIRequest.LOAD_BYPASS_CACHE`, `Ci.nsITimer`, `callbacks.prototype`, `channel.contentDispositionFilename`, `channel.forceAllowThirdPartyCookie`, `channel.loadFlags`, `channel.loadInfo.cookieJarSettings`, `channel.notificationCallbacks`, `channel.referrerInfo`, `saveAsListener.prototype`, `this.browser`, `this.principal`, `this.window`, `timer.TYPE_ONE_SHOT`, `timerCallback.prototype`
- XPCOM: [`nsICachingChannel`](../../../netwerk/base/nsICachingChannel.idl.md) / [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIContentPolicy`](../../../dom/base/nsIContentPolicy.idl.md) / [`nsIHttpChannel`](../../../netwerk/protocol/http/nsIHttpChannel.idl.md) / [`nsIHttpChannelInternal`](../../../netwerk/protocol/http/nsIHttpChannelInternal.idl.md) / [`nsILoadInfo`](../../../dom/base/nsIContentPolicy.idl.md) / [`nsIPrivateBrowsingChannel`](../../../netwerk/base/nsIPrivateBrowsingChannel.idl.md) / [`nsIRequest`](../../../docshell/base/nsIDocShell.idl.md) / [`nsITimer`](../../../xpcom/threads/nsITimer.idl.md) / `@mozilla.org/timer;1` / `Services.prefs`

## saveAsListener()
- 位置: L1993-1996
- 役割: 保存用のリスナーを作るコンストラクター。受け取った principal と window を保持し、後の保存処理で使う。
- 触るとき: 保存リスナーが持つ情報を増やすとき。
- 参照: `this._triggeringPrincipal`, `this._window`

## saveLinkAs_onStartRequest()
- 位置: L2000-2055
- 役割: リクエスト開始時の処理。タイムアウトなら何もせず、失敗していれば拡張機能や一般のエラーを警告で示す。成功していれば外部ヘルパーのリスナーに処理を渡す。
- 触るとき: 保存時のエラー表示の内容や、外部ヘルパーに渡す条件を変えるとき。
- 呼び出し先: `Cc[ "@mozilla.org/uriloader/external-helper-app-service;1" ].getService()`, `Components.isSuccessCode()`, `aRequest.QueryInterface()`, `extHelperAppSvc.doContent()`, `this.extListener.onStartRequest()`, `timer.cancel()`
- 条件付き依存: `if (!Components.isSuccessCode(aRequest.status))` → `aRequest.QueryInterface()`
- 条件付き依存: `if ( reason == Ci.nsILoadInfo.BLOCKING_REASON_EXTENSION_WEBREQUEST )` → `channel.QueryInterface()`
- 条件付き依存: `if ( reason == Ci.nsILoadInfo.BLOCKING_REASON_EXTENSION_WEBREQUEST )` → `properties.getProperty()`
- 条件付き依存: `if ( reason == Ci.nsILoadInfo.BLOCKING_REASON_EXTENSION_WEBREQUEST )` → `l10n.formatValueSync()`
- 条件付き依存: `if ( reason == Ci.nsILoadInfo.BLOCKING_REASON_EXTENSION_WEBREQUEST )` → `WebExtensionPolicy.getByID()`
- 条件付き依存: `if (!Components.isSuccessCode(aRequest.status))` → `l10n.formatValueSync()`
- 条件付き依存: `if (!Components.isSuccessCode(aRequest.status))` → `Services.wm.getOuterWindowWithId()`
- 条件付き依存: `if (!Components.isSuccessCode(aRequest.status))` → `Services.prompt.alert()`
- 参照: `Ci.nsIChannel`, `Ci.nsIExternalHelperAppService`, `Ci.nsILoadInfo.BLOCKING_REASON_EXTENSION_WEBREQUEST`, `Ci.nsIPropertyBag`, `Cr.NS_ERROR_SAVE_LINK_AS_TIMEOUT`, `WebExtensionPolicy.getByID(id).name`, `aRequest.status`, `channel.contentType`, `channel.loadInfo.requestBlockingReason`, `this._window`, `this.extListener`
- XPCOM: [`nsIChannel`](../../../docshell/base/nsIDocShell.idl.md) / [`nsIExternalHelperAppService`](../../../uriloader/exthandler/nsIExternalHelperAppService.idl.md) / [`nsILoadInfo`](../../../dom/base/nsIContentPolicy.idl.md) / [`nsIPropertyBag`](../../../toolkit/components/passwordmgr/nsILoginManager.idl.md) / `@mozilla.org/uriloader/external-helper-app-service;1` / `Services.prompt` / `Services.wm`

## saveLinkAs_onStopRequest()
- 位置: L2057-2078
- 役割: リクエスト終了時の処理。タイムアウトだった場合は従来の saveURL で保存し、外部ヘルパーのリスナーにも終了を伝える。
- 触るとき: タイムアウト後の保存方法を変えるとき。
- 条件付き依存: `if (aStatusCode == Cr.NS_ERROR_SAVE_LINK_AS_TIMEOUT)` → `this._window.saveURL()`
- 条件付き依存: `if (this.extListener)` → `this.extListener.onStopRequest()`
- 参照: `Cr.NS_ERROR_SAVE_LINK_AS_TIMEOUT`, `this._triggeringPrincipal`, `this.extListener`

## saveLinkAs_onDataAvailable()
- 位置: L2080-2092
- 役割: データが届いたとき、外部ヘルパーのリスナーに受け渡す。
- 触るとき: 保存データの受け渡し方を変えるとき。
- 呼び出し先: `this.extListener.onDataAvailable()`

## callbacks()
- 位置: L2095-2095
- 役割: チャンネルの通知先となるコンストラクター。認証を求められたときに保存のタイマーを止めてチャンネルを取り消すために使う。
- 触るとき: 保存中の認証要求の扱いを変えるとき。

## sLA_callbacks_getInterface()
- 位置: L2097-2108
- 役割: 認証プロンプトの要求に対し、タイマーを止めてチャンネルを取り消し、それ以外の要求には NS_ERROR_NO_INTERFACE を返す。
- 触るとき: 保存中に認証の要求が来た時の挙動を変えるとき。
- 呼び出し先: `Components.Exception()`, `aIID.equals()`
- 条件付き依存: `if (aIID.equals(Ci.nsIAuthPrompt) || aIID.equals(Ci.nsIAuthPrompt2))` → `timer.cancel()`
- 条件付き依存: `if (aIID.equals(Ci.nsIAuthPrompt) || aIID.equals(Ci.nsIAuthPrompt2))` → `channel.cancel()`
- 参照: `Ci.nsIAuthPrompt`, `Ci.nsIAuthPrompt2`, `Cr.NS_ERROR_NO_INTERFACE`, `Cr.NS_ERROR_SAVE_LINK_AS_TIMEOUT`
- XPCOM: [`nsIAuthPrompt`](../../../netwerk/base/nsIAuthPrompt.idl.md) / [`nsIAuthPrompt2`](../../../netwerk/base/nsIAuthPrompt2.idl.md)

## timerCallback()
- 位置: L2114-2114
- 役割: 保存用のタイマーが満了したときに呼ばれるコンストラクター。
- 触るとき: タイムアウトの通知方法を変えるとき。

## sLA_timer_notify()
- 位置: L2116-2118
- 役割: タイマーの期限切れで、チャンネルを NS_ERROR_SAVE_LINK_AS_TIMEOUT で取り消す。その後は onStopRequest が従来の保存に切り替える。
- 触るとき: 保存のタイムアウトの長さや切り替えの条件を見直すとき。
- 呼び出し先: `channel.cancel()`
- 参照: `Cr.NS_ERROR_SAVE_LINK_AS_TIMEOUT`

## nsContextMenu.saveLink()
- 位置: L2177-2195
- 役割: クリックしたリンクの参照元情報(リンクか通常のもの)と Cookie 設定を選び、saveHelper で保存する。ブラウザがプライベートかどうかも渡す。
- 触るとき: リンク保存時の参照元や Cookie の扱いを変えるとき。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isBrowserPrivate()`, `this.saveHelper()`
- 参照: `this.browser`, `this.contentData.cookieJarSettings`, `this.contentData.linkReferrerInfo`, `this.contentData.referrerInfo`, `this.frameOuterWindowID`, `this.linkDownload`, `this.linkTextStr`, `this.linkURL`, `this.onLink`, `this.ownerDoc`

## nsContextMenu.saveImage()
- 位置: L2198-2202
- 役割: 互換用の窓口。キャンバスか画像のときだけ saveMedia に処理を渡す。
- 触るとき: 古い呼び出し元が saveImage を使い続けているか確認するとき。
- 条件付き依存: `if (this.onCanvas || this.onImage)` → `this.saveMedia()`
- 参照: `this.onCanvas`, `this.onImage`

## nsContextMenu.saveMedia()
- 位置: L2205-2281
- 役割: クリックしたメディアを保存する。キャンバスは blob URL を canvas.png として保存し、画像は許可された chrome 画像なら system principal で検査して保存し、動画と音声は saveHelper で保存する。data: の動画と音声には既定の名前を付ける。
- 触るとき: メディアの保存先の principal や既定のファイル名を変えるとき。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- 条件付き依存: `if (this.onCanvas)` → `this.#canvasToBlobURL(this.targetIdentifier).then()`
- 条件付き依存: `if (this.onCanvas)` → `this.#canvasToBlobURL()`
- 条件付き依存: `if (this.onCanvas)` → `this.window.internalSave()`
- 条件付き依存: `if (this.onImage)` → `ALLOWED_CHROME_IMAGE_URLS.has()`
- 条件付き依存: `if (this.onImage)` → `Services.scriptSecurityManager.getSystemPrincipal()`
- 条件付き依存: `if (this.onImage)` → `this.window.urlSecurityCheck()`
- 条件付き依存: `if (this.onImage)` → `this.window.internalSave()`
- 条件付き依存: `if (this.onVideo || this.onAudio)` → `this.mediaURL.startsWith()`
- 条件付き依存: `if (this.mediaURL.startsWith("data"))` → `this.window.ContentAreaUtils.stringBundle.GetStringFromName()`
- 条件付き依存: `if (this.onVideo || this.onAudio)` → `this.saveHelper()`
- 参照: `console.error`, `this.browser`, `this.contentData.contentDisposition`, `this.contentData.contentType`, `this.contentData.cookieJarSettings`, `this.contentData.referrerInfo`, `this.document.nodePrincipal`, `this.frameOuterWindowID`, `this.mediaURL`, `this.onAudio`, `this.onCanvas`, `this.onImage`, `this.onVideo`, `this.ownerDoc`, `this.principal`, `this.targetIdentifier`
- XPCOM: `Services.scriptSecurityManager`

## nsContextMenu.sendImage()
- 位置: L2284-2288
- 役割: 互換用の窓口。キャンバスか画像のときだけ sendMedia を呼ぶ。
- 触るとき: 古い呼び出し元が sendImage を使い続けているか確認するとき。
- 条件付き依存: `if (this.onCanvas || this.onImage)` → `this.sendMedia()`
- 参照: `this.onCanvas`, `this.onImage`

## nsContextMenu.sendMedia()
- 位置: L2290-2292
- 役割: メディアの URL を MailIntegration でメールに添付して送る。
- 触るとき: メールで送る方法を変えるとき。
- 呼び出し先: `this.window.MailIntegration.sendMessage()`
- 参照: `this.mediaURL`

## nsContextMenu.copyEmail()
- 位置: L2295-2318
- 役割: mailto リンクからクエリより前の宛先だけを取り出し、URL デコードして、クリップボードにコピーする。
- 触るとき: メールアドレスのコピー形式を変えるとき。
- 呼び出し先: `Services.textToSubURI.unEscapeURIForUI()`, `lazy.clipboard.copyString()`, `url.indexOf()`, `url.substr()`, `url.substring()`
- 参照: `this.actor.manager.browsingContext.currentWindowGlobal`, `this.linkURL`
- XPCOM: `Services.textToSubURI`

## nsContextMenu.copyPhone()
- 位置: L2321-2338
- 役割: tel: リンクから先頭の4文字を除いて電話番号を取り出し、URL デコードしてクリップボードにコピーする。
- 触るとき: 電話番号のコピー形式を変えるとき。
- 呼び出し先: `Services.textToSubURI.unEscapeURIForUI()`, `lazy.clipboard.copyString()`, `url.substr()`
- 参照: `this.actor.manager.browsingContext.currentWindowGlobal`, `this.linkURL`
- XPCOM: `Services.textToSubURI`

## nsContextMenu.copyLink()
- 位置: L2340-2347
- 役割: リンク URL から view-source: の接頭辞を外してクリップボードにコピーする。
- 触るとき: リンクのコピー内容を変えるとき。
- 呼び出し先: `lazy.clipboard.copyString()`, `url.replace()`
- 参照: `this.actor.manager.browsingContext.currentWindowGlobal`, `this.linkURL`

## nsContextMenu.previewLink()
- 位置: L2349-2353
- 役割: view-source: の接頭辞を外した URL を LinkPreview に渡して、プレビューを開く。
- 触るとき: リンクプレビューへの渡し方を変えるとき。
- 呼び出し先: `lazy.LinkPreview.handleContextMenuClick()`, `url.replace()`
- 参照: `this.linkURL`

## nsContextMenu.copyStrippedLink()
- 位置: L2360-2370
- 役割: リンクからトラッキング用のパラメータを取り除き、表示用の URL にしてクリップボードにコピーする。取り除けない場合は元の URL をそのまま使う。
- 触るとき: クリーンリンクのコピー内容を変えるとき。
- 呼び出し先: `Services.io.createExposableURI()`, `this.getStrippedLink()`
- 条件付き依存: `if (strippedLinkURL)` → `lazy.clipboard.copyString()`
- 参照: `Services.io.createExposableURI(strippedLinkURI)?.displaySpec`, `this.actor.manager.browsingContext.currentWindowGlobal`, `this.linkURI`
- XPCOM: `Services.io`

## nsContextMenu.addSearchFieldAsEngine()
- 位置: async L2372-2405
- 役割: 検索欄の情報を子プロセスから受け取り、追加ダイアログで名前とエイリアスを入力させ、確定したら SearchService に検索エンジンとして追加して、URL バーで検索を開始する。
- 触るとき: 検索欄からの検索エンジン追加の手順や保存内容を変えるとき。
- 呼び出し先: `Services.io.newURI()`, `formData.values()`, `this.actor.getSearchFieldEngineData()`, `this.window.gDialogBox.open()`
- 条件付き依存: `if (engineInfo)` → `lazy.SearchService.addUserEngine()`
- 条件付き依存: `if (engineInfo)` → `this.window.gURLBar.search()`
- 参照: `Services.io.newURI(url).host`, `engineInfo.alias`, `engineInfo.name`, `this.targetIdentifier`
- XPCOM: `Services.io`

## nsContextMenu.showItem()
- 位置: L2419-2427
- 役割: ID か要素で指定された項目の hidden を、表示フラグの否定に設定する。要素が無ければ何もしない。
- 触るとき: 項目の表示切り替えの仕組みを変えるとき。
- 呼び出し先: `this.document.getElementById()`
- 参照: `aItemOrId.constructor`, `item.hidden`

## nsContextMenu.setItemAttr()
- 位置: L2432-2453
- 役割: 項目の属性を設定する。値が null なら属性を外し、真偽値なら真のときだけ付け、それ以外は値を入れる。
- 触るとき: 項目の disabled や checked の設定方法を変えるとき。
- 呼び出し先: `elem.setAttribute()`, `this.document.getElementById()`
- 条件付き依存: `if (aVal == null)` → `elem.removeAttribute()`
- 条件付き依存: `if (aVal)` → `elem.setAttribute()`
- 条件付き依存: `if (!(aVal))` → `elem.removeAttribute()`

## nsContextMenu.cloneNode()
- 位置: L2456-2469
- 役割: 指定の要素と同じタグ名と属性を持つ要素を作る。XUL の DOM API が足りない回避策。
- 触るとき: メニュー項目を複製する処理を追加・変更するとき。
- 呼び出し先: `attrs.item()`, `node.setAttribute()`, `this.document.createElement()`
- 参照: `aItem.attributes`, `aItem.tagName`, `attr.nodeName`, `attr.nodeValue`, `attrs.length`

## nsContextMenu.getLinkURI()
- 位置: L2471-2479
- 役割: URL 文字列を nsIURI にする。失敗したら null を返す。
- 触るとき: リンク URL の解析方法を変えるとき。
- 呼び出し先: `this.window.makeURI()`
- 参照: `this.linkURL`

## nsContextMenu.getStrippedLink()
- 位置: L2487-2502
- 役割: URI から既知のトラッキング用パラメータを除く。除けるものが無ければ元の URI を返し、例外時も元の URI を返す。
- 触るとき: 除去対象のパラメータを増やすとき、またはクリーンリンクが元の URL のままになる理由を調べるとき。
- 呼び出し先: `console.warn()`, `lazy.QueryStringStripper.stripForCopyOrShare()`
- 参照: `e.message`, `this.linkURI`

## nsContextMenu.#canStripParams()
- 位置: L2509-2519
- 役割: QueryStringStripper でパラメータを除けるかを調べる。例外時は false を返す。
- 触るとき: クリーンリンクの項目を有効にする条件を変えるとき。
- 呼び出し先: `console.warn()`, `lazy.QueryStringStripper.canStripForShare()`
- 参照: `this.linkURI`

## nsContextMenu.isSecureAboutPage()
- 位置: L2526-2536
- 役割: 現在の URL が about: ページで、そのモジュールが安全なブラウザ UI(IS_SECURE_CHROME_UI)かを判定する。
- 触るとき: about: ページで項目を出し分ける条件を変えるとき。
- 呼び出し先: `currentURI?.schemeIs()`
- 条件付き依存: `if (currentURI?.schemeIs("about"))` → `lazy.E10SUtils.getAboutModule()`
- 条件付き依存: `if (module)` → `module.getURIFlags()`
- 参照: `Ci.nsIAboutModule.IS_SECURE_CHROME_UI`, `this.browser`
- XPCOM: [`nsIAboutModule`](../../../netwerk/protocol/about/nsIAboutModule.idl.md)

## nsContextMenu.linkText()
- 位置: L2539-2541
- 役割: 互換のために残した関数で、linkTextStr をそのまま返す。
- 触るとき: アドオンが linkText を呼んでいるか確認するとき。
- 参照: `this.linkTextStr`

## nsContextMenu.shouldShowSeparator()
- 位置: L2546-2558
- 役割: 指定の区切り線から前の区切り線までの間に、表示中の項目があるかを調べる。
- 触るとき: 区切り線を出すかどうかの判定を変えるとき。
- 呼び出し先: `this.document.getElementById()`
- 参照: `separator.previousSibling`, `sibling.hidden`, `sibling.localName`, `sibling.previousSibling`

## nsContextMenu.shouldShowAddEngine()
- 位置: L2560-2570
- 役割: http/https のテキスト入力欄の検索欄で、ログイン欄ではなく、ポリシーで検索エンジンの追加が許されているときに true を返す。
- 触るとき: 検索エンジンの追加項目の条件を変えるとき。
- 呼び出し先: `Services.policies.isAllowed()`, `this.isLoginForm()`, `uri.schemeIs()`
- 参照: `this.browser.currentURI`, `this.onSearchField`, `this.onTextInput`
- XPCOM: `Services.policies`

## nsContextMenu.addDictionaries()
- 位置: L2572-2595
- 役割: 辞書のダウンロード URL にロケールとバージョンを入れて、設定に応じたタブかウィンドウで開く。
- 触るとき: 辞書の入手先の URL や開き方を変えるとき。
- 呼び出し先: `Services.prefs.getIntPref()`, `Services.urlFormatter.formatURLPref()`, `escape()`, `this.window.openTrustedLinkIn()`, `uri.replace()`, `uri.replace(/%LOCALE%/, escape(locale)).replace()`
- 参照: `Services.appinfo.version`, `Services.locale.acceptLanguages`
- XPCOM: `Services.appinfo` / `Services.locale` / `Services.prefs` / `Services.urlFormatter`

## nsContextMenu.bookmarkThisPage()
- 位置: L2597-2599
- 役割: 最上位のウィンドウの PlacesCommandHook でページをブックマークする。失敗はコンソールに出す。
- 触るとき: ページのブックマーク処理の経路を変えるとき。
- 呼び出し先: `this.window.top.PlacesCommandHook.bookmarkPage()`, `this.window.top.PlacesCommandHook.bookmarkPage().catch()`
- 参照: `console.error`

## nsContextMenu.bookmarkLink()
- 位置: L2601-2606
- 役割: リンク URL とリンク文字列を使って、PlacesCommandHook でリンクをブックマークする。
- 触るとき: リンクのブックマーク時の名前や URL を変えるとき。
- 呼び出し先: `this.window.top.PlacesCommandHook.bookmarkLink()`, `this.window.top.PlacesCommandHook.bookmarkLink( this.linkURL, this.linkTextStr ).catch()`
- 参照: `console.error`, `this.linkTextStr`, `this.linkURL`

## nsContextMenu.addBookmarkForFrame()
- 位置: L2608-2616
- 役割: 子プロセスからフレームのタイトルを取り、フレームの URL をそのタイトルでブックマークする。
- 触るとき: フレームのブックマークの名前の決め方を変えるとき。
- 呼び出し先: `this.actor.getFrameTitle()`, `this.actor.getFrameTitle(this.targetIdentifier).then()`, `this.window.top.PlacesCommandHook.bookmarkLink()`, `this.window.top.PlacesCommandHook.bookmarkLink(uri.spec, title).catch()`
- 参照: `console.error`, `this.contentData.documentURIObject`, `this.targetIdentifier`, `uri.spec`

## nsContextMenu.savePageAs()
- 位置: L2618-2620
- 役割: 現在のブラウザのページを saveBrowser で保存する。
- 触るとき: ページ保存の経路を変えるとき。
- 呼び出し先: `this.window.saveBrowser()`
- 参照: `this.browser`

## nsContextMenu.printFrame()
- 位置: L2622-2626
- 役割: クリックしたフレームだけを印刷対象にして、印刷ウィンドウを開く。
- 触るとき: フレーム印刷の範囲を変えるとき。
- 呼び出し先: `this.window.PrintUtils.startPrintWindow()`
- 参照: `this.actor.browsingContext`

## nsContextMenu.printSelection()
- 位置: L2628-2632
- 役割: 選択範囲だけを印刷対象にして、印刷ウィンドウを開く。
- 触るとき: 選択範囲の印刷の範囲を変えるとき。
- 呼び出し先: `this.window.PrintUtils.startPrintWindow()`
- 参照: `this.actor.browsingContext`

## nsContextMenu.switchPageDirection()
- 位置: L2634-2641
- 役割: 選択中のブラウザに、SwitchDocumentDirection のメッセージを全体に送り、ページの書字方向を切り替える。
- 触るとき: ページの書字方向の切り替え経路を変えるとき。
- 呼び出し先: `this.window.gBrowser.selectedBrowser.sendMessageToActor()`

## nsContextMenu.mediaCommand()
- 位置: L2643-2645
- 役割: 対象のメディアに対するコマンド(再生、ミュートなど)をアクター経由で送る。
- 触るとき: メディアコマンドを増やすとき、またはメディア操作が効かない原因を調べるとき。
- 呼び出し先: `this.actor.mediaCommand()`
- 参照: `this.targetIdentifier`

## nsContextMenu.copyMediaLocation()
- 位置: L2647-2652
- 役割: 元のメディア URL(originalMediaURL)をクリップボードにコピーする。
- 触るとき: メディアの場所をコピーする値を変えるとき。
- 呼び出し先: `lazy.clipboard.copyString()`
- 参照: `this.actor.manager.browsingContext.currentWindowGlobal`, `this.originalMediaURL`

## nsContextMenu.getImageText()
- 位置: L2654-2669
- 役割: 画像から取り出した文字列を、タブのダイアログボックスで文字認識の結果として表示する。計測用のタイマーを開始して渡す。
- 触るとき: 画像文字認識の表示方法や計測を変えるとき。
- 呼び出し先: `Glean.textRecognition.apiPerformance.start()`, `dialog.resizeVertically()`, `dialogBox.open()`, `this.actor.getImageText()`, `this.window.gBrowser.getTabDialogBox()`
- 参照: `Services.prompt.MODAL_TYPE_CONTENT`, `this.browser`, `this.targetIdentifier`, `this.window.openLinkIn`
- XPCOM: `Services.prompt`

## nsContextMenu.drmLearnMore()
- 位置: L2671-2682
- 役割: DRM のサポートページを、クリック位置に応じた場所で開く。現在のタブでは開かない。
- 触るとき: DRM の説明リンクの開き先を変えるとき。
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `lazy.BrowserUtils.whereToOpenLink()`, `this.window.openTrustedLinkIn()`
- XPCOM: `Services.urlFormatter`

## nsContextMenu.createAITab()
- 位置: L2684-2686
- 役割: 現在のブラウザの URL を渡して AI タブを作る。
- 触るとき: AI タブの作成の入力を変えるとき。
- 呼び出し先: `lazy.AIWindow.createAITab()`
- 参照: `this.browser.currentURI.spec`, `this.window`

## nsContextMenu.openSelectTranslationsPanel()
- 位置: L2693-2705
- 役割: 文脈のスクリーン座標を、デバイスのピクセル比で割って、翻訳の選択パネルを開く。翻訳対象の文字列と言語ペアの Promise を渡す。
- 触るとき: 翻訳パネルの位置や渡す情報を変えるとき。
- 呼び出し先: `this.#getTextToTranslate()`, `this.window.SelectTranslationsPanel.open()`
- 参照: `console.error`, `context.screenXDevPx`, `context.screenYDevPx`, `this.#translationsLangPairPromise`, `this.contentData.context`, `this.isTextSelected`, `this.window.devicePixelRatio`

## nsContextMenu.localizeTranslateSelectionItem()
- 位置: async L2716-2766
- 役割: 言語ペアを待ち、翻訳先の言語が元の言語と同じなら汎用の文言にする。異なれば表示名を作って、言語付きの文言に差し替える。失敗時も汎用の文言にする。
- 触るとき: 翻訳項目の文言の決め方を変えるとき。
- 呼び出し先: `this.document.l10n.setAttributes()`, `translateSelectionItem.removeAttribute()`
- 条件付き依存: `if (targetLanguage)` → `lazy.TranslationsUtils.langTagsMatch()`
- 条件付き依存: `if ( lazy.TranslationsUtils.langTagsMatch(sourceLanguage, targetLanguage) )` → `translateSelectionItem.removeAttribute()`
- 条件付き依存: `if ( lazy.TranslationsUtils.langTagsMatch(sourceLanguage, targetLanguage) )` → `this.document.l10n.setAttributes()`
- 条件付き依存: `if (targetLanguage)` → `lazy.TranslationsParent.createLanguageDisplayNames()`
- 条件付き依存: `if (targetLanguage)` → `languageDisplayNames.of()`
- 条件付き依存: `if (displayName)` → `translateSelectionItem.setAttribute()`
- 条件付き依存: `if (displayName)` → `this.document.l10n.setAttributes()`
- 参照: `this.#translationsLangPairPromise`, `this.isTextSelected`

## nsContextMenu.#getTextToTranslate()
- 位置: L2773-2792
- 役割: 選択テキストがあればそれを返す。無ければリンク文字列を返すが、空または URL の場合は空文字を返す。
- 触るとき: 翻訳の対象にする文字列の優先順位を変えるとき。
- 呼び出し先: `URL.canParse()`, `this.linkTextStr.trim()`
- 条件付き依存: `if (this.isTextSelected)` → `this.selectionInfo.fullText.trim()`
- 参照: `this.isTextSelected`

## nsContextMenu.showTranslateSelectionItem()
- 位置: L2797-2824
- 役割: 翻訳機能、選択翻訳の設定、ハードウェアの対応、翻訳対象の文字列の有無をすべて満たすときだけ翻訳項目を出す。出すときは言語ペアの取得と文言の設定を始める。
- 触るとき: 翻訳項目の表示条件を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `lazy.TranslationsParent.getIsTranslationsEngineSupported()`, `this.#getTextToTranslate()`, `this.document.getElementById()`, `this.localizeTranslateSelectionItem()`, `this.window.SelectTranslationsPanel.getLangPairPromise()`
- 条件付き依存: `if (translateSelectionItem.hidden)` → `translateSelectionItem.removeAttribute()`
- 参照: `lazy.TranslationsParent.AIFeature.isEnabled`, `textToTranslate.length`, `this.#translationsLangPairPromise`, `translateSelectionItem.hidden`
- XPCOM: `Services.prefs`

## nsContextMenu.showAndFormatSearchContextItem()
- 位置: L2827-2915
- 役割: 「<エンジン>で検索」の2項目(通常とプライベート)の表示と文言を決める。選択文字列かリンク文字列を15文字で切り、既定の検索エンジン名を入れ、アクセスキーも設定する。両方隠れていれば文言の作成は省く。
- 触るとき: 検索項目の文言や、切り詰めの長さや条件を変えるとき。
- 呼び出し先: `document.getElementById()`, `frameSeparator.toggleAttribute()`, `this.#updateSearchMenuitem()`
- 条件付き依存: `if (selectedText.length > 15)` → `selectedText[15].charCodeAt()`
- 条件付き依存: `if (selectedText.length > 15)` → `selectedText.substr()`
- 条件付き依存: `if (!menuItem.hidden)` → `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- 条件付き依存: `if (!menuItem.hidden)` → `gNavigatorBundle.getFormattedString()`
- 条件付き依存: `if (!menuItem.hidden)` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (otherEngine)` → `gNavigatorBundle.getFormattedString()`
- 条件付き依存: `if (!(otherEngine))` → `gNavigatorBundle.getString()`
- 条件付き依存: `if (!menuItemPrivate.hidden)` → `gNavigatorBundle.getString()`
- 参照: `Services.locale.ellipsis`, `lazy.SearchService.defaultEngine.name`, `lazy.SearchService.defaultPrivateEngine.name`, `lazy.SearchUtils.URL_TYPE.SEARCH`, `menuItem.accessKey`, `menuItem.hidden`, `menuItem.label`, `menuItemPrivate.accessKey`, `menuItemPrivate.hidden`, `menuItemPrivate.label`, `selectedText.length`, `this.browser`, `this.inFrame`, `this.isTextSelected`, `this.linkTextStr`, `this.onImage`, `this.onLink`, `this.selectedText`, `this.window`
- XPCOM: `Services.locale`

## nsContextMenu.#updateSearchMenuitem()
- 位置: L2917-2975
- 役割: 検索系の1項目について、検索サービスの初期化、プライベート項目の条件、エンジンが対応する応答型、コンテンツ型による絞り込みを判定して表示を決める。表示するときはエンジンと検索語と principal を項目に入れる。
- 触るとき: 検索項目が出ない条件や、どのエンジンで検索するかを変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `engine?.supportsResponseType()`, `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- 条件付き依存: `if (!menuitem.hidden)` → `engine.getURLOfType()`
- 条件付き依存: `if (!menuitem.hidden)` → `url.acceptedContentTypes.includes()`
- 参照: `lazy.PrivateBrowsingUtils.enabled`, `lazy.SearchService.defaultEngine`, `lazy.SearchService.defaultPrivateEngine`, `lazy.SearchService.hasSuccessfullyInitialized`, `menuitem.engine`, `menuitem.hidden`, `menuitem.policyContainer`, `menuitem.principal`, `menuitem.searchTerms`, `menuitem.usePrivate`, `this.browser`, `this.contentData.contentType`, `this.contentData?.contentType`, `this.inAboutDevtoolsToolbox`, `this.policyContainer`, `this.principal`, `url?.acceptedContentTypes`
- XPCOM: `Services.prefs`

## nsContextMenu.showAndFormatVisualSearchContextItem()
- 位置: L2981-3028
- 役割: 画像のビジュアル検索項目を、画像の元の URL が使えて、データ URI や添付ではないときに判定する。Nimbus の露出イベントを記録し、機能フラグが無効なら隠す。有効なら文言、新機能バッジ、検索の表示の記録を行う。
- 触るとき: ビジュアル検索の表示条件、実験の露出の記録、または機能フラグの扱いを変えるとき。
- 呼び出し先: `this.#updateSearchMenuitem()`, `this.contentData.contentDisposition?.startsWith()`, `this.imageInfo.currentSrc.startsWith()`, `this.window.document.getElementById()`
- 条件付き依存: `if (!menuitem.hidden)` → `lazy.NimbusFeatures.search.recordExposureEvent()`
- 条件付き依存: `if (!menuitem.hidden)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!menuitem.hidden)` → `menuitem.engine.getURLOfType()`
- 条件付き依存: `if (!menuitem.hidden)` → `this.window.document.l10n.setAttributes()`
- 条件付き依存: `if (!menuitem.hidden)` → `this.#setNewFeatureBadge()`
- 条件付き依存: `if (!menuitem.hidden)` → `visualSearchUrl.isNew()`
- 条件付き依存: `if (!menuitem.hidden)` → `lazy.BrowserSearchTelemetry.recordSapImpression()`
- 参照: `lazy.SearchUtils.URL_TYPE.VISUAL_SEARCH`, `menuitem.engine`, `menuitem.engine.name`, `menuitem.hidden`, `this.browser`, `this.imageInfo?.currentSrc`, `this.onImage`, `visualSearchUrl.displayName`
- XPCOM: `Services.prefs`

## nsContextMenu.loadSearch()
- 位置: L3043-3056
- 役割: 項目の target に載せられたエンジン、検索語、principal などを使い、SearchUIUtils で検索結果を開く。
- 触るとき: 検索項目を押したときの検索の開き方を変えるとき。
- 呼び出し先: `lazy.SearchUIUtils.loadSearchFromContext()`
- 参照: `event.target`, `this.window`

## nsContextMenu.createContainerMenu()
- 位置: L3058-3065
- 役割: コンテナ(ユーザーコンテキスト)の選択メニューを作る。現在のユーザーコンテキストは除いて表示する。
- 触るとき: コンテナの選択肢の中身や、除外する条件を変えるとき。
- 呼び出し先: `this.window.createUserContextMenu()`
- 参照: `this.contentData.userContextId`

## nsContextMenu.#setNewFeatureBadge()
- 位置: async L3080-3100
- 役割: 項目に新機能バッジを付けるか外す。文言が未取得なら取得してから付け、取得後に再び自分を呼んで付ける。
- 触るとき: 新機能バッジの付け方や文言の取得方法を変えるとき。
- 呼び出し先: `menuitem.classList.toggle()`, `this.window.document.l10n.formatValue()`
- 条件付き依存: `if (!shouldShow)` → `menuitem.removeAttribute()`
- 条件付き依存: `if (this.#newFeatureBadgeL10nString)` → `menuitem.setAttribute()`
- 条件付き依存: `if (value)` → `this.#setNewFeatureBadge()`
- 参照: `this.#newFeatureBadgeL10nString`
