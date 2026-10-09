# browser/components/migration/content/migration-wizard.mjs

source: browser/components/migration/content/migration-wizard.mjs
source-hash: f6ada525e6f4fdb0a5ab311d0d47f8bb87d00ccc
lines: 1621

## <module>
- 役割: (未記入)

## MigrationWizard.markup()
- 位置: L35-312
- 役割: (未記入)
- 触るとき: (未記入)

## MigrationWizard.fragment()
- 位置: L314-324
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MigrationWizard.#template.content.cloneNode()`
- 条件付き依存: `if (!MigrationWizard.#template)` → `parser.parseFromString()`
- 条件付き依存: `if (!MigrationWizard.#template)` → `document.importNode()`
- 条件付き依存: `if (!MigrationWizard.#template)` → `doc.querySelector()`
- 参照: `MigrationWizard.#template`, `MigrationWizard.markup`

## MigrationWizard.constructor()
- 位置: L326-411
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `button.addEventListener()`, `document.l10n.connectRoot()`, `link.addEventListener()`, `shadow.appendChild()`, `shadow.querySelector()`, `shadow.querySelectorAll()`, `super()`, `this.#browserProfileSelector.addEventListener()`, `this.#chooseImportFromFile.addEventListener()`, `this.#extensionsSuccessLink.addEventListener()`, `this.#getPermissionsButton.addEventListener()`, `this.#importButton.addEventListener()`, `this.#importFromFileButton.addEventListener()`, `this.#resourceSummary.addEventListener()`, `this.#resourceTypeList.addEventListener()`, `this.#safariPasswordImportInstructions.addEventListener()`, `this.#safariPermissionButton.addEventListener()`, `this.#supportTextLinks.forEach()`, `this.attachShadow()`
- 条件付き依存: `if (window.MozXULElement)` → `window.MozXULElement.insertFTLIfNeeded()`
- 参照: `MigrationWizard.fragment`, `shadow.querySelector("#select-all").control`, `this.#browserProfileSelector`, `this.#chooseImportFromFile`, `this.#deck`, `this.#extensionsSuccessLink`, `this.#getPermissionsButton`, `this.#importButton`, `this.#importFromFileButton`, `this.#resourceSummary`, `this.#resourceTypeList`, `this.#safariPasswordImportInstructions`, `this.#safariPermissionButton`, `this.#selectAllCheckbox`, `this.#shadowRoot`, `this.#supportTextLinks`, `window.MozXULElement`

## MigrationWizard.connectedCallback()
- 位置: L413-417
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`
- 条件付き依存: `if (this.hasAttribute("auto-request-state"))` → `this.requestState()`

## MigrationWizard.requestState()
- 位置: L419-423
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## MigrationWizard.state()
- 位置: L434-436
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.setState()`

## MigrationWizard.setState()
- 位置: L446-475
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#deck.setAttribute()`, `this.#deck.toggleAttribute()`, `this.#onShowingFileImportProgress()`, `this.#onShowingNoBrowsersFound()`, `this.#onShowingProgress()`, `this.#onShowingSelection()`
- 条件付き依存: `if (window.IS_STORYBOOK)` → `this.#updateForStorybook()`
- 参照: `MigrationWizardConstants.PAGES.FILE_IMPORT_PROGRESS`, `MigrationWizardConstants.PAGES.LOADING`, `MigrationWizardConstants.PAGES.NO_BROWSERS_FOUND`, `MigrationWizardConstants.PAGES.PROGRESS`, `MigrationWizardConstants.PAGES.SELECTION`, `state.page`, `window.IS_STORYBOOK`

## MigrationWizard.#dialogMode()
- 位置: L477-479
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.hasAttribute()`

## MigrationWizard.#ensureSelectionDropdown()
- 位置: L481-499
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `this.#browserProfileSelectorList.addEventListener()`, `this.#browserProfileSelectorList.toggleAttribute()`
- 条件付き依存: `if (document.createXULElement)` → `document.createXULElement()`
- 条件付き依存: `if (document.createXULElement)` → `panel.appendChild()`
- 条件付き依存: `if (document.createXULElement)` → `this.#shadowRoot.appendChild()`
- 条件付き依存: `if (!(document.createXULElement))` → `this.#shadowRoot.appendChild()`
- 参照: `document.createXULElement`, `this.#browserProfileSelectorList`

