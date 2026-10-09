# browser/actors/PluginParent.sys.mjs

source: browser/actors/PluginParent.sys.mjs
source-hash: 498e9622c8bde67f7fb8af7916eca114e44b0f46
lines: 204

## <module>
- 役割: GMP のクラッシュ情報を集め、クラッシュ報告の送信やタブ上の通知バーを扱う親側の仕組み。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `Services.strings.createBundle()`

## observe()
- 位置: L21-27
- 役割: gmp-plugin-crash のオブザーバー通知を受け、_registerGMPCrash に渡す。
- 触るとき: クラッシュ通知の受け口を変えるとき。
- 呼び出し先: `this._registerGMPCrash()`

## _registerGMPCrash()
- 位置: L29-60
- 役割: プロパティバッグからクラッシュ情報を読み、ダンプ ID があれば記録して、各コンテンツプロセスへ同じ通知をブロードキャストする。
- 触るとき: クラッシュ情報の保存や子プロセスへの伝播を変えるとき。
- 呼び出し先: `propertyBag.getPropertyAsACString()`, `propertyBag.getPropertyAsAString()`, `propertyBag.getPropertyAsUint32()`, `propertyBag.hasKey()`
- 条件付き依存: `if ( !(propertyBag instanceof Ci.nsIWritablePropertyBag2) || !propertyBag.hasKey("pluginID") || !propertyBag.hasKey("pluginDumpID") || !propertyBag.hasKey("plugi...)` → `console.error()`
- 条件付き依存: `if (pluginDumpID)` → `this.gmpCrashes.set()`
- 条件付き依存: `if (Services.ppmm)` → `Services.ppmm.broadcastAsyncMessage()`
- 参照: `Ci.nsIWritablePropertyBag2`, `Services.ppmm`
- XPCOM: [`nsIWritablePropertyBag2`](../../xpcom/ds/nsIWritablePropertyBag2.idl.md) / `Services.ppmm`

## submitCrashReport()
- 位置: L73-94
- 役割: 記録したダンプ ID でクラッシュ報告を送信し、記録から削除する。報告が見つからなければエラーを出して終える。
- 触るとき: クラッシュ報告の送信条件や付加情報を変えるとき。
- 呼び出し先: `lazy.CrashSubmit.submit()`, `this.getCrashReport()`, `this.gmpCrashes.delete()`
- 条件付き依存: `if (!report)` → `console.error()`
- 条件付き依存: `if (!report)` → `JSON.stringify()`
- 参照: `lazy.CrashSubmit.SUBMITTED_FROM_CRASH_TAB`, `pluginCrashID.pluginID`

## getCrashReport()
- 位置: L96-98
- 役割: プラグイン ID に対応する記録済みクラッシュ情報を返す。
- 触るとき: クラッシュ情報の参照方法を変えるとき。
- 呼び出し先: `this.gmpCrashes.get()`
- 参照: `pluginCrashID.pluginID`

## PluginParent.receiveMessage()
- 位置: L102-118
- 役割: PluginContent:ShowPluginCrashedNotification を受け、対象ブラウザに通知バーを出させる。
- 触るとき: 通知を出すメッセージの扱いを変えるとき。
- 呼び出し先: `console.error()`, `this.showPluginCrashedNotification()`
- 参照: `msg.data.pluginCrashID`, `msg.name`, `this.manager.rootFrameLoader.ownerElement`

## PluginParent.showPluginCrashedNotification()
- 位置: L129-202
- 役割: 同じ通知がなく報告があるとき、再読み込み・報告送信(対応ビルドのみ)・詳細リンクのボタン付きの警告通知を出す。
- 触るとき: クラッシュ通知の文言やボタン構成を変えるとき。
- 呼び出し先: `PluginManager.getCrashReport()`, `browser.getTabBrowser()`, `browser.getTabBrowser().getNotificationBox()`, `buttons.push()`, `lazy.gNavigatorBundle.GetStringFromName()`, `lazy.gNavigatorBundle.formatStringFromName()`, `notificationBox.appendNotification()`, `notificationBox.getNotificationWithValue()`
- 条件付き依存: `if (AppConstants.MOZ_CRASHREPORTER)` → `lazy.gNavigatorBundle.GetStringFromName()`
- 条件付き依存: `if (AppConstants.MOZ_CRASHREPORTER)` → `buttons.push()`
- 参照: `AppConstants.MOZ_CRASHREPORTER`, `notificationBox.PRIORITY_WARNING_MEDIUM`, `report.pluginName`

## PluginParent.callback()
- 位置: L155-157
- 役割: 「再読み込み」ボタンで対象ブラウザを reload する。
- 触るとき: 再読み込みボタンの動作を変えるとき。
- 呼び出し先: `browser.reload()`

## callback()
- 位置: L172-174
- 役割: 「報告を送信」ボタンで PluginManager.submitCrashReport を呼ぶ。
- 触るとき: 報告送信ボタンの動作を変えるとき。
- 呼び出し先: `PluginManager.submitCrashReport()`
