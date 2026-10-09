# browser/modules/PermissionUI.sys.mjs

source: browser/modules/PermissionUI.sys.mjs
source-hash: f998d42c4ca564c43d299cb458d52028c115d7f2
lines: 2829

## <module>
- 役割: 権限プロンプトの基底クラス PermissionPrompt を公開し、内蔵の権限プロンプト(位置情報、XR、LNA、通知、永続ストレージ、MIDI、シリアル、ストレージアクセス、音声認識モデルなど)を実装する
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.strings.createBundle()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `XPCOMUtils.defineLazyServiceGetter()`

## PermissionPrompt.browser()
- 位置: L173-175
- 役割: 要求に対応する xul:browser を返す。基底は未実装で例外を投げる
- 触るとき: 新しい権限プロンプトのサブクラスを作るとき。この値が正しくないと prompt() が通知を出せない

## PermissionPrompt.principal()
- 位置: L184-186
- 役割: 要求元の nsIPrincipal を返す。基底は未実装で例外を投げる
- 触るとき: 権限を保存する対象オリジンを決めるとき。permissionKey の保存先もこの値で決まる

## PermissionPrompt.type()
- 位置: L192-194
- 役割: 要求の種別を返す。既定は undefined で、権限 DB のキーとは別物である
- 触るとき: 利用者に見せる種別と権限 DB のキーを分けたいとき

## PermissionPrompt.permissionKey()
- 位置: L207-209
- 役割: 権限 DB と一時権限で使う鍵を返す。既定は undefined で、その場合は権限の保存も照会もしない
- 触るとき: 許可状態を保存・照会するプロンプトを作るとき。post-prompt を有効にするには必須

## PermissionPrompt.usePermissionManager()
- 位置: L217-219
- 役割: true なら権限 DB を読み書きし、false なら一時権限との連携だけ行う。既定は true
- 触るとき: 永続の保存をせず一時権限だけ使う権限を作るとき

## PermissionPrompt.temporaryPermissionURI()
- 位置: L225-227
- 役割: 一時権限のスコープとなる URI を返す。既定は undefined で、その場合は browser.currentURI が使われる
- 触るとき: 一時権限の対象を現在のページ以外にしたいとき

## PermissionPrompt.temporaryPermissionExpireTimeMS()
- 位置: L233-235
- 役割: 一時権限の期限(ミリ秒)を返す。既定は undefined で、SitePermissions の既定値を使う
- 触るとき: この権限だけ一時権限の期限を変えたいとき

## PermissionPrompt.popupOptions()
- 位置: L246-248
- 役割: PopupNotification に渡す表示オプションを返す。既定は空オブジェクト
- 触るとき: 通知の表示オプションを変えるとき。prompt() は displayURI を要求元 URI に設定する(displayURI が明示的に false の場合を除く)

## PermissionPrompt.postPromptEnabled()
- 位置: L259-261
- 役割: 自動拒否された後に、後から永続許可を出す通知を出すかどうかを返す。既定は false
- 触るとき: 自動拒否のあとに利用者が許可を取り消せる導線を付けるとき。true なら permissionKey と postPromptActions も必要

## PermissionPrompt.requiresUserInput()
- 位置: L267-269
- 役割: true なら、要求に有効な一時的なユーザー操作が無いとき prompt() がキャンセルする。既定は false
- 触るとき: ユーザー操作(ジェスチャー)が必要な権限を作るとき

## PermissionPrompt.notificationID()
- 位置: L288-290
- 役割: PopupNotification の一意な ID を返す。基底は未実装で例外を投げる
- 触るとき: 新しいプロンプトを作るとき。他と重複しない ID を付ける。独自の popupnotification を使うなら ID に -notification を付けた接頭辞を返す

## PermissionPrompt.anchorID()
- 位置: L297-299
- 役割: 通知を付けるアンカー要素の ID を返す。既定は default-notification-icon
- 触るとき: 通知を既定のアイコンとは別の場所に出したいとき

## PermissionPrompt.message()
- 位置: L309-311
- 役割: 通知本文を返す。基底は未実装で例外を投げる
- 触るとき: 要求の文言を決めるとき。サイト名の表示は getPrincipalName を使うことが多い

## PermissionPrompt.hintText()
- 位置: L320-322
- 役割: 通知に出す補足文を返す。既定は undefined で、補足文を出さない
- 触るとき: 通知に補足の説明を添えたいとき

## PermissionPrompt.getPrincipalName()
- 位置: L330-336
- 役割: 拡張機能なら拡張機能名、それ以外は principal の hostPort を返す
- 触るとき: 通知文に出すサイト名や拡張機能名の形式を変えるとき
- 参照: `principal.addonPolicy`, `principal.addonPolicy.name`, `principal.hostPort`, `this.principal`

## PermissionPrompt.cancel()
- 位置: L344-346
- 役割: 要求を拒否するときの処理。基底は未実装で例外を投げる。permissionKey を持つサブクラスでのみ実装する
- 触るとき: 拒否時に要求へ応答を返す処理を書くとき

## PermissionPrompt.allow()
- 位置: L354-356
- 役割: 要求を許可するときの処理。基底は未実装で例外を投げる。permissionKey を持つサブクラスでのみ実装する
- 触るとき: 許可時に要求へ応答を返す処理を書くとき

## PermissionPrompt.promptActions()
- 位置: L380-382
- 役割: 通知の選択肢(許可・拒否など)を返す。既定は空配列で、先頭が既定の選択になる
- 触るとき: 選択肢の文言、アクセスキー、既定動作、保存スコープを変えるとき

## PermissionPrompt.postPromptActions()
- 位置: L402-404
- 役割: 後から出す永続許可通知の選択肢を返す。既定は null
- 触るとき: 自動拒否後の通知に出すボタンを変えるとき。スコープは常に永続になる

## PermissionPrompt.onBeforeShow()
- 位置: L416-418
- 役割: 通知を出す直前に呼ばれ、false を返すと表示を中止する。既定は true
- 触るとき: 表示前に計測を入れたり、表示を取りやめる条件を足したりするとき

## PermissionPrompt.onBeforeShowAsync()
- 位置: L431-431
- 役割: 表示前の非同期フック。既定は何もしない。返された Promise を prompt() が await する
- 触るとき: 通知の文言や選択肢を決めるのに非同期の処理が必要なとき

## PermissionPrompt.onShown()
- 位置: L437-437
- 役割: 通知が表示された後に呼ばれる。既定は何もしない
- 触るとき: 表示後に計測や状態更新を入れたいとき。後から出す通知では呼ばれない

## PermissionPrompt.onAfterShow()
- 位置: L443-443
- 役割: 通知が閉じられた後に呼ばれる。既定は何もしない
- 触るとき: 通知を閉じた後の後始末を書くとき。後から出す通知では呼ばれない

## PermissionPrompt.prompt()
- 位置: async L457-615
- 役割: 保存済みの権限で即座に許可・拒否するか判定し、必要なら通知を出す本体。保存されている BLOCK ならキャンセル、ALLOW なら許可する。ユーザー操作が必要な要求で操作が無いときは、後から出す通知を検討してからキャンセルする。
- 触るとき: 通知が出ない、または自動で許可・拒否される理由を調べるとき。選択肢は選んだ後の保存範囲と allow/cancel に変換される。Deny の選択肢は bug 2035581 に従い、安全遅延を付けない
- 呼び出し先: `popupNotificationActions.push()`, `this.#showNotification()`, `this.onBeforeShowAsync()`
- 条件付き依存: `if (this.usePermissionManager && this.permissionKey)` → `lazy.SitePermissions.getForPrincipal()`
- 条件付き依存: `if (state == lazy.SitePermissions.BLOCK)` → `this.cancel()`
- 条件付き依存: `if ( state == lazy.SitePermissions.ALLOW && !this.request.isRequestDelegatedToUnsafeThirdParty && !this.request.ignoreAllowSitePermission )` → `this.allow()`
- 条件付き依存: `if (this.permissionKey)` → `lazy.SitePermissions.getForPrincipal()`
- 条件付き依存: `if (this.postPromptEnabled)` → `this.onBeforeShowAsync()`
- 条件付き依存: `if (this.postPromptEnabled)` → `this.postPrompt()`
- 条件付き依存: `if ( this.requiresUserInput && !this.request.hasValidTransientUserGestureActivation )` → `this.cancel()`
- 条件付き依存: `if (!chromeWin.PopupNotifications)` → `this.cancel()`
- 参照: `Ci.nsIStandardURL`, `action.disableSecurityDelay`, `action.dismiss`, `chromeWin.PopupNotifications`, `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.BLOCK`, `promptAction.accessKey`, `promptAction.action`, `promptAction.dismiss`, `promptAction.label`, `this.browser`, `this.browser.documentGlobal`, `this.permissionKey`, `this.postPromptEnabled`, `this.principal`, `this.principal.URI`, `this.promptActions`, `this.request.hasValidTransientUserGestureActivation`, `this.request.ignoreAllowSitePermission`, `this.request.isRequestDelegatedToUnsafeThirdParty`, `this.requiresUserInput`, `this.temporaryPermissionURI`, `this.usePermissionManager`
- XPCOM: [`nsIStandardURL`](../../netwerk/base/nsIStandardURL.idl.md)

