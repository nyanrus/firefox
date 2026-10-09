# browser/modules/SitePermissions.sys.mjs

source: browser/modules/SitePermissions.sys.mjs
source-hash: d8be7e764416d2d74aacb70214117e688b05c6a5
lines: 1170

## <module>
- 役割: サイトごとの権限(永続、セッション、一時、グローバル)の状態を取得・設定・削除し、表示ラベルと既定値を管理する。
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.getBoolPref()`, `Services.prefs.getBranch()`, `Services.strings.createBundle()`, `SitePermissions.invalidatePermissionList.bind()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## observe()
- 位置: L16-33
- 役割: browser-perm-changed を受け、対象タブの browserId から PermissionStateChange イベントを発行する。
- 触るとき: 権限パネルやアイデンティティパネルの表示が権限の変更に追随しない問題を調べるとき。
- 呼び出し先: `BrowsingContext.getCurrentTopByBrowserId()`, `subject.QueryInterface()`, `subject?.QueryInterface()`
- 条件付き依存: `if (browser?.documentGlobal)` → `browser.dispatchEvent()`
- 参照: `Ci.nsIPermission`, `Ci.nsISupportsPRUint64`, `bc?.embedderElement`, `browser.documentGlobal.CustomEvent`, `browser?.documentGlobal`, `subject.QueryInterface(Ci.nsIPermission).browserId`, `subject?.QueryInterface(Ci.nsISupportsPRUint64).data`
- XPCOM: [`nsIPermission`](../../netwerk/base/nsIPermission.idl.md) / [`nsISupportsPRUint64`](../../xpcom/ds/nsISupportsPrimitives.idl.md)

## set()
- 位置: L49-91
- 役割: グローバルでブロックされた権限をタブとオリジンごとに記録し、初めての記録なら遷移を監視する登録を行う。新しく記録したら true を返す。
- 触るとき: ブロックされた権限の通知をどの範囲で出すかを変えるとき。
- 呼び出し先: `ChromeUtils.generateQI()`, `browser.addProgressListener()`, `this._stateByBrowser.get()`, `this._stateByBrowser.has()`
- 条件付き依存: `if (!this._stateByBrowser.has(browser))` → `this._stateByBrowser.set()`
- 参照: `Ci.nsIWebProgress.NOTIFY_LOCATION`, `browser.contentPrincipal.origin`, `browser.currentURI`
- XPCOM: [`nsIWebProgress`](../../dom/interfaces/base/nsIBrowser.idl.md)

