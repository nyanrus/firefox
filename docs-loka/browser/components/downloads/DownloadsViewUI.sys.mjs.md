# browser/components/downloads/DownloadsViewUI.sys.mjs

source: browser/components/downloads/DownloadsViewUI.sys.mjs
source-hash: 10b9e6ef4943fcea65da61130103d51c587dd512
lines: 1293

## <module>
- 役割: download.xml バインディングを使う一覧とパネルの表示・コマンド処理を担う prototype 群 (要素シェル、表示更新、コマンド実行) を提供する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Integration.downloads.defineESModuleGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetter()`

## isCommandName()
- 位置: L125-127
- 役割: 名前が cmd_ または downloadsCmd_ で始まるかを返す。
- 触るとき: 新しいコマンドを追加したとき、それが一覧のコマンドとして扱われるかを確認するとき。
- 呼び出し先: `name.startsWith()`

## getStrippedUrl()
- 位置: L132-137
- 役割: ダウンロード元 URL から http と https の接頭辞を除いた表示用文字列を返す。
- 触るとき: 一覧やブロック通知に出る URL の見た目を変えるとき。
- 呼び出し先: `lazy.UrlbarShared.stripPrefixAndTrim()`
- 参照: `download?.source?.url`

## getDisplayName()
- 位置: L145-159
- 役割: スパム判定で拒否されたものは URL の表示文言、それ以外はターゲットのファイル名 (なければ元 URL) を返す。
- 触るとき: ダウンロード一覧に表示される名前が想定と違うとき、または履歴の古い項目で名前が出ないときに見る。
- 呼び出し先: `PathUtils.filename()`
- 条件付き依存: `if ( download.error?.reputationCheckVerdict == lazy.Downloads.Error.BLOCK_VERDICT_DOWNLOAD_SPAM )` → `DownloadsViewUI.getStrippedUrl()`
- 参照: `download.error?.reputationCheckVerdict`, `download.source.url`, `download.target.path`, `lazy.Downloads.Error.BLOCK_VERDICT_DOWNLOAD_SPAM`

## getSizeWithUnits()
- 位置: L166-175
- 役割: ターゲットのサイズを単位付きの文字列にする。サイズ不明なら空文字を返す。
- 触るとき: 完了済みダウンロードのサイズ表示を変えるとき。
- 呼び出し先: `lazy.DownloadUtils.convertByteUnits()`, `lazy.DownloadsCommon.strings.sizeWithUnits()`
- 参照: `download.target.size`

## updateContextMenuForElement()
- 位置: L182-366
- 役割: ダウンロードの状態と種類に応じて、右クリックメニューの各項目の表示・非表示と既定アプリ名の表示を決める。
- 触るとき: 右クリックメニューに出る項目が状態と合わない、または「システムビューアーで開く」などの項目が出ない問題を調べるとき。
- 呼び出し先: `PathUtils.filename()`, `Services.policies.isExemptExecutableExtension()`, `[ DOWNLOAD_NOTSTARTED, DOWNLOAD_DOWNLOADING, DOWNLOAD_FINISHED, DOWNLOAD_PAUSED, ].includes()`, `contextMenu.querySelector()`, `document.l10n.pauseObserving()`, `document.l10n.resumeObserving()`, `document.l10n.translateElements()`, `element.classList.contains()`, `element.getAttribute()`, `element.hasAttribute()`, `filename?.split()`, `filename?.split(".").at()`, `lazy.DownloadsCommon.getMimeInfo()`, `lazy.gReputationService.isBinary()`, `lazy.gReputationService.isExecutable()`, `parseInt()`
- 条件付き依存: `if (defaultDescription && defaultDescription.length < 40)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(defaultDescription && defaultDescription.length < 40))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (preferredAction === useSystemDefault)` → `alwaysUseSystemViewerItem.setAttribute()`
- 条件付き依存: `if (preferredAction === useSystemDefault)` → `alwaysOpenSimilarFilesItem.setAttribute()`
- 条件付き依存: `if (!(preferredAction === useSystemDefault))` → `alwaysUseSystemViewerItem.removeAttribute()`
- 条件付き依存: `if (!(preferredAction === useSystemDefault))` → `alwaysOpenSimilarFilesItem.removeAttribute()`
- 参照: `alwaysOpenSimilarFilesItem.hidden`, `alwaysUseSystemViewerItem.hidden`, `contextMenu.ownerDocument`, `contextMenu.querySelector(".downloadCommandsSeparator").hidden`, `contextMenu.querySelector(".downloadDeleteFileMenuItem").hidden`, `contextMenu.querySelector(".downloadOpenReferrerMenuItem").hidden`, `contextMenu.querySelector(".downloadPauseMenuItem").hidden`, `contextMenu.querySelector(".downloadRemoveFromHistoryMenuItem").hidden`, `contextMenu.querySelector(".downloadResumeMenuItem").hidden`, `contextMenu.querySelector(".downloadShowMenuItem").hidden`, `contextMenu.querySelector(".downloadUnblockMenuItem").hidden`, `defaultDescription.length`, `download.deleted`, `download.source.originalUrl`, `download.source.referrerInfo?.originalReferrer`, `download.source.url`, `download.target.path`, `download.target?.exists`, `download.target?.partFileExists`, `element._shell.download`, `lazy.DownloadsCommon`, `lazy.DownloadsCommon.alwaysOpenInSystemViewerItemEnabled`, `lazy.DownloadsCommon.openInSystemViewerItemEnabled`, `lazy.safeBrowsingAllowOverride`, `mimeInfo.type`, `mimeInfo?.type`, `useSystemViewerItem.hidden`
- XPCOM: `Services.policies`

## canClearDownloads()
- 位置: L377-390
- 役割: 一覧の末尾から見て、停止済みで部分データを持たないダウンロードが 1 つでもあれば true を返す。
- 触るとき: 「ダウンロードを消去」ボタンの有効・無効が想定と違うときに見る。
- 参照: `download.canceled`, `download.hasPartialData`, `download.stopped`, `elt._shell.download`, `elt.previousSibling`, `nodeContainer.lastChild`

## DownloadsViewUI.DownloadElementShell()
- 位置: L406-406
- 役割: 要素シェルの基底コンストラクター。中身は空で、派生側が prototype を継承して使う。
- 触るとき: 要素シェルの継承関係を変えるとき。

## ensureActive()
- 位置: L419-425
- 役割: まだ有効化されていなければ active にして connect で要素を組み立て、表示を更新する。
- 触るとき: 表示範囲に入ったときに項目の中身が描画されない問題を調べるとき。
- 条件付き依存: `if (!this._active)` → `this.connect()`
- 条件付き依存: `if (!this._active)` → `this.onChanged()`
- 参照: `this._active`

## active()
- 位置: L426-428
- 役割: 要素が有効化済みかを返す。
- 触るとき: 非表示の項目の更新を止めている条件を確認するとき。
- 参照: `this._active`

## connect()
- 位置: L430-486
- 役割: 要素にダウンロード用の子要素 (アイコン、名前、詳細、ボタン、進捗バー) を作って付け、クリックとボタンのイベントを DownloadsView に渡す。
- 触るとき: 項目の見た目の構造を変えるとき、またはボタンやクリックが効かない問題を見るとき。
- 呼び出し先: `document.createElementNS()`, `document.importNode()`, `downloadButton.addEventListener()`, `ev.target.documentGlobal.DownloadsView.onDownloadClick()`, `event.target.documentGlobal.DownloadsView.onDownloadButton()`, `gDownloadListItemFragments.get()`, `progress.setAttribute()`, `this._downloadTarget.insertAdjacentElement()`, `this.element.addEventListener()`, `this.element.appendChild()`, `this.element.querySelector()`, `this.element.setAttribute()`
- 条件付き依存: `if (!downloadListItemFragment)` → `MozXULElement.parseXULToFragment()`
- 条件付き依存: `if (!downloadListItemFragment)` → `gDownloadListItemFragments.set()`
- 参照: `document.defaultView.MozXULElement`, `progress.className`, `this._downloadProgress`, `this.element.ownerDocument`

## image()
- 位置: L491-509
- 役割: ターゲットのパスからファイル種別アイコンの moz-icon URL を作る。完了時は再読み込みさせるため state 引数を付ける。
- 触るとき: 完了後にファイルアイコンが古いままになる問題を調べるとき。
- 参照: `this.download.succeeded`, `this.download.target.path`

## browserWindow()
- 位置: L511-515
- 役割: 最前面のブラウザーウィンドウを、別ワークスペースのものも含めて取得する。
- 触るとき: 項目の操作がどのウィンドウに対して行われるかを追うとき。
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`

