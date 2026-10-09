# browser/components/customizableui/ToolbarContextMenu.sys.mjs

source: browser/components/customizableui/ToolbarContextMenu.sys.mjs
source-hash: c87bd45858c9f10a64551cf5a5572c0ceb5507d0
lines: 621

## <module>
- 役割: ツールバーの右クリックメニュー（toolbar-context-menu）の項目の表示・状態・コマンドを扱う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## updateDownloadsAutoHide()
- 位置: L47-62
- 役割: ダウンロードボタンを右クリックしたときだけ自動非表示のチェック項目を出し、現在の設定を反映する。
- 触るとき: ダウンロードボタンの自動非表示項目の表示条件や初期値を変えるとき。
- 呼び出し先: `["downloads-button", "wrapper-downloads-button"].includes()`, `checkbox.toggleAttribute()`, `document.getElementById()`
- 参照: `DownloadsButton.autoHideDownloadsButton`, `checkbox.hidden`, `popup.documentGlobal`, `popup.triggerNode`, `popup.triggerNode.id`

## onDownloadsAutoHideChange()
- 位置: L72-75
- 役割: チェック項目の変更を browser.download.autohideButton に書き込む。
- 触るとき: 自動非表示の設定の保存先を変えるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`, `event.target.hasAttribute()`
- XPCOM: `Services.prefs`

## updateDownloadsAlwaysOpenPanel()
- 位置: L88-103
- 役割: ダウンロードボタン上でだけ区切り線とパネル常時表示項目を出し、browser.download.alwaysOpenPanel を反映する。
- 触るとき: パネル常時表示項目の表示条件を変えるとき。
- 呼び出し先: `["downloads-button", "wrapper-downloads-button"].includes()`, `checkbox.toggleAttribute()`, `document.getElementById()`
- 参照: `checkbox.hidden`, `lazy.gAlwaysOpenPanel`, `popup.documentGlobal`, `popup.triggerNode`, `popup.triggerNode.id`, `separator.hidden`

## onDownloadsAlwaysOpenPanelChange()
- 位置: L113-116
- 役割: チェック項目の変更を browser.download.alwaysOpenPanel に書き込む。
- 触るとき: パネル常時表示の設定の保存先を変えるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`, `event.target.hasAttribute()`
- XPCOM: `Services.prefs`

