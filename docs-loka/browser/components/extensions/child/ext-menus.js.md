# browser/components/extensions/child/ext-menus.js

source: browser/components/extensions/child/ext-menus.js
source-hash: a3b6539b079d7b3b0f407f46638eaffa746b0922
lines: 306

## <module>
- 役割: 拡張の子側で menus と contextMenus の API を提供し、作成・更新と onclick の管理を親側の menusInternal へ橋渡しするファイル。

## ContextMenusClickPropHandler.constructor()
- 位置: L22-27
- 役割: コンテキストごとの onclick を ID で保持する Map を作り、dispatchEvent を this に束縛する。
- 触るとき: onclick の保持先が作成元コンテキストと食い違う問題を調べるとき。
- 呼び出し先: `this.dispatchEvent.bind()`
- 参照: `this.context`, `this.dispatchEvent`, `this.onclickMap`

## ContextMenusClickPropHandler.dispatchEvent()
- 位置: L31-41
- 役割: クリックされたメニュー ID に対応する onclick を探し、ユーザー操作として呼び出す。
- 触るとき: onclick が呼ばれない、または別項目のクリックで呼ばれる問題を調べるとき。
- 呼び出し先: `this.onclickMap.get()`
- 条件付き依存: `if (onclick)` → `withHandlingUserInput()`
- 条件付き依存: `if (onclick)` → `onclick()`
- 参照: `info.menuItemId`, `this.context.contentWindow`

## ContextMenusClickPropHandler.setListener()
- 位置: L45-67
- 役割: onclick を登録し、初回なら親の menusInternal.onClicked に dispatchEvent を付け、別コンテキストに同じ ID の handler があれば外す。
- 触るとき: menus.create や update で onclick を設定した後、別コンテキストと取り合いになる問題を調べるとき。
- 呼び出し先: `gPropHandlers.get()`, `gPropHandlers.set()`, `propHandlerMap.set()`, `this.onclickMap.set()`
- 条件付き依存: `if (this.onclickMap.size === 0)` → `this.context.childManager .getParentEvent("menusInternal.onClicked") .addListener()`
- 条件付き依存: `if (this.onclickMap.size === 0)` → `this.context.childManager .getParentEvent()`
- 条件付き依存: `if (this.onclickMap.size === 0)` → `this.context.callOnClose()`
- 条件付き依存: `if (!(!propHandlerMap))` → `propHandlerMap.get()`
- 条件付き依存: `if (propHandler && propHandler !== this)` → `propHandler.unsetListener()`
- 参照: `this.context.extension`, `this.dispatchEvent`, `this.onclickMap.size`

## ContextMenusClickPropHandler.unsetListener()
- 位置: L71-86
- 役割: 指定 ID の onclick を消し、空になったら親イベントのリスナーと close 登録を外す。
- 触るとき: onclick を解除したのに古いハンドラが呼ばれ続ける問題を調べるとき。
- 呼び出し先: `gPropHandlers.get()`, `propHandlerMap.delete()`, `this.onclickMap.delete()`
- 条件付き依存: `if (this.onclickMap.size === 0)` → `this.context.childManager .getParentEvent("menusInternal.onClicked") .removeListener()`
- 条件付き依存: `if (this.onclickMap.size === 0)` → `this.context.childManager .getParentEvent()`
- 条件付き依存: `if (this.onclickMap.size === 0)` → `this.context.forgetOnClose()`
- 条件付き依存: `if (propHandlerMap.size === 0)` → `gPropHandlers.delete()`
- 参照: `propHandlerMap.size`, `this.context.extension`, `this.dispatchEvent`, `this.onclickMap.size`

## ContextMenusClickPropHandler.unsetListenerFromAnyContext()
- 位置: L90-96
- 役割: 拡張の保持情報から同じ ID の onclick を探し、どのコンテキストで作られたものでも解除する。
- 触るとき: menus.remove や onclick: null で作成元以外に残った handler を消す経路を調べるとき。
- 呼び出し先: `gPropHandlers.get()`, `propHandlerMap.get()`
- 条件付き依存: `if (propHandler)` → `propHandler.unsetListener()`
- 参照: `this.context.extension`

## ContextMenusClickPropHandler.deleteAllListenersFromExtension()
- 位置: L99-106
- 役割: 拡張の全 onclick ハンドラを ID ごとに解除する。
- 触るとき: menus.removeAll の後にハンドラが残らないことを確かめるとき。
- 呼び出し先: `gPropHandlers.get()`
- 条件付き依存: `if (propHandlerMap)` → `propHandler.unsetListener()`
- 参照: `this.context.extension`

## ContextMenusClickPropHandler.close()
- 位置: L109-113
- 役割: コンテキストが閉じるとき、そのコンテキストの全 onclick を解除する。
- 触るとき: 拡張の文脈が閉じた後も onclick が残る問題を調べるとき。
- 呼び出し先: `this.onclickMap.keys()`, `this.unsetListener()`

## getAPI()
- 位置: L117-304
- 役割: menus と contextMenus の API オブジェクトを作り、拡張が持つ権限に応じて公開する名前を決める。
- 触るとき: menus と contextMenus のどちらかだけ使えない、権限判定を調べるとき。
- 呼び出し先: `context.extension.hasPermission()`
- 参照: `api.menus`, `result.contextMenus`, `result.menus`

