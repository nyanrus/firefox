# browser/components/customizableui/CustomizableUI.sys.mjs

source: browser/components/customizableui/CustomizableUI.sys.mjs
source-hash: 76cab7f8e4630119c8f166f14bfc5a781f49f5fd
lines: 8679

## <module>
- 役割: ツールバーやパネルのウィジェット配置を管理する CustomizableUI の内部実装。エリア登録、配置の保存と復元、版ごとのマイグレーションを担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `CustomizableUI.getWidgetIdsInArea()`, `CustomizableUIInternal.initialize()`, `CustomizableUIInternal.updateTabStripOrientation()`, `Object.freeze()`, `Services.prefs.setBoolPref()`, `Services.strings.createBundle()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `gAreas .get()`, `gAreas .get(CustomizableUI.AREA_NAVBAR) .get()`, `lazy.log.debug()`, `navbarPlacements.includes()`

## initialize()
- 位置: L320-458
- 役割: CustomizableUI の初期化。テーマ・アドオン監視を張り、既定ウィジェットとエリアを登録し、保存状態を読み込んで版移行を実行する。
- 触るとき: 起動時に既定ツールバーの構成や新しい既定ボタンの追加タイミングを変えるとき、またはアドオン由来の初期化順序を調べるとき。
- 呼び出し先: `Services.obs.addObserver()`, `Services.policies.isAllowed()`, `Services.prefs.addObserver()`, `addons.find()`, `gAreas.keys()`, `lazy.AddonManager.addAddonListener()`, `lazy.AddonManager.getAddonsByTypes()`, `lazy.AddonManagerPrivate.databaseReady.then()`, `lazy.log.debug()`, `this._setAutoTouchModeDefault()`, `this.addListener()`, `this.defineBuiltInWidgets()`, `this.initializeForTabsOrientation()`, `this.loadSavedState()`, `this.markObsoleteBuiltinButtonsSeen()`, `this.reconcileSidebarPrefs()`, `this.registerArea()`, `this.updateForNewProtonVersion()`, `this.updateForNewVersion()`
- 条件付き依存: `if (!Services.appinfo.nativeMenubar)` → `this.registerArea()`
- 参照: `AppConstants.MOZ_DEV_EDITION`, `CustomizableUI.AREA_ADDONS`, `CustomizableUI.AREA_BOOKMARKS`, `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `CustomizableUI.AREA_MENUBAR`, `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.AREA_VERTICAL_TABSTRIP`, `CustomizableUI.TYPE_PANEL`, `CustomizableUI.TYPE_TOOLBAR`, `CustomizableUI.verticalTabsEnabled`, `Services.appinfo.nativeMenubar`, `addon.id`, `addon.isActive`, `lazy.ippEnabled`, `lazy.resetPBMToolbarButtonEnabled`, `lazy.sidebarRevampEnabled`
- XPCOM: `Services.appinfo` / `Services.obs` / `Services.policies` / `Services.prefs`

## _setAutoTouchModeDefault()
- 位置: L464-471
- 役割: browser.touchmode.auto の既定値を、nova が無効かどうかで既定ブランチに設定する。
- 触るとき: タッチモードの自動切替の既定を変えるとき、または nova 有効時の UI 密度がおかしいと感じて原因を追うとき。
- 呼び出し先: `Services.prefs .getDefaultBranch()`, `Services.prefs .getDefaultBranch("") .setBoolPref()`, `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## onEnabled()
- 位置: L480-484
- 役割: テーマ系アドオンが有効化されたとき、選択中テーマを差し替える。
- 触るとき: テーマの切替後に選択中テーマの参照がずれる不具合を調べるとき。
- 参照: `addon.type`

## builtinAreas()
- 位置: L491-497
- 役割: 組み込みエリアの ID 集合を返す。ツールバー群に加えて固定オーバーフローパネルとアドオン用エリアを含める。
- 触るとき: 組み込みエリアかどうかの判定条件を変えたり、カスタムツールバーの扱いを追加したりするとき。
- 参照: `CustomizableUI.AREA_ADDONS`, `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `this.builtinToolbars`

## builtinToolbars()
- 位置: L505-515
- 役割: 組み込みツールバーの ID 集合を返す。navbar・bookmarks・tabstrip に加え、macOS 以外では menubar を含める。
- 触るとき: プラットフォームごとに出すツールバーを変えるとき、またはメニューバーが macOS で見えない理由を調べるとき。
- 条件付き依存: `if (AppConstants.platform != "macosx")` → `toolbars.add()`
- 参照: `AppConstants.platform`, `CustomizableUI.AREA_BOOKMARKS`, `CustomizableUI.AREA_MENUBAR`, `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.AREA_TABSTRIP`

## defineBuiltInWidgets()
- 位置: L521-525
- 役割: CustomizableWidgets の各定義を createBuiltinWidget に渡して組み込みウィジェットを登録する。
- 触るとき: 新しい組み込みボタンを追加し、それが登録されるか確かめるとき。
- 呼び出し先: `this.createBuiltinWidget()`
- 参照: `lazy.CustomizableWidgets`

## updateForNewVersion()
- 位置: L532-1048
- 役割: 保存状態の currentVersion を見て、版ごとの配置マイグレーションを順に適用する。新規既定ウィジェットの追加候補も gFuturePlacements に積む。
- 触るとき: ツールバーのボタン配置を版をまたいで移すとき、または古いプロファイルでボタンが消えたり重複したりする原因を調べるとき。
- 条件付き依存: `if (widget.defaultArea && widget._introducedInVersion === "pref")` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (widget._introducedInVersion === "pref")` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (!(widget._introducedInVersion > currentVersion))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( widget._introducedByPref && Services.prefs.getBoolPref(widget._introducedByPref) )` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (shouldAdd)` → `gFuturePlacements.get()`
- 条件付き依存: `if (futurePlacements)` → `futurePlacements.add()`
- 条件付き依存: `if (!(futurePlacements))` → `gFuturePlacements.set()`
- 条件付き依存: `if (shouldSetPref)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if ( currentVersion < 7 && gSavedState.placements[CustomizableUI.AREA_NAVBAR] )` → `newPlacements.includes()`
- 条件付き依存: `if (!newPlacements.includes(button))` → `newPlacements.push()`
- 条件付き依存: `if (!newPlacements.includes("sidebar-button"))` → `newPlacements.unshift()`
- 条件付き依存: `if (!AppConstants.MOZ_DEV_EDITION)` → `defaultPlacements.splice()`
- 条件付き依存: `if (currentVersion < 8 && gSavedState.placements["PanelUI-contents"])` → `savedPanelPlacements.filter()`
- 条件付き依存: `if (currentVersion < 8 && gSavedState.placements["PanelUI-contents"])` → `defaultPlacements.includes()`
- 条件付き依存: `if (currentVersion < 9 && gSavedState.placements["nav-bar"])` → `placements.includes()`
- 条件付き依存: `if (placements.includes("urlbar-container"))` → `placements.indexOf()`
- 条件付き依存: `if (placements.includes("urlbar-container"))` → `placements[urlbarIndex - 1].startsWith()`
- 条件付き依存: `if ( urlbarIndex == 0 || !placements[urlbarIndex - 1].startsWith(kSpecialWidgetPfx + "spring") )` → `placements.splice()`
- 条件付き依存: `if (placements.includes("urlbar-container"))` → `placements[secondSpringIndex].startsWith()`
- 条件付き依存: `if ( secondSpringIndex == placements.length || !placements[secondSpringIndex].startsWith( kSpecialWidgetPfx + "spring" ) )` → `placements.splice()`
- 条件付き依存: `if (placements.includes("bookmarks-menu-button"))` → `placements.indexOf()`
- 条件付き依存: `if (placements.includes("bookmarks-menu-button"))` → `placements.splice()`
- 条件付き依存: `if (currentVersion < 10)` → `Object.values()`
- 条件付き依存: `if (currentVersion < 10)` → `placements.includes()`
- 条件付き依存: `if (placements.includes("webcompat-reporter-button"))` → `placements.splice()`
- 条件付き依存: `if (placements.includes("webcompat-reporter-button"))` → `placements.indexOf()`
- 条件付き依存: `if (currentVersion < 11)` → `Object.values()`
- 条件付き依存: `if (currentVersion < 11)` → `placements.indexOf()`
- 条件付き依存: `if (existingIndex != -1)` → `placements.splice()`
- 条件付き依存: `if (navbarPlacements)` → `navbarPlacements.indexOf()`
- 条件付き依存: `if (navbarPlacements)` → `this.matchingSpecials()`
- 条件付き依存: `if (navbarPlacements)` → `navbarPlacements.splice()`
- 条件付き依存: `if (currentVersion < 12)` → `Object.values()`
- 条件付き依存: `if (currentVersion < 12)` → `placements.indexOf()`
- 条件付き依存: `if (buttonIndex != -1)` → `placements.splice()`
- 条件付き依存: `if (currentVersion < 13)` → `Object.values()`
- 条件付き依存: `if (currentVersion < 13)` → `placements.indexOf()`
- 条件付き依存: `if (currentVersion < 14)` → `this.builtinAreas.has()`
- 条件付き依存: `if (navbarPlacements)` → `navbarPlacements.push()`
- 条件付き依存: `if (currentVersion < 18)` → `tabstripPlacements.includes()`
- 条件付き依存: `if ( tabstripPlacements && !tabstripPlacements.includes("firefox-view-button") )` → `tabstripPlacements.unshift()`
- 条件付き依存: `if (currentVersion < 19)` → `CustomizableUI.isWebExtensionWidget()`
- 条件付き依存: `if (CustomizableUI.isWebExtensionWidget(widgetId))` → `extWidgets.push()`
- 条件付き依存: `if (!(CustomizableUI.isWebExtensionWidget(widgetId)))` → `builtInWidgets.push()`
- 条件付き依存: `if (currentVersion < 21)` → `navbarPlacements.includes()`
- 条件付き依存: `if (!navbarPlacements.includes("vertical-spacer"))` → `navbarPlacements.indexOf()`
- 条件付き依存: `if (!navbarPlacements.includes("vertical-spacer"))` → `gSavedState.placements[CustomizableUI.AREA_NAVBAR].splice()`
- 条件付き依存: `if (currentVersion < 22)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (navbarPlacements[0] === "sidebar-button")` → `navbarPlacements.shift()`
- 条件付き依存: `if (navbarPlacements[0] === "sidebar-button")` → `navbarPlacements.push()`
- 条件付き依存: `if (currentVersion < 23)` → `navbarPlacements.indexOf()`
- 条件付き依存: `if (buttonIndex != -1)` → `navbarPlacements.splice()`
- 条件付き依存: `if (currentVersion < 24)` → `navbarPlacements.includes()`
- 条件付き依存: `if ( navbarPlacements && !navbarPlacements.includes("reset-pbm-toolbar-button") )` → `navbarPlacements.push()`
- 条件付き依存: `if (currentVersion < 25)` → `firefoxViewArea?.indexOf()`
- 条件付き依存: `if (firefoxViewArea?.[defaultIndex] === "firefox-view-button")` → `JSON.parse()`
- 条件付き依存: `if (firefoxViewArea?.[defaultIndex] === "firefox-view-button")` → `Services.prefs.getStringPref()`
- 条件付き依存: `if (firefoxViewArea?.[defaultIndex] === "firefox-view-button")` → `console.error()`
- 条件付き依存: `if (!shouldKeepFirefoxView)` → `firefoxViewArea.splice()`
- 条件付き依存: `if (currentVersion < 26)` → `insertBeforeAllTabs()`
- 条件付き依存: `if (currentVersion < 26)` → `CustomizableUIInternal.getSavedHorizontalSnapshotState()`
- 条件付き依存: `if (horizontalSnapshot.length)` → `CustomizableUIInternal.saveHorizontalTabStripState()`
- 条件付き依存: `if (horizontalSnapshot.length)` → `insertBeforeAllTabs()`
- 条件付き依存: `if (currentVersion < 27)` → `areaPlacements()`
- 条件付き依存: `if (currentVersion < 27)` → `tabstrip.includes()`
- 条件付き依存: `if (currentVersion < 27)` → `navbar.includes()`
- 条件付き依存: `if ( CustomizableUI.verticalTabsEnabled && tabstrip.includes(organizeTabs) && !navbar.includes(organizeTabs) && navbar.includes(switcher) )` → `tabstrip.splice()`
- 条件付き依存: `if ( CustomizableUI.verticalTabsEnabled && tabstrip.includes(organizeTabs) && !navbar.includes(organizeTabs) && navbar.includes(switcher) )` → `tabstrip.indexOf()`
- 条件付き依存: `if ( CustomizableUI.verticalTabsEnabled && tabstrip.includes(organizeTabs) && !navbar.includes(organizeTabs) && navbar.includes(switcher) )` → `navbar.splice()`
- 条件付き依存: `if ( CustomizableUI.verticalTabsEnabled && tabstrip.includes(organizeTabs) && !navbar.includes(organizeTabs) && navbar.includes(switcher) )` → `navbar.indexOf()`
- 条件付き依存: `if (currentVersion < 27)` → `gSeenWidgets.has()`
- 条件付き依存: `if (currentVersion < 27)` → `Object.values(gSavedState.placements).some()`
- 条件付き依存: `if (currentVersion < 27)` → `Object.values()`
- 条件付き依存: `if (currentVersion < 27)` → `Array.isArray()`
- 条件付き依存: `if (currentVersion < 27)` → `placements.includes()`
- 条件付き依存: `if (currentVersion < 27)` → `placeBeforeSwitcher()`
- 条件付き依存: `if (currentVersion < 27)` → `CustomizableUIInternal.getSavedHorizontalSnapshotState()`
- 条件付き依存: `if (horizontalSnapshot.length)` → `placeBeforeSwitcher()`
- 条件付き依存: `if (currentVersion < 27)` → `CustomizableUIInternal.getSavedVerticalSnapshotState()`
- 条件付き依存: `if (verticalSnapshot.length)` → `placeBeforeSwitcher()`
- 条件付き依存: `if (verticalSnapshot.length)` → `CustomizableUIInternal.saveNavBarWhenVerticalTabsState()`
- 条件付き依存: `if (currentVersion < 28)` → `restoreFlexibleSpace()`
- 条件付き依存: `if (currentVersion < 28)` → `CustomizableUIInternal.getSavedHorizontalSnapshotState()`
- 条件付き依存: `if (horizontalSnapshot.length)` → `restoreFlexibleSpace()`
- 参照: `AppConstants.MOZ_DEV_EDITION`, `CustomizableUI.AREA_ADDONS`, `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.verticalTabsEnabled`, `gSavedState.currentVersion`, `gSavedState.placements`, `horizontalSnapshot.length`, `navbarPlacements.length`, `placements.length`, `savedPanelPlacements.length`, `verticalSnapshot.length`, `widget._introducedByPref`, `widget._introducedInVersion`, `widget.defaultArea`, `widget.id`
- XPCOM: `Services.prefs`

## insertBeforeAllTabs()
- 位置: L908-920
- 役割: 配置リストの alltabs-button の直前に柔軟スペースを補う。版 26 の移行で使う。
- 触るとき: タブストリップ末尾のスペースが消えた、または余分に入った問題を調べるとき。
- 呼び出し先: `placements.indexOf()`, `placements[alltabsIndex - 1].startsWith()`
- 条件付き依存: `if ( alltabsIndex > 0 && !placements[alltabsIndex - 1].startsWith(kSpecialWidgetPfx + "spring") )` → `placements.splice()`

## areaPlacements()
- 位置: L940-943
- 役割: 保存状態から指定エリアの配置配列を取り出す。配列でなければ空配列を返す。
- 触るとき: 版 27 の移行で保存配置を読むときに、破損した保存状態で落ちないか確かめるとき。
- 呼び出し先: `Array.isArray()`
- 参照: `gSavedState.placements`

## placeBeforeSwitcher()
- 位置: L947-963
- 役割: 整理タブボタンを ai-window-toggle の直前へ移す。新規作成の扱いで未配置なら、reserveSlot が真のとき枠を確保する。
- 触るとき: 整理タブボタンの位置が切替ボタンの近くにならないとき、または未作成の扱いを変えるとき。
- 呼び出し先: `placements.indexOf()`
- 条件付き依存: `if (buttonIndex == appendedIndex)` → `placements.splice()`
- 条件付き依存: `if (buttonIndex == -1 && reserveSlot)` → `placements.splice()`

## restoreFlexibleSpace()
- 位置: L1010-1033
- 役割: alltabs-button を持たない配置に、タブの後ろの柔軟スペースを末尾へ補う。ユーザーが意図して消した場合は触らない。
- 触るとき: alltabs-button を外したプロファイルでタブ列と窓の操作ボタンの間が詰まる問題を調べるとき。
- 呼び出し先: `Array.isArray()`, `CustomizableUIInternal.matchingSpecials()`, `afterTabs.some()`, `placements.includes()`, `placements.indexOf()`, `placements.slice()`
- 条件付き依存: `if ( !afterTabs.some(id => CustomizableUIInternal.matchingSpecials(id, "spring") ) )` → `placements.push()`
- 参照: `placements.length`

## updateForNewProtonVersion()
- 位置: L1056-1108
- 役割: Proton 移行用の toolbar.version に従い、home・library・sidebar ボタンのうち未使用のものを navbar から外す。
- 触るとき: Proton 由来の既定ボタン削除が未使用ボタンに効いているか確かめるとき。
- 呼び出し先: `Services.prefs.getIntPref()`, `Services.prefs.setIntPref()`
- 条件付き依存: `if (!placements)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (currentVersion < 1)` → `lazy.HomePage.get()`
- 条件付き依存: `if (currentVersion < 1)` → `placements.includes()`
- 条件付き依存: `if (currentVersion < 1)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (currentVersion < 1)` → `Services.policies.isAllowed()`
- 条件付き依存: `if ( placements.includes("home-button") && !Services.prefs.getBoolPref(kPrefHomeButtonUsed) && (homePage == "about:home" || homePage == "about:blank") && Service...)` → `placements.splice()`
- 条件付き依存: `if ( placements.includes("home-button") && !Services.prefs.getBoolPref(kPrefHomeButtonUsed) && (homePage == "about:home" || homePage == "about:blank") && Service...)` → `placements.indexOf()`
- 条件付き依存: `if (currentVersion < 2)` → `placements.includes()`
- 条件付き依存: `if (currentVersion < 2)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( placements.includes("library-button") && !Services.prefs.getBoolPref(kPrefLibraryButtonUsed) )` → `placements.splice()`
- 条件付き依存: `if ( placements.includes("library-button") && !Services.prefs.getBoolPref(kPrefLibraryButtonUsed) )` → `placements.indexOf()`
- 条件付き依存: `if (currentVersion < 3)` → `placements.includes()`
- 条件付き依存: `if (currentVersion < 3)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if ( placements.includes("sidebar-button") && !Services.prefs.getBoolPref(kPrefSidebarButtonUsed) )` → `placements.splice()`
- 条件付き依存: `if ( placements.includes("sidebar-button") && !Services.prefs.getBoolPref(kPrefSidebarButtonUsed) )` → `placements.indexOf()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `gSavedState?.placements`
- XPCOM: `Services.policies` / `Services.prefs`

## markObsoleteBuiltinButtonsSeen()
- 位置: L1115-1131
- 役割: アップグレード時に、今回の版で廃止されたボタンを既見扱いにして dirty を立てる。
- 触るとき: 廃止ボタンが再び現れる、または状態が保存されない問題を調べるとき。
- 条件付き依存: `if (version == kVersion)` → `gSeenWidgets.add()`
- 参照: `gSavedState.currentVersion`

## placeNewDefaultWidgetsInArea()
- 位置: L1141-1213
- 役割: 新しく追加された組み込み既定ウィジェットを、既定配置の直前のウィジェットの後ろへ保存済み配置に挿入する。
- 触るとき: 新しい既定ボタンを既存プロファイルのツールバーのどこに入れるかを変えるとき、または新規ボタンが末尾に追加されてしまう原因を調べるとき。
- 呼び出し先: `defaultPlacements.indexOf()`, `gAreas.get()`, `gAreas.get(aArea).has()`, `gFuturePlacements.get()`, `gPalette.get()`, `savedPlacements.includes()`, `this.saveState()`
- 条件付き依存: `if ( CustomizableUI.verticalTabsEnabled && gAreas.get(aArea).has("verticalTabsDefaultPlacements") )` → `gAreas .get(aArea) .get()`
- 条件付き依存: `if ( CustomizableUI.verticalTabsEnabled && gAreas.get(aArea).has("verticalTabsDefaultPlacements") )` → `gAreas .get()`
- 条件付き依存: `if (!( CustomizableUI.verticalTabsEnabled && gAreas.get(aArea).has("verticalTabsDefaultPlacements") ))` → `gAreas.get(aArea).get()`
- 条件付き依存: `if (!( CustomizableUI.verticalTabsEnabled && gAreas.get(aArea).has("verticalTabsDefaultPlacements") ))` → `gAreas.get()`
- 条件付き依存: `if (i === 0 && i === defaultWidgetIndex)` → `savedPlacements.splice()`
- 条件付き依存: `if (i === 0 && i === defaultWidgetIndex)` → `futurePlacedWidgets.delete()`
- 条件付き依存: `if (i)` → `savedPlacements.indexOf()`
- 条件付き依存: `if (previousWidgetIndex != -1)` → `savedPlacements.splice()`
- 条件付き依存: `if (previousWidgetIndex != -1)` → `futurePlacedWidgets.delete()`
- 参照: `CustomizableUI.SOURCE_BUILTIN`, `CustomizableUI.verticalTabsEnabled`, `defaultPlacements.length`, `gSavedState.placements`, `savedPlacements.length`, `widget._introducedByPref`, `widget._introducedInVersion`, `widget.defaultArea`, `widget.id`, `widget.source`

