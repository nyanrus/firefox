# browser/components/aboutwelcome/content/aboutwelcome.bundle.js

source: browser/components/aboutwelcome/content/aboutwelcome.bundle.js
source-hash: 750357b241b3177eed00a6d1e2a48dc525bcf18e
lines: 7320

## <module>
- 役割: (未記入)
- 呼び出し先: `(() => { /******/ __webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop)) /******/ })()`, `(function(f){if(true){module.exports=f()}else { var g; }})()`, `Function.call.bind()`, `Object()`, `Object.fromEntries()`, `Symbol.for()`, `TILE_STYLES.includes()`, `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.CONFIGURABLE_STYLES.map()`, `__webpack_require__()`, `__webpack_require__.d()`, `__webpack_require__.n()`, `__webpack_require__.r()`, `document.querySelector()`, `hasOwnProperty.call()`, `mount()`, `performance.mark()`, `prop_types_prop_types__WEBPACK_IMPORTED_MODULE_13___default()`, `prop_types_prop_types__WEBPACK_IMPORTED_MODULE_13___default().arrayOf()`, `prop_types_prop_types__WEBPACK_IMPORTED_MODULE_13___default().exact()`, `prop_types_prop_types__WEBPACK_IMPORTED_MODULE_13___default().oneOf()`, `prop_types_prop_types__WEBPACK_IMPORTED_MODULE_13___default().oneOfType()`, `prop_types_prop_types__WEBPACK_IMPORTED_MODULE_13___default().shape()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `require()`, `shouldUseNative()`, `toObject()`

## MultiStageUtils()
- 位置: L30-30
- 役割: (未記入)
- 触るとき: (未記入)

## handleUserAction()
- 位置: L45-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.AWSendToParent()`

## handleImpressionAction()
- 位置: L48-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `Promise.resolve( window.AWSendImpressionAction?.({ action, message_id: messageId, screen_id: screenId, }) ).then()`, `window.AWSendImpressionAction()`
- 条件付き依存: `if (fired)` → `this.sendActionTelemetry()`
- 参照: `action.type`

## sendImpressionTelemetry()
- 位置: L63-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.AWSendEventTelemetry()`

## sendActionTelemetry()
- 位置: L73-89
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.AWSendEventTelemetry()`

## sendDismissTelemetry()
- 位置: L90-96
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (page !== "spotlight")` → `this.sendActionTelemetry()`

## fetchFlowParams()
- 位置: async L97-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fetch()`
- 条件付き依存: `if (response.status === 200)` → `response.json()`
- 条件付き依存: `if (!(response.status === 200))` → `console.error()`
- 参照: `response.status`

## sendEvent()
- 位置: L114-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.dispatchEvent()`

## getLoadingStrategyFor()
- 位置: L122-124
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `url?.startsWith()`

## handleCampaignAction()
- 位置: L125-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.AWSendToParent()`, `window.AWSendToParent("HANDLE_CAMPAIGN_ACTION", action).then()`
- 条件付き依存: `if (handled)` → `this.sendActionTelemetry()`

## getValidStyle()
- 位置: L137-149
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Object.keys(style) .filter()`, `Object.keys(style) .filter( key => validStyles.includes(key) || (allowVars && key.startsWith("--")) ) .reduce()`, `key.startsWith()`, `validStyles.includes()`

## getTileStyle()
- 位置: L150-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getValidStyle()`
- 参照: `tile?.style`, `tile?.tiles?.style`

## CARD_STACK_TRANSITION_OUT_TIME()
- 位置: L170-170
- 役割: (未記入)
- 触るとき: (未記入)

## MultiStageAboutWelcome()
- 位置: L171-171
- 役割: (未記入)
- 触るとき: (未記入)

## ProgressBar()
- 位置: L172-172
- 役割: (未記入)
- 触るとき: (未記入)

## SecondaryCTA()
- 位置: L173-173
- 役割: (未記入)
- 触るとき: (未記入)

## StepsIndicator()
- 位置: L174-174
- 役割: (未記入)
- 触るとき: (未記入)

## WelcomeScreen()
- 位置: L175-175
- 役割: (未記入)
- 触るとき: (未記入)

## MultiStageAboutWelcome()
- 位置: L204-579
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,_LanguageSwitcher__WEBPACK_IMPORTED_MODULE_5__.useLanguageSwitcher)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useState)()`, `(async () => { let addons = await window.AWGetInstalledAddons(); setInstalledAddons(addons); })()`, `(async () => { let theme = await window.AWGetSelectedTheme(); setInitialTheme(theme); setActiveTheme(theme); })()`, `console.error()`, `defaultScreens.filter()`, `filteredScreens.forEach()`, `filteredScreens.map()`, `filteredScreens.map(({ id }) => id?.split("_")[1]?.[0]).join()`, `id?.split()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `refreshActiveThemeId()`, `screens.find()`, `screens.map()`, `screens.slice()`, `screensVisited.concat()`, `screensVisited.find()`, `setActiveTheme()`, `setDidMount()`, `setInitialTheme()`, `setInstalledAddons()`, `setPreviousOrder()`, `setScreens()`, `window.AWEvaluateScreenTargeting()`, `window.AWGetInstalledAddons()`, `window.AWGetSelectedTheme()`, `window.AWGetUnhandledCampaignAction()`, `window.AWGetUnhandledCampaignAction?.().then()`, `window.addEventListener()`, `window.matchMedia()`, `window.removeEventListener()`
- 条件付き依存: `if (!didFilter.current)` → `setReady()`
- 条件付き依存: `if (typeof action === "string")` → `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.handleCampaignAction()`
- 条件付き依存: `if (index === order)` → `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.sendImpressionTelemetry()`
- 条件付き依存: `if (index === order)` → `(0,_ContentTiles__WEBPACK_IMPORTED_MODULE_4__.getTileImpressionContext)()`
- 条件付き依存: `if (screen.content?.impression_action)` → `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.handleImpressionAction()`
- 条件付き依存: `if (index === order)` → `window.AWAddScreenImpression()`
- 条件付き依存: `if (props.updateHistory && index > window.history.state)` → `window.history.pushState()`
- 条件付き依存: `if (metricsFlowUri)` → `setFlowParams()`
- 条件付き依存: `if (metricsFlowUri)` → `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.fetchFlowParams()`
- 条件付き依存: `if (transition === "in")` → `requestAnimationFrame()`
- 条件付き依存: `if (transition === "in")` → `setTransition()`
- 条件付き依存: `if (state)` → `setScreenIndex()`
- 条件付き依存: `if (state)` → `Math.min()`
- 条件付き依存: `if (state)` → `setPreviousOrder()`
- 条件付き依存: `if (props.updateHistory)` → `window.addEventListener()`
- 条件付き依存: `if (props.updateHistory)` → `window.removeEventListener()`
- 参照: `_ContentTiles__WEBPACK_IMPORTED_MODULE_4__.getTileImpressionContext`, `_LanguageSwitcher__WEBPACK_IMPORTED_MODULE_5__.useLanguageSwitcher`, `currentScreen.above_button_steps_indicator`, `currentScreen.advance_on_experiment_load`, `currentScreen.auto_advance`, `currentScreen.content`, `currentScreen.content.isRtamo`, `currentScreen.force_hide_steps_indicator`, `currentScreen.id`, `defaultScreens?.[0]?.content?.position`, `didFilter.current`, `filtered.id`, `props.addonIconURL`, `props.addonId`, `props.addonName`, `props.addonType`, `props.addonURL`, `props.appAndSystemLocaleInfo`, `props.ariaRole`, `props.backdrop`, `props.gateInitialPaint`, `props.message_id`, `props.requireAction`, `props.startScreen`, `props.themeScreenshots`, `props.transitions`, `props.updateHistory`, `props.utm_term`, `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useRef`, `react__WEBPACK_IMPORTED_MODULE_0__.useState`, `react__WEBPACK_IMPORTED_MODULE_0___default().Fragment`, `s.id`, `screen.content.impression_action`, `screen.content?.impression_action`, `screen.content?.tiles`, `screen.id`, `screens.length`, `upcomingScreen.id`, `v.id`, `window.history`, `window.history.state`, `window.matchMedia`, `window.matchMedia("(prefers-reduced-motion: reduce)").matches`

## handleTransition()
- 位置: L314-342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setTimeout()`, `setTransition()`
- 条件付き依存: `if (isCardStack && !goBack && index >= screens.length - 1)` → `window.AWFinish()`
- 条件付き依存: `if (goBack)` → `setTransition()`
- 条件付き依存: `if (goBack)` → `setScreenIndex()`
- 条件付き依存: `if (index < screens.length - 1)` → `setTransition()`
- 条件付き依存: `if (index < screens.length - 1)` → `setScreenIndex()`
- 条件付き依存: `if (!(index < screens.length - 1))` → `window.AWFinish()`
- 参照: `props.transitions`, `screens.length`

## handler()
- 位置: L352-363
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `setScreenIndex()`, `setTimeout()`, `setTransition()`
- 参照: `props.transitions`, `screens.length`

## toggleAnimationsPaused()
- 位置: L413-413
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setAnimationsPaused()`

## refreshActiveThemeId()
- 位置: async L429-434
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.AWGetActiveThemeId()`
- 条件付き依存: `if (mounted)` → `setActiveThemeId()`

## setActiveMultiSelect()
- 位置: L473-484
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setActiveMultiSelects()`, `valueOrFn()`
- 参照: `currentScreen.id`

## setScreenMultiSelects()
- 位置: L485-496
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setMultiSelects()`, `valueOrFn()`
- 参照: `currentScreen.id`

## setActiveSingleSelectSelection()
- 位置: L497-508
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setActiveSingleSelectSelections()`, `valueOrFn()`
- 参照: `currentScreen.id`

## setPinnedSite()
- 位置: L509-514
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setPinnedSites()`
- 参照: `currentScreen.id`

## setTextInput()
- 位置: L515-526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setTextInputs()`
- 参照: `currentScreen.id`

## renderSingleSecondaryCTAButton()
- 位置: L580-658
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["split", "callout", "center-large", "card-stack"].includes()`, `computeDisabled()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `_SubmenuButton__WEBPACK_IMPORTED_MODULE_6__.SubmenuButton`, `button?.disabled`, `button?.has_arrow_icon`, `button?.label`, `button?.style`, `button?.text`, `content.position`, `content.submenu_button?.attached_to`, `content.tiles?.type`

## computeDisabled()
- 位置: L602-623
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (disabledValue === "hasTextInput")` → `Object.values(textInputs).every()`
- 条件付き依存: `if (disabledValue === "hasTextInput")` → `Object.values()`
- 条件付き依存: `if (disabledValue === "hasTextInput")` → `input.value.trim()`
- 参照: `activeMultiSelect[key]?.length`, `input.isValid`, `input.value.trim().length`

## shimmedHandleAction()
- 位置: L633-638
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleAction()`
- 条件付き依存: `if (isArrayItem && button?.action)` → `handleAction()`
- 参照: `button.action`, `button?.action`

## SecondaryCTA()
- 位置: L659-720
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `console.error()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().useEffect()`, `react__WEBPACK_IMPORTED_MODULE_0___default().useMemo()`, `react__WEBPACK_IMPORTED_MODULE_0___default().useState()`, `renderSingleSecondaryCTAButton()`, `setVisibleButtons()`, `window.AWEvaluateAttributeTargeting()`
- 条件付き依存: `if (!button?.targeting)` → `filteredButtons.push()`
- 条件付き依存: `if (shouldShowButton)` → `filteredButtons.push()`
- 条件付き依存: `if (Array.isArray(buttonData))` → `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 条件付き依存: `if (Array.isArray(buttonData))` → `react__WEBPACK_IMPORTED_MODULE_0___default()`
- 条件付き依存: `if (Array.isArray(buttonData))` → `visibleButtons.map()`
- 条件付き依存: `if (Array.isArray(buttonData))` → `renderSingleSecondaryCTAButton()`
- 参照: `button.targeting`, `button?.targeting`, `props.activeMultiSelect`, `props.handleAction`, `props.textInputs`, `visibleButtons.length`

## StepsIndicator()
- 位置: L721-732
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `steps.push()`
- 参照: `props.order`, `props.totalNumberOfScreens`

## ProgressBar()
- 位置: L733-751
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `react__WEBPACK_IMPORTED_MODULE_0___default().useState()`, `setProgress()`
- 参照: `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`

## WelcomeScreen.constructor()
- 位置: L753-756
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.handleAction.bind()`
- 参照: `this.handleAction`

