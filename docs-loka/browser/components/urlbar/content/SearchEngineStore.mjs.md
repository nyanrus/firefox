# browser/components/urlbar/content/SearchEngineStore.mjs

source: browser/components/urlbar/content/SearchEngineStore.mjs
source-hash: 6d9c262c83945b27d7c2e44ff8f5d26ab960a4ed
lines: 346

## <module>
- 役割: 検索エンジン一覧を検索サービスの通知で更新し続けるメモリ上のキャッシュ(SearchEngineStore)と、その各エンジンの軽量な代理オブジェクトを定義する。親プロセス外で検索サービスの代わりに使う。
- 呼び出し先: `Promise.withResolvers()`, `UrlbarShared.getLogger()`

## PartialSearchEngine.constructor()
- 位置: L43-53
- 役割: エンジン情報をコピーし、親のコントローラーを保持する。アイコンは未取得の状態にする。
- 触るとき: エンジンの表示に使う項目を増やす、または情報の受け渡し形式を変えるときに見る。
- 参照: `engineInfo.aliases`, `engineInfo.hideOneOffButton`, `engineInfo.id`, `engineInfo.isAppProvided`, `engineInfo.isConfigEngine`, `engineInfo.isGeneralPurposeEngine`, `engineInfo.isNewUntil`, `engineInfo.name`, `this.#controller`, `this.aliases`, `this.hideOneOffButton`, `this.id`, `this.isAppProvided`, `this.isConfigEngine`, `this.isGeneralPurposeEngine`, `this.isNewUntil`, `this.name`

## PartialSearchEngine.getIconURL()
- 位置: async L69-76
- 役割: 初回のみ親に getEngineIconURL を問い合わせ、結果(無ければ null)を保持して返す。
- 触るとき: エンジンアイコンが出ない、または何度も親へ問い合わせてしまうときに見る。
- 条件付き依存: `if (this.#icon === undefined)` → `this.#controller.parentController.getEngineIconURL()`
- 参照: `this.#icon`, `this.id`

## PartialSearchEngine.isNew()
- 位置: L83-89
- 役割: isNewUntil の日付(YYYY-MM-DD)が今日以降なら true を返す。
- 触るとき: 新規エンジンの印を出す期間の判定を変えるときに見る。
- 呼び出し先: `new Date().toISOString()`, `new Date().toISOString().slice()`
- 参照: `this.isNewUntil`

## PartialSearchEngine.invalidateIcon()
- 位置: L94-96
- 役割: キャッシュしたアイコン URL を捨て、次回の getIconURL で取り直させる。
- 触るとき: エンジンのアイコンを変更後に古い画像が残る問題を調べるときに見る。
- 参照: `this.#icon`

## PartialSearchEngine.markAsUsed()
- 位置: L101-103
- 役割: 親に markEngineAsUsed を送り、このエンジンを使用済みとして記録させる。
- 触るとき: 使用済みの記録が付かないエンジンを調べるときに見る。
- 呼び出し先: `this.#controller.parentController.markEngineAsUsed()`
- 参照: `this.id`

## SearchEngineStore.constructor()
- 位置: L129-132
- 役割: コントローラーを保持し、入力欄の isPrivate を読んで保存する。
- 触るとき: プライベートウィンドウでエンジン一覧の扱いがずれるときに見る。
- 参照: `controller.input.isPrivate`, `this.#controller`, `this.isPrivate`

## SearchEngineStore.init()
- 位置: L141-147
- 役割: 未初期化かつ未失敗なら親に initEngineStore を送り、初期化完了を待つ Promise を返す。
- 触るとき: エンジン一覧が空のまま使われる、または初期化待ちで止まる問題を調べるときに見る。
- 条件付き依存: `if (!this.initialized && !this.failed)` → `this.#controller.parentController.initEngineStore()`
- 参照: `this.#initPromiseWithResolvers.promise`, `this.failed`, `this.initialized`

## SearchEngineStore.default()
- 位置: L155-157
- 役割: 既定エンジンを返す。初期化前や失敗時は null。
- 触るとき: 既定エンジンを前提にした表示や検索の挙動を確かめるときに見る。
- 参照: `this.#defaultEngine`

## SearchEngineStore.getEngine()
- 位置: L163-165
- 役割: ID が一致するエンジンを一覧から探して返す。無ければ undefined。
- 触るとき: ID で指定されたエンジンを引く箇所の挙動を追うときに見る。
- 呼び出し先: `this.#store.find()`
- 参照: `e.id`