## showDisplayNameAndIcon()
- 位置: L525-538
- 役割: 表示名 (文字列または l10n 指定) とアイコンの src を要素へ設定する。
- 触るとき: 項目の名前やアイコンが表示されないときに見る。
- 呼び出し先: `this._downloadTypeIcon.setAttribute()`
- 条件付き依存: `if (displayName.l10n)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(displayName.l10n))` → `this._downloadTarget.setAttribute()`
- 参照: `displayName.l10n`, `displayName.l10n.args`, `displayName.l10n.id`, `this._downloadTarget`, `this.element.ownerDocument`

## showProgress()
- 位置: L550-557
- 役割: 進捗バーを数値で表示するか不確定表示にするかを切り替え、一時停止時のスタイルを付ける。
- 触るとき: 進捗バーの見た目や一時停止時の表示を変えるとき。
- 呼び出し先: `this._downloadProgress.toggleAttribute()`
- 条件付き依存: `if (mode == "undetermined")` → `this._downloadProgress.removeAttribute()`
- 条件付き依存: `if (!(mode == "undetermined"))` → `this._downloadProgress.setAttribute()`

## showStatus()
- 位置: L570-594
- 役割: 通常と hover の 2 つの状態行に、l10n 指定または文字列をそのまま設定する。
- 触るとき: 状態行の文言が更新されない、または hover 時に別の文言が出る問題を調べるとき。
- 条件付き依存: `if (status?.l10n)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(status?.l10n))` → `this._downloadDetailsNormal.removeAttribute()`
- 条件付き依存: `if (!(status?.l10n))` → `this._downloadDetailsNormal.setAttribute()`
- 条件付き依存: `if (hoverStatus?.l10n)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(hoverStatus?.l10n))` → `this._downloadDetailsHover.removeAttribute()`
- 条件付き依存: `if (!(hoverStatus?.l10n))` → `this._downloadDetailsHover.setAttribute()`
- 参照: `hoverStatus.l10n.args`, `hoverStatus.l10n.id`, `hoverStatus?.l10n`, `status.l10n.args`, `status.l10n.id`, `status?.l10n`, `this._downloadDetailsHover`, `this._downloadDetailsNormal`, `this.element.ownerDocument`