## WelcomeScreen.handleOpenURL()
- 位置: L757-797
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.handleUserAction()`
- 条件付き依存: `if (type === "OPEN_URL")` → `(0,_lib_addUtmParams_mjs__WEBPACK_IMPORTED_MODULE_7__.addUtmParams)()`
- 条件付き依存: `if (action.addFlowParams && flowParams)` → `url.searchParams.append()`
- 条件付き依存: `if (type === "OPEN_URL")` → `url.toString()`
- 参照: `_lib_addUtmParams_mjs__WEBPACK_IMPORTED_MODULE_7__.BASE_PARAMS`, `_lib_addUtmParams_mjs__WEBPACK_IMPORTED_MODULE_7__.addUtmParams`, `action.addFlowParams`, `data.args`, `data?.extraParams`, `flowParams.deviceId`, `flowParams.flowBeginTime`, `flowParams.flowId`

## WelcomeScreen.handleMigrationIfNeeded()
- 位置: async L798-804
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `hasMigrate()`
- 条件付き依存: `if (hasMigrate(action))` → `window.AWWaitForMigrationClose()`
- 条件付き依存: `if (hasMigrate(action))` → `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.sendActionTelemetry()`
- 参照: `props.messageId`

## hasMigrate()
- 位置: L799-799
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.data?.actions?.some()`
- 参照: `a.type`

## WelcomeScreen.applyThemeIfNeeded()
- 位置: L805-812
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.props.setActiveTheme()`, `window.AWSelectTheme()`
- 参照: `action.theme`, `event.currentTarget.value`, `this.props.initialTheme`

## WelcomeScreen.handlePickerAction()
- 位置: L813-826
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`
- 条件付き依存: `if (opt.id === value)` → `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.handleUserAction()`
- 参照: `opt.action`, `opt.id`, `this.props.content.tiles`, `tile.data`, `tile?.data`

## WelcomeScreen.resolveActionFromContent()
- 位置: L827-848
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `["submenu_button", "more_button", "tile_button"].includes()`
- 条件付き依存: `if (Array.isArray(targetContent))` → `tile.data.find()`
- 参照: `content.languageSwitcher`, `content.tiles`, `event.action`, `matchedTile.action`, `matchedTile?.action`, `t.id`, `targetContent.action`

## WelcomeScreen.handleAction()
- 位置: async L849-939
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `JSON.stringify()`, `Object.values()`, `["OPEN_URL", "SHOW_FIREFOX_ACCOUNTS"].includes()`, `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.sendActionTelemetry()`, `event.currentTarget.getAttribute()`, `shouldDoBehavior()`, `this.applyThemeIfNeeded()`, `this.resolveActionFromContent()`
- 条件付き依存: `if (!action)` → `console.error()`
- 条件付き依存: `if (value === "dismiss_button" && !event.name || action.sendDismissTelemetry)` → `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.sendDismissTelemetry()`
- 条件付き依存: `if (action.collectSelect)` → `this.setMultiSelectActions()`
- 条件付き依存: `if (action.collectTextInput && Object.values(props.textInputs).length)` → `this.setTextInputActions()`
- 条件付き依存: `if (["OPEN_URL", "SHOW_FIREFOX_ACCOUNTS"].includes(action.type))` → `this.handleOpenURL()`
- 条件付き依存: `if (action.type === "INSTALL_ADDON_FROM_URL")` → `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.handleUserAction()`
- 条件付き依存: `if (action.type)` → `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.handleUserAction()`
- 条件付き依存: `if (action.type === "FXA_SIGNIN_FLOW")` → `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.sendActionTelemetry()`
- 条件付き依存: `if (action.type)` → `this.handleMigrationIfNeeded()`
- 条件付き依存: `if (action.picker)` → `this.handlePickerAction()`
- 条件付き依存: `if (action.persistActiveTheme)` → `this.props.setInitialTheme()`
- 条件付き依存: `if (shouldDoBehavior(action.navigate))` → `props.navigate()`
- 条件付き依存: `if (action.advance_screens)` → `shouldDoBehavior()`
- 条件付き依存: `if (shouldDoBehavior(action.advance_screens.behavior ?? true))` → `window.AWAdvanceScreens()`
- 条件付き依存: `if (shouldDoBehavior(action.dismiss))` → `window.AWFinish()`
- 参照: `Object.values(props.textInputs).length`, `action.advance_screens`, `action.advance_screens.behavior`, `action.collectContentToggleState`, `action.collectSelect`, `action.collectTextInput`, `action.data`, `action.data?.url`, `action.dismiss`, `action.goBack`, `action.navigate`, `action.needsAwait`, `action.persistActiveTheme`, `action.picker`, `action.sendDismissTelemetry`, `action.type`, `context.contentToggleState`, `event.currentTarget.value`, `event.name`, `event.source`, `props.UTMTerm`, `props.addonURL`, `props.contentToggleChecked`, `props.flowParams`, `props.isRtamo`, `props.messageId`, `props.textInputs`, `this.props.activeTheme`

## shouldDoBehavior()
- 位置: L913-922
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`
- 参照: `action.needsAwait`

## WelcomeScreen.setMultiSelectActions()
- 位置: L940-1003
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `Object.values()`, `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.sendActionTelemetry()`, `action.data.actions.unshift()`, `value.flat()`
- 条件付き依存: `if (action.type !== "MULTI_ACTION")` → `console.error()`
- 条件付き依存: `if (!Array.isArray(action.data?.actions))` → `console.error()`
- 条件付き依存: `if (props.content?.tiles)` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(props.content.tiles))` → `props.content.tiles.forEach()`
- 条件付き依存: `if (!(Array.isArray(props.content.tiles)))` → `processTile()`
- 参照: `action.data`, `action.data?.actions`, `action.type`, `props.activeMultiSelect`, `props.content.tiles`, `props.content?.tiles`, `props.messageId`

## processTile()
- 位置: L967-984
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `activeSelections.includes()`
- 条件付き依存: `if (checkboxAction)` → `multiSelectActions.push()`
- 参照: `checkbox.action`, `checkbox.checkedAction`, `checkbox.id`, `checkbox.uncheckedAction`, `props.activeMultiSelect`, `tile.data`, `tile?.type`

## WelcomeScreen.setTextInputActions()
- 位置: L1004-1060
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `action.data.actions.unshift()`
- 条件付き依存: `if (action.type !== "MULTI_ACTION")` → `console.error()`
- 条件付き依存: `if (!Array.isArray(action.data?.actions))` → `console.error()`
- 条件付き依存: `if (props.content?.tiles)` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(props.content.tiles))` → `props.content.tiles.entries()`
- 条件付き依存: `if (Array.isArray(props.content.tiles))` → `processTile()`
- 条件付き依存: `if (!(Array.isArray(props.content.tiles)))` → `processTile()`
- 参照: `action.data`, `action.data?.actions`, `action.type`, `props.content.tiles`, `props.content?.tiles`

## truncateToByteSize()
- 位置: L1022-1034
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `encoded.subarray()`, `encoder.encode()`, `new TextDecoder().decode()`
- 参照: `encoded.length`

## processTile()
- 位置: L1035-1049
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `inputData.value.trim()`
- 条件付き依存: `if (tile.data.action)` → `collectedActions.push()`
- 条件付き依存: `if (inputData?.isValid && inputData.value.trim().length)` → `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.sendActionTelemetry()`
- 条件付き依存: `if (inputData?.isValid && inputData.value.trim().length)` → `truncateToByteSize()`
- 参照: `inputData.value`, `inputData.value.trim().length`, `inputData?.isValid`, `props.messageId`, `props.textInputs`, `tile.data`, `tile.data.action`, `tile.data.id`, `tile?.type`

## WelcomeScreen.render()
- 位置: L1061-1109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `_MultiStageProtonScreen__WEBPACK_IMPORTED_MODULE_3__.MultiStageProtonScreen`, `this.handleAction`, `this.props.aboveButtonStepsIndicator`, `this.props.activeMultiSelect`, `this.props.activeSingleSelectSelections`, `this.props.activeTheme`, `this.props.activeThemeId`, `this.props.addonIconURL`, `this.props.addonId`, `this.props.addonName`, `this.props.addonType`, `this.props.addonURL`, `this.props.advanceOnExperimentLoad`, `this.props.animationsPaused`, `this.props.appAndSystemLocaleInfo`, `this.props.ariaRole`, `this.props.autoAdvance`, `this.props.content`, `this.props.content.isRtamo`, `this.props.contentToggleChecked`, `this.props.forceHideStepsIndicator`, `this.props.id`, `this.props.installedAddons`, `this.props.isFirstScreen`, `this.props.isLastScreen`, `this.props.isSingleScreen`, `this.props.langPackInstallPhase`, `this.props.messageId`, `this.props.navigate`, `this.props.negotiatedLanguage`, `this.props.order`, `this.props.pinnedSites`, `this.props.previousOrder`, `this.props.requireAction`, `this.props.screenMultiSelects`, `this.props.setActiveMultiSelect`, `this.props.setActiveSingleSelectSelection`, `this.props.setContentToggleChecked`, `this.props.setPinnedSite`, `this.props.setScreenMultiSelects`, `this.props.setTextInput`, `this.props.startsWithCorner`, `this.props.textInputs`, `this.props.themeScreenshots`, `this.props.toggleAnimationsPaused`, `this.props.totalNumberOfScreens`

## CONFIGURABLE_STYLES()
- 位置: L1119-1119
- 役割: (未記入)
- 触るとき: (未記入)

## Localized()
- 位置: L1120-1120
- 役割: (未記入)
- 触るとき: (未記入)

## pickConfigurableStyles()
- 位置: L1121-1121
- 役割: (未記入)
- 触るとき: (未記入)

## resolveImageSrc()
- 位置: L1122-1122
- 役割: (未記入)
- 触るとき: (未記入)

## pickConfigurableStyles()
- 位置: L1138-1146
- 役割: (未記入)
- 触るとき: (未記入)

## resolveImageSrc()
- 位置: L1151-1157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.matches()`

## Localized()
- 位置: L1197-1275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `Array.isArray()`, `Object.assign()`, `pickConfigurableStyles()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().cloneElement()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createRef()`
- 条件付き依存: `if (current)` → `requestAnimationFrame()`
- 条件付き依存: `if (current)` → `current?.classList.replace()`
- 条件付き依存: `if (current)` → `current.getBoundingClientRect()`
- 条件付き依存: `if (text.args)` → `JSON.stringify()`
- 条件付き依存: `if (text.raw)` → `textNodes.push()`
- 条件付き依存: `if (typeof text === "string")` → `textNodes.push()`
- 条件付き依存: `if (text.zap)` → `textNodes.push()`
- 条件付き依存: `if (text.zap)` → `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 条件付き依存: `if (text.zap)` → `react__WEBPACK_IMPORTED_MODULE_0___default()`
- 条件付き依存: `if (text.string_id && text.inline_icons)` → `Object.entries()`
- 条件付き依存: `if (text.string_id && text.inline_icons)` → `textNodes.push()`
- 条件付き依存: `if (text.string_id && text.inline_icons)` → `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 条件付き依存: `if (text.string_id && text.inline_icons)` → `react__WEBPACK_IMPORTED_MODULE_0___default()`
- 条件付き依存: `if (text.string_id && text.inline_icons)` → `resolveImageSrc()`
- 参照: `children?.props`, `current.getBoundingClientRect().width`, `props.children`, `props.className`, `props.key`, `props.style`, `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `text.args`, `text.aria_label`, `text.inline_icons`, `text.raw`, `text.string_id`, `text.zap`, `textNodes.length`

## MultiStageProtonScreen()
- 位置: L1284-1284
- 役割: (未記入)
- 触るとき: (未記入)

## ProtonScreen()
- 位置: L1285-1285
- 役割: (未記入)
- 触るとき: (未記入)

## ProtonScreenActionButtons()
- 位置: L1286-1286
- 役割: (未記入)
- 触るとき: (未記入)

## screenContentShape()
- 位置: L1287-1287
- 役割: (未記入)
- 触るとき: (未記入)

## resolveCornerImagePosition()
- 位置: L1337-1344
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CORNER_IMAGE_LOGICAL_POSITIONS.get()`, `CORNER_IMAGE_POSITIONS.has()`
- 条件付き依存: `if (logical)` → `document.documentElement.matches()`

