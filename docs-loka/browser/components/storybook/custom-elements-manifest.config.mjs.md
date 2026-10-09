# browser/components/storybook/custom-elements-manifest.config.mjs

source: browser/components/storybook/custom-elements-manifest.config.mjs
source-hash: d49f6468167447d9d067874e049017820bf2782d
lines: 47

## <module>
- 役割: (未記入)
- 呼び出し先: `removePrivateAndStaticFields()`

## removePrivateAndStaticFields()
- 位置: L10-27
- 役割: (未記入)
- 触るとき: (未記入)

## packageLinkPhase()
- 位置: L12-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `customElementsManifest?.modules?.forEach()`, `m?.declarations?.forEach()`
- 条件付き依存: `if (declaration.members != null)` → `declaration.members.filter()`
- 条件付き依存: `if (declaration.members != null)` → `member.name.startsWith()`
- 参照: `declaration.members`, `member.kind`, `member.static`
