# browser/components/aiwindow/ui/modules/ToolActionLog.sys.mjs

source: browser/components/aiwindow/ui/modules/ToolActionLog.sys.mjs
source-hash: 99eed3da8cfccf92c8483edda2c9d04eedcd3b98
lines: 220

## <module>
- 役割: AI Window のツール実行の操作ログ行を組み立てる。ツールごとの表示ラベル、遷移中と完了後の文言、結果の URL 一覧からのチップを決める。
- 呼び出し先: `Object.freeze()`, `urlListChips()`

## urlListChips()
- 位置: L51-56
- 役割: URL を持つ項目の配列を、url と表示ラベルの組のチップ配列に変換する。
- 触るとき: 新しいツールの結果から URL 一覧を行のチップにしたいとき。
- 呼び出し先: `(items ?? []).map()`, `getLabel()`
- 参照: `item.url`

## resolveSupportUrl()
- 位置: L134-138
- 役割: サポートページの相対パスを、app.support.baseURL に続けて完全な URL にする。
- 触るとき: 操作ログのリンク先の書き方や基準 URL を調べるとき。
- 呼び出し先: `Services.urlFormatter.formatURLPref()`
- XPCOM: `Services.urlFormatter`

## getActionLogConfigForTool()
- 位置: L149-177
- 役割: ツール名から表示設定を引く。未登録なら非表示にする。結果が保留中なら遷移中の文言を、完了していれば完了時の文言を選ぶ。
- 触るとき: ツールの行を表示するかどうか、または保留中と完了後で文言を切り替える条件を変えるとき。
- 呼び出し先: `TOOL_ACTION_LOG_CONFIG.get()`, `cfg.label()`, `resolveSupportUrl()`
- 参照: `body?.pending`, `cfg.label`, `cfg.link`, `cfg.link.l10nName`, `cfg.link.supportPage`, `cfg.pendingLabel`

## getActionLogChipsForTool()
- 位置: L187-190
- 役割: ツール名に対応するアダプタでチップ配列を作る。アダプタが無ければ空配列を返す。
- 触るとき: ツールの結果からチップを出す対象を増やす、または減らすとき。
- 呼び出し先: `TOOL_RESULT_TO_CHIPS.get()`, `adapter()`

## buildActionLogRow()
- 位置: L204-219
- 役割: チップ、リンク、ラベル (l10n の ID または文字列) をまとめて、action-result 用の行オブジェクトを作る。
- 触るとき: 操作ログの行の形式を変えるとき、またはラベルが翻訳されずに出るときに、どの値が行に入るかを確かめる。
- 呼び出し先: `getActionLogChipsForTool()`
- 参照: `label.l10nArgs`, `label.l10nId`, `link?.href`, `row.label`, `row.labelL10nArgs`, `row.labelL10nId`, `row.link`