## resolveDirectionalImage()
- 位置: L1349-1355
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.documentElement.matches()`
- 参照: `image.rtl`, `image?.rtl`

## MultiStageProtonScreen()
- 位置: L1356-1523
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `doAdvance()`, `maybeAdvance()`, `performance.now()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `useMediaQuery()`, `window.clearTimeout()`, `window.setTimeout()`
- 条件付き依存: `if (autoAdvance)` → `setTimeout()`
- 条件付き依存: `if (autoAdvance)` → `handleAction()`
- 条件付き依存: `if (autoAdvance)` → `clearTimeout()`
- 条件付き依存: `if (typeof window.AWWaitForNimbus === "function")` → `window.AWWaitForNimbus()`
- 条件付き依存: `if (props.content.narrow)` → `document.querySelector("#multi-stage-message-root")?.setAttribute()`
- 条件付き依存: `if (props.content.narrow)` → `document.querySelector()`
- 条件付き依存: `if (!(props.content.narrow))` → `document.querySelector("#multi-stage-message-root")?.removeAttribute()`
- 条件付き依存: `if (!(props.content.narrow))` → `document.querySelector()`
- 参照: `advanceOnExperimentLoad?.maxDisplayMs`, `advanceOnExperimentLoad?.minDisplayMs`, `autoAdvance?.actionEl`, `autoAdvance?.actionTimeMS`, `props.aboveButtonStepsIndicator`, `props.activeMultiSelect`, `props.activeSingleSelectSelections`, `props.activeTheme`, `props.activeThemeId`, `props.addonIconURL`, `props.addonId`, `props.addonName`, `props.addonType`, `props.addonURL`, `props.advanceOnExperimentLoad`, `props.animationsPaused`, `props.ariaRole`, `props.autoAdvance`, `props.content`, `props.content.narrow`, `props.contentToggleChecked`, `props.forceHideStepsIndicator`, `props.handleAction`, `props.id`, `props.installedAddons`, `props.isFirstScreen`, `props.isLastScreen`, `props.isRtamo`, `props.isSingleScreen`, `props.langPackInstallPhase`, `props.messageId`, `props.navigate`, `props.negotiatedLanguage`, `props.order`, `props.pinnedSites`, `props.previousOrder`, `props.requireAction`, `props.screenMultiSelects`, `props.setActiveMultiSelect`, `props.setActiveSingleSelectSelection`, `props.setContentToggleChecked`, `props.setPinnedSite`, `props.setScreenMultiSelects`, `props.setTextInput`, `props.textInputs`, `props.themeScreenshots`, `props.toggleAnimationsPaused`, `props.totalNumberOfScreens`, `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `window.AWWaitForNimbus`

## doAdvance()
- 位置: L1402-1423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`, `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.sendActionTelemetry()`, `navigate()`, `performance.now()`

## maybeAdvance()
- 位置: L1424-1428
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (minDone && experimentsDone)` → `doAdvance()`

## useMediaQuery()
- 位置: L1466-1475
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useState)()`, `mediaQueryList.addEventListener()`, `mediaQueryList.removeEventListener()`, `window.matchMedia()`
- 参照: `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useState`, `window.matchMedia(query).matches`

## onChange()
- 位置: L1470-1470
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setDoesMatch()`
- 参照: `event.matches`

## ProtonScreenActionButtons()
- 位置: L1524-1645
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useState)()`, `JSON.stringify()`, `isPrimaryDisabled()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `react__WEBPACK_IMPORTED_MODULE_0___default().useRef()`
- 条件付き依存: `if (shouldFocusButton)` → `buttonRef.current?.focus()`
- 条件付き依存: `if (isRtamo)` → `addonType?.includes()`
- 参照: `_AdditionalCTA__WEBPACK_IMPORTED_MODULE_8__.AdditionalCTA`, `_InstallButton__WEBPACK_IMPORTED_MODULE_11__.InstallButton`, `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `_MultiStageAboutWelcome__WEBPACK_IMPORTED_MODULE_3__.SecondaryCTA`, `content.additional_button`, `content.additional_button?.alignment`, `content.additional_button?.flow`, `content.checkbox`, `content.checkbox.label`, `content.checkbox?.defaultValue`, `content.primary_button`, `content.primary_button.install_complete_label`, `content.primary_button.label`, `content.primary_button.label.string_id`, `content.primary_button?.disabled`, `content.primary_button?.has_arrow_icon`, `content.primary_button?.label`, `content.primary_button?.style`, `content.secondary_button`, `content?.primary_button?.should_focus_button`, `props.handleAction`, `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useState`

## isPrimaryDisabled()
- 位置: L1555-1590
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (disabledValue === "hasActiveSingleSelect")` → `Object.values(activeSingleSelectSelections).some()`
- 条件付き依存: `if (disabledValue === "hasActiveSingleSelect")` → `Object.values()`
- 条件付き依存: `if (disabledValue === "hasTextInput")` → `Object.values(textInputs).every()`
- 条件付き依存: `if (disabledValue === "hasTextInput")` → `Object.values()`
- 条件付き依存: `if (disabledValue === "hasTextInput")` → `input.value.trim()`
- 参照: `activeMultiSelect[selectKey]?.length`, `input.isValid`, `input.value.trim().length`

## onChange()
- 位置: L1632-1634
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setIsChecked()`

## ProtonScreen.componentDidMount()
- 位置: L1647-1662
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.props.requireAction && this.titleHeader)` → `this.titleHeader.focus()`
- 条件付き依存: `if (!(this.props.requireAction && this.titleHeader))` → `this.mainContentHeader.focus()`
- 参照: `this.props.content?.position`, `this.props.requireAction`, `this.titleHeader`

## ProtonScreen.getScreenClassName()
- 位置: L1663-1676
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.props.isFirstScreen`, `this.props.isLastScreen`, `this.props.order`, `this.props.previousOrder`

## ProtonScreen.renderTitle()
- 位置: L1677-1709
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 条件付き依存: `if (title_logo)` → `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 条件付き依存: `if (title_logo)` → `react__WEBPACK_IMPORTED_MODULE_0___default()`
- 条件付き依存: `if (title_logo)` → `this.renderPicture()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `this.props.requireAction`, `this.titleHeader`

## ProtonScreen.renderPicture()
- 位置: L1710-1794
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getLoadingStrategy()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `resolveDirectionalImage()`, `window.matchMedia()`
- 条件付き依存: `if (videoURL && !prefersReducedMotion)` → `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 条件付き依存: `if (videoURL && !prefersReducedMotion)` → `react__WEBPACK_IMPORTED_MODULE_0___default()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `window.matchMedia`, `window.matchMedia("(prefers-reduced-motion: reduce)").matches`

## getLoadingStrategy()
- 位置: L1726-1733
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.getLoadingStrategyFor()`

## ProtonScreen.renderNoodles()
- 位置: L1795-1807
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `react__WEBPACK_IMPORTED_MODULE_0___default().Fragment`

## ProtonScreen.renderLastCardImage()
- 位置: L1808-1828
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `this.renderPicture()`
- 参照: `content.center_image`

## ProtonScreen.renderCornerImage()
- 位置: L1829-1856
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `CORNER_IMAGE_ENTRANCE_ANIMATIONS.has()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `resolveCornerImagePosition()`, `this.renderPicture()`
- 参照: `cornerImage.darkModeImageURL`, `cornerImage.darkModeReducedMotionImageURL`, `cornerImage.entrance_animation`, `cornerImage.height`, `cornerImage.imageURL`, `cornerImage.marginBlock`, `cornerImage.marginInline`, `cornerImage.position`, `cornerImage.reducedMotionImageURL`, `cornerImage.rtl`, `cornerImage.style`, `cornerImage.width`, `entranceAnimation.delay`, `entranceAnimation.distance`, `entranceAnimation.duration`, `entranceAnimation.type`, `this.props.content.corner_image`

## ProtonScreen.renderLanguageSwitcher()
- 位置: L1857-1865
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `_LanguageSwitcher__WEBPACK_IMPORTED_MODULE_4__.LanguageSwitcher`, `this.props.content`, `this.props.content.languageSwitcher`, `this.props.handleAction`, `this.props.langPackInstallPhase`, `this.props.messageId`, `this.props.negotiatedLanguage`

## ProtonScreen.renderDismissButton()
- 位置: L1866-1885
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `label?.string_id`, `this.props.content.dismiss_button`, `this.props.handleAction`

## ProtonScreen.renderMoreButton()
- 位置: L1886-1892
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `_SubmenuButton__WEBPACK_IMPORTED_MODULE_12__.SubmenuButton`, `this.props.content`, `this.props.handleAction`

## ProtonScreen.renderStepsIndicator()
- 位置: L1893-1925
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `_MultiStageAboutWelcome__WEBPACK_IMPORTED_MODULE_3__.ProgressBar`, `_MultiStageAboutWelcome__WEBPACK_IMPORTED_MODULE_3__.StepsIndicator`, `content.progress_bar`, `content.steps_indicator?.string_id`, `this.props`

## ProtonScreen.hasAnimatedContent()
- 位置: L1932-1934
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `content.background`, `content.background_static`, `content.hero_image?.static_url`, `content.hero_image?.url`

## ProtonScreen.getEffectiveBackground()
- 位置: L1935-1943
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `content.background`, `content.background_static`, `content.position`, `content.zap_border`, `content.zap_border_gradient`, `this.props.animationsPaused`

## ProtonScreen.getEffectiveHeroImageUrl()
- 位置: L1944-1949
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `content.hero_image`, `content.hero_image.static_url`, `content.hero_image.url`, `this.props.animationsPaused`

## ProtonScreen.renderAnimationPlayPauseButton()
- 位置: L1950-1963
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `this.props`, `this.props.animationsPaused`

## ProtonScreen.renderSecondarySection()
- 位置: L1964-1986
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `this.getEffectiveBackground()`, `this.getEffectiveHeroImageUrl()`, `this.hasAnimatedContent()`, `this.renderAnimationPlayPauseButton()`, `this.renderDismissButton()`, `this.renderHeroText()`, `tiles.some()`
- 参照: `_HeroImage__WEBPACK_IMPORTED_MODULE_6__.HeroImage`, `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `content.dismiss_button`, `content.hero_image`, `content.hero_text`, `content.hide_secondary_section`, `content.image_alt_text`, `content.reverse_split`, `content.split_narrow_bkg_position`, `content.tiles`, `tile?.type`

## ProtonScreen.renderHeroText()
- 位置: L1987-2019
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 条件付き依存: `if (isSimpleText)` → `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 条件付き依存: `if (isSimpleText)` → `react__WEBPACK_IMPORTED_MODULE_0___default()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `hero_text.subtitle`, `hero_text.title`

## HeroTextWrapper()
- 位置: L1995-2004
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `react__WEBPACK_IMPORTED_MODULE_0___default().Fragment`

## ProtonScreen.renderOrderedContent()
- 位置: L2020-2046
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `content.entries()`, `elements.push()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `this.renderPicture()`
- 参照: `_LinkParagraph__WEBPACK_IMPORTED_MODULE_9__.LinkParagraph`, `item.alt_text`, `item.darkModeImageURL`, `item.height`, `item.marginInline`, `item.type`, `item.url`, `item.width`, `react__WEBPACK_IMPORTED_MODULE_0___default().Fragment`, `this.props.handleAction`

## ProtonScreen.renderRTAMOIcon()
- 位置: L2047-2057
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.getLoadingStrategyFor()`, `addonType?.includes()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `themeScreenshots[0].url`

