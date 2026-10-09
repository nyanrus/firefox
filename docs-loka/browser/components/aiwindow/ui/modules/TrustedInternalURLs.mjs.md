# browser/components/aiwindow/ui/modules/TrustedInternalURLs.mjs

source: browser/components/aiwindow/ui/modules/TrustedInternalURLs.mjs
source-hash: 5440fcdb7a97473a52a39deee3e94e1c13af02df
lines: 67

## <module>
- 役割: AI チャットが参照してよい内部 URL(設定、タスク、生成ページ)を判定する関数群。

## isSettingsURL()
- 位置: L21-26
- 役割: about:preferences または about:settings の URL かを判定する。
- 触るとき: チャットからの設定ページへの遷移可否を変えるとき、または設定ページのリンクが信頼されない時に調べる。
- 参照: `url.pathname`, `url?.protocol`

## isTasksURL()
- 位置: L35-37
- 役割: about:smartwindowtasks の URL かを判定する。
- 触るとき: タスク設定ページへのリンクが遷移を拒否される理由を追うとき。
- 参照: `url.pathname`, `url?.protocol`

## getSmartPageName()
- 位置: L47-54
- 役割: about:smartpage?page=... から検証済みのスラッグを取り出し、不正なら null を返す。
- 触るとき: 生成ページの名前の許容文字を変えるとき、または生成ページが保存されない理由を調べるとき。
- 呼び出し先: `PAGE_NAME_REGEX.test()`, `url.searchParams.get()`
- 参照: `url.pathname`, `url?.protocol`

## isSmartPageURL()
- 位置: L64-66
- 役割: getSmartPageName が有効なスラッグを返すかで、生成ページの URL かを判定する。
- 触るとき: 生成ページを内部ページとして扱うか判断する箇所の挙動を変えるとき。
- 呼び出し先: `getSmartPageName()`
