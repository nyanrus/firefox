# browser/components/extensions/parent/ext-tabGroups.js

source: browser/components/extensions/parent/ext-tabGroups.js
source-hash: b901973f1fec795ba3056d0a0c78625188928e10
lines: 301

## <module>
- 役割: tabGroups WebExtension API の実装。タブグループの取得、検索、移動、更新と、4 種類のイベント通知を提供する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## spellColour()
- 位置: L12-12
- 役割: 拡張 API の色名 grey を内部の gray に変換する。
- 触るとき: タブグループの色を拡張から設定・検索したときに色が合わないとき。

## validateTabIndexForMove()
- 位置: L21-45
- 役割: グループを指定位置へ動かせるか検証し、ピン留めタブの途中やほかのグループの途中なら例外を投げる。
- 触るとき: tabGroups.move が『途中に入れない』エラーを出す条件を変えるとき、または移動先インデックスのずれを調べるとき。同じウィンドウ内で後ろへ動かす場合はグループのタブ数を足して補正する。
- 呼び出し先: `Math.min()`, `window.gBrowser.tabs.at()`
- 参照: `group.documentGlobal`, `group.tabs`, `group_tabs.length`, `group_tabs[0].index`, `nextTab.group`, `nextTab?.group`, `nextTab?.pinned`, `prevTab.group`, `window.gBrowser.tabs.length`

## queryGroups()
- 位置: L48-67
- 役割: アクセス可能なウィンドウのタブグループを、collapsed、color、title、windowId で絞り込む。
- 触るとき: tabGroups.query の結果が期待より少ない、または多いとき。title は MatchGlob で照合する。
- 呼び出し先: `glob.matches()`, `spellColour()`, `this.extension.canAccessWindow()`, `windowTracker .browserWindows()`, `windowTracker .browserWindows() .filter()`, `windowTracker.getWindow()`
- 参照: `group.collapsed`, `group.color`, `group.name`, `win.gBrowser.tabGroups`

## get()
- 位置: L69-80
- 役割: 拡張用 ID から内部のタブグループ ID を引き、一致するグループを返す。無ければ例外を投げる。
- 触るとき: 拡張が渡した groupId で『No group with id』が出るときに見る。
- 呼び出し先: `getInternalTabGroupIdForExtTabGroupId()`, `this.queryGroups()`
- 参照: `group.id`

## convert()
- 位置: L82-91
- 役割: 内部のタブグループを拡張用の形式 (collapsed、color、id、title、windowId) に変換する。
- 触るとき: 拡張に返すタブグループの項目を増やすとき、または色や ID の表示がおかしいとき。color の gray は grey に戻す。
- 呼び出し先: `getExtTabGroupIdForInternalTabGroupId()`, `windowTracker.getId()`
- 参照: `group.collapsed`, `group.color`, `group.documentGlobal`, `group.id`, `group.name`

## onCreated()
- 位置: L94-116
- 役割: TabGroupCreate を監視し、他ウィンドウから移動してきたグループ (adopting) 以外を onCreated として通知する。
- 触るとき: onCreated が発火しない、または移動による作成まで拾ってしまうときに見る。
- 呼び出し先: `windowTracker.addListener()`

## onCreate()
- 位置: L95-106
- 役割: adopting でなく、アクセス権のあるウィンドウのグループ作成を fire.async で通知する。
- 触るとき: 作成通知の条件を変えるとき。
- 呼び出し先: `fire.async()`, `this.convert()`, `this.extension.canAccessWindow()`
- 参照: `event.detail.adopting`, `event.originalTarget`, `event.originalTarget.documentGlobal`

## unregister()
- 位置: L109-111
- 役割: onCreated の TabGroupCreate リスナーを外す。
- 触るとき: 拡張の無効化後も作成通知が届くときに解除を確認する。
- 呼び出し先: `windowTracker.removeListener()`

## convert()
- 位置: L112-114
- 役割: 永続イベントの再接続時に onCreated の fire を差し替える。
- 触るとき: 再起動後に onCreated が古い fire へ送られるときに見る。

## onMoved()
- 位置: L117-149
- 役割: TabGroupMoved を監視し、別ウィンドウから移動してきた TabGroupCreate も移動として通知する。
- 触るとき: onMoved の対象を広げる、または移動イベントが二重に出るときに見る。
- 呼び出し先: `windowTracker.addListener()`

## onMove()
- 位置: L118-125
- 役割: TabGroupMoved のうち、アクセス権のあるウィンドウのものを fire.async で通知する。
- 触るとき: 移動通知が届かないときや、アクセス権の判定を変えるとき。
- 呼び出し先: `fire.async()`, `this.convert()`, `this.extension.canAccessWindow()`
- 参照: `event.originalTarget`, `event.originalTarget.documentGlobal`

## onCreate()
- 位置: L126-137
- 役割: adopting のグループ作成 (別ウィンドウからの移動) のみを移動として通知する。
- 触るとき: 別ウィンドウから移動されたグループが onMoved に出ないときに見る。
- 呼び出し先: `fire.async()`, `this.convert()`, `this.extension.canAccessWindow()`
- 参照: `event.detail.adopting`, `event.originalTarget`, `event.originalTarget.documentGlobal`

## unregister()
- 位置: L141-144
- 役割: onMoved の TabGroupMoved と TabGroupCreate のリスナーを外す。
- 触るとき: 無効化後も移動通知が届くときに解除を確認する。
- 呼び出し先: `windowTracker.removeListener()`

## convert()
- 位置: L145-147
- 役割: 永続イベントの再接続時に onMoved の fire を差し替える。
- 触るとき: 再起動後に onMoved が古い fire へ送られるときに見る。