## ProtonScreen.getCombinedInnerStyles()
- 位置: L2058-2066
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.getValidStyle()`
- 参照: `content.main_content_style`, `content.main_content_style_narrow`, `content.split_content_justify_content`

## ProtonScreen.getActionButtonsPosition()
- 位置: L2067-2078
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `VALID_POSITIONS.includes()`
- 参照: `content.action_buttons_above_content`, `content.action_buttons_position`

## ProtonScreen.renderActionButtons()
- 位置: L2079-2093
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `this.getActionButtonsPosition()`
- 参照: `this.props.activeMultiSelect`, `this.props.activeSingleSelectSelections`, `this.props.addonId`, `this.props.addonName`, `this.props.addonType`, `this.props.handleAction`, `this.props.installedAddons`, `this.props.isRtamo`, `this.props.pinnedSites`, `this.props.textInputs`

## ProtonScreen.render()
- 位置: L2096-2208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `String()`, `["center", "center-large"].includes()`, `["split", "card-stack"].includes()`, `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.getValidStyle()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `this.getCombinedInnerStyles()`, `this.getEffectiveBackground()`, `this.getScreenClassName()`, `this.hasAnimatedContent()`, `this.props.messageId?.includes()`, `this.renderActionButtons()`, `this.renderAnimationPlayPauseButton()`, `this.renderCornerImage()`, `this.renderDismissButton()`, `this.renderLanguageSwitcher()`, `this.renderLastCardImage()`, `this.renderMoreButton()`, `this.renderNoodles()`, `this.renderOrderedContent()`, `this.renderPicture()`, `this.renderRTAMOIcon()`, `this.renderSecondarySection()`, `this.renderStepsIndicator()`, `this.renderTitle()`
- 参照: `_CTAParagraph__WEBPACK_IMPORTED_MODULE_5__.CTAParagraph`, `_ContentTiles__WEBPACK_IMPORTED_MODULE_10__.ContentTiles`, `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `_MultiStageAboutWelcome__WEBPACK_IMPORTED_MODULE_3__.SecondaryCTA`, `_OnboardingVideo__WEBPACK_IMPORTED_MODULE_7__.OnboardingVideo`, `content.above_button_content`, `content.corner_image`, `content.cta_paragraph`, `content.dismiss_button`, `content.fullscreen`, `content.has_noodles`, `content.hide_secondary_section`, `content.info_text`, `content.isSystemPromptStyleSpotlight`, `content.layout`, `content.logo`, `content.more_button`, `content.no_rdm`, `content.position`, `content.progress_bar`, `content.reverse_split`, `content.screen_style`, `content.secondary_button_top`, `content.split_content_padding_block`, `content.split_content_padding_inline`, `content.subtitle`, `content.text_color`, `content.tiles?.type`, `content.title`, `content.title_style`, `content.video_container`, `content.width`, `content.zap_border`, `content.zap_shadow`, `content?.tiles_container?.position`, `content?.video_container`, `this.props`, `this.props.activeThemeId`, `this.props.addonIconURL`, `this.props.addonName`, `this.props.appAndSystemLocaleInfo?.displayNames`, `this.props.handleAction`, `this.props.id`, `this.props.themeScreenshots`

## ref()
- 位置: L2159-2161
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.mainContentHeader`

## r()
- 位置: L2759-2759
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `o()`
- 参照: `t.length`

## o()
- 位置: L2759-2759
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!f&&c)` → `require()`
- 条件付き依存: `if (u)` → `u()`
- 条件付き依存: `if (!n[i])` → `e[i][0].call()`
- 条件付き依存: `if (!n[i])` → `o()`
- 参照: `a.code`, `n[i].exports`, `p.exports`

## printWarning()
- 位置: L2769-2769
- 役割: (未記入)
- 触るとき: (未記入)

## printWarning()
- 位置: L2776-2787
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof console !== 'undefined')` → `console.error()`

## checkPropTypes()
- 位置: L2801-2849
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (true)` → `has()`
- 条件付き依存: `if (typeof typeSpecs[typeSpecName] !== 'function')` → `Error()`
- 条件付き依存: `if (has(typeSpecs, typeSpecName))` → `typeSpecs[typeSpecName]()`
- 条件付き依存: `if (error && !(error instanceof Error))` → `printWarning()`
- 条件付き依存: `if (error instanceof Error && !(error.message in loggedTypeFailures))` → `getStack()`
- 条件付き依存: `if (error instanceof Error && !(error.message in loggedTypeFailures))` → `printWarning()`
- 参照: `err.name`, `error.message`

## checkPropTypes.resetWarningCache()
- 位置: L2856-2860
- 役割: (未記入)
- 触るとき: (未記入)

## emptyFunction()
- 位置: L2876-2876
- 役割: (未記入)
- 触るとき: (未記入)

## emptyFunctionWithReset()
- 位置: L2877-2877
- 役割: (未記入)
- 触るとき: (未記入)

## module.exports()
- 位置: L2880-2929
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ReactPropTypes.PropTypes`, `shim.isRequired`

## shim()
- 位置: L2881-2893
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `err.name`

## getShim()
- 位置: L2895-2897
- 役割: (未記入)
- 触るとき: (未記入)

## printWarning()
- 位置: L2948-2948
- 役割: (未記入)
- 触るとき: (未記入)

## printWarning()
- 位置: L2951-2962
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof console !== 'undefined')` → `console.error()`

## emptyFunctionThatReturnsNull()
- 位置: L2965-2967
- 役割: (未記入)
- 触るとき: (未記入)

## module.exports()
- 位置: L2969-3541
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createAnyTypeChecker()`, `createElementTypeChecker()`, `createElementTypeTypeChecker()`, `createNodeChecker()`, `createPrimitiveTypeChecker()`
- 参照: `Error.prototype`, `PropTypeError.prototype`, `ReactPropTypes.PropTypes`, `ReactPropTypes.checkPropTypes`, `ReactPropTypes.resetWarningCache`, `Symbol.iterator`, `checkPropTypes.resetWarningCache`

## getIteratorFn()
- 位置: L2988-2993
- 役割: (未記入)
- 触るとき: (未記入)

## is()
- 位置: L3074-3084
- 役割: (未記入)
- 触るとき: (未記入)

## PropTypeError()
- 位置: L3094-3098
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.data`, `this.message`, `this.stack`

## createChainableTypeChecker()
- 位置: L3102-3158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checkType.bind()`
- 参照: `chainedCheckType.isRequired`

