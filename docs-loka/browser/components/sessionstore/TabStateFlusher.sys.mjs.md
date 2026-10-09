# browser/components/sessionstore/TabStateFlusher.sys.mjs

source: browser/components/sessionstore/TabStateFlusher.sys.mjs
source-hash: fcffc6be2656ba185bbf5e6f8a6ea184957375ce
lines: 144

## <module>
- 役割: コンテンツプロセスが送る遅延したタブ状態を、要求に応じて即座に親プロセスへ反映させる非同期フラッシュの仕組み。
- 呼び出し先: `Object.freeze()`

## flush()
- 位置: L19-21
- 役割: TabStateFlusherInternal.flush を呼ぶ公開の単一タブ用フラッシュ口。
- 触るとき: タブの最新状態が必要な処理が待ち合わせる先を追うとき。
- 呼び出し先: `TabStateFlusherInternal.flush()`

## flushWindow()
- 位置: L27-29
- 役割: TabStateFlusherInternal.flushWindow を呼ぶ公開のウィンドウ単位フラッシュ口。
- 触るとき: ウィンドウ単位の保存前フラッシュの範囲を変えるとき。
- 呼び出し先: `TabStateFlusherInternal.flushWindow()`

## resolveAll()
- 位置: L45-47
- 役割: TabStateFlusherInternal.resolveAll を呼ぶ公開の全解決口。
- 触るとき: コンテンツプロセスのクラッシュや最終更新時の後始末を調べるとき。
- 呼び出し先: `TabStateFlusherInternal.resolveAll()`

## initEntry()
- 位置: L57-66
- 役割: ブラウザごとの要求エントリに cancel 用の Promise を作り、解決後は同じエントリを初期化し直す。
- 触るとき: フラッシュ要求のキャンセルが次の要求に残る問題を調べるとき。
- 呼び出し先: `TabStateFlusherInternal.initEntry()`, `new Promise(resolve => { entry.cancel = resolve; }).then()`
- 参照: `entry.cancel`, `entry.cancelPromise`

## flush()
- 位置: L73-97
- 役割: フレームローダーにフラッシュを要求し、その完了か要求の取り消しのどちらか早い方で解決する Promise を返す。
- 触るとき: フラッシュの待ち時間や、応答が来ない場合の挙動を変えるとき。
- 呼び出し先: `Promise.race()`, `Promise.resolve()`, `this._requests.get()`
- 条件付き依存: `if (browser && browser.frameLoader)` → `browser.frameLoader.requestTabStateFlush()`
- 条件付き依存: `if (!request)` → `this.initEntry()`
- 条件付き依存: `if (!request)` → `this._requests.set()`
- 参照: `browser.frameLoader`, `browser.permanentKey`, `request.cancelPromise`

## flushWindow()
- 位置: L103-111
- 役割: ウィンドウ内で linkedPanel を持つ（遅延読み込みでない）全ブラウザについて flush し、すべて終わるまで待つ。
- 触るとき: ウィンドウ単位の待ち合わせに含めるブラウザの条件を変えるとき。
- 呼び出し先: `Promise.all()`, `window.gBrowser.getTabForBrowser()`
- 条件付き依存: `if (window.gBrowser.getTabForBrowser(browser).linkedPanel)` → `promises.push()`
- 条件付き依存: `if (window.gBrowser.getTabForBrowser(browser).linkedPanel)` → `this.flush()`
- 参照: `window.gBrowser.browsers`, `window.gBrowser.getTabForBrowser(browser).linkedPanel`

## resolveAll()
- 位置: L127-142
- 役割: ブラウザの保留中の要求をすべて cancel で解決し、失敗なら Console にエラーを出す。
- 触るとき: フラッシュ失敗時のエラー表示や解決の仕方を変えるとき。
- 呼び出し先: `cancel()`, `this._requests.get()`, `this._requests.has()`
- 条件付き依存: `if (!success)` → `console.error()`
- 参照: `browser.permanentKey`
