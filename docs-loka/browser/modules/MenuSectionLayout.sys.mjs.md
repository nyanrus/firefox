# browser/modules/MenuSectionLayout.sys.mjs

source: browser/modules/MenuSectionLayout.sys.mjs
source-hash: 886b4aa3da4637d886dc65c3490c2c7b9801058d
lines: 209

## <module>
- 役割: メニュー(menupopup)の子要素を、宣言したセクション順に並べ替える仕組み。

## MenuSectionLayout.constructor()
- 位置: L62-65
- 役割: ポップアップIDごとのセクション定義と、整列の対象外にする動的項目のセレクターを保持する。
- 触るとき: 実行時に挿入される項目(タブグループやプロファイルなど)を整列の検査から外すとき。
- 参照: `this.dynamicItemSelectors`, `this.layout`

## MenuSectionLayout.placementsFor()
- 位置: L75-94
- 役割: セクションの項目を、selector と optional の組に平坦化する。
- 触るとき: 項目の書式(文字列、配列、optional 指定)の解釈を変えるとき。
- 条件付き依存: `if (typeof entry === "string")` → `result.push()`
- 条件付き依存: `if (!(typeof entry === "string"))` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(entry))` → `result.push()`
- 条件付き依存: `if (!(Array.isArray(entry)))` → `result.push()`
- 参照: `entry.optional`, `entry.selector`, `section.items`

## MenuSectionLayout.arrange()
- 位置: L103-207
- 役割: 各セレクターを一意に解決し、全子要素が宣言されているか検査してから、宣言順に移動する。
- 触るとき: メニューの項目が二重に掴まれる、未配置の子があると例外になる、といった報告を調べるとき。検査で失敗すると、メニューは変更されない。open のセクションでは末尾の外部項目を検査から外す。
- 呼び出し先: `MenuSectionLayout.placementsFor()`, `Object.entries()`, `Object.entries(this.layout) .filter()`, `Object.entries(this.layout) .filter(([, sections]) => sections.some(section => section.open)) .map()`, `Object.keys()`, `[...rootPopup.querySelectorAll(selector)].filter()`, `children.filter()`, `children.reduce()`, `claimed.add()`, `claimed.has()`, `fragment.appendChild()`, `node.matches()`, `openPopups.has()`, `ordered.push()`, `orderedByPopup.set()`, `popup.insertBefore()`, `popup.ownerDocument.createDocumentFragment()`, `popups.get()`, `popups.set()`, `rootPopup.querySelector()`, `rootPopup.querySelectorAll()`, `sections.some()`, `this.dynamicItemSelectors.some()`
- 条件付き依存: `if (unplaced.length)` → `unplaced .map(node => (node.id ? "#" + node.id : node.localName)) .join()`
- 条件付き依存: `if (unplaced.length)` → `unplaced .map()`
- 参照: `matches.length`, `node.id`, `node.localName`, `popup.children`, `popup.firstChild`, `rootPopup.id`, `section.open`, `this.layout`, `unplaced.length`