## onViewToolbarsPopupShowing()
- 位置: L131-364
- 役割: 右クリックされた要素からツールバー項目を特定し、ツールバーの表示切替、移動・削除、タブバーやサイドバーの項目の表示を組み立て直す。
- 触るとき: 右クリック時にどの項目を出すか、またはツールバー切替や移動・削除の有効・無効の判定を変えるとき。
- 呼び出し先: `CustomizationHandler.isCustomizing()`, `Services.prefs.getBoolPref()`, `["tabbrowser-tabs", "sidebar-button"].includes()`, `deadItem.hasAttribute()`, `document .getElementById()`, `document .getElementById("toolbar-context-menu") .querySelectorAll()`, `document .getElementById("toolbar-context-menu") .querySelectorAll("[data-lazy-l10n-id]") .forEach()`, `document.getElementById()`, `document.l10n.setAttributes()`, `el.getAttribute()`, `el.removeAttribute()`, `el.setAttribute()`, `lazy.CustomizableUI.isSpecialWidget()`, `lazy.CustomizableUI.isWidgetRemovable()`, `moveToPanel.toggleAttribute()`, `popup.querySelector()`, `popup.querySelectorAll()`, `removeFromToolbar.toggleAttribute()`, `showFullScreenViewContextMenuItems()`, `toolbarItem?.classList.contains()`, `toolbarItem?.id.startsWith()`, `toolbarItem?.localName.includes()`
- 条件付き依存: `if (localName == "menupopup")` → `aEvent.preventDefault()`
- 条件付き依存: `if (localName == "menupopup")` → `aEvent.stopPropagation()`
- 条件付き依存: `if (parent)` → `parent.classList.contains()`
- 条件付き依存: `if (parent)` → `parent.getAttribute()`
- 条件付き依存: `if (deadItem.hasAttribute("toolbarId"))` → `popup.removeChild()`
- 条件付き依存: `if (!isVerticalTabStripMenu)` → `MozXULElement.insertFTLIfNeeded()`
- 条件付き依存: `if (!isVerticalTabStripMenu)` → `gNavToolbox.querySelectorAll()`
- 条件付き依存: `if (!isVerticalTabStripMenu)` → `toolbar.hasAttribute()`
- 条件付き依存: `if (toolbar.id == "PersonalToolbar")` → `BookmarkingUI.buildBookmarksToolbarSubmenu()`
- 条件付き依存: `if (toolbar.id == "PersonalToolbar")` → `popup.insertBefore()`
- 条件付き依存: `if (!(toolbar.id == "PersonalToolbar"))` → `document.createXULElement()`
- 条件付き依存: `if (!(toolbar.id == "PersonalToolbar"))` → `menuItem.setAttribute()`
- 条件付き依存: `if (!(toolbar.id == "PersonalToolbar"))` → `toolbar.getAttribute()`
- 条件付き依存: `if (!(toolbar.id == "PersonalToolbar"))` → `menuItem.toggleAttribute()`
- 条件付き依存: `if (!(toolbar.id == "PersonalToolbar"))` → `toolbar.hasAttribute()`
- 条件付き依存: `if (!(toolbar.id == "PersonalToolbar"))` → `popup.insertBefore()`
- 条件付き依存: `if (!(toolbar.id == "PersonalToolbar"))` → `menuItem.addEventListener()`
- 条件付き依存: `if (showTabStripItems)` → `document.getElementById()`
- 条件付き依存: `if (showTabStripItems)` → `gBrowser.allTabsSelected()`
- 条件付き依存: `if (showTabStripItems)` → `lazy.SessionStore.getLastClosedTabCount()`
- 条件付き依存: `if (showTabStripItems)` → `document .getElementById("History:UndoCloseTab") .toggleAttribute()`
- 条件付き依存: `if (showTabStripItems)` → `document .getElementById()`
- 条件付き依存: `if (showTabStripItems)` → `document.l10n.setArgs()`
- 参照: `aEvent.target`, `aInsertPoint.hidden`, `document.getElementById("customizationMenuSeparator").hidden`, `document.getElementById("sidebarRevampSeparator").hidden`, `document.getElementById("toolbar-context-bookmarkSelectedTab").hidden`, `document.getElementById("toolbar-context-bookmarkSelectedTabs").hidden`, `document.getElementById("toolbar-context-customize").hidden`, `document.getElementById("toolbar-context-customize-sidebar").hidden`, `document.getElementById("toolbar-context-reloadSelectedTab").hidden`, `document.getElementById("toolbar-context-reloadSelectedTabs").hidden`, `document.getElementById("toolbar-context-selectAllTabs").disabled`, `document.getElementById("toolbarNavigatorItemsMenuSeparator").hidden`, `gBrowser.multiSelectedTabsCount`, `gBrowser.tabContainer?.verticalMode`, `menuSeparator.hidden`, `moveToPanel.hidden`, `node.hidden`, `parent.id`, `parent.localName`, `popup.children`, `popup.children.length`, `popup.documentGlobal`, `popup.firstElementChild`, `popup.triggerNode`, `removeFromToolbar.hidden`, `toggleVerticalTabsItem.hidden`, `toolbar.id`, `toolbarItem.firstElementChild`, `toolbarItem.id`, `toolbarItem.localName`, `toolbarItem.parentElement`, `toolbarItem.parentElement.id`, `toolbarItem?.id`, `toolbarItem?.localName`, `toolbarItem?.parentElement?.id`
- XPCOM: `Services.prefs`

## _getUnwrappedTriggerNode()
- 位置: L376-384
- 役割: カスタマイズモードのラッパーを外して、実際に右クリックされたツールバー項目を返す。
- 触るとき: カスタマイズ中の右クリック対象を正しく取りたいとき。
- 呼び出し先: `gCustomizeMode.isWrappedToolbarItem()`
- 参照: `popup.documentGlobal`, `triggerNode.firstElementChild`

## _getExtensionId()
- 位置: L396-399
- 役割: 右クリック対象が拡張機能のボタンなら、その拡張の ID（data-extensionid）を返す。
- 触るとき: 拡張機能ボタンのメニュー操作の対象を判定するとき。
- 呼び出し先: `node.getAttribute()`, `this._getUnwrappedTriggerNode()`

## _getWidgetId()
- 位置: L413-416
- 役割: 右クリック対象の拡張ウィジェットの ID を返す。
- 触るとき: 拡張機能ボタンの配置（ツールバーかアドオン領域か）を調べるとき。
- 呼び出し先: `node?.closest()`, `this._getUnwrappedTriggerNode()`
- 参照: `node?.closest(".unified-extensions-item")?.id`