## checkType()
- 位置: L3107-3152
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( !manualPropTypeCallCache[cacheKey] && // Avoid spamming the console because they are often not actionable except for lib authors manualPropTypeWarningCount ...)` → `printWarning()`
- 条件付き依存: `if (!(props[propName] == null))` → `validate()`
- 参照: `err.name`

## createPrimitiveTypeChecker()
- 位置: L3160-3178
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createChainableTypeChecker()`

## validate()
- 位置: L3161-3176
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getPropType()`
- 条件付き依存: `if (propType !== expectedType)` → `getPreciseType()`

## createAnyTypeChecker()
- 位置: L3180-3182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createChainableTypeChecker()`

## createArrayOfTypeChecker()
- 位置: L3184-3203
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createChainableTypeChecker()`

## validate()
- 位置: L3185-3201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `typeChecker()`
- 条件付き依存: `if (!Array.isArray(propValue))` → `getPropType()`
- 参照: `propValue.length`

## createElementTypeChecker()
- 位置: L3205-3215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createChainableTypeChecker()`

## validate()
- 位置: L3206-3213
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isValidElement()`
- 条件付き依存: `if (!isValidElement(propValue))` → `getPropType()`

## createElementTypeTypeChecker()
- 位置: L3217-3227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createChainableTypeChecker()`

## validate()
- 位置: L3218-3225
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ReactIs.isValidElementType()`
- 条件付き依存: `if (!ReactIs.isValidElementType(propValue))` → `getPropType()`

## createInstanceTypeChecker()
- 位置: L3229-3239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createChainableTypeChecker()`

## validate()
- 位置: L3230-3237
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!(props[propName] instanceof expectedClass))` → `getClassName()`
- 参照: `expectedClass.name`

## createEnumTypeChecker()
- 位置: L3241-3274
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `createChainableTypeChecker()`
- 条件付き依存: `if (arguments.length > 1)` → `printWarning()`
- 条件付き依存: `if (!(arguments.length > 1))` → `printWarning()`
- 参照: `arguments.length`

## validate()
- 位置: L3256-3272
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `String()`, `is()`
- 参照: `expectedValues.length`

## replacer()
- 位置: L3264-3270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getPreciseType()`
- 条件付き依存: `if (type === 'symbol')` → `String()`

## createObjectOfTypeChecker()
- 位置: L3276-3297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createChainableTypeChecker()`

## validate()
- 位置: L3277-3295
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getPropType()`, `has()`
- 条件付き依存: `if (has(propValue, key))` → `typeChecker()`

## createUnionTypeChecker()
- 位置: L3299-3332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `createChainableTypeChecker()`
- 条件付き依存: `if (!Array.isArray(arrayOfTypeCheckers))` → `printWarning()`
- 条件付き依存: `if (typeof checker !== 'function')` → `printWarning()`
- 条件付き依存: `if (typeof checker !== 'function')` → `getPostfixForTypeWarning()`
- 参照: `arrayOfTypeCheckers.length`

## validate()
- 位置: L3316-3330
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checker()`, `checkerResult.data.hasOwnProperty()`, `expectedTypes.join()`
- 条件付き依存: `if (checkerResult.data.hasOwnProperty('expectedType'))` → `expectedTypes.push()`
- 参照: `arrayOfTypeCheckers.length`, `checkerResult.data.expectedType`, `expectedTypes.length`

## createNodeChecker()
- 位置: L3334-3342
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createChainableTypeChecker()`

## validate()
- 位置: L3335-3340
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isNode()`

## invalidValidatorError()
- 位置: L3344-3349
- 役割: (未記入)
- 触るとき: (未記入)

## createShapeTypeChecker()
- 位置: L3351-3371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createChainableTypeChecker()`

## validate()
- 位置: L3352-3369
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checker()`, `getPropType()`
- 条件付き依存: `if (typeof checker !== 'function')` → `invalidValidatorError()`
- 条件付き依存: `if (typeof checker !== 'function')` → `getPreciseType()`

## createStrictShapeTypeChecker()
- 位置: L3373-3403
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `createChainableTypeChecker()`

## validate()
- 位置: L3374-3400
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `assign()`, `checker()`, `getPropType()`, `has()`
- 条件付き依存: `if (has(shapeTypes, key) && typeof checker !== 'function')` → `invalidValidatorError()`
- 条件付き依存: `if (has(shapeTypes, key) && typeof checker !== 'function')` → `getPreciseType()`
- 条件付き依存: `if (!checker)` → `JSON.stringify()`
- 条件付き依存: `if (!checker)` → `Object.keys()`

## isNode()
- 位置: L3405-3450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `getIteratorFn()`, `isValidElement()`
- 条件付き依存: `if (Array.isArray(propValue))` → `propValue.every()`
- 条件付き依存: `if (iteratorFn)` → `iteratorFn.call()`
- 条件付き依存: `if (iteratorFn !== propValue.entries)` → `iterator.next()`
- 条件付き依存: `if (iteratorFn !== propValue.entries)` → `isNode()`
- 条件付き依存: `if (!(iteratorFn !== propValue.entries))` → `iterator.next()`
- 条件付き依存: `if (entry)` → `isNode()`
- 参照: `(step = iterator.next()).done`, `propValue.entries`, `step.value`

## isSymbol()
- 位置: L3452-3474
- 役割: (未記入)
- 触るとき: (未記入)

## getPropType()
- 位置: L3477-3492
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `isSymbol()`

## getPreciseType()
- 位置: L3496-3509
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getPropType()`

## getPostfixForTypeWarning()
- 位置: L3513-3526
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getPreciseType()`

## getClassName()
- 位置: L3529-3534
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `propValue.constructor`, `propValue.constructor.name`

## toObject()
- 位置: L3590-3596
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object()`

## shouldUseNative()
- 位置: L3598-3640
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `'abcdefghijklmnopqrst'.split()`, `'abcdefghijklmnopqrst'.split('').forEach()`, `Object.assign()`, `Object.getOwnPropertyNames()`, `Object.getOwnPropertyNames(test2).map()`, `Object.keys()`, `Object.keys(Object.assign({}, test3)).join()`, `String.fromCharCode()`, `order2.join()`
- 参照: `Object.assign`

## defaultSetTimout()
- 位置: L3681-3683
- 役割: (未記入)
- 触るとき: (未記入)

## defaultClearTimeout()
- 位置: L3684-3686
- 役割: (未記入)
- 触るとき: (未記入)

## runTimeout()
- 位置: L3707-3731
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cachedSetTimeout()`, `cachedSetTimeout.call()`
- 条件付き依存: `if (cachedSetTimeout === setTimeout)` → `setTimeout()`
- 条件付き依存: `if ((cachedSetTimeout === defaultSetTimout || !cachedSetTimeout) && setTimeout)` → `setTimeout()`

## runClearTimeout()
- 位置: L3732-3758
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cachedClearTimeout()`, `cachedClearTimeout.call()`
- 条件付き依存: `if (cachedClearTimeout === clearTimeout)` → `clearTimeout()`
- 条件付き依存: `if ((cachedClearTimeout === defaultClearTimeout || !cachedClearTimeout) && clearTimeout)` → `clearTimeout()`

## cleanUpNextTick()
- 位置: L3764-3777
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (currentQueue.length)` → `currentQueue.concat()`
- 条件付き依存: `if (queue.length)` → `drainQueue()`
- 参照: `currentQueue.length`, `queue.length`

## drainQueue()
- 位置: L3779-3801
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `runClearTimeout()`, `runTimeout()`
- 条件付き依存: `if (currentQueue)` → `currentQueue[queueIndex].run()`
- 参照: `queue.length`

## process.nextTick()
- 位置: L3803-3814
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `queue.push()`
- 条件付き依存: `if (queue.length === 1 && !draining)` → `runTimeout()`
- 参照: `arguments.length`, `queue.length`

## Item()
- 位置: L3817-3820
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.array`, `this.fun`

## Item.prototype.run()
- 位置: L3821-3823
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.fun.apply()`
- 参照: `this.array`

## noop()
- 位置: L3831-3831
- 役割: (未記入)
- 触るとき: (未記入)

## process.listeners()
- 位置: L3843-3843
- 役割: (未記入)
- 触るとき: (未記入)

## process.binding()
- 位置: L3845-3847
- 役割: (未記入)
- 触るとき: (未記入)

## process.cwd()
- 位置: L3849-3849
- 役割: (未記入)
- 触るとき: (未記入)

## process.chdir()
- 位置: L3850-3852
- 役割: (未記入)
- 触るとき: (未記入)

## process.umask()
- 位置: L3853-3853
- 役割: (未記入)
- 触るとき: (未記入)

## isValidElementType()
- 位置: L3898-3901
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `type.$$typeof`

## typeOf()
- 位置: L3903-3943
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `object.$$typeof`, `object.type`, `type.$$typeof`

## isAsyncMode()
- 位置: L3960-3970
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isConcurrentMode()`, `typeOf()`
- 条件付き依存: `if (!hasWarnedAboutDeprecatedIsAsyncMode)` → `console['warn']()`

## isConcurrentMode()
- 位置: L3971-3973
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `typeOf()`

## isContextConsumer()
- 位置: L3974-3976
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `typeOf()`

## isContextProvider()
- 位置: L3977-3979
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `typeOf()`

## isElement()
- 位置: L3980-3982
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `object.$$typeof`

## isForwardRef()
- 位置: L3983-3985
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `typeOf()`

## isFragment()
- 位置: L3986-3988
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `typeOf()`

## isLazy()
- 位置: L3989-3991
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `typeOf()`

## isMemo()
- 位置: L3992-3994
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `typeOf()`

## isPortal()
- 位置: L3995-3997
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `typeOf()`

## isProfiler()
- 位置: L3998-4000
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `typeOf()`

## isStrictMode()
- 位置: L4001-4003
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `typeOf()`

## isSuspense()
- 位置: L4004-4006
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `typeOf()`

## z()
- 位置: L4052-4052
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `a.$$typeof`, `a.type`

## A()
- 位置: L4052-4052
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `z()`

## exports.isAsyncMode()
- 位置: L4053-4053
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `A()`, `z()`

## exports.isContextConsumer()
- 位置: L4053-4053
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `z()`

## exports.isContextProvider()
- 位置: L4053-4053
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `z()`

## exports.isElement()
- 位置: L4053-4053
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `a.$$typeof`

## exports.isForwardRef()
- 位置: L4053-4053
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `z()`

## exports.isFragment()
- 位置: L4053-4053
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `z()`

## exports.isLazy()
- 位置: L4053-4053
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `z()`

## exports.isMemo()
- 位置: L4054-4054
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `z()`

## exports.isPortal()
- 位置: L4054-4054
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `z()`

## exports.isProfiler()
- 位置: L4054-4054
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `z()`

## exports.isStrictMode()
- 位置: L4054-4054
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `z()`

## exports.isSuspense()
- 位置: L4054-4054
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `z()`

## exports.isValidElementType()
- 位置: L4055-4055
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `a.$$typeof`

## LanguageSwitcher()
- 位置: L4079-4079
- 役割: (未記入)
- 触るとき: (未記入)

## useLanguageSwitcher()
- 位置: L4080-4080
- 役割: (未記入)
- 触るとき: (未記入)

## useLanguageSwitcher()
- 位置: L4099-4199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useState)()`, `screens.findIndex()`
- 条件付き依存: `if (mismatchScreen?.content?.languageSwitcher)` → `Object.values()`
- 参照: `appAndSystemLocaleInfo?.matchType`, `mismatchScreen.content.languageSwitcher`, `mismatchScreen?.content?.languageSwitcher`, `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useState`, `text.args.negotiatedLanguage`, `text?.args`

## getNegotiatedLanguage()
- 位置: L4121-4151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.AWNegotiateLangPackForLanguageMismatch()`
- 条件付き依存: `if (langPack)` → `setNegotiatedLanguage()`
- 条件付き依存: `if (!(langPack))` → `setNegotiatedLanguage()`
- 参照: `appAndSystemLocaleInfo.appLocaleRaw`, `appAndSystemLocaleInfo.displayNames.appLanguage`, `appAndSystemLocaleInfo.matchType`, `langPack.target_locale`

## ensureLangPackInstalled()
- 位置: L4163-4177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `setLangPackInstallPhase()`, `window.AWEnsureLangPackInstalled()`, `window.AWEnsureLangPackInstalled(negotiatedLanguage, mismatchScreen?.content).then()`
- 参照: `mismatchScreen.content`, `mismatchScreen?.content`

## filterScreen()
- 位置: L4179-4190
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (screenIndex > languageMismatchScreenIndex)` → `setScreenIndex()`
- 条件付き依存: `if (mismatchScreen && (appAndSystemLocaleInfo?.matchType !== "language-mismatch" || negotiatedLanguage?.langPack === null))` → `setLanguageFilteredScreens()`
- 条件付き依存: `if (mismatchScreen && (appAndSystemLocaleInfo?.matchType !== "language-mismatch" || negotiatedLanguage?.langPack === null))` → `screens.filter()`
- 条件付き依存: `if (!(mismatchScreen && (appAndSystemLocaleInfo?.matchType !== "language-mismatch" || negotiatedLanguage?.langPack === null)))` → `setLanguageFilteredScreens()`
- 参照: `appAndSystemLocaleInfo?.matchType`, `negotiatedLanguage?.langPack`, `s.id`

## LanguageSwitcher()
- 位置: L4207-4329
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useState)()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 条件付き依存: `if (isAwaitingLangpack && langPackInstallPhase !== "installing")` → `window.AWSetRequestedLocales()`
- 条件付き依存: `if (isAwaitingLangpack && langPackInstallPhase !== "installing")` → `requestAnimationFrame()`
- 条件付き依存: `if (isAwaitingLangpack && langPackInstallPhase !== "installing")` → `handleAction()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `content.languageSwitcher.cancel`, `content.languageSwitcher.continue`, `content.languageSwitcher.downloading`, `content.languageSwitcher.skip`, `content.languageSwitcher.switch`, `content.languageSwitcher.waiting`, `negotiatedLanguage.requestSystemLocales`, `negotiatedLanguage?.appDisplayName`, `negotiatedLanguage?.langPackDisplayName`, `negotiatedLanguage?.requestSystemLocales`, `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useState`

## onClick()
- 位置: L4293-4300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleAction()`, `setIsAwaitingLangpack()`

## onClick()
- 位置: L4308-4311
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.sendActionTelemetry()`, `setIsAwaitingLangpack()`

## onClick()
- 位置: L4320-4323
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleAction()`, `window.AWSetRequestedLocales()`
- 参照: `negotiatedLanguage.originalAppLocales`

## CTAParagraph()
- 位置: L4338-4338
- 役割: (未記入)
- 触るとき: (未記入)

## CTAParagraph()
- 位置: L4351-4386
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.getValidStyle()`, `event.preventDefault()`, `handleAction()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `react__WEBPACK_IMPORTED_MODULE_0___default().useCallback()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.CONFIGURABLE_STYLES`, `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `content.text`, `content.text.string_id`, `content.text.string_name`, `content?.icon`, `content?.icon?.iconURL`, `content?.info_tile`, `content?.style`, `content?.text`

## onKeyUp()
- 位置: L4379-4379
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["Enter", " "].includes()`, `onClick()`
- 参照: `event.key`

## HeroImage()
- 位置: L4395-4395
- 役割: (未記入)
- 触るとき: (未記入)

## HeroImage()
- 位置: L4406-4426
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_1__.MultiStageUtils.getLoadingStrategyFor()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`

## OnboardingVideo()
- 位置: L4435-4435
- 役割: (未記入)
- 触るとき: (未記入)

## OnboardingVideo()
- 位置: L4444-4466
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `props.content.autoPlay`, `props.content.video_url`

## handleVideoAction()
- 位置: L4447-4453
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `props.handleAction()`

## onPlay()
- 位置: L4461-4461
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleVideoAction()`

## onEnded()
- 位置: L4462-4462
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleVideoAction()`

## AdditionalCTA()
- 位置: L4475-4475
- 役割: (未記入)
- 触るとき: (未記入)

## AdditionalCTA()
- 位置: L4488-4541
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `computeDisabled()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `react__WEBPACK_IMPORTED_MODULE_0___default().useCallback()`
- 条件付き依存: `if (disabledValue === "hasTextInput")` → `Object.values(textInputs).every()`
- 条件付き依存: `if (disabledValue === "hasTextInput")` → `Object.values()`
- 条件付き依存: `if (disabledValue === "hasTextInput")` → `input.value.trim()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `_SubmenuButton__WEBPACK_IMPORTED_MODULE_2__.SubmenuButton`, `activeMultiSelect[key]?.length`, `content.additional_button?.disabled`, `content.additional_button?.label`, `content.additional_button?.style`, `content.submenu_button?.attached_to`, `input.isValid`, `input.value.trim().length`

## SubmenuButton()
- 位置: L4550-4550
- 役割: (未記入)
- 触るとき: (未記入)

## SubmenuButton()
- 位置: L4561-4563
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `document.createXULElement`

## translateMenuitem()
- 位置: L4564-4589
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (label.raw)` → `element.setAttribute()`
- 条件付き依存: `if (label.access_key)` → `element.setAttribute()`
- 条件付き依存: `if (label.aria_label)` → `element.setAttribute()`
- 条件付き依存: `if (label.tooltip_text)` → `element.setAttribute()`
- 条件付き依存: `if (label.string_id)` → `element.setAttribute()`
- 条件付き依存: `if (label.args)` → `element.setAttribute()`
- 条件付き依存: `if (label.args)` → `JSON.stringify()`
- 参照: `label.access_key`, `label.args`, `label.aria_label`, `label.raw`, `label.string_id`, `label.tooltip_text`

## addMenuitems()
- 位置: L4590-4631
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `addMenuitems()`, `document.createXULElement()`, `menu.appendChild()`, `popup.appendChild()`, `translateMenuitem()`
- 条件付き依存: `if (item.icon)` → `menu.classList.add()`
- 条件付き依存: `if (item.icon)` → `menu.setAttribute()`
- 条件付き依存: `if (item.icon)` → `menuitem.classList.add()`
- 条件付き依存: `if (item.icon)` → `menuitem.setAttribute()`
- 参照: `item.icon`, `item.id`, `item.submenu`, `item.type`, `menu.className`, `menu.value`, `menuitem.config`, `menuitem.value`

