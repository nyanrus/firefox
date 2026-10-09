# browser/components/aiwindow/ui/modules/AITabMigrations.sys.mjs

source: browser/components/aiwindow/ui/modules/AITabMigrations.sys.mjs
source-hash: acf1eb5949d27d6a5fad27a1f9da0f2368eabdf0
lines: 66

## <module>
- 役割: AI タブ用 DB のスキーマを版ごとに上げる移行処理の配列を定義する
- 呼び出し先: `columns.some()`, `connection.execute()`, `row.getResultByName()`
