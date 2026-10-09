# browser/components/preferences/config/LegacyPaneMappings.mjs

source: browser/components/preferences/config/LegacyPaneMappings.mjs
source-hash: f176fdfb4364b39dd547d2c9573b677c9043d9d2
lines: 128

## <module>
- 役割: (未記入)

## resolveLegacyCategory()
- 位置: L115-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^pane[A-Z]/.test()`, `LEGACY_PANE_MAPPINGS.get()`
- 条件付き依存: `if (/^pane[A-Z]/.test(category))` → `category[4].toLowerCase()`
- 条件付き依存: `if (/^pane[A-Z]/.test(category))` → `category.slice()`
- 参照: `dest.category`, `dest.subcategory`
