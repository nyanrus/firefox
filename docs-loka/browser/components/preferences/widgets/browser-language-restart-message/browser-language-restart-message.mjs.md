# browser/components/preferences/widgets/browser-language-restart-message/browser-language-restart-message.mjs

source: browser/components/preferences/widgets/browser-language-restart-message/browser-language-restart-message.mjs
source-hash: 0bbb52a5e0da5acaeba4c93df9ab120a8fd12e8a
lines: 152

## <module>
- 役割: (未記入)
- 呼び出し先: `customElements.define()`

## getBundleForLocales()
- 位置: L21-35
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`
- 参照: `Services.locale.lastFallbackLocale`, `Services.locale.requestedLocales`
- XPCOM: `Services.locale`

## BrowserLanguageRestartMessage.constructor()
- 位置: L48-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.messageStrings`, `this.pendingLocale`, `this.setting`, `this.showError`

## BrowserLanguageRestartMessage.willUpdate()
- 位置: L60-70
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (pendingLocale != this.pendingLocale)` → `this.loadMessages()`
- 参照: `this.browserLanguage`, `this.browserLanguage.pendingLocale`, `this.messageStrings`, `this.pendingLocale`, `this.showError`

## BrowserLanguageRestartMessage.loadMessages()
- 位置: async L78-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `[newBundle, document.l10n].map()`, `bundle.formatValues()`, `getBundleForLocales()`
- 参照: `BrowserLanguageRestartMessage.MESSAGE_L10N_IDS`, `document.l10n`, `this.messageStrings`, `this.pendingLocale`

## BrowserLanguageRestartMessage.browserLanguage()
- 位置: L103-110
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `handler.asyncSetting`, `this.setting.deps.browserLanguages.config`

## BrowserLanguageRestartMessage.applyAndRestart()
- 位置: L112-114
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.browserLanguage.applyAndRestart()`

## BrowserLanguageRestartMessage.render()
- 位置: L116-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`, `this.messageStrings.map()`
- 参照: `this.applyAndRestart`, `this.messageStrings.length`, `this.showError`
