# browser/extensions/webcompat/lib/smartblock_embeds_helper.js

source: browser/extensions/webcompat/lib/smartblock_embeds_helper.js
source-hash: 0003829cee3f74ac19f55ebfc0406f1092c410fa
lines: 501

## <module>
- 役割: (未記入)

## sendMessageToAddon()
- 位置: L23-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.runtime.sendMessage()`

## addonMessageHandler()
- 位置: L27-70
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (newEmbedObserver)` → `newEmbedObserver.disconnect()`
- 条件付き依存: `if (observerTimeout)` → `clearTimeout()`
- 条件付き依存: `if (topic === "smartblock:unblock-embed")` → `embedPlaceholders.forEach()`
- 条件付き依存: `if (topic === "smartblock:unblock-embed")` → `modifiedContainer.replaceWith()`
- 条件付き依存: `if (topic === "smartblock:unblock-embed")` → `document.createElement()`
- 条件付き依存: `if (topic === "smartblock:unblock-embed")` → `document.body.appendChild()`
- 参照: `scriptElement.wrappedJSObject.src`

## createShimPlaceholders()
- 位置: async L82-394
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `disableSetPointerCaptureFor()`, `document.createElement()`, `embedContainers.forEach()`, `embedPlaceholders.push()`, `modifiedContainers.push()`, `originalContainer.replaceWith()`, `originalEmbedContainers.push()`, `placeholderDiv.attachShadow()`, `sendMessageToAddon()`, `shadowRoot .getElementById()`, `shadowRoot .getElementById("smartblock-placeholder-button") .addEventListener()`, `shadowRoot.getElementById()`
- 条件付き依存: `if (!embedContainers.length)` → `document.querySelectorAll()`
- 条件付き依存: `if (isTestShim)` → `placeholderDiv.classList.add()`
- 条件付き依存: `if (shouldShowEmbedContent)` → `document.createElement()`
- 条件付き依存: `if (shouldShowEmbedContent)` → `contentDiv.setHTML()`
- 条件付き依存: `if (shouldShowEmbedContent)` → `contentDiv.querySelectorAll("a[href]").forEach()`
- 条件付き依存: `if (shouldShowEmbedContent)` → `contentDiv.querySelectorAll()`
- 条件付き依存: `if (url.protocol !== "https:")` → `link.removeAttribute()`
- 条件付き依存: `if (shouldShowEmbedContent)` → `link.removeAttribute()`
- 条件付き依存: `if (shouldShowEmbedContent)` → `contentDiv.textContent.trim()`
- 条件付き依存: `if (!hasSanitizedContent)` → `contentDiv.querySelector()`
- 条件付き依存: `if (hasSanitizedContent)` → `document.createElement()`
- 条件付き依存: `if (hasSanitizedContent)` → `safeContentContainer.appendChild()`
- 条件付き依存: `if (hasSanitizedContent)` → `wrapperDiv.appendChild()`
- 条件付き依存: `if (isTestShim)` → `window.dispatchEvent()`
- 参照: `contentDiv.textContent.trim().length`, `document.baseURI`, `embedContainers.length`, `explanationDiv.style.cssText`, `explanationDiv.textContent`, `link.href`, `link.rel`, `link.style.cssText`, `link.target`, `originalContainer.outerHTML`, `safeContentContainer.style.cssText`, `shadowRoot.getElementById("smartblock-placeholder-button").textContent`, `shadowRoot.getElementById("smartblock-placeholder-desc").textContent`, `shadowRoot.getElementById("smartblock-placeholder-image").src`, `shadowRoot.getElementById("smartblock-placeholder-title").textContent`, `shadowRoot.innerHTML`, `url.protocol`

## createEmbedMutationObserver()
- 位置: L402-443
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `newEmbedObserver.observe()`, `node.matches()`, `setTimeout()`
- 条件付き依存: `if (node.matches(embedSelector))` → `createShimPlaceholders()`
- 条件付き依存: `if (!(node.matches(embedSelector)))` → `node.querySelectorAll()`
- 条件付き依存: `if (maybeEmbedNodeList)` → `createShimPlaceholders()`
- 条件付き依存: `if (newEmbedObserver)` → `newEmbedObserver.disconnect()`
- 参照: `Node.ELEMENT_NODE`, `document.documentElement`, `node.nodeType`

## disableSetPointerCaptureFor()
- 位置: L451-468
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`, `console.warn()`, `exportFunction()`
- 参照: `el.wrappedJSObject`

## initEmbedShim()
- 位置: L475-495
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addonMessageHandler()`, `browser.runtime.onMessage.addListener()`, `createEmbedMutationObserver()`, `createShimPlaceholders()`, `prevRanShims.add()`, `prevRanShims.has()`
