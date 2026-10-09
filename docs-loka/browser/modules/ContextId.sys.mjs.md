# browser/modules/ContextId.sys.mjs

source: browser/modules/ContextId.sys.mjs
source-hash: 6165af7407f293b552e9ee680f0ccc36e438bdf6
lines: 264

## <module>
- 役割: Contextual Services 用のコンテキスト ID を保持し、Rust コンポーネント有効時はローテーションと MARS への削除要求を扱う ContextId を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## JsContextIdCallback.constructor()
- 位置: L55-58
- 役割: Rust コンポーネントからのコールバックを受けるため、イベント発火関数を保持する。
- 触るとき: Rust 側からの永続化・ローテーション通知が JS に届かないときに見る。
- 呼び出し先: `super()`
- 参照: `this.dispatchEvent`

## JsContextIdCallback.persist()
- 位置: L60-64
- 役割: 新しい ID と作成時刻を pref に保存し、ContextId:Persisted イベントを発火する。
- 触るとき: 生成された ID が再起動後に残らないとき、または保存先の pref を変えるときに見る。
- 呼び出し先: `Services.prefs.setCharPref()`, `Services.prefs.setIntPref()`, `this.dispatchEvent()`
- XPCOM: `Services.prefs`

## JsContextIdCallback.rotated()
- 位置: L66-72
- 役割: 古い ID を contextId の Glean 値に記録して deletion-request ping を送り、続けて MARS 削除要求を送る。
- 触るとき: ローテーション時に削除 ping や MARS への削除要求が出ないとき、その送信順を確かめたいときに見る。
- 呼び出し先: `ContextId.sendMARSDeletionRequest()`, `Glean.contextualServices.contextId.set()`, `GleanPings.contextIdDeletionRequest.setEnabled()`, `GleanPings.contextIdDeletionRequest.submit()`

## _ContextId.constructor()
- 位置: L85-121
- 役割: rust-component.enabled が真のときだけ、回転日数と作成時刻を読んで Rust コンポーネントを初期化し、shutdown 通知を監視する。偽なら何もしない。
- 触るとき: 回転設定の反映タイミング(起動時に一度だけ読む)を変えるとき、または Rust 経路が使われない理由を調べるときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`, `super()`
- 条件付き依存: `if (this.#rustComponentEnabled)` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (this.#rustComponentEnabled)` → `ContextIdComponent.init()`
- 条件付き依存: `if (this.#rustComponentEnabled)` → `this.dispatchEvent.bind()`
- 条件付き依存: `if (this.#rustComponentEnabled)` → `Services.obs.addObserver()`
- 参照: `lazy.CURRENT_CONTEXT_ID`, `this.#comp`, `this.#observer`, `this.#rotationDays`, `this.#rustComponentEnabled`
- XPCOM: `Services.obs` / `Services.prefs`

## this.#observer()
- 位置: L115-117
- 役割: shutdown 通知の observe 呼び出しを内部の observe に中継する関数。
- 触るとき: shutdown 時の解除処理が呼ばれているかを追うときに見る。
- 呼び出し先: `this.observe()`

## _ContextId.observe()
- 位置: L130-136
- 役割: profile-before-change を受けるとコールバックを解除し、自身の監視を外す。
- 触るとき: 終了時にリーク警告が出るとき、または終了処理の順序を変えるときに見る。
- 条件付き依存: `if (topic == SHUTDOWN_TOPIC)` → `this.#comp.unsetCallback()`
- 条件付き依存: `if (topic == SHUTDOWN_TOPIC)` → `Services.obs.removeObserver()`
- 参照: `this.#observer`
- XPCOM: `Services.obs`

## _ContextId.request()
- 位置: async L148-161
- 役割: Rust 有効時はコンポーネントから回転込みで ID を取得する。無効時は pref が空なら UUID を生成して保存し、pref の値を返す。
- 触るとき: ID を取得する経路を変えるとき、または回転を使わない場合の ID の生成と保存を調べるときに見る。
- 呼び出し先: `Promise.resolve()`
- 条件付き依存: `if (this.#rustComponentEnabled)` → `this.#comp.request()`
- 条件付き依存: `if (!lazy.CURRENT_CONTEXT_ID)` → `Services.uuid.generateUUID().toString()`
- 条件付き依存: `if (!lazy.CURRENT_CONTEXT_ID)` → `Services.uuid.generateUUID()`
- 条件付き依存: `if (!lazy.CURRENT_CONTEXT_ID)` → `Services.prefs.setStringPref()`
- 参照: `lazy.CURRENT_CONTEXT_ID`, `this.#rotationDays`, `this.#rustComponentEnabled`
- XPCOM: `Services.prefs` / `Services.uuid`

## _ContextId.forceRotation()
- 位置: async L170-175
- 役割: Rust 有効時のみコンポーネントの forceRotation を呼ぶ。無効時は何もしない。
- 触るとき: ある機能が無効化されたとき ID を回転させたい場面を実装するときに見る。
- 呼び出し先: `Promise.resolve()`
- 条件付き依存: `if (this.#rustComponentEnabled)` → `this.#comp.forceRotation()`
- 参照: `this.#rustComponentEnabled`

## _ContextId.rotationEnabled()
- 位置: L182-184
- 役割: Rust 有効かつ回転日数が 0 より大きいときに真を返す。
- 触るとき: 回転が有効かどうかで呼び出し側の分岐を決めるときに見る。
- 参照: `this.#rotationDays`, `this.#rustComponentEnabled`

## _ContextId.requestSynchronously()
- 位置: L192-200
- 役割: 回転が有効なら例外を投げ、無効なら保存済みの ID を同期的に返す互換用の関数。
- 触るとき: 同期取得を使う呼び出し元を非同期 request へ移すときや、回転有効時の例外を調べるときに見る。
- 参照: `lazy.CURRENT_CONTEXT_ID`, `this.rotationEnabled`

## _ContextId.sendMARSDeletionRequest()
- 位置: async L212-260
- 役割: UNIFIED_ADS_ENDPOINT と OHTTP の relay・config の URL がすべてあるときだけ、古い ID を付けて OHTTP 経由で delete_user に DELETE を送る。config が取れなくてもエラーを記録するだけで、そのまま送信を続ける。
- 触るとき: MARS への削除要求が届かないとき、または OHTTP の pref や送信先を変えるときに見る。
- 呼び出し先: `JSON.stringify()`, `headers.append()`, `lazy.ObliviousHTTP.getOHTTPConfig()`, `lazy.ObliviousHTTP.ohttpRequest()`
- 条件付き依存: `if (!config)` → `console.error()`
- 条件付き依存: `if (!response.ok)` → `console.error()`
- 参照: `lazy.OHTTP_CONFIG_URL`, `lazy.OHTTP_RELAY_URL`, `lazy.UNIFIED_ADS_ENDPOINT`, `response.ok`, `response.status`
