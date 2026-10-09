# browser/components/aboutlogins/content/components/login-list-item.mjs

source: browser/components/aboutlogins/content/components/login-list-item.mjs
source-hash: 32c8dec98f081c59ce3303c8cd62c28e4f32512d
lines: 35

## <module>
- 役割: (未記入)

## LoginListItemFactory.create()
- 位置: L11-21
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LoginListItemFactory.update()`, `loginListItem.classList.add()`
- 条件付き依存: `if (!login.guid)` → `newListItem.classList.add()`
- 参照: `login.guid`

## LoginListItemFactory.update()
- 位置: L23-33
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `listItem.dataset.guid`, `listItem.favicon`, `listItem.id`, `listItem.title`, `listItem.username`, `login.guid`, `login.origin`, `login.title`, `login.username`