## getCustomizationTarget()
- 位置: L1220-1241
- 役割: エリアノードの customizationtarget 属性から実際に子を置く要素を求め、結果をノードにキャッシュする。
- 触るとき: ツールバーの子要素をどのノードに入れるかを変えるとき、または customizationtarget が見つからない問題を調べるとき。
- 呼び出し先: `aElement.hasAttribute()`
- 条件付き依存: `if ( !aElement._customizationTarget && aElement.hasAttribute("customizable") )` → `aElement.getAttribute()`
- 条件付き依存: `if (id)` → `aElement.ownerDocument.getElementById()`
- 参照: `aElement._customizationTarget`

## wrapWidget()
- 位置: L1259-1284
- 役割: ウィジェット ID から API 提供なら WidgetGroupWrapper、XUL 提供なら XULWidgetGroupWrapper を作って返し、キャッシュする。
- 触るとき: 拡張機能や内部から CustomizableUI のラッパー経由でウィジェットを操作するときの挙動を変えるとき。
- 呼び出し先: `gGroupWrapperCache.has()`, `gGroupWrapperCache.set()`, `this.getWidgetProvider()`
- 条件付き依存: `if (gGroupWrapperCache.has(aWidgetId))` → `gGroupWrapperCache.get()`
- 条件付き依存: `if (provider == CustomizableUI.PROVIDER_API)` → `gPalette.get()`
- 条件付き依存: `if (!widget.wrapper)` → `gGroupWrapperCache.set()`
- 参照: `CustomizableUI.PROVIDER_API`, `widget.wrapper`

## registerArea()
- 位置: L1292-1374
- 役割: エリアの ID と属性を検証して gAreas に登録する。新規エリアなら新しい既定ウィジェットを配置し、保存状態や保留中のノードを反映する。
- 触るとき: 新しいツールバーやパネルのエリアを追加するとき、または type や defaultCollapsed の制約に引っかかるとき。
- 呼び出し先: `/^[a-z0-9-_]{1,}$/i.test()`, `Array.isArray()`, `allTypes.includes()`, `gAreas.get()`, `gAreas.has()`, `kImmutableProperties.has()`, `props.get()`, `props.has()`, `props.set()`
- 条件付き依存: `if (!props.has("type"))` → `props.set()`
- 条件付き依存: `if (props.get("type") == CustomizableUI.TYPE_TOOLBAR)` → `props.has()`
- 条件付き依存: `if (!props.has("defaultCollapsed"))` → `props.set()`
- 条件付き依存: `if (!(props.get("type") == CustomizableUI.TYPE_TOOLBAR))` → `props.has()`
- 条件付き依存: `if (!allTypes.includes(props.get("type")))` → `props.get()`
- 条件付き依存: `if (!props.has("defaultPlacements"))` → `props.set()`
- 条件付き依存: `if (!areaIsKnown)` → `gAreas.set()`
- 条件付き依存: `if (!areaIsKnown)` → `this.placeNewDefaultWidgetsInArea()`
- 条件付き依存: `if (!areaIsKnown)` → `props.get()`
- 条件付き依存: `if (!areaIsKnown)` → `gPlacements.has()`
- 条件付き依存: `if ( props.get("type") == CustomizableUI.TYPE_TOOLBAR && !gPlacements.has(aName) )` → `lazy.log.debug()`
- 条件付き依存: `if ( props.get("type") == CustomizableUI.TYPE_TOOLBAR && !gPlacements.has(aName) )` → `gFuturePlacements.has()`
- 条件付き依存: `if (!gFuturePlacements.has(aName))` → `gFuturePlacements.set()`
- 条件付き依存: `if (!( props.get("type") == CustomizableUI.TYPE_TOOLBAR && !gPlacements.has(aName) ))` → `this.restoreStateForArea()`
- 条件付き依存: `if (!areaIsKnown)` → `gPendingBuildAreas.has()`
- 条件付き依存: `if (gPendingBuildAreas.has(aName))` → `gPendingBuildAreas.get()`
- 条件付き依存: `if (gPendingBuildAreas.has(aName))` → `this.registerToolbarNode()`
- 条件付き依存: `if (gPendingBuildAreas.has(aName))` → `gPendingBuildAreas.delete()`
- 参照: `CustomizableUI.TYPE_PANEL`, `CustomizableUI.TYPE_TOOLBAR`, `aProperties.defaultCollapsed`

## unregisterArea()
- 位置: L1381-1425
- 役割: エリア内のウィジェットを全部外してから、gAreas や gFuturePlacements などの痕跡を消し、ノードの登録解除を通知する。
- 触るとき: アドオンなどが動的に作ったエリアを外すときや、エリア削除後にウィジェットが残る問題を調べるとき。
- 呼び出し先: `/^[a-z0-9-_]{1,}$/i.test()`, `gAreas.delete()`, `gAreas.has()`, `gBuildAreas.delete()`, `gBuildAreas.get()`, `gFuturePlacements.delete()`, `gPlacements.get()`, `gPlacements.has()`, `this.beginBatchUpdate()`, `this.endBatchUpdate()`
- 条件付き依存: `if (placements)` → `placements.forEach()`
- 条件付き依存: `if (aDestroyPlacements)` → `gPlacements.delete()`
- 条件付き依存: `if (!(aDestroyPlacements))` → `gPlacements.set()`
- 条件付き依存: `if (existingAreaNodes)` → `this.notifyListeners()`
- 条件付き依存: `if (existingAreaNodes)` → `this.getCustomizationTarget()`
- 参照: `CustomizableUI.REASON_AREA_UNREGISTERED`, `this.removeWidgetFromArea`

## registerToolbarNode()
- 位置: L1431-1509
- 役割: ツールバー要素をエリアに紐づける。未登録なら保留リストへ入れ、配置が既定と違えば dirty とし、必要なら buildArea で子を組み立てる。
- 触るとき: ツールバーの DOM 生成と配置データの同期を変えるとき、またはツールバーの子が保存配置と食い違う問題を調べるとき。
- 呼び出し先: `areaProperties.get()`, `gAreas.get()`, `gBuildAreas.get()`, `gBuildAreas.get(area).has()`, `gBuildAreas.has()`, `gDirtyAreaCache.has()`, `gPalette.has()`, `gPlacements.get()`, `lazy.log.debug()`, `placements.every()`, `placements.some()`, `this.beginBatchUpdate()`, `this.builtinToolbars.has()`, `this.endBatchUpdate()`, `this.getCustomizationTarget()`, `this.notifyListeners()`, `this.registerBuildArea()`
- 条件付き依存: `if (!areaProperties)` → `gPendingBuildAreas.has()`
- 条件付き依存: `if (!gPendingBuildAreas.has(area))` → `gPendingBuildAreas.set()`
- 条件付き依存: `if (!areaProperties)` → `gPendingBuildAreas.get(area).push()`
- 条件付き依存: `if (!areaProperties)` → `gPendingBuildAreas.get()`
- 条件付き依存: `if ( !placements && areaProperties.get("type") == CustomizableUI.TYPE_TOOLBAR )` → `this.restoreStateForArea()`
- 条件付き依存: `if ( !placements && areaProperties.get("type") == CustomizableUI.TYPE_TOOLBAR )` → `gPlacements.get()`
- 条件付き依存: `if ( !this.builtinToolbars.has(area) || placements.length != defaultPlacements.length || !placements.every((id, i) => id == defaultPlacements[i]) )` → `gDirtyAreaCache.add()`
- 条件付き依存: `if ( gDirtyAreaCache.has(area) || placements.some(id => gPalette.has(id)) )` → `this.buildArea()`
- 条件付き依存: `if (!( gDirtyAreaCache.has(area) || placements.some(id => gPalette.has(id)) ))` → `placements.filter()`
- 条件付き依存: `if (!( gDirtyAreaCache.has(area) || placements.some(id => gPalette.has(id)) ))` → `this.isSpecialWidget()`
- 条件付き依存: `if (specials.length)` → `this.updateSpecialsForBuiltinToolbar()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `aToolbar.id`, `aToolbar.overflowable`, `defaultPlacements.length`, `placements.length`, `specials.length`, `this.tabstripAreasReady`

## updateSpecialsForBuiltinToolbar()
- 位置: L1522-1536
- 役割: 既定状態の組み込みツールバーで、spring などの特殊ノードに保存済みの ID を順に割り当てる。
- 触るとき: スペーサーやスプリングの ID が保存状態とずれる問題を調べるとき。
- 呼び出し先: `kid.getAttribute()`, `this.getCustomizationTarget()`, `this.matchingSpecials()`
- 条件付き依存: `if ( this.matchingSpecials(aSpecialIDs[0], kid) && kid.getAttribute("skipintoolbarset") != "true" )` → `aSpecialIDs.shift()`
- 参照: `aSpecialIDs.length`, `kid.id`

## buildArea()
- 位置: L1554-1717
- 役割: 保存配置に従ってエリアの子要素を並べ替え、不要な子を削除またはパレットへ移す。ウィジェットの追加や除去の DOM 反映を担う。
- 触るとき: 保存配置どおりにツールバーの見た目を組み直すとき、またはウィジェットが消えたり順番が違ったりするとき。
- 呼び出し先: `CustomizableUI.isSpecialWidget()`, `currentNode.getAttribute()`, `gAreas.get()`, `gAreas.get(aAreaId).get()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.beginBatchUpdate()`, `this.endBatchUpdate()`, `this.ensureButtonContextMenu()`, `this.getCustomizationTarget()`, `this.getWidgetNode()`, `this.insertWidgetBefore()`, `this.isSpecialWidget()`, `this.matchingSpecials()`
- 条件付き依存: `if (this.isSpecialWidget(id) && areaIsPanel)` → `placementsToRemove.add()`
- 条件付き依存: `if (!node)` → `lazy.log.debug()`
- 条件付き依存: `if (provider == CustomizableUI.PROVIDER_API)` → `gPalette.get()`
- 条件付き依存: `if (!widget.removable && aAreaId != widget.defaultArea)` → `placementsToRemove.add()`
- 条件付き依存: `if (!(provider == CustomizableUI.PROVIDER_API))` → `this.isWidgetRemovable()`
- 条件付き依存: `if (!(provider == CustomizableUI.PROVIDER_API))` → `aAreaNode.overflowable?.isInOverflowList()`
- 条件付き依存: `if ( provider == CustomizableUI.PROVIDER_XUL && !this.isWidgetRemovable(node) && node.parentNode != container && !aAreaNode.overflowable?.isInOverflowList(node) )` → `placementsToRemove.add()`
- 条件付き依存: `if (gResetting)` → `this.notifyListeners()`
- 条件付き依存: `if (gUndoResetting)` → `this.notifyListeners()`
- 条件付き依存: `if (currentNode)` → `this.isSpecialWidget()`
- 条件付き依存: `if (currentNode)` → `node.getAttribute()`
- 条件付き依存: `if ( (node.id || this.isSpecialWidget(node)) && node.getAttribute("skipintoolbarset") != "true" )` → `this.isWidgetRemovable()`
- 条件付き依存: `if (node.id && (gResetting || gUndoResetting))` → `gPalette.get()`
- 条件付き依存: `if (this.isWidgetRemovable(node))` → `this.notifyDOMChange()`
- 条件付き依存: `if (this.isWidgetRemovable(node))` → `this.isSpecialWidget()`
- 条件付き依存: `if (palette && !this.isSpecialWidget(node.id))` → `palette.appendChild()`
- 条件付き依存: `if (palette && !this.isSpecialWidget(node.id))` → `this.removeLocationAttributes()`
- 条件付き依存: `if (!(palette && !this.isSpecialWidget(node.id)))` → `container.removeChild()`
- 条件付き依存: `if (!(this.isWidgetRemovable(node)))` → `node.setAttribute()`
- 条件付き依存: `if (!(this.isWidgetRemovable(node)))` → `lazy.log.debug()`
- 条件付き依存: `if (!(this.isWidgetRemovable(node)))` → `gPlacements.get(aAreaId).push()`
- 条件付き依存: `if (!(this.isWidgetRemovable(node)))` → `gPlacements.get()`
- 条件付き依存: `if (placementsToRemove.size)` → `gPlacements.get()`
- 条件付き依存: `if (placementsToRemove.size)` → `placementAry.indexOf()`
- 条件付き依存: `if (placementsToRemove.size)` → `placementAry.splice()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.PROVIDER_API`, `CustomizableUI.PROVIDER_XUL`, `CustomizableUI.TYPE_PANEL`, `aAreaNode.collapsed`, `aAreaNode.ownerDocument`, `container.firstElementChild`, `container.lastElementChild`, `currentNode.id`, `currentNode.nextElementSibling`, `currentNode.previousElementSibling`, `document.defaultView`, `node.id`, `node.parentNode`, `node.previousElementSibling`, `placementsToRemove.size`, `widget.currentArea`, `widget.defaultArea`, `widget.removable`, `widget.showInPrivateBrowsing`, `widget?.hideInNonPrivateBrowsing`, `window.gNavToolbox`, `window.gNavToolbox.palette`

## addPanelCloseListeners()
- 位置: L1723-1731
- 役割: パネルに click と keypress の監視を付け、そのウィンドウのパネル集合に登録する。
- 触るとき: パネルの外側クリックや Esc でパネルを閉じる挙動を変えるとき。
- 呼び出し先: `aPanel.addEventListener()`, `gPanelsForWindow.get()`, `gPanelsForWindow.get(win).add()`, `gPanelsForWindow.has()`, `this._getPanelForNode()`
- 条件付き依存: `if (!gPanelsForWindow.has(win))` → `gPanelsForWindow.set()`
- 参照: `aPanel.documentGlobal`

## removePanelCloseListeners()
- 位置: L1737-1745
- 役割: addPanelCloseListeners で付けた click と keypress の監視を外し、ウィンドウのパネル集合からも取り除く。
- 触るとき: パネルを破棄したあとに閉じ処理が残る問題を調べるとき。
- 呼び出し先: `aPanel.removeEventListener()`, `gPanelsForWindow.get()`
- 条件付き依存: `if (panels)` → `panels.delete()`
- 条件付き依存: `if (panels)` → `this._getPanelForNode()`
- 参照: `aPanel.documentGlobal`

## ensureButtonContextMenu()
- 位置: L1762-1790
- 役割: ボタンの配置先に応じて customizationPanelItemContextMenu を付けるか外す。拡張機能ウィジェットは addons エリアやオーバーフロー時に例外扱いする。
- 触るとき: ボタンの右クリックメニューが配置場所によって誤って出る、または出ない問題を調べるとき。
- 呼び出し先: `CustomizableUI.isWebExtensionWidget()`, `aNode.getAttribute()`
- 条件付き依存: `if (!( CustomizableUI.isWebExtensionWidget(aNode.id) && (aAreaNode?.id == CustomizableUI.AREA_ADDONS || aNode.getAttribute("overflowedItem") == "true") ))` → `CustomizableUI.getPlaceForItem()`
- 条件付き依存: `if (contextMenuForPlace && !currentContextMenu)` → `aNode.setAttribute()`
- 条件付き依存: `if ( currentContextMenu == kPanelItemContextMenu && contextMenuForPlace != kPanelItemContextMenu )` → `aNode.removeAttribute()`
- 参照: `CustomizableUI.AREA_ADDONS`, `aAreaNode?.id`, `aNode.id`

## getWidgetProvider()
- 位置: L1801-1819
- 役割: ウィジェット ID から提供元を判定する。特殊ノードなら SPECIAL、API 登録済みなら API、破棄済みなら null、それ以外は XUL とみなす。
- 触るとき: ウィジェットがどの提供元に属するかで処理を分けるとき、または破棄済みウィジェットの扱いを調べるとき。
- 呼び出し先: `gPalette.has()`, `gSeenWidgets.has()`, `this.isSpecialWidget()`
- 参照: `CustomizableUI.PROVIDER_API`, `CustomizableUI.PROVIDER_SPECIAL`, `CustomizableUI.PROVIDER_XUL`

## getWidgetNode()
- 位置: L1842-1879
- 役割: ウィンドウ内でウィジェットのノードを探す。特殊ウィジェットは生成し、API ウィジェットは既存インスタンスを再利用するか新規に作り、それ以外は XUL のツールボックスから探す。
- 触るとき: ウィジェットのノードをどう取得・再利用するかを変えるとき、またはノードが見つからないときの経路を調べるとき。
- 呼び出し先: `gPalette.get()`, `lazy.log.debug()`, `this.findXULWidgetInWindow()`, `this.isSpecialWidget()`
- 条件付き依存: `if (this.isSpecialWidget(aWidgetId))` → `document.getElementById()`
- 条件付き依存: `if (this.isSpecialWidget(aWidgetId))` → `this.createSpecialWidget()`
- 条件付き依存: `if (widget)` → `widget.instances.has()`
- 条件付き依存: `if (widget.instances.has(document))` → `lazy.log.debug()`
- 条件付き依存: `if (widget.instances.has(document))` → `widget.instances.get()`
- 条件付き依存: `if (widget)` → `this.buildWidgetNode()`
- 参照: `CustomizableUI.PROVIDER_API`, `CustomizableUI.PROVIDER_SPECIAL`, `CustomizableUI.PROVIDER_XUL`, `aWindow.document`

## registerPanelNode()
- 位置: L1886-1909
- 役割: パネルのノードをエリアの構築対象として登録し、閉じ監視と配置の反映、子のコンテキストメニュー設定を行う。
- 触るとき: パネル系エリア(メニューやオーバーフロー)の組み立てを変えるとき、またはパネルの子が配置と合わない問題を調べるとき。
- 呼び出し先: `gBuildAreas.get()`, `gBuildAreas.get(aAreaId).has()`, `gBuildAreas.has()`, `gPlacements.get()`, `this._getPanelForNode()`, `this.addPanelCloseListeners()`, `this.buildArea()`, `this.ensureButtonContextMenu()`, `this.notifyListeners()`, `this.registerBuildArea()`
- 条件付き依存: `if (child.localName == "toolbaritem")` → `this.ensureButtonContextMenu()`
- 参照: `aNode._customizationTarget`, `aNode.children`, `child.localName`

## onWidgetAdded()
- 位置: L1914-1920
- 役割: ウィジェットがエリアに追加されたとき、そのエリアの各ウィンドウへ insertNode で反映し、前回の UI 状態を消す。
- 触るとき: ウィジェット追加時の DOM 反映を変えるとき、またはリセット中以外の状態クリアの影響を調べるとき。
- 呼び出し先: `this.insertNode()`
- 条件付き依存: `if (!gResetting)` → `this._clearPreviousUIState()`

## onWidgetRemoved()
- 位置: L1925-1990
- 役割: ウィジェットがエリアから外れたとき、各ウィンドウのノードをパレットへ戻すか削除する。プライベートブラウジングの表示条件も見る。
- 触るとき: ウィジェットを外したときに DOM がどこへ移るかを変えるとき、またはプライベートウィンドウだけ残る不具合を調べるとき。
- 呼び出し先: `area.get()`, `container.contains()`, `gAreas.get()`, `gBuildAreas.get()`, `gPalette.get()`, `gPalette.has()`, `gSingleWrapperCache.get()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.ensureButtonContextMenu()`, `this.getCustomizationTarget()`, `this.isSpecialWidget()`, `this.notifyDOMChange()`, `this.removeLocationAttributes()`, `window.document.getElementById()`
- 条件付き依存: `if (widgetNode && isOverflowable)` → `areaNode.overflowable.getContainerFor()`
- 条件付き依存: `if (!widgetNode || !container.contains(widgetNode))` → `lazy.log.info()`
- 条件付き依存: `if (gPalette.has(aWidgetId) || this.isSpecialWidget(aWidgetId))` → `container.removeChild()`
- 条件付き依存: `if (!(gPalette.has(aWidgetId) || this.isSpecialWidget(aWidgetId)))` → `window.gNavToolbox.palette.appendChild()`
- 条件付き依存: `if (windowCache)` → `windowCache.delete()`
- 条件付き依存: `if (!gResetting)` → `this._clearPreviousUIState()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `areaNode.documentGlobal`, `gPalette.get(aWidgetId).showInPrivateBrowsing`, `gPalette.get(aWidgetId)?.hideInNonPrivateBrowsing`

## onWidgetMoved()
- 位置: L1995-2000
- 役割: ウィジェットが同じエリア内で移動したとき、insertNode で新しい位置へ反映し、リセット中以外は前回の UI 状態を消す。
- 触るとき: ツールバー内での並べ替えが DOM に反映されない問題を調べるとき。
- 呼び出し先: `this.insertNode()`
- 条件付き依存: `if (!gResetting)` → `this._clearPreviousUIState()`

## onCustomizeEnd()
- 位置: L2005-2007
- 役割: カスタマイズモードが終わったとき、前回の UI 状態(_clearPreviousUIState)を消す。
- 触るとき: カスタマイズ終了後に状態が残る、または消えすぎる問題を調べるとき。
- 呼び出し先: `this._clearPreviousUIState()`

## registerBuildArea()
- 位置: L2018-2041
- 役割: ウィンドウのエリアノードを gBuildAreas に登録し、ウィンドウを登録し、ツールボックスも記録して customization-target クラスを付ける。
- 触るとき: ビルド対象のツールバーノードを増やす、または閉じたウィンドウの参照が残る問題を調べるとき。
- 呼び出し先: `customizableNode.classList.add()`, `gBuildAreas.get()`, `gBuildAreas.get(aAreaId).add()`, `gBuildAreas.has()`, `this.getCustomizeTargetForArea()`, `this.registerBuildWindow()`
- 条件付き依存: `if (window.gNavToolbox)` → `gBuildWindows.get(window).add()`
- 条件付き依存: `if (window.gNavToolbox)` → `gBuildWindows.get()`
- 条件付き依存: `if (!gBuildAreas.has(aAreaId))` → `gBuildAreas.set()`
- 参照: `aAreaNode.documentGlobal`, `window.closed`, `window.gNavToolbox`

