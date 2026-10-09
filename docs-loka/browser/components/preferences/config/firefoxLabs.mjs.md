# browser/components/preferences/config/firefoxLabs.mjs

source: browser/components/preferences/config/firefoxLabs.mjs
source-hash: 440cb19ea338db06a35d4d70257e9c9747253cf3
lines: 288

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `Promise.resolve()`, `SettingGroupManager.registerGroup()`

## onNimbusUpdate()
- 位置: L32-36
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `firefoxLabs?.get()`
- 条件付き依存: `if (firefoxLabs?.get(slug))` → `document.getElementById()`
- 参照: `document.getElementById(slug).checked`

## onCheckboxChanged()
- 位置: async L44-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExperimentAPI.manager.store.get()`, `firefoxLabs.get()`
- 条件付き依存: `if (firefoxLabs.get(slug).requiresRestart)` → `window.confirmRestartPrompt()`
- 条件付き依存: `if (enrolling)` → `firefoxLabs.enroll()`
- 条件付き依存: `if (!(enrolling))` → `firefoxLabs.unenroll()`
- 条件付き依存: `if (shouldRestart)` → `Services.startup.quit()`
- 参照: `Ci.nsIAppStartup.eAttemptQuit`, `Ci.nsIAppStartup.eRestart`, `ExperimentAPI.manager.store.get(slug)?.active`, `event.target`, `firefoxLabs.get(slug).requiresRestart`, `target.checked`, `target.dataset.nimbusBranchSlug`, `target.dataset.nimbusSlug`, `target.disabled`, `window.CONFIRM_RESTART_PROMPT_RESTART_NOW`
- XPCOM: [`nsIAppStartup`](../../../../toolkit/components/startup/public/nsIAppStartup.idl.md) / `Services.startup`

## resetAllFeatures()
- 位置: L86-93
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExperimentAPI.manager.store.get()`, `firefoxLabs.all()`
- 条件付き依存: `if (enrolled)` → `firefoxLabs.unenroll()`
- 参照: `ExperimentAPI.manager.store.get(optIn.slug)?.active`, `optIn.slug`

## createDescriptionAndReset()
- 位置: L101-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.append()`, `description.append()`, `description.classList.add()`, `document.createElement()`, `document.l10n.setAttributes()`, `link.setAttribute()`, `resetButton.addEventListener()`, `resetButton.setAttribute()`
- 参照: `resetButton.id`

## renderFeatures()
- 位置: L129-188
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExperimentAPI.manager.store.get()`, `ExperimentAPI.manager.store.on()`, `Object.entries()`, `Services.obs.notifyObservers()`, `card.append()`, `card.classList.add()`, `checkbox.addEventListener()`, `checkbox.append()`, `checkbox.setAttribute()`, `description.append()`, `description.classList.add()`, `document.createDocumentFragment()`, `document.createElement()`, `document.l10n.setAttributes()`, `el.remove()`, `featuresContainer.appendChild()`, `featuresContainer.querySelectorAll()`, `featuresContainer.querySelectorAll(".featureGate").forEach()`, `fieldset.append()`, `firefoxLabs.all()`, `frag.append()`, `groups.get()`, `groups.get(optIn.firefoxLabsGroup).push()`, `groups.has()`, `link.setAttribute()`
- 条件付き依存: `if (!groups.has(optIn.firefoxLabsGroup))` → `groups.set()`
- 参照: `ExperimentAPI.manager.store.get(optIn.slug)?.active`, `checkbox.checked`, `checkbox.dataset.nimbusBranchSlug`, `checkbox.dataset.nimbusSlug`, `checkbox.id`, `description.id`, `description.slot`, `optIn.branches`, `optIn.branches[0].slug`, `optIn.firefoxLabsDescription`, `optIn.firefoxLabsDescriptionLinks`, `optIn.firefoxLabsGroup`, `optIn.firefoxLabsTitle`, `optIn.slug`
- XPCOM: `Services.obs`

## setCategoryVisibility()
- 位置: L196-210
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `document.getElementById()`
- 条件付き依存: `if ( shouldHide && document.getElementById("categories").currentView == "paneExperimental" )` → `window.gotoPref()`
- 参照: `document.getElementById("categories").currentView`, `document.getElementById("category-experimental").hidden`
- XPCOM: `Services.prefs`

## removeObservers()
- 位置: L215-225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ExperimentAPI.manager.store.off()`
- 条件付き依存: `if (observerAdded)` → `Services.obs.removeObserver()`
- 参照: `ExperimentAPI.ENROLLMENTS_UPDATED`
- XPCOM: `Services.obs`

## maybeRenderLabsRecipes()
- 位置: async L233-244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `FirefoxLabs.create()`, `renderFeatures()`, `setCategoryVisibility()`
- 参照: `firefoxLabs.count`

## queueRender()
- 位置: L251-254
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `maybeRenderLabsRecipes()`, `renderingPromise.then()`

## observe()
- 位置: L257-261
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === ExperimentAPI.ENROLLMENTS_UPDATED)` → `queueRender()`
- 参照: `ExperimentAPI.ENROLLMENTS_UPDATED`
