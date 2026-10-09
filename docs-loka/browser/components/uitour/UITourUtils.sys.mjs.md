# browser/components/uitour/UITourUtils.sys.mjs

source: browser/components/uitour/UITourUtils.sys.mjs
source-hash: b390b2b53dcaa3b37e0cbe387b0b3b41eb4f7efd
lines: 85

## <module>
- 役割: (未記入)

## isTestingOrigin()
- 位置: L17-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `Services.prefs.getStringPref()`, `console.error()`, `testingOrigins.split()`
- 参照: `testingURI.prePath`, `uri.prePath`
- XPCOM: `Services.io` / `Services.prefs`

## ensureTrustedOrigin()
- 位置: L45-83
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.perms.testPermissionFromPrincipal()`, `WindowGlobalParent.isInstance()`, `this.isTestingOrigin()`
- 参照: `Services.perms.ALLOW_ACTION`, `document?.documentURIObject`, `document?.nodePrincipal`, `windowGlobal.browsingContext.parent`, `windowGlobal.browsingContext.secureBrowserUI?.isSecureContext`, `windowGlobal.contentWindow.document`, `windowGlobal.contentWindow?.isSecureContext`, `windowGlobal.documentPrincipal`, `windowGlobal.documentURI`, `windowGlobal.isCurrentGlobal`
- XPCOM: `Services.perms`
