# browser/modules/EveryWindow.sys.mjs

source: browser/modules/EveryWindow.sys.mjs
source-hash: 64e7cbaa31be611c2d2d8ffb40f77359dbb5156f
lines: 115

## <module>
- 役割: 既存および今後開く全ブラウザーウィンドウに init/uninit コールバックを登録・解除する EveryWindow を定義する。

## callForEveryWindow()
- 位置: L30-37
- 役割: navigator:browser の全ウィンドウを列挙し、各ウィンドウの delayedStartupPromise の解決後に callback を呼ぶ。
- 触るとき: 起動直後のウィンドウに処理を届けるタイミングを変えたい、または初期化前のウィンドウを扱う処理を追うときに見る。
- 呼び出し先: `Services.wm.getEnumerator()`, `callback()`, `win.delayedStartupPromise.then()`
- XPCOM: `Services.wm`

## readyWindows()
- 位置: L43-47
- 役割: delayedStartupFinished が真になったウィンドウだけを配列で返すゲッター。
- 触るとき: 起動完了済みのウィンドウだけを対象に処理したいときに見る。
- 呼び出し先: `Array.from()`, `Array.from(Services.wm.getEnumerator("navigator:browser")).filter()`, `Services.wm.getEnumerator()`
- 参照: `win.gBrowserInit?.delayedStartupFinished`
- XPCOM: `Services.wm`

## EW_registerCallback()
- 位置: L60-94
- 役割: id を登録し、初回だけ起動完了とウィンドウ終了の監視を張ってから、既存の全ウィンドウに init を呼ぶ。id が使用済みなら false を返す。
- 触るとき: 新しい機能を全ウィンドウに適用する登録を書くとき、または同じ id の二重登録で false になる理由を調べるときに見る。
- 呼び出し先: `callForEveryWindow()`, `callbacks.has()`, `callbacks.set()`
- 条件付き依存: `if (!initialized)` → `Services.obs.addObserver()`
- 条件付き依存: `if (!initialized)` → `callbacks.values()`
- 条件付き依存: `if (!initialized)` → `c.init()`
- 条件付き依存: `if (!initialized)` → `addUnloadListener()`
- 条件付き依存: `if (!initialized)` → `callForEveryWindow()`
- XPCOM: `Services.obs`

## addUnloadListener()
- 位置: L66-76
- 役割: 渡されたウィンドウの domwindowclosed を監視する observer を登録する。
- 触るとき: ウィンドウが閉じられたときに uninit が呼ばれない不具合を調べるときに見る。
- 呼び出し先: `Services.ww.registerNotification()`
- XPCOM: `Services.ww`

## observer()
- 位置: L67-74
- 役割: 対象ウィンドウの domwindowclosed を受けると監視を外し、登録済みの全コールバックの uninit(win, true) を呼ぶ。
- 触るとき: ウィンドウを閉じたときの後始末が実行されない、または二重に実行されるときに見る。
- 条件付き依存: `if (topic == "domwindowclosed" && subject === win)` → `Services.ww.unregisterNotification()`
- 条件付き依存: `if (topic == "domwindowclosed" && subject === win)` → `callbacks.values()`
- 条件付き依存: `if (topic == "domwindowclosed" && subject === win)` → `c.uninit()`
- XPCOM: `Services.ww`

## EW_unregisterCallback()
- 位置: L103-113
- 役割: 未登録の id は何もせず、登録済みなら callUninit が真のとき全ウィンドウに uninit を呼んでから登録を削除する。
- 触るとき: 機能を無効化して全ウィンドウから後始末させたいとき、または uninit を呼ばずに登録だけ外したいときに見る。
- 呼び出し先: `callbacks.delete()`, `callbacks.has()`
- 条件付き依存: `if (callUninit)` → `callForEveryWindow()`
- 条件付き依存: `if (callUninit)` → `callbacks.get()`
- 参照: `callbacks.get(id).uninit`
