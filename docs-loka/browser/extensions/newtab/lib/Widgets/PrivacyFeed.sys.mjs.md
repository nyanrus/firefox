# browser/extensions/newtab/lib/Widgets/PrivacyFeed.sys.mjs

source: browser/extensions/newtab/lib/Widgets/PrivacyFeed.sys.mjs
source-hash: b3fd87309e607f558d81d8aa77bcd39cf91f6d1b
lines: 657

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `WIDGET_REGISTRY.find()`, `XPCOMUtils.defineLazyServiceGetter()`

## utcDayKey()
- 位置: L64-64
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new Date().toISOString()`, `new Date().toISOString().slice()`

## PrivacyFeed.constructor()
- 位置: L104-116
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._countsFetching`, `this._etpOff`, `this._lastCountsAt`, `this._messageQueue`, `this._profileCreatedMs`

## PrivacyFeed.enabled()
- 位置: L118-125
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `isWidgetEnabled()`, `this.store.getState()`
- 参照: `this.store.getState()?.Prefs.values`

## PrivacyFeed.getSitesVisitedToday()
- 位置: async L137-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `db.execute()`, `lazy.PlacesUtils.promiseDBConnection()`, `rows[0]?.getResultByName()`

## PrivacyFeed.getPeriodTotals()
- 位置: async L170-214
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.parse()`, `lazy.TrackingDBService.getEventsByDateRange()`, `new Date(now - i * DAY_MS).toISOString()`, `new Date(now - i * DAY_MS).toISOString().slice()`, `perDay.get()`, `perDay.set()`, `periodBounds()`, `row.getResultByName()`
- 参照: `bounds.month.startMs`, `bounds.week.startMs`, `bounds.year.startMs`

## PrivacyFeed.getFeatureFlags()
- 位置: async L223-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.logins.countLoginsAsync()`, `lazy.FirefoxRelay.getRelayProfileInfo()`, `lazy.UIState.get()`
- 参照: `lazy.UIState.STATUS_SIGNED_IN`, `lazy.UIState.get().status`, `profile?.masksCount`
- XPCOM: `Services.logins`

## PrivacyFeed.getProfileCreatedMs()
- 位置: L240-250
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ProfileAge()`
- 参照: `accessor.created`, `this._profileCreatedMs`

## PrivacyFeed.readMessageState()
- 位置: L253-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `this.store.getState()`
- 参照: `this.store.getState()?.Prefs.values`

## PrivacyFeed.writeMessageState()
- 位置: L266-270
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `ac.SetPref()`, `this.store.dispatch()`

## PrivacyFeed.readCelebrationState()
- 位置: L275-297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.store.getState()`
- 条件付き依存: `if (raw)` → `JSON.parse()`
- 参照: `parsed.baselineCount`, `parsed.date`, `parsed.pending`, `this.store.getState()?.Prefs.values`

## PrivacyFeed.writeCelebrationState()
- 位置: L299-303
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `ac.SetPref()`, `this.store.dispatch()`

## PrivacyFeed.resolveCelebration()
- 位置: L314-370
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `resolvePrivacyCelebrationThreshold()`, `this.readCelebrationState()`, `this.store.getState()`, `utcDayKey()`
- 条件付き依存: `if (forcedTier)` → `Date.now()`
- 条件付き依存: `if (forcedTier)` → `Math.max()`
- 条件付き依存: `if (state.date !== today || trackersToday < state.baselineCount)` → `this.writeCelebrationState()`
- 条件付き依存: `if (trackersToday - state.baselineCount >= threshold)` → `Date.now()`
- 条件付き依存: `if (trackersToday - state.baselineCount >= threshold)` → `this.writeCelebrationState()`
- 条件付き依存: `if ( state.pending && Date.now() - state.pending.awardedAt >= CELEBRATION_WINDOW_MS )` → `this.writeCelebrationState()`
- 参照: `state.baselineCount`, `state.date`, `state.pending`, `state.pending.awardedAt`, `this.store.getState().Prefs.values`

