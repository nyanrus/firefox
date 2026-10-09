# browser/components/asrouter/bin/try-runner.js

source: browser/components/asrouter/bin/try-runner.js
source-hash: 00fc09ab5aa7fdea62786dc47f45ba4684f6f2b6
lines: 328

## <module>
- 役割: (未記入)
- 呼び出し先: `main()`, `require()`

## logErrors()
- 位置: L20-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.log()`

## execOut()
- 位置: L27-48
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `err.toString()`, `execFileSync()`, `out.toString()`
- 参照: `e.status`, `e.stderr`, `e.stdout`

## logStart()
- 位置: L50-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.log()`

## logSkip()
- 位置: L54-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.log()`

## bundles()
- 位置: L61-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `execOut()`, `logErrors()`, `logStart()`, `path.join()`, `process.chdir()`, `process.cwd()`, `readFileSync()`
- 条件付き依存: `if (item.before !== after)` → `errors.push()`
- 条件付き依存: `if (item.extraCheck)` → `item.extraCheck()`
- 条件付き依存: `if (extraError)` → `errors.push()`
- 条件付き依存: `if (welcomeBundleExitCode !== 0)` → `errors.push()`
- 条件付き依存: `if (asrouterBundleExitCode !== 0)` → `errors.push()`
- 参照: `errors.length`, `execOut(npmCommand, [ "run", "bundle", ]).exitCode`, `execOut(npmCommand, ["run", "bundle"]).exitCode`, `item.before`, `item.encoding`, `item.extraCheck`, `item.path`

## extraCheck()
- 位置: L75-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `content.match()`

## karma()
- 位置: L167-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `Array.from(results.result[testArray]).filter()`, `JSON.parse()`, `console.error()`, `console.log()`, `errors.push()`, `execOut()`, `failedTests.map()`, `logErrors()`, `logStart()`, `out.match()`, `path.join()`, `process.cwd()`, `readFileSync()`, `test.suite.join()`
- 条件付き依存: `if (coverage)` → `errors.push()`
- 条件付き依存: `if (coverage)` → `coverage.map()`
- 条件付き依存: `if (coverage)` → `line.match()`
- 参照: `errors.length`, `results.result`, `test.description`, `test.log`, `test.skipped`, `test.success`

## zipCodeCoverage()
- 位置: L224-245
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.log()`, `execOut()`, `logStart()`, `readFileSync()`, `writeFileSync()`

## main()
- 位置: async L248-325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(aliases[input] || input).toLowerCase()`, `Object.keys()`, `[...cli.input, ...cli.flags.test].map()`, `chalk.green()`, `chalk.red()`, `console.log()`, `import()`, `meow()`, `pathToFileURL()`, `results.every()`, `shouldRunTest()`
- 条件付き依存: `if (shouldRunTest(name))` → `results.push()`
- 条件付き依存: `if (shouldRunTest(name))` → `tests[name]()`
- 条件付き依存: `if (!(shouldRunTest(name)))` → `logSkip()`
- 参照: `cli.flags.test`, `cli.input`, `process.exitCode`

## shouldRunTest()
- 位置: L301-306
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (inputs.length)` → `inputs.includes()`
- 条件付き依存: `if (inputs.length)` → `name.toLowerCase()`
- 参照: `inputs.length`