## registerBuildWindow()
- 位置: L2052-2061
- 役割: ウィンドウを初めて登録するとき、unload と command の監視を付けて onWindowOpened を通知する。登録済みなら何もしない。
- 触るとき: ウィンドウごとのイベント監視の付け方や、ウィンドウ開閉の通知順を変えるとき。
- 呼び出し先: `gBuildWindows.has()`
- 条件付き依存: `if (!gBuildWindows.has(aWindow))` → `gBuildWindows.set()`
- 条件付き依存: `if (!gBuildWindows.has(aWindow))` → `aWindow.addEventListener()`
- 条件付き依存: `if (!gBuildWindows.has(aWindow))` → `this.notifyListeners()`

## unregisterBuildWindow()
- 位置: L2073-2114
- 役割: 閉じるウィンドウの監視と各種キャッシュを外し、そのウィンドウのエリアノード、ウィジェットインスタンス、保留ノードを消して通知する。
- 触るとき: ウィンドウを閉じたあとにリスナーやノードが残るメモリリークや不具合を調べるとき。
- 呼び出し先: `aWindow.removeEventListener()`, `gAreas.get()`, `gBuildWindows.delete()`, `gPanelsForWindow.delete()`, `gSingleWrapperCache.delete()`, `this.notifyListeners()`, `widget.instances.delete()`
- 条件付き依存: `if (node.ownerDocument == document)` → `this.notifyListeners()`
- 条件付き依存: `if (node.ownerDocument == document)` → `this.getCustomizationTarget()`
- 条件付き依存: `if (node.ownerDocument == document)` → `areaProperties.get()`
- 条件付き依存: `if (areaProperties.get("overflowable"))` → `node.overflowable.uninit()`
- 条件付き依存: `if (node.ownerDocument == document)` → `areaNodes.delete()`
- 条件付き依存: `if (pendingNodes[i].ownerDocument == document)` → `pendingNodes.splice()`
- 参照: `CustomizableUI.REASON_WINDOW_CLOSED`, `aWindow.document`, `node.overflowable`, `node.ownerDocument`, `pendingNodes.length`, `pendingNodes[i].ownerDocument`, `widget.id`

## handleNewBrowserWindow()
- 位置: L2120-2184
- 役割: 新しいブラウザウィンドウで palette を設定し、縦タブ時はタブコンテナを一時的に除外してから全ツールバーを登録する。縦タブ表示の調整も行う。
- 触るとき: 新規ウィンドウ作成時にツールバーの初期表示が崩れる、または縦タブ切替直後に表示がずれる問題を調べるとき。
- 呼び出し先: `CustomizableUI.getAreaType()`, `Services.prefs.getBoolPref()`, `document.getElementById()`
- 条件付き依存: `if (isVerticalTabs)` → `elem.setAttribute()`
- 条件付き依存: `if (type == CustomizableUI.TYPE_TOOLBAR)` → `document.getElementById()`
- 条件付き依存: `if (type == CustomizableUI.TYPE_TOOLBAR)` → `this.registerToolbarNode()`
- 条件付き依存: `if (isVerticalTabs)` → `aWindow.setToolbarVisibility()`
- 条件付き依存: `if (isVerticalTabs)` → `document.getElementById()`
- 条件付き依存: `if (isVerticalTabs)` → `aWindow.TabBarVisibility.update()`
- 条件付き依存: `if (tabstripToolbar.collapsed !== wasCollapsed)` → `tabstripToolbar.dispatchEvent()`
- 条件付き依存: `if (isVerticalTabs)` → `elem.removeAttribute()`
- 参照: `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.AREA_VERTICAL_TABSTRIP`, `CustomizableUI.TYPE_TOOLBAR`, `CustomizableUI.areas`, `document.getElementById( "BrowserToolbarPalette" ).content`, `gBrowser.tabContainer`, `gNavToolbox.palette`, `tabstripToolbar.collapsed`
- XPCOM: `Services.prefs`

## setLocationAttributes()
- 位置: L2196-2214
- 役割: ウィジェットノードに cui-areatype と cui-anchorid を設定する。anchor が無ければ後者を消す。
- 触るとき: ウィジェットの配置先に応じた CSS やパネル位置合わせの属性を変えるとき。
- 呼び出し先: `aNode.setAttribute()`, `gAreas.get()`, `props.get()`
- 条件付き依存: `if (anchor)` → `aNode.setAttribute()`
- 条件付き依存: `if (!(anchor))` → `aNode.removeAttribute()`

## removeLocationAttributes()
- 位置: L2223-2226
- 役割: ウィジェットノードから cui-areatype と cui-anchorid を取り除く。
- 触るとき: パレットへ戻したウィジェットに古い位置属性が残る問題を調べるとき。
- 呼び出し先: `aNode.removeAttribute()`

## insertNode()
- 位置: L2242-2263
- 役割: エリアに紐づく全ウィンドウのノードに対して insertNodeInWindow を呼ぶ。配置データが無ければエラーを記録して何もしない。
- 触るとき: ウィジェット追加や移動を全ウィンドウへ反映させる経路を調べるとき。
- 呼び出し先: `gBuildAreas.get()`, `gPlacements.get()`, `this.insertNodeInWindow()`
- 条件付き依存: `if (!placements)` → `lazy.log.error()`

## insertNodeInWindow()
- 位置: L2278-2316
- 役割: ウィンドウのウィジェットノードを、プライベート表示の条件を確かめたうえで findInsertionPoints の位置へ挿入する。
- 触るとき: ウィンドウごとに挿入位置がずれる問題や、プライベートウィンドウで出るべき要素が出ない問題を調べるとき。
- 呼び出し先: `gPalette.get()`, `gPalette.has()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `this.findInsertionPoints()`, `this.getWidgetNode()`, `this.insertWidgetBefore()`
- 条件付き依存: `if (!widgetNode)` → `lazy.log.error()`
- 条件付き依存: `if (isNew)` → `this.ensureButtonContextMenu()`
- 参照: `aAreaNode.documentGlobal`, `aAreaNode.id`, `gPalette.get(aWidgetId).showInPrivateBrowsing`, `gPalette.get(aWidgetId)?.hideInNonPrivateBrowsing`

## findInsertionPoints()
- 位置: L2340-2378
- 役割: 保存配置で後ろに続くウィジェットを探し、その直前を挿入位置とする。オーバーフロー可能なツールバーは overflowable に任せる。
- 触るとき: ツールバーのどこに新しいボタンを差し込むかを変えるとき、またはオーバーフロー時の挿入位置を調べるとき。
- 呼び出し先: `aAreaNode.ownerDocument.getElementById()`, `gAreas.get()`, `gPlacements.get()`, `placements.indexOf()`, `props.get()`, `this.getCustomizationTarget()`
- 条件付き依存: `if ( props.get("type") == CustomizableUI.TYPE_TOOLBAR && props.get("overflowable") )` → `aAreaNode.overflowable.findOverflowedInsertionPoints()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `aAreaNode.id`, `aNode.id`, `nextNode.parentNode`, `nextNode.parentNode.localName`, `nextNode.parentNode.parentNode`, `placements.length`

## insertWidgetBefore()
- 位置: L2394-2399
- 役割: notifyDOMChange で前後のイベントを挟みながら、位置属性を付けて指定位置へ挿入する。
- 触るとき: ボタンの DOM 挿入時に通知や属性設定の順序を変えるとき。
- 呼び出し先: `aContainer.insertBefore()`, `this.notifyDOMChange()`, `this.setLocationAttributes()`

## notifyDOMChange()
- 位置: L2419-2435
- 役割: DOM 変更の前後で onWidgetBeforeDOMChange と onWidgetAfterDOMChange のリスナーを呼ぶ。実際の変更は引数のコールバックが行う。
- 触るとき: ツールバーの DOM 変更を監視するリスナーの呼び出し順を確かめるとき。
- 呼び出し先: `aCallback()`, `this.notifyListeners()`

## handleEvent()
- 位置: L2443-2459
- 役割: command、click、keypress を受けてパネル自動非表示を判定し、unload では窓の登録を解除する。
- 触るとき: パネルの自動非表示や窓のアンロード時の後始末を変えるとき。
- 呼び出し先: `this._originalEventInPanel()`, `this.maybeAutoHidePanel()`, `this.unregisterBuildWindow()`
- 参照: `aEvent.currentTarget`, `aEvent.sourceEvent`, `aEvent.type`

## _originalEventInPanel()
- 位置: L2468-2480
- 役割: command イベントの元イベントが、追跡中のパネル内で発生したかを判定する。
- 触るとき: パネル内ボタンのコマンドで誤ってパネルが閉じる、または閉じない問題を調べるとき。
- 呼び出し先: `gPanelsForWindow.get()`, `panels.has()`, `this._getPanelForNode()`
- 参照: `aEvent.sourceEvent`, `e.target`, `e.view`

## _getSpecialIdForNode()
- 位置: L2500-2511
- 役割: ノードなら id を、無ければ toolbar 接頭辞を除いた localName を返す。文字列はそのまま返す。
- 触るとき: spring や separator などの特殊ウィジェットを ID で判定する処理を変えるとき。
- 条件付き依存: `if (typeof aStringOrNode == "object" && aStringOrNode.localName)` → `aStringOrNode.localName.startsWith()`
- 条件付き依存: `if (aStringOrNode.localName.startsWith("toolbar"))` → `aStringOrNode.localName.substring()`
- 参照: `aStringOrNode.id`, `aStringOrNode.localName`

## isSpecialWidget()
- 位置: L2522-2534
- 役割: ID かノードが特殊ウィジェット(spring、separator、spacer、customizableui-special-)かを判定する。
- 触るとき: スペーサー類を配置の対象から外すか含めるかを判断するとき。
- 呼び出し先: `aStringOrNode.startsWith()`, `this._getSpecialIdForNode()`
- 条件付き依存: `if (aStringOrNode === null)` → `lazy.log.debug()`

## matchingSpecials()
- 位置: L2548-2558
- 役割: 2 つの ID かノードが同種の特殊ウィジェット(spring、spacer、separator のどれか)かを比べる。
- 触るとき: 保存配置の spring と DOM の要素を対応付けるとき。
- 呼び出し先: `aId1.match()`, `aId2.match()`, `this._getSpecialIdForNode()`, `this.isSpecialWidget()`

## ensureSpecialWidgetId()
- 位置: L2573-2581
- 役割: 種別だけの ID に対し、連番付きの一意な customizableui-special- 形式の ID を作る。
- 触るとき: 新しく作る spring などに重複しない ID を振る仕組みを変えるとき。
- 呼び出し先: `aId.match()`

## createSpecialWidget()
- 位置: L2589-2595
- 役割: toolbar の spring、spacer、separator 要素を作り、一意な ID を付けて返す。
- 触るとき: 特殊ウィジェットの要素を作る方法や class を変えるとき。
- 呼び出し先: `aDocument.createXULElement()`, `aId.match()`, `this.ensureSpecialWidgetId()`
- 参照: `node.className`, `node.id`

## findXULWidgetInWindow()
- 位置: L2610-2682
- 役割: ウィンドウ内で XUL 提供のウィジェットを ID から探す。ツールバーにあればそれを、無ければツールボックスのパレットから探し、removable 属性を補う。
- 触るとき: XUL 側で定義されたボタンが見つからない、または removable の判定がおかしいとき。
- 呼び出し先: `document.getElementById()`, `gBuildWindows.get()`, `gBuildWindows.has()`
- 条件付き依存: `if (!aId)` → `lazy.log.error()`
- 条件付き依存: `if (node)` → `this.getCustomizationTarget()`
- 条件付き依存: `if (parent)` → `this.getCustomizationTarget()`
- 条件付き依存: `if (parent)` → `gBuildWindows.get(aWindow).has()`
- 条件付き依存: `if (parent)` → `gBuildWindows.get()`
- 条件付き依存: `if ( (this.getCustomizationTarget(parent) == nodeInArea.parentNode && gBuildWindows.get(aWindow).has(aWindow.gNavToolbox)) || aWindow.gNavToolbox.palette == node...)` → `node.hasAttribute()`
- 条件付き依存: `if (!node.hasAttribute("removable"))` → `node.setAttribute()`
- 条件付き依存: `if (!node.hasAttribute("removable"))` → `this.getCustomizationTarget()`
- 条件付き依存: `if (toolbox.palette)` → `toolbox.palette.getElementsByAttribute()`
- 条件付き依存: `if (element)` → `element.hasAttribute()`
- 条件付き依存: `if (!element.hasAttribute("removable"))` → `element.setAttribute()`
- 参照: `aWindow.document`, `aWindow.gNavToolbox`, `aWindow.gNavToolbox.palette`, `node.parentNode`, `node.parentNode.localName`, `nodeInArea.parentNode`, `parent.parentNode`, `toolbox.palette`

## buildWidgetNode()
- 位置: L2702-2891
- 役割: ウィジェット定義から toolbarbutton などの DOM を作り、ラベル、ツールチップ、ショートカット、コマンドとクリックのハンドラを付ける。プライベートブラウジングの条件に合わなければ null を返す。
- 触るとき: ボタンの見た目、属性、イベント処理の初期設定を変えるとき、またはプライベート窓でボタンが出ない問題を調べるとき。
- 呼び出し先: `aWidget.instances.set()`, `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.log.debug()`
- 条件付き依存: `if (typeof aWidget == "string")` → `gPalette.get()`
- 条件付き依存: `if (aWidget.onBuild)` → `aWidget.onBuild()`
- 条件付き依存: `if (aWidget.type == "custom")` → `aDocument.defaultView.XULElement.isInstance()`
- 条件付き依存: `if ( !node || !aDocument.defaultView.XULElement.isInstance(node) || (aWidget.viewId && !node.viewButton) )` → `lazy.log.error()`
- 条件付き依存: `if (button || aWidget.type != "custom")` → `aWidget.onBeforeCreated()`
- 条件付き依存: `if (!button)` → `aDocument.createXULElement()`
- 条件付き依存: `if (button || aWidget.type != "custom")` → `button.classList.add()`
- 条件付き依存: `if (button || aWidget.type != "custom")` → `button.setAttribute()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `button.setAttribute()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `aDocument.createXULElement()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `dropmarker.setAttribute()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `dropmarker.classList.add()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `node.classList.add()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `node.append()`
- 条件付き依存: `if (button || aWidget.type != "custom")` → `node.setAttribute()`
- 条件付き依存: `if (button || aWidget.type != "custom")` → `node.toggleAttribute()`
- 条件付き依存: `if (aWidget.tabSpecific)` → `node.setAttribute()`
- 条件付き依存: `if (aWidget.locationSpecific)` → `node.setAttribute()`
- 条件付き依存: `if (aWidget.keepBroadcastAttributesWhenCustomizing)` → `node.setAttribute()`
- 条件付き依存: `if (aWidget.shortcutId)` → `aDocument.getElementById()`
- 条件付き依存: `if (keyEl)` → `lazy.ShortcutUtils.prettifyShortcut()`
- 条件付き依存: `if (!(keyEl))` → `lazy.log.error()`
- 条件付き依存: `if (aWidget.l10nId)` → `aDocument.l10n.setAttributes()`
- 条件付き依存: `if (button != node)` → `aDocument.l10n.setAttributes()`
- 条件付き依存: `if (shortcut)` → `node.setAttribute()`
- 条件付き依存: `if (shortcut)` → `JSON.stringify()`
- 条件付き依存: `if (button != node)` → `button.setAttribute()`
- 条件付き依存: `if (button != node)` → `JSON.stringify()`
- 条件付き依存: `if (!(aWidget.l10nId))` → `node.setAttribute()`
- 条件付き依存: `if (!(aWidget.l10nId))` → `this.getLocalizedProperty()`
- 条件付き依存: `if (button != node)` → `node.getAttribute()`
- 条件付き依存: `if (tooltip)` → `node.setAttribute()`
- 条件付き依存: `if (button || aWidget.type != "custom")` → `this.handleWidgetCommand.bind()`
- 条件付き依存: `if (button || aWidget.type != "custom")` → `node.addEventListener()`
- 条件付き依存: `if (button || aWidget.type != "custom")` → `this.handleWidgetClick.bind()`
- 条件付き依存: `if (button || aWidget.type != "custom")` → `node.classList.add()`
- 条件付き依存: `if (viewbutton)` → `lazy.log.debug()`
- 条件付き依存: `if (aWidget.source == CustomizableUI.SOURCE_BUILTIN)` → `node.classList.add()`
- 条件付き依存: `if (aWidget.onCreated)` → `aWidget.onCreated()`
- 参照: `CustomizableUI.SOURCE_BUILTIN`, `aDocument.defaultView`, `aDocument.documentURI`, `aWidget.disabled`, `aWidget.hideInNonPrivateBrowsing`, `aWidget.id`, `aWidget.keepBroadcastAttributesWhenCustomizing`, `aWidget.l10nId`, `aWidget.locationSpecific`, `aWidget.onBeforeCreated`, `aWidget.onBuild`, `aWidget.onCreated`, `aWidget.overflows`, `aWidget.removable`, `aWidget.shortcutId`, `aWidget.showInPrivateBrowsing`, `aWidget.source`, `aWidget.tabSpecific`, `aWidget.type`, `aWidget.viewId`, `node.viewButton`

## ensureSubviewListeners()
- 位置: L2897-2916
- 役割: ビュー要素に、そのビューを持つウィジェットの ViewShowing と ViewHiding のハンドラを一度だけ付ける。
- 触るとき: サブビューの表示や非表示のイベントが届かない問題を調べるとき。
- 呼び出し先: `[...gPalette.values()].find()`, `gPalette.values()`, `lazy.log.debug()`
- 条件付き依存: `if (typeof widget[handler] == "function")` → `viewNode.addEventListener()`
- 参照: `viewNode._addedEventListeners`, `viewNode.id`, `w.viewId`, `widget.id`

## getLocalizedProperty()
- 位置: L2926-2969
- 役割: ウィジェットの label や tooltiptext などを、文字列 ID として解決する。解決できなければ既定値を返す。
- 触るとき: ボタンの表示文字列の取得方法を変えるとき、またはローカライズ文字列が出ない問題を調べるとき。
- 呼び出し先: `Array.isArray()`, `kReqStringProps.includes()`, `lazy.gWidgetsBundle.GetStringFromName()`
- 条件付き依存: `if (typeof aWidget == "string")` → `gPalette.get()`
- 条件付き依存: `if (Array.isArray(aFormatArgs) && aFormatArgs.length)` → `lazy.gWidgetsBundle.formatStringFromName()`
- 条件付き依存: `if (!def && (name != "" || kReqStringProps.includes(aProp)))` → `lazy.log.error()`
- 参照: `aFormatArgs.length`, `aWidget.id`, `aWidget.localized`

## addShortcut()
- 位置: L2976-3005
- 役割: key 属性か command 属性から対応するショートカットを探し、表示用の文字列を shortcut 属性に設定する。
- 触るとき: ボタンのツールチップに出るショートカット表示を変えるとき。
- 呼び出し先: `aShortcutNode.getAttribute()`, `aTargetNode.hasAttribute()`, `aTargetNode.setAttribute()`, `lazy.ShortcutUtils.prettifyShortcut()`
- 条件付き依存: `if (shortcutId)` → `document.getElementById()`
- 条件付き依存: `if (!(shortcutId))` → `aShortcutNode.getAttribute()`
- 条件付き依存: `if (commandId)` → `lazy.ShortcutUtils.findShortcut()`
- 条件付き依存: `if (commandId)` → `document.getElementById()`
- 参照: `aShortcutNode.documentGlobal`

## doWidgetCommand()
- 位置: L3017-3032
- 役割: ウィジェットの onCommand を呼ぶ。無ければ customizedui-widget-command を通知する。
- 触るとき: 組み込み外のウィジェットにコマンド処理を追加する経路を調べるとき。
- 条件付き依存: `if (aWidget.onCommand)` → `aWidget.onCommand.call()`
- 条件付き依存: `if (aWidget.onCommand)` → `lazy.log.error()`
- 条件付き依存: `if (!(aWidget.onCommand))` → `Services.obs.notifyObservers()`
- 参照: `aWidget.id`, `aWidget.onCommand`
- XPCOM: `Services.obs`

## showWidgetView()
- 位置: L3047-3074
- 役割: ビューを持つウィジェットのサブビューを開く。サブビューを許さない場合やツールバー上のときは、先に親パネルを閉じてアンカーを差し替える。
- 触るとき: パネル内のボタンからサブビューを開く際のアンカーや閉じ方を変えるとき。
- 呼び出し先: `CustomizableUI.getAreaType()`, `aNode.hasAttribute()`, `ownerWindow.PanelUI.showSubView()`, `this.getPlacementOfWidget()`
- 条件付き依存: `if ( aWidget.disallowSubView && (areaType == CustomizableUI.TYPE_PANEL || aNode.hasAttribute("overflowedItem")) )` → `this.wrapWidget(aWidget.id).forWindow()`
- 条件付き依存: `if ( aWidget.disallowSubView && (areaType == CustomizableUI.TYPE_PANEL || aNode.hasAttribute("overflowedItem")) )` → `this.wrapWidget()`
- 条件付き依存: `if (wrapper?.anchor)` → `this.hidePanelForNode()`
- 条件付き依存: `if (areaType != CustomizableUI.TYPE_PANEL)` → `this.wrapWidget(aWidget.id).forWindow()`
- 条件付き依存: `if (areaType != CustomizableUI.TYPE_PANEL)` → `this.wrapWidget()`
- 条件付き依存: `if (areaType != CustomizableUI.TYPE_PANEL)` → `aNode.closest()`
- 条件付き依存: `if (!hasMultiView && wrapper?.anchor)` → `this.hidePanelForNode()`
- 参照: `CustomizableUI.TYPE_PANEL`, `aNode.documentGlobal`, `aNode.id`, `aWidget.disallowSubView`, `aWidget.id`, `aWidget.viewId`, `this.getPlacementOfWidget(aNode.id).area`, `wrapper.anchor`, `wrapper?.anchor`

