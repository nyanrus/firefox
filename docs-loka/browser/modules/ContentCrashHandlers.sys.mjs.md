# browser/modules/ContentCrashHandlers.sys.mjs

source: browser/modules/ContentCrashHandlers.sys.mjs
source-hash: 0c31dbcbc9c97e3e93e5efdd43cf9e904745efdc
lines: 1398

## <module>
- 役割: タブのクラッシュ時の復旧ページ、サブフレームのクラッシュ通知、未送信クラッシュレポートの通知とクリーンアップを担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.prefs.getBranch()`, `console.createInstance()`, `lazy.cleanerPrefs.getStringPref()`

## BrowserWeakMap.get()
- 位置: L60-65
- 役割: permanentKey があればそれを鍵に、なければ browser 要素そのものを鍵にして値を引く。
- 触るとき: browser 単位の crash 情報を引く鍵が切り替わる理由を追うときに見る。
- 呼び出し先: `super.get()`
- 条件付き依存: `if (browser.permanentKey)` → `super.get()`
- 参照: `browser.permanentKey`

## BrowserWeakMap.set()
- 位置: L67-72
- 役割: get と同じ鍵の規則で値を登録する。
- 触るとき: browser に紐づく crash 情報の登録先が正しいか確かめるときに見る。
- 呼び出し先: `super.set()`
- 条件付き依存: `if (browser.permanentKey)` → `super.set()`
- 参照: `browser.permanentKey`

## BrowserWeakMap.delete()
- 位置: L74-79
- 役割: get と同じ鍵の規則で登録を削除する。
- 触るとき: crash 後に browser の記録が消えないときに見る。
- 呼び出し先: `super.delete()`
- 条件付き依存: `if (browser.permanentKey)` → `super.delete()`
- 参照: `browser.permanentKey`

## prefs()
- 位置: L94-99
- 役割: browser.tabs.crashReporting. のブランチを初回参照時に取得し、以後は再利用する。
- 触るとき: タブのクラッシュ報告の設定 pref を読む箇所を探すときに見る。
- 呼び出し先: `Services.prefs.getBranch()`
- 参照: `this.prefs`
- XPCOM: `Services.prefs`

## init()
- 位置: L101-109
- 役割: ipc:content-shutdown と oop-frameloader-crashed の監視を一度だけ登録する。
- 触るとき: コンテンツプロセスのクラッシュ通知が届かないとき、または起動時の監視登録を変えるときに見る。
- 呼び出し先: `Services.obs.addObserver()`
- 参照: `this.initialized`
- XPCOM: `Services.obs`

## observe()
- 位置: L111-195
- 役割: 異常終了した content プロセスの dumpID を childMap に保存し、subframe 通知の表示、クラッシュページ行きのキュー処理を行う。MOZ_CRASHREPORTER_SHUTDOWN があれば強制終了する。oop-frameloader-crashed では browser と childID を対応付ける。
- 触るとき: クラッシュ後にタブがクラッシュページに切り替わらない、または dumpID が付かないときに見る。
- 呼び出し先: `Services.env.exists()`, `aSubject.QueryInterface()`, `aSubject.get()`, `this.browserMap.set()`, `this.flushCrashedBrowserQueue()`, `this.getAndRemoveSubframeCrash()`
- 条件付き依存: `if (!dumpID)` → `Glean.browserContentCrash.dumpUnavailable.add()`
- 条件付き依存: `if (AppConstants.MOZ_CRASHREPORTER)` → `this.childMap.set()`
- 条件付き依存: `if (subframeCrashItem)` → `ChromeUtils.nondeterministicGetWeakMapKeys()`
- 条件付き依存: `if (subframeCrashItem)` → `subframeCrashItem.get()`
- 条件付き依存: `if (browser.isConnected && !browser.documentGlobal.closed)` → `this.showSubFrameNotification()`
- 条件付き依存: `if (!this.flushCrashedBrowserQueue(childID))` → `this.unseenCrashedChildIDs.push()`
- 条件付き依存: `if ( this.unseenCrashedChildIDs.length > MAX_UNSEEN_CRASHED_CHILD_IDS )` → `this.unseenCrashedChildIDs.shift()`
- 条件付き依存: `if (shutdown)` → `dump()`
- 条件付き依存: `if (shutdown)` → `Services.startup.quit()`
- 参照: `AppConstants.MOZ_CRASHREPORTER`, `Ci.nsIAppStartup.eForceQuit`, `Ci.nsIPropertyBag2`, `aSubject.childID`, `aSubject.ownerElement`, `browser.documentGlobal.closed`, `browser.isConnected`, `this.unseenCrashedChildIDs.length`
- XPCOM: [`nsIAppStartup`](../../toolkit/components/startup/public/nsIAppStartup.idl.md) / [`nsIPropertyBag2`](../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md) / `Services.env` / `Services.startup`

## flushCrashedBrowserQueue()
- 位置: L209-234
- 役割: childID のキューにある browser を、再起動が必要ならリスタート要求ページへ、そうでなければクラッシュページへ送る。1件でも送れば真を返す。
- 触るとき: プロセス終了後にクラッシュページが出る経路を追うとき、または再起動要求時の表示先を変えるときに見る。
- 呼び出し先: `this.crashedBrowserQueues.delete()`, `this.crashedBrowserQueues.get()`, `weakBrowser.get()`
- 条件付き依存: `if (browser)` → `this.restartRequiredBrowsers.has()`
- 条件付き依存: `if ( this.restartRequiredBrowsers.has(browser) || this.testBuildIDMismatch )` → `this.sendToRestartRequiredPage()`
- 条件付き依存: `if (!( this.restartRequiredBrowsers.has(browser) || this.testBuildIDMismatch ))` → `this.sendToTabCrashedPage()`
- 参照: `this.testBuildIDMismatch`

## onSelectedBrowserCrash()
- 位置: L246-282
- 役割: 選択中のリモート browser を childID のキューに入れ、再起動が必要なら記録する。childID が 0 なら dumpID を待たずにキューを即座に処理する。
- 触るとき: 選択中のタブがクラッシュしてからクラッシュページが出るまでの流れを調べるときに見る。
- 呼び出し先: `Cu.getWeakReference()`, `browserQueue.push()`, `this.crashedBrowserQueues.get()`
- 条件付き依存: `if (!browser.isRemoteBrowser)` → `console.error()`
- 条件付き依存: `if (!browser.frameLoader)` → `console.error()`
- 条件付き依存: `if (!browserQueue)` → `this.crashedBrowserQueues.set()`
- 条件付き依存: `if (restartRequired)` → `this.restartRequiredBrowsers.add()`
- 条件付き依存: `if (childID == 0)` → `this.flushCrashedBrowserQueue()`
- 参照: `browser.frameLoader`, `browser.frameLoader.childID`, `browser.isRemoteBrowser`

## onBackgroundBrowserCrash()
- 位置: L295-308
- 役割: 背景タブの browser を非リモートに切り替え、SessionStore の reviveCrashedTab で復旧させる。
- 触るとき: 背景のタブがクラッシュした後、選択された時点で復元される流れを変えるときに見る。
- 呼び出し先: `browser.getTabBrowser()`, `gBrowser.getTabForBrowser()`, `gBrowser.updateBrowserRemoteness()`, `lazy.SessionStore.reviveCrashedTab()`
- 条件付き依存: `if (restartRequired)` → `this.restartRequiredBrowsers.add()`
- 参照: `lazy.E10SUtils.NOT_REMOTE`

## onSubFrameCrash()
- 位置: async L319-350
- 役割: dumpID が既にあれば subframe 通知を出し、なければ保留リストに入れて ipc:content-shutdown で dumpID が届くのを待つ。保留が上限を超えると最も古い childID を捨てる。
- 触るとき: iframe のクラッシュで通知が出ない、または遅れるときに見る。
- 呼び出し先: `this.childMap.get()`
- 条件付き依存: `if (dumpID)` → `this.showSubFrameNotification()`
- 条件付き依存: `if (!(dumpID))` → `this.pendingSubFrameCrashes.get()`
- 条件付き依存: `if (!item)` → `this.pendingSubFrameCrashes.set()`
- 条件付き依存: `if ( this.pendingSubFrameCrashesIDs.length >= MAX_UNSEEN_CRASHED_SUBFRAME_IDS )` → `this.pendingSubFrameCrashesIDs.shift()`
- 条件付き依存: `if ( this.pendingSubFrameCrashesIDs.length >= MAX_UNSEEN_CRASHED_SUBFRAME_IDS )` → `this.pendingSubFrameCrashes.delete()`
- 条件付き依存: `if (!item)` → `this.pendingSubFrameCrashesIDs.push()`
- 条件付き依存: `if (!(dumpID))` → `item.set()`
- 参照: `AppConstants.MOZ_CRASHREPORTER`, `this.pendingSubFrameCrashesIDs.length`

## getAndRemoveSubframeCrash()
- 位置: L361-372
- 役割: childID の保留中 subframe クラッシュ情報を取り出し、保留リストから外す。
- 触るとき: 保留中の subframe 通知が残り続ける、または二重に出るときに見る。
- 呼び出し先: `this.pendingSubFrameCrashes.get()`
- 条件付き依存: `if (item)` → `this.pendingSubFrameCrashes.delete()`
- 条件付き依存: `if (item)` → `this.pendingSubFrameCrashesIDs.indexOf()`
- 条件付き依存: `if (idx >= 0)` → `this.pendingSubFrameCrashesIDs.splice()`

## showSubFrameNotification()
- 位置: async L385-470
- 役割: browser の通知箱に subframe-crashed の通知を出す。同じ通知が既にあれば何もしない。送信ボタンと詳細リンクを付ける。
- 触るとき: subframe クラッシュ通知の文言やボタンを変えるとき、または通知が出ない理由を調べるときに見る。
- 呼び出し先: `browser.getTabBrowser()`, `gBrowser.documentGlobal.MozXULElement.insertFTLIfNeeded()`, `gBrowser.getNotificationBox()`, `notificationBox.appendNotification()`, `notificationBox.getNotificationWithValue()`, `this.notificationsMap.get()`
- 条件付き依存: `if (existingItem)` → `existingItem.push()`
- 条件付き依存: `if (!(existingItem))` → `this.notificationsMap.set()`
- 参照: `notificationBox.PRIORITY_INFO_MEDIUM`

## closeAllNotifications()
- 位置: L396-405
- 役割: 同じ childID に紐づく他のタブの通知をすべて閉じる。
- 触るとき: 1つのクラッシュの通知が別タブに残るときに見る。
- 呼び出し先: `this.notificationsMap.get()`
- 条件付き依存: `if (existingItem)` → `existingItem.slice()`
- 条件付き依存: `if (existingItem)` → `notif.close()`

## callback()
- 位置: async L420-428
- 役割: subframe 通知の送信ボタン。dumpID があれば CRASH_TAB 経由で送信し、関連する通知を閉じる。
- 触るとき: subframe 通知の送信ボタンの挙動を変えるとき。
- 呼び出し先: `closeAllNotifications()`
- 条件付き依存: `if (dumpID)` → `UnsubmittedCrashHandler.submitReports()`
- 参照: `lazy.CrashSubmit.SUBMITTED_FROM_CRASH_TAB`

## eventCallback()
- 位置: L438-459
- 役割: 切断時は通知の管理リストから外す。dismissed 時は dumpID を無視扱いにして childMap から消し、関連する通知を閉じる。
- 触るとき: 通知を閉じた後にレポートが送られる、または送られない理由を追うとき。
- 条件付き依存: `if (eventName == "disconnected")` → `this.notificationsMap.get()`
- 条件付き依存: `if (existingItem)` → `existingItem.indexOf()`
- 条件付き依存: `if (idx >= 0)` → `existingItem.splice()`
- 条件付き依存: `if (!existingItem.length)` → `this.notificationsMap.delete()`
- 条件付き依存: `if (dumpID)` → `lazy.CrashSubmit.ignore()`
- 条件付き依存: `if (dumpID)` → `this.childMap.delete()`
- 条件付き依存: `if (eventName == "dismissed")` → `closeAllNotifications()`
- 参照: `existingItem.length`

## willShowCrashedTab()
- 位置: L487-519
- 役割: SessionStore が復元対象のタブを選んだとき、未表示のクラッシュならクラッシュページを出す(自動送信が有効なら送信のみ)。childID が 0 なら再起動要否に応じた復旧ページを出す。表示したら真を返す。
- 触るとき: セッション復元で選ばれたタブがクラッシュページになるかどうかの条件を変えるときに見る。
- 呼び出し先: `this.browserMap.get()`, `this.unseenCrashedChildIDs.includes()`
- 条件付き依存: `if (UnsubmittedCrashHandler.autoSubmit)` → `this.childMap.get()`
- 条件付き依存: `if (dumpID)` → `UnsubmittedCrashHandler.submitReports()`
- 条件付き依存: `if (!(UnsubmittedCrashHandler.autoSubmit))` → `this.sendToTabCrashedPage()`
- 条件付き依存: `if (childID === 0)` → `this.restartRequiredBrowsers.has()`
- 条件付き依存: `if (this.restartRequiredBrowsers.has(browser))` → `this.sendToRestartRequiredPage()`
- 条件付き依存: `if (!(this.restartRequiredBrowsers.has(browser)))` → `this.sendToTabCrashedPage()`
- 参照: `UnsubmittedCrashHandler.autoSubmit`, `lazy.CrashSubmit.SUBMITTED_FROM_AUTO`

## sendToRestartRequiredPage()
- 位置: L521-532
- 役割: browser を非リモートに切り替え、ビルド ID 不一致のエラーを表示し、tab に crashed 属性を付ける。
- 触るとき: ブラウザー更新後にクラッシュした場合のリスタート要求画面を変えるときに見る。
- 呼び出し先: `browser.docShell.displayLoadError()`, `browser.getTabBrowser()`, `gBrowser.getTabForBrowser()`, `gBrowser.updateBrowserRemoteness()`, `tab.setAttribute()`
- 参照: `Cr.NS_ERROR_BUILDID_MISMATCH`, `browser.currentURI`, `lazy.E10SUtils.NOT_REMOTE`

## sendToTabCrashedPage()
- 位置: L542-556
- 役割: browser を非リモートに切り替え、NS_ERROR_CONTENT_CRASHED のエラーページを表示し、tab に crashed 属性を付ける。
- 触るとき: クラッシュページの表示方法やタイトルの扱いを変えるときに見る。
- 呼び出し先: `browser.docShell.displayLoadError()`, `browser.getTabBrowser()`, `browser.removeAttribute()`, `browser.setAttribute()`, `gBrowser.getTabForBrowser()`, `gBrowser.updateBrowserRemoteness()`, `tab.setAttribute()`
- 参照: `Cr.NS_ERROR_CONTENT_CRASHED`, `browser.contentTitle`, `browser.currentURI`, `lazy.E10SUtils.NOT_REMOTE`

## maybeSendCrashReport()
- 位置: L579-641
- 役割: about:tabcrashed からの送信要求を処理する。自動送信の選択を記録し、送信するなら空でないコメントと URL を extra に付けて CrashSubmit で送る。URL は includeURL が偽なら空にする。送らないなら notSubmitted を記録して sendReport を偽にする。
- 触るとき: クラッシュ報告ページの送信チェックや付加情報の扱いを変えるとき。
- 呼び出し先: `extraExtraKeyVals[key].trim()`, `lazy.CrashSubmit.submit()`, `this.browserMap.get()`, `this.childMap.get()`, `this.childMap.set()`, `this.prefs.setBoolPref()`, `this.removeSubmitCheckboxesForSameCrash()`
- 条件付き依存: `if (!message.data.sendReport)` → `Glean.browserContentCrash.notSubmitted.add()`
- 条件付き依存: `if (!message.data.sendReport)` → `this.prefs.setBoolPref()`
- 参照: `AppConstants.MOZ_CRASHREPORTER`, `UnsubmittedCrashHandler.autoSubmit`, `console.error`, `extraExtraKeyVals.URL`, `lazy.CrashSubmit.SUBMITTED_FROM_CRASH_TAB`, `message.data`, `message.data.autoSubmit`, `message.data.hasReport`, `message.data.sendReport`

## removeSubmitCheckboxesForSameCrash()
- 位置: L643-665
- 役割: 同じ childID の about:tabcrashed を開いている別ウィンドウのページに CrashReportSent を送り、送信チェックを消す。
- 触るとき: 送信後も別ウィンドウのクラッシュページが送信可能なまま残るときに見る。
- 呼び出し先: `Services.wm.getEnumerator()`, `doc.documentURI.startsWith()`, `this.browserMap.get()`
- 条件付き依存: `if (this.browserMap.get(browser) == childID)` → `this.browserMap.delete()`
- 条件付き依存: `if (this.browserMap.get(browser) == childID)` → `browser.sendMessageToActor()`
- 参照: `browser.contentDocument`, `browser.isRemoteBrowser`, `window.gBrowser.browsers`, `window.gMultiProcessBrowser`
- XPCOM: `Services.wm`

## onAboutTabCrashedLoad()
- 位置: L675-708
- 役割: クラッシュ数を増やし、ズームを 1 に戻し、未表示リストから外す。dumpID があれば送信設定と自動送信の要否を返し、なければ hasReport を偽で返す。
- 触るとき: クラッシュページに出す送信欄の初期値を変えるとき、または報告がないのに送信欄が出るときに見る。
- 呼び出し先: `this.browserMap.get()`, `this.getDumpID()`, `this.prefs.getBoolPref()`, `this.unseenCrashedChildIDs.indexOf()`, `window.ZoomManager.setZoomForBrowser()`
- 条件付き依存: `if (index != -1)` → `this.unseenCrashedChildIDs.splice()`
- 参照: `UnsubmittedCrashHandler.autoSubmit`, `browser.documentGlobal`, `this._crashedTabCount`

## onAboutTabCrashedUnload()
- 位置: L710-724
- 役割: クラッシュ数を減らし、0 になったときに childID があれば notSubmitted を記録する。0 未満になる場合はエラーを出して何もしない。
- 触るとき: 未送信件数の Glean 記録がずれるときに見る。
- 呼び出し先: `this.browserMap.get()`
- 条件付き依存: `if (!this._crashedTabCount)` → `console.error()`
- 条件付き依存: `if (this._crashedTabCount == 0 && childID)` → `Glean.browserContentCrash.notSubmitted.add()`
- 参照: `this._crashedTabCount`

## getDumpID()
- 位置: L734-740
- 役割: crash reporter が有効なら browser の childID から dumpID を引き、無効ならこのビルドでは null を返す。
- 触るとき: クラッシュ報告が付かないタブの原因を調べるときに見る。
- 呼び出し先: `this.browserMap.get()`, `this.childMap.get()`
- 参照: `AppConstants.MOZ_CRASHREPORTER`

## queuedCrashedBrowsers()
- 位置: L753-755
- 役割: dumpID 待ちのクラッシュ browser キューの数を返すテスト用のゲッター。
- 触るとき: クラッシュ後に待機キューが残っていないかをテストで確かめるときに見る。
- 参照: `this.crashedBrowserQueues.size`

## prefs()
- 位置: L766-771
- 役割: browser.crashReports.unsubmittedCheck. のブランチを初回参照時に取得し、以後は再利用する。
- 触るとき: 未送信レポート通知の設定 pref を探すときに見る。
- 呼び出し先: `Services.prefs.getBranch()`
- 参照: `this.prefs`
- XPCOM: `Services.prefs`

## enabled()
- 位置: L773-775
- 役割: unsubmittedCheck.enabled の値を返す。
- 触るとき: 未送信レポート通知が有効かを判定する箇所を追うとき。
- 呼び出し先: `this.prefs.getBoolPref()`

## init()
- 位置: L792-831
- 役割: ログを作り、Remote Settings による送信要求の監視を開始する。有効で抑止期間中でなければ profile-before-change を監視する。抑止期間が過ぎていれば suppressUntilDate を消す。
- 触るとき: 起動時に未送信通知が出ない理由(無効化や抑止期間)を調べるときに見る。
- 呼び出し先: `console.createInstance()`, `lazy.RemoteSettingsCrashPull.start()`, `this.prefs.getStringPref()`, `this.showRequestedSubmissionsNotification.bind()`
- 条件付き依存: `if (this.enabled)` → `this.prefs.prefHasUserValue()`
- 条件付き依存: `if (this.prefs.prefHasUserValue("suppressUntilDate"))` → `this.prefs.getCharPref()`
- 条件付き依存: `if (this.prefs.prefHasUserValue("suppressUntilDate"))` → `this.dateString()`
- 条件付き依存: `if (this.prefs.getCharPref("suppressUntilDate") > this.dateString())` → `this.log.debug()`
- 条件付き依存: `if (this.prefs.prefHasUserValue("suppressUntilDate"))` → `this.prefs.clearUserPref()`
- 条件付き依存: `if (this.enabled)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!(this.enabled))` → `this.log.debug()`
- 参照: `this.enabled`, `this.initialized`, `this.log`, `this.suppressed`
- XPCOM: `Services.obs`

## uninit()
- 位置: L833-865
- 役割: タイマーと Remote Settings の監視を止める。通知を表示中に終了したら shutdownWhileShowing を記録し、profile-before-change の監視を外す。
- 触るとき: 終了時の通知の状態の記録方法を変えるときに見る。
- 呼び出し先: `Services.obs.removeObserver()`, `lazy.RemoteSettingsCrashPull.stop()`
- 条件付き依存: `if (this._checkTimeout)` → `lazy.clearTimeout()`
- 条件付き依存: `if (this.showingNotification)` → `this.prefs.setBoolPref()`
- 参照: `this._checkTimeout`, `this.enabled`, `this.initialized`, `this.log`, `this.showingNotification`, `this.suppressed`
- XPCOM: `Services.obs`

## observe()
- 位置: L867-874
- 役割: profile-before-change を受けて uninit を呼ぶ。
- 触るとき: 終了時の後始末がどこから呼ばれるかを追うときに見る。
- 呼び出し先: `this.uninit()`

## scheduleCheckForUnsubmittedCrashReports()
- 位置: L876-882
- 役割: 10 分のタイマー後にアイドル時の確認処理を予約する。
- 触るとき: 未送信レポートの確認を起動直後から遅らせたいとき、または確認の間隔を変えるときに見る。
- 呼び出し先: `Services.tm.idleDispatchToMainThread()`, `lazy.setTimeout()`, `this.checkForUnsubmittedCrashReports()`
- 参照: `this._checkTimeout`
- XPCOM: `Services.tm`

## checkForUnsubmittedCrashReports()
- 位置: async L895-924
- 役割: 直近 28 日の未送信レポートを集め、自動送信が有効なら送信し、そうでなければ表示条件を満たすとき通知を出す。
- 触るとき: 未送信レポートが通知されない、または古い報告が対象になるときに見る。
- 呼び出し先: `dateLimit.getDate()`, `dateLimit.setDate()`, `lazy.CrashSubmit.pendingIDs()`, `this.log.debug()`, `this.log.error()`
- 条件付き依存: `if (reportIDs.length)` → `this.log.debug()`
- 条件付き依存: `if (reportIDs.length)` → `Glean.crashSubmission.pending.add()`
- 条件付き依存: `if (this.autoSubmit)` → `this.log.debug()`
- 条件付き依存: `if (this.autoSubmit)` → `this.submitReports()`
- 条件付き依存: `if (!(this.autoSubmit))` → `this.shouldShowPendingSubmissionsNotification()`
- 条件付き依存: `if (this.shouldShowPendingSubmissionsNotification())` → `this.showPendingSubmissionsNotification()`
- 参照: `lazy.CrashSubmit.SUBMITTED_FROM_AUTO`, `reportIDs.length`, `this.autoSubmit`, `this.enabled`, `this.suppressed`

## shouldShowPendingSubmissionsNotification()
- 位置: L936-978
- 役割: 送信要求の通知が出ていれば出さない。前回表示したまま終了した翌日の表示では chancesUntilSuppress を 1 減らし、尽きたら 30 日間の抑止期限を設定して出さない。
- 触るとき: 未送信通知が出ない、または出続ける理由を調べるとき、または抑止の回数や期間を変えるときに見る。
- 呼び出し先: `this.dateString()`, `this.prefs.clearUserPref()`, `this.prefs.getBoolPref()`, `this.prefs.getCharPref()`, `this.prefs.prefHasUserValue()`
- 条件付き依存: `if (this.dateString() > lastShownDate && shutdownWhileShowing)` → `this.prefs.getIntPref()`
- 条件付き依存: `if (--chances < 0)` → `this.prefs.clearUserPref()`
- 条件付き依存: `if (--chances < 0)` → `this.dateString()`
- 条件付き依存: `if (--chances < 0)` → `Date.now()`
- 条件付き依存: `if (--chances < 0)` → `this.prefs.setCharPref()`
- 条件付き依存: `if (this.dateString() > lastShownDate && shutdownWhileShowing)` → `this.prefs.setIntPref()`
- 参照: `this._requestedSubmission.notification`

## showPendingSubmissionsNotification()
- 位置: async L988-1009
- 役割: pending-crash-reports の通知を出し、表示できたら表示中フラグを立てて lastShownDate を今日に更新する。
- 触るとき: 通知の表示成功時に記録される値を変えるときに見る。
- 呼び出し先: `this.log.debug()`, `this.show()`
- 条件付き依存: `if (notification)` → `this.prefs.setCharPref()`
- 条件付き依存: `if (notification)` → `this.dateString()`
- 参照: `reportIDs.length`, `this.showingNotification`

## onAction()
- 位置: L998-1000
- 役割: 通知の操作(閉じる含む)で表示中フラグを下ろす。
- 触るとき: 通知を閉じた後に再表示の判定がずれるときに見る。
- 参照: `this.showingNotification`

## removeExistingNotification()
- 位置: L1011-1024
- 役割: 既存の送信要求通知を最上位のブラウザーウィンドウから外す。ウィンドウがなければ false を返す。
- 触るとき: 新しい送信要求通知を出す前に古い通知が残るときに見る。
- 条件付き依存: `if (aNotification)` → `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (aNotification)` → `chromeWin.gNotificationBox.removeNotification()`

## showRequestedSubmissionsNotification()
- 位置: async L1039-1076
- 役割: Remote Settings からの送信要求を受けて、古い通知を外し、dontShowBefore を過ぎていれば要求用の通知を出す。
- 触るとき: 開発者からの送信要求の表示条件や待ち時間を変えるときに見る。
- 呼び出し先: `Date.now()`, `Math.trunc()`, `Services.prefs.getIntPref()`, `this._requestedSubmission.reportIDs.push()`, `this.log.debug()`, `this.removeExistingNotification()`, `this.show()`
- 参照: `newReportIDs.length`, `this._requestedSubmission.notification`, `this._requestedSubmission.reportIDs`
- XPCOM: `Services.prefs`

## onAction()
- 位置: L1064-1071
- 役割: 要求通知の操作時に状態を消し、dontShowBefore を 7 日後に設定する。
- 触るとき: 要求通知の操作後に再表示されるまでの期間を確かめるときに見る。
- 呼び出し先: `Services.prefs.setIntPref()`
- 参照: `this._requestedSubmission.notification`, `this._requestedSubmission.reportIDs`
- XPCOM: `Services.prefs`

## dateString()
- 位置: L1087-1092
- 役割: 日付を YYYYMMDD の文字列にする。引数がなければ今日の日付を使う。
- 触るとき: 抑止期限や最終表示日の pref の書式を変えるときに見る。
- 呼び出し先: `String()`, `String(someDate.getDate()).padStart()`, `String(someDate.getFullYear()).padStart()`, `String(someDate.getMonth() + 1).padStart()`, `someDate.getDate()`, `someDate.getFullYear()`, `someDate.getMonth()`

## show()
- 位置: L1128-1235
- 役割: 最上位ウィンドウに同じ ID の通知がなければ、送信・常に送信・全件表示のボタン付きで未送信通知を出す。要求通知の場合は別のボタン構成にする。閉じられたら報告を無視扱いにする。
- 触るとき: 未送信報告の通知の文言・ボタン・優先度を変えるとき、またはボタンが出ない理由を調べるときに見る。
- 呼び出し先: `buttons.push()`, `chromeWin.MozXULElement.insertFTLIfNeeded()`, `chromeWin.gNotificationBox.appendNotification()`, `chromeWin.gNotificationBox.getNotificationWithValue()`, `lazy.BrowserWindowTracker.getTopWindow()`
- 条件付き依存: `if (requestedByDevs)` → `buttons.push()`
- 条件付き依存: `if (!requestedByDevs)` → `buttons.push()`
- 条件付き依存: `if (!(!requestedByDevs))` → `buttons.push()`
- 参照: `chromeWin.gNotificationBox.PRIORITY_INFO_HIGH`, `reportIDs.length`

## callback()
- 位置: L1149-1158
- 役割: 送信ボタン。要求通知なら throttle を無効にして送信し、onAction を呼ぶ。
- 触るとき: 通知の送信ボタンの挙動を変えるときに見る。
- 呼び出し先: `this.submitReports()`
- 条件付き依存: `if (onAction)` → `onAction()`
- 参照: `lazy.CrashSubmit.SUBMITTED_FROM_INFOBAR`

## callback()
- 位置: L1162-1168
- 役割: 常に送信ボタン。autoSubmit を真にしてから送信し、onAction を呼ぶ。
- 触るとき: 自動送信の設定が切り替わる経路を調べるときに見る。
- 呼び出し先: `this.submitReports()`
- 条件付き依存: `if (onAction)` → `onAction()`
- 参照: `lazy.CrashSubmit.SUBMITTED_FROM_INFOBAR`, `this.autoSubmit`

## callback()
- 位置: L1172-1175
- 役割: 全件表示ボタン。about:crashes を新しいタブで開く。
- 触るとき: 全件表示ボタンの遷移先を変えるときに見る。
- 呼び出し先: `chromeWin.openTrustedLinkIn()`

## callback()
- 位置: L1183-1188
- 役割: 今後表示しないボタン。requestedNeverShowAgain を真にし、onAction を呼ぶ。
- 触るとき: 要求通知を今後出さない設定の保存先を確かめるときに見る。
- 条件付き依存: `if (onAction)` → `onAction()`
- 参照: `this.requestedNeverShowAgain`

## eventCallback()
- 位置: L1205-1218
- 役割: dismissed の時、対象の報告を無視扱いにして onAction を呼ぶ。
- 触るとき: 通知を閉じた報告が以後送られなくなる理由を追うときに見る。
- 条件付き依存: `if (eventType == "dismissed")` → `reportIDs.forEach()`
- 条件付き依存: `if (eventType == "dismissed")` → `lazy.CrashSubmit.ignore()`
- 条件付き依存: `if (onAction)` → `onAction()`

## autoSubmit()
- 位置: L1237-1241
- 役割: unsubmittedCheck.autoSubmit2 の値を返すゲッター。
- 触るとき: 自動送信が有効かを判定する箇所を探すときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## autoSubmit()
- 位置: L1243-1248
- 役割: unsubmittedCheck.autoSubmit2 に値を設定するセッター。
- 触るとき: 自動送信の切り替えが pref に反映される経路を追うときに見る。
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## requestedNeverShowAgain()
- 位置: L1250-1255
- 役割: browser.crashReports.requestedNeverShowAgain に値を設定するセッター。
- 触るとき: 要求通知を今後出さない設定を変えるときに見る。
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## submitReports()
- 位置: L1268-1280
- 役割: 報告 ID ごとに CrashSubmit.submit を呼び、失敗はログに残す。
- 触るとき: 未送信報告の送信経路や送信時のパラメータを変えるときに見る。
- 呼び出し先: `lazy.CrashSubmit.submit()`, `lazy.CrashSubmit.submit(reportID, submittedFrom, params).catch()`, `this.log.debug()`, `this.log.error.bind()`
- 参照: `reportIDs.length`, `this.log`

## enabled()
- 位置: L1297-1299
- 役割: cleanupCheck.enabled の値を返すゲッター(CrashFileCleaner 用)。
- 触るとき: クリーンアップ機能の有効判定を調べるときに見る。
- 呼び出し先: `lazy.cleanerPrefs.getBoolPref()`

## init()
- 位置: L1303-1313
- 役割: 初期化済みフラグを立てる。無効ならログを出すだけで、予約はしない。
- 触るとき: クリーンアップが無効のときの動きを確かめるときに見る。
- 条件付き依存: `if (!this.enabled)` → `lazy.cleanerLog.debug()`
- 参照: `this.enabled`, `this.initialized`

## uninit()
- 位置: L1315-1326
- 役割: 初期化済みフラグを下ろし、予約中のクリーンアップのタイマーを止める。
- 触るとき: 終了時にクリーンアップの予約が残るときに見る。
- 条件付き依存: `if (this._checkTimeout)` → `lazy.clearTimeout()`
- 参照: `this._checkTimeout`, `this.initialized`

## scheduleCleanup()
- 位置: L1328-1334
- 役割: 起動から 5 分 23 秒後に、アイドル時にクリーンアップを実行するよう予約する。
- 触るとき: クリーンアップの開始時刻を変えるときに見る。
- 呼び出し先: `Services.tm.idleDispatchToMainThread()`, `lazy.setTimeout()`, `this.runCleanup()`
- 参照: `this._checkTimeout`
- XPCOM: `Services.tm`

## _ranRecently()
- 位置: L1336-1345
- 役割: 最後の実行日時が 7 日以内なら真を返す。日時の pref が無効なら偽を返す。
- 触るとき: クリーンアップが実行されない理由を調べるとき、または実行間隔を変えるときに見る。
- 呼び出し先: `Date.now()`, `Date.parse()`, `isNaN()`, `lazy.cleanerPrefs.getCharPref()`, `lazy.cleanerPrefs.prefHasUserValue()`

## pruneInstallTimeMarkers()
- 位置: async L1347-1349
- 役割: 90 日より古いインストール時刻のマーカーを削除する。
- 触るとき: インストール時のクラッシュ関連ファイルが残る、または消えすぎるときに見る。
- 呼び出し先: `lazy.CrashReports.pruneInstallTimeFiles()`

## pruneOldReports()
- 位置: async L1351-1362
- 役割: 180 日より古いレポートを削除する。保留中のものは保留の削除、送信済みのものは送信済みの削除を使う。
- 触るとき: 古いクラッシュレポートが残る、または消されすぎるときに見る。
- 呼び出し先: `Date.now()`, `lazy.CrashReports.getReports()`
- 条件付き依存: `if (report.pending)` → `lazy.CrashReports.deletePendingReport()`
- 条件付き依存: `if (!(report.pending))` → `lazy.CrashReports.deleteSubmittedReport()`
- 参照: `report.date`, `report.id`, `report.pending`

## enforcePendingCap()
- 位置: async L1367-1375
- 役割: 保留中レポートが 30 件を超えたとき、30 件より後ろのものを削除する。
- 触るとき: 保留レポートの上限を変えるとき、または削除される報告が古い順かを確かめるときに見る。(要確認: 並び順を指定していない)
- 呼び出し先: `lazy.CrashReports.deletePendingReport()`, `lazy.CrashReports.getReports()`, `lazy.CrashReports.getReports().filter()`, `pending.slice()`
- 参照: `pending.length`, `r.pending`, `report.id`

## runCleanup()
- 位置: async L1377-1396
- 役割: 無効、または直近 7 日以内に実行済みなら何もしない。そうでなければ古いマーカー、古いレポート、保留の上限を順に処理し、最後に実行日時を記録する。途中の例外はログに残す。
- 触るとき: クリーンアップの処理順や実行間隔を変えるときに見る。
- 呼び出し先: `lazy.cleanerLog.debug()`, `lazy.cleanerLog.error()`, `lazy.cleanerPrefs.setCharPref()`, `new Date().toISOString()`, `this._ranRecently()`, `this.enforcePendingCap()`, `this.pruneInstallTimeMarkers()`, `this.pruneOldReports()`
- 条件付き依存: `if (this._ranRecently())` → `lazy.cleanerLog.debug()`
- 参照: `this.enabled`
