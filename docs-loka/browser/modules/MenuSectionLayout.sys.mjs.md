# browser/modules/MenuSectionLayout.sys.mjs

source: browser/modules/MenuSectionLayout.sys.mjs
source-hash: 886b4aa3da4637d886dc65c3490c2c7b9801058d
lines: 209

## <module>
- 役割: (未記入)

## MenuSectionLayout.constructor()
- 位置: L62-65
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.dynamicItemSelectors`, `this.layout`

## MenuSectionLayout.placementsFor()
- 位置: L75-94
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof entry === "string")` → `result.push()`
- 条件付き依存: `if (!(typeof entry === "string"))` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(entry))` → `result.push()`
- 条件付き依存: `if (!(Array.isArray(entry)))` → `result.push()`
- 参照: `entry.optional`, `entry.selector`, `section.items`

## MenuSectionLayout.arrange()
- 位置: L103-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `MenuSectionLayout.placementsFor()`, `Object.entries()`, `Object.entries(this.layout) .filter()`, `Object.entries(this.layout) .filter(([, sections]) => sections.some(section => section.open)) .map()`, `Object.keys()`, `[...rootPopup.querySelectorAll(selector)].filter()`, `children.filter()`, `children.reduce()`, `claimed.add()`, `claimed.has()`, `fragment.appendChild()`, `node.matches()`, `openPopups.has()`, `ordered.push()`, `orderedByPopup.set()`, `popup.insertBefore()`, `popup.ownerDocument.createDocumentFragment()`, `popups.get()`, `popups.set()`, `rootPopup.querySelector()`, `rootPopup.querySelectorAll()`, `sections.some()`, `this.dynamicItemSelectors.some()`
- 条件付き依存: `if (unplaced.length)` → `unplaced .map(node => (node.id ? "#" + node.id : node.localName)) .join()`
- 条件付き依存: `if (unplaced.length)` → `unplaced .map()`
- 参照: `matches.length`, `node.id`, `node.localName`, `popup.children`, `popup.firstChild`, `rootPopup.id`, `section.open`, `this.layout`, `unplaced.length`
