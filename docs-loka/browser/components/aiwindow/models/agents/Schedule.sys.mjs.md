# browser/components/aiwindow/models/agents/Schedule.sys.mjs

source: browser/components/aiwindow/models/agents/Schedule.sys.mjs
source-hash: 39add5308a1cf48aa49b5e6f96cb6e3706e5952e
lines: 188

## <module>
- 役割: 監視エージェントの実行スケジュール(一定時間ごと、毎日、毎週)の種類と、次回実行時刻の計算を提供するモジュール。

## Schedule.constructor()
- 位置: L22-25
- 役割: スケジュールの種類名を type に入れ、渡されたオプションを自身にコピーする。
- 触るとき: スケジュールの共通フィールドを増やすとき。
- 呼び出し先: `Object.assign()`
- 参照: `this.type`

## Schedule.fromJSON()
- 位置: L31-52
- 役割: 保存データの type を見て対応するサブクラスを作る。すでに getNextRunTime を持つ値はそのまま返す。未知の type は例外。
- 触るとき: 保存されたスケジュールの読み込み経路や、種類の判定を変えるとき。
- 呼び出し先: `DailySchedule.fromJSON()`, `IntervalSchedule.fromJSON()`, `WeeklySchedule.fromJSON()`
- 参照: `schedule.getNextRunTime`, `schedule.type`

## IntervalSchedule.constructor()
- 位置: L62-68
- 役割: 時間数が正の有限値かを確かめ、一定時間ごとのスケジュールを作る。
- 触るとき: 一定時間ごとの時間数の下限や上限を変えるとき。
- 呼び出し先: `Number.isFinite()`, `super()`

## IntervalSchedule.fromJSON()
- 位置: L74-76
- 役割: 保存データの hours を数値に直して IntervalSchedule を作る。
- 触るとき: 保存データの hours の形式を変えるとき。
- 呼び出し先: `Number()`
- 参照: `schedule.hours`

## IntervalSchedule.getNextRunTime()
- 位置: L78-82
- 役割: 前回実行時刻に時間数を足した時刻を返す。前回が無ければ現在時刻から数える。
- 触るとき: 一定時間ごとの次回時刻の計算を変えるとき。
- 呼び出し先: `lastRun.getTime()`
- 参照: `this.hours`

## DailySchedule.constructor()
- 位置: L93-98
- 役割: 時と分の範囲を確かめ、毎日の時刻スケジュールを作る。
- 触るとき: 毎日の実行時刻の範囲を変えるとき。
- 呼び出し先: `super()`, `validateClockHour()`, `validateClockMinute()`

## DailySchedule.fromJSON()
- 位置: L104-106
- 役割: 保存データの時と分を数値にして DailySchedule を作る。
- 触るとき: 毎日の保存データの形式を変えるとき。
- 呼び出し先: `Number()`
- 参照: `schedule.hour`, `schedule.minute`

## DailySchedule.getNextRunTime()
- 位置: L108-118
- 役割: 前回実行時刻の日の指定時刻を求め、それが前回以前なら翌日の同じ時刻を返す。
- 触るとき: 毎日の次回時刻が前後にずれる原因を調べるとき、またはタイムゾーンや夏時間の扱いを変えるとき。
- 呼び出し先: `next.setHours()`
- 条件付き依存: `if (next <= lastRun)` → `next.setDate()`
- 条件付き依存: `if (next <= lastRun)` → `next.getDate()`
- 参照: `this.hour`, `this.minute`

## WeeklySchedule.constructor()
- 位置: L130-136
- 役割: 曜日、時、分の範囲を確かめ、毎週の時刻スケジュールを作る。
- 触るとき: 毎週の曜日や時刻の範囲を変えるとき。
- 呼び出し先: `super()`, `validateClockHour()`, `validateClockMinute()`, `validateWeekday()`

## WeeklySchedule.fromJSON()
- 位置: L142-148
- 役割: 保存データの曜日、時、分を数値にして WeeklySchedule を作る。
- 触るとき: 毎週の保存データの形式を変えるとき。
- 呼び出し先: `Number()`
- 参照: `schedule.hour`, `schedule.minute`, `schedule.weekday`

## WeeklySchedule.getNextRunTime()
- 位置: L154-167
- 役割: 前回実行時刻から次の指定曜日を求め、同じ曜日で時刻が過ぎていれば 1 週間後を返す。
- 触るとき: 毎週の次回時刻の計算を変えるとき、または曜日がずれる原因を調べるとき。
- 呼び出し先: `next.getDate()`, `next.getDay()`, `next.setDate()`, `next.setHours()`
- 参照: `this.hour`, `this.minute`, `this.weekday`

## validateClockHour()
- 位置: L171-175
- 役割: 時が 0〜23 の整数か確かめ、外れていれば例外を投げる。
- 触るとき: 時の検証範囲を変えるとき。
- 呼び出し先: `Number.isInteger()`

## validateClockMinute()
- 位置: L177-181
- 役割: 分が 0〜59 の整数か確かめ、外れていれば例外を投げる。
- 触るとき: 分の検証範囲を変えるとき。
- 呼び出し先: `Number.isInteger()`

## validateWeekday()
- 位置: L183-187
- 役割: 曜日が 0(日)〜6(土) の整数か確かめ、外れていれば例外を投げる。
- 触るとき: 曜日の番号の規則を変えるとき。
- 呼び出し先: `Number.isInteger()`
