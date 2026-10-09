# browser/components/sessionstore/SessionCookies.sys.mjs

source: browser/components/sessionstore/SessionCookies.sys.mjs
source-hash: c3ad241d57d6e5eba66727243349c9b225bda280
lines: 325

## <module>
- 役割: セッション中だけ有効な Cookie(セッション Cookie)を Cookie サービスから集めて内部に保存し、復元時に Cookie サービスへ書き戻す。
- 呼び出し先: `Object.freeze()`, `XPCOMUtils.declareLazy()`

## collect()
- 位置: L17-19
- 役割: セッション Cookie の一覧を返す公開 API。内部の collect に委譲する。
- 触るとき: セッションファイルに保存される Cookie の範囲が想定と違うとき、呼び出し元から辿って確認する。
- 呼び出し先: `SessionCookiesInternal.collect()`

## restore()
- 位置: L21-23
- 役割: 渡された Cookie の配列を内部の restore に渡す公開 API。
- 触るとき: 復元処理の入口を変えるとき、または復元された Cookie が見つからないときに呼び出しを追う。
- 呼び出し先: `SessionCookiesInternal.restore()`

## collect()
- 位置: L38-41
- 役割: 初期化を確認してから、内部ストアの全件を配列で返す。
- 触るとき: 保存時に Cookie が取りこぼされるとき、初期化前に集められていないかを見る。
- 呼び出し先: `CookieStore.toArray()`, `this._ensureInitialized()`

## restore()
- 位置: L46-107
- 役割: 同じキーの Cookie が無ければ Cookie サービスへ追加する。失敗はコンソールにエラーを出して次の Cookie へ進む。
- 触るとき: 古い形式から移行した Cookie の SameSite やパーティションの扱いを変えるとき、既存 Cookie を上書きしない条件を確認するとき。isPartitioned は partitionKey があれば真、SameSite が無ければ SAMESITE_NONE、有効期限が無ければ MAX_SAFE_INTEGER として扱う。
- 呼び出し先: `JSON.stringify()`, `Services.cookies.cookieExists()`, `console.error()`
- 条件付き依存: `if (!exists)` → `Services.cookies.add()`
- 条件付き依存: `if (cv.result !== Ci.nsICookieValidation.eOK)` → `console.error()`
- 条件付き依存: `if (cv.result !== Ci.nsICookieValidation.eOK)` → `JSON.stringify()`
- 条件付き依存: `if (!exists)` → `console.error()`
- 条件付き依存: `if (!exists)` → `JSON.stringify()`
- 参照: `Ci.nsICookie.SAMESITE_NONE`, `Ci.nsICookie.SCHEME_HTTPS`, `Ci.nsICookieValidation.eOK`, `cookie.expiry`, `cookie.host`, `cookie.httponly`, `cookie.isPartitioned`, `cookie.name`, `cookie.originAttributes`, `cookie.originAttributes?.partitionKey?.length`, `cookie.path`, `cookie.sameSite`, `cookie.schemeMap`, `cookie.secure`, `cookie.value`, `cv.result`
- XPCOM: [`nsICookie`](../../../netwerk/cookie/nsICookie.idl.md) / [`nsICookieValidation`](../../../netwerk/cookie/nsICookieManager.idl.md) / `Services.cookies`

## observe()
- 位置: L113-143
- 役割: Cookie の追加、変更、削除、全消去、一括削除の通知を受け、内部ストアを更新する。未知の通知は例外にする。
- 触るとき: セッション中に変わった Cookie が保存に反映されない不具合を調べるとき。
- 呼び出し先: `CookieStore.clear()`, `subject.QueryInterface()`, `this._addCookie()`, `this._removeCookie()`, `this._removeCookies()`, `this._updateCookie()`
- 参照: `Ci.nsICookieNotification`, `notification.action`, `notification.batchDeletedCookies`, `notification.cookie`
- XPCOM: [`nsICookieNotification`](../../../netwerk/cookie/nsICookieNotification.idl.md)

