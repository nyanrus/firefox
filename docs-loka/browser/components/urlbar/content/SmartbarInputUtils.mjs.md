# browser/components/urlbar/content/SmartbarInputUtils.mjs

source: browser/components/urlbar/content/SmartbarInputUtils.mjs
source-hash: 759b025cdf8b7cedc1612001265acad9b57ef965
lines: 849

## <module>
- 役割: スマートバーの入力欄を拡張する。@ によるタブ・タブグループのメンション、/ によるエージェントコマンドのパレット、エディター生成と SmartbarInputController 向けアダプターを担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## logger()
- 位置: L41-45
- 役割: SmartbarMentionsPanel 用のロガーを返す。ログレベルは専用の pref で決まる。
- 触るとき: メンション周りのログ出力を追加したり、ログが出ない原因を調べたりするとき。
- 呼び出し先: `UrlbarShared.getLogger()`

## isAgentCommandAvailable()
- 位置: L59-64
- 役割: エージェントコマンドが使えるかを、エージェント有効 pref とモニター領域のサポート判定の両方で返す。
- 触るとき: / コマンドを表示する条件を変えるとき。
- 呼び出し先: `UrlbarPrefs.get()`, `lazy.MonitorUIUtils.isMonitorRegionSupported()`

## isAgentCommand()
- 位置: L72-74
- 役割: 入力文字列が既知のエージェントコマンドで始まるかを真偽で返す。
- 触るとき: 送信時にコマンドとして扱うかどうかの判定を呼び出し側で使うとき。
- 呼び出し先: `getAgentCommandId()`

## getAgentCommandId()
- 位置: L83-91
- 役割: 入力先頭のエージェントコマンド ID を返す。利用不可、または既知でなければ null。
- 触るとき: 入力がどのコマンドかを特定して実行に渡す処理を変えるとき。
- 呼び出し先: `AGENT_COMMAND_ITEMS.has()`, `isAgentCommandAvailable()`, `parseAgentCommand()`
- 参照: `parsed.command`

## getCommandSuggestions()
- 位置: L99-111
- 役割: 入力された接頭辞に前方一致するエージェントコマンドを、パネル用のグループにして返す。
- 触るとき: / 入力時にどのコマンド候補が出るかを調べたり、候補の並びや見出しを変えたりするとき。
- 呼び出し先: `[...AGENT_COMMAND_ITEMS] .filter()`, `[...AGENT_COMMAND_ITEMS] .filter(([id]) => id.startsWith(normalized)) .map()`, `id.startsWith()`, `isAgentCommandAvailable()`, `query.trim()`, `query.trim().toLowerCase()`
- 参照: `items.length`

## getMentionSuggestions()
- 位置: L150-211
- 役割: タブを検索して URL で重複排除し、開いているタブを優先して並べる。タブグループを先頭グループに加え、件数付きで返す。
- 触るとき: @ メンションの候補の内容や順序を変えるとき、または検索で例外が出たときの戻り値を確認するとき。
- 呼び出し先: `UrlbarPrefs.get()`, `getTabGroupMentionId()`, `groups.push()`, `logger()`, `logger().error()`, `mentionSearch .getTabGroups()`, `mentionSearch .getTabGroups() .map()`, `mentionSearch .startQuery()`, `seen.add()`, `seen.has()`
- 条件付き依存: `if (tabGroupItems.length)` → `groups.push()`
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `deduplicated.length`, `item.id`, `item.url`, `lazy.MENTION_TYPE.TAB_OPEN`, `r1.type`, `r2.type`, `tabGroupItems.length`

## getAnchorPos()
- 位置: L220-230
- 役割: テキスト範囲の両端の座標から、パネルを置く矩形(left, top, width, height)を求める。
- 触るとき: メンションパネルの表示位置がずれる問題を調べるとき。
- 呼び出し先: `view.coordsAtPos()`
- 参照: `coordsFrom.left`, `coordsFrom.top`, `coordsTo.bottom`, `coordsTo.right`, `range.from`, `range.to`

## refocusEditorOnUnhandledPanelKey()
- 位置: L238-244
- 役割: パネルで処理されなかったキーなら、エディターにフォーカスを戻す。Tab、矢印上下、Enter はそのまま通す。
- 触るとき: パネル表示中のキー操作でフォーカスが迷子になる不具合を調べるとき。
- 呼び出し先: `["Tab", "ArrowUp", "ArrowDown", "Enter"].includes()`, `editorElement.focus()`
- 参照: `e.detail`, `originalEvent.key`

