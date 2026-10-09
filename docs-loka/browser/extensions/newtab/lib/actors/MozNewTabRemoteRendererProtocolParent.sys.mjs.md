# browser/extensions/newtab/lib/actors/MozNewTabRemoteRendererProtocolParent.sys.mjs

source: browser/extensions/newtab/lib/actors/MozNewTabRemoteRendererProtocolParent.sys.mjs
source-hash: 546ab8c7bc4d8c9c39e10b0b703bec569a2bec24
lines: 133

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`

## logConsole()
- 位置: L10-19
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `console.createInstance()`
- XPCOM: `Services.prefs`

## MozNewTabRemoteRendererProtocolParent.assignRenderer()
- 位置: async L32-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AboutNewTab.activityStream.remoteRenderer.assign()`
- 条件付き依存: `if (this.#assignedRenderer)` → `lazy.logConsole.warn()`
- 参照: `this.#assignedRenderer`, `this.#assignedRenderer.appProps`

## MozNewTabRemoteRendererProtocolParent.receiveMessage()
- 位置: L45-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#getInputStream()`
- 条件付き依存: `if ( !this.manager.isInProcess && this.manager.remoteType !== lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE )` → `Promise.reject()`
- 参照: `lazy.E10SUtils.PRIVILEGEDABOUT_REMOTE_TYPE`, `message.data.uriString`, `message.name`, `this.manager.isInProcess`, `this.manager.remoteType`

## MozNewTabRemoteRendererProtocolParent.#getInputStream()
- 位置: async L61-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.io.newURI()`, `lazy.logConsole.error()`, `this.getScriptResource()`, `this.getStyleResource()`
- 条件付き依存: `if (!this.#assignedRenderer)` → `lazy.logConsole.error()`
- 参照: `this.#assignedRenderer`, `uri.host`, `uri.scheme`
- XPCOM: `Services.io`

## MozNewTabRemoteRendererProtocolParent.getScriptResource()
- 位置: async L103-116
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AboutNewTab.activityStream.remoteRenderer.getScriptResource()`
- 条件付き依存: `if (!this.#assignedRenderer)` → `lazy.logConsole.error()`
- 参照: `this.#assignedRenderer`

## MozNewTabRemoteRendererProtocolParent.getStyleResource()
- 位置: async L118-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.AboutNewTab.activityStream.remoteRenderer.getStyleResource()`
- 条件付き依存: `if (!this.#assignedRenderer)` → `lazy.logConsole.error()`
- 参照: `this.#assignedRenderer`
