# browser/components/storybook/.storybook/addon-fluent/withPseudoLocalization.mjs

source: browser/components/storybook/.storybook/addon-fluent/withPseudoLocalization.mjs
source-hash: 569b0647d9534ae557dc8a87b774ce8da8efcf8f
lines: 89

## <module>
- 役割: (未記入)

## withPseudoLocalization()
- 位置: L24-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `StoryFn()`, `useChannel()`, `useEffect()`, `useGlobals()`
- 条件付き依存: `if (pseudoStrategy)` → `emit()`
- 条件付き依存: `if (isInDocs)` → `document.documentElement.setAttribute()`
- 条件付き依存: `if (isInDocs)` → `document.querySelectorAll()`
- 条件付き依存: `if (isInDocs)` → `storyElements.forEach()`
- 条件付き依存: `if (isInDocs)` → `element.setAttribute()`
- 条件付き依存: `if (!(isInDocs))` → `document.documentElement.setAttribute()`
- 参照: `DIRECTIONS.ltr`, `context.viewMode`

## withFluentStrings()
- 位置: L57-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `StoryFn()`, `emit()`, `useChannel()`, `useGlobals()`
- 条件付き依存: `if (context.parameters?.fluent && fileName)` → `fluentStrings.hasOwnProperty()`
- 条件付き依存: `if (!(fluentStrings.hasOwnProperty(fileName)))` → `provideFluent()`
- 条件付き依存: `if (!(fluentStrings.hasOwnProperty(fileName)))` → `strings.push()`
- 条件付き依存: `if (!(fluentStrings.hasOwnProperty(fileName)))` → `[ message.value, ...Object.entries(message.attributes).map( ([key, value]) => ` .${key} = ${value}` ), ].join()`
- 条件付き依存: `if (!(fluentStrings.hasOwnProperty(fileName)))` → `Object.entries(message.attributes).map()`
- 条件付き依存: `if (!(fluentStrings.hasOwnProperty(fileName)))` → `Object.entries()`
- 条件付き依存: `if (!(fluentStrings.hasOwnProperty(fileName)))` → `updateGlobals()`
- 参照: `context.component`, `context.parameters.fluent`, `context.parameters?.fluent`, `message.attributes`, `message.id`, `message.value`, `resource.body`