## callback()
- 位置: L542-598
- 役割: 利用者が選んだ選択肢を保存する。チェックありや Esc 以外、または永続指定なら永続(PB ならセッション)で保存し、要求元がトップレベルと同じなら一時権限として保存する。最後に allow か cancel を呼ぶ
- 触るとき: 「記憶する」チェックや Esc 操作で保存範囲が変わる問題を調べるとき。別オリジンの子フレームの要求は保存せず、この要求だけに効かせる
- 条件付き依存: `if (promptAction.callback)` → `promptAction.callback()`
- 条件付き依存: `if ( (state && state.checkboxChecked && state.source != "esc-press") || promptAction.scope == lazy.SitePermissions.SCOPE_PERSISTENT )` → `lazy.PrivateBrowsingUtils.isBrowserPrivate()`
- 条件付き依存: `if ( (state && state.checkboxChecked && state.source != "esc-press") || promptAction.scope == lazy.SitePermissions.SCOPE_PERSISTENT )` → `lazy.SitePermissions.setForPrincipal()`
- 条件付き依存: `if (!( (state && state.checkboxChecked && state.source != "esc-press") || promptAction.scope == lazy.SitePermissions.SCOPE_PERSISTENT ))` → `this.browser.contentPrincipal.equals()`
- 条件付き依存: `if (this.browser.contentPrincipal.equals(this.principal))` → `lazy.SitePermissions.setForPrincipal()`
- 条件付き依存: `if (promptAction.action == lazy.SitePermissions.ALLOW)` → `this.allow()`
- 条件付き依存: `if (!(promptAction.action == lazy.SitePermissions.ALLOW))` → `this.cancel()`
- 条件付き依存: `if (this.permissionKey)` → `lazy.SitePermissions.setForPrincipal()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.SCOPE_PERSISTENT`, `lazy.SitePermissions.SCOPE_SESSION`, `lazy.SitePermissions.SCOPE_TEMPORARY`, `promptAction.action`, `promptAction.callback`, `promptAction.scope`, `state.checkboxChecked`, `state.source`, `this.browser`, `this.permissionKey`, `this.principal`, `this.temporaryPermissionExpireTimeMS`, `this.usePermissionManager`

## PermissionPrompt.postPrompt()
- 位置: L617-677
- 役割: 自動拒否された要求に対して、永続許可を後から出せる通知を、アニメーション付きで出す
- 触るとき: 後から出す通知の表示条件、ボタン、アニメーションを変えるとき。permissionKey か postPromptActions が無いと例外になる。gReduceMotion が true ならアニメーションを付けない
- 呼び出し先: `popupNotificationActions.push()`, `this.#showNotification()`
- 条件付き依存: `if (!chromeWin.gReduceMotion)` → `chromeWin.document.getElementById()`
- 条件付き依存: `if (!chromeWin.gReduceMotion)` → `anchor.addEventListener()`
- 条件付き依存: `if (!chromeWin.gReduceMotion)` → `anchor.removeAttribute()`
- 条件付き依存: `if (!chromeWin.gReduceMotion)` → `anchor.setAttribute()`
- 参照: `browser.documentGlobal`, `chromeWin.PopupNotifications`, `chromeWin.gReduceMotion`, `promptAction.accessKey`, `promptAction.label`, `this.anchorID`, `this.browser`, `this.permissionKey`, `this.postPromptActions`, `this.principal`

## callback()
- 位置: L639-659
- 役割: 後から出す通知の選択肢を、永続(PB ならセッション)で権限に保存する
- 触るとき: 後から出す通知で選んだ許可の保存範囲を変えるとき
- 呼び出し先: `lazy.PrivateBrowsingUtils.isBrowserPrivate()`, `lazy.SitePermissions.setForPrincipal()`
- 条件付き依存: `if (promptAction.callback)` → `promptAction.callback()`
- 参照: `lazy.SitePermissions.SCOPE_PERSISTENT`, `lazy.SitePermissions.SCOPE_SESSION`, `promptAction.action`, `promptAction.callback`, `this.permissionKey`

## PermissionPrompt.#showNotification()
- 位置: L679-744
- 役割: 通知のオプションを整え、先頭の選択肢を主ボタン、残りを副ボタンとして PopupNotifications.show を呼ぶ。onBeforeShow が false なら表示しない
- 触るとき: 通知の閉じ方、hintText、displayURI、表示される条件を変えるとき。通常の通知は persistent と hideClose を付ける
- 呼び出し先: `actions.splice()`, `options.hasOwnProperty()`, `this.onBeforeShow()`
- 条件付き依存: `if (postPrompt || this.onBeforeShow() !== false)` → `chromeWin.PopupNotifications.show()`
- 参照: `actions.length`, `options.dismissed`, `options.displayURI`, `options.eventCallback`, `options.hideClose`, `options.hintText`, `options.persistent`, `this.anchorID`, `this.browser`, `this.browser.documentGlobal`, `this.hintText`, `this.message`, `this.notificationID`, `this.popupOptions`, `this.principal.URI`

## options.eventCallback()
- 位置: L696-723
- 役割: 通知のイベントを受け、swapping では true を返して通知を新しいブラウザへ移し、shown で onShown、removed で onAfterShow を呼ぶ
- 触るとき: タブの入れ替えで通知が移らない問題や、表示後・閉じた後の処理が呼ばれない問題を調べるとき。後から出す通知では onShown と onAfterShow を呼ばない
- 条件付き依存: `if (topic == "shown" && !postPrompt)` → `this.onShown()`
- 条件付き依存: `if (withoutUserResponse)` → `this.cancel()`
- 条件付き依存: `if (topic == "removed" && !postPrompt)` → `this.onAfterShow()`

## PermissionPromptForRequest.browser()
- 位置: L756-764
- 役割: nsIContentPermissionRequest の element を返し、無ければ window の chromeEventHandler を返す
- 触るとき: 要求から通知を出す xul:browser を特定し直す処理を変えるとき。単一プロセスとマルチプロセスの両方で同じ要素を得る
- 参照: `this.request.element`, `this.request.window.docShell.chromeEventHandler`

## PermissionPromptForRequest.principal()
- 位置: L766-769
- 役割: 要求のデリゲート principal(この権限タイプ用)を返す
- 触るとき: 委譲された要求で保存先のオリジンがずれる問題を調べるとき
- 呼び出し先: `request.getDelegatePrincipal()`, `this.request.QueryInterface()`
- 参照: `Ci.nsIContentPermissionRequest`, `this.type`
- XPCOM: [`nsIContentPermissionRequest`](../../dom/interfaces/base/nsIContentPermissionPrompt.idl.md)

## PermissionPromptForRequest.cancel()
- 位置: L771-773
- 役割: 要求の cancel を呼んで拒否をコンテンツへ返す
- 触るとき: 拒否時に要求へ応答する経路を変えるとき
- 呼び出し先: `this.request.cancel()`

## PermissionPromptForRequest.allow()
- 位置: L775-777
- 役割: 要求の allow を、渡された選択(choices)付きで呼んで許可をコンテンツへ返す
- 触るとき: 許可時に選択内容を要求へ渡す形を変えるとき
- 呼び出し先: `this.request.allow()`

## SitePermsAddonInstallRequest.installSitePermAddon()
- 位置: async L794-822
- 役割: サイト権限のアドオンを Web ページ経由でインストールし、成功か失敗に応じて onSuccess か onError を呼ぶ。失敗時はコンソールにエラーを出す
- 触るとき: サイト権限をアドオンとして入れる経路の失敗時の扱いやエラー文言を変えるとき
- 呼び出し先: `Services.console.logMessage()`, `lazy.AddonManager.installSitePermsAddonFromWebpage()`, `onError()`, `onSuccess()`, `scriptError.initWithWindowID()`, `scriptErrorClass.createInstance()`, `this.getInstallErrorMessage()`
- 参照: `Ci.nsIScriptError`, `err.message`, `this.browser`, `this.browser.browsingContext.currentWindowGlobal.innerWindowId`, `this.permName`, `this.principal`
- XPCOM: [`nsIScriptError`](../../dom/bindings/nsIScriptError.idl.md) / `@mozilla.org/scripterror;1` / `Services.console`

## SitePermsAddonInstallRequest.prompt()
- 位置: L824-841
- 役割: ループバックか、サイト権限アドオンの提供者が無効なら通常の prompt に戻し、それ以外はアドオンのインストールを行う。成功で allow、失敗で cancel する
- 触るとき: サイト権限をアドオン経由で扱う条件を変えるとき。localhost は通常の権限プロンプトになる
- 呼び出し先: `this.allow()`, `this.cancel()`, `this.installSitePermAddon()`
- 条件付き依存: `if (this.principal.isLoopbackHost || !lazy.sitePermsAddonsProviderEnabled)` → `super.prompt()`
- 参照: `lazy.sitePermsAddonsProviderEnabled`, `this.principal.isLoopbackHost`

## SitePermsAddonInstallRequest.getInstallErrorMessage()
- 位置: L850-852
- 役割: インストール失敗時のエラー文言を返す。既定は null で、子クラスが上書きする
- 触るとき: 特定の権限でインストール失敗時に分かりやすい文言を出したいとき

## GeolocationPermissionPrompt.constructor()
- 位置: L863-874
- 役割: 要求を保持し、要求の最初の権限種別からシステム側の案内(sysdlg か syssetting)を読み取る
- 触るとき: 位置情報の要求にシステム設定の案内を出す条件を変えるとき
- 呼び出し先: `request.types.QueryInterface()`, `super()`, `types.queryElementAt()`
- 条件付き依存: `if (perm.options.length)` → `perm.options.queryElementAt()`
- 参照: `Ci.nsIArray`, `Ci.nsIContentPermissionType`, `Ci.nsISupportsString`, `perm.options.length`, `this.request`, `this.systemPermissionMsg`
- XPCOM: [`nsIArray`](../../dom/events/nsIEventListenerService.idl.md) / [`nsIContentPermissionType`](../../dom/interfaces/base/nsIContentPermissionPrompt.idl.md) / [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md)

## GeolocationPermissionPrompt.type()
- 位置: L876-878
- 役割: 権限種別として geo を返す
- 触るとき: 位置情報の権限種別を変えるとき

## GeolocationPermissionPrompt.permissionKey()
- 位置: L880-882
- 役割: 権限 DB の鍵として geo を返す
- 触るとき: 位置情報の許可状態を保存・照会する鍵を変えるとき

## GeolocationPermissionPrompt.popupOptions()
- 位置: L884-912
- 役割: 詳細リンク、表示 URI の非表示、サイト名を設定し、PB 以外なら「記憶する」チェックを付ける。第三者への委譲なら第二の名前を入れてチェックを外す
- 触るとき: 位置情報の通知の記憶チェックや、委譲された要求の表示を変えるとき。非公開ウィンドウでは記憶チェックを出さない
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.getPrincipalName()`
- 条件付き依存: `if (this.request.isRequestDelegatedToUnsafeThirdParty)` → `this.getPrincipalName()`
- 条件付き依存: `if (options.checkbox.show)` → `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `options.checkbox`, `options.checkbox.label`, `options.checkbox.show`, `options.secondName`, `this.browser.documentGlobal`, `this.request.isRequestDelegatedToUnsafeThirdParty`, `this.request.principal`
- XPCOM: `Services.urlFormatter`

