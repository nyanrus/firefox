# browser/actors/AboutReaderChild.sys.mjs

source: browser/actors/AboutReaderChild.sys.mjs
source-hash: 3d70b963f360f308b8dd82884be5e59b5f4d6d6b
lines: 252

## <module>
- 役割: リーダーモードのコンテンツ側アクター。記事の解析要求、リーダー表示への切り替え、ページの読み取り可否判定とツールバーボタンの更新を担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## AboutReaderChild.constructor()
- 位置: L17-23
- 役割: リーダー用の状態（_reader・_articlePromise・離脱フラグ）を初期化する。
- 触るとき: リーダーモードの内部状態の初期値を変えるときに見る。
- 呼び出し先: `super()`
- 参照: `this._articlePromise`, `this._isLeavingReaderableReaderMode`, `this._reader`

## AboutReaderChild.didDestroy()
- 位置: L25-28
- 役割: アクター破棄時に保留中の可読性チェックを取り消し、リーダーの参照を解放する。
- 触るとき: タブを閉じた後やページ遷移後に、リーダーのリスナーや参照が残る問題を調べるときに見る。
- 呼び出し先: `this.cancelPotentialPendingReadabilityCheck()`, `this.readerModeHidden()`

## AboutReaderChild.readerModeHidden()
- 位置: L30-35
- 役割: AboutReader があればその actor を外し、保持していた参照を null にする。
- 触るとき: リーダー表示を解除する経路で参照が残る問題を調べるときに見る。
- 条件付き依存: `if (this._reader)` → `this._reader.clearActor()`
- 参照: `this._reader`

## AboutReaderChild.receiveMessage()
- 位置: async L37-76
- 役割: Toggle・PushState・Enter/Leave の親からのメッセージを処理し、記事を解析して親へ渡し、生成済みリーダーへも転送する。
- 触るとき: リーダーモードへの入退場や記事データの受け渡しを変えるときに見る。
- 呼び出し先: `lazy.ReaderMode.enterReaderMode()`, `lazy.ReaderMode.leaveReaderMode()`, `this.updateReaderButton()`
- 条件付き依存: `if (!this.isAboutReader)` → `gUrlsToDocContentType.set()`
- 条件付き依存: `if (!this.isAboutReader)` → `gUrlsToDocTitle.set()`
- 条件付き依存: `if (!this.isAboutReader)` → `lazy.ReaderMode.parseDocument( this.document ).catch()`
- 条件付き依存: `if (!this.isAboutReader)` → `lazy.ReaderMode.parseDocument()`
- 条件付き依存: `if (!this.isAboutReader)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (!(!this.isAboutReader))` → `this.closeReaderMode()`
- 条件付き依存: `if (this._reader)` → `this._reader.receiveMessage()`
- 参照: `console.error`, `message.data`, `message.data.isArticle`, `message.name`, `this._articlePromise`, `this._reader`, `this.contentWindow`, `this.docShell`, `this.document`, `this.document.URL`, `this.document.contentType`, `this.document.title`, `this.isAboutReader`

## AboutReaderChild.isAboutReader()
- 位置: L78-83
- 役割: 現在のドキュメントの URI が about:reader で始まるかを返す。
- 触るとき: リーダー画面かどうかの判定条件を変えるときに見る。
- 呼び出し先: `this.document.documentURI.startsWith()`
- 参照: `this.document`

## AboutReaderChild.isReaderableAboutReader()
- 位置: L85-87
- 役割: リーダー画面で、かつエラー表示でないかを返す。
- 触るとき: リーダー画面から元ページへ戻る際のアイコン表示を調べるときに見る。
- 参照: `this.document.documentElement.dataset.isError`, `this.isAboutReader`

## AboutReaderChild.handleEvent()
- 位置: L89-146
- 役割: DOMContentLoaded・pagehide・pageshow を処理し、記事の読み込みやボタン状態の更新、bfcache 復帰時の可読性チェックを行う。
- 触るとき: ページ読み込み時やキャッシュ復帰時にリーダーボタンやリーダー画面の初期化が崩れるときに見る。
- 呼び出し先: `this.canDoReadabilityCheck()`, `this.cancelPotentialPendingReadabilityCheck()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (!this.isAboutReader)` → `this.updateReaderButton()`
- 条件付き依存: `if (!this._articlePromise)` → `decodeURIComponent()`
- 条件付き依存: `if (!this._articlePromise)` → `url.substr()`
- 条件付き依存: `if (!this._articlePromise)` → `this.sendQuery()`
- 条件付き依存: `if (this.document.body)` → `this.sendAsyncMessage()`
- 条件付き依存: `if (this.document.body)` → `gUrlsToDocContentType.get()`
- 条件付き依存: `if (this.document.body)` → `gUrlsToDocTitle.get()`
- 条件付き依存: `if (aEvent.persisted && this.canDoReadabilityCheck())` → `this.performReadabilityCheckNow()`
- 参照: `"about:reader?url=".length`, `aEvent.originalTarget.defaultView`, `aEvent.persisted`, `aEvent.type`, `lazy.AboutReader`, `this._articlePromise`, `this._isLeavingReaderableReaderMode`, `this._reader`, `this.contentWindow`, `this.document.body`, `this.document.documentURI`, `this.isAboutReader`

