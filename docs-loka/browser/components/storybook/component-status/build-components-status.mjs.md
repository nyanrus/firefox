# browser/components/storybook/component-status/build-components-status.mjs

source: browser/components/storybook/component-status/build-components-status.mjs
source-hash: e26c882ff52c83c809bb4060c79987b4497f54cf
lines: 222

## <module>
- 役割: (未記入)
- 呼び出し先: `JSON.stringify()`, `buildItems()`, `console.warn()`, `fileURLToPath()`, `fs.writeFileSync()`, `new Date().toISOString()`, `path.dirname()`, `path.join()`, `path.resolve()`, `readJsonIfExists()`

## readJsonIfExists()
- 位置: L34-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `fs.existsSync()`
- 条件付き依存: `if (fs.existsSync(filePath))` → `fs.readFileSync()`
- 条件付き依存: `if (fs.existsSync(filePath))` → `JSON.parse()`

## slugify()
- 位置: L50-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `String()`, `String(str).trim()`, `String(str).trim().toLowerCase()`, `s.replace()`

## getBugzillaUrl()
- 位置: L61-65
- 役割: (未記入)
- 触るとき: (未記入)

## readFileSafe()
- 位置: L67-73
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `fs.readFileSync()`

## findStoriesFiles()
- 位置: L75-88
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/\.stories\.mjs$/i.test()`, `console.error()`, `ent.isDirectory()`, `ent.isFile()`, `fs.readdirSync()`, `fs.readdirSync(dir, { withFileTypes: true }).flatMap()`, `path.join()`
- 条件付き依存: `if (ent.isDirectory())` → `findStoriesFiles()`
- 参照: `ent.name`

## parseMeta()
- 位置: L92-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `paramsContent.match()`, `src.match()`
- 条件付き依存: `if (titleMatch && titleMatch[2])` → `titleMatch[2].trim()`
- 条件付き依存: `if (stringStatusMatch && stringStatusMatch[2])` → `stringStatusMatch[2].trim().toLowerCase()`
- 条件付き依存: `if (stringStatusMatch && stringStatusMatch[2])` → `stringStatusMatch[2].trim()`
- 条件付き依存: `if (objectStatusMatch && objectStatusMatch[2])` → `objectStatusMatch[2].trim().toLowerCase()`
- 条件付き依存: `if (objectStatusMatch && objectStatusMatch[2])` → `objectStatusMatch[2].trim()`
- 参照: `meta.status`, `meta.title`

## pickExportName()
- 位置: L135-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `n.toLowerCase()`, `names.push()`, `names[0].toLowerCase()`, `re.exec()`
- 参照: `names.length`

## componentSlug()
- 位置: L153-162
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `parts[parts.length - 1].trim()`, `path.relative()`, `rel.split()`, `slugify()`, `title.split()`
- 参照: `parts.length`, `path.sep`

## buildItems()
- 位置: L165-209
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `a.component.localeCompare()`, `componentSlug()`, `encodeURIComponent()`, `findStoriesFiles()`, `getBugzillaUrl()`, `items.push()`, `items.sort()`, `parseMeta()`, `pickExportName()`, `readFileSafe()`, `slugify()`
- 参照: `b.component`, `meta.status`, `meta.title`