## GeolocationPermissionPrompt.notificationID()
- 位置: L914-916
- 役割: 通知 ID として geolocation を返す
- 触るとき: 位置情報の通知 ID を変えるとき

## GeolocationPermissionPrompt.anchorID()
- 位置: L918-920
- 役割: 通知を付けるアイコンとして geo-notification-icon を返す
- 触るとき: 位置情報の通知をツールバーのどのアイコンに付けるかを変えるとき

## GeolocationPermissionPrompt.message()
- 位置: L922-940
- 役割: file スキームなら file 用、委譲された第三者なら安全でない委譲用、それ以外は通常の文言を返す
- 触るとき: 位置情報の通知文を変えるとき。文言の差し込みには <> と {} を使う
- 呼び出し先: `lazy.gBrowserBundle.formatStringFromName()`, `this.principal.schemeIs()`
- 条件付き依存: `if (this.principal.schemeIs("file"))` → `lazy.gBrowserBundle.GetStringFromName()`
- 条件付き依存: `if (this.request.isRequestDelegatedToUnsafeThirdParty)` → `lazy.gBrowserBundle.formatStringFromName()`
- 参照: `this.request.isRequestDelegatedToUnsafeThirdParty`

## GeolocationPermissionPrompt.hintText()
- 位置: L942-960
- 役割: システム設定が必要なとき、その案内文を返す。無ければ undefined
- 触るとき: OS 側の位置情報設定を案内する文言を変えるとき
- 呼び出し先: `lazy.gBrandBundle.GetStringFromName()`
- 条件付き依存: `if (this.systemPermissionMsg == "sysdlg")` → `lazy.gBrowserBundle.formatStringFromName()`
- 条件付き依存: `if (this.systemPermissionMsg == "syssetting")` → `lazy.gBrowserBundle.formatStringFromName()`
- 参照: `this.systemPermissionMsg`

## GeolocationPermissionPrompt.promptActions()
- 位置: L962-979
- 役割: 許可と拒否の 2 つの選択肢を返す
- 触るとき: 位置情報の許可・拒否の選択肢の文言や割り当てを変えるとき
- 呼び出し先: `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.BLOCK`

## GeolocationPermissionPrompt.#updateGeoSharing()
- 位置: L981-1004
- 役割: タブの位置情報共有の状態を更新し、タブの現在のホストに最終アクセス時刻を Content Pref で保存する
- 触るとき: 位置情報の共有アイコンや最終アクセス記録が更新されない問題を調べるとき。ホストが無ければ時刻は保存しない
- 呼び出し先: `gBrowser.updateBrowserSharing()`, `lazy.ContentPrefService2.set()`, `new Date().toString()`
- 参照: `this.browser`, `this.browser.currentURI.host`, `this.browser.documentGlobal.gBrowser`, `this.browser.loadContext`

## GeolocationPermissionPrompt.allow()
- 位置: L1006-1009
- 役割: 位置情報の共有を true にしてから、親の allow を呼ぶ
- 触るとき: 位置情報の許可時に追加で行う処理を書くとき
- 呼び出し先: `super.allow()`, `this.#updateGeoSharing()`

## GeolocationPermissionPrompt.cancel()
- 位置: L1011-1014
- 役割: 位置情報の共有を false にしてから、親の cancel を呼ぶ
- 触るとき: 位置情報の拒否時に共有表示を戻す処理を調べるとき
- 呼び出し先: `super.cancel()`, `this.#updateGeoSharing()`

## GeolocationPermissionPrompt.ignoreAllowSitePermission()
- 位置: L1016-1018
- 役割: 要求の ignoreAllowSitePermission の値を返す
- 触るとき: 許可済みのサイトでも通知を出すべき要求を判定する条件を調べるとき。prompt() の自動許可を抑える
- 参照: `this.request.ignoreAllowSitePermission`

## XRPermissionPrompt.constructor()
- 位置: L1029-1032
- 役割: 要求を保持する
- 触るとき: WebXR の要求の初期化内容を変えるとき
- 呼び出し先: `super()`
- 参照: `this.request`

## XRPermissionPrompt.type()
- 位置: L1034-1036
- 役割: 権限種別として xr を返す
- 触るとき: WebXR の権限種別を変えるとき

## XRPermissionPrompt.permissionKey()
- 位置: L1038-1040
- 役割: 権限 DB の鍵として xr を返す
- 触るとき: WebXR の許可状態を保存・照会する鍵を変えるとき

## XRPermissionPrompt.popupOptions()
- 位置: L1042-1063
- 役割: 詳細リンクと表示 URI の非表示を設定し、PB 以外なら記憶チェックを付ける
- 触るとき: WebXR の通知の記憶チェックや詳細リンクを変えるとき
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.getPrincipalName()`
- 条件付き依存: `if (options.checkbox.show)` → `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `options.checkbox`, `options.checkbox.label`, `options.checkbox.show`, `this.browser.documentGlobal`
- XPCOM: `Services.urlFormatter`

## XRPermissionPrompt.notificationID()
- 位置: L1065-1067
- 役割: 通知 ID として xr を返す
- 触るとき: WebXR の通知 ID を変えるとき

## XRPermissionPrompt.anchorID()
- 位置: L1069-1071
- 役割: 通知を付けるアイコンとして xr-notification-icon を返す
- 触るとき: WebXR の通知の付け先を変えるとき

## XRPermissionPrompt.message()
- 位置: L1073-1081
- 役割: file スキームなら file 用、それ以外はサイト用の文言を返す
- 触るとき: WebXR の通知文を変えるとき
- 呼び出し先: `lazy.gBrowserBundle.formatStringFromName()`, `this.principal.schemeIs()`
- 条件付き依存: `if (this.principal.schemeIs("file"))` → `lazy.gBrowserBundle.GetStringFromName()`

## XRPermissionPrompt.promptActions()
- 位置: L1083-1096
- 役割: 許可と拒否の 2 つの選択肢を返す
- 触るとき: WebXR の許可・拒否の選択肢を変えるとき
- 呼び出し先: `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.BLOCK`

## XRPermissionPrompt.#updateXRSharing()
- 位置: L1098-1111
- 役割: タブの XR 共有の状態を更新し、デバイス権限の起点 origin を追加か削除する
- 触るとき: XR のデバイス権限の一覧が正しく更新されない問題を調べるとき
- 呼び出し先: `devicePermOrigins.add()`, `gBrowser.updateBrowserSharing()`, `this.browser.getDevicePermissionOrigins()`
- 条件付き依存: `if (!state)` → `devicePermOrigins.delete()`
- 参照: `this.browser`, `this.browser.documentGlobal.gBrowser`, `this.principal.origin`

## XRPermissionPrompt.allow()
- 位置: L1113-1116
- 役割: XR 共有を true にしてから、親の allow を呼ぶ
- 触るとき: WebXR の許可時の追加処理を書くとき
- 呼び出し先: `super.allow()`, `this.#updateXRSharing()`

## XRPermissionPrompt.cancel()
- 位置: L1118-1121
- 役割: XR 共有を false にしてから、親の cancel を呼ぶ
- 触るとき: WebXR の拒否時の共有表示の戻しを調べるとき
- 呼び出し先: `super.cancel()`, `this.#updateXRSharing()`

## LNAPermissionPromptBase.constructor()
- 位置: L1136-1139
- 役割: 要求を保持する。タイムアウト用のタイマーは未設定のまま始める
- 触るとき: ローカルネットワークアクセスの要求を初期化する内容を変えるとき
- 呼び出し先: `super()`
- 参照: `this.request`

## LNAPermissionPromptBase.onBeforeShow()
- 位置: L1141-1148
- 役割: 要求に notifyShown があれば呼んで表示を知らせ、テレメトリとネットワーク側へ伝える。常に true を返す
- 触るとき: LNA の表示時テレメトリや nsHttpChannel への通知を調べるとき
- 条件付き依存: `if (typeof this.request.notifyShown === "function")` → `this.request.notifyShown()`
- 参照: `this.request.notifyShown`

## LNAPermissionPromptBase.onShown()
- 位置: L1150-1152
- 役割: 表示されたら応答待ちのタイムアウトを開始する
- 触るとき: LNA 通知が出てから自動キャンセルまでの時間の扱いを変えるとき
- 呼び出し先: `this.#startTimeoutTimer()`

## LNAPermissionPromptBase.onAfterShow()
- 位置: L1154-1156
- 役割: 通知が閉じられたらタイムアウトのタイマーを止める
- 触るとき: LNA 通知を閉じた後にタイマーが残って誤って拒否される問題を調べるとき
- 呼び出し先: `this.#clearTimeoutTimer()`

## LNAPermissionPromptBase.cancel()
- 位置: L1158-1160
- 役割: 親の cancel をそのまま呼ぶ
- 触るとき: LNA 専用の拒否処理を足すとき。今は親の処理をそのまま使っている
- 呼び出し先: `super.cancel()`

## LNAPermissionPromptBase.allow()
- 位置: L1162-1164
- 役割: 親の allow をそのまま呼ぶ
- 触るとき: LNA 専用の許可処理を足すとき。今は親の処理をそのまま使っている
- 呼び出し先: `super.allow()`

## LNAPermissionPromptBase.temporaryPermissionExpireTimeMS()
- 位置: L1166-1169
- 役割: LNA の一時権限の期限として network.lna.temporary_permission_expire_time_ms の値を返す。既定は 24 時間
- 触るとき: LNA の一時許可がどれだけ続くかを変えるとき
- 参照: `lazy.lnaTemporaryPermissionExpireTimeMs`

## LNAPermissionPromptBase.#startTimeoutTimer()
- 位置: L1171-1192
- 役割: 既存のタイマーを止めてから、network.lna.prompt.timeout(既定 300 秒)後に警告をコンソールへ出し、通知を消して拒否する
- 触るとき: 利用者が応答しないときの自動拒否の時間や文言を変えるとき
- 呼び出し先: `Cc["@mozilla.org/scripterror;1"].createInstance()`, `Services.console.logMessage()`, `lazy.setTimeout()`, `scriptError.initWithWindowID()`, `this.#clearTimeoutTimer()`, `this.#removePrompt()`, `this.cancel()`
- 参照: `Ci.nsIScriptError`, `Ci.nsIScriptError.warningFlag`, `lazy.lnaPromptTimeoutMs`, `this.#timeoutTimer`, `this.browser.browsingContext.currentWindowGlobal.innerWindowId`
- XPCOM: [`nsIScriptError`](../../dom/bindings/nsIScriptError.idl.md) / `@mozilla.org/scripterror;1` / `Services.console`

