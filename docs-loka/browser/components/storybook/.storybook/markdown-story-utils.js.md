# browser/components/storybook/.storybook/markdown-story-utils.js

source: browser/components/storybook/.storybook/markdown-story-utils.js
source-hash: 183ecf6fbf88436a803761792f963baa206d74c8
lines: 205

## <module>
- 役割: (未記入)
- 呼び出し先: `path.resolve()`, `require()`

## getTitleFromPath()
- 位置: L22-38
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `path.basename()`, `separateWords()`
- 条件付き依存: `if (fileName != "README")` → `path.resolve()`
- 条件付き依存: `if (fileName != "README")` → `filePath.replace()`
- 条件付き依存: `if (fileName != "README")` → `fs.readFileSync(relatedFilePath).toString()`
- 条件付き依存: `if (fileName != "README")` → `fs.readFileSync()`
- 条件付き依存: `if (fileName != "README")` → `relatedFile.match()`

## separateWords()
- 位置: L47-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `str .match()`, `str .match(/[A-Z]?[a-z0-9]+/g) ?.map()`, `str .match(/[A-Z]?[a-z0-9]+/g) ?.map(text => text[0].toUpperCase() + text.substring(1)) .join()`, `text.substring()`, `text[0].toUpperCase()`

## parseStoriesFromMarkdown()
- 位置: L63-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `source.replace()`

## getComponentName()
- 位置: L79-86
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `resourcePath.includes()`
- 条件付き依存: `if (resourcePath.includes("toolkit/content/widgets"))` → `storyNameRegex.exec()`
- 参照: `storyNameRegex.exec(resourcePath)?.groups?.name`

## getStoryTitle()
- 位置: L96-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getComponentName()`, `getTitleFromPath()`, `path .relative()`, `path .relative(projectRoot, resourcePath) .replaceAll()`, `storyTitle.includes()`
- 条件付き依存: `if (componentName)` → `separateWords(componentName).replace()`
- 条件付き依存: `if (componentName)` → `separateWords()`
- 参照: `path.sep`

## getImportPath()
- 位置: L127-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getComponentName()`, `normalizedPath.includes()`, `resourcePath.split()`, `resourcePath.split(path.sep).join()`
- 条件付き依存: `if (componentName)` → `normalizedPath.replace()`
- 条件付き依存: `if (componentName)` → `fs.existsSync()`
- 条件付き依存: `if (!(fs.existsSync(mjsPath)))` → `fs.existsSync()`
- 参照: `path.sep`

## getMDXSource()
- 位置: L167-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getComponentName()`, `getImportPath()`, `parseStoriesFromMarkdown()`
