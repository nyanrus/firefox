# browser/components/enterprisepolicies/content/aboutPolicies.js

source: browser/components/enterprisepolicies/content/aboutPolicies.js
source-hash: b88e54dca2d25e4af2b969f99ab104be0533751d
lines: 558

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`

## col()
- 位置: L16-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `column.appendChild()`, `document.createElement()`, `document.createTextNode()`
- 条件付き依存: `if (className)` → `column.classList.add()`

## link()
- 位置: L26-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.appendChild()`, `column.appendChild()`, `document.createElement()`, `document.createTextNode()`, `text.toLowerCase()`
- 参照: `a.href`, `a.target`

## policyNameCol()
- 位置: L41-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `col()`
- 条件付き依存: `if (policyName && failures[policyName]?.length)` → `column.classList.add()`
- 条件付き依存: `if (policyName && failures[policyName]?.length)` → `document.createElement()`
- 条件付き依存: `if (policyName && failures[policyName]?.length)` → `marker.classList.add()`
- 条件付き依存: `if (policyName && failures[policyName]?.length)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (policyName && failures[policyName]?.length)` → `column.appendChild()`
- 参照: `failures[policyName]?.length`

## addMissingColumns()
- 位置: L55-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (rowLength < maxColumns)` → `table.rows[i].insertCell()`
- 参照: `table.rows`, `table.rows.length`, `table.rows[i].cells.length`

## generateActivePolicies()
- 位置: L86-150
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PolicyFailures.getAll()`, `addMissingColumns()`, `document.getElementById()`, `new_cont.classList.add()`
- 条件付き依存: `if (schema.properties[policyName].type == "array")` → `document.createElement()`
- 条件付き依存: `if (schema.properties[policyName].type == "array")` → `row.classList.add()`
- 条件付き依存: `if (schema.properties[policyName].type == "array")` → `row.appendChild()`
- 条件付き依存: `if (schema.properties[policyName].type == "array")` → `policyNameCol()`
- 条件付き依存: `if (schema.properties[policyName].type == "array")` → `generatePolicy()`
- 条件付き依存: `if (schema.properties[policyName].type == "object")` → `Object.keys()`
- 条件付き依存: `if (schema.properties[policyName].type == "object")` → `document.createElement()`
- 条件付き依存: `if (schema.properties[policyName].type == "object")` → `row.classList.add()`
- 条件付き依存: `if (schema.properties[policyName].type == "object")` → `row.appendChild()`
- 条件付き依存: `if (schema.properties[policyName].type == "object")` → `policyNameCol()`
- 条件付き依存: `if (schema.properties[policyName].type == "object")` → `col()`
- 条件付き依存: `if (schema.properties[policyName].type == "object")` → `generatePolicy()`
- 条件付き依存: `if (!(schema.properties[policyName].type == "object"))` → `document.createElement()`
- 条件付き依存: `if (!(schema.properties[policyName].type == "object"))` → `row.appendChild()`
- 条件付き依存: `if (!(schema.properties[policyName].type == "object"))` → `policyNameCol()`
- 条件付き依存: `if (!(schema.properties[policyName].type == "object"))` → `col()`
- 条件付き依存: `if (!(schema.properties[policyName].type == "object"))` → `JSON.stringify()`
- 条件付き依存: `if (!(schema.properties[policyName].type == "object"))` → `row.classList.add()`
- 条件付き依存: `if (!(schema.properties[policyName].type == "object"))` → `new_cont.appendChild()`
- 条件付き依存: `if (policy_count < 1)` → `document.querySelector()`
- 条件付き依存: `if (Services.policies.status == Services.policies.ACTIVE)` → `current_tab.classList.add()`
- 条件付き依存: `if (!(Services.policies.status == Services.policies.ACTIVE))` → `current_tab.classList.add()`
- 参照: `Object.keys(data[policyName]).length`, `Services.policies.ACTIVE`, `Services.policies.status`, `data[policyName].length`, `schema.properties`, `schema.properties[policyName].type`
- XPCOM: `Services.policies`

