# browser/components/storybook/.storybook/fluent-utils.mjs

source: browser/components/storybook/.storybook/fluent-utils.mjs
source-hash: d8dad4dd33a818cf1523c6ed73109bd1a023f028
lines: 130

## <module>
- 役割: (未記入)
- 呼び出し先: `addons.getChannel()`, `channel.on()`, `document.l10n.translateRoots()`, `storybookBundle.getMessage()`

## transform()
- 位置: L19-24
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (currentStrategy in PSEUDO_STRATEGY_TRANSFORMS)` → `PSEUDO_STRATEGY_TRANSFORMS[currentStrategy]()`

## updatePseudoStrategy()
- 位置: L47-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PSEUDO_STRATEGIES.includes()`
- 条件付き依存: `if (strategy !== currentStrategy && PSEUDO_STRATEGIES.includes(strategy))` → `document.l10n.translateRoots()`

## connectFluent()
- 位置: L54-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.connectRoot()`, `document.l10n.translateRoots()`
- 参照: `document.documentElement`, `document.l10n`

## generateBundles()
- 位置: L60-62
- 役割: (未記入)
- 触るとき: (未記入)

## insertFTLIfNeeded()
- 位置: async L64-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fileName.split()`, `loadedResources.has()`, `provideFluent()`
- 条件付き依存: `if (root == "toolkit")` → `import()`
- 条件付き依存: `if (root == "browser")` → `import()`
- 条件付き依存: `if (root == "locales-preview")` → `import()`
- 条件付き依存: `if (root == "branding")` → `import()`
- 条件付き依存: `if (root == "preview")` → `import()`
- 参照: `imported.default`

## provideFluent()
- 位置: L121-129
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.translateRoots()`, `storybookBundle.addResource()`
- 条件付き依存: `if (fileName)` → `loadedResources.set()`