## SubmenuButtonInner()
- 位置: L4632-4725
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useCallback)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useState)()`, ``${buttonConfig.attached_to || content.attached_to || ""} submenu_button`.trim()`, `addMenuitems()`, `button.appendChild()`, `button.hasAttribute()`, `button.querySelector()`, `button?.querySelector()`, `document.createXULElement()`, `document.head.querySelector()`, `handleAction()`, `menupopup?.remove()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `stylesheet?.remove()`
- 条件付き依存: `if (submenu && !button.hasAttribute("open"))` → `submenu.openPopup()`
- 条件付き依存: `if (!document.head.querySelector(`link[href="chrome://global/content/widgets.css"], link[href="chrome://global/skin/global.css"]`))` → `document.createElement()`
- 条件付き依存: `if (!document.head.querySelector(`link[href="chrome://global/content/widgets.css"], link[href="chrome://global/skin/global.css"]`))` → `document.head.appendChild()`
- 条件付き依存: `if (!menupopup.listenersRegistered)` → `menupopup.addEventListener()`
- 条件付き依存: `if (event.target === menupopup && event.target.anchorNode)` → `event.target.anchorNode.toggleAttribute()`
- 条件付き依存: `if (event.target === menupopup && event.target.anchorNode)` → `setIsSubmenuExpanded()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `buttonConfig.attached_to`, `buttonConfig.label`, `buttonConfig?.style`, `buttonConfig?.submenu`, `config.action`, `config.id`, `content.attached_to`, `content.dismiss_button`, `content.more_button`, `content.submenu_button`, `event.target`, `event.target.anchorNode`, `menupopup.className`, `menupopup.listenersRegistered`, `react__WEBPACK_IMPORTED_MODULE_0__.useCallback`, `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useRef`, `react__WEBPACK_IMPORTED_MODULE_0__.useState`, `ref.current`, `stylesheet.href`, `stylesheet.rel`, `submenuItems.length`

## LinkParagraph()
- 位置: L4734-4734
- 役割: (未記入)
- 触るとき: (未記入)

## renderSegment()
- 位置: L4745-4825
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 条件付き依存: `if (segment?.imageURL)` → `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 条件付き依存: `if (segment?.imageURL)` → `react__WEBPACK_IMPORTED_MODULE_0___default()`
- 条件付き依存: `if (segment?.imageURL)` → `(0,_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.resolveImageSrc)()`
- 条件付き依存: `if (segment?.imageURL)` → `(0,_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.pickConfigurableStyles)()`
- 条件付き依存: `if (segment?.action)` → `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 条件付き依存: `if (segment?.action)` → `react__WEBPACK_IMPORTED_MODULE_0___default()`
- 条件付き依存: `if (segment?.href)` → `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 条件付き依存: `if (segment?.href)` → `react__WEBPACK_IMPORTED_MODULE_0___default()`
- 条件付き依存: `if (segment?.link_key)` → `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 条件付き依存: `if (segment?.link_key)` → `react__WEBPACK_IMPORTED_MODULE_0___default()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.pickConfigurableStyles`, `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.resolveImageSrc`, `segment.alt`, `segment.href`, `segment.id`, `segment.link_key`, `segment.where`, `segment?.action`, `segment?.href`, `segment?.imageURL`, `segment?.link_key`

## onClick()
- 位置: L4766-4769
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `handleAction()`
- 参照: `segment.action`

## onKeyPress()
- 位置: L4770-4775
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.key === "Enter" && !event.repeat)` → `event.preventDefault()`
- 条件付き依存: `if (event.key === "Enter" && !event.repeat)` → `handleAction()`
- 参照: `event.key`, `event.repeat`, `segment.action`

## onClick()
- 位置: L4792-4795
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.preventDefault()`, `handleAction()`

## onKeyPress()
- 位置: L4811-4815
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.key === "Enter" && !event.repeat)` → `handleAction()`
- 参照: `event.key`, `event.repeat`

## LinkParagraph()
- 位置: L4826-4870
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useCallback)()`, `Array.isArray()`, `event.target.closest()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `text_content.link_keys?.map()`
- 条件付き依存: `if (anchor)` → `handleAction()`
- 条件付き依存: `if (event.key === "Enter" && !event.repeat)` → `handleParagraphAction()`
- 条件付き依存: `if (Array.isArray(text))` → `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 条件付き依存: `if (Array.isArray(text))` → `react__WEBPACK_IMPORTED_MODULE_0___default()`
- 条件付き依存: `if (Array.isArray(text))` → `(0,_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.pickConfigurableStyles)()`
- 条件付き依存: `if (Array.isArray(text))` → `text.map()`
- 条件付き依存: `if (Array.isArray(text))` → `renderSegment()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.pickConfigurableStyles`, `event.key`, `event.repeat`, `react__WEBPACK_IMPORTED_MODULE_0__.useCallback`, `text_content?.font_styles`, `text_content?.text`

## ContentTiles()
- 位置: L4879-4879
- 役割: (未記入)
- 触るとき: (未記入)

## getTileImpressionContext()
- 位置: L4880-4880
- 役割: (未記入)
- 触るとき: (未記入)

## _extends()
- 位置: L4902-4902
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `({}).hasOwnProperty.call()`, `Object.assign.bind()`, `_extends.apply()`
- 参照: `Object.assign`, `arguments.length`

## getTileImpressionContext()
- 位置: L4934-4943
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(Array.isArray(tiles) ? tiles : [tiles]).find()`, `Array.isArray()`, `pinnableSites.data.filter()`
- 参照: `item?.personalized`, `pinnableSites.data.filter(item => item?.personalized).length`, `pinnableSites.data.length`, `tile.data`, `tile?.type`

## ContentTiles()
- 位置: L4944-5260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useState)()`, `dialog.addEventListener()`, `dialog.removeEventListener()`, `document.getElementById()`, `document.querySelector()`, `renderContentTiles()`, `tilesEl?.closest()`
- 条件付き依存: `if (!props.activeMultiSelect)` → `Array.isArray()`
- 条件付き依存: `if (!props.activeMultiSelect)` → `tilesArray.forEach()`
- 条件付き依存: `if (!props.activeMultiSelect)` → `tile.data.forEach()`
- 条件付き依存: `if (defaultValue && id)` → `newActiveMultiSelect.push()`
- 条件付き依存: `if (newActiveMultiSelect.length)` → `props.setActiveMultiSelect()`
- 条件付き依存: `if (content.tiles_header)` → `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 条件付き依存: `if (content.tiles_header)` → `react__WEBPACK_IMPORTED_MODULE_0___default()`
- 条件付き依存: `if (content.tiles_header)` → `renderContentTiles()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `content.tiles_header`, `content.tiles_header.title`, `document.location.href`, `document.querySelector("#multi-stage-message-root.onboardingContainer[data-page]")?.dataset.page`, `newActiveMultiSelect.length`, `props.activeMultiSelect`, `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useState`, `react__WEBPACK_IMPORTED_MODULE_0___default().Fragment`, `tile.data`, `tile.type`

## onKeyDown()
- 位置: L5016-5023
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (e.key === "Tab")` → `performance.now()`
- 条件付き依存: `if (e.key === "Tab")` → `tilesEl.contains()`
- 参照: `document.activeElement`, `e.key`

## onFocusIn()
- 位置: L5024-5060
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `actionButtons?.contains()`, `dialog.querySelector()`, `document.contains()`, `lastTilesEl.focus()`, `performance.now()`, `tilesEl.contains()`

## toggleTile()
- 位置: L5070-5082
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_13__.MultiStageUtils.sendActionTelemetry()`
- 条件付き依存: `if (tile.type === "link" && tile.action)` → `props.handleAction()`
- 条件付き依存: `if (!(tile.type === "link" && tile.action))` → `setExpandedTileIndex()`
- 参照: `props.messageId`, `tile.action`, `tile.id`, `tile.type`

## toggleTiles()
- 位置: L5083-5086
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_13__.MultiStageUtils.sendActionTelemetry()`, `setTilesHeaderExpanded()`
- 参照: `props.messageId`

## getTileMultiSelects()
- 位置: L5087-5089
- 役割: (未記入)
- 触るとき: (未記入)

## getTileActiveMultiSelect()
- 位置: L5090-5092
- 役割: (未記入)
- 触るとき: (未記入)

## renderContentTile()
- 位置: L5093-5233
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `["theme", "single-select"].includes()`, `_extends()`, `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_13__.MultiStageUtils.getTileStyle()`, `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_13__.MultiStageUtils.getValidStyle()`, `getTileActiveMultiSelect()`, `getTileMultiSelects()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `_ActionChecklist__WEBPACK_IMPORTED_MODULE_10__.ActionChecklist`, `_AddonsPicker__WEBPACK_IMPORTED_MODULE_2__.AddonsPicker`, `_ConfirmationChecklist__WEBPACK_IMPORTED_MODULE_12__.ConfirmationChecklist`, `_ContentToggle__WEBPACK_IMPORTED_MODULE_16__.ContentToggle`, `_EmbeddedBackupRestore__WEBPACK_IMPORTED_MODULE_14__.EmbeddedBackupRestore`, `_EmbeddedBrowser__WEBPACK_IMPORTED_MODULE_11__.EmbeddedBrowser`, `_EmbeddedFxBackupOptIn__WEBPACK_IMPORTED_MODULE_9__.EmbeddedFxBackupOptIn`, `_EmbeddedMigrationWizard__WEBPACK_IMPORTED_MODULE_7__.EmbeddedMigrationWizard`, `_EmbeddedThemePicker__WEBPACK_IMPORTED_MODULE_8__.EmbeddedThemePicker`, `_LinkParagraph__WEBPACK_IMPORTED_MODULE_18__.LinkParagraph`, `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `_MobileDownloads__WEBPACK_IMPORTED_MODULE_4__.MobileDownloads`, `_MultiSelect__WEBPACK_IMPORTED_MODULE_5__.MultiSelect`, `_PinnableSitesList__WEBPACK_IMPORTED_MODULE_15__.PinnableSitesList`, `_SingleSelect__WEBPACK_IMPORTED_MODULE_3__.SingleSelect`, `_TextAreaTile__WEBPACK_IMPORTED_MODULE_6__.TextAreaTile`, `_TextBoxTile__WEBPACK_IMPORTED_MODULE_17__.TextBoxTile`, `content.isEncryptedBackup`, `content.position`, `header.linkStyle`, `header.style`, `header.subtitle`, `header?.alternateTitle`, `header?.title`, `props.activeMultiSelect`, `props.activeSingleSelectSelections`, `props.activeTheme`, `props.content.skip_button`, `props.contentToggleChecked`, `props.handleAction`, `props.installedAddons`, `props.messageId`, `props.screenMultiSelects`, `props.setActiveMultiSelect`, `props.setActiveSingleSelectSelection`, `props.setContentToggleChecked`, `props.setPinnedSite`, `props.setScreenMultiSelects`, `props.setTextInput`, `props.textInputs`, `tile.data`, `tile.data.style`, `tile.data.url`, `tile.data?.installSource`, `tile.data?.url`, `tile.options`, `tile.text`, `tile.type`

## onClick()
- 位置: L5113-5113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `toggleTile()`

## renderContentTiles()
- 位置: L5234-5244
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `renderContentTile()`
- 条件付き依存: `if (Array.isArray(tiles))` → `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 条件付き依存: `if (Array.isArray(tiles))` → `react__WEBPACK_IMPORTED_MODULE_0___default()`
- 条件付き依存: `if (Array.isArray(tiles))` → `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_13__.MultiStageUtils.getValidStyle()`
- 条件付き依存: `if (Array.isArray(tiles))` → `tiles.map()`
- 条件付き依存: `if (Array.isArray(tiles))` → `renderContentTile()`
- 参照: `content?.tiles_container?.style`

## AddonsPicker()
- 位置: L5269-5269
- 役割: (未記入)
- 触るとき: (未記入)

## AddonsPicker()
- 位置: L5284-5396
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `content.tiles.data.map()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `_InstallButton__WEBPACK_IMPORTED_MODULE_3__.InstallButton`, `_MSLocalized__WEBPACK_IMPORTED_MODULE_2__.Localized`, `author.byLine`, `author.name`, `react__WEBPACK_IMPORTED_MODULE_0___default().Fragment`

