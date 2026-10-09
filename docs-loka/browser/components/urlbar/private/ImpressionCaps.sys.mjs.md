# browser/components/urlbar/private/ImpressionCaps.sys.mjs

source: browser/components/urlbar/private/ImpressionCaps.sys.mjs
source-hash: 9bddf7752e1e0299df61db0f83f442822e2c79d7
lines: 459

## <module>
- 役割: Quick Suggest 提案のインプレッション上限(caps)について、利用者ごとの表示回数を期間別に数えて pref に保存する機能を提供する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ImpressionCaps.constructor()
- 位置: L23-26
- 役割: 基底の SuggestFeature を初期化し、UrlbarPrefs の変更を監視するオブザーバーとして自身を登録する。
- 触るとき: 上限機能の設定読み込みや pref 変更への反応が始まるタイミングを調べるとき。
- 呼び出し先: `lazy.UrlbarPrefs.addObserver()`, `super()`

## ImpressionCaps.enablingPreferences()
- 位置: L28-33
- 役割: 上限機能を有効にするかを決める2つの pref 名(スポンサー用・非スポンサー用)を返す。
- 触るとき: スポンサー提案と非スポンサー提案で上限の有効・無効を別々に切り替える pref を追加・改名するとき。

## ImpressionCaps.enable()
- 位置: L35-41
- 役割: 有効なら #init() で統計の読み込みとタイマー登録を行い、無効なら #uninit() で後始末する。
- 触るとき: 機能の有効化・無効化の切り替え時に、タイマーや shutdown blocker が残らないか確認するとき。
- 条件付き依存: `if (enabled)` → `this.#init()`
- 条件付き依存: `if (!(enabled))` → `this.#uninit()`

## ImpressionCaps.updateStats()
- 位置: L51-104
- 役割: インプレッションを1件記録したとき、種別の全期間カウンターを1増やし、統計を JSON にして pref へ保存する。
- 触るとき: 提案が表示されたときに何を数えるかを変えるとき、または上限到達のログが出ない原因を追うとき。上限が無効な種別や統計がない種別では何もしない。
- 呼び出し先: `Date.now()`, `JSON.stringify()`, `lazy.UrlbarPrefs.get()`, `lazy.UrlbarPrefs.set()`, `this.logger.debug()`
- 条件付き依存: `if ( (isSponsored && !lazy.UrlbarPrefs.get("quickSuggestImpressionCapsSponsoredEnabled")) || (!isSponsored && !lazy.UrlbarPrefs.get("quickSuggestImpressionCapsNo...)` → `this.logger.debug()`
- 条件付き依存: `if (!stats)` → `this.logger.debug()`
- 条件付き依存: `if (stat.count == stat.maxCount)` → `this.logger.debug()`
- 参照: `lazy.QuickSuggest.config.impression_caps`, `stat.count`, `stat.impressionDateMs`, `stat.maxCount`, `this.#stats`, `this.#updatingStats`

## ImpressionCaps.getHitStats()
- 位置: L118-128
- 役割: まず期限切れカウンターをリセットし、maxCount 以上に達した統計の配列を返す。該当がなければ null を返す。
- 触るとき: 上限到達を理由に提案の表示を止める判定を、呼び出し元で使うときや見直すとき。
- 呼び出し先: `this.#resetElapsedCounters()`
- 条件付き依存: `if (stats)` → `stats.filter()`
- 参照: `hitStats.length`, `s.count`, `s.maxCount`, `this.#stats`

## ImpressionCaps.onPrefChanged()
- 位置: L136-147
- 役割: 統計 pref が外部で変わったとき、自分の更新中でなければ #loadStats() で読み直す。
- 触るとき: 別のタブや同期で統計 pref が書き換わったときに、メモリ上の値と食い違わないか確認するとき。
- 条件付き依存: `if (!this.#updatingStats)` → `this.logger.debug()`
- 条件付き依存: `if (!this.#updatingStats)` → `this.#loadStats()`
- 参照: `this.#updatingStats`