## LNAPermissionPromptBase.#removePrompt()
- 位置: L1194-1203
- 役割: 同じ通知 ID の通知を、その browser の PopupNotifications から取り除く
- 触るとき: タイムアウトで通知を消す経路が効かない問題を調べるとき
- 呼び出し先: `chromeWin?.PopupNotifications.getNotification()`
- 条件付き依存: `if (notification)` → `chromeWin.PopupNotifications.remove()`
- 参照: `this.browser`, `this.browser?.documentGlobal`, `this.notificationID`

## LNAPermissionPromptBase.#clearTimeoutTimer()
- 位置: L1205-1210
- 役割: タイムアウトのタイマーがあれば止めて参照を空にする
- 触るとき: 通知を閉じた後や再表示時にタイマーが二重に動く問題を調べるとき
- 条件付き依存: `if (this.#timeoutTimer)` → `lazy.clearTimeout()`
- 参照: `this.#timeoutTimer`

## LoopbackNetworkPermissionPrompt.type()
- 位置: L1221-1223
- 役割: 権限種別として loopback-network を返す
- 触るとき: ループバック(localhost)へのアクセス権限の種別を変えるとき

## LoopbackNetworkPermissionPrompt.permissionKey()
- 位置: L1225-1227
- 役割: 権限 DB の鍵として loopback-network を返す
- 触るとき: localhost アクセスの許可状態を保存・照会する鍵を変えるとき

## LoopbackNetworkPermissionPrompt.popupOptions()
- 位置: L1229-1252
- 役割: 詳細リンクと表示 URI の非表示を設定し、PB 以外なら記憶チェックを付ける
- 触るとき: localhost アクセスの通知の記憶チェックや詳細リンクを変えるとき
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.getPrincipalName()`
- 条件付き依存: `if (options.checkbox.show)` → `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `options.checkbox`, `options.checkbox.label`, `options.checkbox.show`, `this.browser.documentGlobal`
- XPCOM: `Services.urlFormatter`

## LoopbackNetworkPermissionPrompt.notificationID()
- 位置: L1254-1256
- 役割: 通知 ID として loopback-network を返す
- 触るとき: localhost アクセスの通知 ID を変えるとき

## LoopbackNetworkPermissionPrompt.anchorID()
- 位置: L1258-1260
- 役割: 通知を付けるアイコンとして loopback-network-notification-icon を返す
- 触るとき: localhost アクセスの通知の付け先を変えるとき

## LoopbackNetworkPermissionPrompt.message()
- 位置: L1262-1267
- 役割: サイトのローカルホストへのアクセスを許可するかを尋ねる文言を返す
- 触るとき: localhost アクセスの通知文を変えるとき
- 呼び出し先: `lazy.gBrowserBundle.formatStringFromName()`

## LoopbackNetworkPermissionPrompt.promptActions()
- 位置: L1269-1286
- 役割: 許可と拒否の 2 つの選択肢を返す
- 触るとき: localhost アクセスの許可・拒否の選択肢を変えるとき
- 呼び出し先: `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.BLOCK`

## DesktopNotificationPermissionPrompt.constructor()
- 位置: L1304-1318
- 役割: 要求を保持し、requiresUserInput と postPromptEnabled を pref から遅延取得するように設定する
- 触るとき: 通知権限で user gesture 必須や後から出す通知の有効化を pref で切り替えるとき
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `super()`
- 参照: `this.request`

## DesktopNotificationPermissionPrompt.type()
- 位置: L1320-1322
- 役割: 権限種別として desktop-notification を返す
- 触るとき: デスクトップ通知の権限種別を変えるとき

## DesktopNotificationPermissionPrompt.permissionKey()
- 位置: L1324-1326
- 役割: 権限 DB の鍵として desktop-notification を返す
- 触るとき: デスクトップ通知の許可状態の保存先を変えるとき

## DesktopNotificationPermissionPrompt.#resolveL10n()
- 位置: L1337-1357
- 役割: Fluent の ID を同期的に解決して値と accesskey を返す。解決できなければ null を返し、例外はコンソールに出す
- 触るとき: Nimbus の文言を Fluent ID で指定したときに解決結果を確認するとき
- 呼び出し先: `console.error()`, `lazy.gFluentStrings.formatMessagesSync()`, `message.attributes?.find()`
- 参照: `attr.name`, `message.attributes?.find( attr => attr.name === "accesskey" )?.value`, `message.value`

## DesktopNotificationPermissionPrompt.#applyTreatmentLabels()
- 位置: L1373-1406
- 役割: Nimbus の処方(treatment)で許可と拒否のボタン文言を差し替える。動作や保存範囲は変えず、PB では拒否の文言を既定のままにする
- 触るとき: 実験の文言で通知ボタンの見た目を変えるとき。PB の拒否文言が既定のままになる条件を確認する
- 呼び出し先: `lazy.PrivateBrowsingUtils.isBrowserPrivate()`, `this.#resolveL10n()`
- 参照: `allowAction.accessKey`, `allowAction.label`, `blockAction.accessKey`, `blockAction.label`, `primary.accessKey`, `primary.value`, `secondary.accessKey`, `secondary.value`, `t.primaryCtaAccessKey`, `t.primaryCtaLabel`, `t.primaryCtaLabelL10nId`, `t.secondaryCtaAccessKey`, `t.secondaryCtaLabel`, `t.secondaryCtaLabelL10nId`, `this.#treatment`, `this.browser`

## DesktopNotificationPermissionPrompt.popupOptions()
- 位置: L1408-1420
- 役割: サポートページの push 向け URL と表示 URI の非表示を設定し、treatment の logoUrl をアイコンに使う
- 触るとき: デスクトップ通知の詳細リンクやアイコンを変えるとき。不正な logoUrl は null となり既定アイコンになる
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `this.getPrincipalName()`
- 参照: `this.#treatment?.logoUrl`
- XPCOM: `Services.urlFormatter`

## DesktopNotificationPermissionPrompt.notificationID()
- 位置: L1422-1424
- 役割: 通知 ID として web-notifications を返す
- 触るとき: デスクトップ通知の通知 ID を変えるとき

## DesktopNotificationPermissionPrompt.anchorID()
- 位置: L1426-1428
- 役割: 通知を付けるアイコンとして web-notifications-notification-icon を返す
- 触るとき: デスクトップ通知の付け先アイコンを変えるとき

## DesktopNotificationPermissionPrompt.message()
- 位置: L1430-1451
- 役割: 見出しを返す。Nimbus の見出しに <> が無ければ既定文言を使う。<> は要求元のサイト名に置き換わる
- 触るとき: デスクトップ通知の見出しを変えるとき。サイト名が無い同意文を出さないため、<> を必ず含める
- 呼び出し先: `candidate?.includes()`, `lazy.gBrowserBundle.formatStringFromName()`, `this.#resolveL10n()`
- 参照: `resolved?.value`, `this.#treatment?.headline`, `this.#treatment?.headlineL10nId`

## DesktopNotificationPermissionPrompt.hintText()
- 位置: L1453-1459
- 役割: Nimbus の本文(Fluent ID 優先、次に生の文字列)を返す。無ければ undefined
- 触るとき: デスクトップ通知の補足本文を実験で差し替えるとき
- 呼び出し先: `this.#resolveL10n()`
- 参照: `this.#resolveL10n(this.#treatment?.bodyL10nId)?.value`, `this.#treatment?.body`, `this.#treatment?.bodyL10nId`

## DesktopNotificationPermissionPrompt.promptActions()
- 位置: L1461-1513
- 役割: 許可(永続)と拒否の選択肢を作る。PB では拒否をセッション範囲にし、いずれも記録のコールバックを付けてから treatment で文言を差し替える
- 触るとき: 通知の許可・拒否ボタンの動作や保存範囲、テレメトリを変えるとき。拒否の文言は通常と PB で異なる
- 呼び出し先: `actions.push()`, `lazy.PrivateBrowsingUtils.isBrowserPrivate()`, `lazy.SiteCategory.getCategory()`, `lazy.gBrowserBundle.GetStringFromName()`, `this.#applyTreatmentLabels()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.BLOCK`, `lazy.SitePermissions.SCOPE_PERSISTENT`, `lazy.SitePermissions.SCOPE_SESSION`, `this.browser`, `this.principal`

## callback()
- 位置: L1472-1478
- 役割: 許可の選択を webNotificationPermission.promptInteraction に記録する
- 触るとき: 通知の許可操作のテレメトリを変えるとき
- 呼び出し先: `Glean.webNotificationPermission.promptInteraction.record()`

## callback()
- 位置: L1500-1506
- 役割: 拒否の選択を webNotificationPermission.promptInteraction に記録する
- 触るとき: 通知の拒否操作のテレメトリを変えるとき
- 呼び出し先: `Glean.webNotificationPermission.promptInteraction.record()`

## DesktopNotificationPermissionPrompt.postPromptActions()
- 位置: L1515-1563
- 役割: 後から出す通知の許可と拒否の選択肢を作る。どちらも永続で保存し、treatment で文言を差し替える
- 触るとき: 自動拒否後の通知ボタンを変えるとき。通常の通知と違い、拒否の保存範囲は指定しない
- 呼び出し先: `actions.push()`, `lazy.PrivateBrowsingUtils.isBrowserPrivate()`, `lazy.SiteCategory.getCategory()`, `lazy.gBrowserBundle.GetStringFromName()`, `this.#applyTreatmentLabels()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.BLOCK`, `this.browser`, `this.principal`

## callback()
- 位置: L1525-1531
- 役割: 後から出す通知の許可の選択を記録する
- 触るとき: 後から出す通知の許可操作のテレメトリを変えるとき
- 呼び出し先: `Glean.webNotificationPermission.promptInteraction.record()`

## callback()
- 位置: L1550-1556
- 役割: 後から出す通知の拒否の選択を記録する
- 触るとき: 後から出す通知の拒否操作のテレメトリを変えるとき
- 呼び出し先: `Glean.webNotificationPermission.promptInteraction.record()`

