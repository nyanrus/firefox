# browser/components/aboutlogins/content/components/login-list-section.mjs

source: browser/components/aboutlogins/content/components/login-list-section.mjs
source-hash: 5495f55e28a534f218082196a5d3a783b8a8183b
lines: 35

## <module>
- 役割: ログイン一覧のセクション見出し(#login-list-section-template)を作る・更新するファクトリ。見出し ID の接頭辞 id- を解釈する

## LoginListHeaderFactory.create()
- 位置: L8-16
- 役割: テンプレートから見出し要素を複製し、見出し文言を流し込んで返す
- 触るとき: 一覧にセクションを新しく作るとき
- 呼び出し先: `document.querySelector()`, `template.content.cloneNode()`, `this.update()`
- 参照: `fragment.firstElementChild`

## LoginListHeaderFactory.update()
- 位置: L18-33
- 役割: 見出しが id- で始まればローカライズ ID として、それ以外は文字列として表示し、空なら見出しを隠す
- 触るとき: セクション見出しの表示文言の出し分けを変えるとき。ID は login-list.mjs の headersFnOptions が返す
- 呼び出し先: `headerItem.querySelector()`
- 条件付き依存: `if (header)` → `header.startsWith()`
- 条件付き依存: `if (header.startsWith(this.ID_PREFIX))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (header.startsWith(this.ID_PREFIX))` → `header.substring()`
- 参照: `headerElement.hidden`, `headerElement.textContent`, `this.ID_PREFIX`, `this.ID_PREFIX.length`
