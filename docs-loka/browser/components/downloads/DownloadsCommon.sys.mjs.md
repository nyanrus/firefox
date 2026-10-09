# browser/components/downloads/DownloadsCommon.sys.mjs

source: browser/components/downloads/DownloadsCommon.sys.mjs
source-hash: 24bcd55f748277b583a9039d1d2ca227904756e5
lines: 1717

## <module>
- 役割: ダウンロードパネル、一覧、インジケーターで共有する状態判定・操作・データ購読を提供する。ダウンロードの一覧データと集計ビュー (インジケーター、要約) の基盤でもある。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.generateQI()`, `ChromeUtils.importESModule()`, `Object.setPrototypeOf()`, `PrefObserver.register()`, `Services.prefs.getBranch()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetters()`, `lazy.DownloadsLogger.error.bind()`, `lazy.DownloadsLogger.log.bind()`

## getPref()
- 位置: L107-115
- 役割: pref の値を、boolean なら getBoolPref で、それ以外は既定値 (キャッシュ) から読む。
- 触るとき: browser.download.* の pref を追加して読み出し方を変えるとき。
- 呼び出し先: `kPrefBranch.getBoolPref()`
- 参照: `this.prefs`

## observe()
- 位置: L116-121
- 役割: 監視対象の pref が変わったら、キャッシュされた値を読み直す。
- 触るとき: pref を切り替えても一覧のメニュー項目が即時に反映されないときに見る。
- 呼び出し先: `this.prefs.hasOwnProperty()`
- 条件付き依存: `if (this.prefs.hasOwnProperty(aData))` → `this.getPref()`

## register()
- 位置: L122-131
- 役割: 監視する pref の既定値を登録し、各 pref を遅延ゲッターとして定義して変更監視を張る。
- 触るとき: 新しい browser.download.* の pref を監視対象に加えるとき。
- 呼び出し先: `ChromeUtils.defineLazyGetter()`, `PrefObserver.getPref()`, `kPrefBranch.addObserver()`
- 参照: `this.prefs`

## strings()
- 位置: L178-194
- 役割: downloads.properties の文字列を読み込み、書式付きのものは関数として公開する。結果はキャッシュされる。
- 触るとき: ダウンロード関連の文言が反映されない、または文字列の名前を追加するときに見る。
- 呼び出し先: `Services.strings.createBundle()`, `sb.getSimpleEnumeration()`
- 参照: `string.key`, `string.value`, `this.strings`
- XPCOM: `Services.strings`

## strings[stringName]()
- 位置: L184-187
- 役割: 書式引数を持つ文字列を、引数を受けてフォーマットする関数にする。
- 触るとき: 引数付きの文字列 (サイズやステータス) の表示を変えるとき。
- 呼び出し先: `Array.from()`, `sb.formatStringFromName()`

## openInSystemViewerItemEnabled()
- 位置: L199-201
- 役割: 「システムビューアーで開く」のメニューを出すかの pref 値を返す。
- 触るとき: そのメニュー項目を表示する条件を変えるとき。
- 参照: `PrefObserver.openInSystemViewerContextMenuItem`

## alwaysOpenInSystemViewerItemEnabled()
- 位置: L206-208
- 役割: 「今後は常にシステムビューアーで開く」のメニューを出すかの pref 値を返す。
- 触るとき: そのメニュー項目を表示する条件を変えるとき。
- 参照: `PrefObserver.alwaysOpenInSystemViewerContextMenuItem`

## getData()
- 位置: L227-242
- 役割: ウィンドウの私用・公開と履歴の要否に応じて、対応するダウンロードデータ (全件、履歴、制限付き) を返す。
- 触るとき: パネルや一覧がどのデータの集まりを購読するかを変えるとき。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isContentWindowPrivate()`
- 参照: `lazy.DownloadsData`, `lazy.HistoryDownloadsData`, `lazy.LimitedHistoryDownloadsData`, `lazy.LimitedPrivateHistoryDownloadData`, `lazy.PrivateDownloadsData`

## initializeAllDataLinks()
- 位置: L248-251
- 役割: 公開と私用の両方のダウンロードデータで、バックエンドとの接続を開始する。
- 触るとき: 起動時にダウンロードの読み込みが始まらない問題を調べるとき。
- 呼び出し先: `lazy.DownloadsData.initializeDataLink()`, `lazy.PrivateDownloadsData.initializeDataLink()`

## initializeForWindow()
- 位置: L264-270
- 役割: ウィンドウ初期化時に、データ接続、タスクバー進捗の登録、macOS の Finder 進捗の登録を行う。
- 触るとき: 起動後のアイドル時にダウンロード機能の初期化を遅らせる仕組みを変えるとき。
- 呼び出し先: `lazy.DownloadsTaskbar.registerIndicator()`, `lazy.DownloadsTaskbar.registerIndicator(window).catch()`, `this.initializeAllDataLinks()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `lazy.DownloadsMacFinderProgress.register()`
- 参照: `AppConstants.platform`, `console.error`

## getIndicatorData()
- 位置: L277-282
- 役割: ウィンドウが私用なら私用用、そうでなければ公開用のインジケーターデータを返す。
- 触るとき: ツールバーのダウンロードボタンがどのインジケーターを見るかを追うとき。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isContentWindowPrivate()`
- 参照: `lazy.DownloadsIndicatorData`, `lazy.PrivateDownloadsIndicatorData`