## DesktopNotificationPermissionPrompt.#resolveTreatment()
- 位置: async L1581-1622
- 役割: Nimbus の実験や rollout に入っていて表示条件を満たす利用者だけ、露出対象とし、内容があれば処方を保存する。失敗や対象外なら既定の通知になる
- 触るとき: デスクトップ通知の Nimbus 実験の対象判定や露出記録の条件を変えるとき。対照群では内容が無いので既定の通知を出す
- 呼び出し先: `feature.getAllVariables()`, `feature.getEnrollmentMetadata()`, `lazy.SiteCategory.getCategory()`, `lazy.evalPermissionPromptTargeting()`
- 条件付き依存: `if (hasContent)` → `this.#resolveLogoUrl()`
- 参照: `lazy.NimbusFeatures`, `lazy.PERMISSION_UI_FEATURE_ID`, `this.#exposureQualified`, `this.#treatment`, `this.principal`, `vars.activationTargeting`, `vars.body`, `vars.bodyL10nId`, `vars.headline`, `vars.headlineL10nId`, `vars.logoUrl`, `vars.primaryCtaLabel`, `vars.primaryCtaLabelL10nId`, `vars.secondaryCtaLabel`, `vars.secondaryCtaLabelL10nId`, `vars.useSiteFavicon`

## DesktopNotificationPermissionPrompt.#resolveLogoUrl()
- 位置: async L1639-1672
- 役割: 有効な logoUrl があればそれを、useSiteFavicon なら保存済みの page-icon かタブの同一オリジンのアイコンを、どれも無ければ null を返す
- 触るとき: 通知に出すアイコンの優先順位を変えるとき。リモートの URL は取らず、別オリジンのアイコンは使わない
- 呼び出し先: `lazy.PlacesUtils.favicons .getFaviconForPage()`, `lazy.PlacesUtils.favicons .getFaviconForPage(pageURI) .catch()`, `lazy.isValidLogoUrl()`, `this.browser.contentPrincipal.equals()`
- 参照: `pageURI.spec`, `this.browser.mIconURL`, `this.principal`, `this.principal.URI`, `vars.logoUrl`, `vars.useSiteFavicon`

## DesktopNotificationPermissionPrompt.onBeforeShowAsync()
- 位置: async L1682-1690
- 役割: 処方の解決を行い、失敗時は既定の通知に戻す。例外は外へ投げない
- 触るとき: 表示前の非同期処理で実験の処方が効かない問題を調べるとき
- 呼び出し先: `console.error()`, `this.#resolveTreatment()`
- 参照: `this.#exposureQualified`, `this.#treatment`

## DesktopNotificationPermissionPrompt.prompt()
- 位置: L1692-1718
- 役割: requiresUserInput が有効でユーザー操作が無い場合にテレメトリを記録し、親の prompt を呼ぶ
- 触るとき: ユーザー操作の無い通知要求の遮断理由を計測するとき
- 呼び出し先: `lazy.SiteCategory.getCategory()`, `super.prompt()`
- 条件付き依存: `if ( this.requiresUserInput && !this.request.hasValidTransientUserGestureActivation )` → `Glean.webNotificationPermission.promptBlocked.record()`
- 参照: `this.principal`, `this.request.hasValidTransientUserGestureActivation`, `this.requiresUserInput`

## DesktopNotificationPermissionPrompt.postPrompt()
- 位置: L1720-1732
- 役割: 後から出す通知のアイコン表示をテレメトリに記録し、露出対象なら露出を記録してから親の postPrompt を呼ぶ
- 触るとき: 後から出す通知の表示計測や Nimbus の露出記録を変えるとき
- 呼び出し先: `Glean.webNotificationPermission.iconShown.record()`, `lazy.SiteCategory.getCategory()`, `super.postPrompt()`
- 条件付き依存: `if (this.#exposureQualified)` → `lazy.NimbusFeatures[lazy.PERMISSION_UI_FEATURE_ID].recordExposureEvent()`
- 参照: `lazy.NimbusFeatures`, `lazy.PERMISSION_UI_FEATURE_ID`, `this.#exposureQualified`, `this.principal`

## DesktopNotificationPermissionPrompt.onShown()
- 位置: L1734-1768
- 役割: 表示の契機(スクリプトかアイコンのクリックか)を判定して promptShown を記録し、露出対象なら once で露出を記録する
- 触るとき: 通知の表示計測や露出イベントの二重記録を調べるとき。タブ切り替えで再度表示されても露出は 1 回に抑える
- 呼び出し先: `Glean.webNotificationPermission.promptShown.record()`, `lazy.SiteCategory.getCategory()`
- 条件付き依存: `if ( this.requiresUserInput && !this.request.hasValidTransientUserGestureActivation )` → `Glean.webNotificationPermission.iconClicked.record()`
- 条件付き依存: `if ( this.requiresUserInput && !this.request.hasValidTransientUserGestureActivation )` → `lazy.SiteCategory.getCategory()`
- 条件付き依存: `if (this.#exposureQualified)` → `lazy.NimbusFeatures[lazy.PERMISSION_UI_FEATURE_ID].recordExposureEvent()`
- 参照: `lazy.NimbusFeatures`, `lazy.PERMISSION_UI_FEATURE_ID`, `this.#exposureQualified`, `this.principal`, `this.request.hasValidTransientUserGestureActivation`, `this.requiresUserInput`

## LocalNetworkPermissionPrompt.type()
- 位置: L1779-1781
- 役割: 権限種別として local-network を返す
- 触るとき: ローカルネットワークアクセスの権限種別を変えるとき

## LocalNetworkPermissionPrompt.permissionKey()
- 位置: L1783-1785
- 役割: 権限 DB の鍵として local-network を返す
- 触るとき: ローカルネットワークアクセスの許可状態の保存先を変えるとき

## LocalNetworkPermissionPrompt.popupOptions()
- 位置: L1787-1810
- 役割: 詳細リンクと表示 URI の非表示を設定し、PB 以外なら記憶チェックを付ける
- 触るとき: ローカルネットワークアクセスの通知の記憶チェックを変えるとき
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.getPrincipalName()`
- 条件付き依存: `if (options.checkbox.show)` → `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `options.checkbox`, `options.checkbox.label`, `options.checkbox.show`, `this.browser.documentGlobal`
- XPCOM: `Services.urlFormatter`

## LocalNetworkPermissionPrompt.notificationID()
- 位置: L1812-1814
- 役割: 通知 ID として local-network を返す
- 触るとき: ローカルネットワークアクセスの通知 ID を変えるとき

## LocalNetworkPermissionPrompt.anchorID()
- 位置: L1816-1818
- 役割: 通知を付けるアイコンとして local-network-notification-icon を返す
- 触るとき: ローカルネットワークアクセスの通知の付け先を変えるとき

## LocalNetworkPermissionPrompt.message()
- 位置: L1820-1825
- 役割: サイトのローカルネットワークへのアクセスを許可するかを尋ねる文言を返す
- 触るとき: ローカルネットワークアクセスの通知文を変えるとき
- 呼び出し先: `lazy.gBrowserBundle.formatStringFromName()`

## LocalNetworkPermissionPrompt.promptActions()
- 位置: L1827-1844
- 役割: ローカルネットワークアクセスの許可と拒否の 2 つの選択肢を返す
- 触るとき: ローカルネットワークアクセスの選択肢の文言や割り当てを変えるとき
- 呼び出し先: `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.BLOCK`

## PersistentStoragePermissionPrompt.constructor()
- 位置: L1854-1857
- 役割: 要求を保持する
- 触るとき: 永続ストレージの要求の初期化内容を変えるとき
- 呼び出し先: `super()`
- 参照: `this.request`

## PersistentStoragePermissionPrompt.type()
- 位置: L1859-1861
- 役割: 権限種別として persistent-storage を返す
- 触るとき: 永続ストレージの権限種別を変えるとき

## PersistentStoragePermissionPrompt.permissionKey()
- 位置: L1863-1865
- 役割: 権限 DB の鍵として persistent-storage を返す
- 触るとき: 永続ストレージの許可状態の保存先を変えるとき

## PersistentStoragePermissionPrompt.popupOptions()
- 位置: L1867-1890
- 役割: ストレージ権限の詳細リンクと表示 URI の非表示を設定し、PB 以外なら Fluent の記憶チェックを付ける
- 触るとき: 永続ストレージの通知の記憶チェックや詳細リンクを変えるとき
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.getPrincipalName()`
- 条件付き依存: `if (options.checkbox.show)` → `lazy.gFluentStrings.formatValueSync()`
- 参照: `options.checkbox`, `options.checkbox.label`, `options.checkbox.show`, `this.browser.documentGlobal`
- XPCOM: `Services.urlFormatter`

## PersistentStoragePermissionPrompt.notificationID()
- 位置: L1892-1894
- 役割: 通知 ID として persistent-storage を返す
- 触るとき: 永続ストレージの通知 ID を変えるとき

## PersistentStoragePermissionPrompt.anchorID()
- 位置: L1896-1898
- 役割: 通知を付けるアイコンとして persistent-storage-notification-icon を返す
- 触るとき: 永続ストレージの通知の付け先を変えるとき

## PersistentStoragePermissionPrompt.message()
- 位置: L1900-1905
- 役割: サイトが永続ストレージを使ってよいかを尋ねる文言を返す
- 触るとき: 永続ストレージの通知文を変えるとき
- 呼び出し先: `lazy.gBrowserBundle.formatStringFromName()`

## PersistentStoragePermissionPrompt.promptActions()
- 位置: L1907-1927
- 役割: 許可(永続で保存)と拒否の 2 つの選択肢を返す
- 触るとき: 永続ストレージの許可・拒否の選択肢や保存範囲を変えるとき
- 呼び出し先: `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `Ci.nsIPermissionManager.ALLOW_ACTION`, `lazy.SitePermissions.BLOCK`, `lazy.SitePermissions.SCOPE_PERSISTENT`
- XPCOM: [`nsIPermissionManager`](../../netwerk/base/nsIPermissionManager.idl.md)

