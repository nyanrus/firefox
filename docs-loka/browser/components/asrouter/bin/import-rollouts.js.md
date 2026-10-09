# browser/components/asrouter/bin/import-rollouts.js

source: browser/components/asrouter/bin/import-rollouts.js
source-hash: 36bad24b9793720954608ceb0393c2efc07f4f32
lines: 367

## <module>
- 役割: Nimbus のメッセージ用実験・ロールアウトを取得し、テスト用の NimbusRolloutMessageProvider.sys.mjs を生成する開発用 Node スクリプト。
- 呼び出し先: `main()`, `require()`

## fetchJSON()
- 位置: L46-58
- 役割: 指定 URL を https で取得し、本文を JSON として解析して返す。
- 触るとき: Nimbus レコードの取得方法や取得失敗時の挙動を変えるとき。
- 呼び出し先: `JSON.parse()`, `https .get()`, `resolve()`, `resp.on()`

## isMessageValid()
- 位置: L60-66
- 役割: バリデータがあれば JSON スキーマで検査し、エラーがなければ true を返す。バリデータがなければ常に true。
- 触るとき: 取り込むメッセージの検証基準を変えるとき、または有効なのに弾かれるメッセージを調べるとき。
- 条件付き依存: `if (validator)` → `validator.validate()`
- 参照: `result.errors.length`, `result.valid`

## getMessageValidators()
- 位置: async L68-141
- 役割: 実験用のスキーマと、テンプレートごとのスキーマ(共通スキーマ付き)を読み込んで検証器を組み立てる。skipValidation なら空を返す。
- 触るとき: 新しいテンプレートを取り込み対象に加えるとき、またはテンプレートとスキーマの対応を直すとき。
- 呼び出し先: `getValidator()`

## getSchema()
- 位置: async L73-76
- 役割: 指定パスの JSON スキーマファイルを読んで解析する。
- 触るとき: スキーマファイルの読み込み方法を変えるとき。
- 呼び出し先: `JSON.parse()`, `util.promisify()`, `util.promisify(fs.readFile)()`
- 参照: `fs.readFile`

## getValidator()
- 位置: async L78-90
- 役割: スキーマから検証器を作り、common が指定されていれば FxMSCommon スキーマを追加する。
- 触るとき: 共通スキーマの適用範囲を変えるとき。
- 呼び出し先: `getSchema()`
- 条件付き依存: `if (common)` → `getSchema()`
- 条件付き依存: `if (common)` → `validator.addSchema()`
- 参照: `jsonschema.Validator`

## annotateMessage()
- 位置: L143-169
- 役割: メッセージの JSON 表現の先頭に、Nimbus slug、バージョン範囲、レシピ URL のコメントを付けた文字列を作る。
- 触るとき: 生成ファイルに付く注釈の形式を変えるとき、またはバージョン範囲の表示がずれると調べるとき。
- 呼び出し先: `JSON.stringify()`, `JSON.stringify(message, null, 2).replace()`, `comments.join()`
- 条件付き依存: `if (slug)` → `comments.push()`
- 条件付き依存: `if (versionRange)` → `comments.push()`
- 条件付き依存: `if (url)` → `comments.push()`

## format()
- 位置: async L171-174
- 役割: 生成内容を、リポジトリの .prettierrc.js の設定で prettier 整形する。
- 触るとき: 生成ファイルの整形ルールを変えるとき。
- 呼び出し先: `prettier.format()`, `prettier.resolveConfig()`

## main()
- 位置: async L176-364
- 役割: CLI オプションを読み、Nimbus のレコードを絞り込み、ブランチごとに検証済みのメッセージを集めて、テスト用ファイルへ書き出す。
- 触るとき: 取り込み対象の条件(ロールアウトのみか、実験も含めるか、機能 ID)を変えるとき、または生成ファイルの内容が想定と違うと調べるとき。
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