## PrivacyFeed.isEtpOff()
- 位置: L379-401
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getIntPref()`, `isPrefOn()`
- XPCOM: `Services.prefs`

## isPrefOn()
- 位置: L380-380
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## PrivacyFeed.fetchTodayCounts()
- 位置: async L406-417
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `Promise.all()`, `lazy.PrivacyMetricsService.getTodayStats()`, `this.getSitesVisitedToday()`
- 参照: `stats.lastUpdated`, `stats.total`, `this._lastCountsAt`

## PrivacyFeed.updateCounts()
- 位置: async L422-438
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.BroadcastToContent()`, `this.fetchTodayCounts()`, `this.isEtpOff()`, `this.resolveCelebration()`, `this.store.dispatch()`
- 参照: `at.WIDGETS_PRIVACY_UPDATE`, `counts.trackersToday`

## PrivacyFeed.refreshCountsForView()
- 位置: async L442-464
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `ac.BroadcastToContent()`, `this.fetchTodayCounts()`, `this.store.dispatch()`
- 参照: `at.WIDGETS_PRIVACY_UPDATE`, `this._countsFetching`, `this._lastCountsAt`

## PrivacyFeed.updateMessage()
- 位置: L484-489
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(this._messageQueue ?? Promise.resolve()) .catch()`, `(this._messageQueue ?? Promise.resolve()) .catch(() => {}) .then()`, `Promise.resolve()`, `this._runMessageSelection()`
- 参照: `this._messageQueue`

## PrivacyFeed._runMessageSelection()
- 位置: async L491-558
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.now()`, `JSON.stringify()`, `Promise.all()`, `Services.prefs.getBoolPref()`, `ac.BroadcastToContent()`, `resolvePrivacyBlankChance()`, `resolvePrivacyMaxCount()`, `resolvePrivacyShowVpnMessages()`, `selectPrivacyMessage()`, `this.fetchTodayCounts()`, `this.getFeatureFlags()`, `this.getPeriodTotals()`, `this.getProfileCreatedMs()`, `this.isEtpOff()`, `this.readMessageState()`, `this.resolveCelebration()`, `this.store.dispatch()`, `this.store.getState()`
- 条件付き依存: `if (JSON.stringify(nextState) !== JSON.stringify(prevState))` → `this.writeMessageState()`
- 参照: `Math.random`, `at.WIDGETS_PRIVACY_UPDATE`, `counts.sitesToday`, `counts.trackersToday`, `decision.category`, `decision.countArg`, `decision.countCeiling`, `decision.cta`, `decision.icon`, `decision.messageId`, `decision.variant`, `this.store.getState().Prefs.values`, `totals.allTimeTotal`, `totals.monthTotal`, `totals.streakDays`, `totals.weekTotal`, `totals.yearTotal`
- XPCOM: `Services.prefs`

## PrivacyFeed.handleCtaAction()
- 位置: L562-569
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SpecialMessageActions.handleAction()`
- 参照: `action._target?.browser`, `action.data?.action`

## PrivacyFeed.init()
- 位置: L573-578
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.addObserver()`, `this.isEtpOff()`
- 参照: `this._etpOff`
- XPCOM: `Services.prefs`

## PrivacyFeed.uninit()
- 位置: L580-584
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.removeObserver()`
- XPCOM: `Services.prefs`

## PrivacyFeed.observe()
- 位置: L586-604
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ETP_PREFS.includes()`, `this.isEtpOff()`
- 条件付き依存: `if (this.enabled)` → `this.updateCounts()`
- 参照: `this._etpOff`, `this.enabled`

## PrivacyFeed.onAction()
- 位置: async L606-655
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ENABLEMENT_PREFS.has()`, `this.handleCtaAction()`, `this.init()`, `this.readCelebrationState()`, `this.uninit()`
- 条件付き依存: `if (this.enabled)` → `this.updateCounts()`
- 条件付き依存: `if (this.enabled)` → `this.updateMessage()`
- 条件付き依存: `if (this.enabled)` → `this.refreshCountsForView()`
- 条件付き依存: `if (ENABLEMENT_PREFS.has(action.data?.name) && this.enabled)` → `this.updateCounts()`
- 条件付き依存: `if (state.pending?.awardedAt === action.data)` → `this.writeCelebrationState()`
- 参照: `action.data`, `action.data?.name`, `action.type`, `at.INIT`, `at.NEW_TAB_INIT`, `at.PREF_CHANGED`, `at.SYSTEM_TICK`, `at.UNINIT`, `at.WIDGETS_PRIVACY_CTA`, `at.WIDGETS_PRIVACY_MARK_CELEBRATED`, `at.WIDGETS_PRIVACY_VISIBLE`, `state.pending?.awardedAt`, `this.enabled`
