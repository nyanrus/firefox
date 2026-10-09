# browser/components/downloads/DownloadsViewableInternally.sys.mjs

source: browser/components/downloads/DownloadsViewableInternally.sys.mjs
source-hash: 6b508b700f148af560a7c448b3e8283f6f9927ad
lines: 336

## <module>
- 役割: ダウンロードしたファイルを Firefox 内で開く種類 (XML、SVG、WebP など) を MIME ハンドラーとして登録・解除し、ダウンロード統合へ判定を渡す。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyServiceGetter()`

## register()
- 位置: L46-74
- 役割: enabledTypes の監視を張り、各種類の初期化を行ってハンドラーを更新し、DownloadIntegration に内部表示の判定関数を登録する。
- 触るとき: 起動時に内部表示の設定が反映されない、または判定が DownloadIntegration に届かないときに見る。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `itemStr.split()`, `itemStr.split(",").map()`, `lazy.Integration.downloads.register()`, `pref.trim()`, `s.trim()`, `this._shouldViewDownloadInternally.bind()`, `this._updateAllHandlers()`
- 条件付き依存: `if (handlerType.initAvailable)` → `handlerType.initAvailable()`
- 参照: `handlerType.initAvailable`, `this._downloadTypesViewableInternally`

## initAvailable()
- 位置: L112-122
- 役割: SVG の available を svg.disabled の反転として遅延取得し、変化時にハンドラーを更新する。
- 触るとき: svg.disabled を切り替えても SVG の内部表示が追随しないときに見る。
- 呼び出し先: `DownloadsViewableInternally._updateHandler()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## initAvailable()
- 位置: L141-149
- 役割: JPEG XL の available を image.jxl.enabled から遅延取得し、変化時にハンドラーを更新する。
- 触るとき: JPEG XL の内部表示を有効化する条件を変えるとき。
- 呼び出し先: `DownloadsViewableInternally._updateHandler()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## _shouldViewDownloadInternally()
- 位置: L167-186
- 役割: MIME 型か拡張子が一致し、有効な種類のどれかに当たれば true を返す。managedElsewhere でない種類は enabledTypes に含まれている必要がある。
- 触るとき: ダウンロードが内部で開かれるべきなのに外部アプリで開かれる、またはその逆の問題を調べるとき。
- 呼び出し先: `aExtension?.toLowerCase()`, `handlerType.mimeTypes.includes()`, `this._downloadTypesViewableInternally.some()`, `this._enabledTypes.includes()`
- 参照: `handlerType.available`, `handlerType.extension`, `handlerType.managedElsewhere`

## _makeFakeHandler()
- 位置: L188-205
- 役割: 内部表示用の nsIMIMEInfo 風オブジェクトを作る。preferredAction は handleInternally に固定する。
- 触るとき: ハンドラー登録に使う偽の MIME 情報の中身を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/array;1"].createInstance()`, `ChromeUtils.generateQI()`
- 参照: `Ci.nsIHandlerInfo.handleInternally`, `Ci.nsIMutableArray`
- XPCOM: [`nsIHandlerInfo`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / [`nsIMutableArray`](../../../docshell/shistory/nsISHEntry.idl.md) / `@mozilla.org/array;1`

## getFileExtensions()
- 位置: L192-194
- 役割: 偽ハンドラーが持つ拡張子を 1 つだけ返す。
- 触るとき: 偽ハンドラーの拡張子情報が使われる箇所を追うとき。

## extensionExists()
- 位置: L198-200
- 役割: 偽ハンドラーの拡張子と引数の拡張子が一致するかを返す。
- 触るとき: 偽ハンドラーが拡張子の存在を問われたときの応答を確認するとき。

## _saveSettings()
- 位置: L207-216
- 役割: ハンドラーの元の preferredAction と alwaysAskBeforeHandling を、種類ごとの pref に退避する。
- 触るとき: 内部表示を有効にした後に元の動作へ戻せない問題を調べるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`, `Services.prefs.setIntPref()`
- 参照: `handlerInfo.alwaysAskBeforeHandling`, `handlerInfo.preferredAction`, `handlerType.extension`
- XPCOM: `Services.prefs`

## _restoreSettings()
- 位置: L218-230
- 役割: 退避した設定があれば復元して保存し、なければそのハンドラーを削除する。
- 触るとき: 内部表示を無効にしたときに OS の既定動作が戻らない問題を調べるとき。
- 呼び出し先: `Services.prefs.prefHasUserValue()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(prevActionPref))` → `Services.prefs.getBoolPref()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(prevActionPref))` → `Services.prefs.getIntPref()`
- 条件付き依存: `if (Services.prefs.prefHasUserValue(prevActionPref))` → `lazy.HandlerService.store()`
- 条件付き依存: `if (!(Services.prefs.prefHasUserValue(prevActionPref)))` → `lazy.HandlerService.remove()`
- 参照: `handlerInfo.alwaysAskBeforeHandling`, `handlerInfo.preferredAction`, `handlerType.extension`
- XPCOM: `Services.prefs`

## _clearSavedSettings()
- 位置: L232-235
- 役割: 種類ごとに退避した 2 つの pref を消す。
- 触るとき: 退避情報が残ったままになる問題を調べるとき。
- 呼び出し先: `Services.prefs.clearUserPref()`
- XPCOM: `Services.prefs`

## _updateAllHandlers()
- 位置: L237-244
- 役割: managedElsewhere でない全種類について、ハンドラーの登録状態を更新する。
- 触るとき: enabledTypes を変更した後にどの種類が登録・解除されたかを追うとき。
- 条件付き依存: `if (!handlerType.managedElsewhere)` → `this._updateHandler()`
- 参照: `handlerType.managedElsewhere`, `this._downloadTypesViewableInternally`

## _updateHandler()
- 位置: L246-261
- 役割: 有効化されていて未登録なら登録し、無効化されていて登録済みなら解除する。
- 触るとき: 特定の種類だけ内部表示が切り替わらないときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`, `this._enabledTypes.includes()`
- 条件付き依存: `if (toBeRegistered && !wasRegistered)` → `this._becomeHandler()`
- 条件付き依存: `if (!toBeRegistered && wasRegistered)` → `this._unbecomeHandler()`
- 参照: `handlerType.available`, `handlerType.extension`
- XPCOM: `Services.prefs`

