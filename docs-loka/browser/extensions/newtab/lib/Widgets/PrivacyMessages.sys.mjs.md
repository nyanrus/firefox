# browser/extensions/newtab/lib/Widgets/PrivacyMessages.sys.mjs

source: browser/extensions/newtab/lib/Widgets/PrivacyMessages.sys.mjs
source-hash: dacbe56795bcda9f29317bac0892fd4ad73aba47
lines: 754

## <module>
- 役割: (未記入)
- 呼び出し先: `ctaAboutPage()`, `ctaAttributedUrl()`, `ctaUrl()`

## ctaAboutPage()
- 位置: L123-126
- 役割: (未記入)
- 触るとき: (未記入)

## ctaUrl()
- 位置: L127-127
- 役割: (未記入)
- 触るとき: (未記入)

## ctaAttributedUrl()
- 位置: L135-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ctaUrl()`

## startOfUTCDay()
- 位置: L415-418
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.UTC()`, `d.getUTCDate()`, `d.getUTCFullYear()`, `d.getUTCMonth()`

## utcDayKey()
- 位置: L420-422
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new Date(startOfUTCDay(ms)).toISOString()`, `new Date(startOfUTCDay(ms)).toISOString().slice()`, `startOfUTCDay()`

## periodBounds()
- 位置: L432-447
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Date.UTC()`, `d.getUTCDay()`, `d.getUTCFullYear()`, `d.getUTCMonth()`, `startOfUTCDay()`, `utcDayKey()`

## normalizeState()
- 位置: L449-463
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `s.dayStamp`, `s.firstProtectionShown`, `s.lastCelebrationDay`, `s.lastShownMs`, `s.messageLastShown`, `s.milestoneWatermark`, `s.promoLastDay`, `s.recentId`, `s.shownToday`, `s.streakFiredAt`

## countArgFor()
- 位置: L465-484
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `ctx.allTimeTotal`, `ctx.monthTotal`, `ctx.sitesToday`, `ctx.streakDays`, `ctx.trackersToday`, `ctx.weekTotal`, `ctx.yearTotal`, `msg.countSource`

## toDecision()
- 位置: L486-501
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `msg.category`, `msg.cta`, `msg.icon`, `msg.id`

## blankDecision()
- 位置: L503-516
- 役割: (未記入)
- 触るとき: (未記入)

## firstByCategory()
- 位置: L518-520
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PRIVACY_MESSAGES.find()`
- 参照: `m.category`

## variantForCategory()
- 位置: L524-532
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `CATEGORY.STREAK`

## forcedResult()
- 位置: L537-556
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PRIVACY_MESSAGES.find()`, `countArgFor()`, `toDecision()`, `variantForCategory()`
- 参照: `EMPTY_MESSAGE.id`, `ctx.forceMessageId`, `forced.category`, `m.id`

## isFeatureInUse()
- 位置: L558-570
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `features.hasLogins`, `features.relayMasks`, `features.signedIn`

## detectMilestone()
- 位置: L574-600
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MILESTONE_TIERS[period].filter()`
- 参照: `CATEGORY.MILESTONE_MONTH`, `CATEGORY.MILESTONE_TOTAL`, `CATEGORY.MILESTONE_WEEK`, `CATEGORY.MILESTONE_YEAR`, `bounds.month.key`, `bounds.week.key`, `bounds.year.key`, `crossed.length`, `ctx.allTimeTotal`, `ctx.monthTotal`, `ctx.weekTotal`, `ctx.yearTotal`, `state.milestoneWatermark`, `wm.key`, `wm.tier`

## buildPool()
- 位置: L602-625
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PRIVACY_MESSAGES.filter()`
- 条件付き依存: `if (state.promoLastDay !== today)` → `isFeatureInUse()`
- 条件付き依存: `if ( m.category === CATEGORY.PROMO && m.id !== recent && !isFeatureInUse(m.feature, ctx.features) && // VPN promos need both gates: showVpnMessages (operator/exp...)` → `pool.push()`
- 参照: `CATEGORY.INFO`, `CATEGORY.PROMO`, `ctx.features`, `ctx.showVpnMessages`, `ctx.vpnEnabled`, `m.category`, `m.feature`, `m.id`, `state.messageLastShown`, `state.promoLastDay`, `state.recentId`

## selectPrivacyMessage()
- 位置: L641-753
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `buildPool()`, `countArgFor()`, `forcedResult()`, `normalizeState()`, `periodBounds()`, `rand()`, `toDecision()`, `utcDayKey()`
- 条件付き依存: `if (!ctx.trackersToday)` → `toDecision()`
- 条件付き依存: `if (!state.firstProtectionShown)` → `firstByCategory()`
- 条件付き依存: `if (!state.firstProtectionShown)` → `toDecision()`
- 条件付き依存: `if (!state.firstProtectionShown)` → `countArgFor()`
- 条件付き依存: `if (state.lastCelebrationDay !== today)` → `STREAK_DAYS.includes()`
- 条件付き依存: `if ( STREAK_DAYS.includes(ctx.streakDays) && ctx.streakDays > state.streakFiredAt )` → `firstByCategory()`
- 条件付き依存: `if ( STREAK_DAYS.includes(ctx.streakDays) && ctx.streakDays > state.streakFiredAt )` → `toDecision()`
- 条件付き依存: `if ( STREAK_DAYS.includes(ctx.streakDays) && ctx.streakDays > state.streakFiredAt )` → `countArgFor()`
- 条件付き依存: `if (state.lastCelebrationDay !== today)` → `detectMilestone()`
- 条件付き依存: `if (milestone)` → `firstByCategory()`
- 条件付き依存: `if (milestone)` → `toDecision()`
- 条件付き依存: `if (milestone)` → `countArgFor()`
- 条件付き依存: `if (ctx.trackersToday >= ctx.maxCount)` → `firstByCategory()`
- 条件付き依存: `if (ctx.trackersToday >= ctx.maxCount)` → `toDecision()`
- 条件付き依存: `if (ctx.trackersToday >= ctx.maxCount)` → `countArgFor()`
- 条件付き依存: `if ( state.shownToday >= cap.perDay || (state.lastShownMs && now - state.lastShownMs < cap.intervalMs) )` → `blankDecision()`
- 条件付き依存: `if (!pool.length)` → `blankDecision()`
- 条件付き依存: `if (pick.category === CATEGORY.INFO && rand() < ctx.blankChance)` → `blankDecision()`
- 参照: `CAPS.newProfile`, `CAPS.normal`, `CATEGORY.DAILY_CAP`, `CATEGORY.FIRST_PROTECTION`, `CATEGORY.INFO`, `CATEGORY.PROMO`, `CATEGORY.STREAK`, `cap.intervalMs`, `cap.perDay`, `ctx.blankChance`, `ctx.maxCount`, `ctx.profileCreatedMs`, `ctx.streakDays`, `ctx.trackersToday`, `pick.category`, `pick.id`, `pool.length`, `state.dayStamp`, `state.firstProtectionShown`, `state.lastCelebrationDay`, `state.lastShownMs`, `state.messageLastShown`, `state.promoLastDay`, `state.recentId`, `state.shownToday`, `state.streakFiredAt`