## suppressEnterWhilePanelOpen()
- 位置: L252-256
- 役割: パネルが開いている間に Enter が押されたら伝播を止め、スマートバーの送信を防ぐ。
- 触るとき: メンションやコマンドの選択中に誤って送信される問題を調べるとき。
- 呼び出し先: `isPanelOpen()`
- 条件付き依存: `if (isPanelOpen() && e.key === "Enter")` → `e.stopPropagation()`
- 参照: `e.key`

## setupContextMentionsButton()
- 位置: L264-302
- 役割: コンテキスト(+)ボタンでタブ候補パネルを開き、表示中はボタンを active 表示にし、開いた回数を計測する。
- 触るとき: コンテキストボタンからのタブ追加の動作や計測を変えるとき。
- 呼び出し先: `Glean.smartWindow.addTabsClick.record()`, `String()`, `contextButton.addEventListener()`, `contextButton.removeAttribute()`, `getMentionSuggestions()`, `panelList.addEventListener()`, `panelList.getAttribute()`, `panelList.setAttribute()`, `panelList.toggle()`, `smartbarInput.querySelector()`
- 条件付き依存: `if (panelList.getAttribute("data-triggered-by") === "context-mention")` → `contextButton.setAttribute()`
- 参照: `lazy.SmartbarMentionsPanelSearch`, `panelList.anchor`, `panelList.groups`, `smartbarInput.contextWebsitesCount`, `smartbarInput.conversationTelemetryInfo`, `smartbarInput.sapLocation`, `window.browsingContext.topChromeWindow`

## setupMentionsPlugin()
- 位置: L311-557
- 役割: @ メンションのプラグインを作り、エディターのイベントとパネルの選択を結び付ける。さらに isHandlingMentions や hasMention などをエディターに公開する。
- 触るとき: @ メンションの挿入・削除・候補表示のつながりを追うとき。
- 呼び出し先: `Object.defineProperties()`, `createMentionsPlugin()`, `document.l10n .formatValue()`, `document.l10n .formatValue("smartbar-mention-typing-placeholder") .then()`, `editorElement.addEventListener()`, `editorElement.closest()`, `editorElement.style.setProperty()`, `panelList.addEventListener()`

## handleMentionsChange()
- 位置: L326-337
- 役割: 入力テキストの先頭の @ を除いた文字列で候補を取り直し、パネルのグループを更新する。
- 触るとき: 入力に応じた候補の再検索が効かない問題を調べるとき。
- 呼び出し先: `getMentionSuggestions()`, `text.substring()`
- 参照: `panelList.groups`

## toDOM()
- 位置: L345-353
- 役割: メンションをエディター内で span 要素として描画するための属性と内容を返す。
- 触るとき: メンションの DOM 表現や data 属性を変えるとき。
- 参照: `node.attrs.id`, `node.attrs.label`, `node.attrs.type`

## nodeView()
- 位置: L354-366
- 役割: メンションをチップ表示(ai-website-chip)の要素として描く。タブグループは色付き、タブは URL とアイコンで表示する。
- 触るとき: インラインのメンションチップの見た目や属性を変えるとき。
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `node.attrs.color`, `node.attrs.id`, `node.attrs.label`, `node.attrs.type`

## onEnter()
- 位置: L367-389
- 役割: @ が入力されたときに検索を作り、パネルを表示して候補を出し、開始をテレメトリに記録する。
- 触るとき: @ を打った直後にパネルが出ない、または候補が空になる問題を調べるとき。
- 呼び出し先: `Glean.smartWindow.mentionStart.record()`, `String()`, `editorElement.setAttribute()`, `getAnchorPos()`, `getMentionSuggestions()`, `panelList.setAttribute()`, `panelList.show()`
- 参照: `lazy.SmartbarMentionsPanelSearch`, `mentionData.range`, `mentionData.view`, `panelList.anchor`, `panelList.groups`, `smartbarInput.conversationTelemetryInfo`, `smartbarInput.sapLocation`, `window.browsingContext.topChromeWindow`

## onChange()
- 位置: L390-405
- 役割: 入力が変わるたびにプレースホルダー表示を切り替え、候補検索をデバウンス用のタイマーに予約する。
- 触るとき: 入力中の候補更新の遅れや、プレースホルダーの出し分けを変えるとき。
- 呼び出し先: `editorElement.toggleAttribute()`
- 参照: `lazy.SkippableTimer`, `mentionData.text.length`