## handleWidgetCommand()
- 位置: L3087-3122
- 役割: onBeforeCommand の戻り値に従い、ボタン型はコマンドを実行、ビュー型はサブビューを開く。複合ボタンでは押した場所で振り分ける。
- 触るとき: ボタンを押したときにコマンドを実行するか、ビューを開くかの判定を変えるとき。
- 呼び出し先: `lazy.log.debug()`
- 条件付き依存: `if (aWidget.onBeforeCommand)` → `aWidget.onBeforeCommand.call()`
- 条件付き依存: `if (aWidget.onBeforeCommand)` → `lazy.log.error()`
- 条件付き依存: `if (aWidget.type == "button" || action == "command")` → `this.doWidgetCommand()`
- 条件付き依存: `if (aWidget.type == "view" || action == "view")` → `this.showWidgetView()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `this.getPlacementOfWidget()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `CustomizableUI.getAreaType()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `button.contains()`
- 条件付き依存: `if (aWidget.type == "button-and-view")` → `aNode.hasAttribute()`
- 条件付き依存: `if ( areaType == CustomizableUI.TYPE_TOOLBAR && button.contains(aEvent.target) && !aNode.hasAttribute("overflowedItem") )` → `this.doWidgetCommand()`
- 条件付き依存: `if (!( areaType == CustomizableUI.TYPE_TOOLBAR && button.contains(aEvent.target) && !aNode.hasAttribute("overflowedItem") ))` → `this.showWidgetView()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `aEvent.target`, `aNode.firstElementChild`, `aNode.id`, `aWidget.onBeforeCommand`, `aWidget.type`, `this.getPlacementOfWidget(aNode.id).area`

## handleWidgetClick()
- 位置: L3136-3152
- 役割: ウィジェットの onClick を呼ぶ。未定義なら customizedui-widget-click を通知する。
- 触るとき: ボタンのクリック処理を拡張したい、または onClick が呼ばれない問題を調べるとき。
- 呼び出し先: `lazy.log.debug()`
- 条件付き依存: `if (aWidget.onClick)` → `aWidget.onClick.call()`
- 条件付き依存: `if (aWidget.onClick)` → `console.error()`
- 条件付き依存: `if (!(aWidget.onClick))` → `Services.obs.notifyObservers()`
- 参照: `aWidget.id`, `aWidget.onClick`
- XPCOM: `Services.obs`

## _getPanelForNode()
- 位置: L3162-3164
- 役割: ノードを含む最も近い panel 要素を返す。
- 触るとき: パネル判定の基準となる要素の取り方を変えるとき。
- 呼び出し先: `aNode.closest()`

## _isOnInteractiveElement()
- 位置: L3183-3251
- 役割: クリックの元ターゲットを親方向にたどり、入力欄やメニュー、無効化された項目などパネルを閉じてはいけない要素かを判定する。
- 触るとき: パネル内の入力欄やメニューを操作してもパネルが閉じてしまう問題を調べるとき。
- 呼び出し先: `getNextTarget()`, `target.closest()`, `target.hasAttribute()`, `this._getPanelForNode()`
- 条件付き依存: `if (tagName == "toolbaritem" || tagName == "toolbarbutton")` → `target.getAttribute()`
- 参照: `aEvent.currentTarget`, `aEvent.originalTarget`, `target.DOCUMENT_FRAGMENT_NODE`, `target.DOCUMENT_NODE`, `target.containingShadowRoot`, `target.localName`, `target.nodeType`

## getNextTarget()
- 位置: L3191-3202
- 役割: _isOnInteractiveElement の内部関数。文書ならその文書を含むフレーム要素へ、要素なら shadow root を越えて親へ進む。
- 触るとき: パネル内の iframe やシャドウ DOM の中で入力欄を判定できない問題を調べるとき。
- 参照: `target.DOCUMENT_NODE`, `target.defaultView`, `target.defaultView.docShell.chromeEventHandler`, `target.nodeType`, `target.parentNode`, `target.parentNode?.host`

## hidePanelForNode()
- 位置: L3260-3265
- 役割: ノードを含むパネルを PanelMultiView.hidePopup で閉じる。
- 触るとき: ボタン操作後にパネルを閉じる経路を変えるとき。
- 呼び出し先: `this._getPanelForNode()`
- 条件付き依存: `if (panel)` → `lazy.PanelMultiView.hidePopup()`

## maybeAutoHidePanel()
- 位置: L3275-3327
- 役割: keypress は Enter、click は主ボタンだけを見る。対話要素でなければ、閉じ防止属性を持つ祖先を除き、パネルを閉じる。
- 触るとき: パネルが意図せず閉じる、または閉じるべき場面で閉じない問題を調べるとき。
- 呼び出し先: `ShadowRoot.isInstance()`, `target.getAttribute()`, `target.hasAttribute()`, `this._isOnInteractiveElement()`, `this.hidePanelForNode()`
- 参照: `aEvent.DOM_VK_RETURN`, `aEvent.button`, `aEvent.keyCode`, `aEvent.originalTarget`, `aEvent.target`, `aEvent.type`, `target.host`, `target.isConnected`, `target.localName`, `target.parentNode`

## getUnusedWidgets()
- 位置: L3334-3366
- 役割: 現在どのエリアにも無いウィジェットを集める。ウィンドウがプライベートかどうかで表示条件を見て、パレットの未配置ノードも加える。
- 触るとき: カスタマイズ画面のパレットに出るボタンの集合を変えるとき。
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.log.debug()`, `this.getPlacementOfWidget()`
- 条件付き依存: `if ( (isWindowPrivate && widget.showInPrivateBrowsing) || (!isWindowPrivate && !widget.hideInNonPrivateBrowsing) )` → `widgets.add()`
- 条件付き依存: `if (node.id && !this.getPlacementOfWidget(node.id))` → `widgets.add()`
- 参照: `aWindowPalette.children`, `aWindowPalette.documentGlobal`, `node.id`, `widget.currentArea`, `widget.hideInNonPrivateBrowsing`, `widget.showInPrivateBrowsing`

## getPlacementOfWidget()
- 位置: L3375-3391
- 役割: gPlacements を走査して、そのウィジェットの所属エリアと位置を返す。登録済みでなければ null を返す。
- 触るとき: ウィジェットが今どこにあるかを参照する処理を追加または変更するとき。
- 呼び出し先: `gAreas.has()`, `placements.indexOf()`, `this.widgetExists()`

## widgetExists()
- 位置: L3404-3418
- 役割: ウィジェットが登録済み、または特殊ウィジェットなら真を返す。過去に見たが破棄された API ウィジェットは偽を返す。
- 触るとき: 破棄されたボタンを配置や復元の対象から外すか判定する処理を変えるとき。
- 呼び出し先: `gPalette.has()`, `gSeenWidgets.has()`, `this.isSpecialWidget()`

## addWidgetToArea()
- 位置: L3429-3509
- 役割: ウィジェットを指定エリアの指定位置へ入れる。既に同エリアなら移動、別エリアなら元から外してから入れ、保存と通知を行う。遅延エリアは gFuturePlacements に積む。
- 触るとき: ボタンを配置に追加する処理や、遅延エリアへの登録の挙動を追うとき。
- 呼び出し先: `gAreas.get()`, `gAreas.get(aArea).get()`, `gAreas.has()`, `gPalette.get()`, `gPlacements.has()`, `this.canWidgetMoveToArea()`, `this.getPlacementOfWidget()`, `this.isAreaLazy()`, `this.isSpecialWidget()`, `this.notifyListeners()`, `this.saveState()`
- 条件付き依存: `if (this.isAreaLazy(aArea))` → `gFuturePlacements.get(aArea).add()`
- 条件付き依存: `if (this.isAreaLazy(aArea))` → `gFuturePlacements.get()`
- 条件付き依存: `if (this.isSpecialWidget(aWidgetId))` → `this.ensureSpecialWidgetId()`
- 条件付き依存: `if (oldPlacement && oldPlacement.area == aArea)` → `this.moveWidgetWithinArea()`
- 条件付き依存: `if (oldPlacement)` → `this.removeWidgetFromArea()`
- 条件付き依存: `if (!gPlacements.has(aArea))` → `gPlacements.set()`
- 条件付き依存: `if (!(!gPlacements.has(aArea)))` → `gPlacements.get()`
- 条件付き依存: `if (!(!gPlacements.has(aArea)))` → `placements.splice()`
- 条件付き依存: `if (!aInitialAdd)` → `gDirtyAreaCache.add()`
- 参照: `CustomizableUI.AREA_NO_AREA`, `CustomizableUI.TYPE_PANEL`, `oldPlacement.area`, `placements.length`, `widget.currentArea`, `widget.currentPosition`

## removeWidgetFromArea()
- 位置: L3515-3556
- 役割: ウィジェットを配置から外し、保存と通知を行う。縦タブ時は水平スナップショットからも消す。
- 触るとき: ボタンを外したときに保存状態から消えない問題や、縦タブ切替後に復元されてしまう問題を調べるとき。
- 呼び出し先: `gDirtyAreaCache.add()`, `gPalette.get()`, `gPlacements.get()`, `placements.indexOf()`, `this.getPlacementOfWidget()`, `this.isWidgetRemovable()`, `this.notifyListeners()`, `this.saveState()`
- 条件付き依存: `if (position != -1)` → `placements.splice()`
- 条件付き依存: `if (oldPlacement.area == CustomizableUI.AREA_TABSTRIP)` → `this.deleteWidgetInSavedHorizontalTabStripState()`
- 条件付き依存: `if (!(oldPlacement.area == CustomizableUI.AREA_TABSTRIP))` → `this.getSavedHorizontalSnapshotState().includes()`
- 条件付き依存: `if (!(oldPlacement.area == CustomizableUI.AREA_TABSTRIP))` → `this.getSavedHorizontalSnapshotState()`
- 条件付き依存: `if ( oldPlacement.area == CustomizableUI.AREA_NAVBAR && this.getSavedHorizontalSnapshotState().includes(aWidgetId) )` → `this.deleteWidgetInSavedHorizontalTabStripState()`
- 条件付き依存: `if ( oldPlacement.area == CustomizableUI.AREA_NAVBAR && this.getSavedHorizontalSnapshotState().includes(aWidgetId) )` → `this.deleteWidgetInSavedNavBarWhenVerticalTabsState()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.verticalTabsEnabled`, `oldPlacement.area`, `widget.currentArea`, `widget.currentPosition`

## moveWidgetWithinArea()
- 位置: L3563-3608
- 役割: 同じエリア内でウィジェットの位置を移す。範囲外の値は端へ丸め、位置が変わったときだけ保存して onWidgetMoved を通知する。
- 触るとき: ツールバー内の並べ替えの位置計算を変えるとき、またはドラッグ後の順序がずれる問題を調べるとき。
- 呼び出し先: `gDirtyAreaCache.add()`, `gPalette.get()`, `gPlacements.get()`, `placements.splice()`, `this.getPlacementOfWidget()`, `this.notifyListeners()`, `this.saveState()`
- 参照: `oldPlacement.area`, `oldPlacement.position`, `placements.length`, `widget.currentArea`, `widget.currentPosition`

## getSavedHorizontalSnapshotState()
- 位置: L3618-3632
- 役割: 水平タブストリップの退避配置を pref から JSON として読む。解析に失敗したら空配列を返す。
- 触るとき: 縦タブから水平タブへ戻すときの復元内容を変えるとき。
- 条件付き依存: `if (prefValue)` → `JSON.parse()`
- 条件付き依存: `if (prefValue)` → `lazy.log.warn()`
- 参照: `lazy.horizontalPlacementsPref`

## getSavedVerticalSnapshotState()
- 位置: L3642-3656
- 役割: 縦タブ時のナビバー退避配置を pref から JSON として読む。解析に失敗したら空配列を返す。
- 触るとき: 水平タブから縦タブへ戻すときのナビバー復元内容を変えるとき。
- 条件付き依存: `if (prefValue)` → `JSON.parse()`
- 条件付き依存: `if (prefValue)` → `lazy.log.warn()`
- 参照: `lazy.verticalPlacementsPref`

## loadSavedState()
- 位置: L3664-3695
- 役割: 保存状態の pref を読んで gSavedState に入れる。壊れていれば pref を消して空の状態にし、seen・dirtyAreaCache・newElementCount を復元する。
- 触るとき: 起動時の保存状態の読み込みや壊れた状態の扱いを変えるとき。
- 呼び出し先: `JSON.parse()`, `Services.prefs.clearUserPref()`, `Services.prefs.getCharPref()`, `lazy.log.debug()`
- 条件付き依存: `if (!state)` → `lazy.log.debug()`
- 参照: `gSavedState.currentVersion`, `gSavedState.dirtyAreaCache`, `gSavedState.newElementCount`, `gSavedState.placements`, `gSavedState.seen`
- XPCOM: `Services.prefs`

## restoreStateForArea()
- 位置: L3705-3782
- 役割: エリアの配置を、既存の配置、保存状態、既定値の順に復元する。最後に遅延中のウィジェットを末尾へ足す。
- 触るとき: エリアを登録または再構築したときに、どの配置を採用するかを追うとき。
- 呼び出し先: `gFuturePlacements.has()`, `gPlacements.get()`, `gPlacements.get(aAreaId).join()`, `gPlacements.has()`, `lazy.log.debug()`, `this.beginBatchUpdate()`, `this.endBatchUpdate()`
- 条件付き依存: `if (placementsPreexisted)` → `lazy.log.debug()`
- 条件付き依存: `if (placementsPreexisted)` → `gPlacements.get(aAreaId).entries()`
- 条件付き依存: `if (placementsPreexisted)` → `gPlacements.get()`
- 条件付き依存: `if (placementsPreexisted)` → `this.moveWidgetWithinArea()`
- 条件付き依存: `if (!(placementsPreexisted))` → `gPlacements.set()`
- 条件付き依存: `if (!restored && gSavedState && aAreaId in gSavedState.placements)` → `lazy.log.debug()`
- 条件付き依存: `if (!restored && gSavedState && aAreaId in gSavedState.placements)` → `this.addWidgetToArea()`
- 条件付き依存: `if (!restored)` → `lazy.log.debug()`
- 条件付き依存: `if (!restored)` → `gAreas.get(aAreaId).get()`
- 条件付き依存: `if (!restored)` → `gAreas.get()`
- 条件付き依存: `if (!restored)` → `gAreas.get(aAreaId).has()`
- 条件付き依存: `if ( CustomizableUI.verticalTabsEnabled && gAreas.get(aAreaId).has("verticalTabsDefaultPlacements") )` → `lazy.log.debug()`
- 条件付き依存: `if ( CustomizableUI.verticalTabsEnabled && gAreas.get(aAreaId).has("verticalTabsDefaultPlacements") )` → `gAreas.get(aAreaId).get()`
- 条件付き依存: `if ( CustomizableUI.verticalTabsEnabled && gAreas.get(aAreaId).has("verticalTabsDefaultPlacements") )` → `gAreas.get()`
- 条件付き依存: `if (defaults)` → `this.addWidgetToArea()`
- 条件付き依存: `if (gFuturePlacements.has(aAreaId))` → `gPlacements.get()`
- 条件付き依存: `if (gFuturePlacements.has(aAreaId))` → `gFuturePlacements.get()`
- 条件付き依存: `if (gFuturePlacements.has(aAreaId))` → `areaPlacements.includes()`
- 条件付き依存: `if (gFuturePlacements.has(aAreaId))` → `this.addWidgetToArea()`
- 条件付き依存: `if (gFuturePlacements.has(aAreaId))` → `gFuturePlacements.delete()`
- 参照: `CustomizableUI.verticalTabsEnabled`, `gSavedState.placements`

## restoreSavedHorizontalTabStripState()
- 位置: L3799-3839
- 役割: 退避した水平タブ配置でタブストリップを作り直す。tabbrowser-tabs を含まない場合は既定配置へ戻し、pref を消す。
- 触るとき: 縦タブから水平タブへ切り替えたときにタブ列の並びが崩れる問題を調べるとき。
- 呼び出し先: `Services.prefs.clearUserPref()`, `gPlacements.get()`, `lazy.log.debug()`, `savedPlacements.entries()`, `savedPlacements.includes()`, `this.addWidgetToArea()`, `this.beginBatchUpdate()`, `this.endBatchUpdate()`, `this.getSavedHorizontalSnapshotState()`
- 条件付き依存: `if (!savedPlacements.includes("tabbrowser-tabs"))` → `gAreas.get(tabstripAreaId).get()`
- 条件付き依存: `if (!savedPlacements.includes("tabbrowser-tabs"))` → `gAreas.get()`
- 条件付き依存: `if (!savedPlacements.includes("tabbrowser-tabs"))` → `lazy.log.debug()`
- 条件付き依存: `if (gPlacements.get(CustomizableUI.AREA_VERTICAL_TABSTRIP)?.length)` → `lazy.log.warn()`
- 条件付き依存: `if (gPlacements.get(CustomizableUI.AREA_VERTICAL_TABSTRIP)?.length)` → `gPlacements.get()`
- 参照: `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.AREA_VERTICAL_TABSTRIP`, `gPlacements.get(CustomizableUI.AREA_VERTICAL_TABSTRIP)?.length`
- XPCOM: `Services.prefs`

## deleteWidgetInSavedHorizontalTabStripState()
- 位置: L3850-3857
- 役割: 水平タブの退避配置から指定ウィジェットを取り除き、保存し直す。
- 触るとき: 縦タブ中に外したボタンが水平に戻ったときに再出現する問題を調べるとき。
- 呼び出し先: `savedPlacements.indexOf()`, `this.getSavedHorizontalSnapshotState()`
- 条件付き依存: `if (position != -1)` → `savedPlacements.splice()`
- 条件付き依存: `if (position != -1)` → `this.saveHorizontalTabStripState()`

## deleteWidgetInSavedNavBarWhenVerticalTabsState()
- 位置: L3868-3875
- 役割: 縦タブ時のナビバー退避配置から指定ウィジェットを取り除き、保存し直す。
- 触るとき: 縦タブ中に外したナビバーのボタンが戻ってくる問題を調べるとき。
- 呼び出し先: `savedPlacements.indexOf()`, `this.getSavedVerticalSnapshotState()`
- 条件付き依存: `if (position != -1)` → `savedPlacements.splice()`
- 条件付き依存: `if (position != -1)` → `this.saveNavBarWhenVerticalTabsState()`

## saveHorizontalTabStripState()
- 位置: L3889-3901
- 役割: 水平タブストリップの配置を JSON にして pref へ書く。引数が空なら現在の配置を使う。
- 触るとき: 縦タブへ切り替える直前の水平配置の保存方法を変えるとき。
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setCharPref()`, `lazy.log.debug()`
- 条件付き依存: `if (!placements.length)` → `this.getAreaPlacementsForSaving()`
- 参照: `CustomizableUI.AREA_TABSTRIP`, `placements.length`, `this.serializerHelper`
- XPCOM: `Services.prefs`

## saveNavBarWhenVerticalTabsState()
- 位置: L3915-3925
- 役割: 縦タブ中のナビバー配置を JSON にして pref へ書く。引数が空なら現在の配置を使う。
- 触るとき: 水平タブへ切り替える直前の縦タブ用ナビバー配置の保存方法を変えるとき。
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setCharPref()`, `lazy.log.debug()`
- 条件付き依存: `if (!placements.length)` → `this.getAreaPlacementsForSaving()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `placements.length`, `this.serializerHelper`
- XPCOM: `Services.prefs`

## getAreaPlacementsForSaving()
- 位置: L3940-3961
- 役割: 保存対象となるエリアの配置を、遅延中の配置、現在の配置、保存済みの配置の順に返す。
- 触るとき: 保存時にエリアの配置がどこから取られるかを調べるとき、または一時的に無効なアドオンの配置が消える問題を追うとき。
- 呼び出し先: `gFuturePlacements.get()`, `gPlacements.get()`, `lazy.log.debug()`, `this.isAreaLazy()`
- 条件付き依存: `if (this.isAreaLazy(aAreaId) && gFuturePlacements.get(aAreaId)?.size)` → `gFuturePlacements.get()`
- 条件付き依存: `if (!(this.isAreaLazy(aAreaId) && gFuturePlacements.get(aAreaId)?.size))` → `gPlacements.has()`
- 条件付き依存: `if (gPlacements.has(aAreaId))` → `gPlacements.get()`
- 参照: `gFuturePlacements.get(aAreaId)?.size`, `gSavedState.placements`

