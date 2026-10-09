# browser/base/content/contentTheme.js

source: browser/base/content/contentTheme.js
source-hash: 73bd581c6cc9496e4798114332029f8d06834511
lines: 214

## <module>
- 役割: LightweightTheme(テーマ)の色を、about:newtab などのコンテンツページのルート要素の CSS 変数と属性へ反映するコントローラーを定義し起動する。
- 呼び出し先: `ContentThemeController.init()`, `window.matchMedia()`

## _isTextColorDark()
- 位置: L10-12
- 役割: RGB 値を輝度式(0.2125R+0.7154G+0.0721B)に通し、110 以下なら暗い色として true を返す。
- 触るとき: テーマの文字色が明るいか暗いかの判定基準を変えるとき、または lwt-sidebar や lwt-newtab-brighttext の付与結果がおかしいとき。

## processColor()
- 位置: L19-26
- 役割: --newtab-background-color 用に、RGBA 値を alpha を捨てた rgb() 文字列へ変換する。値が無ければ null を返す。
- 触るとき: 新規タブの背景色が透明度付きで渡されてきたときの扱いを変えるとき、またはテーマ背景色が反映されない原因を調べるとき。

## processColor()
- 位置: L45-59
- 役割: --newtab-text-primary-color 用に、lwt-newtab 属性を値の有無で付け替え、テーマ無しなら prefers-color-scheme に合わせて lwt-newtab-brighttext を立てる。テーマ有りなら輝度で brighttext を決め rgba を返す。
- 触るとき: 新規タブの文字色テーマと明暗切替(brighttext)の連動を変えるとき、またはダークモード時に文字が読めない問題を調べるとき。
- 呼び出し先: `_isTextColorDark()`, `element.toggleAttribute()`
- 条件付き依存: `if (!rgbaChannels)` → `element.toggleAttribute()`
- 参照: `prefersDarkQuery.matches`

## processColor()
- 位置: L66-68
- 役割: --in-content-zap-gradient 用に、テーマの値をそのまま返す(加工しない)。
- 触るとき: Zap グラデーションの値の扱いを変えるとき、または値が CSS にそのまま入っているか確認するとき。

## processColor()
- 位置: L75-82
- 役割: --sidebar-background-color 用に、RGBA を alpha を捨てた rgb() 文字列へ変換する。値が無ければ null を返す。
- 触るとき: サイドバー背景色の反映方法を変えるとき、またはサイドバー背景が透明なテーマで色が崩れる原因を調べるとき。

## processColor()
- 位置: L89-102
- 役割: --sidebar-text-color 用に、テキスト色の輝度から lwt-sidebar 属性を light または dark に設定し、rgba を返す。値が無ければ属性を外して null を返す。
- 触るとき: サイドバー文字色に応じたアイコンや見た目の切替を変えるとき、またはテーマ適用後にサイドバーの属性が残る原因を調べるとき。
- 呼び出し先: `_isTextColorDark()`, `element.setAttribute()`
- 条件付き依存: `if (!rgbaChannels)` → `element.removeAttribute()`

## processColor()
- 位置: L109-117
- 役割: --lwt-sidebar-highlight-background-color 用に、lwt-sidebar-highlight 属性を値の有無で付け替え、rgba を返す。値が無ければ null を返す。
- 触るとき: サイドバーの選択項目の背景色テーマを変えるとき、または選択ハイライトが消えない原因を調べるとき。
- 呼び出し先: `element.toggleAttribute()`

## processColor()
- 位置: L130-132
- 役割: --ai-background-color 用に、テーマの値をそのまま返す(加工しない)。
- 触るとき: AI 関連の背景色の値の扱いを変えるとき。

## init()
- 位置: L147-154
- 役割: LightweightTheme:Set イベントを自身のハンドラーとして購読し、prefers-color-scheme のメディアクエリ変化も監視する。
- 触るとき: テーマ更新イベントの購読先を増やすとき、またはテーマが初回に反映されない原因を調べるとき。
- 呼び出し先: `addEventListener()`, `prefersDarkQuery.addEventListener()`

## handleEvent()
- 位置: L162-173
- 役割: LightweightTheme:Set ならテーマデータを _setProperties へ渡し、change なら lwt-newtab 属性が無い場合に lwt-newtab-brighttext をシステムのダーク設定へ合わせる。
- 触るとき: テーマ更新時やシステムのダークモード切替時の挙動を変えるとき、またはダークモードへ切り替えたのに新規タブの文字色が変わらないとき。
- 条件付き依存: `if (event.type == "LightweightTheme:Set")` → `this._setProperties()`
- 条件付き依存: `if (event.type == "change")` → `root.hasAttribute()`
- 条件付き依存: `if (!root.hasAttribute("lwt-newtab"))` → `root.toggleAttribute()`
- 参照: `document.documentElement`, `event.detail.data`, `event.matches`, `event.type`

## _setProperty()
- 位置: L182-188
- 役割: 値があれば要素の style に CSS 変数を設定し、値が空なら removeProperty で削除する。
- 触るとき: CSS 変数の設定や削除の条件を変えるとき、またはテーマを外しても古い色が残るとき。
- 条件付き依存: `if (value)` → `elem.style.setProperty()`
- 条件付き依存: `if (!(value))` → `elem.style.removeProperty()`

## _setProperties()
- 位置: L195-210
- 役割: inContentVariableMap の各項目について、テーマデータから lwtProperty の値を取り出し、processColor があればそれで加工、無ければ rgba 文字列化して、ルート要素に CSS 変数を設定する。
- 触るとき: 新しいテーマ項目や CSS 変数を追加するとき、またはテーマ色がルート要素へ正しく渡らないとき。
- 呼び出し先: `this._setProperty()`
- 条件付き依存: `if (processColor)` → `processColor()`
- 参照: `document.documentElement`
