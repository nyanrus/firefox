# browser/extensions/webcompat/about-compat/aboutCompat.js

source: browser/extensions/webcompat/about-compat/aboutCompat.js
source-hash: d3b3c107cb77b7ff6638cef36ecd1fd1a4117868
lines: 333

## <module>
- 役割: (未記入)
- 呼び出し先: `Promise.all()`, `Promise.all([ browser.runtime.sendMessage("getAllInterventions"), DOMContentLoadedPromise, ]).then()`, `browser.runtime.sendMessage()`, `connect()`, `document.addEventListener()`, `document.body.addEventListener()`, `redraw()`, `resolve()`

## connect()
- 位置: L14-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.runtime.connect()`, `port.onDisconnect.addListener()`, `port.onMessage.addListener()`

## send()
- 位置: async L24-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.reject()`
- 条件付き依存: `if (port)` → `port.postMessage()`

## $()
- 位置: L34-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`

## onMessageFromAddon()
- 位置: async L88-152
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("interventionsChanged" in msg)` → `document.querySelector()`
- 条件付き依存: `if ("interventionsChanged" in msg)` → `section.querySelector()`
- 条件付き依存: `if ( msg.interventionsChanged === false || section.querySelector("[data-l10n-id=text-disabled-in-about-config]") )` → `redrawSection()`
- 条件付き依存: `if ( msg.interventionsChanged === false || section.querySelector("[data-l10n-id=text-disabled-in-about-config]") )` → `$()`
- 条件付き依存: `if (!( msg.interventionsChanged === false || section.querySelector("[data-l10n-id=text-disabled-in-about-config]") ))` → `createArticle()`
- 条件付き依存: `if (!( msg.interventionsChanged === false || section.querySelector("[data-l10n-id=text-disabled-in-about-config]") ))` → `document.querySelector()`
- 条件付き依存: `if (!( msg.interventionsChanged === false || section.querySelector("[data-l10n-id=text-disabled-in-about-config]") ))` → `oldArticle?.querySelector()`
- 条件付き依存: `if (domain == oldDomain)` → `oldArticle.parentNode.replaceChild()`
- 条件付き依存: `if (!( msg.interventionsChanged === false || section.querySelector("[data-l10n-id=text-disabled-in-about-config]") ))` → `oldArticle?.remove()`
- 条件付き依存: `if (!( msg.interventionsChanged === false || section.querySelector("[data-l10n-id=text-disabled-in-about-config]") ))` → `whereToInsert.querySelector()`
- 条件付き依存: `if (!( msg.interventionsChanged === false || section.querySelector("[data-l10n-id=text-disabled-in-about-config]") ))` → `section.insertBefore()`
- 条件付き依存: `if ("shimsChanged" in msg)` → `updateShimSections()`
- 条件付き依存: `if ("toggling" in msg)` → `$()`
- 参照: `button.disabled`, `config.hidden`, `config.id`, `location.hash`, `msg.interventionsChanged`, `msg.shimsChanged`, `msg.toggling`, `oldArticle?.querySelector("span").innerText`, `section.firstElementChild`, `whereToInsert.nextElementSibling`, `whereToInsert.nodeName`, `whereToInsert.querySelector("span").innerText`

## redraw()
- 位置: L154-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `$()`, `redrawSection()`, `updateShimSections()`
- 参照: `location.hash`

## clearSectionAndAddMessage()
- 位置: L164-178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `article.appendChild()`, `article.remove()`, `document.createElement()`, `document.l10n.setAttributes()`, `section.appendChild()`, `section.querySelectorAll()`, `section.querySelectorAll("article").forEach()`
- 参照: `article.className`, `article.id`

## hideMessagesOnSection()
- 位置: L180-184
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `article.remove()`, `section.querySelectorAll()`, `section.querySelectorAll("article.message").forEach()`

## updateShimSections()
- 位置: L186-267
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `article.appendChild()`, `article.setAttribute()`, `document.createElement()`, `document.l10n.setAttributes()`, `document.querySelector()`, `document.querySelectorAll()`, `section.querySelector()`, `span.appendChild()`
- 条件付き依存: `if (disabledReason === "globalPref")` → `clearSectionAndAddMessage()`
- 条件付き依存: `if (row)` → `row.replaceWith()`
- 条件付き依存: `if (!(row))` → `section.appendChild()`
- 条件付き依存: `if (!section.querySelector("article:not(.message)"))` → `clearSectionAndAddMessage()`
- 条件付き依存: `if (!(!section.querySelector("article:not(.message)")))` → `hideMessagesOnSection()`
- 参照: `a.href`, `a.target`, `section.id`, `sections.length`, `span.innerText`

## redrawSection()
- 位置: L269-301
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `article.remove()`, `createArticle()`, `df.appendChild()`, `document.createDocumentFragment()`, `section.appendChild()`, `section.querySelectorAll()`, `section.querySelectorAll("article").forEach()`
- 条件付き依存: `if (noEntriesMessage)` → `document.createElement()`
- 条件付き依存: `if (noEntriesMessage)` → `df.appendChild()`
- 条件付き依存: `if (noEntriesMessage)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (noEntriesMessage)` → `article.appendChild()`
- 条件付き依存: `if (noEntriesMessage)` → `section.appendChild()`
- 参照: `data.length`, `row.hidden`, `section.id`

## createArticle()
- 位置: L303-330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `article.appendChild()`, `article.setAttribute()`, `document.createElement()`, `document.l10n.setAttributes()`, `span.appendChild()`
- 参照: `a.href`, `a.target`, `row.active`, `row.bug`, `row.domain`, `row.id`, `span.innerText`