## handleInstallClick()
- 位置: L5294-5309
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_1__.MultiStageUtils.sendActionTelemetry()`, `handleAction()`
- 参照: `action.data`, `action.type`, `content.tiles.data`, `event.currentTarget.value`

## handleAuthorClick()
- 位置: L5310-5319
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_1__.MultiStageUtils.handleUserAction()`, `event.stopPropagation()`

## onClick()
- 位置: L5359-5361
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleAuthorClick()`
- 参照: `author.id`

## InstallButton()
- 位置: L5405-5405
- 役割: (未記入)
- 触るとき: (未記入)

## Loader()
- 位置: L5406-5406
- 役割: (未記入)
- 触るとき: (未記入)

## Loader()
- 位置: L5417-5425
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`

## InstallButton()
- 位置: L5426-5482
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useState)()`, `JSON.stringify()`, `getDefaultInstallCompleteLabel()`, `props.installedAddons?.includes()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `setInstallComplete()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `props.addonId`, `props.addonName`, `props.addonType`, `props.index`, `props.install_complete_label`, `props.install_label`, `props.installedAddons`, `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useState`

## getDefaultInstallCompleteLabel()
- 位置: L5434-5450
- 役割: (未記入)
- 触るとき: (未記入)

## onClick()
- 位置: L5455-5467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `props.handleAction()`, `setInstalling()`, `window.AWEnsureAddonInstalled()`, `window.AWEnsureAddonInstalled(props.addonId).then()`
- 条件付き依存: `if (value === "complete")` → `setInstallComplete()`
- 参照: `props.addonId`

## SingleSelect()
- 位置: L5491-5491
- 役割: (未記入)
- 触るとき: (未記入)

## SingleSelect()
- 位置: L5512-5684
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)()`, `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_4__.MultiStageUtils.getValidStyle()`, `content.tiles.data.map()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `valOrObj()`
- 条件付き依存: `if (isSingleSelect && !activeSingleSelectSelections[singleSelectId])` → `setActiveSingleSelectSelection()`
- 条件付き依存: `if (isSingleSelect && !activeSingleSelectSelections[singleSelectId])` → `content.tiles?.data.find()`
- 条件付き依存: `if (isSingleSelect && !activeSingleSelectSelections[singleSelectId])` → `autoTriggerAllowed()`
- 条件付き依存: `if (isSingleSelect && content.tiles?.autoTrigger && autoTriggerAllowed(selectedTile?.action))` → `handleAction()`
- 参照: `_CarouselNav__WEBPACK_IMPORTED_MODULE_5__.CarouselNav`, `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `_TileButton__WEBPACK_IMPORTED_MODULE_2__.TileButton`, `_TileList__WEBPACK_IMPORTED_MODULE_3__.TileList`, `body.items`, `content.subtitle`, `content.tiles?.autoTrigger`, `content.tiles?.category?.type`, `content.tiles?.data`, `content.tiles?.data[0].id`, `content.tiles?.pill_nav_label`, `content.tiles?.selected`, `content.tiles?.subtitle`, `content.tiles?.type`, `flair.centered`, `flair.spacer`, `flair.text`, `icon.background`, `icon.darkModeBackground`, `icon.width`, `icon?.darkModeBackground`, `icon?.width`, `iconStyle.background`, `opt.id`, `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useRef`, `selectedTile.id`, `selectedTile?.action`

## handlePillSelect()
- 位置: L5524-5533
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `card?.scrollIntoView()`, `cardRefs.current.get()`, `setActiveSingleSelectSelection()`, `window.matchMedia()`
- 参照: `window.matchMedia?.("(prefers-reduced-motion: reduce)")?.matches`

## autoTriggerAllowed()
- 位置: L5534-5552
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checkAction()`
- 条件付き依存: `if (itemAction.type === "MULTI_ACTION")` → `itemAction.data.actions.some()`
- 条件付き依存: `if (itemAction.type === "MULTI_ACTION")` → `checkAction()`
- 参照: `itemAction.type`

## checkAction()
- 位置: L5538-5546
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allowedActions.includes()`, `allowedPrefs.includes()`
- 参照: `action.data?.pref.name`, `action.type`

## valOrObj()
- 位置: L5608-5608
- 役割: (未記入)
- 触るとき: (未記入)

## handleClick()
- 位置: L5615-5620
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleAction()`
- 条件付き依存: `if (isSingleSelect)` → `setActiveSingleSelectSelection()`

## handleKeyDown()
- 位置: L5621-5627
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (evt.key === "Enter" || evt.keyCode === 13)` → `handleClick()`
- 参照: `evt.currentTarget.value`, `evt.key`, `evt.keyCode`

## ref()
- 位置: L5633-5639
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (el)` → `cardRefs.current.set()`
- 条件付き依存: `if (!(el))` → `cardRefs.current.delete()`

## onKeyDown()
- 位置: L5640-5640
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleKeyDown()`

## onClick()
- 位置: L5660-5660
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleClick()`

## TileButton()
- 位置: L5693-5693
- 役割: (未記入)
- 触るとき: (未記入)

## TileButton()
- 位置: L5704-5731
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `content.label`, `content.style`, `react__WEBPACK_IMPORTED_MODULE_0__.useRef`

## onClick()
- 位置: L5714-5721
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleAction()`
- 参照: `content.action`, `event.target.id`, `ref.current`

## TileList()
- 位置: L5740-5740
- 役割: (未記入)
- 触るとき: (未記入)

## TileList()
- 位置: L5753-5783
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_1__.MultiStageUtils.getValidStyle()`, `content.items.map()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_2__.Localized`

## CarouselNav()
- 位置: L5792-5792
- 役割: (未記入)
- 触るとき: (未記入)

## _extends()
- 位置: L5796-5796
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `({}).hasOwnProperty.call()`, `Object.assign.bind()`, `_extends.apply()`
- 参照: `Object.assign`, `arguments.length`

## CarouselNav()
- 位置: L5802-5844
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)()`, `_extends()`, `group.addEventListener()`, `group.removeEventListener()`, `items.filter()`, `pillItems.map()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `groupRef.current`, `item.id`, `item?.pill`, `navLabel.raw`, `navLabel?.raw`, `navLabel?.string_id`, `onSelectRef.current`, `pill.icon`, `pill.label?.raw`, `pill.label?.string_id`, `pillItems.length`, `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useRef`

## handleChange()
- 位置: L5816-5816
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `onSelectRef.current()`
- 参照: `group.value`

## MarketplaceButtons()
- 位置: L5853-5853
- 役割: (未記入)
- 触るとき: (未記入)

## MobileDownloads()
- 位置: L5854-5854
- 役割: (未記入)
- 触るとき: (未記入)

## MarketplaceButtons()
- 位置: L5867-5883
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `props.buttons.includes()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `props.handleAction`

## MobileDownloads()
- 位置: L5884-5907
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.getLoadingStrategyFor()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `window.AWSendToDeviceEmailsSupported()`
- 参照: `QRCode.alt_text`, `QRCode.alt_text.string_id`, `QRCode.image_url`, `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `props.data`, `props.data.email`, `props.data.email.link_text`, `props.data.marketplace_buttons`, `props.handleAction`

## MultiSelect()
- 位置: L5916-5916
- 役割: (未記入)
- 触るとき: (未記入)

## UncheckedNotice()
- 位置: L5954-5984
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`

## MultiSelect()
- 位置: L5985-6160
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useCallback)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useMemo)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)()`, `Object.keys()`, `Object.keys(refs.current).forEach()`, `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.getTileStyle()`, `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.getValidStyle()`, `activeMultiSelect?.includes()`, `data.find()`, `getOrderedIds()`, `getOrderedIds().map()`, `items.map()`, `items.some()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `setActiveMultiSelect()`
- 条件付き依存: `if (refs.current[key]?.checked)` → `newActiveMultiSelect.push()`
- 条件付き依存: `if (!activeMultiSelect)` → `items.forEach()`
- 条件付き依存: `if (defaultValue && id)` → `newActiveMultiSelect.push()`
- 条件付き依存: `if (!activeMultiSelect)` → `setActiveMultiSelect()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `content.tiles`, `content.tiles.footer`, `content.tiles.footer.checkedLabel`, `content.tiles.footer.unCheckAllLabel`, `content.tiles.label`, `i.id`, `icon?.style`, `item.id`, `react__WEBPACK_IMPORTED_MODULE_0__.useCallback`, `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useMemo`, `react__WEBPACK_IMPORTED_MODULE_0__.useRef`, `refs.current`, `refs.current[key]?.checked`

## getOrderedIds()
- 位置: L6009-6021
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.random()`, `data.map()`, `data.map(item => ({ id: item.id, rank: item.randomize ? Math.random() : NaN })).sort()`, `data.map(item => ({ id: item.id, rank: item.randomize ? Math.random() : NaN })).sort((a, b) => b.rank - a.rank).map()`, `setScreenMultiSelects()`
- 参照: `a.rank`, `b.rank`, `item.id`, `item.randomize`

## PickerIcon()
- 位置: L6026-6039
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`

## handleCheckboxContainerInteraction()
- 位置: L6044-6066
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `container.querySelector()`, `handleChange()`
- 条件付き依存: `if (e.key === " ")` → `e.preventDefault()`
- 参照: `checkbox.checked`, `e.currentTarget`, `e.key`, `e.type`

## ref()
- 位置: L6127-6127
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `refs.current`

## TextAreaTile()
- 位置: L6169-6169
- 役割: (未記入)
- 触るとき: (未記入)

## TextAreaTile()
- 位置: L6181-6236
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useCallback)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useMemo)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useState)()`, `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_1__.MultiStageUtils.getValidStyle()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `setIsValid()`, `setTextInput()`
- 条件付き依存: `if (data.character_limit)` → `setCharCounter()`
- 条件付き依存: `if (!textInput)` → `setTextInput()`
- 参照: `content.tiles`, `data.char_counter_style`, `data.character_limit`, `data.cols`, `data.container_style`, `data.id`, `data.placeholder`, `data.rows`, `data.textarea_style`, `event.target.value`, `event.target.value.length`, `react__WEBPACK_IMPORTED_MODULE_0__.useCallback`, `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useMemo`, `react__WEBPACK_IMPORTED_MODULE_0__.useState`, `textInput?.value`

## EmbeddedMigrationWizard()
- 位置: L6245-6245
- 役割: (未記入)
- 触るとき: (未記入)

## EmbeddedMigrationWizard()
- 位置: L6282-6336
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)()`, `current?.addEventListener()`, `current?.removeEventListener()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `content.tiles?.migration_wizard_options`, `options?.checkbox_margin_block`, `options?.checkbox_margin_inline`, `options?.data_import_complete_success_string`, `options?.force_show_import_all`, `options?.header_font_size`, `options?.header_font_weight`, `options?.header_margin_block`, `options?.hide_option_expander_subtitle`, `options?.hide_select_all`, `options?.import_button_class`, `options?.import_button_string`, `options?.option_expander_title_string`, `options?.selection_header_string`, `options?.selection_subheader_string`, `options?.subheader_font_size`, `options?.subheader_font_weight`, `options?.subheader_margin_block`, `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useRef`

## handleBeginMigration()
- 位置: L6289-6296
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleAction()`

## handleClose()
- 位置: L6297-6303
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleAction()`

## EmbeddedThemePicker()
- 位置: L6345-6345
- 役割: (未記入)
- 触るとき: (未記入)

## EmbeddedThemePicker()
- 位置: L6354-6372
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)()`, `customElements.whenDefined()`, `customElements.whenDefined("theme-picker").then()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `themePickerRef.current?.shown()`
- 参照: `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useRef`

## EmbeddedFxBackupOptIn()
- 位置: L6381-6381
- 役割: (未記入)
- 触るとき: (未記入)

## EmbeddedFxBackupOptIn()
- 位置: L6390-6476
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)()`, `current?.addEventListener()`, `current?.removeEventListener()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useRef`