## ImpressionCaps.#init()
- 位置: L149-167
- 役割: 統計を読み込み、リセット用の定期タイマーを作り、プロファイル終了時にリセット記録を行う shutdown blocker を登録する。
- 触るとき: 機能を有効化したときの初期化の順序や内容を変えるとき。
- 呼び出し先: `lazy.AsyncShutdown.profileChangeTeardown.addBlocker()`, `this.#loadStats()`, `this.#setCountersResetInterval()`
- 参照: `this._onConfigSet`, `this._shutdownBlocker`

## this._onConfigSet()
- 位置: L153-153
- 役割: config-set イベントで統計を検証する関数を保持する。現状は emitter への登録がコメントアウトされていて呼ばれない。
- 触るとき: impression caps を再び有効にし、設定変更時の再検証をつなぎ直すとき。
- 呼び出し先: `this.#validateStats()`

## this._shutdownBlocker()
- 位置: L162-162
- 役割: プロファイル終了時に #resetElapsedCounters() を呼び、経過したカウンターのリセットを記録する blocker。
- 触るとき: 終了時にリセットの記録が漏れる、または終了処理が遅れる問題を調べるとき。
- 呼び出し先: `this.#resetElapsedCounters()`

## ImpressionCaps.#uninit()
- 位置: L169-182
- 役割: 定期タイマーを止め、shutdown blocker を外す。config-set の購読解除は TODO でコメントアウトされている。
- 触るとき: 機能を無効にした後もタイマーや blocker が残っていないか確認するとき。
- 呼び出し先: `lazy.AsyncShutdown.profileChangeTeardown.removeBlocker()`, `lazy.clearInterval()`
- 参照: `this._impressionCountersResetInterval`, `this._onConfigSet`, `this._shutdownBlocker`

## ImpressionCaps.#loadStats()
- 位置: L187-203
- 役割: pref の JSON を読んで統計にする。Infinity の intervalSeconds を null から復元し、解析に失敗した場合は無視して、その後 #validateStats() を呼ぶ。
- 触るとき: 保存済みの統計を起動時にどう読み込むかを変えるとき、または壊れた JSON の扱いを見直すとき。
- 呼び出し先: `lazy.UrlbarPrefs.get()`, `this.#validateStats()`
- 条件付き依存: `if (!(!json))` → `JSON.parse()`
- 参照: `this.#stats`

## ImpressionCaps.#validateStats()
- 位置: L213-324
- 役割: 統計を caps と1対1に揃える。不正な統計を捨て、caps にない間隔の統計は間隔が等しいか長い統計へ統合し、足りない統計を作り、lifetime の count を最大値に合わせ、間隔順に並べる。
- 触るとき: caps の設定が変わったときや pref が手で書き換えられたときに、統計がどう整合されるかを調べるとき。
- 呼び出し先: `(cap.custom || []).reduce()`, `Array.isArray()`, `Object.entries()`, `map.set()`, `maxCapCounts.entries()`, `stats.find()`, `stats.some()`, `stats.sort()`, `this.logger.debug()`
- 条件付き依存: `if (typeof cap.lifetime == "number")` → `maxCapCounts.set()`
- 条件付き依存: `if ( typeof stat.intervalSeconds != "number" || typeof stat.startDateMs != "number" || typeof stat.count != "number" || typeof stat.maxCount != "number" || typeo...)` → `stats.splice()`
- 条件付き依存: `if (!( typeof stat.intervalSeconds != "number" || typeof stat.startDateMs != "number" || typeof stat.count != "number" || typeof stat.maxCount != "number" || typeo...))` → `Math.max()`
- 条件付き依存: `if (!( typeof stat.intervalSeconds != "number" || typeof stat.startDateMs != "number" || typeof stat.count != "number" || typeof stat.maxCount != "number" || typeo...))` → `maxCapCounts.get()`
- 条件付き依存: `if (maxCount === undefined)` → `stats.splice()`
- 条件付き依存: `if (maxCount === undefined)` → `orphanStats.push()`
- 条件付き依存: `if (!stats.some(s => s.intervalSeconds == intervalSeconds))` → `stats.push()`
- 条件付き依存: `if (!stats.some(s => s.intervalSeconds == intervalSeconds))` → `Date.now()`
- 条件付き依存: `if (orphan.intervalSeconds <= stat.intervalSeconds)` → `Math.max()`
- 条件付き依存: `if (orphan.intervalSeconds <= stat.intervalSeconds)` → `Math.min()`
- 参照: `a.intervalSeconds`, `b.intervalSeconds`, `cap.custom`, `cap.lifetime`, `lazy.QuickSuggest.config`, `lifetimeStat.count`, `orphan.count`, `orphan.impressionDateMs`, `orphan.intervalSeconds`, `orphan.startDateMs`, `s.intervalSeconds`, `stat.count`, `stat.impressionDateMs`, `stat.intervalSeconds`, `stat.maxCount`, `stat.startDateMs`, `stats.length`, `this.#stats`

