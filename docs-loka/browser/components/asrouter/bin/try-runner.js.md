# browser/components/asrouter/bin/try-runner.js

source: browser/components/asrouter/bin/try-runner.js
source-hash: 00fc09ab5aa7fdea62786dc47f45ba4684f6f2b6
lines: 328

## <module>
- 役割: ASRouter 関連のバンドル差分、Karma テスト、カバレッジの zip 化を try 上で順に実行して結果を報告する Node スクリプト。
- 呼び出し先: `main()`, `require()`

## logErrors()
- 位置: L20-25
- 役割: 各エラーを TEST-UNEXPECTED-FAIL 形式で表示し、そのまま返す。
- 触るとき: try の失敗ログの書式を変えるとき。
- 呼び出し先: `console.log()`

## execOut()
- 位置: L27-48
- 役割: コマンドを同期実行し、終了コード、標準出力、標準エラーを返す。失敗時も例外にせず値を返す。
- 触るとき: 外部コマンドの失敗を検出できない、または出力が取れないと調べるとき。
- 呼び出し先: `err.toString()`, `execFileSync()`, `out.toString()`
- 参照: `e.status`, `e.stderr`, `e.stdout`

## logStart()
- 位置: L50-52
- 役割: テスト開始を TEST-START 形式で表示する。
- 触るとき: テスト開始のログ形式を変えるとき。
- 呼び出し先: `console.log()`

## logSkip()
- 位置: L54-56
- 役割: スキップしたテストを TEST-SKIP 形式で表示する。
- 触るとき: 指定されなかったテストの扱いを変えるとき。
- 呼び出し先: `console.log()`

## bundles()
- 位置: L61-165
- 役割: about:welcome と about:asrouter のバンドルを再生成し、対象ファイルが変わっていないか、追加の検査にも通るかを確認する。
- 触るとき: バンドル対象のファイルを増やすとき、または bundles の out of date 失敗を調べるとき。
- 呼び出し先: `Object.keys()`, `execOut()`, `logErrors()`, `logStart()`, `path.join()`, `process.chdir()`, `process.cwd()`, `readFileSync()`
- 条件付き依存: `if (item.before !== after)` → `errors.push()`
- 条件付き依存: `if (item.extraCheck)` → `item.extraCheck()`
- 条件付き依存: `if (extraError)` → `errors.push()`
- 条件付き依存: `if (welcomeBundleExitCode !== 0)` → `errors.push()`
- 条件付き依存: `if (asrouterBundleExitCode !== 0)` → `errors.push()`
- 参照: `errors.length`, `execOut(npmCommand, [ "run", "bundle", ]).exitCode`, `execOut(npmCommand, ["run", "bundle"]).exitCode`, `item.before`, `item.encoding`, `item.extraCheck`, `item.path`

## extraCheck()
- 位置: L75-80
- 役割: aboutwelcome.css に @import が無いことを確認し、あれば理由の文字列を返す。
- 触るとき: CSS の読み込み方の制約を変えるとき。
- 呼び出し先: `content.match()`

## karma()
- 位置: L167-222
- 役割: npm run testmc:unit を実行し、結果 JSON の失敗テストとカバレッジ閾値違反を集めて判定する。
- 触るとき: Karma の失敗が検出されない、または偽陽性が出ると調べるとき。
- 呼び出し先: `Array.from()`, `Array.from(results.result[testArray]).filter()`, `JSON.parse()`, `console.error()`, `console.log()`, `errors.push()`, `execOut()`, `failedTests.map()`, `logErrors()`, `logStart()`, `out.match()`, `path.join()`, `process.cwd()`, `readFileSync()`, `test.suite.join()`
- 条件付き依存: `if (coverage)` → `errors.push()`
- 条件付き依存: `if (coverage)` → `coverage.map()`
- 条件付き依存: `if (coverage)` → `line.match()`
- 参照: `errors.length`, `results.result`, `test.description`, `test.log`, `test.skipped`, `test.success`

## zipCodeCoverage()
- 位置: L224-245
- 役割: logs/coverage/lcov.info を zip して code-coverage-grcov を作る。
- 触るとき: カバレッジの成果物の形式や名前を変えるとき。
- 呼び出し先: `console.log()`, `execOut()`, `logStart()`, `readFileSync()`, `writeFileSync()`

## main()
- 位置: async L248-325
- 役割: 引数とエイリアス(bundle、cov、zip など)から実行するテストを決め、順に実行して終了コードを設定する。
- 触るとき: try の実行対象の指定方法を変えるとき、または新しいテストを追加するとき。
- 呼び出し先: `(aliases[input] || input).toLowerCase()`, `Object.keys()`, `[...cli.input, ...cli.flags.test].map()`, `chalk.green()`, `chalk.red()`, `console.log()`, `import()`, `meow()`, `pathToFileURL()`, `results.every()`, `shouldRunTest()`
- 条件付き依存: `if (shouldRunTest(name))` → `results.push()`
- 条件付き依存: `if (shouldRunTest(name))` → `tests[name]()`
- 条件付き依存: `if (!(shouldRunTest(name)))` → `logSkip()`
- 参照: `cli.flags.test`, `cli.input`, `process.exitCode`

## shouldRunTest()
- 位置: L301-306
- 役割: 指定がなければ全テストを実行し、指定があれば名前が含まれるものだけを実行対象にする。
- 触るとき: テスト名の照合方法(大文字小文字など)を変えるとき。
- 条件付き依存: `if (inputs.length)` → `inputs.includes()`
- 条件付き依存: `if (inputs.length)` → `name.toLowerCase()`
- 参照: `inputs.length`