## updateExtensionsButtonContextMenu()
- 位置: L424-463
- 役割: 拡張機能メニューボタン用に『常に表示』と『ツールバーから削除』の項目を、ボタンの状態に応じて出し分ける。
- 触るとき: 拡張機能メニューボタンの右クリック項目の表示条件を変えるとき。
- 呼び出し先: `popup.querySelector()`
- 条件付き依存: `if (isCustomizingExtsButton)` → `checkbox.toggleAttribute()`
- 条件付き依存: `if (isExtsButton && !gUnifiedExtensions.buttonAlwaysVisible)` → `checkbox.removeAttribute()`
- 条件付き依存: `if (isExtsButton)` → `popup.querySelector()`
- 条件付き依存: `if (gUnifiedExtensions.buttonAlwaysVisible)` → `removeFromToolbar.removeAttribute()`
- 参照: `checkbox.hidden`, `gUnifiedExtensions.buttonAlwaysVisible`, `popup.documentGlobal`, `popup.triggerNode?.id`, `removeFromToolbar.hidden`

## updateExtension()
- 位置: async L475-521
- 役割: 拡張機能のボタン上で、削除・管理・報告・ツールバーへのピン留め項目を、アドオンの権限と設定に応じて設定する。
- 触るとき: 拡張機能の右クリック項目の表示や権限による無効化を変えるとき。
- 呼び出し先: `lazy.AddonManager.getAddonByID()`, `popup.querySelector()`, `this._getExtensionId()`
- 条件付き依存: `if (addon)` → `popup.querySelector()`
- 条件付き依存: `if (pinToToolbar)` → `this._getWidgetId()`
- 条件付き依存: `if (widgetId)` → `lazy.CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if (widgetId)` → `pinToToolbar.toggleAttribute()`
- 条件付き依存: `if (popup.id === "toolbar-context-menu")` → `lazy.ExtensionsUI.originControlsMenu()`
- 参照: `addon.permissions`, `element.hidden`, `lazy.AddonManager.PERM_CAN_UNINSTALL`, `lazy.CustomizableUI.AREA_ADDONS`, `lazy.CustomizableUI.getPlacementOfWidget(widgetId).area`, `lazy.gAddonAbuseReportEnabled`, `pinToToolbar.hidden`, `popup.id`, `popup.querySelector(".customize-context-moveToPanel").hidden`, `popup.querySelector(".customize-context-removeFromToolbar").hidden`, `removeExtension.disabled`, `reportExtension.hidden`, `reportExtension.nextElementSibling`

## removeExtensionForContextAction()
- 位置: async L531-536
- 役割: 右クリック対象の拡張機能を BrowserAddonUI で削除する。
- 触るとき: 拡張機能の削除操作の経路を調べるとき。
- 呼び出し先: `BrowserAddonUI.removeAddon()`, `this._getExtensionId()`
- 参照: `popup.documentGlobal`

## reportExtensionForContextAction()
- 位置: async L548-552
- 役割: 右クリック対象の拡張機能について、BrowserAddonUI で報告を出す。
- 触るとき: 拡張機能の報告フローの入口を変えるとき。
- 呼び出し先: `BrowserAddonUI.reportAddon()`, `this._getExtensionId()`
- 参照: `popup.documentGlobal`

## openAboutAddonsForContextAction()
- 位置: async L563-567
- 役割: 右クリック対象の拡張機能の管理画面（about:addons）を開く。
- 触るとき: 拡張機能の管理画面を開く経路を変えるとき。
- 呼び出し先: `BrowserAddonUI.manageAddon()`, `this._getExtensionId()`
- 参照: `popup.documentGlobal`

## hideLeadingSeparatorIfNeeded()
- 位置: L579-593
- 役割: 非表示でない最初の項目が区切り線なら、その区切り線を隠す。
- 触るとき: メニュー先頭に区切り線だけ残る表示崩れ（Bug 1955241）を調べるとき。
- 参照: `firstVisibleElement.hidden`, `firstVisibleElement.localName`, `firstVisibleElement.nextElementSibling`, `popup.firstElementChild`

## updateCustomizationItemsVisibility()
- 位置: L606-619
- 役割: 『パネルへ移動』と『ツールバーから削除』の両方が無効なら、両方を隠す。
- 触るとき: カスタマイズ項目を隠す条件を変えるとき。
- 呼び出し先: `moveToPanel.hasAttribute()`, `popup.querySelector()`, `removeFromToolbar?.hasAttribute()`
- 参照: `moveToPanel.hidden`, `removeFromToolbar.hidden`
