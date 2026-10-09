# browser/components/aiwindow/ui/modules/TrustedInternalURLs.mjs

source: browser/components/aiwindow/ui/modules/TrustedInternalURLs.mjs
source-hash: 5440fcdb7a97473a52a39deee3e94e1c13af02df
lines: 67

## <module>
- 役割: (未記入)

## isSettingsURL()
- 位置: L21-26
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `url.pathname`, `url?.protocol`

## isTasksURL()
- 位置: L35-37
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `url.pathname`, `url?.protocol`

## getSmartPageName()
- 位置: L47-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PAGE_NAME_REGEX.test()`, `url.searchParams.get()`
- 参照: `url.pathname`, `url?.protocol`

## isSmartPageURL()
- 位置: L64-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getSmartPageName()`
