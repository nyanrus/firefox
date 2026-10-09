# browser/actors/PageInfoPreviewChild.sys.mjs

source: browser/actors/PageInfoPreviewChild.sys.mjs
source-hash: 1c7279829757d94dde973c4e79b42e22014a8d86
lines: 38

## <module>
- 役割: ページ情報のプレビューで、画像の表示サイズを親からの指示で変える子側アクター。

## PageInfoPreviewChild.receiveMessage()
- 位置: async L6-12
- 役割: PageInfoPreview:resize のときだけ resize を呼び、その結果を返す。
- 触るとき: リサイズ要求の受け口を変えるとき。
- 条件付き依存: `if (message.name === "PageInfoPreview:resize")` → `this.resize()`
- 参照: `message.data`, `message.name`, `this.contentWindow.document`

## PageInfoPreviewChild.resize()
- 位置: L14-36
- 役割: 先頭の img に指定の幅と高さを設定し、元サイズと現在サイズを返す。img がなければ undefined。
- 触るとき: プレビュー画像のサイズ計算や返す値を変えるとき。
- 呼び出し先: `document.querySelector()`
- 参照: `data.height`, `data.width`, `img.height`, `img.naturalHeight`, `img.naturalWidth`, `img.width`
