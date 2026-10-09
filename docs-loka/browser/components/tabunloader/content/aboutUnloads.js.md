# browser/components/tabunloader/content/aboutUnloads.js

source: browser/components/tabunloader/content/aboutUnloads.js
source-hash: db4b8531205684f512cec3fa26c292cb5592622e
lines: 127

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `console.error()`, `document.addEventListener()`

## refreshData()
- 位置: async L10-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabUnloader.getSortedTabs()`, `TabUnloader.isDiscardable()`, `document.getElementById()`, `document.querySelector()`, `fragment.querySelector()`, `fragmentRows.appendChild()`, `getHost()`, `tabTable.appendChild()`, `tabTable.deleteRow()`, `templateRow.content.cloneNode()`, `updateTimestamp()`
- 条件付き依存: `if (!sortedTabs.length)` → `document.getElementById()`
- 条件付き依存: `if (!sortedTabs.length)` → `updateTimestamp()`
- 条件付き依存: `if ("lastAccessed" in tabInfo.tab)` → `document.l10n.setAttributes()`
- 条件付き依存: `if ("memory" in tabInfo)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (tabInfo.processes)` → `document.createElement()`
- 条件付き依存: `if (procEntry.isTopLevel)` → `procLabel.classList.add()`
- 条件付き依存: `if (procInfo.tabSet.size > 1)` → `procLabel.classList.add()`
- 条件付き依存: `if (tabInfo.processes)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (tabInfo.processes)` → `row.children[6].appendChild()`
- 条件付き依存: `if (tabInfo.processes)` → `document.createTextNode()`
- 参照: `document.getElementById("button-unload").disabled`, `document.getElementById("no-unloadable-tab-message").hidden`, `procEntry.entryToProcessMap`, `procEntry.isTopLevel`, `procInfo.memory`, `procInfo.tabSet.size`, `procLabel.textContent`, `row.children`, `row.children[0].textContent`, `row.children[1].textContent`, `row.children[3].textContent`, `row.children[4].textContent`, `sortedTabs.length`, `tabInfo.memory`, `tabInfo.processes`, `tabInfo.sortWeight`, `tabInfo.tab`, `tabInfo.tab.lastAccessed`, `tabInfo.tab?.linkedBrowser?.currentURI`, `tabInfo.weight`, `tabTable.rows.length`

## getHost()
- 位置: L13-19
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `uri?.host`, `uri?.spec`

## updateTimestamp()
- 位置: L20-26
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `document.getElementById()`, `document.l10n.setAttributes()`

## onLoad()
- 位置: async L112-120
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TabUnloader.unloadLeastRecentlyUsedTab()`, `document .getElementById()`, `document .getElementById("button-unload") .addEventListener()`, `refreshData()`
