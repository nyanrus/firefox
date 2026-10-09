# browser/components/aiwindow/ui/modules/MonitorAttention.sys.mjs

source: browser/components/aiwindow/ui/modules/MonitorAttention.sys.mjs
source-hash: 605225c8d07e1643d723658153c687a822203ae8
lines: 167

## <module>
- 役割: 監視（Monitor）の注意喚起を管理する。一致した監視と確認に失敗した監視を、7 日間だけ保持する設定値に記録する。
- 呼び出し先: `Object.freeze()`

## attentionIds()
- 位置: L42-44
- 役割: 一致と失敗のどちらでも、期限内の監視 ID を新しい順に返す。
- 触るとき: ツールバーのドットを点灯させる対象を変えるとき。
- 呼び出し先: `this._read()`, `this.unexpiredIds()`

## matchedIds()
- 位置: L52-56
- 役割: 期限内に条件へ一致した監視の ID だけを、新しい順に返す。
- 触るとき: パネルの一致の見出しに載る監視を変えるとき。確認失敗はここに含まれない。
- 呼び出し先: `this._read()`, `this._read().filter()`, `this.unexpiredIds()`
- 参照: `ATTENTION_KINDS.MATCH`, `entry.kind`

## hasAttention()
- 位置: L62-64
- 役割: 注意すべき監視が一つでもあるかを返す。
- 触るとき: ツールバーのボタンを点灯させるかどうかの条件を変えるとき。
- 参照: `this.attentionIds.length`

## recordMatch()
- 位置: L69-71
- 役割: 監視の実行が条件に一致したことを、一致の種類で記録する。
- 触るとき: 一致時に注意の記録が残らない問題を調べるとき。
- 呼び出し先: `this._record()`
- 参照: `ATTENTION_KINDS.MATCH`

## recordError()
- 位置: L76-78
- 役割: 監視の確認が失敗したことを、失敗の種類で記録する。
- 触るとき: 確認に失敗したときにドットが点くかを調べるとき。
- 呼び出し先: `this._record()`
- 参照: `ATTENTION_KINDS.ERROR`

## clearAttention()
- 位置: L80-82
- 役割: 保存されている注意の記録を消す。
- 触るとき: パネルを開いた後も点灯が消えない問題を調べるとき。
- 呼び出し先: `Services.prefs.clearUserPref()`
- XPCOM: `Services.prefs`

## parseEntries()
- 位置: L92-112
- 役割: 保存された JSON を読んで検証する。壊れていれば空とみなし、種類の無い旧エントリは一致として補う。
- 触るとき: 保存形式を変えるとき、または旧形式の記録の扱いを調べるとき。
- 呼び出し先: `Array.isArray()`, `JSON.parse()`, `parsed .filter()`, `parsed .filter(entry => entry?.id && typeof entry.at == "number") .map()`
- 参照: `ATTENTION_KINDS.MATCH`, `entry.at`, `entry.kind`, `entry?.id`

## unexpiredIds()
- 位置: L119-122
- 役割: 基準時刻から 7 日以内に記録された監視 ID だけを返す。
- 触るとき: 注意の保持期間を変えるとき、または古い記録が残り続ける問題を調べるとき。
- 呼び出し先: `Date.now()`, `entries.filter()`, `entries.filter(entry => entry.at > cutoff).map()`
- 参照: `entry.at`, `entry.id`

## withEntry()
- 位置: L136-144
- 役割: 同じ監視の古い記録を外し、新しい記録を先頭に加えた配列を返す。
- 触るとき: 監視ごとに一件だけ残す仕組みや並び順を変えるとき。同時刻の記録は配列の順で区別する。
- 呼び出し先: `Date.now()`, `entries.filter()`
- 参照: `ATTENTION_KINDS.MATCH`, `entry.id`

## _record()
- 位置: L150-158
- 役割: 注意の記録を読み、一件追加して設定に保存する。監視 ID が空なら何もしない。
- 触るとき: 一致や失敗の記録が保存されない問題を調べるとき。
- 呼び出し先: `JSON.stringify()`, `Services.prefs.setStringPref()`, `this._read()`, `this.withEntry()`
- XPCOM: `Services.prefs`

## _read()
- 位置: L163-165
- 役割: 設定から注意の記録を読み、解析して返す。
- 触るとき: 保存された記録の読み出し元を確認するとき。
- 呼び出し先: `Services.prefs.getStringPref()`, `this.parseEntries()`
- XPCOM: `Services.prefs`