## onExit()
- 位置: L406-418
- 役割: @ メンションを抜けたときにパネルを隠し、保留中の検索タイマーを止め、関連する状態を消す。
- 触るとき: メンション終了後にパネルや状態が残る問題を調べるとき。
- 呼び出し先: `editorElement.removeAttribute()`, `panelList.hide()`
- 条件付き依存: `if (mentionChangeTimer)` → `mentionChangeTimer.cancel()`

## handleChipDisconnected()
- 位置: L421-431
- 役割: インラインのメンションチップが外れたときに、削除のテレメトリを記録する。
- 触るとき: メンションの削除計測を変えるとき。
- 条件付き依存: `if (e.detail.type === "in-line")` → `Glean.smartWindow.mentionRemove.record()`
- 条件付き依存: `if (e.detail.type === "in-line")` → `String()`
- 条件付き依存: `if (e.detail.type === "in-line")` → `plugin.mentions.getAll()`
- 参照: `e.detail.type`, `plugin.mentions.getAll().length`, `smartbarInput.conversationTelemetryInfo`, `smartbarInput.sapLocation`

## handleItemSelected()
- 位置: L433-509
- 役割: 候補選択時に、コンテキストボタン経由ならコンテキストへ追加し、@ 経由ならインラインのメンションとして挿入する。
- 触るとき: 候補を選んだ後にタブがどこへ入るかを変えるとき。
- 呼び出し先: `panelList.getAttribute()`, `panelList.removeAttribute()`
- 条件付き依存: `if (isContextButtonTrigger)` → `smartbarInput.addContextMention()`
- 条件付き依存: `if (isContextButtonTrigger)` → `parseTabGroupMentionId()`
- 条件付き依存: `if (isContextButtonTrigger)` → `Glean.smartWindow.addTabsSelection.record()`
- 条件付き依存: `if (isContextButtonTrigger)` → `String()`
- 条件付き依存: `if (isContextButtonTrigger)` → `panelList.groups.reduce()`
- 条件付き依存: `if (!(isContextButtonTrigger))` → `Glean.smartWindow.mentionSelect.record()`
- 条件付き依存: `if (!(isContextButtonTrigger))` → `panelList.groups.reduce()`
- 条件付き依存: `if (!(isContextButtonTrigger))` → `String()`
- 条件付き依存: `if (!(isContextButtonTrigger))` → `plugin.mentions.insert()`
- 参照: `CONTEXT_MENTION_TYPE.TAB`, `CONTEXT_MENTION_TYPE.TAB_GROUP`, `e.detail`, `group.items.length`, `label.length`, `latestMentionData?.range.from`, `latestMentionData?.range.to`, `smartbarInput.contextWebsitesCount`, `smartbarInput.conversationTelemetryInfo`, `smartbarInput.sapLocation`

## handlePanelKeyDown()
- 位置: L511-512
- 役割: パネルのキー操作を、エディターのフォーカス戻しの処理へ渡す。
- 触るとき: パネルのキー操作の処理を追加するとき。
- 呼び出し先: `refocusEditorOnUnhandledPanelKey()`

## handleEditorKeyDown()
- 位置: L513-514
- 役割: パネル表示中のエディターの Enter を抑止する処理へ渡す。
- 触るとき: メンション表示中のキー操作の抑止条件を変えるとき。
- 呼び出し先: `suppressEnterWhilePanelOpen()`

## get()
- 位置: L534-534
- 役割: メンションのパネルが表示中かどうか(isHandlingMentions)を返す。
- 触るとき: エディター側から @ メンションの表示状態を参照するとき。

## get()
- 位置: L537-537
- 役割: エディターにインラインのメンションがあるかどうか(hasMention)を返す。
- 触るとき: 送信前にメンションが付いているかを判定する箇所を調べるとき。
- 呼び出し先: `plugin.mentions.hasMention()`

## value()
- 位置: L540-540
- 役割: エディター上の全メンションを返す(getAllMentions)。
- 触るとき: 送信時にメンションの一覧を取り出す処理を変えるとき。
- 呼び出し先: `plugin.mentions.getAll()`

## value()
- 位置: L549-552
- 役割: 指定した文字オフセットの位置にメンションノードを挿入する(insertMention)。
- 触るとき: プログラムからメンションを挿入する処理を追加するとき。
- 呼び出し先: `editorElement.textOffsetToPos()`, `plugin.mentions.insertNode()`

## setupCommandsPlugin()
- 位置: L570-733
- 役割: / コマンドのプラグインを作る。入力の先頭が / のときにパネルでコマンドを絞り込み、Enter や矢印キーで実行や移動を行う。
- 触るとき: / コマンドパレットのキー操作や候補の表示条件を変えるとき。
- 呼び出し先: `Object.defineProperties()`, `createCommandsPlugin()`, `editorElement.addEventListener()`, `editorElement.closest()`, `panelList.addEventListener()`

