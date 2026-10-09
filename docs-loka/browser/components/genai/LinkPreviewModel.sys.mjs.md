# browser/components/genai/LinkPreviewModel.sys.mjs

source: browser/components/genai/LinkPreviewModel.sys.mjs
source-hash: 55441406dd7dbee166df3f64616df8a12535db6e
lines: 742

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `JSON.parse()`, `JSON.stringify()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## sha256Hex()
- 位置: async L71-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `[...new Uint8Array(digest)] .map()`, `[...new Uint8Array(digest)] .map(b => b.toString(16).padStart(2, "0")) .join()`, `b.toString()`, `b.toString(16).padStart()`, `crypto.subtle.digest()`, `new TextEncoder().encode()`

## runSmokeTest()
- 位置: async L95-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.genaiLinkpreview.smokeTest.record()`, `Services.prefs.getStringPref()`, `Services.prefs.setStringPref()`, `engine.runWithGenerator()`, `sha256Hex()`
- 参照: `chunk.text`, `engine.telemetry?.flowId`, `engine?.pipelineOptions`, `opts.modelId`, `opts.modelRevision`, `opts?.backend`
- XPCOM: `Services.prefs`

## id()
- 位置: L237-239
- 役割: (未記入)
- 触るとき: (未記入)

## engineId()
- 位置: L241-243
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.FEATURES`, `lazy.FEATURES[this.id].engineId`, `this.id`

## getBlockTokenList()
- 位置: L250-252
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.penalizedTokens`

## getSentences()
- 位置: L259-397
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`, `abbrev .replace()`, `abbrev .replace(/[.*+?^${}()|[\]\\]/g, "\\$&") .replace()`, `abbrev.replace()`, `abbreviations.forEach()`, `modifiedText.replace()`, `segmenter.segment()`, `sentence.replace()`, `sentences.map()`
- 参照: `Intl.Segmenter`, `segment.segment`

## preprocessText()
- 位置: L406-441
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/\p{P}$/u.test()`, `s.split()`, `s.trim()`, `s.trim().replace()`, `text.replace()`, `this.getSentences()`, `this.getSentences(textWithoutEmoji) .map()`
- 参照: `lazy.inputSentences`, `s.length`, `s.split(" ").length`

## createEngine()
- 位置: async L451-453
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.createEngine()`

## generateTextAI()
- 位置: async L465-589
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array()`, `Array(blockedTokens.length).fill()`, `JSON.parse()`, `Math.ceil()`, `SentencePostProcessor.initialize()`, `console.error()`, `engine.runWithGenerator()`, `engine?.terminate()`, `lazy.RemoteSettingsManager.getRemoteData()`, `onError()`, `postProcessor.put()`, `this.createEngine()`, `this.getBlockTokenList()`, `this.preprocessText()`
- 条件付き依存: `if (data.type == lazy.Progress.ProgressType.DOWNLOAD)` → `onDownload()`
- 条件付き依存: `if (data.type == lazy.Progress.ProgressType.DOWNLOAD)` → `Math.round()`
- 条件付き依存: `if (sentence)` → `onText()`
- 条件付き依存: `if (!val.text)` → `postProcessor.flush()`
- 条件付き依存: `if (remaining)` → `onText()`
- 条件付き依存: `if (!abandonedGeneration)` → `runSmokeTest()`
- 参照: `Services.appinfo.appBuildID`, `blockedTokens.length`, `data.statusText`, `data.total`, `data.totalLoaded`, `data.type`, `lazy.Progress.ProgressStatusText.DONE`, `lazy.Progress.ProgressType.DOWNLOAD`, `lazy.config`, `lazy.inputSentences`, `lazy.postUserPrompt`, `lazy.preUserPrompt`, `lazy.prompt`, `lazy.stopTokens`, `processedInput.length`, `remoteRequestOptions?.inputSentences`, `remoteRequestOptions?.systemPrompt`, `remoteRequestRecord.options`, `remoteRequestRecord?.options`, `systemPrompt.length`, `this.engineId`, `this.id`, `val.text`
- XPCOM: `Services.appinfo`

## SentencePostProcessor.constructor()
- 位置: L637-643
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.outputSentences`, `this.blockListManager`, `this.maxNumOutputSentences`

## SentencePostProcessor.initialize()
- 位置: async L653-673
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!LinkPreviewModel.blockListManager)` → `lazy.BlockListManager.initializeFromRemoteSettings()`
- 参照: `LinkPreviewModel.blockListManager`, `lazy.blockListEnabled`, `lazy.outputSentences`

## SentencePostProcessor.put()
- 位置: L685-730
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LinkPreviewModel.getSentences()`
- 条件付き依存: `if (sentences.length >= 2)` → `sentences.slice(1).join()`
- 条件付き依存: `if (sentences.length >= 2)` → `sentences.slice()`
- 条件付き依存: `if (sentences.length >= 2)` → `sentences[0].trim().split()`
- 条件付き依存: `if (sentences.length >= 2)` → `sentences[0].trim()`
- 条件付き依存: `if (sentences.length >= 2)` → `this.blockListManager.matchAtWordBoundary()`
- 条件付き依存: `if (sentences.length >= 2)` → `sentence.toLowerCase()`
- 参照: `lazy.minWordsPerOutputSentences`, `sentences.length`, `sentences[0].trim().split(/\p{White_Space}+/u).length`, `this.blockListManager`, `this.currentNumSentences`, `this.currentText`, `this.maxNumOutputSentences`

## SentencePostProcessor.flush()
- 位置: L738-740
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.currentText`