## showStatusWithDetails()
- 位置: L611-641
- 役割: 状態ラベルにホスト名と日付を組み合わせて表示する。パネルでは hover 用に別の文字列を使う。
- 触るとき: 一覧に出る「失敗 - ホスト - 時刻」のような行の組み立てを変えるとき。
- 呼び出し先: `URL.parse()`, `lazy.BrowserUtils.formatURIForDisplay()`, `lazy.DownloadUtils.getReadableDates()`, `lazy.DownloadsCommon.strings.statusSeparator()`
- 条件付き依存: `if (stateLabel.l10n)` → `this.showStatus()`
- 条件付き依存: `if (!this.isPanel)` → `this.showStatus()`
- 条件付き依存: `if (!(!this.isPanel))` → `this.showStatus()`
- 参照: `URL.parse(this.download.source.url)?.URI`, `stateLabel.l10n`, `this.download.endTime`, `this.download.source.url`, `this.isPanel`

## showButton()
- 位置: L649-665
- 役割: プリセットに従って主要ボタンのコマンド、文言、アイコンを設定し、表示する。
- 触るとき: 状態ごとにどのボタンが出るかを変えるとき。
- 呼び出し先: `document.l10n.setAttributes()`, `this._downloadButton.removeAttribute()`, `this._downloadButton.setAttribute()`
- 条件付き依存: `if (this.isPanel && descriptionL10nId)` → `document.l10n.setAttributes()`
- 参照: `this._downloadButton`, `this._downloadDetailsButtonHover`, `this.buttonCommandName`, `this.element.ownerDocument`, `this.isPanel`

## hideButton()
- 位置: L667-669
- 役割: 主要ボタンを隠す。
- 触るとき: ボタンが出ないことが仕様どおりかを確認するとき。
- 参照: `this._downloadButton.hidden`

