# browser/components/remotecontrol/RemoteControlBanner.sys.mjs

source: browser/components/remotecontrol/RemoteControlBanner.sys.mjs
source-hash: 0a38a985074119ff570139cce5ce3c6f6d5ae60d
lines: 352

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `RemoteControlBanner.onBannerPrefChanged()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## RemoteControlBannerClass.constructor()
- 位置: L74-82
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `BANNER_STATES.NONE`, `this.#initialized`, `this.#state`, `this.#stoppedState`, `this.#stopping`

## RemoteControlBannerClass.init()
- 位置: L84-91
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.RemoteControlServers.addListener()`
- 参照: `this.#initialized`, `this.#onServersChanged`

## RemoteControlBannerClass.onBannerPrefChanged()
- 位置: L98-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#update()`
- 参照: `this.#initialized`

## RemoteControlBannerClass.uninit()
- 位置: L105-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.RemoteControlServers.removeListener()`, `this.#hide()`
- 参照: `BANNER_STATES.NONE`, `this.#initialized`, `this.#onServersChanged`, `this.#state`, `this.#stoppedState`

## RemoteControlBannerClass.#addNotification()
- 位置: L120-143
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `notificationBox.appendNotification()`, `this.#getButtons()`, `this.#getMessageId()`, `this.#removeNotification()`
- 参照: `BANNER_STATES.STOPPED`, `notificationBox.PRIORITY_INFO_HIGH`, `notificationBox.PRIORITY_WARNING_HIGH`, `this.#state`, `win.gNotificationBox`

## eventCallback()
- 位置: L134-139
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event == "dismissed")` → `this.#hide()`

## RemoteControlBannerClass.#getButtons()
- 位置: L145-178
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `BANNER_STATES.CONNECTED`, `this.#state`

## callback()
- 位置: L154-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#stopServers()`

## callback()
- 位置: L165-168
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#stopServers()`

## callback()
- 位置: L172-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#stopServers()`

## RemoteControlBannerClass.#getMessageId()
- 位置: L180-193
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `BANNER_STATES.CONNECTED`, `BANNER_STATES.RUNNING`, `BANNER_STATES.STOPPED`, `STOPPED_STATES.DISABLED`, `this.#state`, `this.#stoppedState`

## RemoteControlBannerClass.#getNotification()
- 位置: L195-197
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `win.gNotificationBox.getNotificationWithValue()`

## RemoteControlBannerClass.#getState()
- 位置: L199-225
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `BANNER_STATES.CONNECTED`, `BANNER_STATES.NONE`, `BANNER_STATES.RUNNING`, `BANNER_STATES.STOPPED`, `lazy.RemoteControlServers.hasActiveSession`, `lazy.RemoteControlServers.runningDynamically`, `lazy.connectionBannerEnabled`, `lazy.dynamicStartBannerEnabled`, `this.#stoppedState`

## RemoteControlBannerClass.#hide()
- 位置: L227-235
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.EveryWindow.unregisterCallback()`, `this.#removeNotification()`
- 参照: `lazy.EveryWindow.readyWindows`

## RemoteControlBannerClass.#onServersChanged()
- 位置: L237-239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#update()`

## RemoteControlBannerClass.#removeNotification()
- 位置: L241-246
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getNotification()`
- 条件付き依存: `if (notification)` → `win.gNotificationBox.removeNotification()`

## RemoteControlBannerClass.#show()
- 位置: L248-254
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.EveryWindow.registerCallback()`, `this.#addNotification()`, `this.#removeNotification()`

## RemoteControlBannerClass.#showStoppedConfirmation()
- 位置: L260-273
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.EveryWindow.readyWindows.filter()`, `this.#addNotification()`, `this.#getNotification()`, `this.#hide()`

## RemoteControlBannerClass.#stopServers()
- 位置: async L284-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `lazy.RemoteControlServers.stop()`, `this.#update()`
- 条件付き依存: `if (permanently)` → `Services.prefs.setBoolPref()`
- 参照: `STOPPED_STATES.DISABLED`, `STOPPED_STATES.STOPPED`, `this.#stoppedState`, `this.#stopping`
- XPCOM: `Services.prefs`

## RemoteControlBannerClass.#update()
- 位置: L316-348
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getState()`, `this.#hide()`, `this.#show()`, `this.#showStoppedConfirmation()`
- 参照: `BANNER_STATES.CONNECTED`, `BANNER_STATES.NONE`, `BANNER_STATES.RUNNING`, `BANNER_STATES.STOPPED`, `lazy.RemoteControlServers.runningDynamically`, `this.#state`, `this.#stoppedState`, `this.#stopping`