## MigrationWizard.#onBrowserProfileSelectionChanged()
- 位置: L508-618
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelItem.getAttribute()`, `selectionPage.setAttribute()`, `selectionPage.toggleAttribute()`, `this.#browserProfileSelector.querySelector()`, `this.#browserProfileSelectorList.selectedPanelItem.classList.add()`, `this.#displaySelectedResources()`, `this.#resourceTypeList.querySelector()`, `this.#resourceTypeList.querySelectorAll()`, `this.#shadowRoot.querySelector()`
- 条件付き依存: `if (this.#browserProfileSelectorList.selectedPanelItem)` → `this.#browserProfileSelectorList.selectedPanelItem.classList.remove()`
- 条件付き依存: `if (panelItem.brandImage)` → `this.#browserProfileSelector.querySelector()`
- 条件付き依存: `if (!(panelItem.brandImage))` → `this.#browserProfileSelector.querySelector()`
- 条件付き依存: `if (resourceLabel)` → `resourceLabel.querySelector()`
- 条件付き依存: `if (labelSpan)` → `MigrationWizardConstants.USES_FAVORITES.includes()`
- 条件付き依存: `if (MigrationWizardConstants.USES_FAVORITES.includes(key))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (MigrationWizardConstants.USES_FAVORITES.includes(key))` → `labelSpan.getAttribute()`
- 条件付き依存: `if (!(MigrationWizardConstants.USES_FAVORITES.includes(key)))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(MigrationWizardConstants.USES_FAVORITES.includes(key)))` → `labelSpan.getAttribute()`
- 条件付き依存: `if (showNoPermissionsMessage)` → `selectionPage.querySelector()`
- 条件付き依存: `if (showNoPermissionsMessage)` → `step2.setAttribute()`
- 条件付き依存: `if (showNoPermissionsMessage)` → `JSON.stringify()`
- 条件付き依存: `if (showNoPermissionsMessage)` → `this.dispatchEvent()`
- 参照: `MigrationWizardConstants.MIGRATOR_TYPES.BROWSER`, `child.control.checked`, `child.hidden`, `panelItem.brandImage`, `panelItem.displayName`, `panelItem.hasPermissions`, `panelItem.permissionsPath`, `panelItem.profile?.name`, `panelItem.resourceTypes`, `resourceLabel.control.checked`, `resourceLabel.hidden`, `resourceTypes.length`, `selectAll.checked`, `this.#browserProfileSelector.querySelector( ".migrator-icon" ).style.content`, `this.#browserProfileSelector.querySelector("#migrator-name").textContent`, `this.#browserProfileSelector.querySelector("#profile-name").textContent`, `this.#browserProfileSelector.selectedPanelItem`, `this.#browserProfileSelectorList.selectedPanelItem`, `this.#shadowRoot.querySelector("#select-all").control`

## MigrationWizard.#onShowingSelection()
- 位置: L637-748
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.createElement()`, `opt.setAttribute()`, `opt.shadowRoot.querySelector()`, `requestAnimationFrame()`, `selectionPage.querySelector()`, `subheader.toggleAttribute()`, `this.#applyContentCustomizations()`, `this.#browserProfileSelector.focus()`, `this.#browserProfileSelectorList.appendChild()`, `this.#ensureSelectionDropdown()`, `this.#shadowRoot.querySelector()`, `this.getAttribute()`, `this.hasAttribute()`
- 条件付き依存: `if (this.hasAttribute("selection-header-string"))` → `header.toggleAttribute()`
- 条件付き依存: `if (!(this.hasAttribute("selection-header-string")))` → `header.removeAttribute()`
- 条件付き依存: `if (this.hasAttribute("force-show-import-all"))` → `this.getAttribute()`
- 条件付き依存: `if (this.hasAttribute("force-show-import-all"))` → `selectionPage.toggleAttribute()`
- 条件付き依存: `if (!(this.hasAttribute("force-show-import-all")))` → `selectionPage.toggleAttribute()`
- 条件付き依存: `if (migrator.profile)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(migrator.profile))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (state.migrators.length)` → `this.#onBrowserProfileSelectionChanged()`
- 条件付き依存: `if (state.migratorKey)` → `this.#browserProfileSelectorList.querySelector()`
- 条件付き依存: `if (state.migratorKey)` → `this.#onBrowserProfileSelectionChanged()`
- 条件付き依存: `if (state.fileImportErrorMessage)` → `selectionPage.toggleAttribute()`
- 条件付き依存: `if (!(state.fileImportErrorMessage))` → `selectionPage.toggleAttribute()`
- 参照: `button.style.backgroundImage`, `details.open`, `fileImportErrorMessageEl.textContent`, `header.textContent`, `migrator.brandImage`, `migrator.displayName`, `migrator.hasPermissions`, `migrator.key`, `migrator.permissionsPath`, `migrator.profile`, `migrator.profile.name`, `migrator.resourceTypes`, `migrator.type`, `opt.brandImage`, `opt.displayName`, `opt.hasPermissions`, `opt.permissionsPath`, `opt.profile`, `opt.resourceTypes`, `state.fileImportErrorMessage`, `state.migratorKey`, `state.migrators`, `state.migrators.length`, `state.showImportAll`, `subheader.textContent`, `this.#browserProfileSelectorList.firstElementChild`, `this.#browserProfileSelectorList.textContent`, `this.#expandedDetails`

