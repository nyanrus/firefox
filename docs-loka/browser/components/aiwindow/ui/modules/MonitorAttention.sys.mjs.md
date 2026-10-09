# browser/components/aiwindow/ui/modules/MonitorAttention.sys.mjs

source: browser/components/aiwindow/ui/modules/MonitorAttention.sys.mjs
source-hash: 605225c8d07e1643d723658153c687a822203ae8
lines: 167

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.freeze()`

## attentionIds()
- 位置: L42-44
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._read()`, `this.unexpiredIds()`

## matchedIds()
- 位置: L52-56
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._read()`, `this._read().filter()`, `this.unexpiredIds()`
- 参照: `ATTENTION_KINDS.MATCH`, `entry.kind`

## hasAttention()
- 位置: L62-64
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.attentionIds.length`

## recordMatch()
- 位置: L69-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._record()`
- 参照: `ATTENTION_KINDS.MATCH`

## recordError()
- 位置: L76-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._record()`
- 参照: `ATTENTION_KINDS.ERROR`

## clearAttention()
- 位置: L80-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.clearUserPref()`
- XPCOM: `Services.prefs`

## parseEntries()
- 位置: L92-112
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `JSON.parse()`, `parsed .filter()`, `parsed .filter(entry => entry?.id && typeof entry.at == "number") .map()`
- 参照: `ATTENTION_KINDS.MATCH`, `entry.at`, `entry.kind`, `entry?.id`

## unexpiredIds()
- 位置: L119-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `entries.filter()`, `entries.filter(entry => entry.at > cutoff).map()`
- 参照: `entry.at`, `entry.id`

## withEntry()
- 位置: L136-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `entries.filter()`
- 参照: `ATTENTION_KINDS.MATCH`, `entry.id`

## _record()
- 位置: L150-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setStringPref()`, `this._read()`, `this.withEntry()`
- XPCOM: `Services.prefs`

## _read()
- 位置: L163-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getStringPref()`, `this.parseEntries()`
- XPCOM: `Services.prefs`
