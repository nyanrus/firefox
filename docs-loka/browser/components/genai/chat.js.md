# browser/components/genai/chat.js

source: browser/components/genai/chat.js
source-hash: 4ecfb821003054875ed7ba9af3b7d2b45d0c21b8
lines: 597

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `Glean.genaiChatbot.sidebarCloseClick.record()`, `Glean.genaiChatbot.sidebarToggle.record()`, `JSON.stringify()`, `Object.freeze()`, `Services.prefs.getBoolPref()`, `Services.urlFormatter.formatURLPref()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `addEventListener()`, `closeSidebar()`, `console.error()`, `document .getElementById()`, `document .getElementById("summarize-button") .addEventListener()`, `document.getElementById()`, `document.getElementById("header-close").addEventListener()`, `document.querySelector()`, `document.querySelector("#browser-container browser").focus()`, `lazy.GenAI.getProviderId()`, `lazy.GenAI.summarizeCurrentPage()`, `node.menu?.remove()`, `reject()`, `renderChat()`, `renderMore()`, `renderProviders()`, `resolve()`, `topChromeWindow.gBrowser.addProgressListener()`, `topChromeWindow.gBrowser.removeProgressListener()`, `updateSummarizeButton()`, `window.addEventListener()`

## closeSidebar()
- 位置: L113-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.hide()`
- 参照: `controller._state.launcherHiddenWithPanel`, `topChromeWindow.SidebarController`

## openLink()
- 位置: L123-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createNullPrincipal()`, `topChromeWindow.openLinkIn()`
- XPCOM: `Services.scriptSecurityManager`

## request()
- 位置: L129-139
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.scriptSecurityManager.createNullPrincipal()`, `console.error()`, `node.chat.fixupAndLoadURIString()`
- 参照: `lazy.providerPref`
- XPCOM: `Services.scriptSecurityManager`

## renderChat()
- 位置: L141-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.setAttribute()`, `browserContainer.appendChild()`, `document.createXULElement()`, `document.getElementById()`

## renderProviders()
- 位置: async L153-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.genaiChatbot.provider.set()`, `addOption()`, `document.createElement()`, `document.getElementById()`, `document.hasFocus()`, `document.l10n.setAttributes()`, `lazy.GenAI.chatProviders.forEach()`, `lazy.GenAI.getProviderId()`, `request()`, `select.appendChild()`
- 条件付き依存: `if (!selected)` → `addOption()`
- 条件付き依存: `if (!lazy.providerPref)` → `showOnboarding()`
- 条件付き依存: `if (renderProviders.lastId && document.hasFocus())` → `Glean.genaiChatbot.providerChange.record()`
- 参照: `data.hidden`, `data.name`, `document.visibilityState`, `lazy.providerPref`, `option.hidden`, `option.selected`, `renderProviders.lastId`, `select.innerHTML`

## addOption()
- 位置: L163-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `select.appendChild()`
- 参照: `option.textContent`, `option.value`

## renderMore()
- 位置: L211-292
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.genaiChatbot.sidebarMoreMenuClick.record()`, `Glean.genaiChatbot.sidebarMoreMenuDisplay.record()`, `button.addEventListener()`, `button.setAttribute()`, `command()`, `document.getElementById()`, `document.l10n.setAttributes()`, `item.addEventListener()`, `lazy.GenAI.chatProviders.get()`, `lazy.GenAI.getProviderId()`, `menu.appendChild()`, `menu.openPopup()`, `topDoc.createXULElement()`, `topDoc.getElementById()`
- 条件付き依存: `if (!menu)` → `topDoc .getElementById("mainPopupSet") .appendChild()`
- 条件付き依存: `if (!menu)` → `topDoc .getElementById()`
- 条件付き依存: `if (!menu)` → `topDoc.createXULElement()`
- 条件付き依存: `if (!menu)` → `menu.addEventListener()`
- 条件付き依存: `if (!menu)` → `button.setAttribute()`
- 条件付き依存: `if (checked !== undefined)` → `item.setAttribute()`
- 条件付き依存: `if (checked)` → `item.setAttribute()`
- 参照: `command.name`, `lazy.GenAI.chatProviders.get(lazy.providerPref)?.name`, `lazy.providerPref`, `lazy.shortcutsPref`, `menu.id`, `menu.innerHTML`, `node.menu`, `topChromeWindow.document`

## reload()
- 位置: L239-241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `request()`

## show_shortcuts()
- 位置: L247-249
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## hide_shortcuts()
- 位置: L255-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## about()
- 位置: L264-266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `openLink()`
- 参照: `lazy.supportLink`

## handleChange()
- 位置: L294-317
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (value == "")` → `showOnboarding()`
- 条件付き依存: `if (value == "")` → `Glean.genaiChatbot.sidebarProviderMenuClick.record()`
- 条件付き依存: `if (value == "")` → `lazy.GenAI.getProviderId()`
- 条件付き依存: `if (!(value == ""))` → `Services.prefs.setStringPref()`
- 条件付き依存: `if (!(value == ""))` → `topChromeWindow.dispatchEvent()`
- 参照: `lazy.providerPref`, `node.provider`, `target.value`
- XPCOM: `Services.prefs`

