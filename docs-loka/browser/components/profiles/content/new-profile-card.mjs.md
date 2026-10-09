# browser/components/profiles/content/new-profile-card.mjs

source: browser/components/profiles/content/new-profile-card.mjs
source-hash: 8c43d92ba075bee60e38c2236c9668c281cb7806
lines: 137

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## NewProfileCard.init()
- 位置: async L17-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `RPMSendQuery()`, `this.setInitialInput()`, `this.setProfile()`, `this.setRandomTheme()`
- 条件付き依存: `if (!isInAutomation)` → `this.maybeRedirectExistingProfile()`
- 参照: `this.initialized`, `this.novaEnabled`, `this.profiles`, `this.themes`, `this.updateNameDebouncer.timeout`

## NewProfileCard.maybeRedirectExistingProfile()
- 位置: L60-65
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`
- 条件付き依存: `if (Date.now() - TEN_MINUTES_IN_MS > profileCreated)` → `window.removeEventListener()`
- 条件付き依存: `if (Date.now() - TEN_MINUTES_IN_MS > profileCreated)` → `window.location.replace()`

## NewProfileCard.setRandomTheme()
- 位置: async L67-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Math.random()`, `super.updateTheme()`
- 条件付き依存: `if (isInAutomation && !this.novaEnabled)` → `possibleThemes.filter()`
- 条件付き依存: `if (this.novaEnabled)` → `this.themesPicker.dispatchEvent()`
- 参照: `newTheme.id`, `possibleThemes.length`, `t.useInAutomation`, `this.novaEnabled`, `this.profile.themeId`, `this.themes`, `this.updateComplete`

## NewProfileCard.setInitialInput()
- 位置: async L94-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMGetBoolPref()`, `this.getUpdateComplete()`
- 参照: `this.nameInput.value`

## NewProfileCard.onDeleteClick()
- 位置: L104-107
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `RPMSendAsyncMessage()`, `window.removeEventListener()`

## NewProfileCard.headerTemplate()
- 位置: L109-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`

## NewProfileCard.nameInputTemplate()
- 位置: L123-133
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `super.handleInputEvent`, `this.profile.name`
