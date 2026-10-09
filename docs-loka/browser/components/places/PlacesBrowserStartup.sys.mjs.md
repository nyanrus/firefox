# browser/components/places/PlacesBrowserStartup.sys.mjs

source: browser/components/places/PlacesBrowserStartup.sys.mjs
source-hash: b0ff1c184b1909bbbc8a359074426dc6a437e4e2
lines: 381

## <module>
- 役割: 起動時に Places を初期化し、ブックマークの取り込み・復元と定期バックアップを管理するオブジェクト。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `PlacesBrowserStartup._backupBookmarks.bind()`, `Promise.withResolvers()`, `XPCOMUtils.defineLazyServiceGetters()`

## onFirstWindowReady()
- 位置: L41-47
- 役割: 最初のウィンドウ準備完了を通知し、ファビコンの既定サイズを 16 に devicePixelRatio を掛けた値へ設定する。
- 触るとき: Places のファビコン表示サイズを変えるとき、初期化がウィンドウ準備を待つ理由を追うとき。
- 呼び出し先: `lazy.PlacesUtils.favicons.setDefaultIconURIPreferredSize()`, `this._firstWindowReady.resolve()`
- 参照: `window.devicePixelRatio`

## backendInitComplete()
- 位置: L49-53
- 役割: 移行で既定ブックマークを取り込み中でなければ initPlaces を呼ぶ。
- 触るとき: データベースの初期化完了後に Places を起動する順序を変えるとき。
- 条件付き依存: `if (!this._migrationImportsDefaultBookmarks)` → `this.initPlaces()`
- 参照: `this._migrationImportsDefaultBookmarks`

## willImportDefaultBookmarks()
- 位置: L55-57
- 役割: 既定ブックマークを取り込む予定のフラグを立て、backendInitComplete からの initPlaces を止める。
- 触るとき: 移行による取り込みと起動時の初期化が競合する問題を調べるとき。
- 参照: `this._migrationImportsDefaultBookmarks`

## didImportDefaultBookmarks()
- 位置: L59-61
- 役割: 取り込み完了後に initialMigrationPerformed を真にして initPlaces を呼ぶ。
- 触るとき: 移行直後の初期化でブックマークが二重に取り込まれる問題を調べるとき。
- 呼び出し先: `this.initPlaces()`

## initPlaces()
- 位置: L84-282
- 役割: DB の状態に応じてブックマークを取り込み・復元し、ディストリビューションの適用とバックアップの待ち受けを設定する。二重初期化は例外、DB がロック中ならウィンドウ準備後に通知を出す。
- 触るとき: 初回起動や破損時の取り込み順序を変えるとき、places.sqlite がロックされた場合の通知を調べるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `Services.prefs.getBoolPref()`, `console.error()`, `lazy.PlacesBackups.hasRecentBackup()`
- 条件付き依存: `if (dbStatus == lazy.PlacesUtils.history.DATABASE_STATUS_LOCKED)` → `this._firstWindowReady.promise.then()`
- 条件付き依存: `if (dbStatus == lazy.PlacesUtils.history.DATABASE_STATUS_LOCKED)` → `this._showPlacesLockedNotificationBox()`
- 条件付き依存: `if (dbStatus == lazy.PlacesUtils.history.DATABASE_STATUS_LOCKED)` → `Services.obs.notifyObservers()`
- 条件付き依存: `if (autoExportHTML)` → `lazy.AsyncShutdown.profileChangeTeardown.addBlocker()`
- 条件付き依存: `if (autoExportHTML)` → `lazy.BookmarkHTMLUtils.exportToFile()`
- 条件付き依存: `if (restoreDefaultBookmarks)` → `this._backupBookmarks()`
- 条件付き依存: `if (importBookmarks && !restoreDefaultBookmarks && !importBookmarksHTML)` → `lazy.PlacesBackups.getMostRecentBackup()`
- 条件付き依存: `if (lastBackupFile)` → `lazy.BookmarkJSONUtils.importFromFile()`
- 条件付き依存: `if (!(lastBackupFile))` → `IOUtils.exists()`
- 条件付き依存: `if (!importBookmarks)` → `lazy.DistributionManagement.applyBookmarks()`
- 条件付き依存: `if (!importBookmarks)` → `console.error()`
- 条件付き依存: `if (!(restoreDefaultBookmarks))` → `IOUtils.exists()`
- 条件付き依存: `if (await IOUtils.exists(lazy.BookmarkHTMLUtils.defaultPath))` → `PathUtils.toFileURI()`
- 条件付き依存: `if (bookmarksUrl)` → `Services.policies.isAllowed()`
- 条件付き依存: `if (bookmarksUrl)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( Services.policies.isAllowed("defaultBookmarks") && // Default bookmarks are imported after startup, and they may // influence the outcome of tests, thus it'...)` → `lazy.BookmarkHTMLUtils.importFromURL()`
- 条件付き依存: `if (bookmarksUrl)` → `console.error()`
- 条件付き依存: `if (bookmarksUrl)` → `lazy.DistributionManagement.applyBookmarks()`
- 条件付き依存: `if (!(bookmarksUrl))` → `console.error()`
- 条件付き依存: `if (importBookmarksHTML)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (restoreDefaultBookmarks)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!this._isObservingIdle)` → `lazy.UserIdleService.addIdleObserver()`
- 条件付き依存: `if (!this._isObservingIdle)` → `Services.obs.addObserver()`
- 参照: `Cu.isInAutomation`, `lazy.BookmarkHTMLUtils.defaultPath`, `lazy.PlacesUtils.bookmarks.SOURCES.RESTORE_ON_STARTUP`, `lazy.PlacesUtils.history.DATABASE_STATUS_CORRUPT`, `lazy.PlacesUtils.history.DATABASE_STATUS_CREATE`, `lazy.PlacesUtils.history.DATABASE_STATUS_LOCKED`, `lazy.PlacesUtils.history.databaseStatus`, `this._backupBookmarks`, `this._bookmarksBackupIdleTime`, `this._isObservingIdle`, `this._placesBrowserInitComplete`, `this._placesInitialized`
- XPCOM: `Services.obs` / `Services.policies` / `Services.prefs`