## onRemoved()
- 位置: L150-184
- 役割: TabGroupRemoved と domwindowclosed を監視し、削除と、ウィンドウを閉じる際の各グループの削除を通知する。
- 触るとき: 削除通知が二重に出る、またはウィンドウ終了時の通知が欠けるときに見る。
- 呼び出し先: `windowTracker.addListener()`

## onRemove()
- 位置: L151-164
- 役割: adopting でない (別ウィンドウへ移動した場合を除く) グループ削除を、isWindowClosing を false にして通知する。
- 触るとき: グループを閉じたときの通知内容や、移動による削除を除外する条件を確認するとき。
- 呼び出し先: `fire.async()`, `this.convert()`, `this.extension.canAccessWindow()`
- 参照: `event.detail.adopting`, `event.originalTarget`, `event.originalTarget.documentGlobal`

## onClosed()
- 位置: L165-172
- 役割: ウィンドウを閉じるとき、そのウィンドウの各グループを isWindowClosing を true にして通知する。
- 触るとき: ウィンドウ終了時に削除通知が出ない、または対象外のウィンドウが含まれるときに見る。
- 呼び出し先: `fire.async()`, `this.convert()`, `this.extension.canAccessWindow()`
- 参照: `window.gBrowser.tabGroups`

## unregister()
- 位置: L176-179
- 役割: onRemoved の TabGroupRemoved と domwindowclosed のリスナーを外す。
- 触るとき: 無効化後も削除通知が届くときに解除を確認する。
- 呼び出し先: `windowTracker.removeListener()`

## convert()
- 位置: L180-182
- 役割: 永続イベントの再接続時に onRemoved の fire を差し替える。
- 触るとき: 再起動後に onRemoved が古い fire へ送られるときに見る。

## onUpdated()
- 位置: L185-207
- 役割: TabGroupCollapse、TabGroupExpand、TabGroupUpdate を監視し、グループの変化を通知する。
- 触るとき: 折りたたみや名前変更の通知が出ないときに見る。
- 呼び出し先: `windowTracker.addListener()`

## onUpdate()
- 位置: L186-193
- 役割: アクセス権のあるウィンドウのグループ変化を fire.async で通知する。
- 触るとき: 更新通知の対象ウィンドウの判定を変えるとき。
- 呼び出し先: `fire.async()`, `this.convert()`, `this.extension.canAccessWindow()`
- 参照: `event.originalTarget`, `event.originalTarget.documentGlobal`

## unregister()
- 位置: L198-202
- 役割: onUpdated の三つの更新リスナーを外す。
- 触るとき: 無効化後も更新通知が届くときに解除を確認する。
- 呼び出し先: `windowTracker.removeListener()`

## convert()
- 位置: L203-205
- 役割: 永続イベントの再接続時に onUpdated の fire を差し替える。
- 触るとき: 再起動後に onUpdated が古い fire へ送られるときに見る。

## getAPI()
- 位置: L210-299
- 役割: tabGroups の get、move、query、update と四つのイベントを組み立てて返す。
- 触るとき: 拡張から見える tabGroups API を増減するとき。
- 呼び出し先: `new EventManager({ context, module: "tabGroups", event: "onCreated", extensionApi: this, }).api()`, `new EventManager({ context, module: "tabGroups", event: "onMoved", extensionApi: this, }).api()`, `new EventManager({ context, module: "tabGroups", event: "onRemoved", extensionApi: this, }).api()`, `new EventManager({ context, module: "tabGroups", event: "onUpdated", extensionApi: this, }).api()`
- 参照: `this.extension`

## get()
- 位置: L214-216
- 役割: groupId に対応するグループを拡張用の形式にして返す。
- 触るとき: tabGroups.get の戻り値を確認するとき。
- 呼び出し先: `this.convert()`, `this.get()`

## move()
- 位置: L218-248
- 役割: グループを指定ウィンドウ・位置へ移動する。別ウィンドウなら adoptTabGroup、同じなら moveTabTo を使う。
- 触るとき: タブグループの移動で private と通常の混在エラーが出る、または移動先が normal 以外のウィンドウだと弾かれるときに見る。index が -1 なら末尾へ動かす。
- 呼び出し先: `Math.min()`, `this.convert()`, `this.get()`, `validateTabIndexForMove()`
- 条件付き依存: `if (windowId != null)` → `windowTracker.getWindow()`
- 条件付き依存: `if (windowId != null)` → `PrivateBrowsingUtils.isWindowPrivate()`
- 条件付き依存: `if (windowId != null)` → `windowManager.getWrapper()`
- 条件付き依存: `if (win !== group.documentGlobal)` → `win.gBrowser.adoptTabGroup()`
- 条件付き依存: `if (!(win !== group.documentGlobal))` → `win.gBrowser.moveTabTo()`
- 参照: `group.documentGlobal`, `win.gBrowser.tabs.length`, `windowManager.getWrapper(win).type`

## query()
- 位置: L250-254
- 役割: queryGroups の結果を拡張用の形式に変換した配列を返す。
- 触るとき: tabGroups.query の結果の並びや項目を確認するとき。
- 呼び出し先: `Array.from()`, `this.convert()`, `this.queryGroups()`

## update()
- 位置: L256-268
- 役割: グループの collapsed、color (grey を変換して設定)、title を更新し、変換後の値を返す。
- 触るとき: tabGroups.update で値が反映されない、または色の綴りがずれるときに見る。
- 呼び出し先: `this.convert()`, `this.get()`
- 条件付き依存: `if (color != null)` → `spellColour()`
- 参照: `group.collapsed`, `group.color`, `group.name`