## MIDIPermissionPrompt.constructor()
- 位置: L1938-1950
- 役割: 要求を保持し、最初の権限オプションが sysex なら権限名を midi-sysex、それ以外は midi にする
- 触るとき: WebMIDI の通常要求と SysEx 要求を区別する判定を変えるとき
- 呼び出し先: `perm.options.queryElementAt()`, `request.types.QueryInterface()`, `super()`, `types.queryElementAt()`
- 参照: `Ci.nsIArray`, `Ci.nsIContentPermissionType`, `Ci.nsISupportsString`, `perm.options.length`, `this.isSysexPerm`, `this.permName`, `this.request`
- XPCOM: [`nsIArray`](../../dom/events/nsIEventListenerService.idl.md) / [`nsIContentPermissionType`](../../dom/interfaces/base/nsIContentPermissionPrompt.idl.md) / [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md)

## MIDIPermissionPrompt.type()
- 位置: L1952-1954
- 役割: 権限種別として midi を返す
- 触るとき: WebMIDI の権限種別を変えるとき

## MIDIPermissionPrompt.permissionKey()
- 位置: L1956-1958
- 役割: 権限 DB の鍵として、通常は midi、SysEx なら midi-sysex を返す
- 触るとき: WebMIDI の許可状態を通常と SysEx で別々に保存する挙動を調べるとき
- 参照: `this.permName`

## MIDIPermissionPrompt.popupOptions()
- 位置: L1960-1980
- 役割: 表示 URI の非表示と名前を設定し、PB 以外なら記憶チェックを付ける。詳細リンクは未整備(TODO)
- 触るとき: WebMIDI の通知の記憶チェックや、詳細リンクを追加するとき
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.getPrincipalName()`
- 条件付き依存: `if (options.checkbox.show)` → `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `options.checkbox`, `options.checkbox.label`, `options.checkbox.show`, `this.browser.documentGlobal`

## MIDIPermissionPrompt.notificationID()
- 位置: L1982-1984
- 役割: 通知 ID として midi を返す
- 触るとき: WebMIDI の通知 ID を変えるとき

## MIDIPermissionPrompt.anchorID()
- 位置: L1986-1988
- 役割: 通知を付けるアイコンとして midi-notification-icon を返す
- 触るとき: WebMIDI の通知の付け先を変えるとき

## MIDIPermissionPrompt.message()
- 位置: L1990-2011
- 役割: file スキーム、SysEx、通常の 3 通りで文言を選んで返す
- 触るとき: WebMIDI の通知文や SysEx 用の文言を変えるとき
- 呼び出し先: `this.principal.schemeIs()`
- 条件付き依存: `if (this.isSysexPerm)` → `lazy.gBrowserBundle.GetStringFromName()`
- 条件付き依存: `if (!(this.isSysexPerm))` → `lazy.gBrowserBundle.GetStringFromName()`
- 条件付き依存: `if (this.isSysexPerm)` → `lazy.gBrowserBundle.formatStringFromName()`
- 条件付き依存: `if (!(this.isSysexPerm))` → `lazy.gBrowserBundle.formatStringFromName()`
- 参照: `this.isSysexPerm`

## MIDIPermissionPrompt.promptActions()
- 位置: L2013-2030
- 役割: 許可(ALLOW_ACTION)と拒否(DENY_ACTION)の 2 つの選択肢を返す
- 触るとき: WebMIDI の許可・拒否の選択肢を変えるとき
- 呼び出し先: `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `Ci.nsIPermissionManager.ALLOW_ACTION`, `Ci.nsIPermissionManager.DENY_ACTION`
- XPCOM: [`nsIPermissionManager`](../../netwerk/base/nsIPermissionManager.idl.md)

## MIDIPermissionPrompt.getInstallErrorMessage()
- 位置: L2037-2039
- 役割: アドオンのインストールが拒否された時のエラー文言(WebMIDI 用)を、元の例外メッセージ込みで返す
- 触るとき: WebMIDI でインストールが失敗したときのコンソールの文言を変えるとき
- 参照: `err.message`

## SerialPermissionPrompt.constructor()
- 位置: L2050-2054
- 役割: 要求を保持し、権限名を serial にする
- 触るとき: WebSerial の要求の初期化内容を変えるとき
- 呼び出し先: `super()`
- 参照: `this.permName`, `this.request`

## SerialPermissionPrompt.type()
- 位置: L2056-2058
- 役割: 権限種別として serial を返す
- 触るとき: WebSerial の権限種別を変えるとき

## SerialPermissionPrompt.permissionKey()
- 位置: L2060-2062
- 役割: 権限 DB の鍵として serial を返す
- 触るとき: WebSerial の許可状態の保存先を変えるとき
- 参照: `this.permName`

## SerialPermissionPrompt.popupOptions()
- 位置: L2064-2071
- 役割: 表示 URI の非表示と名前を設定し、記憶チェックを出さない
- 触るとき: WebSerial の通知オプションを変えるとき。記憶チェックは出さない仕様である点に注意する
- 呼び出し先: `this.getPrincipalName()`

## SerialPermissionPrompt._populateDeviceList()
- 位置: L2073-2127
- 役割: 要求のオプションから機器の一覧を作り、ポート選択のメニューに入れる。機器が無ければメニューを隠して許可ボタンを無効にする。自動選択フラグも読み取る
- 触るとき: WebSerial のポート選択 UI の表示内容や、機器が無いときの動作を変えるとき
- 呼び出し先: `JSON.parse()`, `document.createXULElement()`, `document.getElementById()`, `i.toString()`, `menuitem.setAttribute()`, `menupopup.appendChild()`, `menupopup.firstChild.remove()`, `options.queryElementAt()`, `perm.options.QueryInterface()`, `ports.push()`, `this._getDeviceDisplayName()`, `this.request.types.QueryInterface()`, `types.queryElementAt()`
- 条件付き依存: `if (!menulist || !menupopup || !noPortsMsg)` → `console.error()`
- 参照: `Ci.nsIArray`, `Ci.nsIContentPermissionType`, `Ci.nsISupportsString`, `menulist.hidden`, `menulist.selectedIndex`, `menupopup.firstChild`, `noPortsMsg.hidden`, `notification.browser.ownerDocument`, `notification.mainAction.disabled`, `options.length`, `options.queryElementAt(i, Ci.nsISupportsString).data`, `parsed.__autoselect__`, `ports.length`, `this._autoselect`
- XPCOM: [`nsIArray`](../../dom/events/nsIEventListenerService.idl.md) / [`nsIContentPermissionType`](../../dom/interfaces/base/nsIContentPermissionPrompt.idl.md) / [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md)

## SerialPermissionPrompt._getDeviceDisplayName()
- 位置: L2129-2145
- 役割: 機器名があればそれを、USB なら パス と 16 進の VID:PID を、無ければパスを返す
- 触るとき: WebSerial のポート一覧に出す機器の名前の形式を変えるとき
- 条件付き依存: `if (vid != null && pid != null && vid !== 0 && pid !== 0)` → `vid.toString(16).padStart()`
- 条件付き依存: `if (vid != null && pid != null && vid !== 0 && pid !== 0)` → `vid.toString()`
- 条件付き依存: `if (vid != null && pid != null && vid !== 0 && pid !== 0)` → `pid.toString(16).padStart()`
- 条件付き依存: `if (vid != null && pid != null && vid !== 0 && pid !== 0)` → `pid.toString()`
- 参照: `port.friendlyName`, `port.friendlyName?.length`, `port.path`, `port.usbProductId`, `port.usbVendorId`

## SerialPermissionPrompt.prompt()
- 位置: async L2147-2180
- 役割: localhost、file、またはアドオン提供者が無効ならポート選択を直接出す。許可済みか webserial 制限が無ければ同様に出し、そうでなければアドオンをインストールしてから出す。失敗なら拒否する
- 触るとき: WebSerial の要求がどの経路で通知に進むかを調べるとき
- 呼び出し先: `Services.perms.testPermissionFromPrincipal()`, `this._showDevicePicker()`, `this.cancel()`, `this.installSitePermAddon()`, `this.principal.schemeIs()`
- 条件付き依存: `if ( this.principal.isLoopbackHost || this.principal.schemeIs("file") || !lazy.sitePermsAddonsProviderEnabled )` → `this._showDevicePicker()`
- 条件付き依存: `if (hasAddon || !lazy.webserialGated)` → `this._showDevicePicker()`
- 参照: `Services.perms.ALLOW_ACTION`, `lazy.sitePermsAddonsProviderEnabled`, `lazy.webserialGated`, `this.permName`, `this.principal`, `this.principal.isLoopbackHost`
- XPCOM: `Services.perms`

## SerialPermissionPrompt._showDevicePicker()
- 位置: L2182-2275
- 役割: 許可と拒否の選択肢を持つポート選択の通知を出す。例外時は拒否する
- 触るとき: WebSerial のポート選択通知の選択肢や閉じ方を変えるとき
- 呼び出し先: `chromeWin.PopupNotifications.show()`, `console.error()`, `lazy.gBrowserBundle.GetStringFromName()`, `this.cancel()`, `this.getPrincipalName()`
- 参照: `this.anchorID`, `this.browser`, `this.browser.documentGlobal`, `this.message`, `this.notificationID`

## callback()
- 位置: L2190-2204
- 役割: メニューで選ばれた機器の番号を、serial の選択として許可する
- 触るとき: WebSerial で選んだポートが許可に渡らない問題を調べるとき
- 呼び出し先: `document.getElementById()`, `selectedIndex.toString()`, `this.allow()`
- 参照: `menulist.selectedIndex`, `this.browser.ownerDocument`

## callback()
- 位置: L2212-2214
- 役割: 拒否の選択で要求を拒否する
- 触るとき: WebSerial の拒否操作の後処理を変えるとき
- 呼び出し先: `this.cancel()`

## SerialPermissionPrompt.eventCallback()
- 位置: L2225-2258
- 役割: 通知が表示されたら機器一覧を作り、自動選択なら 100 ミリ秒後に許可か拒否を自動で実行する。通知が閉じられたら要求を拒否する
- 触るとき: WebSerial の自動選択(テスト用)や、閉じたときに要求が残る問題を調べるとき
- 条件付き依存: `if (topic === "showing")` → `promptInstance._populateDeviceList()`
- 条件付き依存: `if (promptInstance._autoselect)` → `lazy.setTimeout()`
- 条件付き依存: `if (promptInstance._autoselect)` → `document.getElementById()`
- 条件付き依存: `if (menulist && menulist.itemCount > 0)` → `selectAction.callback()`
- 条件付き依存: `if (!(menulist && menulist.itemCount > 0))` → `cancelAction.callback()`
- 条件付き依存: `if (promptInstance._autoselect)` → `notification.remove()`
- 条件付き依存: `if (topic === "showing")` → `console.error()`
- 条件付き依存: `if (topic === "removed")` → `promptInstance.cancel()`
- 参照: `menulist.itemCount`, `promptInstance._autoselect`, `promptInstance.browser.ownerDocument`

## SerialPermissionPrompt.notificationID()
- 位置: L2277-2279
- 役割: 通知 ID として webSerial-choosePort を返す
- 触るとき: WebSerial のポート選択通知 ID を変えるとき

## SerialPermissionPrompt.anchorID()
- 位置: L2281-2283
- 役割: 通知を付けるアイコンとして serial-notification-icon を返す
- 触るとき: WebSerial の通知の付け先を変えるとき

## SerialPermissionPrompt.message()
- 位置: L2285-2296
- 役割: file スキームなら file 用、それ以外はサイト用の文言を返す
- 触るとき: WebSerial の通知文を変えるとき
- 呼び出し先: `this.principal.schemeIs()`
- 条件付き依存: `if (this.principal.schemeIs("file"))` → `lazy.gBrowserBundle.GetStringFromName()`
- 条件付き依存: `if (!(this.principal.schemeIs("file")))` → `lazy.gBrowserBundle.formatStringFromName()`

## SerialPermissionPrompt.getInstallErrorMessage()
- 位置: L2303-2305
- 役割: アドオンのインストールが拒否された時のエラー文言(WebSerial 用)を、元の例外メッセージ込みで返す
- 触るとき: WebSerial でインストールが失敗したときのコンソールの文言を変えるとき
- 参照: `err.message`

## StorageAccessPermissionPrompt.constructor()
- 位置: L2311-2337
- 役割: 要求を保持し、3rd パーティのストレージの鍵を作る。オプションが 2 つあれば、トップレベルの URL を siteOption に入れ、フレーム側の指定があれば鍵をフレーム用に変える
- 触るとき: サードパーティの Cookie やストレージアクセスの要求の鍵(誰を対象に保存するか)を変えるとき
- 呼び出し先: `options.queryElementAt()`, `perm.options.QueryInterface()`, `super()`, `this.request.types.QueryInterface()`, `types.queryElementAt()`
- 参照: `Ci.nsIArray`, `Ci.nsIContentPermissionType`, `Ci.nsISupportsString`, `lazy.SitePermissions.PERM_KEY_DELIMITER`, `options.length`, `options.queryElementAt(0, Ci.nsISupportsString).data`, `options.queryElementAt(1, Ci.nsISupportsString).data`, `this.#permissionKey`, `this.principal.origin`, `this.principal.siteOrigin`, `this.request`, `this.siteOption`
- XPCOM: [`nsIArray`](../../dom/events/nsIEventListenerService.idl.md) / [`nsIContentPermissionType`](../../dom/interfaces/base/nsIContentPermissionPrompt.idl.md) / [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md)