## _backupBookmarks()
- 位置: async L287-301
- 役割: 当日のバックアップが無い、または最後のバックアップから 1 日以上経っていれば、browser.bookmarks.max_backups の上限付きで作成する。
- 触るとき: バックアップの間隔や上限を変えるとき、アイドル時にバックアップが作られない問題を調べるとき。
- 呼び出し先: `Date.now()`, `lazy.PlacesBackups.getDateForFile()`, `lazy.PlacesBackups.getDateForFile(lastBackupFile).getTime()`, `lazy.PlacesBackups.getMostRecentBackup()`
- 条件付き依存: `if ( !lastBackupFile || Date.now() - lazy.PlacesBackups.getDateForFile(lastBackupFile).getTime() > BOOKMARKS_BACKUP_MIN_INTERVAL_DAYS * 86400000 )` → `Services.prefs.getIntPref()`
- 条件付き依存: `if ( !lastBackupFile || Date.now() - lazy.PlacesBackups.getDateForFile(lastBackupFile).getTime() > BOOKMARKS_BACKUP_MIN_INTERVAL_DAYS * 86400000 )` → `lazy.PlacesBackups.create()`
- XPCOM: `Services.prefs`

## _showPlacesLockedNotificationBox()
- 位置: async L306-322
- 役割: 最上位ウィンドウのブラウザー通知欄に places-locked の通知を、ユーザーが閉じるまで残して表示する。
- 触るとき: ロック時の通知文言や案内リンクを変えるとき。
- 呼び出し先: `lazy.BrowserWindowTracker.getTopWindow()`, `notifyBox.appendNotification()`, `win.gBrowser.getNotificationBox()`
- 参照: `notification.persistence`, `win.gNotificationBox.PRIORITY_CRITICAL_MEDIUM`

## notifyIfInitializationComplete()
- 位置: L324-328
- 役割: 初期化が完了していれば places-browser-init-complete を通知し直す。
- 触るとき: 初期化完了を待つ側が後から登録した場合に通知を取りこぼす問題を調べるとき。
- 条件付き依存: `if (this._placesBrowserInitComplete)` → `Services.obs.notifyObservers()`
- 参照: `this._placesBrowserInitComplete`
- XPCOM: `Services.obs`

## maybeAddImportButton()
- 位置: async L330-356
- 役割: 取り込みボタンの追加済みフラグを見て、ポリシーで不可なら外し、新規プロファイルなら追加する。自動化テスト中は追加しない。
- 触るとき: 取り込みボタンの表示条件を変えるとき、新規プロファイルでボタンが出ない問題を調べるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.bookmarks.addedImportButton", false) )` → `Services.policies.isAllowed()`
- 条件付き依存: `if (!Services.policies.isAllowed("profileImport"))` → `lazy.PlacesUIUtils.removeImportButton()`
- 条件付き依存: `if ( Services.prefs.getBoolPref("browser.bookmarks.addedImportButton", false) )` → `lazy.PlacesUIUtils.removeImportButtonWhenImportSucceeds()`
- 条件付き依存: `if ( lazy.BrowserHandler.firstRunProfile && // Not in automation: the button changes CUI state, breaking tests !Cu.isInAutomation )` → `lazy.PlacesUIUtils.maybeAddImportButton()`
- 参照: `Cu.isInAutomation`, `lazy.BrowserHandler.firstRunProfile`
- XPCOM: `Services.policies` / `Services.prefs`

## handleShutdown()
- 位置: L358-366
- 役割: アイドル時のバックアップ処理の登録を外す。
- 触るとき: 終了時にバックアップ処理が残る問題を調べるとき。
- 条件付き依存: `if (this._bookmarksBackupIdleTime)` → `lazy.UserIdleService.removeIdleObserver()`
- 参照: `this._backupBookmarks`, `this._bookmarksBackupIdleTime`

## observe()
- 位置: L368-374
- 役割: profile-before-change を受けたとき handleShutdown を呼ぶ。
- 触るとき: 終了通知への対応を増やすとき。
- 呼び出し先: `this.handleShutdown()`