## MigrationWizard.#onShowingProgress()
- 位置: L786-945
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `document.createTextNode()`, `document.l10n.setAttributes()`, `group.querySelector()`, `messageText.appendChild()`, `progressIcon.setAttribute()`, `progressPage.querySelector()`, `progressPage.querySelectorAll()`, `state.progress.hasOwnProperty()`, `supportLink.removeAttribute()`, `this.#shadowRoot.getElementById()`, `this.#shadowRoot.querySelector()`
- 条件付き依存: `if (labelSpan)` → `MigrationWizardConstants.USES_FAVORITES.includes()`
- 条件付き依存: `if (MigrationWizardConstants.USES_FAVORITES.includes(state.key))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (MigrationWizardConstants.USES_FAVORITES.includes(state.key))` → `labelSpan.getAttribute()`
- 条件付き依存: `if (!(MigrationWizardConstants.USES_FAVORITES.includes(state.key)))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(MigrationWizardConstants.USES_FAVORITES.includes(state.key)))` → `labelSpan.getAttribute()`
- 条件付き依存: `if (supportLink)` → `supportLink.removeAttribute()`
- 条件付き依存: `if (!(totalWarnings))` → `this.getAttribute()`
- 条件付き依存: `if (this.getAttribute("data-import-complete-success-string"))` → `this.getAttribute()`
- 条件付き依存: `if (migrationDone)` → `requestAnimationFrame()`
- 条件付き依存: `if (migrationDone)` → `progressPage.querySelector()`
- 条件付き依存: `if (migrationDone)` → `button.focus()`
- 参照: `MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.EXTENSIONS`, `MigrationWizardConstants.PROGRESS_VALUE.INFO`, `MigrationWizardConstants.PROGRESS_VALUE.LOADING`, `MigrationWizardConstants.PROGRESS_VALUE.SUCCESS`, `MigrationWizardConstants.PROGRESS_VALUE.WARNING`, `Object.keys(state.progress).length`, `cancelButton.hidden`, `finishButton.hidden`, `group.dataset.resourceType`, `group.hidden`, `header.textContent`, `messageText.textContent`, `state.key`, `state.progress`, `state.progress[resourceType].linkText`, `state.progress[resourceType].linkURL`, `state.progress[resourceType].message`, `state.progress[resourceType].value`, `supportLink.href`, `supportLink.target`, `supportLink.textContent`, `this.#dialogMode`, `this.#extensionsSuccessLink.target`, `this.#extensionsSuccessLink.textContent`