## StorageAccessPermissionPrompt.usePermissionManager()
- 位置: L2339-2341
- 役割: false を返し、権限 DB を使わず一時権限だけ扱う
- 触るとき: ストレージアクセスの許可を永続化しない仕様を変えるとき

## StorageAccessPermissionPrompt.type()
- 位置: L2343-2345
- 役割: 権限種別として storage-access を返す
- 触るとき: ストレージアクセスの権限種別を変えるとき

## StorageAccessPermissionPrompt.permissionKey()
- 位置: L2347-2350
- 役割: 構築時に決めた鍵を返す。第三者の追跡者ごとに一意になる
- 触るとき: ストレージアクセスの一時権限の鍵が衝突する問題を調べるとき
- 参照: `this.#permissionKey`

## StorageAccessPermissionPrompt.temporaryPermissionURI()
- 位置: L2352-2357
- 役割: siteOption があればそれを URI にして返し、無ければ undefined を返す
- 触るとき: 一時権限の対象サイトを、フレームの要求でどう決めるかを変えるとき
- 条件付き依存: `if (this.siteOption)` → `Services.io.newURI()`
- 参照: `this.siteOption`
- XPCOM: `Services.io`

## StorageAccessPermissionPrompt.prettifyHostPort()
- 位置: L2359-2366
- 役割: ホスト名を表示用の IDN に変換し、ポートがあれば付けて返す
- 触るとき: 通知文に出すホスト名の表示形式を変えるとき
- 呼び出し先: `hostport.split()`, `lazy.IDNService.convertToDisplayIDN()`

## StorageAccessPermissionPrompt.popupOptions()
- 位置: L2368-2383
- 役割: サードパーティ Cookie の詳細リンク、表示 URI の非表示、要求元ホストを入れた補足文、Esc で二番目のボタンを押す設定を返す
- 触るとき: ストレージアクセス通知の補足文や Esc の動作を変えるとき
- 呼び出し先: `Services.urlFormatter.formatURLPref()`, `lazy.gBrowserBundle.formatStringFromName()`, `this.prettifyHostPort()`
- 参照: `this.principal.hostPort`
- XPCOM: `Services.urlFormatter`

## StorageAccessPermissionPrompt.notificationID()
- 位置: L2385-2387
- 役割: 通知 ID として storage-access を返す
- 触るとき: ストレージアクセスの通知 ID を変えるとき

## StorageAccessPermissionPrompt.anchorID()
- 位置: L2389-2391
- 役割: 通知を付けるアイコンとして storage-access-notification-icon を返す
- 触るとき: ストレージアクセスの通知の付け先を変えるとき

## StorageAccessPermissionPrompt.message()
- 位置: L2393-2404
- 役割: 要求元ホストと埋め込み元ホストを入れた通知文を返す。埋め込み元は siteOption があればそのホスト、無ければトップレベルのホスト
- 触るとき: ストレージアクセスの通知文で、どのサイトが誰に対して許可を求めるかを変えるとき
- 呼び出し先: `lazy.gBrowserBundle.formatStringFromName()`, `this.prettifyHostPort()`
- 条件付き依存: `if (this.siteOption)` → `this.siteOption.split("://").at()`
- 条件付き依存: `if (this.siteOption)` → `this.siteOption.split()`
- 参照: `this.principal.hostPort`, `this.siteOption`, `this.topLevelPrincipal.host`

## StorageAccessPermissionPrompt.promptActions()
- 位置: L2406-2435
- 役割: 許可(ALLOW_ACTION)は allow に storage-access: allow を渡し、拒否(DENY_ACTION)は cancel を呼ぶ
- 触るとき: ストレージアクセスの選択肢の文言や、許可・拒否の応答を変えるとき
- 呼び出し先: `lazy.gBrowserBundle.GetStringFromName()`
- 参照: `Ci.nsIPermissionManager.ALLOW_ACTION`, `Ci.nsIPermissionManager.DENY_ACTION`
- XPCOM: [`nsIPermissionManager`](../../netwerk/base/nsIPermissionManager.idl.md)

## StorageAccessPermissionPrompt.callback()
- 位置: L2418-2420
- 役割: 許可の選択で allow({storage-access: allow}) を呼ぶ
- 触るとき: ストレージアクセスの許可の応答内容を変えるとき
- 呼び出し先: `self.allow()`

## StorageAccessPermissionPrompt.callback()
- 位置: L2430-2432
- 役割: 拒否の選択で cancel を呼ぶ
- 触るとき: ストレージアクセスの拒否の応答を変えるとき
- 呼び出し先: `self.cancel()`

## StorageAccessPermissionPrompt.topLevelPrincipal()
- 位置: L2437-2439
- 役割: 要求のトップレベル principal を返す
- 触るとき: 埋め込み元サイトを判定する値の出どころを確かめるとき
- 参照: `this.request.topLevelPrincipal`

## SpeechRecognitionModelDownloadPermissionPrompt.constructor()
- 位置: L2466-2476
- 役割: 要求を保持し、オプションの 1 番目からモデルのサイズ(MB)、2 番目から進捗を識別するトークンを読む
- 触るとき: 音声認識モデルのダウンロード要求で、サイズ表示や進捗の照合がずれる問題を調べるとき
- 呼び出し先: `perm.options.queryElementAt()`, `request.types.QueryInterface()`, `super()`, `types.queryElementAt()`
- 参照: `Ci.nsIArray`, `Ci.nsIContentPermissionType`, `Ci.nsISupportsString`, `perm.options.queryElementAt( 1, Ci.nsISupportsString ).data`, `perm.options.queryElementAt(0, Ci.nsISupportsString).data`, `this.#progressToken`, `this.#sizeMB`, `this.request`
- XPCOM: [`nsIArray`](../../dom/events/nsIEventListenerService.idl.md) / [`nsIContentPermissionType`](../../dom/interfaces/base/nsIContentPermissionPrompt.idl.md) / [`nsISupportsString`](../../xpcom/ds/nsISupportsPrimitives.idl.md)

## SpeechRecognitionModelDownloadPermissionPrompt.type()
- 位置: L2478-2480
- 役割: 権限種別として speech-recognition-model-download を返す
- 触るとき: 音声認識モデルの要求の種別名を変えるとき

## SpeechRecognitionModelDownloadPermissionPrompt.popupOptions()
- 位置: L2485-2490
- 役割: 表示 URI の非表示と記憶チェックなしを返す
- 触るとき: モデルダウンロードの通知オプションを変えるとき。同意は一度きりで保存されない

## SpeechRecognitionModelDownloadPermissionPrompt.notificationID()
- 位置: L2492-2494
- 役割: 通知 ID としてモデルダウンロード用の ID を返す
- 触るとき: モデルダウンロード通知の ID を変えるとき

## SpeechRecognitionModelDownloadPermissionPrompt.anchorID()
- 位置: L2496-2498
- 役割: 通知を付けるアイコンとして default-notification-icon を返す
- 触るとき: モデルダウンロード通知の付け先を変えるとき

## SpeechRecognitionModelDownloadPermissionPrompt.message()
- 位置: L2500-2505
- 役割: Fluent の文言に、モデルのサイズ(MB)を入れて返す
- 触るとき: ダウンロードの同意文でサイズ表示を変えるとき
- 呼び出し先: `lazy.gFluentStrings.formatValueSync()`
- 参照: `this.#sizeMB`