## generatePolicy()
- 位置: L157-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `row.classList.contains()`
- 条件付き依存: `if (count == data.length - 1)` → `generatePolicy()`
- 条件付き依存: `if (!(count == data.length - 1))` → `generatePolicy()`
- 条件付き依存: `if (count == data.length - 1)` → `document.createElement()`
- 条件付き依存: `if (count == data.length - 1)` → `last_row.classList.add()`
- 条件付き依存: `if (count == data.length - 1)` → `last_row.appendChild()`
- 条件付き依存: `if (count == data.length - 1)` → `col()`
- 条件付き依存: `if (!(count == data.length - 1))` → `document.createElement()`
- 条件付き依存: `if (!(count == data.length - 1))` → `new_row.classList.add()`
- 条件付き依存: `if (!(count == data.length - 1))` → `new_row.appendChild()`
- 条件付き依存: `if (!(count == data.length - 1))` → `col()`
- 条件付き依存: `if (!(Array.isArray(data)))` → `Object.keys()`
- 条件付き依存: `if (count == 0)` → `row.appendChild()`
- 条件付き依存: `if (count == 0)` → `col()`
- 条件付き依存: `if (count == 0)` → `Object.keys()`
- 条件付き依存: `if (count == Object.keys(data).length - 1)` → `generatePolicy()`
- 条件付き依存: `if (!(count == Object.keys(data).length - 1))` → `generatePolicy()`
- 条件付き依存: `if (!(count == 0))` → `Object.keys()`
- 条件付き依存: `if (count == Object.keys(data).length - 1)` → `document.createElement()`
- 条件付き依存: `if (count == Object.keys(data).length - 1)` → `last_row.appendChild()`
- 条件付き依存: `if (count == Object.keys(data).length - 1)` → `col()`
- 条件付き依存: `if (count == Object.keys(data).length - 1)` → `last_row.classList.add()`
- 条件付き依存: `if (arr_sep)` → `last_row.classList.add()`
- 条件付き依存: `if (!(count == Object.keys(data).length - 1))` → `document.createElement()`
- 条件付き依存: `if (!(count == Object.keys(data).length - 1))` → `new_row.classList.add()`
- 条件付き依存: `if (!(count == Object.keys(data).length - 1))` → `new_row.appendChild()`
- 条件付き依存: `if (!(count == Object.keys(data).length - 1))` → `col()`
- 条件付き依存: `if (!(typeof data == "object" && Object.keys(data).length))` → `row.appendChild()`
- 条件付き依存: `if (!(typeof data == "object" && Object.keys(data).length))` → `col()`
- 条件付き依存: `if (!(typeof data == "object" && Object.keys(data).length))` → `JSON.stringify()`
- 条件付き依存: `if (arr_sep)` → `row.classList.add()`
- 条件付き依存: `if (islast)` → `row.classList.add()`
- 条件付き依存: `if (!(typeof data == "object" && Object.keys(data).length))` → `new_cont.appendChild()`
- 参照: `Object.keys(data).length`, `data.length`

## generateErrors()
- 位置: L266-327
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `PolicyFailures.getAll()`, `addRow()`, `consoleStorage.getService()`, `document.getElementById()`, `listed.add()`, `listed.has()`, `new_cont.classList.add()`, `policyByMessage.get()`, `policyByMessage.set()`, `prefixes.includes()`, `storage.getEvents()`
- 条件付き依存: `if (!listed.has(message))` → `addRow()`
- 条件付き依存: `if (!flag)` → `document.getElementById()`
- 参照: `Ci.nsIConsoleAPIStorage`, `err.arguments`, `err.prefix`, `errors_tab.hidden`
- XPCOM: [`nsIConsoleAPIStorage`](../../../../dom/console/nsIConsoleAPIStorage.idl.md) / `@mozilla.org/consoleAPI-storage;1` → `ConsoleAPIStorageService` (dom/console/components.conf)

## addRow()
- 位置: L287-293
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `col()`, `document.createElement()`, `new_cont.appendChild()`, `row.appendChild()`

