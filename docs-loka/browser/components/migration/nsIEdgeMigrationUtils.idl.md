# nsIEdgeMigrationUtils (browser/components/migration/nsIEdgeMigrationUtils.idl)

source: browser/components/migration/nsIEdgeMigrationUtils.idl
source-hash: 8c15d002514c1013caf339be899abb04235a85d1

- 継承: nsISupports
- 役割: Utilities for migrating from legacy (non-Chromimum-based) Edge.
- 実装: (未記入)
- 使っているJS: [`browser/components/migration/ESEDBReader.sys.mjs`](ESEDBReader.sys.mjs.md)

## メソッド / 属性
- `Promise isDbLocked(nsIFile aFile)`: Determine if the Edge database is locked for writing.