## AboutReaderChild.updateReaderButton()
- 位置: L154-160
- 役割: 可読性チェックが可能なら、次の再描画後に判定を予約する。
- 触るとき: リーダーボタンの表示が遅れたり出なかったりするときに見る。
- 呼び出し先: `this.canDoReadabilityCheck()`, `this.scheduleReadabilityCheckPostPaint()`

## AboutReaderChild.canDoReadabilityCheck()
- 位置: L162-171
- 役割: 読み込み時解析が有効で、HTML の通常ドキュメントかつ about:reader でないときに真を返す。
- 触るとき: どのページで可読性チェックを行うかの条件を変えるときに見る。
- 呼び出し先: `this.contentWindow.HTMLDocument.isInstance()`
- 参照: `lazy.Readerable.isEnabledForParseOnLoad`, `this.contentWindow`, `this.contentWindow.windowRoot`, `this.document`, `this.document.mozSyntheticDocument`, `this.isAboutReader`

## AboutReaderChild.cancelPotentialPendingReadabilityCheck()
- 位置: L173-184
- 役割: 予約済みの MozAfterPaint リスナーを外し、関連する参照を消す。
- 触るとき: 再描画待ちのリスナーが残って余分な更新が走るときに見る。
- 条件付き依存: `if (this._listenerWindow)` → `this._listenerWindow.removeEventListener()`
- 参照: `this._listenerWindow`, `this._pendingReadabilityCheck`

## AboutReaderChild.scheduleReadabilityCheckPostPaint()
- 位置: L186-202
- 役割: 既存の予約を取り消してから、ウィンドウの MozAfterPaint に可読性チェックを登録する。
- 触るとき: 再描画後の判定タイミングを変えるときに見る。
- 呼び出し先: `this.contentWindow.windowRoot.addEventListener()`, `this.onPaintWhenWaitedFor.bind()`
- 条件付き依存: `if (this._pendingReadabilityCheck)` → `this.cancelPotentialPendingReadabilityCheck()`
- 参照: `this._listenerWindow`, `this._pendingReadabilityCheck`, `this.contentWindow.windowRoot`

## AboutReaderChild.onPaintWhenWaitedFor()
- 位置: L204-215
- 役割: 描画矩形がある再描画イベントを受けたときだけ、可読性チェックを即時実行する。
- 触るとき: 描画前の空のイベントで判定が走る問題を調べるときに見る。
- 呼び出し先: `this.performReadabilityCheckNow()`
- 参照: `event.clientRects.length`

## AboutReaderChild.performReadabilityCheckNow()
- 位置: L217-243
- 役割: ドキュメントが記事として読めるかを判定し、結果を Reader:UpdateReaderButton として親へ送る。
- 触るとき: 記事判定の結果がボタンに反映されない、または誤判定されるときに見る。
- 呼び出し先: `lazy.Readerable.isProbablyReaderable()`, `lazy.Readerable.shouldCheckUri()`, `this.cancelPotentialPendingReadabilityCheck()`
- 条件付き依存: `if ( lazy.Readerable.shouldCheckUri(document.baseURIObject, true) && lazy.Readerable.isProbablyReaderable(document) )` → `this.sendAsyncMessage()`
- 条件付き依存: `if (forceNonArticle)` → `this.sendAsyncMessage()`
- 参照: `document.baseURIObject`, `this.document`

## AboutReaderChild.closeReaderMode()
- 位置: L245-250
- 役割: リーダー画面を閉じる要求を親へ送り、戻り先で記事アイコンを残すかの状態を保存する。
- 触るとき: リーダー画面から元ページへ戻る動作を変えるときに見る。
- 条件付き依存: `if (this.isAboutReader)` → `this.sendAsyncMessage()`
- 参照: `this._isLeavingReaderableReaderMode`, `this.isAboutReader`, `this.isReaderableAboutReader`
