# browser/components/urlbar/content/SmartbarInputUtils.mjs

source: browser/components/urlbar/content/SmartbarInputUtils.mjs
source-hash: 759b025cdf8b7cedc1612001265acad9b57ef965
lines: 849

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## logger()
- 位置: L41-45
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarShared.getLogger()`

## isAgentCommandAvailable()
- 位置: L59-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `lazy.MonitorUIUtils.isMonitorRegionSupported()`

## isAgentCommand()
- 位置: L72-74
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getAgentCommandId()`

## getAgentCommandId()
- 位置: L83-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AGENT_COMMAND_ITEMS.has()`, `isAgentCommandAvailable()`, `parseAgentCommand()`
- 参照: `parsed.command`

## getCommandSuggestions()
- 位置: L99-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...AGENT_COMMAND_ITEMS] .filter()`, `[...AGENT_COMMAND_ITEMS] .filter(([id]) => id.startsWith(normalized)) .map()`, `id.startsWith()`, `isAgentCommandAvailable()`, `query.trim()`, `query.trim().toLowerCase()`
- 参照: `items.length`

## getMentionSuggestions()
- 位置: L150-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UrlbarPrefs.get()`, `getTabGroupMentionId()`, `groups.push()`, `logger()`, `logger().error()`, `mentionSearch .getTabGroups()`, `mentionSearch .getTabGroups() .map()`, `mentionSearch .startQuery()`, `seen.add()`, `seen.has()`
- 条件付き依存: `if (tabGroupItems.length)` → `groups.push()`
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `deduplicated.length`, `item.id`, `item.url`, `lazy.MENTION_TYPE.TAB_OPEN`, `r1.type`, `r2.type`, `tabGroupItems.length`

## getAnchorPos()
- 位置: L220-230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `view.coordsAtPos()`
- 参照: `coordsFrom.left`, `coordsFrom.top`, `coordsTo.bottom`, `coordsTo.right`, `range.from`, `range.to`

## refocusEditorOnUnhandledPanelKey()
- 位置: L238-244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["Tab", "ArrowUp", "ArrowDown", "Enter"].includes()`, `editorElement.focus()`
- 参照: `e.detail`, `originalEvent.key`

## suppressEnterWhilePanelOpen()
- 位置: L252-256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isPanelOpen()`
- 条件付き依存: `if (isPanelOpen() && e.key === "Enter")` → `e.stopPropagation()`
- 参照: `e.key`

## setupContextMentionsButton()
- 位置: L264-302
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.addTabsClick.record()`, `String()`, `contextButton.addEventListener()`, `contextButton.removeAttribute()`, `getMentionSuggestions()`, `panelList.addEventListener()`, `panelList.getAttribute()`, `panelList.setAttribute()`, `panelList.toggle()`, `smartbarInput.querySelector()`
- 条件付き依存: `if (panelList.getAttribute("data-triggered-by") === "context-mention")` → `contextButton.setAttribute()`
- 参照: `lazy.SmartbarMentionsPanelSearch`, `panelList.anchor`, `panelList.groups`, `smartbarInput.contextWebsitesCount`, `smartbarInput.conversationTelemetryInfo`, `smartbarInput.sapLocation`, `window.browsingContext.topChromeWindow`

## setupMentionsPlugin()
- 位置: L311-557
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperties()`, `createMentionsPlugin()`, `document.l10n .formatValue()`, `document.l10n .formatValue("smartbar-mention-typing-placeholder") .then()`, `editorElement.addEventListener()`, `editorElement.closest()`, `editorElement.style.setProperty()`, `panelList.addEventListener()`

## handleMentionsChange()
- 位置: L326-337
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getMentionSuggestions()`, `text.substring()`
- 参照: `panelList.groups`

## toDOM()
- 位置: L345-353
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `node.attrs.id`, `node.attrs.label`, `node.attrs.type`

## nodeView()
- 位置: L354-366
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `CONTEXT_MENTION_TYPE.TAB_GROUP`, `node.attrs.color`, `node.attrs.id`, `node.attrs.label`, `node.attrs.type`

## onEnter()
- 位置: L367-389
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.mentionStart.record()`, `String()`, `editorElement.setAttribute()`, `getAnchorPos()`, `getMentionSuggestions()`, `panelList.setAttribute()`, `panelList.show()`
- 参照: `lazy.SmartbarMentionsPanelSearch`, `mentionData.range`, `mentionData.view`, `panelList.anchor`, `panelList.groups`, `smartbarInput.conversationTelemetryInfo`, `smartbarInput.sapLocation`, `window.browsingContext.topChromeWindow`

## onChange()
- 位置: L390-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `editorElement.toggleAttribute()`
- 参照: `lazy.SkippableTimer`, `mentionData.text.length`

## onExit()
- 位置: L406-418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `editorElement.removeAttribute()`, `panelList.hide()`
- 条件付き依存: `if (mentionChangeTimer)` → `mentionChangeTimer.cancel()`

## handleChipDisconnected()
- 位置: L421-431
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (e.detail.type === "in-line")` → `Glean.smartWindow.mentionRemove.record()`
- 条件付き依存: `if (e.detail.type === "in-line")` → `String()`
- 条件付き依存: `if (e.detail.type === "in-line")` → `plugin.mentions.getAll()`
- 参照: `e.detail.type`, `plugin.mentions.getAll().length`, `smartbarInput.conversationTelemetryInfo`, `smartbarInput.sapLocation`

## handleItemSelected()
- 位置: L433-509
- 役割: (未記入)
- 触るとき: (未記入)
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
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `refocusEditorOnUnhandledPanelKey()`