## _updateState()
- 位置: L677-702
- 役割: 状態が大きく変わったときに、名前、アイコン、state 属性、ボタンを更新する。進行中になったらキャンセルボタンを出し、verdict を消す。
- 触るとき: ダウンロードの開始・完了・失敗の遷移で表示が追随しないときに見る。進捗の細かい更新は _updateStateInner 側。
- 呼び出し先: `DownloadsViewUI.getDisplayName()`, `lazy.DownloadsCommon.stateOfDownload()`, `this._updateStateInner()`, `this.element.setAttribute()`, `this.showDisplayNameAndIcon()`
- 条件付き依存: `if (!this.download.stopped)` → `this.showButton()`
- 条件付き依存: `if (!this.download.stopped)` → `this.element.removeAttribute()`
- 参照: `this.download`, `this.download.stopped`, `this.image`, `this.lastEstimatedSecondsLeft`

## _updateStateInner()
- 位置: L710-904
- 役割: 毎回の更新で、進行中なら残り時間と状態行を、停止後は完了・ブロック・失敗・キャンセル・一時停止ごとに表示と主要ボタンを決める。
- 触るとき: ダウンロードの状態ごとに出る文言やボタンを変えるとき、または進捗が更新されない問題を調べるとき。
- 呼び出し先: `this.element.classList.toggle()`
- 条件付き依存: `if (!this.download.stopped)` → `lazy.DownloadUtils.getDownloadStatus()`
- 条件付き依存: `if (this.download.launchWhenSucceeded)` → `lazy.DownloadUtils.getFormattedTimeStatus()`
- 条件付き依存: `if (!this.download.stopped)` → `this.showStatus()`
- 条件付き依存: `if (this.download.deleted)` → `this.showDeletedOrMissing()`
- 条件付き依存: `if (this.download.succeeded)` → `lazy.DownloadsCommon.log()`
- 条件付き依存: `if (this.download.target.exists)` → `this.element.setAttribute()`
- 条件付き依存: `if (this.download.target.exists)` → `this.element.toggleAttribute()`
- 条件付き依存: `if (this.download.target.exists)` → `lazy.DownloadIntegration.shouldViewDownloadInternally()`
- 条件付き依存: `if (this.download.target.exists)` → `lazy.DownloadsCommon.getMimeInfo()`
- 条件付き依存: `if (this.download.target.exists)` → `DownloadsViewUI.getSizeWithUnits()`
- 条件付き依存: `if (sizeWithUnits)` → `lazy.DownloadsCommon.strings.statusSeparator()`
- 条件付き依存: `if (this.isPanel)` → `this.showStatus()`
- 条件付き依存: `if (!(this.isPanel))` → `this.showStatusWithDetails()`
- 条件付き依存: `if (this.download.target.exists)` → `this.showButton()`
- 条件付き依存: `if (!(this.download.target.exists))` → `this.showDeletedOrMissing()`
- 条件付き依存: `if (this.download.error.becauseBlockedByParentalControls)` → `this.showStatusWithDetails()`
- 条件付き依存: `if (this.download.error.becauseBlockedByParentalControls)` → `this.hideButton()`
- 条件付き依存: `if (!this.download.hasBlockedData)` → `this.hideButton()`
- 条件付き依存: `if (this.isPanel)` → `this.showButton()`
- 条件付き依存: `if (this.download.launchWhenSucceeded)` → `this.showButton()`
- 条件付き依存: `if (!(this.download.launchWhenSucceeded))` → `this.showButton()`
- 条件付き依存: `if (!(this.isPanel))` → `this.showButton()`
- 条件付き依存: `if ( this.download.error.becauseBlockedByReputationCheck || this.download.error.becauseBlockedByContentAnalysis )` → `this.showStatusWithDetails()`
- 条件付き依存: `if (!( this.download.error.becauseBlockedByReputationCheck || this.download.error.becauseBlockedByContentAnalysis ))` → `this.showStatusWithDetails()`
- 条件付き依存: `if (!( this.download.error.becauseBlockedByReputationCheck || this.download.error.becauseBlockedByContentAnalysis ))` → `this.showButton()`
- 条件付き依存: `if (this.download.hasPartialData)` → `lazy.DownloadUtils.getTransferTotal()`
- 条件付き依存: `if (this.download.hasPartialData)` → `this.showStatus()`
- 条件付き依存: `if (this.download.hasPartialData)` → `lazy.DownloadsCommon.strings.statusSeparatorBeforeNumber()`
- 条件付き依存: `if (this.download.hasPartialData)` → `this.showButton()`
- 条件付き依存: `if (!(this.download.hasPartialData))` → `this.showStatusWithDetails()`
- 条件付き依存: `if (!(this.download.hasPartialData))` → `this.showButton()`
- 条件付き依存: `if (!(this.download.canceled))` → `this.showStatus()`
- 条件付き依存: `if (!(this.download.canceled))` → `this.showButton()`
- 条件付き依存: `if (verdict)` → `this.element.setAttribute()`
- 条件付き依存: `if (!(verdict))` → `this.element.removeAttribute()`
- 条件付き依存: `if (!(!this.download.stopped))` → `this.element.classList.toggle()`
- 条件付き依存: `if (this.download.hasProgress)` → `this.showProgress()`
- 条件付き依存: `if (!(this.download.hasProgress))` → `this.showProgress()`
- 参照: `lazy.Downloads.Error.BLOCK_VERDICT_DOWNLOAD_SPAM`, `lazy.Downloads.Error.BLOCK_VERDICT_INSECURE`, `lazy.Downloads.Error.BLOCK_VERDICT_POTENTIALLY_UNWANTED`, `lazy.Downloads.Error.BLOCK_VERDICT_UNCOMMON`, `lazy.DownloadsCommon.getMimeInfo(this.download)?.type`, `lazy.DownloadsCommon.strings.sizeUnknown`, `lazy.DownloadsCommon.strings.stateBlockedParentalControls`, `lazy.DownloadsCommon.strings.stateCanceled`, `lazy.DownloadsCommon.strings.stateCompleted`, `lazy.DownloadsCommon.strings.stateFailed`, `lazy.DownloadsCommon.strings.statePaused`, `lazy.DownloadsCommon.strings.stateStarting`, `this.download`, `this.download.canceled`, `this.download.currentBytes`, `this.download.deleted`, `this.download.error`, `this.download.error.becauseBlockedByContentAnalysis`, `this.download.error.becauseBlockedByParentalControls`, `this.download.error.becauseBlockedByReputationCheck`, `this.download.error.localizedReason`, `this.download.error.reputationCheckVerdict`, `this.download.hasBlockedData`, `this.download.hasPartialData`, `this.download.hasProgress`, `this.download.launchWhenSucceeded`, `this.download.progress`, `this.download.speed`, `this.download.stopped`, `this.download.succeeded`, `this.download.target.exists`, `this.download.target.path`, `this.download.totalBytes`, `this.isPanel`, `this.lastEstimatedSecondsLeft`, `this.rawBlockedTitleAndDetails`