## legacyType()
- 位置: L337-353
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (node.format === "moz-url")` → `node.pattern?.includes()`
- 条件付き依存: `if (node.contentMediaType === "application/json")` → `Array.isArray()`
- 参照: `node.contentMediaType`, `node.format`, `node.type`

## constValues()
- 位置: L357-361
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `node.oneOf.map()`, `node.oneOf?.every()`
- 参照: `branch.const`

## legacySchemaForDisplay()
- 位置: L363-412
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Object.entries()`, `constValues()`
- 条件付き依存: `if (Array.isArray(node))` → `node.map()`
- 条件付き依存: `if (node.anyOf)` → `node.anyOf.some()`
- 条件付き依存: `if (node.anyOf)` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(branch.type))` → `types.push()`
- 条件付き依存: `if (branch.type)` → `types.push()`
- 条件付き依存: `if (node.anyOf)` → `constValues()`
- 条件付き依存: `if (values)` → `legacySchemaForDisplay()`
- 条件付き依存: `if (key === "type")` → `legacyType()`
- 条件付き依存: `if (!(key === "type"))` → `legacySchemaForDisplay()`
- 参照: `branch.enum`, `branch.format`, `branch.type`, `node.anyOf`, `rest.oneOf`, `result.enum`, `result.type`

## generateDocumentation()
- 位置: L414-492
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `col()`, `content.classList.toggle()`, `deprecated_policies.includes()`, `document.createElement()`, `document.getElementById()`, `document.l10n.setAttributes()`, `legacySchemaForDisplay()`, `link()`, `main_tbody.addEventListener()`, `main_tbody.appendChild()`, `main_tbody.classList.add()`, `new_cont.appendChild()`, `new_cont.setAttribute()`, `row.appendChild()`, `sec_tbody.classList.add()`
- 条件付き依存: `if (policySchema.properties)` → `col()`
- 条件付き依存: `if (policySchema.properties)` → `JSON.stringify()`
- 条件付き依存: `if (policySchema.properties)` → `schema_row.appendChild()`
- 条件付き依存: `if (policySchema.properties)` → `sec_tbody.appendChild()`
- 条件付き依存: `if (policySchema.items)` → `col()`
- 条件付き依存: `if (policySchema.items)` → `JSON.stringify()`
- 条件付き依存: `if (policySchema.items)` → `schema_row.appendChild()`
- 条件付き依存: `if (policySchema.items)` → `sec_tbody.appendChild()`
- 条件付き依存: `if (!(policySchema.items))` → `col()`
- 条件付き依存: `if (!(policySchema.items))` → `schema_row.appendChild()`
- 条件付き依存: `if (!(policySchema.items))` → `sec_tbody.appendChild()`
- 条件付き依存: `if (policySchema.enum)` → `document.createElement()`
- 条件付き依存: `if (policySchema.enum)` → `col()`
- 条件付き依存: `if (policySchema.enum)` → `JSON.stringify()`
- 条件付き依存: `if (policySchema.enum)` → `enum_row.appendChild()`
- 条件付き依存: `if (policySchema.enum)` → `sec_tbody.appendChild()`
- 参照: `column.colSpan`, `policySchema.enum`, `policySchema.items`, `policySchema.properties`, `policySchema.type`, `schema.properties`, `this.nextElementSibling`

## window.onload()
- 位置: L495-526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.getActivePolicies()`, `document.getElementById()`, `generateActivePolicies()`, `generateDocumentation()`, `generateErrors()`, `menu.addEventListener()`, `onChangeView()`, `onHashChange()`, `window.addEventListener()`
- 参照: `e.target`
- XPCOM: `Services.policies`

## onHashChange()
- 位置: L510-519
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (location.hash)` → `document.getElementById()`
- 条件付き依存: `if (location.hash)` → `location.hash.substring()`
- 条件付き依存: `if (sectionButton)` → `sectionButton.activate()`
- 参照: `location.hash`

## onChangeView()
- 位置: L528-545
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.getAttribute()`, `button.getAttribute("id").substring()`, `button.textContent.trim()`, `content.classList.add()`, `current_tab.classList.remove()`, `document.getElementById()`, `document.querySelector()`, `restoreScrollPosition()`, `saveScrollPosition()`
- 参照: `"category-".length`, `content.hidden`, `current_tab.hidden`, `current_tab.id`, `location.hash`, `title.textContent`

## saveScrollPosition()
- 位置: L548-551
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 参照: `mainContent.scrollTop`

## restoreScrollPosition()
- 位置: L553-557
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`, `mainContent.scrollTo()`