## saveState()
- 位置: L3966-3996
- 役割: 全エリアの配置と seen、dirtyAreaCache、版、連番を JSON にして pref に保存する。バッチ中か未変更なら何もしない。
- 触るとき: ツールバーの状態が保存されない、または保存が頻繁すぎる問題を調べるとき。
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setCharPref()`, `gPlacements.keys()`, `lazy.log.debug()`, `placements.set()`, `this.getAreaPlacementsForSaving()`
- 条件付き依存: `if (gSavedState?.placements)` → `Object.keys()`
- 条件付き依存: `if (gSavedState?.placements)` → `allAreaIds.add()`
- 参照: `gSavedState.placements`, `gSavedState?.placements`, `this.serializerHelper`
- XPCOM: `Services.prefs`

## serializerHelper()
- 位置: L4008-4022
- 役割: JSON.stringify の replacer。Map をオブジェクトに、Set を配列に変換する。
- 触るとき: 保存する状態に新しい Map や Set を入れるとき。
- 参照: `aValue.constructor.name`

## beginBatchUpdate()
- 位置: L4027-4029
- 役割: バッチ更新の深さを 1 増やし、その間は保存を遅らせる。
- 触るとき: 複数の配置変更をまとめて一度だけ保存したいとき。

## endBatchUpdate()
- 位置: L4035-4047
- 役割: バッチ更新の深さを 1 減らす。aForceDirty が真なら dirty を立て、深さ 0 で保存する。負になれば例外。
- 触るとき: バッチの開始と終了の対応がずれて例外になる問題を調べるとき。
- 条件付き依存: `if (gInBatchStack == 0)` → `this.saveState()`

## addListener()
- 位置: L4053-4055
- 役割: CustomizableUI の変更通知を受けるリスナーを登録する。
- 触るとき: 配置変更の通知を受ける側を追加するとき。
- 呼び出し先: `gListeners.add()`

## removeListener()
- 位置: L4061-4067
- 役割: リスナーの登録を外す。内部自身は外せないように除外する。
- 触るとき: リスナーを外したあとも通知が届く問題を調べるとき。
- 呼び出し先: `gListeners.delete()`

## notifyListeners()
- 位置: L4081-4095
- 役割: 復元中は何もせず、それ以外は登録済みリスナーの指定名のメソッドを呼ぶ。例外はログに記録して次へ進む。
- 触るとき: 新しい通知イベントを増やす、または特定のリスナーへ通知が届かない理由を調べるとき。
- 呼び出し先: `lazy.log.error()`
- 条件付き依存: `if (typeof listener[aListenerName] == "function")` → `listener[aListenerName].apply()`
- 参照: `e.fileName`, `e.lineNumber`

## _dispatchToolboxEventToWindow()
- 位置: L4111-4118
- 役割: 指定ウィンドウの gNavToolbox に、バブリングする CustomEvent を発火する。
- 触るとき: ツールボックスへのイベント発火の仕組みを変えるとき。
- 呼び出し先: `aWindow.gNavToolbox.dispatchEvent()`
- 参照: `aWindow.CustomEvent`

## dispatchToolboxEvent()
- 位置: L4136-4144
- 役割: 指定ウィンドウ、または全登録ウィンドウの gNavToolbox にカスタムイベントを発火する。
- 触るとき: カスタマイズモードの開始や終了などをツールボックスへ伝えるとき。
- 呼び出し先: `this._dispatchToolboxEventToWindow()`
- 条件付き依存: `if (aWindow)` → `this._dispatchToolboxEventToWindow()`

## createWidget()
- 位置: L4155-4296
- 役割: API 経由でウィジェットを登録する。既定エリアの配置に加え、保存状態からの復元や自動追加を判定し、必要なら追加する。拡張機能ウィジェットは AREA_ADDONS へ回す。
- 触るとき: アドオンや内部コードからボタンを新規作成したときの配置がどう決まるかを調べるとき。
- 呼び出し先: `gAreas.has()`, `gGroupWrapperCache.delete()`, `gPalette.set()`, `gPlacements.get()`, `gPlacements.get(area).indexOf()`, `gSeenWidgets.add()`, `gSingleWrapperCache.get()`, `seenAreas.add()`, `this.beginBatchUpdate()`, `this.endBatchUpdate()`, `this.normalizeWidget()`, `this.notifyListeners()`
- 条件付き依存: `if (!widget)` → `lazy.log.error()`
- 条件付き依存: `if (cache)` → `cache.delete()`
- 条件付き依存: `if (widget.defaultArea)` → `gAreas.get()`
- 条件付き依存: `if (widget.defaultArea)` → `CustomizableUI.isBuiltinToolbar()`
- 条件付き依存: `if (addToDefaultPlacements)` → `area.has()`
- 条件付き依存: `if (area.has("defaultPlacements"))` → `area.get("defaultPlacements").push()`
- 条件付き依存: `if (area.has("defaultPlacements"))` → `area.get()`
- 条件付き依存: `if (!(area.has("defaultPlacements")))` → `area.set()`
- 条件付き依存: `if (widgetMightNeedAutoAdding && gSavedState)` → `Object.keys()`
- 条件付き依存: `if (widgetMightNeedAutoAdding && gSavedState)` → `seenAreas.has()`
- 条件付き依存: `if (widgetMightNeedAutoAdding && gSavedState)` → `gAreas.has()`
- 条件付き依存: `if (widgetMightNeedAutoAdding && gSavedState)` → `gSavedState.placements[area].indexOf()`
- 条件付き依存: `if (widget.currentArea)` → `this.notifyListeners()`
- 条件付き依存: `if (widgetMightNeedAutoAdding)` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (widgetMightNeedAutoAdding)` → `gSeenWidgets.has()`
- 条件付き依存: `if (defaultArea)` → `this.isAreaLazy()`
- 条件付き依存: `if (this.isAreaLazy(defaultArea))` → `gFuturePlacements.get(defaultArea).add()`
- 条件付き依存: `if (this.isAreaLazy(defaultArea))` → `gFuturePlacements.get()`
- 条件付き依存: `if (!(this.isAreaLazy(defaultArea)))` → `this.addWidgetToArea()`
- 条件付き依存: `if (widgetMightNeedAutoAdding)` → `CustomizableUI.isWebExtensionWidget()`
- 条件付き依存: `if ( !widget.currentArea && CustomizableUI.isWebExtensionWidget(widget.id) )` → `this.addWidgetToArea()`
- 参照: `CustomizableUI.AREA_ADDONS`, `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `CustomizableUI.SOURCE_EXTERNAL`, `CustomizableUI.verticalTabsEnabled`, `gSavedState.placements`, `widget.currentArea`, `widget.currentPosition`, `widget.defaultArea`, `widget.defaultAreaVerticalTabs`, `widget.id`, `widget.removable`
- XPCOM: `Services.prefs`

## createBuiltinWidget()
- 位置: L4304-4339
- 役割: CustomizableWidgets の定義を組み込みウィジェットとして登録する。条件付き破棄の Promise があれば、解決時にウィジェットと配置を外す。
- 触るとき: 組み込みボタンの登録や、条件によって消すボタンの仕組みを変えるとき。
- 呼び出し先: `gPalette.set()`, `lazy.log.debug()`, `this.normalizeWidget()`
- 条件付き依存: `if (!widget)` → `lazy.log.error()`
- 条件付き依存: `if (conditionalDestroyPromise)` → `conditionalDestroyPromise.then()`
- 条件付き依存: `if (shouldDestroy)` → `this.destroyWidget()`
- 条件付き依存: `if (shouldDestroy)` → `this.removeWidgetFromArea()`
- 条件付き依存: `if (conditionalDestroyPromise)` → `console.error()`
- 参照: `CustomizableUI.SOURCE_BUILTIN`, `aData.conditionalDestroyPromise`, `aData.id`, `widget.id`

## isAreaLazy()
- 位置: L4348-4353
- 役割: エリアがツールバー型で、まだ配置が復元されていない(遅延中の)場合に真を返す。
- 触るとき: ウィジェットの追加を即時に行うか遅延配列へ回すかを判断する処理を変えるとき。
- 呼び出し先: `gAreas.get()`, `gAreas.get(aAreaId).get()`, `gAreas.has()`, `gPlacements.has()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`

## normalizeWidget()
- 位置: L4368-4525
- 役割: ウィジェット定義の ID や既定値を検証し、既定のプロパティを補った正規化オブジェクトを作る。ID が不正、または必須項目が無い場合は null を返す。
- 触るとき: ボタン定義に新しいプロパティを足す、または不正な定義が登録されない理由を調べるとき。
- 呼び出し先: `/^[a-z0-9-_]{1,}$/i.test()`, `gAreas.has()`, `gPalette.has()`, `gSupportedWidgetTypes.has()`, `this.wrapWidgetEventHandler()`, `widget.implementation.__defineGetter__()`
- 条件付き依存: `if (typeof aData.id != "string" || !/^[a-z0-9-_]{1,}$/i.test(aData.id))` → `lazy.log.error()`
- 条件付き依存: `if (typeof aData[prop] != "string")` → `lazy.log.error()`
- 条件付き依存: `if (!widget.removable)` → `lazy.log.error()`
- 条件付き依存: `if (typeof aData.viewId != "string")` → `lazy.log.error()`
- 条件付き依存: `if ( widget.type == "view" || widget.type == "button-and-view" || aData.viewId )` → `this.wrapWidgetEventHandler()`
- 条件付き依存: `if (widget.type == "custom")` → `this.wrapWidgetEventHandler()`
- 参照: `CustomizableUI.SOURCE_BUILTIN`, `CustomizableUI.SOURCE_EXTERNAL`, `aData._introducedByPref`, `aData.defaultArea`, `aData.defaultAreaVerticalTabs`, `aData.disabled`, `aData.id`, `aData.introducedInVersion`, `aData.onBeforeCommand`, `aData.onCommand`, `aData.type`, `aData.viewId`, `widget._introducedByPref`, `widget._introducedInVersion`, `widget.currentArea`, `widget.defaultArea`, `widget.defaultAreaVerticalTabs`, `widget.disabled`, `widget.id`, `widget.implementation.currentArea`, `widget.onBeforeCommand`, `widget.onCommand`, `widget.removable`, `widget.type`, `widget.viewId`

## wrapWidgetEventHandler()
- 位置: L4538-4558
- 役割: 定義側の onBeforeCreated などのイベント関数を、例外をログに出して握りつぶすラッパーで包んで正規化オブジェクトに入れる。
- 触るとき: ボタンのライフサイクル関数で例外が出たときに上位へ伝わらない挙動を調べるとき。
- 参照: `aWidget.implementation`

## aWidget[aEventName]()
- 位置: L4543-4557
- 役割: ラッパー本体。呼ばれると定義側の同名関数を元の実装オブジェクトの this で実行し、例外は console.error に流す。
- 触るとき: ボタン定義側の関数の this や戻り値がおかしいときに、ここで値が変わっていないか確かめるとき。
- 呼び出し先: `aWidget.implementation[aEventName].apply()`, `console.error()`
- 参照: `aWidget.implementation`

## destroyWidget()
- 位置: L4564-4645
- 役割: API ウィジェットを削除する。既定配置から外し、各ウィンドウのノードを消して onDestroyed を呼ぶ。gPlacements は残し、再登場時に元の位置へ戻す。
- 触るとき: アドオンがボタンを破棄したあとの DOM や配置の後始末を変えるとき、または破棄後に再作成したとき位置が保たれるかを調べるとき。
- 呼び出し先: `gGroupWrapperCache.delete()`, `gPalette.delete()`, `gPalette.get()`, `gSingleWrapperCache.get()`, `this.notifyListeners()`, `window.document.getElementById()`, `window.gNavToolbox.palette.getElementsByAttribute()`
- 条件付き依存: `if (!widget)` → `gGroupWrapperCache.delete()`
- 条件付き依存: `if (!widget)` → `gSingleWrapperCache.get()`
- 条件付き依存: `if (windowCache)` → `windowCache.delete()`
- 条件付き依存: `if (widget.defaultArea)` → `gAreas.get()`
- 条件付き依存: `if (area)` → `area.get()`
- 条件付き依存: `if (area)` → `defaultPlacements.indexOf()`
- 条件付き依存: `if (widgetIndex != -1)` → `defaultPlacements.splice()`
- 条件付き依存: `if (widgetNode)` → `this.notifyListeners()`
- 条件付き依存: `if (widgetNode)` → `widgetNode.remove()`
- 条件付き依存: `if ( widget.type == "view" || widget.type == "button-and-view" || widget.viewId )` → `window.document.getElementById()`
- 条件付き依存: `if (typeof widget[handler] == "function")` → `viewNode.removeEventListener()`
- 条件付き依存: `if (widgetNode && widget.onDestroyed)` → `widget.onDestroyed()`
- 参照: `viewNode._addedEventListeners`, `widget.defaultArea`, `widget.onDestroyed`, `widget.type`, `widget.viewId`, `widgetNode.parentNode`, `window.document`

## getCustomizeTargetForArea()
- 位置: L4653-4666
- 役割: 指定エリアのビルドノードのうち、指定ウィンドウに属するものの customizationTarget を返す。
- 触るとき: 特定ウィンドウのカスタマイズ対象要素を取り出す処理を追うとき。
- 呼び出し先: `gBuildAreas.get()`
- 条件付き依存: `if (node.documentGlobal == aWindow)` → `this.getCustomizationTarget()`
- 参照: `node.documentGlobal`

## reset()
- 位置: L4671-4694
- 役割: 縦タブ設定を偽にしてから UI 状態をリセットし、各エリアを組み直す。外部のウィジェットを見たことにして保存する。
- 触るとき: ツールバーの初期化(リセット)の流れを変えるとき、またはリセット後に縦タブが戻らない問題を調べるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`, `this._rebuildRegisteredAreas()`, `this._resetUIState()`
- 条件付き依存: `if (widget.source == CustomizableUI.SOURCE_EXTERNAL)` → `gSeenWidgets.add()`
- 条件付き依存: `if (gSeenWidgets.size || gNewElementCount)` → `this.saveState()`
- 参照: `CustomizableUI.SOURCE_EXTERNAL`, `gSeenWidgets.size`, `widget.source`
- XPCOM: `Services.prefs`

## _resetUIState()
- 位置: L4703-4780
- 役割: リセット前の密度、タッチモード、テーマなどを退避してから関連 pref を消し、配置を既定値で復元する。拡張機能ウィジェットは AREA_ADDONS へ入れ直す。
- 触るとき: リセットで戻る設定の範囲を変えるとき、またはリセット後に既定と違う設定が残る問題を調べるとき。
- 呼び出し先: `CustomizableUI.isWebExtensionWidget()`, `Services.prefs.clearUserPref()`, `Services.prefs.getBoolPref()`, `Services.prefs.getCharPref()`, `Services.prefs.getIntPref()`, `Services.prefs.prefHasUserValue()`, `gDefaultTheme.enable()`, `gPlacements.set()`, `lazy.log.debug()`, `oldAddonPlacements.includes()`
- 条件付き依存: `if (areaId != CustomizableUI.AREA_ADDONS)` → `this.restoreStateForArea()`
- 条件付き依存: `if ( CustomizableUI.isWebExtensionWidget(widgetId) && !oldAddonPlacements.includes(widgetId) )` → `this.addWidgetToArea()`
- 参照: `CustomizableUI.AREA_ADDONS`, `gUIStateBeforeReset.autoHideDownloadsButton`, `gUIStateBeforeReset.autoTouchMode`, `gUIStateBeforeReset.autoTouchModeHadUserValue`, `gUIStateBeforeReset.currentTheme`, `gUIStateBeforeReset.drawInTitlebar`, `gUIStateBeforeReset.newElementCount`, `gUIStateBeforeReset.sidebarPositionStart`, `gUIStateBeforeReset.uiCustomizationState`, `gUIStateBeforeReset.uiDensity`, `gUIStateBeforeReset.uiDensityHadUserValue`
- XPCOM: `Services.prefs`

## _rebuildRegisteredAreas()
- 位置: L4786-4810
- 役割: 全ビルド済みエリアを現在の配置で組み直し、ツールバー型なら defaultCollapsed に従って表示状態を設定する。
- 触るとき: 配置の変更後にすべてのウィンドウのツールバーを再描画させたいとき。
- 呼び出し先: `area.get()`, `gAreas.get()`, `gPlacements.get()`, `this.buildArea()`
- 条件付き依存: `if (area.get("type") == CustomizableUI.TYPE_TOOLBAR)` → `area.get()`
- 条件付き依存: `if (defaultCollapsed !== null)` → `win.setToolbarVisibility()`
- 参照: `CustomizableUI.TYPE_TOOLBAR`, `areaNode.documentGlobal`