## getContentAnalysisErrorTitle()
- 位置: L906-929
- 役割: コンテンツ分析のキャンセル理由に応じて、エージェント名入りのエラー文言を選ぶ。
- 触るとき: コンテンツ分析で止まったときのエラー文言を変えるとき。
- 呼び出し先: `strings.contentAnalysisInvalidAgentSignatureError()`, `strings.contentAnalysisNoAgentError()`, `strings.contentAnalysisTimeoutError()`, `strings.contentAnalysisUnspecifiedError()`
- 参照: `Ci.nsIContentAnalysisResponse.eErrorOther`, `Ci.nsIContentAnalysisResponse.eInvalidAgentSignature`, `Ci.nsIContentAnalysisResponse.eNoAgent`, `Ci.nsIContentAnalysisResponse.eTimeout`, `lazy.contentAnalysisAgentName`, `strings.blockedByContentAnalysis`
- XPCOM: [`nsIContentAnalysisResponse`](../../../toolkit/components/contentanalysis/nsIContentAnalysis.idl.md)

## rawBlockedTitleAndDetails()
- 位置: L935-1004
- 役割: ブロックの判定 (不審、マルウェア、スパム、コンテンツ分析など) に応じて、タイトルと詳細の文言の組を返す。
- 触るとき: ブロックされたダウンロードの説明文を判定ごとに変えるとき、または未知の判定で例外が出る問題を調べるとき。
- 呼び出し先: `DownloadsViewUI.getStrippedUrl()`, `this.getContentAnalysisErrorTitle()`
- 参照: `lazy.Downloads.Error.BLOCK_VERDICT_DOWNLOAD_SPAM`, `lazy.Downloads.Error.BLOCK_VERDICT_INSECURE`, `lazy.Downloads.Error.BLOCK_VERDICT_MALWARE`, `lazy.Downloads.Error.BLOCK_VERDICT_POTENTIALLY_UNWANTED`, `lazy.Downloads.Error.BLOCK_VERDICT_UNCOMMON`, `lazy.DownloadsCommon.strings`, `s.blockedMalware`, `s.blockedPotentiallyInsecure`, `s.blockedPotentiallyUnwanted`, `s.blockedUncommon2`, `s.unblockContentAnalysis1`, `s.unblockContentAnalysis2`, `s.unblockContentAnalysisWarnTip`, `s.unblockInsecure2`, `s.unblockTip2`, `s.unblockTypeContentAnalysisWarn`, `s.unblockTypeMalware`, `s.unblockTypePotentiallyUnwanted2`, `s.unblockTypeUncommon2`, `s.warnedByContentAnalysis`, `this.download`, `this.download.blockedDownloadsCount`, `this.download.error`, `this.download.error.becauseBlockedByContentAnalysis`, `this.download.error.becauseBlockedByReputationCheck`, `this.download.error.contentAnalysisCancelError`, `this.download.error.reputationCheckVerdict`