## isLeadingCommand()
- 位置: L577-578
- 役割: エディターの値の先頭が / で始まるかを判定する。
- 触るとき: / で始まる入力だけをコマンドとして扱う条件を変えるとき。
- 呼び出し先: `editorElement.value.trimStart()`, `editorElement.value.trimStart().startsWith()`

## updatePanel()
- 位置: L580-592
- 役割: コマンド候補をパネルに反映する。候補が無ければ隠し、あれば表示して真を返す。
- 触るとき: コマンド候補が出たり消えたりする条件を調べるとき。
- 呼び出し先: `getCommandSuggestions()`, `panelList.setAttribute()`, `panelList.show()`
- 条件付き依存: `if (!groups.length)` → `panelList.hide()`
- 参照: `groups.length`, `panelList.anchor`, `panelList.groups`

## onExitPalette()
- 位置: L594-602
- 役割: コマンドパレットの状態を消し、パネルがコマンド用に開いていた場合だけ隠す。
- 触るとき: パレットを閉じた後にメンション用のパネル状態が壊れる問題を調べるとき。
- 呼び出し先: `panelList.getAttribute()`
- 条件付き依存: `if (panelList.getAttribute("data-triggered-by") === COMMAND_TRIGGER)` → `panelList.hide()`
- 条件付き依存: `if (panelList.getAttribute("data-triggered-by") === COMMAND_TRIGGER)` → `panelList.removeAttribute()`

## executeCommand()
- 位置: L605-624
- 役割: 選ばれたコマンドを計測したうえで、/ID として送信する。
- 触るとき: コマンド実行時の送信内容や計測を変えるとき。
- 呼び出し先: `Glean.smartWindow.agentCommandSelect.record()`, `String()`, `onExitPalette()`, `panelList.groups.reduce()`, `smartbarInput.submitChat()`
- 参照: `group.items.length`, `smartbarInput.conversationTelemetryInfo`, `smartbarInput.sapLocation`

## handleItemSelected()
- 位置: L626-635
- 役割: コマンド用に開いたパネルで項目が選ばれたら、そのコマンドを実行する。
- 触るとき: パネルのマウス選択からコマンドが実行されない問題を調べるとき。
- 呼び出し先: `executeCommand()`, `panelList.getAttribute()`
- 参照: `e.detail.id`

## handlePanelKeyDown()
- 位置: L637-643
- 役割: パネルで Escape が押されたらパレットを閉じ、それ以外はエディターのフォーカス戻しへ渡す。
- 触るとき: Escape の振る舞いや、コマンドパネルのキー処理を変えるとき。
- 呼び出し先: `refocusEditorOnUnhandledPanelKey()`
- 条件付き依存: `if (e.detail?.originalEvent?.key === "Escape")` → `onExitPalette()`
- 参照: `e.detail?.originalEvent?.key`

## handleEditorKeyDown()
- 位置: L645-676
- 役割: パレット表示中に矢印キー、Enter、Escape を横取りし、修飾キー付きの入力は通す。
- 触るとき: パレット表示中のキーボード操作を追加・変更するとき。
- 呼び出し先: `e.preventDefault()`, `e.stopPropagation()`, `handler()`
- 参照: `e.altKey`, `e.ctrlKey`, `e.key`, `e.metaKey`, `e.shiftKey`

## ArrowDown()
- 位置: L657-657
- 役割: パネルの選択を一つ下へ動かす。
- 触るとき: コマンド候補の上下移動の挙動を変えるとき。
- 呼び出し先: `panelList.moveSelection()`

## ArrowUp()
- 位置: L658-658
- 役割: パネルの選択を一つ上へ動かす。
- 触るとき: コマンド候補の上下移動の挙動を変えるとき。
- 呼び出し先: `panelList.moveSelection()`

## Enter()
- 位置: L659-664
- 役割: 選択中のコマンドがあれば Enter で実行する。
- 触るとき: Enter でのコマンド実行条件を変えるとき。
- 呼び出し先: `panelList.getSelectedItem()`
- 条件付き依存: `if (selected)` → `executeCommand()`
- 参照: `selected.id`

## Escape()
- 位置: L665-665
- 役割: パレットを閉じる。
- 触るとき: Escape でパレットを閉じる条件を変えるとき。
- 呼び出し先: `onExitPalette()`

