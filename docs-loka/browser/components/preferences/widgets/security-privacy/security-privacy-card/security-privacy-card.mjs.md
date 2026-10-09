# browser/components/preferences/widgets/security-privacy/security-privacy-card/security-privacy-card.mjs

source: browser/components/preferences/widgets/security-privacy/security-privacy-card/security-privacy-card.mjs
source-hash: 43f36558c25f585792dd5334f2bed5ac5d784dbd
lines: 338

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `customElements.define()`

## SecurityPrivacyCard.#okUpdateStatus()
- 位置: L41-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `okStatuses.includes()`
- 参照: `lazy.AppConstants.MOZ_UPDATER`, `lazy.AppUpdater.STATUS.CHECKING`, `lazy.AppUpdater.STATUS.NO_UPDATER`, `lazy.AppUpdater.STATUS.NO_UPDATES_FOUND`, `lazy.AppUpdater.STATUS.OTHER_INSTANCE_HANDLING_UPDATES`, `lazy.AppUpdater.STATUS.UPDATE_DISABLED_BY_POLICY`, `this.appUpdateStatus`

## SecurityPrivacyCard.strictEnabled()
- 位置: L58-60
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.setting.deps.etpStrictEnabled.value`

## SecurityPrivacyCard.customEnabled()
- 位置: L62-64
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.setting.deps.etpCustomEnabled.value`

## SecurityPrivacyCard.trackersBlocked()
- 位置: L66-68
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.setting.deps.trackerCount.value`

## SecurityPrivacyCard.appUpdateStatus()
- 位置: L70-72
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.setting.deps.appUpdateStatus.value`

## SecurityPrivacyCard.appUpdateStatus()
- 位置: L76-79
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.requestUpdate()`
- 参照: `this.setting.deps.appUpdateStatus.value`

## SecurityPrivacyCard.configIssueCount()
- 位置: L81-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(this.setting.deps).filter()`, `filteredWarnings.includes()`
- 参照: `Object.values(this.setting.deps).filter( warning => !filteredWarnings.includes(warning.id) && warning.visible ).length`, `this.setting.deps`, `warning.id`, `warning.visible`

## SecurityPrivacyCard.#spotlightSubcategoryOnPane()
- 位置: L101-105
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `document.location.hash`

## SecurityPrivacyCard.#openWarningCardAndScroll()
- 位置: L107-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this.#spotlightSubcategoryOnPane()`, `this.#spotlightSubcategoryOnPane("#privacy", "security-warning-card")()`
- 参照: `accordion.expanded`

## SecurityPrivacyCard.getStatusImage()
- 位置: L116-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 条件付き依存: `if (this.configIssueCount > 0)` → `html()`
- 参照: `this.configIssueCount`

## SecurityPrivacyCard.buildIssuesElement()
- 位置: L137-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#openWarningCardAndScroll()`
- 条件付き依存: `if (this.configIssueCount == 0)` → `html()`
- 参照: `L10N_IDS.okLabel`, `L10N_IDS.problemHelperLabel`, `L10N_IDS.problemLabel`, `this.configIssueCount`

## SecurityPrivacyCard.buildTrackersElement()
- 位置: L165-215
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`
- 条件付き依存: `if (this.strictEnabled)` → `html()`
- 条件付き依存: `if (this.strictEnabled)` → `this.#spotlightSubcategoryOnPane()`
- 条件付き依存: `if (this.customEnabled)` → `html()`
- 条件付き依存: `if (this.customEnabled)` → `this.#spotlightSubcategoryOnPane()`
- 参照: `L10N_IDS.customEnabledLabel`, `L10N_IDS.strictEnabledLabel`, `L10N_IDS.trackersLabel`, `L10N_IDS.trackersPendingLabel`, `this.customEnabled`, `this.strictEnabled`, `this.trackersBlocked`

## SecurityPrivacyCard.buildUpdateElement()
- 位置: L223-290
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#spotlightSubcategoryOnPane()`
- 条件付き依存: `if (!lazy.AppConstants.MOZ_UPDATER)` → `html()`
- 参照: `L10N_IDS.upToDateLabel`, `L10N_IDS.updateButtonLabel`, `L10N_IDS.updateCheckingLabel`, `L10N_IDS.updateErrorLabel`, `L10N_IDS.updateNeededDescription`, `L10N_IDS.updateNeededLabel`, `lazy.AppConstants.MOZ_UPDATER`, `lazy.AppUpdater.STATUS.CHECKING`, `lazy.AppUpdater.STATUS.CHECKING_FAILED`, `lazy.AppUpdater.STATUS.DOWNLOADING`, `lazy.AppUpdater.STATUS.DOWNLOAD_AND_INSTALL`, `lazy.AppUpdater.STATUS.DOWNLOAD_FAILED`, `lazy.AppUpdater.STATUS.INTERNAL_ERROR`, `lazy.AppUpdater.STATUS.MANUAL_UPDATE`, `lazy.AppUpdater.STATUS.NEVER_CHECKED`, `lazy.AppUpdater.STATUS.NO_UPDATER`, `lazy.AppUpdater.STATUS.NO_UPDATES_FOUND`, `lazy.AppUpdater.STATUS.OTHER_INSTANCE_HANDLING_UPDATES`, `lazy.AppUpdater.STATUS.READY_FOR_RESTART`, `lazy.AppUpdater.STATUS.STAGING`, `lazy.AppUpdater.STATUS.UNSUPPORTED_SYSTEM`, `lazy.AppUpdater.STATUS.UPDATE_DISABLED_BY_POLICY`, `this.appUpdateStatus`

## SecurityPrivacyCard.render()
- 位置: L299-335
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.#okUpdateStatus()`, `this.buildIssuesElement()`, `this.buildTrackersElement()`, `this.buildUpdateElement()`, `this.getStatusImage()`
- 参照: `L10N_IDS.okHeader`, `L10N_IDS.problemHeader`, `this.configIssueCount`