## MigrationWizard.#onShowingFileImportProgress()
- 位置: L967-1050
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `console.error()`, `document.createTextNode()`, `document.l10n.setAttributes()`, `group.querySelector()`, `messageText.appendChild()`, `progressIcon.setAttribute()`, `progressPage.querySelector()`, `progressPage.querySelectorAll()`, `state.progress.hasOwnProperty()`, `this.#shadowRoot.getElementById()`, `this.#shadowRoot.querySelector()`
- 条件付き依存: `if (migrationDone)` → `requestAnimationFrame()`
- 条件付き依存: `if (migrationDone)` → `doneButton.focus()`
- 参照: `MigrationWizardConstants.PROGRESS_VALUE.LOADING`, `MigrationWizardConstants.PROGRESS_VALUE.SUCCESS`, `MigrationWizardConstants.PROGRESS_VALUE.WARNING`, `Object.keys(state.progress).length`, `cancelButton.hidden`, `doneButton.hidden`, `group.dataset.resourceType`, `group.hidden`, `header.textContent`, `messageText.textContent`, `state.progress`, `state.progress[resourceType].message`, `state.progress[resourceType].value`, `state.title`

## MigrationWizard.#onShowingNoBrowsersFound()
- 位置: L1061-1063
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `state.hasFileMigrators`, `this.#chooseImportFromFile.hidden`

## MigrationWizard.#updateForStorybook()
- 位置: L1070-1082
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `progressEl.getAttribute()`, `this.#shadowRoot.querySelectorAll()`, `this.#shadowRoot.querySelectorAll(".progress-icon").forEach()`
- 条件付き依存: `if (progressEl.getAttribute("state") == "loading")` → `progressEl.setAttribute()`
- 条件付き依存: `if (!(progressEl.getAttribute("state") == "loading"))` → `progressEl.removeAttribute()`

## MigrationWizard.doAutoImport()
- 位置: L1098-1111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#gatherMigrationEventDetails()`, `this.dispatchEvent()`

## MigrationWizard.#doImport()
- 位置: L1118-1127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#gatherMigrationEventDetails()`, `this.dispatchEvent()`

## MigrationWizard.#gatherMigrationEventDetails()
- 位置: L1175-1215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `panelItem.getAttribute()`, `this.#resourceTypeList.querySelectorAll()`
- 条件付き依存: `if (resourceTypeField.control.checked)` → `resourceTypes.push()`
- 参照: `MigrationWizardConstants.MIGRATOR_TYPES.BROWSER`, `autoMigrationDetails?.migratorKey`, `panelItem.hasPermissions`, `panelItem.profile`, `resourceTypeField.control.checked`, `resourceTypeField.dataset.resourceType`, `this.#browserProfileSelector.selectedPanelItem`, `this.#expandedDetails`

## MigrationWizard.#requestSafariPermissions()
- 位置: L1222-1230
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#gatherMigrationEventDetails()`, `this.dispatchEvent()`

## MigrationWizard.#selectManualPasswordFile()
- 位置: L1237-1245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#gatherMigrationEventDetails()`, `this.dispatchEvent()`

## MigrationWizard.#getPermissions()
- 位置: L1251-1259
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#gatherMigrationEventDetails()`, `this.dispatchEvent()`

## MigrationWizard.#displaySelectedResources()
- 位置: async L1265-1364
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MigrationWizardConstants.USES_FAVORITES.includes()`, `Object.keys()`, `Object.values()`, `Object.values(resourceTypeToLabelIDs).map()`, `document.l10n.formatValues()`, `panelItem.getAttribute()`, `resourceTypeLabelMapping.set()`, `selectionPage.toggleAttribute()`, `this.#resourceTypeList.querySelectorAll()`, `this.#shadowRoot.querySelector()`, `this.dispatchEvent()`, `this.hasAttribute()`
- 条件付き依存: `if (resourceTypeLabel.control.checked)` → `selectedDataArray.push()`
- 条件付き依存: `if (resourceTypeLabel.control.checked)` → `resourceTypeLabelMapping.get()`
- 条件付き依存: `if (selectedDataArray.length)` → `selectedDataArray[0].charAt(0).toLocaleUpperCase()`
- 条件付き依存: `if (selectedDataArray.length)` → `selectedDataArray[0].charAt()`
- 条件付き依存: `if (selectedDataArray.length)` → `selectedDataArray[0].slice()`
- 条件付き依存: `if (selectedDataArray.length)` → `formatter.format()`
- 条件付き依存: `if (this.hasAttribute("option-expander-title-string"))` → `this.getAttribute()`
- 条件付き依存: `if (checkedResources == 0)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (checkedResources < totalResources)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(checkedResources < totalResources))` → `document.l10n.setAttributes()`
- 参照: `Intl.ListFormat`, `MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.BOOKMARKS`, `MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.EXTENSIONS`, `MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.FORMDATA`, `MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.HISTORY`, `MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.PASSWORDS`, `MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.PAYMENT_METHODS`, `importButton.disabled`, `resourceTypeLabel.control.checked`, `resourceTypeLabel.dataset.resourceType`, `resourceTypeLabels.length`, `resourceTypes.length`, `selectedData.textContent`, `selectedDataArray.length`, `selectedDataHeader.textContent`, `this.#browserProfileSelector.selectedPanelItem`

