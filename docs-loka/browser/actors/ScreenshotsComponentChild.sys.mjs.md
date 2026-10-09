# browser/actors/ScreenshotsComponentChild.sys.mjs

source: browser/actors/ScreenshotsComponentChild.sys.mjs
source-hash: 26416f14fc98d5bf560b7b26980d7ccc11724558
lines: 443

## <module>
- 役割: スクリーンショットの範囲選択オーバーレイをページ内で表示・操作し、選択結果や撮影範囲を親プロセスとやり取りする子側アクター。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ScreenshotsComponentChild.overlay()
- 位置: L56-58
- 役割: 表示中のオーバーレイのオブジェクトを返す。
- 触るとき: オーバーレイの参照方法を変えるとき。
- 参照: `this.#overlay`

## ScreenshotsComponentChild.receiveMessage()
- 位置: L60-87
- 役割: 表示・非表示、範囲の取得、フォーカス、監視の追加と削除などの親からの要求を、対応する処理へ振り分ける。
- 触るとき: 親から受ける要求を増やすとき。
- 呼び出し先: `Services.focus.clearFocus()`, `this.addEventListeners()`, `this.endScreenshotsOverlay()`, `this.focusOverlay()`, `this.getDocumentTitle()`, `this.getFullPageBounds()`, `this.getMethodsUsed()`, `this.getVisibleBounds()`, `this.removeEventListeners()`, `this.startScreenshotsOverlay()`
- 参照: `message.data`, `message.data?.mode`, `message.name`, `this.contentWindow`, `this.overlay?.initialized`
- XPCOM: `Services.focus`

## ScreenshotsComponentChild.handleEvent()
- 位置: L89-176
- 役割: 信頼されたイベントだけを扱う。オーバーレイ中は操作をページへ届かせず、オーバーレイに渡す。ページ移動、サイズ変更、スクロール、各種の操作要求も処理する。
- 触るとき: オーバーレイ中の操作の扱いを変えるとき。
- 呼び出し先: `Glean.screenshots[eventName].record()`, `this.#resizeTask.arm()`, `this.#scrollTask.arm()`, `this.endScreenshotsOverlay()`, `this.requestCancelScreenshot()`, `this.requestCopyScreenshot()`, `this.requestDownloadScreenshot()`, `this.sendAsyncMessage()`, `this.sendOverlaySelection()`
- 条件付き依存: `if ( [ ...ScreenshotsComponentChild.OVERLAY_EVENTS, ...ScreenshotsComponentChild.PREVENTABLE_EVENTS, "selectionchange", ].includes(event.type) )` → `["contextmenu", "pointerdown"].includes()`
- 条件付き依存: `if (!["contextmenu", "pointerdown"].includes(event.type))` → `event.preventDefault()`
- 条件付き依存: `if ( [ ...ScreenshotsComponentChild.OVERLAY_EVENTS, ...ScreenshotsComponentChild.PREVENTABLE_EVENTS, "selectionchange", ].includes(event.type) )` → `event.stopImmediatePropagation()`
- 条件付き依存: `if ( [ ...ScreenshotsComponentChild.OVERLAY_EVENTS, ...ScreenshotsComponentChild.PREVENTABLE_EVENTS, "selectionchange", ].includes(event.type) )` → `this.overlay.handleEvent()`
- 条件付き依存: `if (!this.#resizeTask && this.overlay?.initialized)` → `this.overlay.updateScreenshotsOverlayDimensions()`
- 条件付き依存: `if (!this.#scrollTask && this.overlay?.initialized)` → `this.overlay.updateScreenshotsOverlayDimensions()`
- 参照: `Glean.screenshots`, `ScreenshotsComponentChild.OVERLAY_EVENTS`, `ScreenshotsComponentChild.PREVENTABLE_EVENTS`, `event.detail`, `event.detail.reason`, `event.detail.region`, `event.detail.viewportHeight`, `event.detail.viewportWidth`, `event.isTrusted`, `event.type`, `lazy.DeferredTask`, `this.#resizeTask`, `this.#scrollTask`, `this.overlay?.initialized`

