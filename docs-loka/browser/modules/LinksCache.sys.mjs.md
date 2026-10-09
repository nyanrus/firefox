# browser/modules/LinksCache.sys.mjs

source: browser/modules/LinksCache.sys.mjs
source-hash: b6ab328b930857b24ffc5a1cff7e6f91c9bab2bf
lines: 134

## <module>
- 役割: リンク一覧の取得結果を一定時間キャッシュし、古いリンクの状態を引き継ぐ。

## LinksCache.constructor()
- 位置: L28-45
- 役割: リンク取得元のオブジェクトとプロパティ、引き継ぐ項目、再取得条件を保持する。
- 触るとき: キャッシュに引き継ぐプロパティを追加するとき、または再取得の条件を差し替えるとき。__sharedCache は常に引き継ぐ。
- 呼び出し先: `this.clear()`
- 参照: `this.linkGetter`, `this.migrateProperties`, `this.shouldRefresh`

## this.linkGetter()
- 位置: L37-40
- 役割: 取得元がメソッドならそれを呼び、配列ならそのまま返す。
- 触るとき: リンクの取得元にメソッドと配列の両方を使う理由を確かめるとき。
- 呼び出し先: `ret.call()`

## LinksCache.clear()
- 位置: L50-54
- 役割: キャッシュを空にして、次の要求で必ず更新されるようにする。
- 触るとき: キャッシュを捨てる処理の影響を確かめるとき。
- 呼び出し先: `Promise.resolve()`, `this.expire()`
- 参照: `this.cache`, `this.lastOptions`

## LinksCache.expire()
- 位置: L59-61
- 役割: 最終更新時刻を消して、次の要求で再取得させる。
- 触るとき: 特定の操作の後に一覧を強制的に更新させたいとき。
- 参照: `this.lastUpdate`

## LinksCache.request()
- 位置: async L69-132
- 役割: 期限切れか再取得条件を満たすときだけ取得し直し、古いリンクの値を url 一致で移して返す。
- 触るとき: リンク一覧の更新タイミング、または更新後に値が消える・残る報告を調べるとき。期限は 4.5 分。返すのは各リンクの浅いコピー。
- 呼び出し先: `(await this.cache).map()`, `Date.now()`, `Object.assign()`, `this.shouldRefresh()`
- 条件付き依存: `if (oldLink)` → `toMigrate.set()`
- 条件付き依存: `if ( this.lastUpdate === undefined || now > this.lastUpdate + EXPIRATION_TIME || // Allow custom rules around refreshing based on options this.shouldRefresh(this...)` → `resolve()`
- 条件付き依存: `if ( this.lastUpdate === undefined || now > this.lastUpdate + EXPIRATION_TIME || // Allow custom rules around refreshing based on options this.shouldRefresh(this...)` → `(await this.linkGetter(options)).map()`
- 条件付き依存: `if ( this.lastUpdate === undefined || now > this.lastUpdate + EXPIRATION_TIME || // Allow custom rules around refreshing based on options this.shouldRefresh(this...)` → `this.linkGetter()`
- 条件付き依存: `if ( this.lastUpdate === undefined || now > this.lastUpdate + EXPIRATION_TIME || // Allow custom rules around refreshing based on options this.shouldRefresh(this...)` → `Object.assign()`
- 条件付き依存: `if ( this.lastUpdate === undefined || now > this.lastUpdate + EXPIRATION_TIME || // Allow custom rules around refreshing based on options this.shouldRefresh(this...)` → `toMigrate.get()`
- 条件付き依存: `if ( this.lastUpdate === undefined || now > this.lastUpdate + EXPIRATION_TIME || // Allow custom rules around refreshing based on options this.shouldRefresh(this...)` → `reject()`
- 参照: `newLink.__sharedCache`, `newLink.__sharedCache.updateLink`, `newLink.url`, `oldLink.url`, `this.cache`, `this.lastOptions`, `this.lastUpdate`, `this.migrateProperties`

## newLink.__sharedCache.updateLink()
- 位置: L117-119
- 役割: キャッシュ側のリンクに値を設定する補助関数。
- 触るとき: 表示側から取得済みリンクの値を書き換えて次回に残したいとき。