## SpeechRecognitionModelDownloadPermissionPrompt.promptActions()
- 位置: L2507-2544
- 役割: Fluent から同意・後で・キャンセル・OK の文言を読み、同意(ALLOW)では進捗表示を出して許可し、後でを選ぶと拒否する選択肢を返す
- 触るとき: ダウンロード同意ボタンの文言や、同意後に進捗表示へ移る流れを変えるとき。キャンセルと OK の文言は後の進捗表示で使うため保持する
- 呼び出し先: `lazy.gFluentStrings .formatMessagesSync()`, `msg.attributes.reduce()`
- 参照: `allowMessage.accesskey`, `allowMessage.label`, `lazy.SitePermissions.ALLOW`, `lazy.SitePermissions.BLOCK`, `notNowMessage.accesskey`, `notNowMessage.label`, `this.#cancelMessage`, `this.#okMessage`

## callback()
- 位置: L2530-2533
- 役割: 同意ボタンが押されたら進捗表示を出し、そのあと許可する
- 触るとき: 同意ボタン押下後に進捗表示が出ない問題を調べるとき
- 呼び出し先: `this.#showProgress()`, `this.allow()`

## callback()
- 位置: L2539-2541
- 役割: 後で(拒否)ボタンが押されたら要求を拒否する
- 触るとき: 後でボタンの挙動を変えるとき
- 呼び出し先: `this.cancel()`

## SpeechRecognitionModelDownloadPermissionPrompt.allow()
- 位置: L2546-2552
- 役割: 要求が未決のときだけ親の allow を呼び、一度決まったら再度の応答を無視する
- 触るとき: 同意の二重応答を防ぐ条件を変えるとき
- 呼び出し先: `super.allow()`
- 参照: `this.#requestSettled`

## SpeechRecognitionModelDownloadPermissionPrompt.cancel()
- 位置: L2554-2560
- 役割: 要求が未決のときだけ親の cancel を呼び、一度決まったら再度の応答を無視する
- 触るとき: 拒否の二重応答を防ぐ条件を変えるとき
- 呼び出し先: `super.cancel()`
- 参照: `this.#requestSettled`

## SpeechRecognitionModelDownloadPermissionPrompt.observe()
- 位置: L2562-2582
- 役割: 進捗のトピックのうち自分のトークンに一致するものだけを取り出し、サイズ、進捗、完了、成否を更新に渡す
- 触るとき: 同時に走る他のモデルのダウンロードを取り違えないよう、トークンの照合を変えるとき
- 呼び出し先: `props.getPropertyAsAString()`, `props.getPropertyAsBool()`, `props.getPropertyAsInt32()`, `props.getPropertyAsInt64()`, `subject.QueryInterface()`, `this.#updateProgress()`
- 参照: `Ci.nsIPropertyBag2`, `this.#progressToken`
- XPCOM: [`nsIPropertyBag2`](../../toolkit/components/autocomplete/nsIAutoCompleteSearch.idl.md)

## SpeechRecognitionModelDownloadPermissionPrompt.#notificationElement()
- 位置: L2588-2595
- 役割: 進捗用の popupnotification 要素を、通知のブラウザのドキュメントから探して返す。無ければ null
- 触るとき: 進捗表示の DOM 要素が見つからず更新されない問題を調べるとき
- 呼び出し先: `browser?.documentGlobal?.document.getElementById()`
- 参照: `this.#notification?.browser`

## SpeechRecognitionModelDownloadPermissionPrompt.#showProgress()
- 位置: L2597-2656
- 役割: 進捗表示の通知を出し(主ボタンは無効、キャンセルはダウンロードを止める)、状態を初期化して進捗トピックの監視を始める
- 触るとき: ダウンロード中の進捗表示やキャンセルの動作を変えるとき
- 呼び出し先: `ChromeUtils.now()`, `Services.obs.addObserver()`, `lazy.gFluentStrings.formatValueSync()`, `popupNotifications.show()`, `this.#applyProgressUI()`, `this.#resetProgressUI()`, `this.#updateProgress()`
- 参照: `allowMessage.accesskey`, `allowMessage.label`, `browser.documentGlobal.PopupNotifications`, `this.#cancelMessage.accesskey`, `this.#cancelMessage.label`, `this.#downloadStartedAt`, `this.#lastSec`, `this.#notification`, `this.#observingProgress`, `this.#renderedPercent`, `this.anchorID`, `this.browser`
- XPCOM: `Services.obs`

## callback()
- 位置: L2607-2607
- 役割: 進捗中の主ボタンは無効なので、何もしない
- 触るとき: 主ボタンに動作を持たせたいときに、この空の処理を置き換える

## callback()
- 位置: L2613-2619
- 役割: 監視中ならモデルハブのダウンロードをトークン指定で取り消す
- 触るとき: 進捗表示のキャンセルでダウンロードが止まらない問題を調べるとき
- 条件付き依存: `if (this.#observingProgress)` → `Cc["@mozilla.org/ml-modelhub;1"] .getService(Ci.nsIMLModelHub) .cancelDownload()`
- 条件付き依存: `if (this.#observingProgress)` → `Cc["@mozilla.org/ml-modelhub;1"] .getService()`
- 参照: `Ci.nsIMLModelHub`, `this.#observingProgress`, `this.#progressToken`
- XPCOM: [`nsIMLModelHub`](../../toolkit/components/ml/nsIMLModelHub.idl.md) / `@mozilla.org/ml-modelhub;1` → `MLModelHubService` (toolkit/components/ml/components.conf)

## eventCallback()
- 位置: L2637-2646
- 役割: swapping では true を返して通知を別ブラウザへ移し、removed では進捗の監視を止めて通知の参照を消す
- 触るとき: タブを移動したときに進捗表示が引き継がれない、または閉じた後も監視が残る問題を調べるとき
- 条件付き依存: `if (topic == "removed")` → `this.#stopObservingProgress()`
- 参照: `this.#notification`

## SpeechRecognitionModelDownloadPermissionPrompt.#applyProgressUI()
- 位置: L2663-2673
- 役割: 通知要素に進行中の属性を付け、進捗の内容部分を表示する
- 触るとき: 進捗表示が別ウィンドウに移った後も見えるようにする処理を変えるとき
- 呼び出し先: `notificationEl.querySelector()`, `notificationEl.toggleAttribute()`, `this.#notificationElement()`
- 参照: `notificationEl.querySelector( "#speech-recognition-model-download-progress-content" ).hidden`

## SpeechRecognitionModelDownloadPermissionPrompt.#setSecondaryLabel()
- 位置: L2680-2689
- 役割: 副ボタンの動作と文言(ラベルとアクセスキー)を差し替え、描画済みのボタンにも属性で反映する
- 触るとき: 完了後に副ボタンを OK に変えるときや、アクセスキーが反映されない問題を調べるとき
- 呼び出し先: `notificationEl.setAttribute()`
- 参照: `message.accesskey`, `message.label`, `secondaryAction.accessKey`, `secondaryAction.label`, `this.#notification.secondaryActions`

## SpeechRecognitionModelDownloadPermissionPrompt.#resetProgressUI()
- 位置: L2691-2709
- 役割: 進捗表示の属性を外し、バーを 0 にし、状態の文字を消す
- 触るとき: 同じ通知を再利用するときに前回の表示が残る問題を調べるとき
- 呼び出し先: `notificationEl.querySelector()`, `notificationEl.toggleAttribute()`, `this.#notificationElement()`
- 参照: `notificationEl.querySelector( "#speech-recognition-model-download-progress" ).value`, `notificationEl.querySelector( "#speech-recognition-model-download-progress-content" ).hidden`, `notificationEl.querySelector( "#speech-recognition-model-download-progress-status" ).textContent`

## SpeechRecognitionModelDownloadPermissionPrompt.#updateProgress()
- 位置: L2711-2780
- 役割: 進捗の整数パーセントが変わったときだけバーと状態を更新する。完了時は監視を止め、成否の文言に変え、副ボタンを OK にし、成功なら 5 秒後に閉じる
- 触るとき: 進捗表示の更新頻度や完了時の見せ方を変えるとき。失敗時は利用者が閉じるまで残す
- 呼び出し先: `Math.floor()`, `Math.max()`, `Math.min()`, `lazy.gFluentStrings.formatValueSync()`, `notificationEl.hasAttribute()`, `notificationEl.querySelector()`, `notificationEl.setAttribute()`, `notificationEl.toggleAttribute()`, `this.#notificationElement()`, `this.#setProgressStatus()`, `this.#setSecondaryLabel()`, `this.#stopObservingProgress()`
- 条件付き依存: `if (!notificationEl.hasAttribute("model-download-in-progress"))` → `this.#applyProgressUI()`
- 条件付き依存: `if (!notificationEl.hasAttribute("model-download-in-progress"))` → `this.#notificationElement()`
- 条件付き依存: `if (progress.ok)` → `lazy.setTimeout()`
- 条件付き依存: `if (progress.ok)` → `this.#notification?.remove()`
- 参照: `progress.done`, `progress.ok`, `progress.progress`, `progressEl.value`, `statusEl.textContent`, `this.#notification.message`, `this.#okMessage`, `this.#renderedPercent`

## SpeechRecognitionModelDownloadPermissionPrompt.#setProgressStatus()
- 位置: L2786-2805
- 役割: 合計が 0 以下なら空にし、それ以外は経過時間で平均した速度から残り時間と容量の文字列を作って表示する
- 触るとき: ダウンロードの残り時間や速度の表示形式を変えるとき
- 呼び出し先: `ChromeUtils.now()`, `lazy.DownloadUtils.getDownloadStatus()`
- 参照: `progress.total`, `progress.totalLoaded`, `statusEl.textContent`, `this.#downloadStartedAt`, `this.#lastSec`

## SpeechRecognitionModelDownloadPermissionPrompt.#stopObservingProgress()
- 位置: L2807-2813
- 役割: 進捗トピックの監視を一度だけ外す
- 触るとき: 通知を閉じた後や完了後に監視が残る問題を調べるとき
- 呼び出し先: `Services.obs.removeObserver()`
- 参照: `this.#observingProgress`
- XPCOM: `Services.obs`