## ScreenshotsComponentChild.requestCancelScreenshot()
- 位置: L181-187
- 役割: 親に取り消しを通知し、オーバーレイを終了する。
- 触るとき: 取り消し時の処理を変えるとき。
- 呼び出し先: `this.endScreenshotsOverlay()`, `this.sendAsyncMessage()`

## ScreenshotsComponentChild.requestCopyScreenshot()
- 位置: L194-198
- 役割: 選択範囲に device pixel ratio を加えて親にコピーを依頼し、メソッドの記録を残したままオーバーレイを閉じる。
- 触るとき: コピー機能の要求内容を変えるとき。
- 呼び出し先: `this.endScreenshotsOverlay()`, `this.sendAsyncMessage()`
- 参照: `region.devicePixelRatio`, `this.contentWindow.devicePixelRatio`

## ScreenshotsComponentChild.requestDownloadScreenshot()
- 位置: L205-212
- 役割: 選択範囲とページタイトルを添えて親にダウンロードを依頼し、メソッドの記録を残したままオーバーレイを閉じる。
- 触るとき: ダウンロードの要求内容を変えるとき。
- 呼び出し先: `this.endScreenshotsOverlay()`, `this.getDocumentTitle()`, `this.sendAsyncMessage()`
- 参照: `region.devicePixelRatio`, `this.contentWindow.devicePixelRatio`

## ScreenshotsComponentChild.getDocumentTitle()
- 位置: L214-216
- 役割: 文書のタイトルを返す。
- 触るとき: 保存名に使うタイトルの取り方を変えるとき。
- 参照: `this.document.title`

## ScreenshotsComponentChild.sendOverlaySelection()
- 位置: L218-220
- 役割: オーバーレイの選択状態を親へ送る。
- 触るとき: 選択状態の通知内容を変えるとき。
- 呼び出し先: `this.sendAsyncMessage()`

## ScreenshotsComponentChild.getMethodsUsed()
- 位置: L222-226
- 役割: オーバーレイで使われた操作方法を返し、その記録を初期化する。
- 触るとき: 操作方法の計測を変えるとき。
- 呼び出し先: `this.#overlay.resetMethodsUsed()`
- 参照: `this.#overlay.methodsUsed`

## ScreenshotsComponentChild.focusOverlay()
- 位置: L228-231
- 役割: コンテンツにフォーカスを移し、指定された方向でオーバーレイ側のフォーカスを動かす。
- 触るとき: キーボードでのフォーカス移動を変えるとき。
- 呼び出し先: `this.#overlay.focus()`, `this.contentWindow.focus()`

## ScreenshotsComponentChild.documentIsReady()
- 位置: L239-267
- 役割: 文書が使える状態になったら解決する。準備前にページが閉じられたら拒否する。
- 触るとき: オーバーレイを出すタイミングを変えるとき。
- 呼び出し先: `document.addEventListener()`, `readyEnough()`, `this.contentWindow.addEventListener()`
- 条件付き依存: `if (readyEnough())` → `Promise.resolve()`
- 参照: `this.document`

## readyEnough()
- 位置: L243-247
- 役割: 文書の readyState が uninitialized でなく documentElement があるかを返す。
- 触るとき: 準備完了の判定条件を変えるとき。
- 参照: `document.documentElement`, `document.readyState`

## onChange()
- 位置: L253-263
- 役割: readystatechange を待ち、準備完了なら解決し、pagehide なら拒否する。 ソースの疑い: 通常の function 内で this.contentWindow を使っており、this が未定義になる可能性がある (要確認)。
- 触るとき: ページが読み込み中に閉じられた時の挙動を調べるとき。
- 条件付き依存: `if (event.type === "pagehide")` → `document.removeEventListener()`
- 条件付き依存: `if (event.type === "pagehide")` → `this.contentWindow.removeEventListener()`
- 条件付き依存: `if (event.type === "pagehide")` → `reject()`
- 条件付き依存: `if (!(event.type === "pagehide"))` → `readyEnough()`
- 条件付き依存: `if (readyEnough())` → `document.removeEventListener()`
- 条件付き依存: `if (readyEnough())` → `this.contentWindow.removeEventListener()`
- 条件付き依存: `if (readyEnough())` → `resolve()`
- 参照: `event.type`