## updateSummarizeButton()
- 位置: L321-325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `lazy.GenAI.getPageUrl()`
- 参照: `document.getElementById("summarize-button").disabled`, `topChromeWindow.gBrowser.selectedBrowser`

## onLocationChange()
- 位置: L328-332
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (webProgress.isTopLevel)` → `updateSummarizeButton()`
- 参照: `webProgress.isTopLevel`

## showOnboarding()
- 位置: L392-587
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `document.body.prepend()`, `document.createElement()`, `document.getElementById()`, `document.getElementById(root.id)?.remove()`, `document.head.appendChild()`, `history.replaceState()`, `lazy.GenAI.chatProviders.forEach()`
- 条件付き依存: `if (!data.hidden)` → `providerConfigs.set()`
- 参照: `data.hidden`, `data.id`, `lazy.sidebarVisibilityPref`, `root.id`, `root.nextElementSibling`, `script.src`, `sibling.id`, `sibling.inert`, `sibling.nextElementSibling`

## AWEvaluateScreenTargeting()
- 位置: L427-429
- 役割: (未記入)
- 触るとき: (未記入)

## AWFinish()
- 位置: L430-448
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `root.remove()`, `showOnboarding.resolve()`
- 条件付き依存: `if (lazy.providerPref == "")` → `closeSidebar()`
- 参照: `lazy.providerPref`, `root.nextElementSibling`, `showOnboarding.resolve`, `sibling.inert`, `sibling.nextElementSibling`

## AWGetFeatureConfig()
- 位置: L449-469
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `[...providerConfigs.values()].map()`, `onboarding.screens.slice()`, `providerConfigs.values()`
- 参照: `ACTIONS.CHATBOT_SELECT`, `config.id`, `config.name`, `config.tooltipId`, `lazy.onboardingConfig`, `onboarding.screens`, `onboarding.screens[0].content.tiles`

## AWGetInstalledAddons()
- 位置: L470-470
- 役割: (未記入)
- 触るとき: (未記入)

## AWGetSelectedTheme()
- 位置: L471-476
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.querySelector()`
- 参照: `primary.disabled`

## AWSendEventTelemetry()
- 位置: L477-512
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.genaiChatbot.onboardingClose.record()`, `Glean.genaiChatbot.onboardingFinish.record()`, `Glean.genaiChatbot.onboardingLearnMore.record()`, `Glean.genaiChatbot.onboardingProviderChoiceDisplayed.record()`, `Glean.genaiChatbot.onboardingProviderSelection.record()`, `Glean.genaiChatbot.onboardingProviderTerms.record()`, `lazy.GenAI.getProviderId()`, `source.startsWith()`
- 参照: `lazy.providerPref`, `window.AWSendEventTelemetry`, `window.AWSendEventTelemetry.provider`

## AWSendToParent()
- 位置: L513-585
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setStringPref()`, `div.closest()`, `div.closest("label").querySelector()`, `div.querySelector()`, `document.querySelector()`, `document.querySelectorAll()`, `document.querySelectorAll("label .text div").forEach()`, `lazy.SpecialMessageActions.handleAction()`, `openLink()`, `providerConfigs.get()`, `request()`
- 条件付き依存: `if (links && links.dataset.l10nId != config.linksId)` → `links.appendChild()`
- 条件付き依存: `if (links && links.dataset.l10nId != config.linksId)` → `document.createElement()`
- 条件付き依存: `if (links && links.dataset.l10nId != config.linksId)` → `link.setAttribute()`
- 条件付き依存: `if (links && links.dataset.l10nId != config.linksId)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!links._listenerAdded)` → `links?.addEventListener()`
- 参照: `ACTIONS.CHATBOT_PERSIST`, `ACTIONS.CHATBOT_REVERT`, `ACTIONS.CHATBOT_SELECT`, `ACTIONS.CHATBOT_SUPPORT`, `ACTIONS.OPEN_URL`, `a.tabIndex`, `action.type`, `config.id`, `config.linksId`, `config.url`, `div.closest("label").querySelector("input").value`, `div.scrollHeight`, `div.style.maxHeight`, `document.querySelector(".primary").disabled`, `lazy.supportLink`, `link.dataset.l10nName`, `link.href`, `links._listenerAdded`, `links.dataset.l10nId`, `links.innerHTML`, `providerConfigs.get(value).url`
- XPCOM: `Services.prefs`

## handleLink()
- 位置: L565-571
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (href)` → `ev.preventDefault()`
- 条件付き依存: `if (href)` → `openLink()`
- 参照: `ev.target`
