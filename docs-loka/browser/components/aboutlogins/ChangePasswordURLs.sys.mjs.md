# browser/components/aboutlogins/ChangePasswordURLs.sys.mjs

source: browser/components/aboutlogins/ChangePasswordURLs.sys.mjs
source-hash: 6ffb0df1c543e844f0913a434aeeeb596991c09b
lines: 115

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `lazy.LoginHelper.createLogger()`

## _getDomainToChangePasswordURLMap()
- 位置: async L40-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `domainMap.set()`, `lazy .RemoteSettings()`, `lazy .RemoteSettings(this.REMOTE_SETTINGS_COLLECTION) .get()`, `this._isValidHTTPSURL()`
- 条件付き依存: `if (ex instanceof lazy.RemoteSettingsClient.UnknownCollectionError)` → `lazy.log.warn()`
- 参照: `lazy.RemoteSettingsClient.UnknownCollectionError`, `record.host`, `record.url`, `this.REMOTE_SETTINGS_COLLECTION`

## getChangePasswordURLsByLoginGUID()
- 位置: async L82-104
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.hasRootDomain()`, `Services.io.newURI()`, `this._getDomainToChangePasswordURLMap()`
- 条件付き依存: `if (Services.eTLD.hasRootDomain(loginHost, domain))` → `changePasswordURLsByLoginGUID.set()`
- 参照: `Services.io.newURI(login.origin).host`, `login.guid`, `login.origin`
- XPCOM: `Services.eTLD` / `Services.io`

## _isValidHTTPSURL()
- 位置: L106-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`
- 参照: `uri.scheme`
- XPCOM: `Services.io`