## ScreenshotsComponentChild.addEventListeners()
- 位置: L269-274
- 役割: 窓の beforeunload、resize、scroll を登録し、オーバーレイ用の監視も追加する。
- 触るとき: オーバーレイの監視対象を変えるとき。
- 呼び出し先: `this.addOverlayEventListeners()`, `this.contentWindow.addEventListener()`

## ScreenshotsComponentChild.addOverlayEventListeners()
- 位置: L276-291
- 役割: 操作イベントを捕捉フェーズで登録し、設定が有効なら抑止対象の入力イベントも登録する。
- 触るとき: 抑止する入力イベントの範囲を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `chromeEventHandler.addEventListener()`, `this.document.addEventListener()`
- 条件付き依存: `if (Services.prefs.getBoolPref(SCREENSHOTS_PREVENT_CONTENT_EVENTS_PREF))` → `chromeEventHandler.addEventListener()`
- 参照: `ScreenshotsComponentChild.OVERLAY_EVENTS`, `ScreenshotsComponentChild.PREVENTABLE_EVENTS`, `this.#preventableEventsAdded`, `this.docShell.chromeEventHandler`
- XPCOM: `Services.prefs`

## ScreenshotsComponentChild.startScreenshotsOverlay()
- 位置: async L300-316
- 役割: 文書の準備を待ち、オーバーレイを作る(既にあれば再利用する)。イベントを登録し、指定モードで初期化する。準備に失敗したら false を返す。
- 触るとき: オーバーレイの開始条件や初期化を変えるとき。
- 呼び出し先: `console.warn()`, `overlay.initialize()`, `this.addEventListeners()`, `this.documentIsReady()`
- 参照: `SELECTION_MODES.SCREENSHOTS`, `ex.message`, `lazy.ScreenshotsOverlay`, `this.#overlay`, `this.document`, `this.overlay`

## ScreenshotsComponentChild.removeEventListeners()
- 位置: L318-323
- 役割: 窓に登録した beforeunload、resize、scroll の監視を外す。
- 触るとき: 後始末の範囲を変えるとき。
- 呼び出し先: `this.contentWindow.removeEventListener()`, `this.removeOverlayEventListeners()`

## ScreenshotsComponentChild.removeOverlayEventListeners()
- 位置: L325-340
- 役割: オーバーレイ用に登録したイベントを外す。抑止用のイベントは追加された時だけ外す。
- 触るとき: イベントの登録解除の漏れを調べるとき。
- 呼び出し先: `chromeEventHandler.removeEventListener()`, `this.document.removeEventListener()`
- 条件付き依存: `if (this.#preventableEventsAdded)` → `chromeEventHandler.removeEventListener()`
- 参照: `ScreenshotsComponentChild.OVERLAY_EVENTS`, `ScreenshotsComponentChild.PREVENTABLE_EVENTS`, `this.#preventableEventsAdded`, `this.docShell.chromeEventHandler`

## ScreenshotsComponentChild.endScreenshotsOverlay()
- 位置: L345-351
- 役割: 監視を外し、オーバーレイを片付け、リサイズとスクロールの遅延処理を止める。
- 触るとき: オーバーレイの終了処理を変えるとき。
- 呼び出し先: `this.#resizeTask?.disarm()`, `this.#scrollTask?.disarm()`, `this.overlay?.tearDown()`, `this.removeEventListeners()`

## ScreenshotsComponentChild.didDestroy()
- 位置: L353-356
- 役割: リサイズとスクロールの遅延処理を止める。
- 触るとき: アクター破棄時の後始末を変えるとき。
- 呼び出し先: `this.#resizeTask?.disarm()`, `this.#scrollTask?.disarm()`

## ScreenshotsComponentChild.getFullPageBounds()
- 位置: L380-398
- 役割: 全ページ撮影用に、スクロール可能な範囲の位置と大きさ、device pixel ratio を返す。
- 触るとき: 全ページ撮影の範囲計算を変えるとき。
- 参照: `this.#overlay.windowDimensions.dimensions`

## ScreenshotsComponentChild.getVisibleBounds()
- 位置: L423-441
- 役割: 表示中の範囲の位置と大きさ、device pixel ratio を返す。
- 触るとき: 表示範囲の撮影の計算を変えるとき。
- 参照: `this.#overlay.windowDimensions.dimensions`
