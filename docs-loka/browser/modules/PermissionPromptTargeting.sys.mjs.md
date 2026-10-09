# browser/modules/PermissionPromptTargeting.sys.mjs

source: browser/modules/PermissionPromptTargeting.sys.mjs
source-hash: 7bc6a8813c06e9bb67c511c791bbec21cd347f5d
lines: 45

## <module>
- 役割: 通知の許可ダイアログ(webNotificationsPermissionUi)の表示条件とロゴの検証を行う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## isValidLogoUrl()
- 位置: L18-28
- 役割: ロゴ URL が chrome: か resource: の文字列なら真を返す。
- 触るとき: ダイアログに表示するロゴの許可スキームを変えるとき。リモートの画像は親プロセスで描画しないため許可しない。
- 呼び出し先: `ALLOWED_LOGO_SCHEMES.includes()`, `Services.io.newURI()`
- 参照: `uri.scheme`
- XPCOM: `Services.io`

## evalPermissionPromptTargeting()
- 位置: async L30-44
- 役割: JEXL 式を webNotificationSiteCategory を使って評価し、真偽を返す。
- 触るとき: サイトのカテゴリでダイアログを出し分ける条件式を変えるとき。式が空なら真、評価中の例外は偽として扱う。
- 呼び出し先: `console.error()`, `targetingContext.evalWithDefault()`
- 参照: `lazy.TargetingContext`
