# browser/extensions/newtab/bin/try-runner.js

source: browser/extensions/newtab/bin/try-runner.js
source-hash: b2366d164fa1294bedd1c5f1ed509edd83856c33
lines: 264

## <module>
- 役割: (未記入)
- 呼び出し先: `main()`, `require()`

## logErrors()
- 位置: L19-24
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.log()`

## execOut()
- 位置: L26-47
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `err.toString()`, `execFileSync()`, `out.toString()`
- 参照: `e.status`, `e.stderr`, `e.stdout`

## logStart()
- 位置: L49-51
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.log()`

## logSkip()
- 位置: L53-55
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.log()`

## bundles()
- 位置: L60-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `execOut()`, `logErrors()`, `logStart()`, `path.join()`, `readFileSync()`
- 条件付き依存: `if (item.before !== after)` → `errors.push()`
- 条件付き依存: `if (item.extraCheck)` → `item.extraCheck()`
- 条件付き依存: `if (extraError)` → `errors.push()`
- 条件付き依存: `if (newtabBundleExitCode !== 0)` → `errors.push()`
- 参照: `errors.length`, `execOut(npmCommand, ["run", "bundle"]).exitCode`, `item.before`, `item.encoding`, `item.extraCheck`, `item.path`

## jest()
- 位置: L107-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `a.ancestorTitles.join()`, `a.failureMessages.join()`, `console.error()`, `console.log()`, `errors.push()`, `execOut()`, `failed.map()`, `logErrors()`, `logStart()`, `path.join()`, `process.cwd()`, `readFileSync()`, `testResult.assertionResults.filter()`
- 条件付き依存: `if (testResult.status === "failed" && !failed.length)` → `errors.push()`
- 参照: `a.status`, `a.title`, `errors.length`, `failed.length`, `results.testResults`, `testResult.message`, `testResult.name`, `testResult.status`

## zipCodeCoverage()
- 位置: L166-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.log()`, `execOut()`, `logStart()`

## main()
- 位置: async L185-261
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(aliases[input] || input).toLowerCase()`, `Object.keys()`, `[...cli.input, ...cli.flags.test].map()`, `console.log()`, `import()`, `meow()`, `pathToFileURL()`, `results.every()`, `shouldRunTest()`
- 条件付き依存: `if (shouldRunTest(name))` → `results.push()`
- 条件付き依存: `if (shouldRunTest(name))` → `tests[name]()`
- 条件付き依存: `if (!(shouldRunTest(name)))` → `logSkip()`
- 参照: `cli.flags.test`, `cli.input`, `process.exitCode`

## shouldRunTest()
- 位置: L238-243
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (inputs.length)` → `inputs.includes()`
- 条件付き依存: `if (inputs.length)` → `name.toLowerCase()`
- 参照: `inputs.length`