## _ensureInitialized()
- 位置: L149-161
- 役割: 初回だけ既存のセッション Cookie を読み直し、Cookie 通知とプライバシーレベルの変更を監視し始める。
- 触るとき: 起動直後の最初の保存で Cookie が集まらないとき、またはプライバシーレベル変更への反応を変えるとき。
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.addObserver()`, `this._reloadCookies()`
- 参照: `this._initialized`
- XPCOM: `Services.obs` / `Services.prefs`

## _addCookie()
- 位置: L166-173
- 役割: セッション Cookie で、プライバシーレベルが保存を許す場合だけ内部ストアに追加する。
- 触るとき: どの Cookie を保存対象にするかの条件を変えるとき、secure な Cookie が保存されない原因を調べるとき。
- 呼び出し先: `cookie.QueryInterface()`, `lazy.PrivacyLevel.canSave()`
- 条件付き依存: `if (cookie.isSession && lazy.PrivacyLevel.canSave(cookie.isSecure))` → `CookieStore.add()`
- 参照: `Ci.nsICookie`, `cookie.isSecure`, `cookie.isSession`
- XPCOM: [`nsICookie`](../../../netwerk/cookie/nsICookie.idl.md)

## _updateCookie()
- 位置: L178-187
- 役割: 変更された Cookie が保存対象なら追加し直し、対象から外れたら削除する。
- 触るとき: セッション中に属性が変わった Cookie が保存対象から外れたのに残り続けないかを確認するとき。
- 呼び出し先: `cookie.QueryInterface()`, `lazy.PrivacyLevel.canSave()`
- 条件付き依存: `if (cookie.isSession && lazy.PrivacyLevel.canSave(cookie.isSecure))` → `CookieStore.add()`
- 条件付き依存: `if (!(cookie.isSession && lazy.PrivacyLevel.canSave(cookie.isSecure)))` → `CookieStore.delete()`
- 参照: `Ci.nsICookie`, `cookie.isSecure`, `cookie.isSession`
- XPCOM: [`nsICookie`](../../../netwerk/cookie/nsICookie.idl.md)

## _removeCookie()
- 位置: L192-198
- 役割: セッション Cookie だった場合だけ内部ストアから削除する。
- 触るとき: 削除通知を受けたあとも Cookie が保存され続ける問題を調べるとき。
- 呼び出し先: `cookie.QueryInterface()`
- 条件付き依存: `if (cookie.isSession)` → `CookieStore.delete()`
- 参照: `Ci.nsICookie`, `cookie.isSession`
- XPCOM: [`nsICookie`](../../../netwerk/cookie/nsICookie.idl.md)

## _removeCookies()
- 位置: L203-207
- 役割: 一括削除された Cookie の配列を一つずつ _removeCookie に渡す。
- 触るとき: 一括削除の通知の扱いを変えるとき。
- 呼び出し先: `cookies.queryElementAt()`, `this._removeCookie()`
- 参照: `Ci.nsICookie`, `cookies.length`
- XPCOM: [`nsICookie`](../../../netwerk/cookie/nsICookie.idl.md)

## _reloadCookies()
- 位置: L213-224
- 役割: 内部ストアを空にし、プライバシーレベルが許す場合だけ全てのセッション Cookie を読み直す。
- 触るとき: プライバシーレベルを変えたときの保存内容を確認するとき、または保存対象を一度作り直す処理を追加するとき。
- 呼び出し先: `CookieStore.clear()`, `lazy.PrivacyLevel.canSave()`, `this._addCookie()`
- 参照: `Services.cookies.sessionCookies`
- XPCOM: `Services.cookies`

## add()
- 位置: L242-281
- 役割: Cookie から保存用のオブジェクトを作り、既定値の項目は省いて、host・name・path・originAttributes の組をキーに登録する。
- 触るとき: セッションファイルに残す Cookie の項目を増減するとき。
- 呼び出し先: `this._entries.set()`, `this._getKeyForCookie()`
- 参照: `cookie.expiry`, `cookie.host`, `cookie.isHttpOnly`, `cookie.isPartitioned`, `cookie.isSecure`, `cookie.name`, `cookie.originAttributes`, `cookie.path`, `cookie.sameSite`, `cookie.schemeMap`, `cookie.value`, `jscookie.expiry`, `jscookie.httponly`, `jscookie.isPartitioned`, `jscookie.name`, `jscookie.originAttributes`, `jscookie.path`, `jscookie.sameSite`, `jscookie.schemeMap`, `jscookie.secure`

## delete()
- 位置: L289-291
- 役割: Cookie のキーに対応する項目を内部ストアから削除する。
- 触るとき: 削除通知で正しい項目が消えているかを確認するとき。
- 呼び出し先: `this._entries.delete()`, `this._getKeyForCookie()`

## clear()
- 位置: L296-298
- 役割: 内部ストアの全項目を消す。
- 触るとき: 全消去の通知やプライバシーレベルの再読み込みで消える範囲を確認するとき。
- 呼び出し先: `this._entries.clear()`

## toArray()
- 位置: L303-305
- 役割: 内部ストアの項目を配列にして返す。
- 触るとき: セッションファイルへ書き出される Cookie 一覧の形式を確認するとき。
- 呼び出し先: `this._entries.values()`

## _getKeyForCookie()
- 位置: L316-323
- 役割: host、name、path、originAttributes のサフィックスを JSON にしてキーを作る。
- 触るとき: 同じ名前の Cookie が別々に保存される、または互いに上書きされる原因を調べるとき。
- 呼び出し先: `ChromeUtils.originAttributesToSuffix()`, `JSON.stringify()`
- 参照: `cookie.host`, `cookie.name`, `cookie.originAttributes`, `cookie.path`