## _becomeHandler()
- 位置: L263-311
- 役割: ハンドラーが未登録なら偽情報を保存し、既存なら元の preferredAction を退避して handleInternally に切り替える。最後に登録済みフラグを立てる。
- 触るとき: 内部表示を有効にした際に既存の OS ハンドラー設定が上書きされる問題を調べるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`, `lazy.HandlerService.exists()`, `this._makeFakeHandler()`
- 条件付き依存: `if (!lazy.HandlerService.exists(fakeHandlerInfo))` → `lazy.HandlerService.store()`
- 条件付き依存: `if (!(!lazy.HandlerService.exists(fakeHandlerInfo)))` → `lazy.MIMEService.getFromTypeAndExtension()`
- 条件付き依存: `if (handlerInfo.preferredAction != Ci.nsIHandlerInfo.handleInternally)` → `this._saveSettings()`
- 条件付き依存: `if (!(handlerInfo.preferredAction != Ci.nsIHandlerInfo.handleInternally))` → `this._clearSavedSettings()`
- 条件付き依存: `if ( handlerInfo.preferredAction != Ci.nsIHandlerInfo.useHelperApp && handlerInfo.preferredAction != Ci.nsIHandlerInfo.useSystemDefault )` → `lazy.HandlerService.store()`
- 参照: `Ci.nsIHandlerInfo.handleInternally`, `Ci.nsIHandlerInfo.useHelperApp`, `Ci.nsIHandlerInfo.useSystemDefault`, `handlerInfo.alwaysAskBeforeHandling`, `handlerInfo.preferredAction`, `handlerType.extension`, `handlerType.mimeTypes`
- XPCOM: [`nsIHandlerInfo`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / `Services.prefs`

## _unbecomeHandler()
- 位置: L313-334
- 役割: preferredAction がまだ handleInternally なら退避値を復元し、退避情報と登録済みフラグを消す。
- 触るとき: 内部表示を無効にした後に OS の既定アプリが戻らない問題を調べるとき。
- 呼び出し先: `Services.prefs.clearUserPref()`, `lazy.MIMEService.getFromTypeAndExtension()`, `this._clearSavedSettings()`
- 条件付き依存: `if (handlerInfo?.preferredAction == Ci.nsIHandlerInfo.handleInternally)` → `this._restoreSettings()`
- 参照: `Ci.nsIHandlerInfo.handleInternally`, `handlerInfo?.preferredAction`, `handlerType.extension`, `handlerType.mimeTypes`
- XPCOM: [`nsIHandlerInfo`](../../../netwerk/mime/nsIMIMEInfo.idl.md) / `Services.prefs`