## handleEnableScheduledBackups()
- 位置: L6411-6421
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleAction()`

## handleAdvanceScreens()
- 位置: L6422-6432
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleAction()`

## handleStateUpdate()
- 位置: L6433-6450
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `current.setAttribute()`
- 参照: `current.supportBaseLink`, `state.defaultParent`, `state.supportBaseLink`

## ActionChecklist()
- 位置: L6485-6485
- 役割: (未記入)
- 触るとき: (未記入)

## ActionChecklistItem()
- 位置: L6486-6486
- 役割: (未記入)
- 触るとき: (未記入)

## ActionChecklistProgressBar()
- 位置: L6487-6487
- 役割: (未記入)
- 触るとき: (未記入)

## evaluateTargeting()
- 位置: async L6500-6502
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.AWEvaluateAttributeTargeting()`

## ActionChecklistItem()
- 位置: L6503-6545
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useState)()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `setInitialTargetingValue()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `item.id`, `item.label`, `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useState`

## setInitialTargetingValue()
- 位置: async L6510-6512
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `evaluateTargeting()`, `setActionTargeting()`
- 参照: `item.targeting`

## onButtonClick()
- 位置: L6516-6521
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleAction()`, `setActionTargeting()`

## ActionChecklistProgressBar()
- 位置: L6546-6566
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.round()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`

## ActionChecklist()
- 位置: L6567-6652
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useState)()`, `determineProgressValue()`, `evaluateAllActionsTargeting()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `tiles.map()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `content.action_checklist_subtitle`, `content.remove_checklist_button`, `content.remove_checklist_button.label`, `content.tiles.data`, `item.id`, `item.showExternalLinkIcon`, `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useState`, `tiles.length`

## determineProgressValue()
- 位置: L6576-6579
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setProgressValue()`
- 参照: `tiles.length`

## evaluateAllActionsTargeting()
- 位置: async L6587-6591
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `completedActions.filter()`, `evaluateTargeting()`, `setNumberOfCompletedActions()`, `tiles.map()`
- 参照: `completedActions.filter(item => item).length`, `item.targeting`

## handleTileClick()
- 位置: L6601-6616
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.handleUserAction()`, `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.sendActionTelemetry()`, `setNumberOfCompletedActions()`
- 参照: `content.tiles.data`, `event.currentTarget.value`

## handleRemoveChecklistClick()
- 位置: L6617-6626
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handleAction()`
- 参照: `event.currentTarget`, `event.currentTarget.value`

## EmbeddedBrowser()
- 位置: L6661-6661
- 役割: (未記入)
- 触るとき: (未記入)

## "default"()
- 位置: L6662-6662
- 役割: (未記入)
- 触るとき: (未記入)

## EmbeddedBrowser()
- 位置: L6674-6677
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `document.createXULElement`, `props.url`

## EmbeddedBrowserInner()
- 位置: L6678-6719
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)()`, `attributes.forEach()`, `browserEl.setAttribute()`, `document.createXULElement()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `ref.current.appendChild()`, `window.AWPredictRemoteType()`
- 条件付き依存: `if (browserRef.current)` → `browserRef.current.fixupAndLoadURIString()`
- 条件付き依存: `if (browserRef.current)` → `Services.scriptSecurityManager.createNullPrincipal()`
- 条件付き依存: `if (browserRef.current && style)` → `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_1__.MultiStageUtils.getValidStyle()`
- 条件付き依存: `if (browserRef.current && style)` → `Object.keys(validStyles).forEach()`
- 条件付き依存: `if (browserRef.current && style)` → `Object.keys()`
- 条件付き依存: `if (browserRef.current && style)` → `browserRef.current.style.setProperty()`
- 参照: `browserRef.current`, `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useRef`, `ref.current`
- XPCOM: `Services.scriptSecurityManager`

## ConfirmationChecklist()
- 位置: L6729-6729
- 役割: (未記入)
- 触るとき: (未記入)

## ConfirmationChecklist()
- 位置: L6741-6783
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_1__.MultiStageUtils.getValidStyle()`, `content.items.map()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `_LinkParagraph__WEBPACK_IMPORTED_MODULE_3__.LinkParagraph`, `_MSLocalized__WEBPACK_IMPORTED_MODULE_2__.Localized`, `content.style`

## EmbeddedBackupRestore()
- 位置: L6792-6792
- 役割: (未記入)
- 触るとき: (未記入)

## EmbeddedBackupRestore()
- 位置: L6805-6861
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useCallback)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)()`, `(0,react__WEBPACK_IMPORTED_MODULE_0__.useState)()`, `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_1__.MultiStageUtils.handleUserAction()`, `backupRef.addEventListener()`, `backupRef.removeEventListener()`, `loadRestore()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `setRecoveryInProgress()`
- 条件付き依存: `if (backupRef.backupServiceState)` → `setRecoveryInProgress()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_2__.Localized`, `backupRef.backupServiceState`, `backupRef.backupServiceState.recoveryInProgress`, `e.detail.recoveryInProgress`, `react__WEBPACK_IMPORTED_MODULE_0__.useCallback`, `react__WEBPACK_IMPORTED_MODULE_0__.useEffect`, `react__WEBPACK_IMPORTED_MODULE_0__.useRef`, `react__WEBPACK_IMPORTED_MODULE_0__.useState`, `ref.current`, `skipButton.label`, `skipButton?.has_arrow_icon`

## loadRestore()
- 位置: async L6812-6814
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `window.AWFindBackupsInWellKnownLocations()`

## PinnableSitesList()
- 位置: L6870-6870
- 役割: (未記入)
- 触るとき: (未記入)

## PinnableSitesList()
- 位置: L6888-6973
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(0,react__WEBPACK_IMPORTED_MODULE_0__.useState)()`, `(items ?? []).map()`, `Object.fromEntries()`, `items.map()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `item.description`, `item.iconUrl`, `item.id`, `item.name`, `item.title`, `items?.length`, `react__WEBPACK_IMPORTED_MODULE_0__.useState`, `tile?.alwaysShowPinButton`, `tile?.data`, `tile?.pinButtonLabel`

## setItemState()
- 位置: L6901-6904
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `setItemStates()`

## handlePin()
- 位置: async L6905-6938
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.sendActionTelemetry()`, `handleAction()`, `setItemState()`
- 条件付き依存: `if (result !== false)` → `setPinnedSite()`
- 参照: `item.iconUrl`, `item.id`, `item.name`, `item.personalized`, `item.url`

## onClick()
- 位置: L6967-6967
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `handlePin()`

## ContentToggle()
- 位置: L6982-6982
- 役割: (未記入)
- 触るとき: (未記入)

## ContentToggle()
- 位置: L6993-7014
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `onToggle()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `react__WEBPACK_IMPORTED_MODULE_0___default().useCallback()`
- 参照: `_MSLocalized__WEBPACK_IMPORTED_MODULE_1__.Localized`, `content.tiles`, `data.label`, `data.visible`, `e.target.checked`

## TextBoxTile()
- 位置: L7023-7023
- 役割: (未記入)
- 触るとき: (未記入)

## TextBoxTile()
- 位置: L7035-7049
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_1__.MultiStageUtils.getValidStyle()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `content.tiles`, `data.alternateContent`, `data.content`, `data.style`

## BASE_PARAMS()
- 位置: L7058-7058
- 役割: (未記入)
- 触るとき: (未記入)

## addUtmParams()
- 位置: L7059-7059
- 役割: (未記入)
- 触るとき: (未記入)

## addUtmParams()
- 位置: L7080-7094
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `returnUrl.searchParams.has()`
- 条件付き依存: `if (!returnUrl.searchParams.has(key))` → `returnUrl.searchParams.append()`
- 条件付き依存: `if (!returnUrl.searchParams.has("utm_term"))` → `returnUrl.searchParams.append()`

## __webpack_require__()
- 位置: L7104-7122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `__webpack_modules__[moduleId]()`
- 参照: `cachedModule.exports`, `module.exports`

## __webpack_require__.n()
- 位置: L7128-7134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `__webpack_require__.d()`
- 参照: `module.__esModule`

## __webpack_require__.d()
- 位置: L7140-7146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `__webpack_require__.o()`
- 条件付き依存: `if (__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key))` → `Object.defineProperty()`

## __webpack_require__.o()
- 位置: L7151-7151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.prototype.hasOwnProperty.call()`

## __webpack_require__.r()
- 位置: L7157-7162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`
- 条件付き依存: `if (typeof Symbol !== 'undefined' && Symbol.toStringTag)` → `Object.defineProperty()`
- 参照: `Symbol.toStringTag`

## _extends()
- 位置: L7177-7177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `({}).hasOwnProperty.call()`, `Object.assign.bind()`, `_extends.apply()`
- 参照: `Object.assign`, `arguments.length`

## AboutWelcome.constructor()
- 位置: L7187-7193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.fetchFxAFlowUri.bind()`
- 参照: `this.fetchFxAFlowUri`, `this.state`

## AboutWelcome.fetchFxAFlowUri()
- 位置: async L7194-7198
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setState()`, `window.AWGetFxAMetricsFlowURI()`

## AboutWelcome.componentDidMount()
- 位置: L7199-7233
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.props.skipFxA)` → `this.fetchFxAFlowUri()`
- 条件付き依存: `if (document.readyState === "complete")` → `recordImpression()`
- 条件付き依存: `if (!(document.readyState === "complete"))` → `window.addEventListener()`
- 条件付き依存: `if (!(document.readyState === "complete"))` → `recordImpression()`
- 条件付き依存: `if (document.location.href === "about:welcome")` → `window.AWSendToParent()`
- 参照: `document.location.href`, `document.readyState`, `this.props.messageId`, `this.props.skipFxA`

## recordImpression()
- 位置: L7205-7217
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_asrouter_content_src_lib_multistage_utils_mjs__WEBPACK_IMPORTED_MODULE_2__.MultiStageUtils.sendImpressionTelemetry()`, `performance.getEntriesByName()`, `performance.getEntriesByName("mount").pop()`, `performance.getEntriesByType()`, `performance.getEntriesByType("navigation").pop()`
- 参照: `performance.getEntriesByName("mount").pop().startTime`, `this.props.UTMTerm`, `this.props.messageId`

## AboutWelcome.render()
- 位置: L7234-7258
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`
- 参照: `_asrouter_content_src_components_MultiStageAboutWelcome__WEBPACK_IMPORTED_MODULE_3__.MultiStageAboutWelcome`, `props.UTMTerm`, `props.addonId`, `props.appAndSystemLocaleInfo`, `props.aria_role`, `props.backdrop`, `props.disableHistoryUpdates`, `props.iconURL`, `props.messageId`, `props.name`, `props.requireAction`, `props.screens`, `props.screenshots`, `props.startScreen`, `props.transitions`, `props.type`, `props.url`, `this.state.metricsFlowUri`

## ComputeTelemetryInfo()
- 位置: L7262-7275
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `welcomeContent.type.toUpperCase()`
- 条件付き依存: `if (welcomeContent.id)` → `welcomeContent.id.toUpperCase()`
- 条件付き依存: `if (experimentId && branchId)` → ``aboutwelcome-${experimentId}-${branchId}`.toLowerCase()`
- 参照: `welcomeContent.id`, `welcomeContent.template`

## retrieveRenderContent()
- 位置: async L7276-7303
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ComputeTelemetryInfo()`, `window.AWGetFeatureConfig()`
- 条件付き依存: `if (document.location.href === "about:welcome" && window.AWWaitForNimbus)` → `window.AWWaitForNimbus()`
- 条件付き依存: `if (document.location.href === "about:welcome" && window.AWWaitForNimbus)` → `console.error()`
- 参照: `document.location.href`, `featureConfig.branch`, `featureConfig.branch.slug`, `featureConfig.slug`, `window.AWWaitForNimbus`

## mount()
- 位置: async L7304-7314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `_extends()`, `document.getElementById()`, `react__WEBPACK_IMPORTED_MODULE_0___default()`, `react__WEBPACK_IMPORTED_MODULE_0___default().createElement()`, `react_dom__WEBPACK_IMPORTED_MODULE_1___default()`, `react_dom__WEBPACK_IMPORTED_MODULE_1___default().render()`, `retrieveRenderContent()`