## ImpressionCaps.#resetElapsedCounters()
- 位置: L329-364
- 役割: 各統計について開始時刻からの経過を間隔で割り、1回以上経過していれば開始時刻を進めて count を 0 に戻す。
- 触るとき: カウンターが期待どおりに 0 に戻らない、または戻るタイミングがずれるときに確認するとき。
- 呼び出し先: `Date.now()`, `Math.floor()`, `Object.entries()`, `this.logger.debug()`
- 条件付き依存: `if (elapsedIntervalCount)` → `this.logger.debug()`
- 参照: `lazy.QuickSuggest.config.impression_caps`, `stat.count`, `stat.intervalSeconds`, `stat.startDateMs`, `this.#stats`

## ImpressionCaps.#setCountersResetInterval()
- 位置: L375-383
- 役割: 既存のタイマーを止めてから、指定ms(既定は1時間)ごとに #resetElapsedCounters() を呼ぶタイマーを作り直す。
- 触るとき: リセットの周期を変えるとき、またはテストで短い周期を与えるとき。
- 呼び出し先: `lazy.setInterval()`, `this.#resetElapsedCounters()`
- 条件付き依存: `if (this._impressionCountersResetInterval)` → `lazy.clearInterval()`
- 参照: `this._impressionCountersResetInterval`

## ImpressionCaps._getStartupDateMs()
- 位置: L393-395
- 役割: Services.startup からプロセス開始時刻をミリ秒で返す。テストで起動時刻を差し替えられるよう独立したメソッドになっている。
- 触るとき: 起動時刻を基準にする処理をテストで模擬するとき。
- 呼び出し先: `Services.startup.getStartupInfo()`, `Services.startup.getStartupInfo().process.getTime()`
- XPCOM: `Services.startup`

## ImpressionCaps._test_stats()
- 位置: L397-399
- 役割: テスト用に内部の統計オブジェクトを返す getter。
- 触るとき: テストで統計の中身を直接検証するとき。
- 参照: `this.#stats`

## ImpressionCaps._test_reloadStats()
- 位置: L401-404
- 役割: 統計を null にしてから pref を読み直す、テスト用の関数。
- 触るとき: テストで pref を書き換えた後の読み込み結果を確かめるとき。
- 呼び出し先: `this.#loadStats()`
- 参照: `this.#stats`

## ImpressionCaps._test_resetElapsedCounters()
- 位置: L406-408
- 役割: 経過カウンターのリセットを外部から直接実行するテスト用関数。
- 触るとき: 時刻を進めたときのリセット動作をテストするとき。
- 呼び出し先: `this.#resetElapsedCounters()`

## ImpressionCaps._test_setCountersResetInterval()
- 位置: L410-412
- 役割: リセット周期を指定してタイマーを作り直す、テスト用の関数。
- 触るとき: 短い周期でリセットを発火させるテストを書くとき。
- 呼び出し先: `this.#setCountersResetInterval()`