## undoReset()
- 位置: L4816-4875
- 役割: 退避しておいた状態と pref を戻し、保存状態から配置を読み直して全エリアを組み直す。退避が無ければ何もしない。
- 触るとき: リセットの取り消し機能の挙動を変えるとき、またはリセットを取り消しても戻らない項目を調べるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`, `Services.prefs.setCharPref()`, `Services.prefs.setIntPref()`, `currentTheme.enable()`, `this._clearPreviousUIState()`, `this.loadSavedState()`
- 条件付き依存: `if (uiDensityHadUserValue)` → `Services.prefs.setIntPref()`
- 条件付き依存: `if (!(uiDensityHadUserValue))` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (autoTouchModeHadUserValue)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!(autoTouchModeHadUserValue))` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (gSavedState)` → `Object.keys()`
- 条件付き依存: `if (gSavedState)` → `gPlacements.set()`
- 条件付き依存: `if (gSavedState)` → `this._rebuildRegisteredAreas()`
- 参照: `gSavedState.placements`, `gUIStateBeforeReset.drawInTitlebar`, `gUIStateBeforeReset.newElementCount`, `gUIStateBeforeReset.uiCustomizationState`
- XPCOM: `Services.prefs`

## _clearPreviousUIState()
- 位置: L4881-4885
- 役割: リセット前に退避した状態の値をすべて null にする。
- 触るとき: 取り消し可能な状態の期限を変えるとき。
- 呼び出し先: `Object.getOwnPropertyNames()`, `Object.getOwnPropertyNames(gUIStateBeforeReset).forEach()`

## isWidgetRemovable()
- 位置: L4893-4950
- 役割: API 提供は定義の removable、XUL 提供はノードの removable 属性を見る。特殊ウィジェットや破棄済みは常に真を返す。
- 触るとき: ボタンを外せるかどうかの判定を変えるとき、または移動できないボタンが出る問題を調べるとき。
- 呼び出し先: `this.getWidgetProvider()`
- 条件付き依存: `if (!(typeof aWidget == "string"))` → `aWidget.getAttribute()`
- 条件付き依存: `if (!(typeof aWidget == "string"))` → `["toolbarspring", "toolbarspacer", "toolbarseparator"].includes()`
- 条件付き依存: `if (!(typeof aWidget == "string"))` → `aWidget.nodeName.substring()`
- 条件付き依存: `if (provider == CustomizableUI.PROVIDER_API)` → `gPalette.get()`
- 条件付き依存: `if (!widgetNode)` → `this.getWidgetNode()`
- 条件付き依存: `if (provider == CustomizableUI.PROVIDER_XUL)` → `widgetNode.getAttribute()`
- 参照: `CustomizableUI.PROVIDER_API`, `CustomizableUI.PROVIDER_XUL`, `aWidget.id`, `aWidget.nodeName`, `gBuildWindows.size`, `gPalette.get(widgetId).removable`

## canWidgetMoveToArea()
- 位置: L4958-4998
- 役割: 特殊ウィジェットをパネルへ入れない、拡張機能を AREA_ADDONS 以外のパネルや一覧へ入れない、といった移動可否を判定する。
- 触るとき: ボタンの移動先の制限を変えるとき、または拡張機能ボタンを移せない理由を調べるとき。
- 呼び出し先: `CustomizableUI.isWebExtensionWidget()`, `gAreas.get()`, `gAreas.get(aArea).get()`, `gAreas.has()`, `this.getPlacementOfWidget()`, `this.isSpecialWidget()`, `this.isWidgetRemovable()`
- 条件付き依存: `if (CustomizableUI.isWebExtensionWidget(aWidgetId))` → `gAreas.get(aArea).get()`
- 条件付き依存: `if (CustomizableUI.isWebExtensionWidget(aWidgetId))` → `gAreas.get()`
- 参照: `CustomizableUI.AREA_ADDONS`, `CustomizableUI.AREA_NO_AREA`, `CustomizableUI.TYPE_PANEL`, `placement.area`

## ensureWidgetPlacedInWindow()
- 位置: L5006-5026
- 役割: 配置があるのにそのウィンドウのエリアにノードが無ければ、insertNodeInWindow で挿入する。
- 触るとき: 新しく開いたウィンドウに既存ボタンが出ない問題を調べるとき。
- 呼び出し先: `[...areaNodes].filter()`, `container[0].getElementsByAttribute()`, `gBuildAreas.get()`, `this.getPlacementOfWidget()`, `this.insertNodeInWindow()`
- 参照: `container.length`, `n.documentGlobal`, `placement.area`

## _getCurrentWidgetsInContainer()
- 位置: L5039-5075
- 役割: コンテナの子(オーバーフロー先を含む)のうち、保存配置の順に、存在するものだけを返す。
- 触るとき: ツールバーの現在の中身と配置を比べる処理を変えるとき。
- 呼び出し先: `CustomizableUI.getWidgetIdsInArea()`, `addUnskippedChildren()`, `container.getAttribute()`, `currentWidgets.has()`, `orderedPlacements.filter()`, `this.getCustomizationTarget()`, `this.getWidgetProvider()`
- 条件付き依存: `if (container.getAttribute("overflowing") == "true")` → `container.getAttribute()`
- 条件付き依存: `if (container.getAttribute("overflowing") == "true")` → `addUnskippedChildren()`
- 条件付き依存: `if (container.getAttribute("overflowing") == "true")` → `container.ownerDocument.getElementById()`
- 参照: `CustomizableUI.PROVIDER_API`, `container.id`

## addUnskippedChildren()
- 位置: L5041-5051
- 役割: 親要素の子から skipintoolbarset でないものの ID を集める。toolbarpaletteitem の場合は内側の要素を見る。
- 触るとき: ツールバーの子のうち対象外の要素をどう除外するかを変えるとき。
- 呼び出し先: `realNode.getAttribute()`
- 条件付き依存: `if (realNode.getAttribute("skipintoolbarset") != "true")` → `currentWidgets.add()`
- 参照: `node.firstElementChild`, `node.localName`, `parent.children`, `realNode.id`

## inDefaultState()
- 位置: L5082-5213
- 役割: 全エリアの現在の配置が既定と一致するか、ツールバーの表示状態、密度、テーマ、関連 pref の既定値を調べて真偽を返す。縦タブ中は常に偽。
- 触るとき: 既定状態かどうかで表示や「リセット」ボタンの有効化を変えるとき、または既定状態と判定されない理由を調べるとき。
- 呼び出し先: `Services.prefs.prefHasUserValue()`, `currentPlacements.join()`, `defaultPlacements.join()`, `gBuildAreas.get()`, `gPlacements.get()`, `lazy.log.debug()`, `props .get()`, `props .get("defaultPlacements") .filter()`, `this.matchingSpecials()`, `this.widgetExists()`
- 条件付き依存: `if (buildAreaNodes && buildAreaNodes.size)` → `props.get()`
- 条件付き依存: `if (props.get("type") == CustomizableUI.TYPE_TOOLBAR)` → `this._getCurrentWidgetsInContainer(container).filter()`
- 条件付き依存: `if (props.get("type") == CustomizableUI.TYPE_TOOLBAR)` → `this._getCurrentWidgetsInContainer()`
- 条件付き依存: `if (!(props.get("type") == CustomizableUI.TYPE_TOOLBAR))` → `currentPlacements.filter()`
- 条件付き依存: `if (!(props.get("type") == CustomizableUI.TYPE_TOOLBAR))` → `container.getElementsByAttribute()`
- 条件付き依存: `if (!(props.get("type") == CustomizableUI.TYPE_TOOLBAR))` → `removableOrDefault()`
- 条件付き依存: `if (props.get("type") == CustomizableUI.TYPE_TOOLBAR)` → `props.get()`
- 条件付き依存: `if (areaId == CustomizableUI.AREA_BOOKMARKS)` → `Services.prefs.getCharPref()`
- 条件付き依存: `if (areaId == CustomizableUI.AREA_BOOKMARKS)` → `Services.prefs.prefHasUserValue()`
- 条件付き依存: `if (!(areaId == CustomizableUI.AREA_BOOKMARKS))` → `container.getAttribute()`
- 条件付き依存: `if (!(areaId == CustomizableUI.AREA_BOOKMARKS))` → `container.hasAttribute()`
- 条件付き依存: `if (defaultCollapsed !== null && nondefaultState)` → `lazy.log.debug()`
- 条件付き依存: `if ( currentPlacements[i] != defaultPlacements[i] && !this.matchingSpecials(currentPlacements[i], defaultPlacements[i]) )` → `lazy.log.debug()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(kPrefUIDensity))` → `lazy.log.debug()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(kPrefAutoTouchMode))` → `lazy.log.debug()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(kPrefDrawInTitlebar))` → `lazy.log.debug()`
- 条件付き依存: `if (gDefaultTheme && gDefaultTheme.id != gSelectedTheme.id)` → `lazy.log.debug()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(kPrefSidebarPositionStartEnabled))` → `lazy.log.debug()`
- 参照: `CustomizableUI.AREA_BOOKMARKS`, `CustomizableUI.TYPE_TOOLBAR`, `CustomizableUI.verticalTabsEnabled`, `buildAreaNodes.size`, `currentPlacements.length`, `defaultPlacements.length`, `gDefaultTheme.id`, `gSelectedTheme.id`
- XPCOM: `Services.prefs`

## removableOrDefault()
- 位置: L5100-5105
- 役割: inDefaultState の内部関数。ノードや ID が取り外し可能、または既定配置に含まれていれば真を返す。
- 触るとき: 既定状態の判定で、外せない項目が状態比較から除外されない問題を調べるとき。
- 呼び出し先: `defaultPlacements.includes()`, `this.isWidgetRemovable()`
- 参照: `itemNodeOrItem.id`

## getCollapsedToolbarIds()
- 位置: L5220-5236
- 役割: 組み込みツールバーのうち、collapsed(メニューバーは autohide)の属性を持つ ID の集合を返す。
- 触るとき: ツールバーが隠れているかどうかで表示判断を変えるとき。
- 呼び出し先: `toolbar.getAttribute()`, `toolbar.hasAttribute()`, `window.document.getElementById()`
- 条件付き依存: `if (toolbar.hasAttribute(hidingAttribute))` → `collapsedToolbars.add()`
- 参照: `CustomizableUIInternal.builtinToolbars`

## setToolbarVisibility()
- 位置: L5243-5253
- 役割: 全ウィンドウで、指定ツールバーの表示状態を切り替える。永続化は最初に変わったツールバーだけで行う。
- 触るとき: ツールバーの表示切替を全ウィンドウに伝えるとき。
- 呼び出し先: `window.document.getElementById()`
- 条件付き依存: `if (toolbar)` → `window.setToolbarVisibility()`
- 参照: `CustomizableUI.windows`

## widgetIsLikelyVisible()
- 位置: L5261-5286
- 役割: ウィジェットの配置先から、画面に見えていそうかを推定する。ナビバーは真、メニューバーや水平タブやブックマークは状態によって判断する。
- 触るとき: 見えていない機能の表示の判断(テレメトリや表示切替)を変えるとき。
- 呼び出し先: `Services.prefs.getCharPref()`, `this.getCollapsedToolbarIds()`, `this.getCollapsedToolbarIds(window).has()`, `this.getPlacementOfWidget()`
- 参照: `CustomizableUI.AREA_BOOKMARKS`, `CustomizableUI.AREA_MENUBAR`, `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.verticalTabsEnabled`, `placement.area`
- XPCOM: `Services.prefs`

## observe()
- 位置: L5296-5305
- 役割: browser-set-toolbar-visibility の通知でツールバー表示を変え、nsPref:changed では sidebar 関連の pref を整合させる。
- 触るとき: 縦タブやサイドバー関連の pref 変更が効かない問題を調べるとき。
- 条件付き依存: `if (aTopic == "browser-set-toolbar-visibility")` → `JSON.parse()`
- 条件付き依存: `if (aTopic == "browser-set-toolbar-visibility")` → `CustomizableUI.setToolbarVisibility()`
- 条件付き依存: `if (aTopic === "nsPref:changed")` → `this.reconcileSidebarPrefs()`

## initializeForTabsOrientation()
- 位置: L5313-5428
- 役割: 起動時のタブの向きに応じて配置を整える。水平なら退避した配置を復元し、縦なら tabbrowser-tabs を縦用エリアへ移し、他のボタンはナビバーへ移す。
- 触るとき: 縦タブの初回起動や保存状態の移行で、ボタンがどのエリアに入るかを変えるとき。
- 呼び出し先: `CustomizableUI.isWebExtensionWidget()`, `gAreas.get()`, `gAreas.get(CustomizableUI.AREA_TABSTRIP).get()`, `gFuturePlacements.has()`, `lazy.log.debug()`, `this.addWidgetToArea()`, `this.isSpecialWidget()`, `this.removeWidgetFromArea()`, `widgetId.includes()`, `widgetsMoved.push()`
- 条件付き依存: `if (!toVertical)` → `this.getSavedHorizontalSnapshotState()`
- 条件付き依存: `if (!toVertical)` → `lazy.log.debug()`
- 条件付き依存: `if (savedPlacements.length)` → `this.restoreSavedHorizontalTabStripState()`
- 条件付き依存: `if (!savedPlacements[CustomizableUI.AREA_VERTICAL_TABSTRIP]?.length)` → `gAreas .get(CustomizableUI.AREA_VERTICAL_TABSTRIP) .get()`
- 条件付き依存: `if (!savedPlacements[CustomizableUI.AREA_VERTICAL_TABSTRIP]?.length)` → `gAreas .get()`
- 条件付き依存: `if (!savedPlacements[CustomizableUI.AREA_VERTICAL_TABSTRIP]?.length)` → `lazy.log.debug()`
- 条件付き依存: `if (gFuturePlacements.has(CustomizableUI.AREA_TABSTRIP))` → `gFuturePlacements.get()`
- 条件付き依存: `if (gFuturePlacements.has(CustomizableUI.AREA_TABSTRIP))` → `tabstripPlacements.includes()`
- 条件付き依存: `if (!tabstripPlacements.includes(id))` → `tabstripPlacements.push()`
- 条件付き依存: `if (gFuturePlacements.has(CustomizableUI.AREA_TABSTRIP))` → `gFuturePlacements.delete()`
- 条件付き依存: `if (widgetId == "tabbrowser-tabs")` → `lazy.log.debug()`
- 条件付き依存: `if (widgetId == "tabbrowser-tabs")` → `this.addWidgetToArea()`
- 条件付き依存: `if (this.isSpecialWidget(widgetId) && widgetId.includes("spring"))` → `this.removeWidgetFromArea()`
- 条件付き依存: `if (CustomizableUI.isWebExtensionWidget(widgetId))` → `lazy.log.debug()`
- 条件付き依存: `if (!lazy.horizontalPlacementsPref)` → `lazy.log.debug()`
- 条件付き依存: `if (!lazy.horizontalPlacementsPref)` → `CustomizableUIInternal.saveHorizontalTabStripState()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.AREA_VERTICAL_TABSTRIP`, `gSavedState?.placements`, `lazy.horizontalPlacementsPref`, `savedPlacements.length`, `savedPlacements[CustomizableUI.AREA_VERTICAL_TABSTRIP]?.length`, `tabstripPlacements.length`, `widgetsMoved.length`

## reconcileSidebarPrefs()
- 位置: L5440-5497
- 役割: サイドバーの revamp、縦タブ、位置(左右)の pref の組み合わせを整える。ナビバーの既定配置にサイドバーボタンを入れたり外したりする。
- 触るとき: サイドバーと縦タブの pref を連動させる仕様を変えるとき、またはサイドバーボタンの位置がおかしいとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `defaults.indexOf()`, `gAreas.get()`, `gAreas.set()`, `gPlacements.get()`, `lazy.log.debug()`, `navbarPlacements.indexOf()`, `props.get()`, `props.set()`
- 条件付き依存: `if (verticalTabsEnabled && !sidebarRevampEnabled)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (sidebarRevampEnabled && sidebarButtonIndex < 0)` → `defaults.unshift()`
- 条件付き依存: `if (!sidebarRevampEnabled && sidebarButtonIndex > -1)` → `defaults.splice()`
- 条件付き依存: `if (!sidebarRevampEnabled && verticalTabsEnabled)` → `lazy.log.debug()`
- 条件付き依存: `if (!sidebarRevampEnabled && verticalTabsEnabled)` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (!positionStartEnabled && index === 0)` → `this.moveWidgetWithinArea()`
- 条件付き依存: `if (positionStartEnabled && index === navbarPlacements.length - 1)` → `this.moveWidgetWithinArea()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `navbarPlacements.length`
- XPCOM: `Services.prefs`

## tabstripAreasReady()
- 位置: L5503-5508
- 役割: 水平と縦のタブストリップ両方のビューが構築済みかを返す。
- 触るとき: タブストリップの向きの切替を始めてよい時点かを判断するとき。
- 呼び出し先: `gBuildAreas.get()`
- 参照: `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.AREA_VERTICAL_TABSTRIP`, `gBuildAreas.get(CustomizableUI.AREA_TABSTRIP)?.size`, `gBuildAreas.get(CustomizableUI.AREA_VERTICAL_TABSTRIP)?.size`

## updateTabStripOrientation()
- 位置: L5514-5636
- 役割: 縦タブ設定が前回と変わったときだけ、必要に応じて水平配置を退避し、タブストリップを縦か水平に切り替える。
- 触るとき: 縦タブへの切替や戻し操作のタイミングや配置の保存を変えるとき。
- 呼び出し先: `Services.obs.notifyObservers()`, `changeWidgetRemovability()`, `lazy.log.debug()`, `this.setToolbarVisibility()`, `win.TabBarVisibility.update()`
- 条件付き依存: `if (!this.tabstripAreasReady)` → `lazy.log.debug()`
- 条件付き依存: `if (toVertical === gCurrentVerticalTabs)` → `lazy.log.debug()`
- 条件付き依存: `if (toVertical && gCurrentVerticalTabs !== null)` → `lazy.log.debug()`
- 条件付き依存: `if (toVertical && gCurrentVerticalTabs !== null)` → `CustomizableUIInternal.saveHorizontalTabStripState()`
- 条件付き依存: `if (toVertical)` → `lazy.log.debug()`
- 条件付き依存: `if (toVertical)` → `Services.prefs.getCharPref()`
- 条件付き依存: `if ( !Services.prefs.getCharPref(kPrefCustomizationHorizontalTabsBackup, "") )` → `Services.prefs.setCharPref()`
- 条件付き依存: `if ( !Services.prefs.getCharPref(kPrefCustomizationHorizontalTabsBackup, "") )` → `Services.prefs.getCharPref()`
- 条件付き依存: `if (toVertical)` → `CustomizableUI.beginBatchUpdate()`
- 条件付き依存: `if (toVertical)` → `this.getSavedVerticalSnapshotState()`
- 条件付き依存: `if (toVertical)` → `this.getSavedHorizontalSnapshotState()`
- 条件付き依存: `if (toVertical)` → `gPlacements.get(CustomizableUI.AREA_NAVBAR).at()`
- 条件付き依存: `if (toVertical)` → `gPlacements.get()`
- 条件付き依存: `if (toVertical)` → `CustomizableUI.getWidgetIdsInArea()`
- 条件付き依存: `if (id == "tabbrowser-tabs")` → `CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if (toVertical)` → `this.isSpecialWidget()`
- 条件付き依存: `if (toVertical)` → `id.includes()`
- 条件付き依存: `if (this.isSpecialWidget(id) && id.includes("spring"))` → `this.removeWidgetFromArea()`
- 条件付き依存: `if (toVertical)` → `tabstripPlacements.includes()`
- 条件付き依存: `if (toVertical)` → `customVerticalNavbarPlacements.includes()`
- 条件付き依存: `if (toVertical)` → `CustomizableUI.isWidgetRemovable()`
- 条件付き依存: `if (toVertical)` → `CustomizableUI.isWebExtensionWidget()`
- 条件付き依存: `if (toVertical)` → `CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if (toVertical)` → `this.removeWidgetFromArea()`
- 条件付き依存: `if (toVertical)` → `customVerticalNavbarPlacements.forEach()`
- 条件付き依存: `if (tabstripPlacements.includes(id))` → `CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if (isSidebarLast)` → `this.addWidgetToArea()`
- 条件付き依存: `if (toVertical)` → `CustomizableUI.endBatchUpdate()`
- 条件付き依存: `if (!(toVertical))` → `this.saveNavBarWhenVerticalTabsState()`
- 条件付き依存: `if (!(toVertical))` → `this.restoreSavedHorizontalTabStripState()`
- 参照: `CustomizableUI.AREA_NAVBAR`, `CustomizableUI.AREA_TABSTRIP`, `CustomizableUI.AREA_VERTICAL_TABSTRIP`, `CustomizableUI.verticalTabsEnabled`, `this.tabstripAreasReady`
- XPCOM: `Services.obs` / `Services.prefs`

## changeWidgetRemovability()
- 位置: L5537-5544
- 役割: updateTabStripOrientation の内部関数。指定ウィジェットの全インスタンスノードの removable 属性を書き換える。tabbrowser-tabs を一時的に動かすために使う。
- 触るとき: 縦タブ切替の途中で tabbrowser-tabs の removable を一時的に変える理由を追うとき。
- 呼び出し先: `CustomizableUI.getWidget()`
- 条件付き依存: `if (node)` → `node.setAttribute()`
- 条件付き依存: `if (node)` → `removable.toString()`
- 参照: `widget.instances`

## [Symbol.iterator]()
- 位置: L5734-5738
- 役割: 公開の windows プロパティのイテレータ。ビルド済みの全ブラウザウィンドウを順に返す。
- 触るとき: CustomizableUI が管理する全ウィンドウに同じ処理を回すとき。
- 参照: `Symbol.iterator`

## verticalTabsEnabled()
- 位置: L5741-5743
- 役割: 縦タブが有効かを、sidebar.verticalTabs の監視値から返す。
- 触るとき: 縦タブかどうかで配置や表示を分ける判断を追うとき。
- 参照: `lazy.verticalTabsPref`

## addListener()
- 位置: L6013-6015
- 役割: 公開 API。CustomizableUIInternal.addListener へ転送する。
- 触るとき: 外部から配置変更の通知を受けたいとき、または公開 API の入口を追うとき。
- 呼び出し先: `CustomizableUIInternal.addListener()`

## removeListener()
- 位置: L6023-6025
- 役割: 公開 API。CustomizableUIInternal.removeListener へ転送する。
- 触るとき: 外部のリスナー解除が効かない問題を調べるとき。
- 呼び出し先: `CustomizableUIInternal.removeListener()`

## registerArea()
- 位置: L6052-6054
- 役割: 公開 API。エリアを登録する。内部実装へ転送する。
- 触るとき: アドオンや内部モジュールが新しいツールバーやパネルを登録するとき。
- 呼び出し先: `CustomizableUIInternal.registerArea()`

## registerToolbarNode()
- 位置: L6069-6071
- 役割: 公開 API。ツールバーのノードを登録する。内部実装へ転送する。
- 触るとき: customizable 属性のあるツールバーを登録するとき。
- 呼び出し先: `CustomizableUIInternal.registerToolbarNode()`

## registerPanelNode()
- 位置: L6082-6084
- 役割: 公開 API。パネルのノードを登録する。内部実装へ転送する。
- 触るとき: パネル内容の DOM をエリアに結び付けるとき。
- 呼び出し先: `CustomizableUIInternal.registerPanelNode()`

## unregisterArea()
- 位置: L6108-6110
- 役割: 公開 API。エリアの登録を解除する。内部実装へ転送する。
- 触るとき: エリアを削除するときに配置情報を残すかどうかを決めるとき。
- 呼び出し先: `CustomizableUIInternal.unregisterArea()`

## addWidgetToArea()
- 位置: L6133-6135
- 役割: 公開 API。ウィジェットを指定エリアへ追加する。内部実装へ転送する。
- 触るとき: アドオンなどが既存ツールバーへボタンを入れるとき。
- 呼び出し先: `CustomizableUIInternal.addWidgetToArea()`

## removeWidgetFromArea()
- 位置: L6146-6148
- 役割: 公開 API。ウィジェットをエリアから外す。内部実装へ転送する。
- 触るとき: ボタンを外す操作を呼び出し側から行うとき。
- 呼び出し先: `CustomizableUIInternal.removeWidgetFromArea()`

## moveWidgetWithinArea()
- 位置: L6165-6167
- 役割: 公開 API。同じエリア内でウィジェットを移動させる。内部実装へ転送する。
- 触るとき: ボタンの並び替えをプログラムから行うとき。
- 呼び出し先: `CustomizableUIInternal.moveWidgetWithinArea()`

## ensureWidgetPlacedInWindow()
- 位置: L6186-6191
- 役割: 公開 API。ウィンドウ作成後に作られた XUL ウィジェットを、正しい位置へ配置する。内部実装へ転送する。
- 触るとき: 新しいウィンドウに作ったボタンの位置を揃えたいとき。
- 呼び出し先: `CustomizableUIInternal.ensureWidgetPlacedInWindow()`

## beginBatchUpdate()
- 位置: L6204-6206
- 役割: 公開 API。バッチ更新を開始する。その間は状態を保存しない。
- 触るとき: 複数の配置変更を一度にまとめて行うとき。
- 呼び出し先: `CustomizableUIInternal.beginBatchUpdate()`

## endBatchUpdate()
- 位置: L6220-6222
- 役割: 公開 API。バッチ更新を終了する。すべて終われば保存する。
- 触るとき: beginBatchUpdate と対になる終了処理を書くとき。
- 呼び出し先: `CustomizableUIInternal.endBatchUpdate()`

## createWidget()
- 位置: L6424-6428
- 役割: 公開 API。ウィジェットを作成し、内部で登録した結果をラッパーにして返す。
- 触るとき: アドオンや内部から新しいボタンを作るとき、その戻り値を配置やイベントに使うとき。
- 呼び出し先: `CustomizableUIInternal.createWidget()`, `CustomizableUIInternal.wrapWidget()`

## destroyWidget()
- 位置: L6441-6443
- 役割: 公開 API。ウィジェットを破棄する。内部実装へ転送する。
- 触るとき: ボタンを削除する処理を呼び出し側から行うとき。
- 呼び出し先: `CustomizableUIInternal.destroyWidget()`

## getWidget()
- 位置: L6508-6510
- 役割: ウィジェット ID からラッパーを返す。存在が分からない XUL 提供ウィジェットでも、ラッパーは返る。
- 触るとき: ウィジェットの状態を読むか操作するための入口として使うとき。
- 呼び出し先: `CustomizableUIInternal.wrapWidget()`

## getUnusedWidgets()
- 位置: L6524-6529
- 役割: パレットにあるウィジェットを、ラッパーの配列で返す。
- 触るとき: カスタマイズ画面で未使用のボタン一覧を作るとき。
- 呼び出し先: `CustomizableUIInternal.getUnusedWidgets()`, `CustomizableUIInternal.getUnusedWidgets(aWindowPalette).map()`
- 参照: `CustomizableUIInternal.wrapWidget`

## getWidgetIdsInArea()
- 位置: L6542-6552
- 役割: 指定エリアの配置を ID の配列で返す。未登録エリアや未復元のエリアでは例外を投げる。
- 触るとき: エリア内のボタン順を調べるとき。例外が出た場合はエリアの復元が済んでいるかを確かめる。
- 呼び出し先: `gAreas.has()`, `gPlacements.get()`, `gPlacements.has()`

## getDefaultPlacementsForArea()
- 位置: L6563-6565
- 役割: 指定エリアの既定配置を ID の配列で返す。
- 触るとき: 既定配置と現在の配置を比べる処理を書くとき。
- 呼び出し先: `gAreas.get()`, `gAreas.get(aArea).get()`

## getWidgetsInArea()
- 位置: L6582-6587
- 役割: 指定エリア内のウィジェットを、ラッパーの配列で返す。
- 触るとき: エリアのボタンをまとめて操作するとき。null が混ざる点に注意する。
- 呼び出し先: `this.getWidgetIdsInArea()`, `this.getWidgetIdsInArea(aArea).map()`
- 参照: `CustomizableUIInternal.wrapWidget`

## ensureSubviewListeners()
- 位置: L6597-6599
- 役割: 公開 API。ビューノードにサブビューのイベント監視を付ける。内部実装へ転送する。
- 触るとき: ビューを後から作ったときに ViewShowing などを届けたいとき。
- 呼び出し先: `CustomizableUIInternal.ensureSubviewListeners()`

## areas()
- 位置: L6605-6607
- 役割: 既知のエリア ID を配列のコピーで返す。
- 触るとき: 全エリアを列挙する処理を書くとき。
- 呼び出し先: `gAreas.keys()`

## getAreaType()
- 位置: L6620-6623
- 役割: エリアの種別(ツールバーかパネル)を返す。未知のエリアなら null を返す。
- 触るとき: ボタンの振る舞いを、ツールバーとパネルで分けるとき。
- 呼び出し先: `area.get()`, `gAreas.get()`

## isToolbarDefaultCollapsed()
- 位置: L6634-6637
- 役割: ツールバーの既定の折りたたみ状態を返す。未知のエリアなら null を返す。
- 触るとき: ツールバーの既定の表示状態を判定するとき。
- 呼び出し先: `area.get()`, `gAreas.get()`

## getCustomizeTargetForArea()
- 位置: L6665-6667
- 役割: 公開 API。指定エリアと窓の customization target を返す。内部実装へ転送する。
- 触るとき: ボタンを入れる実際の親要素を知りたいとき。
- 呼び出し先: `CustomizableUIInternal.getCustomizeTargetForArea()`

## reset()
- 位置: L6675-6677
- 役割: 公開 API。カスタマイズの状態を既定へ戻す。内部実装へ転送する。
- 触るとき: 利用者が「既定に戻す」を押したときの流れを追うとき。
- 呼び出し先: `CustomizableUIInternal.reset()`

## undoReset()
- 位置: L6685-6687
- 役割: 公開 API。直前のリセットを取り消す。内部実装へ転送する。
- 触るとき: リセットの取り消しを呼び出すとき。
- 呼び出し先: `CustomizableUIInternal.undoReset()`

## removeExtraToolbar()
- 位置: L6698-6700
- 役割: 公開 API。追加されたツールバーを外す。内部実装へ転送する。
- 触るとき: カスタマイズ画面から追加ツールバーを削除するとき。
- 呼び出し先: `CustomizableUIInternal.removeExtraToolbar()`

## canUndoReset()
- 位置: L6708-6717
- 役割: 直前のリセットを取り消せるかを、退避状態の値が残っているかで判定する。
- 触るとき: 取り消しボタンを有効にするかを判断するとき。
- 参照: `gUIStateBeforeReset.autoTouchMode`, `gUIStateBeforeReset.currentTheme`, `gUIStateBeforeReset.drawInTitlebar`, `gUIStateBeforeReset.sidebarPositionStart`, `gUIStateBeforeReset.uiCustomizationState`, `gUIStateBeforeReset.uiDensity`

## getPlacementOfWidget()
- 位置: L6746-6752
- 役割: 公開 API。ウィジェットの配置先と位置を返す。内部実装へ転送する。
- 触るとき: ボタンが今どのエリアの何番目にあるかを調べるとき。最も軽い問い合わせ方法。
- 呼び出し先: `CustomizableUIInternal.getPlacementOfWidget()`

## isWidgetRemovable()
- 位置: L6772-6774
- 役割: 公開 API。ウィジェットを外せるかを返す。内部実装へ転送する。
- 触るとき: 外すボタンを表示するかを決めるとき。
- 呼び出し先: `CustomizableUIInternal.isWidgetRemovable()`

## canWidgetMoveToArea()
- 位置: L6790-6792
- 役割: 公開 API。ウィジェットを指定エリアへ移せるかを返す。内部実装へ転送する。
- 触るとき: ドラッグ先の有効性を判定するとき。
- 呼び出し先: `CustomizableUIInternal.canWidgetMoveToArea()`

## inDefaultState()
- 位置: L6802-6804
- 役割: 公開 API。現在の状態が既定かを返す。内部実装へ転送する。
- 触るとき: 既定状態かどうかで表示を変えるとき。コストがあるので必要な時だけ呼ぶ。
- 参照: `CustomizableUIInternal.inDefaultState`

## setToolbarVisibility()
- 位置: L6814-6816
- 役割: 公開 API。ツールバーの表示状態を全ウィンドウで変える。内部実装へ転送する。
- 触るとき: ツールバーを表示したり隠したりするとき。
- 呼び出し先: `CustomizableUIInternal.setToolbarVisibility()`

## getCollapsedToolbarIds()
- 位置: L6827-6829
- 役割: 公開 API。ウィンドウ内で折りたたまれている組み込みツールバーの ID 集合を返す。内部実装へ転送する。
- 触るとき: 隠れているツールバーに依存する表示判断を行うとき。
- 呼び出し先: `CustomizableUIInternal.getCollapsedToolbarIds()`

## widgetIsLikelyVisible()
- 位置: L6848-6850
- 役割: ウィジェットが画面に見えていそうかを返す。配置がなければ偽、ナビバーは真、それ以外はエリアごとに判定する。
- 触るとき: 見えていない機能の表示判定を変えるとき。
- 呼び出し先: `CustomizableUIInternal.widgetIsLikelyVisible()`

## getLocalizedProperty()
- 位置: L6878-6885
- 役割: 公開 API。ウィジェットの文字列を取得する。内部実装へ転送し、非推奨として扱う。
- 触るとき: 組み込みボタンが独自の DOM を作るときに旧来の文字列を取得するとき。新規の文字列は Fluent を使う。
- 呼び出し先: `CustomizableUIInternal.getLocalizedProperty()`

## addShortcut()
- 位置: L6896-6898
- 役割: 公開 API。ショートカットの表示用文字列を対象ノードの shortcut 属性へ設定する。内部実装へ転送する。
- 触るとき: メニュー項目からボタンへショートカット表示を引き継ぐとき。
- 呼び出し先: `CustomizableUIInternal.addShortcut()`

## hidePanelForNode()
- 位置: L6905-6907
- 役割: 公開 API。ノードを含むパネルを閉じる。内部実装へ転送する。
- 触るとき: ボタン操作の後でパネルを閉じたいとき。
- 呼び出し先: `CustomizableUIInternal.hidePanelForNode()`

## isSpecialWidget()
- 位置: L6914-6916
- 役割: 公開 API。spring、spacer、separator などの特殊ウィジェットかを返す。内部実装へ転送する。
- 触るとき: 特殊ウィジェットを通常のボタンと区別したいとき。
- 呼び出し先: `CustomizableUIInternal.isSpecialWidget()`

## isWebExtensionWidget()
- 位置: L6929-6935
- 役割: ウィジェットが拡張機能由来かを返す。作成前や破棄後は ID の -browser-action 接尾辞で判定する。
- 触るとき: 拡張機能のボタンを AREA_ADDONS に入れる判断や、拡張機能用の例外を追うとき。
- 呼び出し先: `CustomizableUI.getWidget()`, `aWidgetId.endsWith()`
- 参照: `widget?.webExtension`

## addPanelCloseListeners()
- 位置: L6944-6946
- 役割: 公開 API。パネルに閉じるための監視を付ける。内部実装へ転送する。
- 触るとき: メニューパネルやオーバーフローの実装で閉じ処理を付けるとき。
- 呼び出し先: `CustomizableUIInternal.addPanelCloseListeners()`

## removePanelCloseListeners()
- 位置: L6955-6957
- 役割: 公開 API。パネルの閉じる監視を外す。内部実装へ転送する。
- 触るとき: パネルを破棄するときの後始末をするとき。
- 呼び出し先: `CustomizableUIInternal.removePanelCloseListeners()`

## onWidgetDrag()
- 位置: L6967-6969
- 役割: カスタマイズモード専用。ウィジェットがエリアへドラッグされていることをリスナーへ通知する。
- 触るとき: ドラッグ中の表示をリスナーに伝える処理を変えるとき。
- 呼び出し先: `CustomizableUIInternal.notifyListeners()`

## notifyStartCustomizing()
- 位置: L6977-6979
- 役割: カスタマイズモード専用。ウィンドウがカスタマイズを開始したことをリスナーへ通知する。
- 触るとき: カスタマイズ開始時の処理をリスナーに頼むとき。
- 呼び出し先: `CustomizableUIInternal.notifyListeners()`

## notifyEndCustomizing()
- 位置: L6987-6989
- 役割: カスタマイズモード専用。ウィンドウがカスタマイズを終了したことをリスナーへ通知する。
- 触るとき: カスタマイズ終了時の後始末の流れを追うとき。
- 呼び出し先: `CustomizableUIInternal.notifyListeners()`

## dispatchToolboxEvent()
- 位置: L7003-7005
- 役割: カスタマイズモード専用。ツールボックスにカスタムイベントを送る。内部実装へ転送する。
- 触るとき: カスタマイズモードの状態を各ツールボックスへ伝えるとき。
- 呼び出し先: `CustomizableUIInternal.dispatchToolboxEvent()`

## isAreaOverflowable()
- 位置: L7015-7020
- 役割: エリアがツールバーかつ overflowable かを返す。未知のエリアは偽。
- 触るとき: ボタンがはみ出して格納される対象のエリアかを判断するとき。
- 呼び出し先: `area.get()`, `gAreas.get()`
- 参照: `this.TYPE_TOOLBAR`

## getPlaceForItem()
- 位置: L7033-7048
- 役割: 要素の祖先をたどり、ツールバー、オーバーフローパネル、パレットのどれに属するかを文字列で返す。
- 触るとき: コンテキストメニューやラベルを置き場所で変えるとき。
- 参照: `CustomizableUI.AREA_FIXED_OVERFLOW_PANEL`, `node.id`, `node.localName`, `node.parentNode`

## isBuiltinToolbar()
- 位置: L7056-7058
- 役割: 指定 ID が組み込みツールバーかを返す。
- 触るとき: 組み込みかどうかで扱いを分けるとき。
- 呼び出し先: `CustomizableUIInternal.builtinToolbars.has()`

## createSpecialWidget()
- 位置: L7070-7072
- 役割: 公開 API。spring などの特殊要素を作る。内部実装へ転送する。
- 触るとき: ツールバーにスペーサーを追加するとき。
- 呼び出し先: `CustomizableUIInternal.createSpecialWidget()`

## fillSubviewFromMenuItems()
- 位置: L7082-7183
- 役割: メニュー項目を、サブビュー用のボタンやセパレーターに変換して追加する。非表示の項目は飛ばし、重複や先頭の区切りも除く。クリックやコマンドは元の項目へ転送し、テレメトリは元のイベントだけを数える。
- 触るとき: メニューの項目をパネルのサブビューに写すとき、またはサブビューの項目が元のメニューと違う動きをするとき。
- 呼び出し先: `aSubview.appendChild()`, `doc.createDocumentFragment()`, `fragment.appendChild()`, `menuChild.getAttribute()`
- 条件付き依存: `if (menuChild.localName == "menuseparator")` → `doc.createXULElement()`
- 条件付き依存: `if (menuChild.localName == "menuitem")` → `doc.createXULElement()`
- 条件付き依存: `if (menuChild.localName == "menuitem")` → `CustomizableUI.addShortcut()`
- 条件付き依存: `if (menuChild.localName == "menuitem")` → `item.hasAttribute()`
- 条件付き依存: `if (!item.hasAttribute("onclick"))` → `subviewItem.addEventListener()`
- 条件付き依存: `if (!item.hasAttribute("onclick"))` → `lazy.BrowserUsageTelemetry.ignoreEvent()`
- 条件付き依存: `if (!item.hasAttribute("onclick"))` → `item.dispatchEvent()`
- 条件付き依存: `if (!item.hasAttribute("oncommand"))` → `subviewItem.addEventListener()`
- 条件付き依存: `if (!item.hasAttribute("oncommand"))` → `doc.createEvent()`
- 条件付き依存: `if (!item.hasAttribute("oncommand"))` → `newEvent.initCommandEvent()`
- 条件付き依存: `if (!item.hasAttribute("oncommand"))` → `lazy.BrowserUsageTelemetry.ignoreEvent()`
- 条件付き依存: `if (!item.hasAttribute("oncommand"))` → `item.dispatchEvent()`
- 条件付き依存: `if (attrVal !== null)` → `subviewItem.setAttribute()`
- 条件付き依存: `if (menuChild.localName == "menuitem")` → `subviewItem.classList.add()`
- 条件付き依存: `if (l10nId)` → `doc.l10n.setAttributes()`
- 参照: `aSubview.documentGlobal.document`, `doc.documentGlobal.PointerEvent`, `event.altKey`, `event.bubbles`, `event.cancelable`, `event.ctrlKey`, `event.detail`, `event.metaKey`, `event.shiftKey`, `event.sourceEvent`, `event.type`, `event.view`, `fragment.lastElementChild`, `fragment.lastElementChild.localName`, `menuChild.hidden`, `menuChild.localName`

## clearSubview()
- 位置: L7191-7202
- 役割: サブビューの子要素をすべて消す。描画の負担を減らすため、いったん親から外してから消す。
- 触るとき: サブビューの内容を作り直す前に中身を空にするとき。
- 呼び出し先: `aSubview.firstChild.remove()`, `parent.appendChild()`, `parent.removeChild()`
- 参照: `aSubview.firstChild`, `aSubview.parentNode`

## handleNewBrowserWindow()
- 位置: L7210-7212
- 役割: 公開 API。新しいブラウザウィンドウの初期化を内部実装へ転送する。
- 触るとき: ウィンドウ作成時のツールバー準備を追うとき。
- 呼び出し先: `CustomizableUIInternal.handleNewBrowserWindow()`

## getCustomizationTarget()
- 位置: L7228-7230
- 役割: 公開 API。customization target を返す。内部実装へ転送する。
- 触るとき: customizable 要素の実際の子の置き場所を知りたいとき。
- 呼び出し先: `CustomizableUIInternal.getCustomizationTarget()`

## getTestOnlyInternalProp()
- 位置: L7242-7265
- 役割: テスト自動化の実行中だけ、内部の状態(gAreas、gPlacements など)を読み出す。それ以外は null を返す。
- 触るとき: テストで内部状態を確かめるとき。本番コードから使わない。
- 参照: `Cu.isInAutomation`

## setTestOnlyInternalProp()
- 位置: L7279-7294
- 役割: テスト自動化の実行中だけ、保存状態・版・dirty の値を書き換える。それ以外は何もしない。
- 触るとき: テストで保存状態や版を差し替えるとき。
- 参照: `Cu.isInAutomation`

## WidgetGroupWrapper()
- 位置: L7311-7391
- 役割: API で作られたウィジェット群(全ウィンドウのインスタンス)へのラッパー。ID や無効化状態を読み書きし、ウィンドウごとのラッパーを返す。
- 触るとき: アドオンなどに返すウィジェットラッパーの振る舞いを変えるとき。
- 呼び出し先: `Array.from()`, `CustomizableUIInternal.getPlacementOfWidget()`, `Object.freeze()`, `areaProps.get()`, `gAreas.get()`, `gBuildAreas.get()`, `this.__defineGetter__()`, `this.__defineSetter__()`, `this.forWindow()`
- 参照: `CustomizableUI.PROVIDER_API`, `aWidget.disabled`, `aWidget.id`, `aWidget.instances`, `instance.disabled`, `node.documentGlobal`, `placement.area`, `this.forWindow`, `this.isGroup`

## WidgetGroupWrapper_forWindow()
- 位置: L7342-7365
- 役割: WidgetGroupWrapper の内部関数。ウィンドウ用のラッパーを作って単一ウィンドウのキャッシュに入れる。インスタンスが無ければノードを作る。
- 触るとき: ウィンドウごとのラッパーがずれる、または作られない問題を調べるとき。
- 呼び出し先: `aWidget.instances.get()`, `gSingleWrapperCache.has()`, `wrapperMap.has()`, `wrapperMap.set()`
- 条件付き依存: `if (!gSingleWrapperCache.has(aWindow))` → `gSingleWrapperCache.set()`
- 条件付き依存: `if (!(!gSingleWrapperCache.has(aWindow)))` → `gSingleWrapperCache.get()`
- 条件付き依存: `if (wrapperMap.has(aWidget.id))` → `wrapperMap.get()`
- 条件付き依存: `if (!instance)` → `CustomizableUIInternal.buildWidgetNode()`
- 参照: `aWidget.id`, `aWindow.document`

## WidgetSingleWrapper()
- 位置: L7397-7453
- 役割: 1 つのウィンドウのウィジェットノードを包む。ラベルやツールチップは現在のノードから読み、anchor は配置先のエリアや属性から決める。
- 触るとき: ウィジェットのアンカー(パネルの基準要素)がずれる問題を調べるとき。
- 呼び出し先: `CustomizableUIInternal.getPlacementOfWidget()`, `Object.freeze()`, `aNode.getAttribute()`, `this.__defineGetter__()`, `this.__defineSetter__()`
- 条件付き依存: `if (placement)` → `gAreas.get(placement.area).get()`
- 条件付き依存: `if (placement)` → `gAreas.get()`
- 条件付き依存: `if (!anchorId)` → `aNode.getAttribute()`
- 条件付き依存: `if (anchorId)` → `aNode.ownerDocument.getElementById()`
- 参照: `CustomizableUI.PROVIDER_API`, `aNode.disabled`, `aNode.lastElementChild`, `aWidget.id`, `aWidget.type`, `placement.area`, `this.isGroup`, `this.node`, `this.provider`

## XULWidgetGroupWrapper()
- 位置: L7463-7517
- 役割: XUL 側で作られたウィジェット群のラッパー。ID と種別を固定し、ウィンドウごとのラッパーを返す。
- 触るとき: XUL 提供のボタンの扱いを変えるとき。
- 呼び出し先: `Array.from()`, `CustomizableUIInternal.getPlacementOfWidget()`, `Object.freeze()`, `areaProps.get()`, `gAreas.get()`, `this.__defineGetter__()`, `this.forWindow()`
- 参照: `CustomizableUI.PROVIDER_XUL`, `placement.area`, `this.forWindow`, `this.id`, `this.isGroup`, `this.provider`, `this.type`, `this.webExtension`

## XULWidgetGroupWrapper_forWindow()
- 位置: L7471-7500
- 役割: XULWidgetGroupWrapper の内部関数。ウィンドウの document やパレットからノードを探してラッパーを作る。
- 触るとき: XUL ボタンのノードが見つからない問題を調べるとき。
- 呼び出し先: `aWindow.document.getElementById()`, `gSingleWrapperCache.has()`, `wrapperMap.has()`, `wrapperMap.set()`
- 条件付き依存: `if (!gSingleWrapperCache.has(aWindow))` → `gSingleWrapperCache.set()`
- 条件付き依存: `if (!(!gSingleWrapperCache.has(aWindow)))` → `gSingleWrapperCache.get()`
- 条件付き依存: `if (wrapperMap.has(aWidgetId))` → `wrapperMap.get()`
- 条件付き依存: `if (!instance)` → `aWindow.gNavToolbox.palette.getElementsByAttribute()`
- 参照: `aWindow.document`

## XULWidgetSingleWrapper()
- 位置: L7523-7595
- 役割: XUL ボタン 1 つを包むラッパー。ノードは弱参照で保ち、切り離されたら findXULWidgetInWindow で探し直す。anchor と overflowed を提供する。
- 触るとき: XUL ボタンのノードが古いまま使われる問題や、アンカーがずれる問題を調べるとき。
- 呼び出し先: `Cu.getWeakReference()`, `CustomizableUIInternal.getPlacementOfWidget()`, `Object.freeze()`, `node.getAttribute()`, `node.ownerDocument.getElementById()`, `this.__defineGetter__()`, `weakDoc.get()`
- 条件付き依存: `if (doc)` → `CustomizableUIInternal.findXULWidgetInWindow()`
- 条件付き依存: `if (placement)` → `gAreas.get(placement.area).get()`
- 条件付き依存: `if (placement)` → `gAreas.get()`
- 条件付き依存: `if (!anchorId && node)` → `node.getAttribute()`
- 参照: `CustomizableUI.PROVIDER_XUL`, `aNode.documentGlobal.gNavToolbox`, `aNode.isConnected`, `aNode.parentNode`, `doc.defaultView`, `placement.area`, `this.id`, `this.isGroup`, `this.node`, `this.provider`, `this.type`, `toolbox.palette`

## OverflowableToolbar.constructor()
- 位置: L7764-7787
- 役割: ツールバーに overflowable を付け、既定の格納先リストを設定する。window の起動が済んでいれば init を呼び、未済ならその通知を待つ。
- 触るとき: ナビバーのように、幅が足りないとボタンをパネルへ逃がすツールバーを作る流れを調べるとき。
- 呼び出し先: `CustomizableUI.getCustomizationTarget()`, `doc.getElementById()`, `this.#toolbar.getAttribute()`, `this.#toolbar.setAttribute()`
- 条件付き依存: `if (window.gBrowserInit.delayedStartupFinished)` → `this.init()`
- 条件付き依存: `if (!(window.gBrowserInit.delayedStartupFinished))` → `Services.obs.addObserver()`
- 参照: `this.#defaultList`, `this.#defaultList._customizationTarget`, `this.#target`, `this.#target.parentNode`, `this.#toolbar`, `this.#toolbar.documentGlobal`, `this.#toolbar.ownerDocument`, `window.gBrowserInit.delayedStartupFinished`
- XPCOM: `Services.obs`

