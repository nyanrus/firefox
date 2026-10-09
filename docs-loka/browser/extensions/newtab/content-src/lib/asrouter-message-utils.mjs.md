# browser/extensions/newtab/content-src/lib/asrouter-message-utils.mjs

source: browser/extensions/newtab/content-src/lib/asrouter-message-utils.mjs
source-hash: 43d94b0d1ddd22d17df86ec27feb2fa5ed92a5df
lines: 58

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`

## shouldShowOMCHighlight()
- 位置: L19-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`
- 参照: `Object.keys(messageData).length`, `messageData?.content?.messageType`, `messagesProp?.isVisible`, `messagesProp?.messageData`

## shouldShowASRouterNewTabMessage()
- 位置: L38-57
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (configuredPosition === currentPosition)` → `shouldShowOMCHighlight()`
- 参照: `ASROUTER_NEWTAB_MESSAGE_POSITIONS.ABOVE_TOPSITES`, `messageData.content?.position`, `messagesProps?.messageData`
