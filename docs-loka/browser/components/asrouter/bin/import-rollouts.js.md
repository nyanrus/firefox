# browser/components/asrouter/bin/import-rollouts.js

source: browser/components/asrouter/bin/import-rollouts.js
source-hash: 36bad24b9793720954608ceb0393c2efc07f4f32
lines: 367

## <module>
- 役割: (未記入)
- 呼び出し先: `main()`, `require()`

## fetchJSON()
- 位置: L46-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `https .get()`, `resolve()`, `resp.on()`

## isMessageValid()
- 位置: L60-66
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (validator)` → `validator.validate()`
- 参照: `result.errors.length`, `result.valid`

## getMessageValidators()
- 位置: async L68-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getValidator()`

## getSchema()
- 位置: async L73-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `util.promisify()`, `util.promisify(fs.readFile)()`
- 参照: `fs.readFile`

## getValidator()
- 位置: async L78-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `getSchema()`
- 条件付き依存: `if (common)` → `getSchema()`
- 条件付き依存: `if (common)` → `validator.addSchema()`
- 参照: `jsonschema.Validator`

## annotateMessage()
- 位置: L143-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `JSON.stringify(message, null, 2).replace()`, `comments.join()`
- 条件付き依存: `if (slug)` → `comments.push()`
- 条件付き依存: `if (versionRange)` → `comments.push()`
- 条件付き依存: `if (url)` → `comments.push()`

## format()
- 位置: async L171-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `prettier.format()`, `prettier.resolveConfig()`

## main()
- 位置: async L176-364
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `MESSAGING_EXPERIMENTS_DEFAULT_FEATURES.includes()`, `String()`, `chalk.blue()`, `chalk.green()`, `chalk.underline()`, `chalk.underline.green()`, `chalk.underline.yellow()`, `console.log()`, `fetchJSON()`, `format()`, `getMessageValidators()`, `import()`, `importItems.map()`, `importItems.map(annotateMessage).join()`, `meow()`, `path.resolve()`, `pathToFileURL()`, `record.featureIds.some()`, `records.filter()`, `targeting?.match()`, `util.promisify()`, `util.promisify(fs.writeFile)()`
- 条件付き依存: `if ( MESSAGING_EXPERIMENTS_DEFAULT_FEATURES.includes(feature.featureId) && feature.value && typeof feature.value === "object" && feature.value.template )` → `isMessageValid()`
- 条件付き依存: `if (!isMessageValid(experimentValidator, feature.value))` → `console.log()`
- 条件付き依存: `if (!isMessageValid(experimentValidator, feature.value))` → `chalk.red()`
- 条件付き依存: `if (!isMessageValid(experimentValidator, feature.value))` → `chalk.blue()`
- 条件付き依存: `if ( MESSAGING_EXPERIMENTS_DEFAULT_FEATURES.includes(feature.featureId) && feature.value && typeof feature.value === "object" && feature.value.template )` → `Array.isArray()`
- 条件付き依存: `if ( MESSAGING_EXPERIMENTS_DEFAULT_FEATURES.includes(feature.featureId) && feature.value && typeof feature.value === "object" && feature.value.template )` → `chalk.italic.green()`
- 条件付き依存: `if (!isMessageValid(messageValidators[message.template], message))` → `console.log()`
- 条件付き依存: `if (!isMessageValid(messageValidators[message.template], message))` → `chalk.red()`
- 条件付き依存: `if ( MESSAGING_EXPERIMENTS_DEFAULT_FEATURES.includes(feature.featureId) && feature.value && typeof feature.value === "object" && feature.value.template )` → `console.log()`
- 条件付き依存: `if ( MESSAGING_EXPERIMENTS_DEFAULT_FEATURES.includes(feature.featureId) && feature.value && typeof feature.value === "object" && feature.value.template )` → `importItems.push()`
- 参照: `branches.length`, `cli.flags.collection`, `cli.flags.experiments`, `cli.flags.skipValidation`, `feature.featureId`, `feature.value`, `feature.value.messages`, `feature.value.template`, `fs.writeFile`, `importItems.length`, `m.id`, `message.id`, `message.template`, `messages.length`, `recipe.isRollout`, `record.appId`, `record.application`, `record.isRollout`
