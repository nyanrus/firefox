# browser/actors/ContextMenuParent.sys.mjs

source: browser/actors/ContextMenuParent.sys.mjs
source-hash: 9e0ef4f14fdf455c3a8693dbfc3741faecb6fc08
lines: 259

## <module>
- 役割: コンテキストメニューの親側アクター。子から届いた右クリック情報でメニューを開き、子へのメディア・画像・テキストフラグメントなどの操作要求を送る。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetters()`

## ContextMenuParent.receiveMessage()
- 位置: L27-47
- 役割: 子からの contextmenu データを受け、表示先ウィンドウを決めて Relay の可否を反映し、メニューを開く。
- 触るとき: 右クリックメニューが開かない、または別ウィンドウに出る問題を調べるときに見る。
- 呼び出し先: `browser.hasAttribute()`, `this.#openContextMenu()`
- 参照: `browser.documentGlobal`, `browser.documentGlobal.docShell.chromeEventHandler`, `lazy.FirefoxRelay.isEnabled`, `message.data`, `message.data.context.showRelay`, `this.manager.rootFrameLoader.ownerElement`, `topBrowser.documentGlobal`, `win.nsContextMenu`

## ContextMenuParent.hiding()
- 位置: L49-56
- 役割: メニューが閉じたことを子へ ContextMenu:Hiding で伝える（子が既に無い場合は無視）。
- 触るとき: メニューを閉じた後に子の状態が残る問題を調べるときに見る。
- 呼び出し先: `this.sendAsyncMessage()`

## ContextMenuParent.reloadFrame()
- 位置: L58-63
- 役割: 対象フレームの再読み込みを子へ依頼する。
- 触るとき: フレームの再読み込みメニューの動作を変えるときに見る。
- 呼び出し先: `this.sendAsyncMessage()`

## ContextMenuParent.getImageText()
- 位置: L65-69
- 役割: 画像内の文字認識結果と文字方向を子に問い合わせて返す。
- 触るとき: 画像のテキスト抽出メニューの結果が出ない問題を調べるときに見る。
- 呼び出し先: `this.sendQuery()`

## ContextMenuParent.toggleRevealPassword()
- 位置: L71-75
- 役割: パスワード欄の表示・非表示を子へ切り替えさせる。
- 触るとき: パスワードの表示切り替えの動作を調べるときに見る。
- 呼び出し先: `this.sendAsyncMessage()`

## ContextMenuParent.useRelayMask()
- 位置: async L77-91
- 役割: Firefox Relay で作ったメールマスクを生成し、子の入力欄へ書き込むよう依頼する。
- 触るとき: Relay のマスク生成と入力の反映を変えるときに見る。
- 呼び出し先: `lazy.FirefoxRelay.generateUsername()`
- 条件付き依存: `if (emailMask)` → `this.sendAsyncMessage()`
- 参照: `this.manager.browsingContext.currentWindowGlobal`, `windowGlobal.rootFrameLoader.ownerElement`

## ContextMenuParent.reloadImage()
- 位置: L93-95
- 役割: 対象の画像を子で再読み込みさせる。
- 触るとき: 画像の再読み込みメニューの動作を変えるときに見る。
- 呼び出し先: `this.sendAsyncMessage()`

## ContextMenuParent.getFrameTitle()
- 位置: L97-99
- 役割: 対象フレームのドキュメントタイトルを子に問い合わせて返す。
- 触るとき: フレームのタイトル表示や利用箇所を調べるときに見る。
- 呼び出し先: `this.sendQuery()`

## ContextMenuParent.mediaCommand()
- 位置: L101-112
- 役割: 再生・一時停止・ループ・ミュート・PiP などのメディア操作を、ユーザー入力の有無と共に子へ送る。
- 触るとき: 動画や音声のメニュー操作が効かない問題を調べるときに見る。
- 呼び出し先: `this.sendAsyncMessage()`
- 参照: `browser.documentGlobal`, `this.manager.browsingContext.currentWindowGlobal`, `win.windowUtils`, `windowGlobal.rootFrameLoader.ownerElement`, `windowUtils.isHandlingUserInput`

## ContextMenuParent.canvasToBlobURL()
- 位置: L114-116
- 役割: キャンバスの内容を子で Blob URL にして返す。
- 触るとき: キャンバス画像の保存や表示用 URL の生成を調べるときに見る。
- 呼び出し先: `this.sendQuery()`