## getSummary()
- 位置: L294-308
- 役割: 私用か公開かに応じて DownloadsSummaryData を一度だけ作って返す。aNumToExclude の件数だけ先頭を除外する。
- 触るとき: ダウンロードの要約 (進捗、残り時間) の対象範囲を変えるとき。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isContentWindowPrivate()`
- 参照: `this._privateSummary`, `this._summary`

## stateOfDownload()
- 位置: L315-351
- 役割: Download の状態を、停止、成功、各種エラー、キャンセル、一時停止の優先順位で旧来の数値状態に変換する。
- 触るとき: 状態の判定を変えたり、新しい状態を追加したりするとき。ほとんどの表示はこの値を基にしている。
- 参照: `DownloadsCommon.DOWNLOAD_BLOCKED_CONTENT_ANALYSIS`, `DownloadsCommon.DOWNLOAD_BLOCKED_PARENTAL`, `DownloadsCommon.DOWNLOAD_CANCELED`, `DownloadsCommon.DOWNLOAD_DIRTY`, `DownloadsCommon.DOWNLOAD_DOWNLOADING`, `DownloadsCommon.DOWNLOAD_FAILED`, `DownloadsCommon.DOWNLOAD_FINISHED`, `DownloadsCommon.DOWNLOAD_NOTSTARTED`, `DownloadsCommon.DOWNLOAD_PAUSED`, `download.canceled`, `download.error`, `download.error.becauseBlockedByContentAnalysis`, `download.error.becauseBlockedByParentalControls`, `download.error.becauseBlockedByReputationCheck`, `download.error.reputationCheckVerdict`, `download.hasPartialData`, `download.stopped`, `download.succeeded`, `lazy.Downloads.Error.BLOCK_VERDICT_MALWARE`

## deleteDownload()
- 位置: async L356-374
- 役割: 履歴の URL を消し、一覧から除いてから、ブロックの確認やコンテンツ分析の応答を行い、最後に finalize する。
- 触るとき: 一覧から項目を完全に削除する流れ (履歴、ファイル、ブロック) を変えるとき。
- 呼び出し先: `URL.parse()`, `download.finalize()`, `lazy.Downloads.getList()`, `lazy.PlacesUtils.history.canAddURI()`, `list.remove()`
- 条件付き依存: `if (sourceURI && lazy.PlacesUtils.history.canAddURI(sourceURI))` → `lazy.PlacesUtils.history.remove(sourceURI).catch()`
- 条件付き依存: `if (sourceURI && lazy.PlacesUtils.history.canAddURI(sourceURI))` → `lazy.PlacesUtils.history.remove()`
- 条件付き依存: `if (download.hasBlockedData)` → `download.confirmBlock()`
- 条件付き依存: `if (download.error?.becauseBlockedByContentAnalysis)` → `download.respondToContentAnalysisWarnWithBlock()`
- 参照: `URL.parse(download.source.url)?.URI`, `console.error`, `download.error?.becauseBlockedByContentAnalysis`, `download.hasBlockedData`, `download.source.url`, `lazy.Downloads.ALL`

## deleteDownloadFiles()
- 位置: async L388-406
- 役割: clearHistoryOnDelete の値に応じて履歴 URL と一覧を消し、ファイルを削除し、必要ならメタデータを更新する。
- 触るとき: 「ファイルを削除」が履歴に残す範囲を変えるとき。
- 呼び出し先: `download.manuallyRemoveData()`
- 条件付き依存: `if (clearHistoryOnDelete > 1)` → `URL.parse()`
- 条件付き依存: `if (clearHistoryOnDelete > 1)` → `lazy.PlacesUtils.history.canAddURI()`
- 条件付き依存: `if (sourceURI && lazy.PlacesUtils.history.canAddURI(sourceURI))` → `lazy.PlacesUtils.history.remove(sourceURI).catch()`
- 条件付き依存: `if (sourceURI && lazy.PlacesUtils.history.canAddURI(sourceURI))` → `lazy.PlacesUtils.history.remove()`
- 条件付き依存: `if (clearHistoryOnDelete > 0)` → `lazy.Downloads.getList()`
- 条件付き依存: `if (clearHistoryOnDelete > 0)` → `list.remove()`
- 条件付き依存: `if (download.error?.becauseBlockedByContentAnalysis)` → `download.respondToContentAnalysisWarnWithBlock()`
- 条件付き依存: `if (clearHistoryOnDelete < 2)` → `lazy.DownloadHistory.updateMetaData(download).catch()`
- 条件付き依存: `if (clearHistoryOnDelete < 2)` → `lazy.DownloadHistory.updateMetaData()`
- 参照: `URL.parse(download.source.url)?.URI`, `console.error`, `download.error?.becauseBlockedByContentAnalysis`, `download.source.url`, `lazy.Downloads.ALL`

## getMimeInfo()
- 位置: L411-453
- 役割: 成功したダウンロードについて、Content-Type か拡張子から nsIMIMEInfo を取得する。取得できなければ null を返す。
- 触るとき: ファイルの種類による開き方 (内部表示、システム既定) の判定を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/network/standard-url-mutator;1"] .createInstance()`, `Cc["@mozilla.org/network/standard-url-mutator;1"] .createInstance(Ci.nsIURIMutator) .setSpec()`, `DownloadsCommon.log()`, `kGenericContentTypes.includes()`, `lazy.gMIMEService.getFromTypeAndExtension()`
- 条件付き依存: `if (!contentType || kGenericContentTypes.includes(contentType))` → `lazy.gMIMEService.getTypeFromExtension()`
- 条件付き依存: `if (!contentType || kGenericContentTypes.includes(contentType))` → `DownloadsCommon.log()`
- 参照: `Ci.nsIURIMutator`, `Ci.nsIURL`, `download.contentType`, `download.succeeded`, `download.target.path`, `url.fileExtension`
- XPCOM: [`nsIURIMutator`](../../../netwerk/base/nsIFileURL.idl.md) / [`nsIURL`](../../../netwerk/base/nsIURL.idl.md) / `@mozilla.org/network/standard-url-mutator;1`