## onLocationChange()
- 位置: L74-86
- 役割: トップレベルでページを離れた、またはリロードされたとき、その権限の記録を消して監視を外す。
- 触るとき: ブロックの記録がいつ消えるかを変えるとき、リロード後も通知が残る問題を調べるとき。
- 条件付き依存: `if (aWebProgress.isTopLevel && (hasLeftPage || isReload))` → `GloballyBlockedPermissions.remove()`
- 条件付き依存: `if (aWebProgress.isTopLevel && (hasLeftPage || isReload))` → `browser.removeProgressListener()`
- 参照: `Ci.nsIWebProgressListener.LOCATION_CHANGE_RELOAD`, `Ci.nsIWebProgressListener.LOCATION_CHANGE_SAME_DOCUMENT`, `aLocation.prePath`, `aWebProgress.isTopLevel`
- XPCOM: [`nsIWebProgressListener`](../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## remove()
- 位置: L94-102
- 役割: タブとオリジンの組に対して指定 ID の記録を削除する。オリジンが省略されたら現在のコンテンツのオリジンを使う。
- 触るとき: グローバルブロックの記録の削除対象を変えるとき。
- 呼び出し先: `this._stateByBrowser.get()`
- 参照: `browser.contentPrincipal.origin`

## getAll()
- 位置: L107-122
- 役割: 現在のオリジンで記録されているグローバルブロック権限を、既定の状態と共に返す。
- 触るとき: グローバルにブロックされた権限の表示内容を変えるとき。
- 呼び出し先: `this._stateByBrowser.get()`
- 条件付き依存: `if (entry && entry[origin])` → `Object.keys()`
- 条件付き依存: `if (entry && entry[origin])` → `permissions.push()`
- 条件付き依存: `if (entry && entry[origin])` → `gPermissions.get(id).getDefault()`
- 条件付き依存: `if (entry && entry[origin])` → `gPermissions.get()`
- 参照: `SitePermissions.SCOPE_GLOBAL`, `browser.contentPrincipal.origin`

## copy()
- 位置: L126-131
- 役割: あるタブのグローバルブロック記録を、別のタブへ移す。
- 触るとき: タブを入れ替えた後にブロック記録が失われる問題を調べるとき。
- 呼び出し先: `this._stateByBrowser.get()`
- 条件付き依存: `if (entry)` → `this._stateByBrowser.set()`

## getAllByPrincipal()
- 位置: L175-223
- 役割: プリンシパルの永続、セッション、ポリシーの権限を返す。無効な権限と、拡張の unlimitedStorage が許可された永続ストレージは除く。
- 触るとき: サイトの権限一覧に出す項目や除外条件を変えるとき。
- 呼び出し先: `Services.perms .getAllForPrincipal()`, `Services.perms .getAllForPrincipal(principal) .filter()`, `SitePermissions.getForPrincipal()`, `gPermissions.get()`, `permissions.map()`, `this.isSupportedPrincipal()`
- 参照: `Services.perms.EXPIRE_POLICY`, `Services.perms.EXPIRE_SESSION`, `SitePermissions.ALLOW`, `SitePermissions.getForPrincipal( principal, "WebExtensions-unlimitedStorage" ).state`, `entry.disabled`, `entry.id`, `permission.capability`, `permission.expireType`, `permission.type`, `this.SCOPE_PERSISTENT`, `this.SCOPE_POLICY`, `this.SCOPE_SESSION`
- XPCOM: `Services.perms`

## getAllForBrowser()
- 位置: L241-268
- 役割: タブの一時権限、グローバルブロック、プリンシパルの権限を1つの一覧にまとめる。同じ ID は後から入れたものが優先される。
- 触るとき: タブの権限表示の内容や優先順位を変えるとき。
- 呼び出し先: `GloballyBlockedPermissions.getAll()`, `Object.values()`, `this.getAllByPrincipal()`, `this.isSupportedPrincipal()`
- 条件付き依存: `if (browserId && this.isSupportedPrincipal(browser.contentPrincipal))` → `Services.perms.getAllForBrowser()`
- 参照: `browser.browserId`, `browser.contentPrincipal`, `perm.capability`, `perm.type`, `permission.id`, `this.SCOPE_TEMPORARY`
- XPCOM: `Services.perms`

## getAllPermissionDetailsForBrowser()
- 位置: L285-292
- 役割: getAllForBrowser の結果に表示ラベルを付けて返す。
- 触るとき: 権限の詳細表示に出す情報を増やすとき。
- 呼び出し先: `this.getAllForBrowser()`, `this.getAllForBrowser(browser).map()`, `this.getPermissionLabel()`

## isSupportedPrincipal()
- 位置: L303-313
- 役割: プリンシパルのスキームが権限管理の対象かを返す。nsIPrincipal でなければ例外を投げる。
- 触るとき: 権限 UI を出す対象を判定する箇所を変えるとき。
- 呼び出し先: `this.isSupportedScheme()`
- 参照: `Ci.nsIPrincipal`, `principal.scheme`
- XPCOM: [`nsIPrincipal`](../../docshell/base/nsIDocShell.idl.md)

## isSupportedScheme()
- 位置: L321-323
- 役割: http、https、moz-extension、file のいずれかなら true を返す。
- 触るとき: 権限管理の対象スキームを増やす・減らすとき。
- 呼び出し先: `["http", "https", "moz-extension", "file"].includes()`

## listPermissions()
- 位置: L330-335
- 役割: 有効な権限 ID の一覧を初回に作ってキャッシュし、以後はそれを返す。
- 触るとき: 権限の一覧が設定変更後も古いままになる問題を調べるとき。
- 条件付き依存: `if (this._permissionsArray === null)` → `gPermissions.getEnabledPermissions()`
- 参照: `this._permissionsArray`

## isSitePermission()
- 位置: L343-345
- 役割: 指定の type が SitePermissions で管理される権限かを返す。
- 触るとき: 管理対象外の権限を除外する判定を変えるとき。
- 呼び出し先: `gPermissions.has()`

## invalidatePermissionList()
- 位置: L357-361
- 役割: キャッシュした権限一覧を破棄し、次の listPermissions で作り直させる。
- 触るとき: 権限一覧が依存する pref の変更に追随しない問題を調べるとき。
- 参照: `this._permissionsArray`

## getAvailableStates()
- 位置: L372-396
- 役割: 権限の選択肢を返す。権限固有の定義があればそれを使い、無ければ既定値が UNKNOWN かどうかで UNKNOWN か PROMPT のどちらか一方を入れた標準の3択を返す。
- 触るとき: 権限ごとに利用者へ見せる状態の並びを変えるとき。
- 呼び出し先: `gPermissions.get()`, `gPermissions.has()`, `this.getDefault()`
- 条件付き依存: `if ( gPermissions.has(permissionID) && gPermissions.get(permissionID).states )` → `gPermissions.get()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.BLOCK`, `SitePermissions.PROMPT`, `SitePermissions.UNKNOWN`, `gPermissions.get(permissionID).states`, `this.UNKNOWN`

## getDefault()
- 位置: L406-418
- 役割: 権限の既定値を、権限固有の関数があればそれで、無ければ permissions.default.<ID> の pref から返す。
- 触るとき: 権限の既定値の決め方を変えるとき。
- 呼び出し先: `gPermissions.get()`, `gPermissions.has()`, `this._defaultPrefBranch.getIntPref()`
- 条件付き依存: `if ( gPermissions.has(permissionID) && gPermissions.get(permissionID).getDefault )` → `gPermissions.get(permissionID).getDefault()`
- 条件付き依存: `if ( gPermissions.has(permissionID) && gPermissions.get(permissionID).getDefault )` → `gPermissions.get()`
- 参照: `gPermissions.get(permissionID).getDefault`, `this.UNKNOWN`

## setDefault()
- 位置: L429-438
- 役割: 権限固有の setDefault があればそれに任せ、無ければ permissions.default.<ID> の pref に値を保存する。
- 触るとき: 既定値の保存先を変えるとき。
- 呼び出し先: `Services.prefs.setIntPref()`, `gPermissions.get()`, `gPermissions.has()`
- 条件付き依存: `if ( gPermissions.has(permissionID) && gPermissions.get(permissionID).setDefault )` → `gPermissions.get(permissionID).setDefault()`
- 条件付き依存: `if ( gPermissions.has(permissionID) && gPermissions.get(permissionID).setDefault )` → `gPermissions.get()`
- 参照: `gPermissions.get(permissionID).setDefault`
- XPCOM: `Services.prefs`

## getForPrincipal()
- 位置: L459-524
- 役割: 永続権限を取得し、既定値のままか PROMPT の場合は、タブの一時権限があればそれで上書きする。状態と scope を返す。
- 触るとき: サイトの現在の状態を決める優先順位を変えるとき、一時的に許可したのに効かない問題を調べるとき。
- 呼び出し先: `this.getDefault()`, `this.isSupportedPrincipal()`
- 条件付き依存: `if (this.isSupportedPrincipal(principal))` → `gPermissions.has()`
- 条件付き依存: `if (this.isSupportedPrincipal(principal))` → `gPermissions.get()`
- 条件付き依存: `if ( gPermissions.has(permissionID) && gPermissions.get(permissionID).exactHostMatch )` → `Services.perms.getPermissionObject()`
- 条件付き依存: `if (!( gPermissions.has(permissionID) && gPermissions.get(permissionID).exactHostMatch ))` → `Services.perms.getPermissionObject()`
- 条件付き依存: `if (browserId)` → `Services.perms.getForBrowser()`
- 参照: `Services.perms.EXPIRE_POLICY`, `Services.perms.EXPIRE_SESSION`, `SitePermissions.PROMPT`, `browser.browserId`, `browser.contentPrincipal`, `gPermissions.get(permissionID).exactHostMatch`, `permission.capability`, `permission.expireType`, `result.scope`, `result.state`, `tempPerm.capability`, `this.SCOPE_PERSISTENT`, `this.SCOPE_POLICY`, `this.SCOPE_SESSION`, `this.SCOPE_TEMPORARY`
- XPCOM: `Services.perms`

## setForPrincipal()
- 位置: L547-621
- 役割: 権限を保存する。グローバルな BLOCK は記録だけ行う。既定値と同じか UNKNOWN なら cookie 以外は削除する。一時の scope はタブに、それ以外は scope に応じた期限でプリンシパルに保存する。
- 触るとき: 権限の保存先や期限の扱いを変えるとき、設定した権限が期待どおりに保存されない問題を調べるとき。
- 呼び出し先: `this.getDefault()`
- 条件付き依存: `if (scope == this.SCOPE_GLOBAL && state == this.BLOCK)` → `GloballyBlockedPermissions.set()`
- 条件付き依存: `if (GloballyBlockedPermissions.set(browser, permissionID))` → `browser.dispatchEvent()`
- 条件付き依存: `if (permissionID != "cookie")` → `this.removeFromPrincipal()`
- 条件付き依存: `if (scope == this.SCOPE_TEMPORARY)` → `Number.isInteger()`
- 条件付き依存: `if (browserId)` → `Services.perms.addFromPrincipalForBrowser()`
- 条件付き依存: `if (!(scope == this.SCOPE_TEMPORARY))` → `this.isSupportedPrincipal()`
- 条件付き依存: `if (this.isSupportedPrincipal(principal))` → `Services.perms.addFromPrincipal()`
- 参照: `Services.perms.EXPIRE_NEVER`, `Services.perms.EXPIRE_POLICY`, `Services.perms.EXPIRE_SESSION`, `SitePermissions.temporaryPermissionExpireTime`, `browser.browserId`, `browser.contentPrincipal`, `browser.documentGlobal.CustomEvent`, `this.ALLOW_COOKIES_FOR_SESSION`, `this.BLOCK`, `this.SCOPE_GLOBAL`, `this.SCOPE_PERSISTENT`, `this.SCOPE_POLICY`, `this.SCOPE_SESSION`, `this.SCOPE_TEMPORARY`, `this.UNKNOWN`
- XPCOM: `Services.perms`

## removeFromPrincipal()
- 位置: L635-655
- 役割: プリンシパルの永続権限を削除し、タブが渡されていればそのタブの一時権限も削除する。
- 触るとき: 権限を消したのに一時権限が残る問題を調べるとき。
- 呼び出し先: `this.isSupportedPrincipal()`
- 条件付き依存: `if (this.isSupportedPrincipal(principal))` → `Services.perms.removeFromPrincipal()`
- 条件付き依存: `if (browserId)` → `Services.perms.removeFromPrincipalForBrowser()`
- 参照: `browser.browserId`, `browser.contentPrincipal`
- XPCOM: `Services.perms`

## clearTemporaryBlockPermissions()
- 位置: L663-671
- 役割: タブに一時的に保存された拒否(DENY)の権限を、すべて削除する。
- 触るとき: 一時的なブロックがタブに残って再びブロックされる問題を調べるとき。
- 条件付き依存: `if (browserId)` → `Services.perms.removeByActionForBrowser()`
- 参照: `Services.perms.DENY_ACTION`, `browser.browserId`
- XPCOM: `Services.perms`

## copyTemporaryPermissions()
- 位置: L684-690
- 役割: 一時権限をソースのタブからの宛先のタブへ複製し、グローバルブロック記録も移す。
- 触るとき: タブを移動したときに一時権限やブロック記録が引き継がれない問題を調べるとき。
- 呼び出し先: `GloballyBlockedPermissions.copy()`
- 条件付き依存: `if (srcBrowserId && destBrowserId && srcBrowserId !== destBrowserId)` → `Services.perms.copyBrowserPermissions()`
- 参照: `destBrowser.browserId`
- XPCOM: `Services.perms`

## getPermissionLabel()
- 位置: L703-724
- 役割: 権限 ID(第2キーを含む)から表示用のラベルを返す。3rdPartyStorage は第2キーをそのまま返し、ラベルの無い権限は null を返す。
- 触るとき: 権限パネルの表示名を変えるとき、ラベルが出ない権限を調べるとき。
- 呼び出し先: `gPermissions.get()`, `gPermissions.has()`, `gStringBundle.formatStringFromName()`, `permissionID.split()`
- 参照: `gPermissions.get(id).labelID`, `this.PERM_KEY_DELIMITER`

## getMultichoiceStateLabel()
- 位置: L739-764
- 役割: 権限の状態に対応する選択肢の文言を返す。権限固有の定義があればそれを使う。
- 触るとき: 選択肢の文言を変えるとき。
- 呼び出し先: `gPermissions.get()`, `gPermissions.has()`, `gStringBundle.GetStringFromName()`
- 条件付き依存: `if ( gPermissions.has(permissionID) && gPermissions.get(permissionID).getMultichoiceStateLabel )` → `gPermissions.get(permissionID).getMultichoiceStateLabel()`
- 条件付き依存: `if ( gPermissions.has(permissionID) && gPermissions.get(permissionID).getMultichoiceStateLabel )` → `gPermissions.get()`
- 参照: `gPermissions.get(permissionID).getMultichoiceStateLabel`, `this.ALLOW`, `this.ALLOW_COOKIES_FOR_SESSION`, `this.BLOCK`, `this.PROMPT`, `this.UNKNOWN`

## getCurrentStateLabel()
- 位置: L779-813
- 役割: 状態と期間(一時か恒久か)に応じた、現在の状態の表示文言を返す。
- 触るとき: 許可や拒否の現在状態の表示、一時の表記を変えるとき。
- 呼び出し先: `gStringBundle.GetStringFromName()`
- 条件付き依存: `if ( scope && scope != this.SCOPE_PERSISTENT && scope != this.SCOPE_POLICY )` → `gStringBundle.GetStringFromName()`
- 条件付き依存: `if ( scope && scope != this.SCOPE_PERSISTENT && scope != this.SCOPE_POLICY && scope != this.SCOPE_GLOBAL )` → `gStringBundle.GetStringFromName()`
- 参照: `this.ALLOW`, `this.ALLOW_COOKIES_FOR_SESSION`, `this.BLOCK`, `this.PROMPT`, `this.SCOPE_GLOBAL`, `this.SCOPE_PERSISTENT`, `this.SCOPE_POLICY`

## _getId()
- 位置: L817-821
- 役割: 権限型から第2キー(^ 以降)を取り除いた ID を返す。
- 触るとき: open-protocol-handler^irc のような二重キーの権限の扱いを変えるとき。
- 呼び出し先: `type.split()`
- 参照: `SitePermissions.PERM_KEY_DELIMITER`

## has()
- 位置: L823-825
- 役割: 権限 ID が登録済みかどうかを返す。
- 触るとき: 未登録の権限が渡されたときの振る舞いを確認するとき。
- 呼び出し先: `this._getId()`
- 参照: `this._permissions`

## get()
- 位置: L827-834
- 役割: 登録済みの権限定義を ID 付きで返す。
- 触るとき: exactHostMatch や states などの定義項目を参照するとき。
- 呼び出し先: `this._getId()`
- 参照: `perm.id`, `this._permissions`

## getEnabledPermissions()
- 位置: L836-840
- 役割: 無効化されていない登録済みの権限 ID を返す。
- 触るとき: 無効化された権限(スピーカー、シリアルなど)が一覧に出ない問題を調べるとき。
- 呼び出し先: `Object.keys()`, `Object.keys(this._permissions).filter()`
- 参照: `this._permissions`, `this._permissions[id].disabled`

## getDefault()
- 位置: L869-881
- 役割: media.autoplay.default の値から ALLOW、AUTOPLAY_BLOCKED_ALL、BLOCK のいずれかを返す。
- 触るとき: 自動再生の既定値の判定を変えるとき。
- 呼び出し先: `Services.prefs.getIntPref()`
- 参照: `Ci.nsIAutoplay.ALLOWED`, `Ci.nsIAutoplay.BLOCKED`, `Ci.nsIAutoplay.BLOCKED_ALL`, `SitePermissions.ALLOW`, `SitePermissions.AUTOPLAY_BLOCKED_ALL`, `SitePermissions.BLOCK`
- XPCOM: [`nsIAutoplay`](../../dom/media/autoplay/nsIAutoplay.idl.md) / `Services.prefs`

## setDefault()
- 位置: L882-890
- 役割: 自動再生の既定値を media.autoplay.default に保存する。ALLOW は ALLOWED、AUTOPLAY_BLOCKED_ALL は BLOCKED_ALL、それ以外は BLOCKED にする。
- 触るとき: 自動再生の既定値の保存を変えるとき。
- 呼び出し先: `Services.prefs.setIntPref()`
- 参照: `Ci.nsIAutoplay.ALLOWED`, `Ci.nsIAutoplay.BLOCKED`, `Ci.nsIAutoplay.BLOCKED_ALL`, `SitePermissions.ALLOW`, `SitePermissions.AUTOPLAY_BLOCKED_ALL`
- XPCOM: [`nsIAutoplay`](../../dom/media/autoplay/nsIAutoplay.idl.md) / `Services.prefs`

## getMultichoiceStateLabel()
- 位置: L897-913
- 役割: 自動再生の3つの状態に対応する文言を返し、それ以外の状態なら例外を投げる。
- 触るとき: 自動再生の選択肢の文言を変えるとき。
- 呼び出し先: `gStringBundle.GetStringFromName()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.AUTOPLAY_BLOCKED_ALL`, `SitePermissions.BLOCK`

## getDefault()
- 位置: L922-931
- 役割: Cookie の動作が全て拒否(REJECT)なら BLOCK、それ以外は ALLOW を返す。
- 触るとき: Cookie の既定の判定を変えるとき、拒否設定にしても既定が変わらない問題を調べるとき。
- 呼び出し先: `Services.cookies.getCookieBehavior()`
- 参照: `Ci.nsICookieService.BEHAVIOR_REJECT`, `SitePermissions.ALLOW`, `SitePermissions.BLOCK`
- XPCOM: [`nsICookieService`](../../netwerk/cookie/nsICookieService.idl.md) / `Services.cookies`

## disabled()
- 位置: L946-948
- 役割: network.lna.blocking が無効なら、この権限を非表示にする。
- 触るとき: ローカルホストへのアクセス権限を表示する条件を変えるとき。
- 参照: `SitePermissions.localNetworkAccessPermissionsEnabled`

## disabled()
- 位置: L953-955
- 役割: network.lna.blocking が無効なら、この権限を非表示にする。
- 触るとき: ローカルネットワークへのアクセス権限を表示する条件を変えるとき。
- 参照: `SitePermissions.localNetworkAccessPermissionsEnabled`

## disabled()
- 位置: L970-972
- 役割: media.setsinkid.enabled が無効なら、この権限を非表示にする。
- 触るとき: スピーカー選択の権限を表示する条件を変えるとき。
- 参照: `SitePermissions.setSinkIdEnabled`

## labelID()
- 位置: L981-997
- 役割: ポップアップ抑止と枠組み破りの防止のどちらが有効かで、ラベル ID を popup-only、framebusting-only、popup-and-framebusting から選ぶ。
- 触るとき: ポップアップの権限の表示名を変えるとき。
- 参照: `SitePermissions.framebustingInterventionEnabled`, `SitePermissions.popupBlockerEnabled`

## disabled()
- 位置: L999-1004
- 役割: ポップアップ抑止と枠組み破りの防止の両方が無効なら、この権限を非表示にする。
- 触るとき: ポップアップの権限を表示する条件を変えるとき。
- 参照: `SitePermissions.framebustingInterventionEnabled`, `SitePermissions.popupBlockerEnabled`

## getDefault()
- 位置: L1005-1007
- 役割: 既定値として BLOCK を返す。
- 触るとき: ポップアップの既定値を変えるとき。
- 参照: `SitePermissions.BLOCK`

## getDefault()
- 位置: L1011-1015
- 役割: xpinstall.whitelist.required が有効なら UNKNOWN、無効なら ALLOW を返す。
- 触るとき: 拡張機能のインストール権限の既定値を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.UNKNOWN`
- XPCOM: `Services.prefs`

## disabled()
- 位置: L1048-1050
- 役割: 終了時のサイトデータ消去が無効なら、この権限を非表示にする。
- 触るとき: 終了時にデータを残す例外を表示する条件を変えるとき。
- 参照: `SitePermissions.sanitizeOnShutdownEnabled`

## getDefault()
- 位置: L1051-1053
- 役割: 既定値として UNKNOWN(終了時に消去)を返す。
- 触るとき: 終了時の既定の動作を変えるとき。
- 参照: `SitePermissions.UNKNOWN`

## getMultichoiceStateLabel()
- 位置: L1055-1067
- 役割: UNKNOWN と ALLOW の文言を返し、それ以外の状態なら例外を投げる。
- 触るとき: 終了時にデータを残す選択肢の文言を変えるとき。
- 呼び出し先: `gStringBundle.GetStringFromName()`
- 参照: `SitePermissions.ALLOW`, `SitePermissions.UNKNOWN`

## disabled()
- 位置: L1075-1077
- 役割: privacy.resistFingerprinting が無効なら、この権限を非表示にする。
- 触るとき: canvas の権限を表示する条件を変えるとき。
- 参照: `SitePermissions.resistFingerprinting`

## disabled()
- 位置: L1082-1084
- 役割: dom.webmidi.enabled が無効なら、この権限を非表示にする。
- 触るとき: MIDI の権限を表示する条件を変えるとき。
- 参照: `SitePermissions.midiPermissionEnabled`

## disabled()
- 位置: L1089-1091
- 役割: dom.webmidi.enabled が無効なら、この権限を非表示にする。
- 触るとき: MIDI の SysEx 権限を表示する条件を変えるとき。
- 参照: `SitePermissions.midiPermissionEnabled`

## disabled()
- 位置: L1096-1098
- 役割: dom.webserial.enabled が無効なら、この権限を非表示にする。
- 触るとき: シリアルポートの権限を表示する条件を変えるとき。
- 参照: `SitePermissions.serialPermissionEnabled`

## getDefault()
- 位置: L1103-1105
- 役割: 既定値として UNKNOWN を返す。
- 触るとき: ストレージアクセス権限の既定値を変えるとき。
- 参照: `SitePermissions.UNKNOWN`