## get()
- 位置: L692-692
- 役割: コマンドパレットが候補を表示中かどうか(isHandlingCommands)を返す。
- 触るとき: エディター側からコマンドパレットの表示状態を参照するとき。

## onEnter()
- 位置: L699-721
- 役割: 先頭が / の入力で候補を作って表示し、表示できたらコマンド開始を計測する。
- 触るとき: / を打った直後のパレット表示や計測を変えるとき。
- 呼び出し先: `data.text.substring()`, `isLeadingCommand()`, `updatePanel()`
- 条件付き依存: `if (isHandlingCommands)` → `Glean.smartWindow.agentCommandStart.record()`
- 条件付き依存: `if (isHandlingCommands)` → `String()`
- 条件付き依存: `if (isHandlingCommands)` → `panelList.groups.reduce()`
- 参照: `group.items.length`, `smartbarInput.conversationTelemetryInfo`, `smartbarInput.sapLocation`

## onChange()
- 位置: L722-728
- 役割: 入力が変わるたびに、先頭が / の場合だけ候補を取り直す。
- 触るとき: 入力中にコマンド候補が絞り込まれない問題を調べるとき。
- 呼び出し先: `data.text.substring()`, `isLeadingCommand()`, `updatePanel()`

## onExit()
- 位置: L729-731
- 役割: コマンドパレットを閉じる処理へ渡す。
- 触るとき: コマンドの入力を抜けたときの後始末を変えるとき。
- 呼び出し先: `onExitPalette()`

## createEditor()
- 位置: L746-812
- 役割: 既存の input 要素を moz-multiline-editor に置き換え、属性を引き継ぎ、メンションとコマンドのプラグインとコンテキストボタンを組み立てる。
- 触るとき: スマートバーの入力欄の初期化や、プラグインの組み合わせを変えるとき。
- 呼び出し先: `PLACEHOLDER_HINT_L10N_IDS.map()`, `container.querySelector()`, `createEditorAdapter()`, `doc.createElement()`, `document.l10n .formatValues()`, `document.l10n .formatValues(PLACEHOLDER_HINT_L10N_IDS.map(id => ({ id }))) .then()`, `editorElement.closest()`, `editorElement.setAttribute()`, `inputElement.replaceWith()`, `setupContextMentionsButton()`, `setupMentionsPlugin()`
- 条件付き依存: `if (inputElement instanceof MultilineEditor)` → `createEditorAdapter()`
- 条件付き依存: `if (smartbarInput.sapName === "smartbar")` → `plugins.push()`
- 条件付き依存: `if (smartbarInput.sapName === "smartbar")` → `setupCommandsPlugin()`
- 参照: `attr.name`, `attr.value`, `console.error`, `editorElement.className`, `editorElement.id`, `editorElement.placeholderHints`, `editorElement.plugins`, `editorElement.showPlaceholderAnimation`, `editorElement.value`, `inputElement.attributes`, `inputElement.className`, `inputElement.id`, `inputElement.ownerDocument`, `inputElement.value`, `lazy.AIWindowUI.BROWSER_ID`, `panelList.placeholderL10nId`, `panelList.sidebarMode`, `smartbarInput.sapName`, `window.browsingContext?.embedderElement?.id`

## createEditorAdapter()
- 位置: L820-848
- 役割: エディターを SmartbarInputController が期待する composing や selection の形に合わせるアダプターを作る。
- 触るとき: エディターの選択範囲や変換状態が正しく取れない問題を調べるとき。

## getSelectionBounds()
- 位置: L821-828
- 役割: 選択の開始と終了を取り、開始が終了より後ならば入れ替えて返す。
- 触るとき: 選択範囲を逆向きに選んだときの扱いを確認するとき。
- 参照: `editorElement.selectionEnd`, `editorElement.selectionStart`

## composing()
- 位置: L831-833
- 役割: エディターが変換中かどうかを真偽で返す。
- 触るとき: IME 変換中の判定を使う箇所を追うとき。
- 参照: `editorElement.composing`

## rangeCount()
- 位置: L835-838
- 役割: 選択範囲の数を返す。入力が空で選択がゼロ幅なら 0、それ以外は 1。
- 触るとき: 空の入力欄での選択判定を変えるとき。
- 呼び出し先: `getSelectionBounds()`
- 参照: `editorElement.value`

## toStringWithFormat()
- 位置: L839-845
- 役割: 選択範囲の文字列を書式なしで返す。
- 触るとき: 選択中のテキストを取り出す箇所の結果を確かめるとき。
- 呼び出し先: `editorElement.value?.substring()`, `getSelectionBounds()`