## isFileOfType()
- 位置: L458-467
- 役割: 成功して存在するダウンロードの MIME 型が、指定の型 (小文字比較) と一致するかを返す。
- 触るとき: 特定の種類のファイルだけに機能を適用するときに使う。
- 呼び出し先: `DownloadsCommon.getMimeInfo()`, `mimeType.toLowerCase()`
- 条件付き依存: `if (!(download.succeeded && download.target?.exists))` → `DownloadsCommon.log()`
- 参照: `download.succeeded`, `download.target?.exists`, `mimeInfo?.type`

## copyDownloadLink()
- 位置: L472-476
- 役割: ダウンロード元 URL (元の URL 優先) をクリップボードにコピーする。
- 触るとき: 「ダウンロードのリンクをコピー」の対象 URL を変えるとき。
- 呼び出し先: `lazy.gClipboardHelper.copyString()`
- 参照: `download.source.originalUrl`, `download.source.url`

## summarizeDownloads()
- 位置: L498-552
- 役割: ダウンロード列から、件数、一時停止数、総サイズ、転送量、最も遅い速度、残り時間、完了率を集計する。
- 触るとき: 進捗表示や残り時間の数値が合わないときに見る。
- 条件付き依存: `if (download.hasProgress && download.speed > 0)` → `Math.max()`
- 条件付き依存: `if (download.hasProgress && download.speed > 0)` → `Math.min()`
- 条件付き依存: `if (summary.totalSize != 0)` → `Math.floor()`
- 参照: `download.canceled`, `download.currentBytes`, `download.hasPartialData`, `download.hasProgress`, `download.speed`, `download.stopped`, `download.succeeded`, `download.target.size`, `download.totalBytes`, `summary.numActive`, `summary.numDownloading`, `summary.numPaused`, `summary.percentComplete`, `summary.rawTimeLeft`, `summary.slowestSpeed`, `summary.totalSize`, `summary.totalTransferred`

## smoothSeconds()
- 位置: L563-587
- 役割: 残り秒数の推定値を、前回の値に対してヒステリシス付きで平滑化する。下限は 1 秒。
- 触るとき: 残り時間の表示がふらつく、または急に増減するといった問題を調べるとき。
- 呼び出し先: `Math.max()`
- 条件付き依存: `if (shouldApplySmoothing)` → `Math.abs()`

## openDownload()
- 位置: async L606-612
- 役割: ダウンロードを開く。シリアライズされた値なら Download を作り直してから launch を呼ぶ。
- 触るとき: ダウンロードを開く経路 (開き先、システム既定の指定) を変えるとき。
- 呼び出し先: `console.error()`, `download.launch()`, `download.launch(options).catch()`
- 条件付き依存: `if (typeof download.launch !== "function")` → `lazy.Downloads.createDownload()`
- 参照: `download.launch`

## showDownloadedFile()
- 位置: L620-635
- 役割: ファイルを reveal で表示する。失敗したら親フォルダーを showDirectory で開く。
- 触るとき: 「フォルダーで表示」が特定の OS で動かないときに見る。
- 呼び出し先: `aFile.reveal()`
- 条件付き依存: `if (parent)` → `this.showDirectory()`
- 参照: `Ci.nsIFile`, `aFile.parent`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md)

## showDirectory()
- 位置: L643-659
- 役割: フォルダーを launch で開き、失敗したら外部プロトコルのサービスで開く。
- 触るとき: フォルダーを開く手段の順番を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/uriloader/external-protocol-service;1"] .getService()`, `Cc["@mozilla.org/uriloader/external-protocol-service;1"] .getService(Ci.nsIExternalProtocolService) .loadURI()`, `Services.scriptSecurityManager.getSystemPrincipal()`, `aDirectory.launch()`, `lazy.NetUtil.newURI()`
- 参照: `Ci.nsIExternalProtocolService`, `Ci.nsIFile`
- XPCOM: [`nsIExternalProtocolService`](../../../uriloader/exthandler/nsIExternalProtocolService.idl.md) / [`nsIFile`](../shell/nsIShellService.idl.md) / `@mozilla.org/uriloader/external-protocol-service;1` / `Services.scriptSecurityManager`