## SearchEngineStore.getEngines()
- 位置: L172-178
- 役割: 表示順のエンジン一覧を返す。初期化前に呼ぶと例外を投げる。
- 触るとき: エンジン一覧を画面に出す前の初期化待ちの扱いを変えるときに見る。
- 参照: `this.#store`, `this.initialized`

## SearchEngineStore.getEngineByName()
- 位置: L184-186
- 役割: 名前が一致するエンジンを一覧から探して返す。
- 触るとき: 名前で検索エンジンを指定する経路を追うときに見る。
- 呼び出し先: `this.#store.find()`
- 参照: `e.name`

## SearchEngineStore.addObserver()
- 位置: L191-195
- 役割: 重複しないように変更通知のリスナーを登録する。
- 触るとき: エンジン変更の通知を受け取る側を追加するときに見る。
- 呼び出し先: `this.#observers.includes()`
- 条件付き依存: `if (!this.#observers.includes(observer))` → `this.#observers.push()`

## SearchEngineStore.removeObserver()
- 位置: L200-205
- 役割: 登録済みのリスナーを外す。無ければ何もしない。
- 触るとき: リスナーを外し忘れて通知が残る問題を調べるときに見る。
- 呼び出し先: `this.#observers.findIndex()`
- 条件付き依存: `if (index != -1)` → `this.#observers.splice()`

## SearchEngineStore.receive()
- 位置: L213-229
- 役割: 親からの通知の種類(init、error、removed、changed、default)を、対応する内部処理へ振り分ける。
- 触るとき: 親から届く通知の種類を増やす、または通知が無視される問題を調べるときに見る。
- 呼び出し先: `this.#handleError()`, `this.#handleInit()`, `this.#handleUpdate()`

## SearchEngineStore.#handleInit()
- 位置: L239-251
- 役割: エンジン情報の一覧から PartialSearchEngine を作って格納し、defaultIndex の engine を既定にして初期化済みとする。二重初期化は例外。
- 触るとき: 起動時の一覧の構築や既定エンジンの決まり方を変えるときに見る。
- 呼び出し先: `this.#initPromiseWithResolvers.resolve()`, `this.#store.push()`
- 参照: `this.#controller`, `this.#defaultEngine`, `this.#store`, `this.initialized`

## SearchEngineStore.#handleError()
- 位置: L257-265
- 役割: 検索サービスが失敗したことを記録し、初期化 Promise を拒否する。
- 触るとき: 検索サービスの失敗時に urlbar がどう振る舞うかを追うときに見る。
- 呼び出し先: `this.#initPromiseWithResolvers.reject()`
- 参照: `this.failed`, `this.initialized`

## SearchEngineStore.#handleUpdate()
- 位置: L279-332
- 役割: removed は一覧から外して通知、changed は無ければ追加、あれば情報と並び順を更新してアイコンを無効化し通知、default は既定エンジンを差し替えて通知する。一覧にない既定エンジンは警告を出して無視する。
- 触るとき: エンジンの追加、削除、並び替え、既定変更が画面に反映されない問題を調べるときに見る。
- 呼び出し先: `Object.keys()`, `engine.invalidateIcon()`, `this.#notifyObservers()`, `this.#store.findIndex()`
- 条件付き依存: `if (currentIndex != -1)` → `this.#store.splice()`
- 条件付き依存: `if (currentIndex != -1)` → `this.#notifyObservers()`
- 条件付き依存: `if (newIndex == -1)` → `this.#store.push()`
- 条件付き依存: `if (!(newIndex == -1))` → `this.#store.splice()`
- 条件付き依存: `if (currentIndex == -1)` → `this.#notifyObservers()`
- 条件付き依存: `if (newIndex != currentIndex)` → `this.#store.splice()`
- 条件付き依存: `if (currentIndex == -1)` → `logger.warn()`
- 参照: `e.id`, `engineInfo.id`, `this.#controller`, `this.#defaultEngine`, `this.#store`, `this.initialized`

## SearchEngineStore.#notifyObservers()
- 位置: L340-344
- 役割: 登録された全リスナーに変更の種類とエンジンを渡して呼ぶ。
- 触るとき: 変更通知の内容や呼び出し順を変えるときに見る。
- 呼び出し先: `observer()`
- 参照: `this.#observers`