## ContextMenuParent.canvasToBlob()
- 位置: L118-120
- 役割: キャンバスの内容を子で Blob にして返す。
- 触るとき: キャンバスの Blob 取得が失敗する問題を調べるときに見る。
- 呼び出し先: `this.sendQuery()`

## ContextMenuParent.saveVideoFrameAsImage()
- 位置: L122-126
- 役割: 動画の現在フレームを子で JPEG の data URL にして返す。
- 触るとき: 動画フレームの画像保存の形式を変えるときに見る。
- 呼び出し先: `this.sendQuery()`

## ContextMenuParent.setAsDesktopBackground()
- 位置: L128-132
- 役割: 画像をデスクトップ背景に設定するため、子に画像データを要求して返す。
- 触るとき: デスクトップ背景設定の画像取得や失敗時の扱いを変えるときに見る。
- 呼び出し先: `this.sendQuery()`

## ContextMenuParent.getSearchFieldEngineData()
- 位置: L134-138
- 役割: 検索欄のフォームから、検索エンジン追加に必要な URL・フォームデータ・文字コードを子に問い合わせる。
- 触るとき: ページの検索欄から検索エンジンを追加する機能を変えるときに見る。
- 呼び出し先: `this.sendQuery()`

## ContextMenuParent.getTextDirective()
- 位置: L140-144
- 役割: テキストフラグメント機能が有効なら、選択範囲のリンク（text directive）を子に問い合わせる。
- 触るとき: テキストフラグメントのリンクをコピーする機能を調べるときに見る。
- 呼び出し先: `this.sendQuery()`
- 参照: `lazy.TEXT_FRAGMENTS_ENABLED`

## ContextMenuParent.removeAllTextFragments()
- 位置: L146-148
- 役割: ページ上の全テキストフラグメントの強調を子で削除させる。
- 触るとき: テキストフラグメントの一括解除が効かない問題を調べるときに見る。
- 呼び出し先: `this.sendQuery()`

## ContextMenuParent.#openContextMenu()
- 位置: L160-257
- 役割: キオスクや未読み込み文書を除き、子から来た文脈と参照元情報をまとめ、contentAreaContextMenu を画面上の座標で開く。
- 触るとき: 右クリック時のメニュー内容や表示位置、参照元の受け渡しを変えるときに見る。
- 呼び出し先: `lazy.E10SUtils.deserializeReferrerInfo()`, `lazy.WebNavigationFrames.getFrameId()`, `popup.openPopupAtScreen()`, `win.document.getElementById()`
- 条件付き依存: `if (frameReferrerInfo)` → `lazy.E10SUtils.deserializeReferrerInfo()`
- 条件付き依存: `if (linkReferrerInfo)` → `lazy.E10SUtils.deserializeReferrerInfo()`
- 参照: `MouseEvent.MOZ_SOURCE_CURSOR`, `MouseEvent.MOZ_SOURCE_ERASER`, `MouseEvent.MOZ_SOURCE_KEYBOARD`, `MouseEvent.MOZ_SOURCE_MOUSE`, `MouseEvent.MOZ_SOURCE_PEN`, `MouseEvent.MOZ_SOURCE_TOUCH`, `context.frameBrowsingContextID`, `context.frameID`, `context.frameOuterWindowID`, `context.inputSource`, `context.principal`, `context.screenXDevPx`, `context.screenYDevPx`, `context.storagePrincipal`, `data.charSet`, `data.contentDisposition`, `data.contentType`, `data.context`, `data.disableSetDesktopBackground`, `data.editFlags`, `data.frameReferrerInfo`, `data.linkReferrerInfo`, `data.loginFillInfo`, `data.referrerInfo`, `data.selectionInfo`, `data.showRelay`, `data.spellInfo`, `data.webExtContextData`, `documentURIObject.spec`, `lazy.BrowserHandler.kiosk`, `newEvent.screenX`, `newEvent.screenY`, `this.manager`, `wgp.browsingContext`, `wgp.browsingContext.currentURI`, `wgp.browsingContext.id`, `wgp.browsingContext.originAttributes.userContextId`, `wgp.cookieJarSettings`, `wgp.documentPrincipal`, `wgp.documentStoragePrincipal`, `wgp.isCurrentGlobal`, `wgp.outerWindowId`, `win.devicePixelRatio`, `win.nsContextMenu.contentData`, `win.nsContextMenu.contentData.context`