## confirmUnblockDownload()
- 位置: async L691-795
- 役割: 判定 (verdict) と dialogType に応じて確認ダイアログの文言とボタンを選び、押されたボタンを open、unblock、confirmBlock、cancel のいずれかで返す。
- 触るとき: ブロック解除の確認ダイアログの文言やボタンを変えるとき。
- 呼び出し先: `Services.prompt.confirmEx()`, `Services.ww.registerNotification()`, `console.error()`
- 参照: `Ci.nsIPrompt.BUTTON_POS_0`, `Ci.nsIPrompt.BUTTON_POS_0_DEFAULT`, `Ci.nsIPrompt.BUTTON_POS_1`, `Ci.nsIPrompt.BUTTON_POS_1_DEFAULT`, `Ci.nsIPrompt.BUTTON_POS_2`, `Ci.nsIPrompt.BUTTON_POS_2_DEFAULT`, `Ci.nsIPrompt.BUTTON_TITLE_CANCEL`, `Ci.nsIPrompt.BUTTON_TITLE_IS_STRING`, `DownloadsCommon.strings`, `lazy.Downloads.Error.BLOCK_VERDICT_INSECURE`, `lazy.Downloads.Error.BLOCK_VERDICT_POTENTIALLY_UNWANTED`, `lazy.Downloads.Error.BLOCK_VERDICT_UNCOMMON`, `s.unblockButtonConfirmBlock`, `s.unblockButtonOpen`, `s.unblockButtonUnblock`, `s.unblockContentAnalysisTip`, `s.unblockHeaderOpen`, `s.unblockHeaderUnblock`, `s.unblockInsecure2`, `s.unblockTip2`, `s.unblockTypeContentAnalysisWarn`, `s.unblockTypeMalware`, `s.unblockTypePotentiallyUnwanted2`, `s.unblockTypeUncommon2`
- XPCOM: [`nsIPrompt`](../../../netwerk/base/nsIAuthPrompt.idl.md) / `Services.prompt` / `Services.ww`

## onOpen()
- 位置: L759-781
- 役割: 確認ダイアログが開いたら、共通ダイアログに警告アイコンのクラスを付ける。
- 触るとき: 確認ダイアログの見た目 (警告表示) を変えるとき。
- 条件付き依存: `if (topic == "domwindowopened" && subj instanceof Ci.nsIDOMWindow)` → `subj.addEventListener()`
- 条件付き依存: `if ( subj.document.documentURI == "chrome://global/content/commonDialog.xhtml" )` → `Services.ww.unregisterNotification()`
- 条件付き依存: `if ( subj.document.documentURI == "chrome://global/content/commonDialog.xhtml" )` → `subj.document.getElementById()`
- 条件付き依存: `if (dialog)` → `dialog.classList.add()`
- 参照: `Ci.nsIDOMWindow`, `subj.document.documentURI`
- XPCOM: [`nsIDOMWindow`](../../../dom/base/nsISlowScriptDebug.idl.md) / `Services.ww`

## DownloadsDataCtor()
- 位置: L819-857
- 役割: ダウンロードデータのコンストラクター。履歴版は公開または私用のリストを取得し、通常版は Download 一覧を購読する。初期化は initializeDataLink を呼ぶまで遅らせる。
- 触るとき: 起動時にダウンロード一覧が読み込まれるタイミング、または履歴の取得元を変えるとき。
- 呼び出し先: `lazy.Downloads.getList()`, `list.addView()`
- 条件付き依存: `if (isPrivate)` → `lazy.PrivateDownloadsData.initializeDataLink()`
- 条件付き依存: `if (isHistory)` → `lazy.DownloadsData.initializeDataLink()`
- 条件付き依存: `if (isHistory)` → `lazy.DownloadsData._promiseList.then()`
- 条件付き依存: `if (isHistory)` → `lazy.DownloadHistory.getList()`
- 参照: `lazy.Downloads.ALL`, `lazy.Downloads.PRIVATE`, `lazy.Downloads.PUBLIC`, `this._isPrivate`, `this._oldDownloadStates`, `this._promiseList`, `this.initializeDataLink`

## initializeDataLink()
- 位置: L863-863
- 役割: 既定では何もしない。コンストラクター内で resolve 関数に置き換えられ、呼ばれると遅延していた読み込みが始まる。
- 触るとき: ダウンロードの読み込みを開始する契機を追うとき。