## showDeletedOrMissing()
- 位置: L1006-1019
- 役割: 削除済み、ブロック後に削除、またはファイル不明のいずれかの文言を状態行に出し、ボタンを隠す。
- 触るとき: ファイルを移動・削除したときに出る表示を確認するとき。
- 呼び出し先: `this.element.removeAttribute()`, `this.hideButton()`, `this.showStatusWithDetails()`
- 参照: `lazy.DownloadsCommon.strings`, `this.download.deleted`, `this.download.error?.becauseBlocked`

## confirmUnblock()
- 位置: L1031-1050
- 役割: ブロック確認ダイアログを開き、選ばれた操作 (開く、ブロック解除、ブロック削除) を実行する。
- 触るとき: ブロック解除の確認後の処理を追うとき、または確認ダイアログの選択肢を変えるとき。
- 呼び出し先: `Promise.resolve()`, `lazy.DownloadsCommon.confirmUnblockDownload()`
- 条件付き依存: `if (action == "open")` → `this.unblockAndOpenDownload()`
- 条件付き依存: `if (action == "unblock")` → `this.download.unblock()`
- 条件付き依存: `if (action == "confirmBlock")` → `this.download.confirmBlock()`
- 参照: `console.error`, `this.download.error.becauseBlockedByReputationCheck`, `this.download.error.reputationCheckVerdict`

## unblockAndOpenDownload()
- 位置: L1057-1059
- 役割: ブロックを解除してから、既定のコマンドでファイルを開く。
- 触るとき: ブロック解除後に開かれないといった問題を調べるとき。
- 呼び出し先: `this.download.unblock()`, `this.download.unblock().then()`, `this.downloadsCmd_open()`

## unblockAndSave()
- 位置: L1061-1063
- 役割: ダウンロードのブロックを解除するだけで、ファイルは開かない。
- 触るとき: ブロック解除の結果を保存だけにしたいとき。
- 呼び出し先: `this.download.unblock()`

## currentDefaultCommandName()
- 位置: L1070-1088
- 役割: ダブルクリックなどの既定操作となるコマンド名を、状態ごとに返す。該当しなければ空文字を返す。
- 触るとき: ダブルクリックで何が起きるかを状態ごとに変えるとき。
- 呼び出し先: `lazy.DownloadsCommon.stateOfDownload()`
- 参照: `lazy.DownloadsCommon.DOWNLOAD_BLOCKED_CONTENT_ANALYSIS`, `lazy.DownloadsCommon.DOWNLOAD_BLOCKED_PARENTAL`, `lazy.DownloadsCommon.DOWNLOAD_CANCELED`, `lazy.DownloadsCommon.DOWNLOAD_DIRTY`, `lazy.DownloadsCommon.DOWNLOAD_FAILED`, `lazy.DownloadsCommon.DOWNLOAD_FINISHED`, `lazy.DownloadsCommon.DOWNLOAD_NOTSTARTED`, `lazy.DownloadsCommon.DOWNLOAD_PAUSED`, `this.download`

