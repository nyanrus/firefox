# browser/actors/BrowserTabChild.sys.mjs

source: browser/actors/BrowserTabChild.sys.mjs
source-hash: 2c261cebb62a599ac7532cb4c1116ea4c7c7ae91
lines: 21

## <module>
- 役割: タブ（ブラウジングコンテキスト）ごとのコンテンツ側アクター。親からのエンコーディング検出要求を docShell へ渡す。

## BrowserTabChild.constructor()
- 位置: L6-8
- 役割: 基底クラスのコンストラクタを呼ぶだけで、独自の初期化はしていない。
- 触るとき: アクター生成時に状態を追加するときに見る。
- 呼び出し先: `super()`

## BrowserTabChild.receiveMessage()
- 位置: L10-19
- 役割: ForceEncodingDetection を受け、現在のブラウジングコンテキストの docShell でエンコーディング検出を強制する。
- 触るとき: 文字化けしたページを再判定させる経路を変えるときに見る。
- 呼び出し先: `docShell.forceEncodingDetection()`
- 参照: `context.docShell`, `message.name`, `this.manager.browsingContext`