## MigrationWizard.#applyContentCustomizations()
- 位置: L1370-1469
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#shadowRoot.querySelector()`, `this.hasAttribute()`
- 条件付き依存: `if (this.hasAttribute("hide-select-all"))` → `this.getAttribute()`
- 条件付き依存: `if (this.hasAttribute("hide-select-all"))` → `selectionPage.toggleAttribute()`
- 条件付き依存: `if (!(this.hasAttribute("hide-select-all")))` → `selectionPage.removeAttribute()`
- 条件付き依存: `if (this.hasAttribute("import-button-string"))` → `this.getAttribute()`
- 条件付き依存: `if (this.getAttribute("import-button-string"))` → `this.getAttribute()`
- 条件付き依存: `if (this.hasAttribute("checkbox-margin-inline"))` → `this.getAttribute()`
- 条件付き依存: `if (this.hasAttribute("checkbox-margin-inline"))` → `this.style.setProperty()`
- 条件付き依存: `if (this.hasAttribute("checkbox-margin-block"))` → `this.getAttribute()`
- 条件付き依存: `if (this.hasAttribute("checkbox-margin-block"))` → `this.style.setProperty()`
- 条件付き依存: `if (this.hasAttribute("import-button-class"))` → `this.getAttribute()`
- 条件付き依存: `if (importButtonClass)` → `this.#importButton.classList.add()`
- 条件付き依存: `if (this.hasAttribute("header-font-size"))` → `this.getAttribute()`
- 条件付き依存: `if (headerFontSize)` → `this.style.setProperty()`
- 条件付き依存: `if (this.hasAttribute("header-font-weight"))` → `this.getAttribute()`
- 条件付き依存: `if (headerFontWeight)` → `this.style.setProperty()`
- 条件付き依存: `if (this.hasAttribute("header-margin-block"))` → `this.getAttribute()`
- 条件付き依存: `if (headerMarginBlock)` → `this.style.setProperty()`
- 条件付き依存: `if (this.hasAttribute("subheader-font-size"))` → `this.getAttribute()`
- 条件付き依存: `if (subheaderFontSize)` → `this.style.setProperty()`
- 条件付き依存: `if (this.hasAttribute("subheader-font-weight"))` → `this.getAttribute()`
- 条件付き依存: `if (subheaderFontWeight)` → `this.style.setProperty()`
- 条件付き依存: `if (this.hasAttribute("subheader-margin-block"))` → `this.getAttribute()`
- 条件付き依存: `if (subheaderMarginBlock)` → `this.style.setProperty()`
- 参照: `this.#importButton.textContent`

