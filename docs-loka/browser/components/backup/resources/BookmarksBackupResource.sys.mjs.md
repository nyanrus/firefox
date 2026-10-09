# browser/components/backup/resources/BookmarksBackupResource.sys.mjs

source: browser/components/backup/resources/BookmarksBackupResource.sys.mjs
source-hash: 4a5126085d6e68ab4989ad5e7bb7e85de5333c02
lines: 83

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## BookmarksBackupResource.key()
- 位置: L19-21
- 役割: (未記入)
- 触るとき: (未記入)

## BookmarksBackupResource.requiresEncryption()
- 位置: L23-25
- 役割: (未記入)
- 触るとき: (未記入)

## BookmarksBackupResource.canBackupResource()
- 位置: L27-35
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `BackupResource.backingUpPlaces`

## BookmarksBackupResource.priority()
- 位置: L37-39
- 役割: (未記入)
- 触るとき: (未記入)

## BookmarksBackupResource.backup()
- 位置: async L41-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`, `lazy.BookmarkJSONUtils.exportToFile()`
- 参照: `PathUtils.profileDir`

## BookmarksBackupResource.recover()
- 位置: async L56-66
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `PathUtils.join()`

## BookmarksBackupResource.postRecovery()
- 位置: async L68-77
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (postRecoveryEntry?.bookmarksBackupPath)` → `lazy.BookmarkJSONUtils.importFromFile()`
- 参照: `postRecoveryEntry.bookmarksBackupPath`, `postRecoveryEntry?.bookmarksBackupPath`

## BookmarksBackupResource.measure()
- 位置: async L79-81
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `PathUtils.profileDir`