## handleEditorKeyDown()
- 位置: L513-514
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `suppressEnterWhilePanelOpen()`

## get()
- 位置: L534-534
- 役割: (未記入)
- 触るとき: (未記入)

## get()
- 位置: L537-537
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `plugin.mentions.hasMention()`

## value()
- 位置: L540-540
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `plugin.mentions.getAll()`

## value()
- 位置: L549-552
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `editorElement.textOffsetToPos()`, `plugin.mentions.insertNode()`

## setupCommandsPlugin()
- 位置: L570-733
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperties()`, `createCommandsPlugin()`, `editorElement.addEventListener()`, `editorElement.closest()`, `panelList.addEventListener()`

## isLeadingCommand()
- 位置: L577-578
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `editorElement.value.trimStart()`, `editorElement.value.trimStart().startsWith()`

## updatePanel()
- 位置: L580-592
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getCommandSuggestions()`, `panelList.setAttribute()`, `panelList.show()`
- 条件付き依存: `if (!groups.length)` → `panelList.hide()`
- 参照: `groups.length`, `panelList.anchor`, `panelList.groups`

## onExitPalette()
- 位置: L594-602
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelList.getAttribute()`
- 条件付き依存: `if (panelList.getAttribute("data-triggered-by") === COMMAND_TRIGGER)` → `panelList.hide()`
- 条件付き依存: `if (panelList.getAttribute("data-triggered-by") === COMMAND_TRIGGER)` → `panelList.removeAttribute()`

## executeCommand()
- 位置: L605-624
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.smartWindow.agentCommandSelect.record()`, `String()`, `onExitPalette()`, `panelList.groups.reduce()`, `smartbarInput.submitChat()`
- 参照: `group.items.length`, `smartbarInput.conversationTelemetryInfo`, `smartbarInput.sapLocation`

## handleItemSelected()
- 位置: L626-635
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `executeCommand()`, `panelList.getAttribute()`
- 参照: `e.detail.id`

## handlePanelKeyDown()
- 位置: L637-643
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `refocusEditorOnUnhandledPanelKey()`
- 条件付き依存: `if (e.detail?.originalEvent?.key === "Escape")` → `onExitPalette()`
- 参照: `e.detail?.originalEvent?.key`

## handleEditorKeyDown()
- 位置: L645-676
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `e.preventDefault()`, `e.stopPropagation()`, `handler()`
- 参照: `e.altKey`, `e.ctrlKey`, `e.key`, `e.metaKey`, `e.shiftKey`

## ArrowDown()
- 位置: L657-657
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelList.moveSelection()`

## ArrowUp()
- 位置: L658-658
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelList.moveSelection()`

## Enter()
- 位置: L659-664
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelList.getSelectedItem()`
- 条件付き依存: `if (selected)` → `executeCommand()`
- 参照: `selected.id`

## Escape()
- 位置: L665-665
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `onExitPalette()`

## get()
- 位置: L692-692
- 役割: (未記入)
- 触るとき: (未記入)

## onEnter()
- 位置: L699-721
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `data.text.substring()`, `isLeadingCommand()`, `updatePanel()`
- 条件付き依存: `if (isHandlingCommands)` → `Glean.smartWindow.agentCommandStart.record()`
- 条件付き依存: `if (isHandlingCommands)` → `String()`
- 条件付き依存: `if (isHandlingCommands)` → `panelList.groups.reduce()`
- 参照: `group.items.length`, `smartbarInput.conversationTelemetryInfo`, `smartbarInput.sapLocation`

## onChange()
- 位置: L722-728
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `data.text.substring()`, `isLeadingCommand()`, `updatePanel()`

## onExit()
- 位置: L729-731
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `onExitPalette()`

## createEditor()
- 位置: L746-812
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PLACEHOLDER_HINT_L10N_IDS.map()`, `container.querySelector()`, `createEditorAdapter()`, `doc.createElement()`, `document.l10n .formatValues()`, `document.l10n .formatValues(PLACEHOLDER_HINT_L10N_IDS.map(id => ({ id }))) .then()`, `editorElement.closest()`, `editorElement.setAttribute()`, `inputElement.replaceWith()`, `setupContextMentionsButton()`, `setupMentionsPlugin()`
- 条件付き依存: `if (inputElement instanceof MultilineEditor)` → `createEditorAdapter()`
- 条件付き依存: `if (smartbarInput.sapName === "smartbar")` → `plugins.push()`
- 条件付き依存: `if (smartbarInput.sapName === "smartbar")` → `setupCommandsPlugin()`
- 参照: `attr.name`, `attr.value`, `console.error`, `editorElement.className`, `editorElement.id`, `editorElement.placeholderHints`, `editorElement.plugins`, `editorElement.showPlaceholderAnimation`, `editorElement.value`, `inputElement.attributes`, `inputElement.className`, `inputElement.id`, `inputElement.ownerDocument`, `inputElement.value`, `lazy.AIWindowUI.BROWSER_ID`, `panelList.placeholderL10nId`, `panelList.sidebarMode`, `smartbarInput.sapName`, `window.browsingContext?.embedderElement?.id`

## createEditorAdapter()
- 位置: L820-848
- 役割: (未記入)
- 触るとき: (未記入)

## getSelectionBounds()
- 位置: L821-828
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `editorElement.selectionEnd`, `editorElement.selectionStart`

## composing()
- 位置: L831-833
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `editorElement.composing`

## rangeCount()
- 位置: L835-838
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getSelectionBounds()`
- 参照: `editorElement.value`

## toStringWithFormat()
- 位置: L839-845
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `editorElement.value?.substring()`, `getSelectionBounds()`