## isCommandEnabled()
- 位置: L1097-1144
- 役割: コマンドごとに、ダウンロードの状態 (再試行、部分データ、ブロック、ファイルの存在など) から有効かどうかを判定する。
- 触るとき: メニューやボタンのコマンドが灰色になる条件を変えるとき、または有効なのに実行できない問題を調べるとき。
- 呼び出し先: `DownloadsViewUI.isCommandName()`, `lazy.DownloadIntegration.shouldViewDownloadInternally()`, `lazy.DownloadsCommon.getMimeInfo()`
- 参照: `lazy.DownloadsCommon.getMimeInfo(this.download)?.type`, `lazy.safeBrowsingAllowOverride`, `referrer.asciiSpec`, `target.exists`, `target.partFileExists`, `this.download`, `this.download.canceled`, `this.download.deleted`, `this.download.error`, `this.download.hasBlockedData`, `this.download.hasPartialData`, `this.download.source.referrerInfo?.originalReferrer`, `this.download.stopped`, `this.download.target.exists`

## doCommand()
- 位置: L1146-1153
- 役割: コマンド名の「:修飾子」を分けて、自身の同名メソッドを呼ぶ。
- 触るとき: コマンドに修飾子 (例: downloadsCmd_open:window) を渡す経路を追うとき。
- 呼び出し先: `DownloadsViewUI.isCommandName()`, `aCommand.split()`
- 条件付き依存: `if (DownloadsViewUI.isCommandName(command))` → `this[command]()`

## onButton()
- 位置: L1155-1157
- 役割: ボタンに割り当てられたコマンドを実行する。
- 触るとき: ボタン押下で想定外のコマンドが動くときに見る。
- 呼び出し先: `this.doCommand()`
- 参照: `this.buttonCommandName`

## downloadsCmd_cancel()
- 位置: L1159-1166
- 役割: ダウンロードを中止し、部分データを削除してターゲットの存在情報を更新する。
- 触るとき: キャンセル後にファイルが残る、または一覧の状態が更新されない問題を調べるとき。
- 呼び出し先: `this.download .removePartialData()`, `this.download .removePartialData() .catch()`, `this.download .removePartialData() .catch(console.error) .finally()`, `this.download.cancel()`, `this.download.cancel().catch()`, `this.download.target.refresh()`
- 参照: `console.error`

## downloadsCmd_confirmBlock()
- 位置: L1168-1170
- 役割: ブロックされたダウンロードの確認 (データの削除) を実行する。
- 触るとき: ブロックされたファイルを削除する操作を変えるとき。
- 呼び出し先: `this.download.confirmBlock()`, `this.download.confirmBlock().catch()`
- 参照: `console.error`

## downloadsCmd_open()
- 位置: L1172-1176
- 役割: ダウンロード済みファイルを開く。既定の開き先はタブで、修飾子で窓やタブの位置を指定できる。
- 触るとき: ダウンロードしたファイルを開く先 (タブかウィンドウか) を変えるとき。
- 呼び出し先: `lazy.DownloadsCommon.openDownload()`
- 参照: `this.download`

## downloadsCmd_openReferrer()
- 位置: L1178-1182
- 役割: ダウンロード元のページ (リファラー) を開く。
- 触るとき: 「ダウンロード元のページを開く」が正しい URL を開かないときに見る。
- 呼び出し先: `this.element.documentGlobal.openURL()`
- 参照: `this.download.source.referrerInfo.originalReferrer`

## downloadsCmd_pauseResume()
- 位置: L1184-1190
- 役割: 停止中なら再開し、進行中ならキャンセル (一時停止) する。
- 触るとき: 一時停止と再開の切り替えが効かない問題を調べるとき。
- 条件付き依存: `if (this.download.stopped)` → `this.download.start()`
- 条件付き依存: `if (!(this.download.stopped))` → `this.download.cancel()`
- 参照: `this.download.stopped`

## downloadsCmd_show()
- 位置: L1192-1195
- 役割: ダウンロードしたファイルを、OS のファイルマネージャーで表示する。
- 触るとき: 「フォルダーで表示」の挙動を変えるとき。
- 呼び出し先: `lazy.DownloadsCommon.showDownloadedFile()`
- 参照: `lazy.FileUtils.File`, `this.download.target.path`

## downloadsCmd_retry()
- 位置: L1197-1212
- 役割: ダウンロードを再開する。開始 API がなければ、元の URL から DownloadURL で新規にダウンロードする。
- 触るとき: 失敗したダウンロードの再試行で別ファイル名になる、または再試行できない問題を調べるとき。
- 呼び出し先: `PathUtils.filename()`, `window.DownloadURL()`
- 条件付き依存: `if (this.download.start)` → `this.download.start().catch()`
- 条件付き依存: `if (this.download.start)` → `this.download.start()`
- 参照: `this.browserWindow`, `this.download.source.url`, `this.download.start`, `this.download.target.path`, `this.element.documentGlobal`, `window.document`

