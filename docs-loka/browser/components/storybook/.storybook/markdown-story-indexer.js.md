# browser/components/storybook/.storybook/markdown-story-indexer.js

source: browser/components/storybook/.storybook/markdown-story-indexer.js
source-hash: fa1c4997024c90cf7a19cc4ac0829511c88cbfbb
lines: 51

## <module>
- 役割: (未記入)
- 呼び出し先: `require()`

## module.exports()
- 位置: async L22-50
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `compile()`, `fs.readFileSync()`, `getMDXSource()`, `getStoryTitle()`, `indexInputs.map()`, `loadCsf()`, `loadCsf(csfCode, { fileName, makeTitle: () => title }).parse()`, `tags.includes()`
- 条件付き依存: `if (docsOnly)` → `tags.push()`
- 条件付き依存: `if (!tags.includes("stories-mdx"))` → `tags.push()`
- 参照: `input.tags`, `stories[index].parameters?.docsOnly`

## makeTitle()
- 位置: L32-32
- 役割: (未記入)
- 触るとき: (未記入)
