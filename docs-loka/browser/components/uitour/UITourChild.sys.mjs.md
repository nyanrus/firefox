# browser/components/uitour/UITourChild.sys.mjs

source: browser/components/uitour/UITourChild.sys.mjs
source-hash: 2df3b6e4c51a8e9c077f50fed1da6a9d3c93bbe0
lines: 45

## <module>
- 役割: (未記入)

## UITourChild.handleEvent()
- 位置: L8-18
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UITourUtils.ensureTrustedOrigin()`, `this.sendAsyncMessage()`
- 参照: `event.detail`, `event.type`, `this.document.visibilityState`, `this.manager`

## UITourChild.receiveMessage()
- 位置: L20-29
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sendPageEvent()`
- 参照: `aMessage.data`, `aMessage.name`

## UITourChild.sendPageEvent()
- 位置: L31-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cu.cloneInto()`, `UITourUtils.ensureTrustedOrigin()`, `win.document.dispatchEvent()`
- 参照: `this.contentWindow`, `this.manager`, `win.CustomEvent`