## OverflowableToolbar.init()
- 位置: L7794-7820
- 役割: リサイズ、カスタマイズ開始・終了、既定のオーバーフローボタンとパネルのイベントを接続し、最初の溢れ確認を行う。
- 触るとき: ウィンドウ起動後にオーバーフローの監視が始まらない問題を調べるとき。
- 呼び出し先: `CustomizableUI.addListener()`, `CustomizableUIInternal.addPanelCloseListeners()`, `doc.getElementById()`, `this.#checkOverflow()`, `this.#defaultListButton.addEventListener()`, `this.#defaultListPanel.addEventListener()`, `this.#toolbar.getAttribute()`, `window.addEventListener()`, `window.gNavToolbox.addEventListener()`
- 参照: `doc.defaultView`, `this.#defaultListButton`, `this.#defaultListPanel`, `this.#initialized`, `this.#toolbar.ownerDocument`

## OverflowableToolbar.uninit()
- 位置: L7826-7850
- 役割: init で付けたイベント監視とリスナーを外す。初期化前なら通知の監視だけ外す。
- 触るとき: ウィンドウを閉じた後にリスナーが残る問題を調べるとき。
- 呼び出し先: `CustomizableUI.removeListener()`, `CustomizableUIInternal.removePanelCloseListeners()`, `this.#defaultListButton.removeEventListener()`, `this.#defaultListPanel.removeEventListener()`, `this.#disable()`, `this.#toolbar.removeAttribute()`, `window.gNavToolbox.removeEventListener()`, `window.removeEventListener()`
- 条件付き依存: `if (!this.#initialized)` → `Services.obs.removeObserver()`
- 条件付き依存: `if (!this.#initialized)` → `Services.prefs.removeObserver()`
- 参照: `this.#defaultListPanel`, `this.#initialized`, `this.#toolbar.documentGlobal`
- XPCOM: `Services.obs` / `Services.prefs`