## MigrationWizard.#handleClickEvent()
- 位置: L1471-1568
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( event.target == this.#importButton || event.target == this.#importFromFileButton )` → `this.#doImport()`
- 条件付き依存: `if (!( event.target == this.#importButton || event.target == this.#importFromFileButton ))` → `event.target.classList.contains()`
- 条件付き依存: `if ( event.target.classList.contains("cancel-close") || event.target.classList.contains("finish-button") )` → `this.dispatchEvent()`
- 条件付き依存: `if ( event.currentTarget == this.#browserProfileSelectorList && event.target != this.#browserProfileSelectorList )` → `this.#onBrowserProfileSelectionChanged()`
- 条件付き依存: `if ( event.currentTarget == this.#browserProfileSelectorList && event.target != this.#browserProfileSelectorList )` → `event.target.getAttribute()`
- 条件付き依存: `if ( event.target.getAttribute("type") == MigrationWizardConstants.MIGRATOR_TYPES.FILE )` → `this.#doImport()`
- 条件付き依存: `if (event.target == this.#safariPermissionButton)` → `this.#requestSafariPermissions()`
- 条件付き依存: `if (event.target == this.#chooseImportFromFile)` → `this.dispatchEvent()`
- 条件付き依存: `if (event.target.id == "launch-macos-passwords-app")` → `this.dispatchEvent()`
- 条件付き依存: `if (!(event.target.id == "launch-macos-passwords-app"))` → `event.target.classList.contains()`
- 条件付き依存: `if (event.target.classList.contains("manual-password-import-skip"))` → `this.#shadowRoot.querySelector()`
- 条件付き依存: `if (event.target.classList.contains("manual-password-import-skip"))` → `this.#shadowRoot.querySelectorAll()`
- 条件付き依存: `if (!checked)` → `this.requestState()`
- 条件付き依存: `if (!(!checked))` → `this.#doImport()`
- 条件付き依存: `if (!(event.target.classList.contains("manual-password-import-skip")))` → `event.target.classList.contains()`
- 条件付き依存: `if ( event.target.classList.contains("manual-password-import-select") )` → `this.#selectManualPasswordFile()`
- 条件付き依存: `if (event.target == this.#extensionsSuccessLink)` → `this.dispatchEvent()`
- 条件付き依存: `if (event.target == this.#extensionsSuccessLink)` → `event.preventDefault()`
- 条件付き依存: `if (!(event.target == this.#extensionsSuccessLink))` → `[...this.#supportTextLinks].includes()`
- 条件付き依存: `if (!(event.target == this.#extensionsSuccessLink))` → `this.hasAttribute()`
- 条件付き依存: `if ( [...this.#supportTextLinks].includes(event.target) && this.hasAttribute("in-aboutwelcome-bundle") )` → `this.dispatchEvent()`
- 条件付き依存: `if ( [...this.#supportTextLinks].includes(event.target) && this.hasAttribute("in-aboutwelcome-bundle") )` → `event.preventDefault()`
- 条件付き依存: `if (event.target == this.#getPermissionsButton)` → `this.#getPermissions()`
- 参照: `MigrationWizardConstants.DISPLAYED_RESOURCE_TYPES.PASSWORDS`, `MigrationWizardConstants.MIGRATOR_TYPES.FILE`, `checkbox.checked`, `event.currentTarget`, `event.target`, `event.target.href`, `event.target.id`, `this.#browserProfileSelectorList`, `this.#chooseImportFromFile`, `this.#expandedDetails`, `this.#extensionsSuccessLink`, `this.#getPermissionsButton`, `this.#importButton`, `this.#importFromFileButton`, `this.#resourceSummary`, `this.#safariPermissionButton`, `this.#shadowRoot.querySelectorAll( `label[data-resource-type] > input:checked` ).length`, `this.#supportTextLinks`

## MigrationWizard.#handleChangeEvent()
- 位置: L1570-1593
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.target == this.#browserProfileSelector)` → `this.#onBrowserProfileSelectionChanged()`
- 条件付き依存: `if (event.target == this.#selectAllCheckbox)` → `this.#shadowRoot.querySelectorAll()`
- 条件付き依存: `if (event.target == this.#selectAllCheckbox)` → `this.#displaySelectedResources()`
- 条件付き依存: `if (!(event.target == this.#selectAllCheckbox))` → `this.#shadowRoot.querySelectorAll()`
- 条件付き依存: `if (!(event.target == this.#selectAllCheckbox))` → `Array.from(checkboxes).every()`
- 条件付き依存: `if (!(event.target == this.#selectAllCheckbox))` → `Array.from()`
- 条件付き依存: `if (!(event.target == this.#selectAllCheckbox))` → `this.#displaySelectedResources()`
- 参照: `checkbox.checked`, `event.target`, `this.#browserProfileSelector`, `this.#selectAllCheckbox`, `this.#selectAllCheckbox.checked`

## MigrationWizard.handleEvent()
- 位置: L1595-1615
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#handleChangeEvent()`, `this.#handleClickEvent()`
- 条件付き依存: `if ( event.target == this.#browserProfileSelector && (event.type == "mousedown" || (event.type == "click" && event.mozInputSource == MouseEvent.MOZ_SOURCE_KEYBOA...)` → `this.#browserProfileSelectorList.toggle()`
- 参照: `MouseEvent.MOZ_SOURCE_KEYBOARD`, `event.mozInputSource`, `event.target`, `event.type`, `this.#browserProfileSelector`
