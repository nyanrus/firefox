# browser/components/aiwindow/ui/components/smartwindow-topsites/smartwindow-topsites.mjs

source: browser/components/aiwindow/ui/components/smartwindow-topsites/smartwindow-topsites.mjs
source-hash: 690911458907ad346a19696280792384499ccbf1
lines: 76

## <module>
- 役割: スマートバー下に並ぶトップサイトのタイル列を描く custom element を定義する
- 呼び出し先: `customElements.define()`

## SmartWindowTopSites.constructor()
- 位置: L20-23
- 役割: sites を空配列で初期化する
- 触るとき: サイト一覧が未設定のときの既定値を調べるとき
- 呼び出し先: `super()`
- 参照: `this.sites`

## SmartWindowTopSites.#siteSelected()
- 位置: L25-33
- 役割: url と位置(position)を付けて SmartWindowTopSites:site-selected を発火する
- 触るとき: 選択時に親へ渡す情報(位置など)を増やすとき、イベントの受け側を調べるとき
- 呼び出し先: `this.dispatchEvent()`
- 参照: `site.url`

## SmartWindowTopSites.#iconSrc()
- 位置: L35-37
- 役割: tippyTopIcon、favicon、page-icon:URL の順にアイコンの参照先を選ぶ
- 触るとき: アイコンが表示されないときや、取得元の優先順位を変えるとき
- 参照: `site.favicon`, `site.tippyTopIcon`, `site.url`

## SmartWindowTopSites.render()
- 位置: L39-72
- 役割: sites が空なら何も描かず、各サイトを a 要素のタイルとして描画し、クリックは既定遷移を止めて通知する
- 触るとき: タイルの見た目、表示名(label か hostname)、クリック時の挙動を変えるとき
- 呼び出し先: `e.preventDefault()`, `html()`, `this.#iconSrc()`, `this.#siteSelected()`, `this.sites.map()`
- 条件付き依存: `if (!this.sites.length)` → `html()`
- 参照: `site.hostname`, `site.label`, `site.url`, `this.sites.length`