## downloadsCmd_delete()
- 位置: L1214-1219
- 役割: cmd_delete を呼ぶだけの別名。他のコントローラーと衝突しないように用意されている。
- 触るとき: 削除コマンドが他のコントローラーに横取りされる問題を調べるとき。
- 呼び出し先: `this.cmd_delete()`

## cmd_delete()
- 位置: L1221-1223
- 役割: ダウンロードを一覧と履歴から削除する。
- 触るとき: 一覧から項目を消す操作の範囲を変えるとき。
- 呼び出し先: `lazy.DownloadsCommon.deleteDownload()`, `lazy.DownloadsCommon.deleteDownload(this.download).catch()`
- 参照: `console.error`, `this.download`

## downloadsCmd_deleteFile()
- 位置: async L1225-1231
- 役割: ファイルとその部分データを削除し、設定 clearHistoryOnDelete に応じて履歴からも消す。
- 触るとき: 「ファイルを削除」の範囲を変えるとき、または削除後に履歴が残る問題を調べるとき。
- 呼び出し先: `lazy.DownloadsCommon.deleteDownloadFiles()`
- 参照: `DownloadsViewUI.clearHistoryOnDelete`, `this.download`

## downloadsCmd_openInSystemViewer()
- 位置: L1233-1239
- 役割: 今回だけ既定の設定を無視して、システムの既定アプリでファイルを開く。
- 触るとき: 「システムビューアーで開く」の動作を変えるとき。
- 呼び出し先: `lazy.DownloadsCommon.openDownload()`, `lazy.DownloadsCommon.openDownload(this.download, { useSystemDefault: true, }).catch()`
- 参照: `console.error`, `this.download`

## downloadsCmd_alwaysOpenInSystemViewer()
- 位置: L1241-1270
- 役割: この MIME 種類の preferredAction をシステム既定と内部表示で切り替え、保存してから開く。
- 触るとき: 「今後は常にシステムビューアーで開く」の設定が保存されない問題を調べるとき。
- 呼び出し先: `lazy.DownloadsCommon.getMimeInfo()`, `lazy.DownloadsCommon.openDownload()`, `lazy.DownloadsCommon.openDownload(this.download).catch()`, `lazy.handlerSvc.store()`
- 条件付き依存: `if (mimeInfo.preferredAction !== mimeInfo.useSystemDefault)` → `lazy.DownloadsCommon.log()`
- 条件付き依存: `if (!(mimeInfo.preferredAction !== mimeInfo.useSystemDefault))` → `lazy.DownloadsCommon.log()`
- 参照: `console.error`, `mimeInfo.alwaysAskBeforeHandling`, `mimeInfo.handleInternally`, `mimeInfo.preferredAction`, `mimeInfo.type`, `mimeInfo.useSystemDefault`, `this.download`

## downloadsCmd_alwaysOpenSimilarFiles()
- 位置: L1272-1291
- 役割: この MIME 種類をシステム既定で開くよう保存し、すぐ開く。すでに設定済みなら保存先を saveToDisk に戻す。
- 触るとき: 「同種のファイルは常に開く」の設定を変えるとき、または解除しても設定が残るときに見る。
- 呼び出し先: `lazy.DownloadsCommon.getMimeInfo()`
- 条件付き依存: `if (mimeInfo.preferredAction !== mimeInfo.useSystemDefault)` → `lazy.handlerSvc.store()`
- 条件付き依存: `if (mimeInfo.preferredAction !== mimeInfo.useSystemDefault)` → `lazy.DownloadsCommon.openDownload(this.download).catch()`
- 条件付き依存: `if (mimeInfo.preferredAction !== mimeInfo.useSystemDefault)` → `lazy.DownloadsCommon.openDownload()`
- 条件付き依存: `if (!(mimeInfo.preferredAction !== mimeInfo.useSystemDefault))` → `lazy.handlerSvc.store()`
- 参照: `console.error`, `mimeInfo.preferredAction`, `mimeInfo.saveToDisk`, `mimeInfo.useSystemDefault`, `this.download`
