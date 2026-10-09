# browser/components/preferences/widgets/setting-element/setting-element.mjs

source: browser/components/preferences/widgets/setting-element/setting-element.mjs
source-hash: 68f56cd951ef2986109f012d5d5754f7fe51b838
lines: 213

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `XPCOMUtils.declareLazy()`, `directive()`

## expandPaneName()
- 位置: L27-31
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `category.slice()`, `category[0].toUpperCase()`

## SpreadDirective.render()
- 位置: L93-95
- 役割: (未記入)
- 触るとき: (未記入)

## SpreadDirective.update()
- 位置: L104-142
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `key.startsWith()`
- 条件付き依存: `if (key.startsWith("?"))` → `el.toggleAttribute()`
- 条件付き依存: `if (key.startsWith("?"))` → `key.slice()`
- 条件付き依存: `if (key.startsWith("?"))` → `Boolean()`
- 条件付き依存: `if (!(key.startsWith("?")))` → `key.startsWith()`
- 条件付き依存: `if (key.startsWith("."))` → `key.slice()`
- 条件付き依存: `if (!(key.startsWith(".")))` → `key.startsWith()`
- 条件付き依存: `if (!(key.startsWith("@")))` → `el.setAttribute()`
- 条件付き依存: `if (!(key.startsWith("@")))` → `String()`
- 参照: `part.element`, `this.#prevProps`

## bumpHeadingLevelForSrd()
- 位置: L167-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`

## SettingElement.getCommonPropertyMapping()
- 位置: L182-211
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `bumpHeadingLevelForSrd()`, `expandPaneName()`
- 条件付き依存: `if (typeof controlAttrs[key] === "number")` → `bumpHeadingLevelForSrd()`
- 参照: `config.controlAttrs`, `config.headingLevel`, `config.iconSrc`, `config.id`, `config.l10nArgs`, `config.l10nId`, `config.loadPane`, `config.slot`, `config.supportPage`, `lazy.srdEnabled`
