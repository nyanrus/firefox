# browser/actors/PluginChild.sys.mjs

source: browser/actors/PluginChild.sys.mjs
source-hash: 8dda1191040ad8f16878d38f92f826fc2fc7a370
lines: 95

## <module>
- 役割: GMP(ゲーム/メディアプラグイン)のクラッシュイベントを子プロセス側で受け、親へ通知を依頼するアクター。

## PluginChild.handleEvent()
- 位置: L7-18
- 役割: 自分の文書のイベントだけを対象に、PluginCrashed を onPluginCrashed へ回す。
- 触るとき: クラッシュイベントの受け付け条件を変えるとき。
- 条件付き依存: `if (eventType == "PluginCrashed")` → `this.onPluginCrashed()`
- 参照: `event.target.document`, `event.target.ownerDocument`, `event.type`, `this.document`

## PluginChild.isWithinFullScreenElement()
- 位置: L32-65
- 役割: クラッシュしたプラグインが全画面要素の子孫かを、iframe の親をたどって判定する。
- 触るとき: 全画面解除の判定を直すとき。
- 呼び出し先: `fullScreenElement.contains()`
- 条件付き依存: `if (fullScreenElement.tagName === "IFRAME")` → `getTrueFullScreenElement()`
- 条件付き依存: `if (parentIframe)` → `this.isWithinFullScreenElement()`
- 参照: `domElement.documentGlobal.frameElement`, `fullScreenElement.tagName`

## getTrueFullScreenElement()
- 位置: L41-51
- 役割: iframe の中で全画面になっている実際の要素を、再帰的にたどって返す。
- 触るとき: 入れ子の iframe で全画面要素が正しく取れない不具合を調べるとき。
- 条件付き依存: `if ( typeof fullScreenIframe.contentDocument !== "undefined" && fullScreenIframe.contentDocument.mozFullScreenElement )` → `getTrueFullScreenElement()`
- 参照: `fullScreenIframe.contentDocument`, `fullScreenIframe.contentDocument.mozFullScreenElement`

## PluginChild.onPluginCrashed()
- 位置: async L71-93
- 役割: 全画面中ならプラグインを含む場合に全画面を解除し、通知を親へ送る。gmpPlugin がなければ何もしない。
- 触るとき: クラッシュ後の全画面解除や通知依頼の条件を変えるとき。
- 呼び出し先: `this.contentWindow.PluginCrashedEvent.isInstance()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (fullScreenElement)` → `this.isWithinFullScreenElement()`
- 条件付き依存: `if (this.isWithinFullScreenElement(fullScreenElement, target))` → `this.contentWindow.top.document.mozCancelFullScreen()`
- 参照: `target.document`, `this.contentWindow.top.document.mozFullScreenElement`
