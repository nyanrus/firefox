# browser/extensions/newtab/bin/render-activity-stream-html.js

source: browser/extensions/newtab/bin/render-activity-stream-html.js
source-hash: b6f91d15e39cfb404fdd0ea90739d6356ab44370
lines: 254

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.assign()`, `main()`, `require()`, `templateHTML()`

## templateHTML()
- 位置: L29-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `scripts .map()`, `scripts .map(script => ` <script src="${script}"></script>`) .join()`
- 参照: `options.baseUrl`, `options.noscripts`

## writeFiles()
- 位置: L175-180
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.log()`, `fs.writeFileSync()`, `path.join()`, `templater()`

## main()
- 位置: async L200-251
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.log()`, `import()`, `meow()`, `mkdir()`, `path.join()`, `path.resolve()`, `pathToFileURL()`, `writeFiles()`
- 参照: `DEFAULT_OPTIONS.addonPath`, `DEFAULT_OPTIONS.baseUrl`, `cli.flags`, `options.addonPath`
