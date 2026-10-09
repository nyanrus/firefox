# browser/modules/PermissionPromptTargeting.sys.mjs

source: browser/modules/PermissionPromptTargeting.sys.mjs
source-hash: 7bc6a8813c06e9bb67c511c791bbec21cd347f5d
lines: 45

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## isValidLogoUrl()
- 位置: L18-28
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ALLOWED_LOGO_SCHEMES.includes()`, `Services.io.newURI()`
- 参照: `uri.scheme`
- XPCOM: `Services.io`

## evalPermissionPromptTargeting()
- 位置: async L30-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `targetingContext.evalWithDefault()`
- 参照: `lazy.TargetingContext`