## _downloads()
- 位置: L875-877
- 役割: 読み込み済みの Download をすべて列挙するイテレーターを返す。
- 触るとき: ダウンロードの集計や検索の対象範囲を確認するとき。
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakMapKeys()`
- 参照: `this._oldDownloadStates`

## canRemoveFinished()
- 位置: L882-890
- 役割: 停止済みで、キャンセルかつ部分データを持たないものがあれば true を返す。
- 触るとき: 「ダウンロードを消去」が有効かどうかの判定を変えるとき。
- 参照: `download.canceled`, `download.hasPartialData`, `download.stopped`, `this._downloads`

## removeFinished()
- 位置: L896-902
- 役割: バックエンドのリストに、終了済みダウンロードの削除を依頼する。
- 触るとき: 終了済みのダウンロードの消去が効かない問題を調べるとき。
- 呼び出し先: `lazy.Downloads.getList()`, `lazy.Downloads.getList( this._isPrivate ? lazy.Downloads.PRIVATE : lazy.Downloads.PUBLIC ) .then()`, `list.removeFinished()`
- 参照: `console.error`, `lazy.Downloads.PRIVATE`, `lazy.Downloads.PUBLIC`, `this._isPrivate`

## onDownloadAdded()
- 位置: L906-923
- 役割: 追加された Download に終了時刻を仮に入れ、状態を記録する。ブロックや内容分析のエラーなら error 通知を出す。
- 触るとき: 新規ダウンロードがエラー通知を出す条件を変えるとき。
- 呼び出し先: `Date.now()`, `DownloadsCommon.stateOfDownload()`, `this._oldDownloadStates.set()`
- 条件付き依存: `if ( download.error?.becauseBlockedByReputationCheck || download.error?.becauseBlockedByContentAnalysis )` → `this._notifyDownloadEvent()`
- 参照: `download.endTime`, `download.error?.becauseBlockedByContentAnalysis`, `download.error?.becauseBlockedByReputationCheck`

## onDownloadChanged()
- 位置: L925-972
- 役割: 状態の遷移時に終了時刻、履歴のメタデータ、大きい data URI の切り詰めを行い、完了・ブロック時に finish 通知を出す。初回には start 通知を出す。
- 触るとき: パネルの開閉通知が出ない、または大きい data URI の保持量を変えたいときに見る。
- 呼び出し先: `DownloadsCommon.stateOfDownload()`, `this._oldDownloadStates.get()`, `this._oldDownloadStates.set()`
- 条件付き依存: `if ( download.succeeded || (download.canceled && !download.hasPartialData) || download.error )` → `Date.now()`
- 条件付き依存: `if ( download.succeeded || (download.canceled && !download.hasPartialData) || download.error )` → `lazy.DownloadHistory.updateMetaData(download).catch()`
- 条件付き依存: `if ( download.succeeded || (download.canceled && !download.hasPartialData) || download.error )` → `lazy.DownloadHistory.updateMetaData()`
- 条件付き依存: `if ( download.succeeded || (download.canceled && !download.hasPartialData) || download.error )` → `download.source.url?.startsWith()`
- 条件付き依存: `if ( download.succeeded && download.source.url?.startsWith("data:") && download.source.url.length > kLargeDataUriLengthThreshold )` → `download.source.url.indexOf()`
- 条件付き依存: `if ( download.succeeded && download.source.url?.startsWith("data:") && download.source.url.length > kLargeDataUriLengthThreshold )` → `download.source.url.slice()`
- 条件付き依存: `if ( download.succeeded || (download.error && download.error.becauseBlocked) )` → `this._notifyDownloadEvent()`
- 条件付き依存: `if (!download.newDownloadNotified)` → `this._notifyDownloadEvent()`
- 参照: `console.error`, `download.canceled`, `download.endTime`, `download.error`, `download.error.becauseBlocked`, `download.hasPartialData`, `download.newDownloadNotified`, `download.openDownloadsListOnStart`, `download.source.isDataURICleared`, `download.source.url`, `download.source.url.length`, `download.succeeded`

## onDownloadRemoved()
- 位置: L974-976
- 役割: 削除された Download の状態記録を消す。
- 触るとき: 削除後に状態の記録が残る問題を追うとき。
- 呼び出し先: `this._oldDownloadStates.delete()`

## addView()
- 位置: L988-990
- 役割: ビューを、バックエンドのリストに非同期で登録する。
- 触るとき: 一覧やインジケーターがデータを受け取らない問題を調べるとき。
- 呼び出し先: `list.addView()`, `this._promiseList.then()`, `this._promiseList.then(list => list.addView(aView)).catch()`
- 参照: `console.error`

## removeView()
- 位置: L998-1000
- 役割: ビューを、バックエンドのリストから非同期で外す。
- 触るとき: ウィンドウを閉じた後も購読が残る問題を調べるとき。
- 呼び出し先: `list.removeView()`, `this._promiseList.then()`, `this._promiseList.then(list => list.removeView(aView)).catch()`
- 参照: `console.error`

## panelHasShownBefore()
- 位置: L1008-1013
- 役割: pref browser.download.panel.shown を読む。読めなければ false を返す。
- 触るとき: 初めてのダウンロードでパネルを自動表示する条件を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## panelHasShownBefore()
- 位置: L1015-1017
- 役割: pref browser.download.panel.shown を書き込む。
- 触るとき: パネル表示の記録を変える処理を追うとき。
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## _notifyDownloadEvent()
- 位置: L1031-1069
- 役割: 最前面のブラウザーウィンドウに対して、開始、完了、エラーのどれかの通知を出す。開始時は条件によりパネルを開き、それ以外はインジケーター通知にとどめる。
- 触るとき: ダウンロード開始時にパネルが開く条件、または通知の種類を変えるとき。
- 呼び出し先: `DownloadsCommon.log()`, `DownloadsCommon.summarizeDownloads()`, `browserWin.DownloadsPanel.showPanel()`, `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if ( aType != "error" && ((this.panelHasShownBefore && !shouldOpenDownloadsPanel) || !openDownloadsListOnStart || browserWin != Services.focus.activeWindow) )` → `DownloadsCommon.log()`
- 条件付き依存: `if ( aType != "error" && ((this.panelHasShownBefore && !shouldOpenDownloadsPanel) || !openDownloadsListOnStart || browserWin != Services.focus.activeWindow) )` → `browserWin.DownloadsIndicatorView.showEventNotification()`
- 参照: `DownloadsCommon.summarizeDownloads(this._downloads).numDownloading`, `Services.focus.activeWindow`, `lazy.gAlwaysOpenPanel`, `this._downloads`, `this._isPrivate`, `this.panelHasShownBefore`
- XPCOM: `Services.focus`

## addView()
- 位置: L1143-1155
- 役割: ビューを登録する。最初のビューのときだけバックエンドの購読を始め、その後に現在の状態を反映する。
- 触るとき: ビューの初回登録時に購読が始まるかどうかを確認するとき。
- 呼び出し先: `this._views.push()`, `this.refreshView()`
- 条件付き依存: `if (this._isPrivate)` → `lazy.PrivateDownloadsData.addView()`
- 条件付き依存: `if (!(this._isPrivate))` → `lazy.DownloadsData.addView()`
- 参照: `this._isPrivate`, `this._views.length`

## refreshView()
- 位置: L1163-1168
- 役割: 集計値を更新し、そのビューへ反映する。
- 触るとき: ビューを登録した直後に表示が古いままになる問題を調べるとき。
- 呼び出し先: `this._refreshProperties()`, `this._updateView()`

## removeView()
- 位置: L1176-1190
- 役割: ビューを外し、最後のビューなら購読を止める。
- 触るとき: 購読が止まるタイミングを変えるとき。
- 呼び出し先: `this._views.indexOf()`
- 条件付き依存: `if (index != -1)` → `this._views.splice()`
- 条件付き依存: `if (this._isPrivate)` → `lazy.PrivateDownloadsData.removeView()`
- 条件付き依存: `if (!(this._isPrivate))` → `lazy.DownloadsData.removeView()`
- 参照: `this._isPrivate`, `this._views.length`

## onDownloadBatchStarting()
- 位置: L1202-1204
- 役割: 読み込み中フラグを立て、一括読み込み中は表示を更新しないようにする。
- 触るとき: 起動時の大量の読み込みで表示が点滅する問題を調べるとき。
- 参照: `this._loading`

## onDownloadBatchEnded()
- 位置: L1209-1212
- 役割: 読み込み中フラグを下ろし、表示を一度だけ更新する。
- 触るとき: 読み込み完了後に表示が更新されない問題を追うとき。
- 呼び出し先: `this._updateViews()`
- 参照: `this._loading`

## onDownloadAdded()
- 位置: L1223-1228
- 役割: 基底の状態記録を行い、ビューの 1 件数分を更新する。
- 触るとき: 新規ダウンロード後に表示が更新されない問題を見るとき。
- 呼び出し先: `DownloadsCommon.stateOfDownload()`, `this._oldDownloadStates.set()`

## onDownloadStateChanged()
- 位置: L1239-1241
- 役割: 状態遷移時の処理の基底。何もしない。
- 触るとき: 状態遷移時の共通処理を足すときに、ここを派生で上書きする。
- 呼び出し先: `Components.Exception()`
- 参照: `Cr.NS_ERROR_NOT_IMPLEMENTED`

## onDownloadChanged()
- 位置: L1252-1260
- 役割: 旧状態と新状態を比べ、変わっていれば onDownloadStateChanged を呼ぶ。
- 触るとき: 状態が変わったときにだけ処理させたいとき。
- 呼び出し先: `DownloadsCommon.stateOfDownload()`, `this._oldDownloadStates.get()`, `this._oldDownloadStates.set()`
- 条件付き依存: `if (oldState != newState)` → `this.onDownloadStateChanged()`

## onDownloadRemoved()
- 位置: L1271-1273
- 役割: 削除された Download の状態記録を消す。
- 触るとき: 削除時の基底処理を変えるとき。
- 呼び出し先: `this._oldDownloadStates.delete()`

## _refreshProperties()
- 位置: L1281-1283
- 役割: 派生が上書きする前提の集計更新。基底は例外を投げる。
- 触るとき: 集計を行うビューを新しく作るとき、このメソッドを実装する。
- 呼び出し先: `Components.Exception()`
- 参照: `Cr.NS_ERROR_NOT_IMPLEMENTED`

## _updateView()
- 位置: L1290-1292
- 役割: 派生が上書きする前提の、ビューへの反映。基底は例外を投げる。
- 触るとき: 新しいビューに値を渡す仕組みを作るとき、このメソッドを実装する。
- 呼び出し先: `Components.Exception()`
- 参照: `Cr.NS_ERROR_NOT_IMPLEMENTED`

## _updateViews()
- 位置: L1297-1305
- 役割: 読み込み中でなければ集計を更新し、登録されている全ビューへ反映する。
- 触るとき: インジケーターや要約の表示が一括で更新されない問題を調べるとき。
- 呼び出し先: `this._refreshProperties()`, `this._views.forEach()`
- 参照: `this._loading`, `this._updateView`

## DownloadsIndicatorDataCtor()
- 位置: L1320-1324
- 役割: インジケーターのデータのコンストラクター。私用か公開かの区別と、ビュー一覧を持つ。
- 触るとき: インジケーターのデータが公開と私用で分かれる仕組みを変えるとき。
- 参照: `this._isPrivate`, `this._oldDownloadStates`, `this._views`

## _downloads()
- 位置: L1343-1345
- 役割: 読み込み済みの Download を列挙するイテレーター。
- 触るとき: インジケーターの注意表示の対象を調べるとき。
- 呼び出し先: `ChromeUtils.nondeterministicGetWeakMapKeys()`
- 参照: `this._oldDownloadStates`

## removeView()
- 位置: L1353-1359
- 役割: ビューを外し、最後の 1 件が外れたら件数をゼロに戻す。
- 触るとき: インジケーターを閉じた後に件数が残る問題を調べるとき。
- 呼び出し先: `DownloadsViewPrototype.removeView.call()`
- 参照: `this._itemCount`, `this._views.length`

## onDownloadAdded()
- 位置: L1361-1365
- 役割: 件数を 1 増やし、表示を更新する。
- 触るとき: ダウンロード件数のバッジが増えない問題を見るとき。
- 呼び出し先: `DownloadsViewPrototype.onDownloadAdded.call()`, `this._updateViews()`
- 参照: `this._itemCount`

## onDownloadStateChanged()
- 位置: L1367-1403
- 役割: 成功、エラー、ブロックの判定に応じて注意の種類 (成功、情報、警告、重大) を決め、注意表示を更新する。抑止中は何もしない。
- 触るとき: ダウンロード完了やブロック時にインジケーターが光る条件を変えるとき。
- 呼び出し先: `this.updateAttention()`
- 条件付き依存: `if ( !download.succeeded && download.error && download.error.reputationCheckVerdict )` → `console.error()`
- 参照: `DownloadsCommon.ATTENTION_INFO`, `DownloadsCommon.ATTENTION_SEVERE`, `DownloadsCommon.ATTENTION_SUCCESS`, `DownloadsCommon.ATTENTION_WARNING`, `DownloadsCommon.SUPPRESS_NONE`, `download.attention`, `download.error`, `download.error.reputationCheckVerdict`, `download.succeeded`, `lazy.Downloads.Error.BLOCK_VERDICT_DOWNLOAD_SPAM`, `lazy.Downloads.Error.BLOCK_VERDICT_INSECURE`, `lazy.Downloads.Error.BLOCK_VERDICT_MALWARE`, `lazy.Downloads.Error.BLOCK_VERDICT_POTENTIALLY_UNWANTED`, `lazy.Downloads.Error.BLOCK_VERDICT_UNCOMMON`, `this._attentionSuppressed`

## onDownloadChanged()
- 位置: L1405-1408
- 役割: 基底の処理を呼び、表示を更新する。
- 触るとき: インジケーターの表示更新の頻度を変えるとき。
- 呼び出し先: `DownloadsViewPrototype.onDownloadChanged.call()`, `this._updateViews()`

## onDownloadRemoved()
- 位置: L1410-1415
- 役割: 件数を 1 減らし、注意表示を再計算してから表示を更新する。
- 触るとき: 削除後に注意表示が残る問題を調べるとき。
- 呼び出し先: `DownloadsViewPrototype.onDownloadRemoved.call()`, `this._updateViews()`, `this.updateAttention()`
- 参照: `this._itemCount`

## attention()
- 位置: L1427-1430
- 役割: 注意の種類を保存し、表示を更新する。
- 触るとき: インジケーターの注意の色や状態を変えるとき。
- 呼び出し先: `this._updateViews()`
- 参照: `this._attention`

## attentionSuppressed()
- 位置: L1437-1445
- 役割: 抑止フラグを保存する。抑止が有効になったら全 Download と表示の注意を消す。
- 触るとき: パネルを開いている間に注意表示を出さない仕組みを変えるとき。
- 参照: `DownloadsCommon.ATTENTION_NONE`, `DownloadsCommon.SUPPRESS_NONE`, `download.attention`, `this._attentionSuppressed`, `this._downloads`, `this.attention`

## attentionSuppressed()
- 位置: L1446-1448
- 役割: 現在の抑止フラグを返す。
- 触るとき: 抑止中かを調べるとき。
- 参照: `this._attentionSuppressed`

## updateAttention()
- 位置: L1455-1467
- 役割: 未確認のダウンロードのうち、最も重い注意の種類を選んで表示に反映する。
- 触るとき: 注意の優先順位や未確認の範囲を変えるとき。
- 呼び出し先: `this._attentionPriority.get()`
- 参照: `DownloadsCommon.ATTENTION_NONE`, `this._downloads`, `this.attention`

## _updateView()
- 位置: L1475-1482
- 役割: 件数、割合、注意 (抑止中なら無し) をビューに反映する。
- 触るとき: インジケーターに表示する値を追加するとき。
- 参照: `DownloadsCommon.ATTENTION_NONE`, `DownloadsCommon.SUPPRESS_NONE`, `aView.attention`, `aView.hasDownloads`, `aView.percentComplete`, `this._attention`, `this._hasDownloads`, `this._percentComplete`, `this.attentionSuppressed`

## _activeDownloads()
- 位置: L1497-1509
- 役割: 現在のバッチ中のダウンロード、または一時停止中のものを列挙する。
- 触るとき: インジケーターの進捗計算の対象を変えるとき。
- 参照: `download.canceled`, `download.hasPartialData`, `download.isInCurrentBatch`, `lazy.DownloadsData._downloads`, `lazy.PrivateDownloadsData._downloads`, `this._isPrivate`

## _refreshProperties()
- 位置: L1514-1528
- 役割: アクティブなダウンロードを集計し、表示有無と完了率 (進行中なら最低 0%) を決める。
- 触るとき: インジケーターの進捗バーや表示有無の条件を変えるとき。
- 呼び出し先: `DownloadsCommon.summarizeDownloads()`, `this._activeDownloads()`
- 参照: `summary.numDownloading`, `summary.percentComplete`, `this._hasDownloads`, `this._itemCount`, `this._percentComplete`

## DownloadsSummaryData()
- 位置: L1563-1595
- 役割: 要約ビューのコンストラクター。除外件数と、私用か公開かを保持し、残り時間の平滑化用の値を初期化する。
- 触るとき: ダウンロード要約の除外の仕組み、または初期値を変えるとき。
- 参照: `this._description`, `this._details`, `this._downloads`, `this._isPrivate`, `this._lastRawTimeLeft`, `this._lastTimeLeft`, `this._loading`, `this._numActive`, `this._numToExclude`, `this._oldDownloadStates`, `this._percentComplete`, `this._showingProgress`, `this._views`

## removeView()
- 位置: L1604-1612
- 役割: ビューを外し、最後の 1 件が外れたら一覧を空にする。
- 触るとき: 要約を閉じた後に一覧が残る問題を調べるとき。
- 呼び出し先: `DownloadsViewPrototype.removeView.call()`
- 参照: `this._downloads`, `this._views.length`

## onDownloadAdded()
- 位置: L1614-1618
- 役割: 新しいダウンロードを一覧の先頭に入れて、表示を更新する。
- 触るとき: 要約の対象の順番を変えるとき。
- 呼び出し先: `DownloadsViewPrototype.onDownloadAdded.call()`, `this._downloads.unshift()`, `this._updateViews()`

## onDownloadStateChanged()
- 位置: L1620-1624
- 役割: 状態が変わったら残り時間の推定値をリセットする。
- 触るとき: 残り時間の表示が状態変化で飛ぶ問題を調べるとき。
- 参照: `this._lastRawTimeLeft`, `this._lastTimeLeft`

## onDownloadChanged()
- 位置: L1626-1629
- 役割: 基底の処理を呼び、表示を更新する。
- 触るとき: 要約の表示更新を追うとき。
- 呼び出し先: `DownloadsViewPrototype.onDownloadChanged.call()`, `this._updateViews()`

## onDownloadRemoved()
- 位置: L1631-1636
- 役割: 一覧から削除されたダウンロードを取り除き、表示を更新する。
- 触るとき: 要約の件数が削除後にずれる問題を調べるとき。indexOf が -1 を返すと splice(-1, 1) で末尾の項目が消える点は要確認。
- 呼び出し先: `DownloadsViewPrototype.onDownloadRemoved.call()`, `this._downloads.indexOf()`, `this._downloads.splice()`, `this._updateViews()`

## _updateView()
- 位置: L1646-1651
- 役割: 進捗の表示、完了率、説明文、詳細文をビューに反映する。
- 触るとき: 要約の表示に値を追加するとき。
- 参照: `aView.description`, `aView.details`, `aView.percentComplete`, `aView.showingProgress`, `this._description`, `this._details`, `this._percentComplete`, `this._showingProgress`

## _downloadsForSummary()
- 位置: L1662-1668
- 役割: 一覧のうち先頭の除外件数を飛ばした残りを列挙する。
- 触るとき: 要約の対象範囲を変えるとき。
- 参照: `this._downloads`, `this._downloads.length`, `this._numToExclude`

## _refreshProperties()
- 位置: L1673-1714
- 役割: 対象範囲を集計し、説明文、完了率、進捗表示の有無、残り時間 (平滑化後) を求める。
- 触るとき: 要約に出る残り時間や「ダウンロード中」の件数の計算を変えるとき。
- 呼び出し先: `DownloadsCommon.summarizeDownloads()`, `kDownloadsFluentStrings.formatValueSync()`, `this._downloadsForSummary()`
- 条件付き依存: `if (this._lastRawTimeLeft != summary.rawTimeLeft)` → `DownloadsCommon.smoothSeconds()`
- 条件付き依存: `if (!(summary.rawTimeLeft == -1))` → `lazy.DownloadUtils.getDownloadStatusNoRate()`
- 参照: `summary.numDownloading`, `summary.percentComplete`, `summary.rawTimeLeft`, `summary.slowestSpeed`, `summary.totalSize`, `summary.totalTransferred`, `this._description`, `this._details`, `this._lastRawTimeLeft`, `this._lastTimeLeft`, `this._percentComplete`, `this._showingProgress`