## create()
- 位置: L124-155
- 役割: 永続バックグラウンドなら ID を自動採番し、親の menusInternal.create を呼ぶ。成功後に onclick を登録して callback を実行し、失敗は lastError として返す。
- 触るとき: menus.create の onclick 登録のタイミングやエラー時の表示を変えるとき。
- 呼び出し先: `context.childManager .callParentAsyncFunction()`, `context.childManager .callParentAsyncFunction("menusInternal.create", [createProperties]) .then()`, `context.getCaller()`, `context.withLastError()`
- 条件付き依存: `if (onclick)` → `onClickedProp.setListener()`
- 条件付き依存: `if (callback)` → `context.runSafeWithoutClone()`
- 参照: `context.extension.persistentBackground`, `createProperties.id`, `createProperties.onclick`, `extension.persistentBackground`

## update()
- 位置: L157-178
- 役割: 親の menusInternal.update を呼び、成功後に onclick を設定、null なら解除、未指定なら変更しない。
- 触るとき: menus.update での onclick の扱いを変えるとき。
- 呼び出し先: `context.childManager .callParentAsyncFunction()`, `context.childManager .callParentAsyncFunction("menusInternal.update", [ id, updateProperties, ]) .then()`
- 条件付き依存: `if (onclick)` → `onClickedProp.setListener()`
- 条件付き依存: `if (onclick === null)` → `onClickedProp.unsetListenerFromAnyContext()`
- 参照: `context.extension.persistentBackground`, `updateProperties.onclick`

## remove()
- 位置: L180-186
- 役割: 全コンテキストから onclick を外してから親の menusInternal.remove を呼ぶ。
- 触るとき: menus.remove の後にクリックが届く不具合を調べるとき。
- 呼び出し先: `context.childManager.callParentAsyncFunction()`, `onClickedProp.unsetListenerFromAnyContext()`

## removeAll()
- 位置: L188-195
- 役割: 拡張の全 onclick を外してから親の menusInternal.removeAll を呼ぶ。
- 触るとき: menus.removeAll の後片付けの順序を調べるとき。
- 呼び出し先: `context.childManager.callParentAsyncFunction()`, `onClickedProp.deleteAllListenersFromExtension()`

## overrideContext()
- 位置: L197-270
- 役割: contextOptions を検証し、webExtContextData を作って次の on-prepare-contextmenu で表示中のメニューに反映させる。
- 触るとき: menus.overrideContext の引数検証や、どのメニュー表示に適用されるかを調べるとき。
- 呼び出し先: `Services.obs.addObserver()`, `Services.tm.dispatchToMainThread()`, `checkValidArg()`
- 条件付き依存: `if (checkValidArg("tab", "tabId"))` → `context.extension.hasPermission()`
- 条件付き依存: `if (checkValidArg("bookmark", "bookmarkId"))` → `context.extension.hasPermission()`
- 参照: `context.extension.id`, `contextOptions.bookmarkId`, `contextOptions.context`, `contextOptions.showDefaults`, `contextOptions.tabId`, `pendingMenuEvent.webExtContextData`
- XPCOM: `Services.obs` / `Services.tm`

## checkValidArg()
- 位置: L198-218
- 役割: context が contextType と一致すれば showDefaults の併用を禁じ、必須の propKey があるか確かめる。一致しなければ propKey の指定を禁じる。
- 触るとき: tab や bookmark のコンテキストで tabId や bookmarkId の指定条件を変えるとき。
- 参照: `contextOptions.context`, `contextOptions.showDefaults`

## observe()
- 位置: L249-256
- 役割: on-prepare-contextmenu を受けると、表示中のメニューが拡張の principal に属する場合だけ webExtContextData を設定し、監視を解除する。
- 触るとき: overrideContext の反映先が正しいメニューかを確かめるとき。
- 呼び出し先: `Services.obs.removeObserver()`, `context.principal.subsumes()`
- 条件付き依存: `if (context.principal.subsumes(subject.principal))` → `subject.setWebExtContextData()`
- 参照: `subject.principal`, `subject.wrappedJSObject`, `this.webExtContextData`
- XPCOM: `Services.obs`

## run()
- 位置: L257-266
- 役割: contextmenu イベント中に observe されなかった保留情報を、次のタスクで破棄する。
- 触るとき: overrideContext の効果が残り続ける、または効かないときに調べる。
- 条件付き依存: `if (pendingMenuEvent === this)` → `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## register()
- 位置: L277-291
- 役割: 親の menusInternal.onClicked に listener を付け、子側の onClicked イベントを作る。
- 触るとき: onClicked が発火しない、または二重に届く問題を調べるとき。
- 呼び出し先: `context.childManager.getParentEvent()`, `event.addListener()`, `event.removeListener()`

## listener()
- 位置: L278-282
- 役割: クリック情報を user input として扱い、同期的に onClicked へ流す。
- 触るとき: onClicked の引数や、ユーザー操作として扱われるかを調べるとき。
- 呼び出し先: `fire.sync()`, `withHandlingUserInput()`
- 参照: `context.contentWindow`
