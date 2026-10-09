# browser/components/aiwindow/models/agents/Schedule.sys.mjs

source: browser/components/aiwindow/models/agents/Schedule.sys.mjs
source-hash: 39add5308a1cf48aa49b5e6f96cb6e3706e5952e
lines: 188

## <module>
- 役割: (未記入)

## Schedule.constructor()
- 位置: L22-25
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`
- 参照: `this.type`

## Schedule.fromJSON()
- 位置: L31-52
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DailySchedule.fromJSON()`, `IntervalSchedule.fromJSON()`, `WeeklySchedule.fromJSON()`
- 参照: `schedule.getNextRunTime`, `schedule.type`

## IntervalSchedule.constructor()
- 位置: L62-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isFinite()`, `super()`

## IntervalSchedule.fromJSON()
- 位置: L74-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`
- 参照: `schedule.hours`

## IntervalSchedule.getNextRunTime()
- 位置: L78-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lastRun.getTime()`
- 参照: `this.hours`

## DailySchedule.constructor()
- 位置: L93-98
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `validateClockHour()`, `validateClockMinute()`

## DailySchedule.fromJSON()
- 位置: L104-106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`
- 参照: `schedule.hour`, `schedule.minute`

## DailySchedule.getNextRunTime()
- 位置: L108-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `next.setHours()`
- 条件付き依存: `if (next <= lastRun)` → `next.setDate()`
- 条件付き依存: `if (next <= lastRun)` → `next.getDate()`
- 参照: `this.hour`, `this.minute`

## WeeklySchedule.constructor()
- 位置: L130-136
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `validateClockHour()`, `validateClockMinute()`, `validateWeekday()`

## WeeklySchedule.fromJSON()
- 位置: L142-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number()`
- 参照: `schedule.hour`, `schedule.minute`, `schedule.weekday`

## WeeklySchedule.getNextRunTime()
- 位置: L154-167
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `next.getDate()`, `next.getDay()`, `next.setDate()`, `next.setHours()`
- 参照: `this.hour`, `this.minute`, `this.weekday`

## validateClockHour()
- 位置: L171-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isInteger()`

## validateClockMinute()
- 位置: L177-181
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isInteger()`

## validateWeekday()
- 位置: L183-187
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isInteger()`
