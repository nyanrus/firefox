# browser/components/aiwindow/models/IntentClassifier.sys.mjs

source: browser/components/aiwindow/models/IntentClassifier.sys.mjs
source-hash: 88e22f24e497c539b5c9f52224d5544fade38af2
lines: 334

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## normalizeTextForChatAllowlist()
- 位置: L163-174
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `s .normalize()`, `s .normalize("NFKC") .toLowerCase()`, `s .normalize("NFKC") .toLowerCase() .normalize()`, `s .normalize("NFKC") .toLowerCase() .normalize("NFD") .replace()`, `s .normalize("NFKC") .toLowerCase() .normalize("NFD") .replace(/\p{M}/gu, "") .replace()`, `s .normalize("NFKC") .toLowerCase() .normalize("NFD") .replace(/\p{M}/gu, "") .replace(/\s+/g, " ") .trim()`

## tokenizeTextForChatAllowlist()
- 位置: L177-181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `normalizeTextForChatAllowlist()`, `normalizeTextForChatAllowlist(s) .split()`, `normalizeTextForChatAllowlist(s) .split(/[^\p{L}\p{N}_]+/u) .filter()`

## buildChatAllowlist()
- 位置: L183-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `byLen.get()`, `byLen.get(k).add()`, `byLen.has()`, `key.split()`, `tokenizeTextForChatAllowlist()`, `tokenizeTextForChatAllowlist(p).join()`
- 条件付き依存: `if (!byLen.has(k))` → `byLen.set()`
- 参照: `key.split(" ").length`

## makeIsolatedPhraseChecker()
- 位置: L200-222
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `buildChatAllowlist()`

## containsIsolatedPhrase()
- 位置: L204-221
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cache.has()`, `cache.set()`, `normalizeTextForChatAllowlist()`, `qNorm.split()`, `qNorm.split(/[^\p{L}\p{N}_]+/u).filter()`, `set.has()`, `toks.slice()`, `toks.slice(i, i + k).join()`
- 条件付き依存: `if (cache.has(qNorm))` → `cache.get()`
- 条件付き依存: `if (set.has(toks.slice(i, i + k).join(" ")))` → `cache.set()`
- 参照: `toks.length`

## getIntentModelInfoForLocale()
- 位置: L230-241
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.Region.home`

## getForcedChatPhrasesForModel()
- 位置: L250-255
- 役割: (未記入)
- 触るとき: (未記入)

## _isForcedChat()
- 位置: L279-288
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `checker()`, `this._forcedChatCheckers.get()`
- 条件付き依存: `if (!checker)` → `makeIsolatedPhraseChecker()`
- 条件付き依存: `if (!checker)` → `getForcedChatPhrasesForModel()`
- 条件付き依存: `if (!checker)` → `this._forcedChatCheckers.set()`

## getPromptIntent()
- 位置: async L296-322
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `engine.run()`, `getIntentModelInfoForLocale()`, `resp[0].label.toLowerCase()`, `this._createEngine()`, `this._isForcedChat()`, `this._preprocessQuery()`
- 参照: `modelInfo.modelId`, `resp[0].score`

## _preprocessQuery()
- 位置: L325-332
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `query.replace()`, `query.replace(/\?/g, "").trim()`
