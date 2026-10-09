# browser/components/backup/MeasurementUtils.sys.mjs

source: browser/components/backup/MeasurementUtils.sys.mjs
source-hash: bcab7101127651955226e3b703e726fab4ebd464
lines: 61

## <module>
- 役割: (未記入)

## fuzzByteSize()
- 位置: L29-32
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.round()`

## measure()
- 位置: async L48-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `timer.cancel()`, `timer.start()`, `timer.stopAndAccumulate()`