## OverflowableToolbar.show()
- 位置: L7859-7926
- 役割: 既定のオーバーフローパネルを開く。開く直前に閉じられた場合は再度開き直し、表示後に解決する Promise を返す。
- 触るとき: ドラッグやクリックでオーバーフローパネルが開かない、またはすぐ閉じる問題を調べるとき。
- 呼び出し先: `Services.tm.dispatchToMainThread()`, `contextMenu.addEventListener()`, `doc.getElementById()`, `mainView.getAttribute()`, `multiview.getAttribute()`, `openPanel()`, `this.#defaultListPanel.addEventListener()`, `this.#defaultListPanel.querySelector()`
- 条件付き依存: `if (this.#defaultListPanel.state == "open")` → `Promise.resolve()`
- 参照: `this.#defaultListButton.icon`, `this.#defaultListPanel.hidden`, `this.#defaultListPanel.ownerDocument`, `this.#defaultListPanel.state`
- XPCOM: `Services.tm`

## openPanel()
- 位置: L7891-7922
- 役割: show の内部関数。コンテキストメニューの更新を仕込み、PanelMultiView.openPopup でパネルをアンカーに対して開く。
- 触るとき: パネルを開いた直後の編集メニューの表示状態がおかしいときに見る。
- 呼び出し先: `doc.defaultView.updateEditUIVisibility()`, `lazy.PanelMultiView.openPopup()`, `this.#defaultListPanel.addEventListener()`
- 条件付き依存: `if (!popupshown)` → `openPanel()`
- 参照: `this.#defaultListButton`, `this.#defaultListButton.open`, `this.#defaultListPanel`

## OverflowableToolbar.isHandlingOverflow()
- 位置: L7933-7935
- 役割: 溢れ確認(#checkOverflow)が実行中かを、ハンドルの有無で返す。
- 触るとき: 溢れ確認が重なって動いているかを他の処理から知りたいとき。
- 参照: `this.#checkOverflowHandle`

## OverflowableToolbar.findOverflowedInsertionPoints()
- 位置: L7949-8014
- 役割: 溢れたボタンの位置を考慮して、新しいボタンを入れる親要素と直後のノードを決める。溢れたボタンより前なら格納先リストに入れる。
- 触るとき: 溢れた状態でボタンを追加や移動したとき、どこへ入るかがずれる問題を調べるとき。
- 呼び出し先: `CustomizableUI.isWebExtensionWidget()`, `aNode.getAttribute()`, `gPlacements.get()`, `placements.indexOf()`
- 条件付き依存: `if (loopIndex > nodeIndex)` → `this.#toolbar.ownerDocument.getElementById()`
- 条件付き依存: `if (loopIndex > nodeIndex)` → `this.#overflowedInfo.has()`
- 条件付き依存: `if (!(loopIndex > nodeIndex))` → `this.#overflowedInfo.has()`
- 参照: `aNode.id`, `nextNode.parentNode`, `nextNode.parentNode.localName`, `nextNode.parentNode.parentNode`, `placements.length`, `this.#defaultList`, `this.#overflowedInfo.size`, `this.#target`, `this.#toolbar.id`, `this.#webExtList`

## OverflowableToolbar.getContainerFor()
- 位置: L8028-8035
- 役割: ボタンの現在の親を返す。溢れていれば格納先リスト、拡張機能ボタンなら拡張機能用リスト、そうでなければツールバーの本体。
- 触るとき: 溢れたボタンの親要素を取り直す処理を変えるとき。
- 呼び出し先: `aNode.getAttribute()`
- 条件付き依存: `if (aNode.getAttribute("overflowedItem") == "true")` → `CustomizableUI.isWebExtensionWidget()`
- 参照: `aNode.id`, `this.#defaultList`, `this.#target`, `this.#webExtList`

## OverflowableToolbar.#onOverflow()
- 位置: async L8044-8115
- 役割: ツールバーの右端から順に、はみ出している子を格納先リストへ移す。移した幅を記録し、通知を出す。
- 触るとき: ボタンが溢れてパネルへ移る順番や条件を変えるとき。
- 呼び出し先: `child.getAttribute()`, `this.#getOverflowInfo()`, `this.#toolbar.getAttribute()`, `win.UpdateUrlbarSearchSplitterState()`
- 条件付き依存: `if (win.closed || this.#checkOverflowHandle != checkOverflowHandle)` → `lazy.log.debug()`
- 条件付き依存: `if (child.getAttribute("overflows") != "false")` → `this.#overflowedInfo.set()`
- 条件付き依存: `if (child.getAttribute("overflows") != "false")` → `win.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if (!childWidth)` → `this.#hiddenOverflowedNodes.add()`
- 条件付き依存: `if (child.getAttribute("overflows") != "false")` → `child.setAttribute()`
- 条件付き依存: `if (child.getAttribute("overflows") != "false")` → `CustomizableUIInternal.ensureButtonContextMenu()`
- 条件付き依存: `if (child.getAttribute("overflows") != "false")` → `CustomizableUIInternal.notifyListeners()`
- 条件付き依存: `if (child.getAttribute("overflows") != "false")` → `CustomizableUI.isWebExtensionWidget()`
- 条件付き依存: `if (webExtList && CustomizableUI.isWebExtensionWidget(child.id))` → `child.setAttribute()`
- 条件付き依存: `if (webExtList && CustomizableUI.isWebExtensionWidget(child.id))` → `webExtList.insertBefore()`
- 条件付き依存: `if (!(webExtList && CustomizableUI.isWebExtensionWidget(child.id)))` → `child.setAttribute()`
- 条件付き依存: `if (!(webExtList && CustomizableUI.isWebExtensionWidget(child.id)))` → `this.#defaultList.insertBefore()`
- 条件付き依存: `if (!(webExtList && CustomizableUI.isWebExtensionWidget(child.id)))` → `CustomizableUI.isSpecialWidget()`
- 条件付き依存: `if (!CustomizableUI.isSpecialWidget(child.id) && childWidth)` → `this.#toolbar.setAttribute()`
- 参照: `child.id`, `child.previousElementSibling`, `this.#checkOverflowHandle`, `this.#defaultList.firstElementChild`, `this.#defaultListButton.id`, `this.#enabled`, `this.#target`, `this.#target.documentGlobal`, `this.#target.lastElementChild`, `this.#toolbar`, `this.#webExtList`, `webExtList.firstElementChild`, `win.closed`

## OverflowableToolbar.#getOverflowInfo()
- 位置: async L8135-8196
- 役割: ツールバーの利用可能な幅と、子要素の合計幅をレイアウトのフラッシュ後に計算し、溢れているかを返す。
- 触るとき: 溢れの判定がずれる、またはレイアウトの再計算で誤判定する問題を調べるとき。
- 呼び出し先: `Math.ceil()`, `Math.floor()`, `Math.max()`, `getInlineSize()`, `lazy.log.debug()`, `parseFloat()`, `sumChildrenInlineSize()`, `win.getComputedStyle()`, `win.promiseDocumentFlushed()`
- 参照: `style.paddingLeft`, `style.paddingRight`, `this.#target`, `this.#target.documentGlobal`, `this.#toolbar`

## getInlineSize()
- 位置: L8136-8138
- 役割: 要素の横幅(getBoundingClientRect)を返す。
- 触るとき: 幅の計測方法を変えるとき。
- 呼び出し先: `aElement.getBoundingClientRect()`
- 参照: `aElement.getBoundingClientRect().width`

## sumChildrenInlineSize()
- 位置: L8140-8157
- 役割: 表示されている子要素の幅と余白を合計する。ポップアップや絶対配置の要素は除く。
- 触るとき: ツールバーの中身の幅が過小・過大に出る問題を調べるとき。
- 呼び出し先: `parseFloat()`, `win.XULPopupElement.isInstance()`, `win.getComputedStyle()`
- 条件付き依存: `if (child != aExceptChild)` → `getInlineSize()`
- 参照: `aParent.children`, `style.display`, `style.marginLeft`, `style.marginRight`, `style.position`

## OverflowableToolbar.#moveItemsBackToTheirOrigin()
- 位置: async L8215-8312
- 役割: 溢れたボタンを、幅に余裕があれば元の位置へ戻す。全件戻す指定もできる。戻せない場合や、途中でレイアウトが変わった場合は止まる。
- 触るとき: 溢れから戻るボタンの順番や、戻る条件の幅を調べるとき。
- 呼び出し先: `Array.from()`, `CustomizableUI.isSpecialWidget()`, `CustomizableUIInternal.ensureButtonContextMenu()`, `CustomizableUIInternal.notifyListeners()`, `child.removeAttribute()`, `defaultListItems.every()`, `gPlacements.get()`, `lazy.PanelMultiView.getViewNode()`, `lazy.log.debug()`, `placements.indexOf()`, `this.#hiddenOverflowedNodes.has()`, `this.#overflowedInfo.delete()`, `this.#overflowedInfo.entries()`, `this.#target.getElementsByAttribute()`, `win.UpdateUrlbarSearchSplitterState()`
- 条件付き依存: `if (!child)` → `this.#overflowedInfo.delete()`
- 条件付き依存: `if (!totalAvailWidth)` → `this.#getOverflowInfo()`
- 条件付き依存: `if (win.closed || this.#checkOverflowHandle != checkOverflowHandle)` → `lazy.log.debug()`
- 条件付き依存: `if (totalAvailWidth <= minSize)` → `lazy.log.debug()`
- 条件付き依存: `if (beforeNode && this.#target == beforeNode.parentElement)` → `this.#target.insertBefore()`
- 条件付き依存: `if (!inserted)` → `this.#target.appendChild()`
- 条件付き依存: `if ( defaultListItems.every( item => CustomizableUI.isSpecialWidget(item.id) || this.#hiddenOverflowedNodes.has(item) ) )` → `this.#toolbar.removeAttribute()`
- 参照: `beforeNode.parentElement`, `child.id`, `item.id`, `overflowedItemStack.length`, `placements.length`, `this.#checkOverflowHandle`, `this.#defaultList.children`, `this.#target`, `this.#target.documentGlobal`, `this.#target.ownerDocument`, `this.#toolbar.id`, `win.closed`

## OverflowableToolbar.#checkOverflow()
- 位置: async L8331-8360
- 役割: 溢れの有無を確かめ、溢れていれば溢れを格納し、無ければ戻す。古い確認は途中で打ち切る。
- 触るとき: リサイズや並べ替えの後に溢れの状態が追従しないときに見る。
- 呼び出し先: `lazy.log.debug()`, `this.#getOverflowInfo()`, `win.document.documentElement.hasAttribute()`
- 条件付き依存: `if (isOverflowing)` → `this.#onOverflow()`
- 条件付き依存: `if (!(isOverflowing))` → `this.#moveItemsBackToTheirOrigin()`
- 参照: `this.#checkOverflowHandle`, `this.#enabled`, `this.#target.documentGlobal`, `win.closed`

## OverflowableToolbar.#disable()
- 位置: L8366-8372
- 役割: 進行中の溢れ確認を打ち切り、溢れたボタンを全部ツールバーへ戻して無効にする。
- 触るとき: カスタマイズ開始時にボタンが戻らない問題を調べるとき。
- 呼び出し先: `this.#moveItemsBackToTheirOrigin()`
- 参照: `this.#checkOverflowHandle`, `this.#enabled`

## OverflowableToolbar.#enable()
- 位置: L8379-8382
- 役割: 有効に戻し、溢れ確認を行う。
- 触るとき: カスタマイズ終了後に溢れの監視が再開しない問題を調べるとき。
- 呼び出し先: `this.#checkOverflow()`
- 参照: `this.#enabled`

## OverflowableToolbar.#showWithTimeout()
- 位置: L8388-8402
- 役割: パネルを開き、500 ミリ秒後にマウスが乗っていなければ閉じるタイマーを設定する。
- 触るとき: ドラッグで開いたパネルが閉じるタイミングを変えるとき。
- 呼び出し先: `this.#defaultListPanel.firstElementChild.matches()`, `this.show()`, `this.show().then()`, `window.setTimeout()`
- 条件付き依存: `if (this.#hideTimeoutId)` → `window.clearTimeout()`
- 条件付き依存: `if (!this.#defaultListPanel.firstElementChild.matches(":hover"))` → `lazy.PanelMultiView.hidePopup()`
- 参照: `this.#defaultListPanel`, `this.#hideTimeoutId`, `this.#toolbar.documentGlobal`

## OverflowableToolbar.#webExtList()
- 位置: L8413-8427
- 役割: 拡張機能ボタンの格納先を、初回に統合拡張パネルから取得してキャッシュする。属性が無ければ例外。
- 触るとき: 統合拡張機能パネルで拡張機能ボタンの格納先が見つからない問題を調べるとき。
- 条件付き依存: `if (!this.#webExtListRef)` → `this.#toolbar.getAttribute()`
- 条件付き依存: `if (!this.#webExtListRef)` → `panel.querySelector()`
- 参照: `this.#toolbar.documentGlobal`, `this.#toolbar.id`, `this.#webExtListRef`, `win.gUnifiedExtensions`

## OverflowableToolbar.#isOverflowList()
- 位置: L8436-8438
- 役割: 指定ノードが既定の格納先リストか拡張機能の格納先リストかを返す。
- 触るとき: ノードが溢れ先かどうかを判定するとき。
- 参照: `this.#defaultList`, `this.#webExtList`

## OverflowableToolbar.#onClickDefaultListButton()
- 位置: L8449-8459
- 役割: 溢れボタンのクリックで、パネルが開いていれば閉じ、そうでなければ開く。
- 触るとき: 溢れボタンのクリック挙動を変えるとき。
- 条件付き依存: `if (this.#defaultListButton.open)` → `lazy.PanelMultiView.hidePopup()`
- 条件付き依存: `if ( this.#defaultListPanel.state != "hiding" && !this.#defaultListButton.disabled )` → `this.show()`
- 参照: `this.#defaultListButton.disabled`, `this.#defaultListButton.open`, `this.#defaultListPanel`, `this.#defaultListPanel.state`

## OverflowableToolbar.#onPanelHiding()
- 位置: L8467-8485
- 役割: 既定のパネルが閉じるときに、ボタンの open 状態と編集メニューの表示、コンテキストメニューの監視を片付ける。
- 触るとき: パネルを閉じた後に編集コマンドの状態がおかしい問題を調べるとき。
- 呼び出し先: `doc.defaultView.updateEditUIVisibility()`, `this.#defaultListPanel.getAttribute()`, `this.#defaultListPanel.removeEventListener()`
- 条件付き依存: `if (contextMenuId)` → `doc.getElementById()`
- 条件付き依存: `if (contextMenuId)` → `contextMenu.removeEventListener()`
- 参照: `aEvent.target`, `aEvent.target.ownerDocument`, `this.#defaultListButton.open`, `this.#defaultListPanel`

## OverflowableToolbar.#onResize()
- 位置: L8493-8499
- 役割: ウィンドウのリサイズで溢れ確認を行う。バブルで届いたリサイズは無視する。
- 触るとき: ウィンドウ幅の変更に対する溢れの反応を変えるとき。
- 呼び出し先: `this.#checkOverflow()`
- 参照: `aEvent.currentTarget`, `aEvent.target`

## OverflowableToolbar.onWidgetBeforeDOMChange()
- 位置: L8505-8530
- 役割: 溢れたボタンが API から移動または削除される前に、後続ボタンの最小幅を更新する。
- 触るとき: 溢れた状態でボタンを外したときに、残りが戻るタイミングを調べるとき。
- 呼び出し先: `this.#isOverflowList()`, `this.#overflowedInfo.set()`
- 条件付き依存: `if (aNode.previousElementSibling)` → `this.#overflowedInfo.get()`
- 参照: `aNode.nextElementSibling`, `aNode.previousElementSibling`, `aNode.previousElementSibling.id`, `nextItem.id`, `nextItem.nextElementSibling`, `this.#enabled`

## OverflowableToolbar.onWidgetAfterDOMChange()
- 位置: L8532-8597
- 役割: ボタンの移動や削除の後に、溢れ・戻りの状態を整え、溢れ確認を再度行う。溢れ先に入ったボタンには overflowedItem を付ける。
- 触るとき: ボタンを追加・移動した後に溢れの表示や通知が正しく出るかを調べるとき。
- 呼び出し先: `this.#checkOverflow()`, `this.#isOverflowList()`, `this.#overflowedInfo.has()`
- 条件付き依存: `if (nowOverflowed)` → `this.#overflowedInfo.get()`
- 条件付き依存: `if (nowOverflowed)` → `this.#overflowedInfo.set()`
- 条件付き依存: `if (nowOverflowed)` → `aNode.setAttribute()`
- 条件付き依存: `if (nowOverflowed)` → `CustomizableUIInternal.ensureButtonContextMenu()`
- 条件付き依存: `if (nowOverflowed)` → `CustomizableUIInternal.notifyListeners()`
- 条件付き依存: `if (!nowOverflowed)` → `this.#overflowedInfo.delete()`
- 条件付き依存: `if (!nowOverflowed)` → `aNode.removeAttribute()`
- 条件付き依存: `if (!nowOverflowed)` → `CustomizableUIInternal.ensureButtonContextMenu()`
- 条件付き依存: `if (!nowOverflowed)` → `CustomizableUIInternal.notifyListeners()`
- 条件付き依存: `if (!nowOverflowed)` → `Array.from()`
- 条件付き依存: `if (!nowOverflowed)` → `this.#overflowedInfo.keys()`
- 条件付き依存: `if (!nowOverflowed)` → `collapsedWidgetIds.every()`
- 条件付き依存: `if (!nowOverflowed)` → `CustomizableUI.isSpecialWidget()`
- 条件付き依存: `if (collapsedWidgetIds.every(w => CustomizableUI.isSpecialWidget(w)))` → `this.#toolbar.removeAttribute()`
- 条件付き依存: `if (aNode.previousElementSibling)` → `this.#overflowedInfo.get()`
- 条件付き依存: `if (aNode.previousElementSibling)` → `this.#overflowedInfo.set()`
- 参照: `aNode.id`, `aNode.parentNode`, `aNode.previousElementSibling`, `aNode.previousElementSibling.id`, `sourceOfMinSize.id`, `this.#defaultListButton.id`, `this.#enabled`, `this.#target`

## OverflowableToolbar.isInOverflowList()
- 位置: L8602-8604
- 役割: ノードの親が既定の格納先リストかを返す。
- 触るとき: ボタンが溢れ先にあるかを判定する箇所を追うとき。
- 参照: `node.parentNode`, `this.#defaultList`

## OverflowableToolbar.observe()
- 位置: L8610-8620
- 役割: ウィンドウの起動完了通知を受けたとき、init を呼んで遅延初期化を完了させる。
- 触るとき: 起動時に溢れの監視が始まるタイミングを変えるとき。
- 条件付き依存: `if ( aTopic == "browser-delayed-startup-finished" && aSubject == this.#toolbar.documentGlobal )` → `Services.obs.removeObserver()`
- 条件付き依存: `if ( aTopic == "browser-delayed-startup-finished" && aSubject == this.#toolbar.documentGlobal )` → `this.init()`
- 参照: `this.#toolbar.documentGlobal`
- XPCOM: `Services.obs`

## OverflowableToolbar.handleEvent()
- 位置: L8626-8675
- 役割: リサイズ、マウス操作、キー操作、ドラッグ、カスタマイズの開始と終了、パネルの閉じる各イベントを、対応する非公開メソッドへ振り分ける。
- 触るとき: 溢れツールバーの操作イベントの対応を追うとき。
- 呼び出し先: `lazy.PanelMultiView.hidePopup()`, `this.#disable()`, `this.#enable()`, `this.#onPanelHiding()`, `this.#onResize()`
- 条件付き依存: `if (aEvent.target == this.#defaultListButton)` → `this.#onClickDefaultListButton()`
- 条件付き依存: `if (!(aEvent.target == this.#defaultListButton))` → `lazy.PanelMultiView.hidePopup()`
- 条件付き依存: `if ( aEvent.target == this.#defaultListButton && (aEvent.key == " " || aEvent.key == "Enter") )` → `this.#onClickDefaultListButton()`
- 条件付き依存: `if (this.#enabled)` → `this.#showWithTimeout()`
- 参照: `aEvent.button`, `aEvent.key`, `aEvent.target`, `aEvent.type`, `this.#defaultListButton`, `this.#defaultListPanel`, `this.#enabled`
