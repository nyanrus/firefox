# browser/components/migration/FileMigrators.sys.mjs

source: browser/components/migration/FileMigrators.sys.mjs
source-hash: dd346e8aed2e59f539bf4d0b570effdb343bfe87
lines: 356

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`

## FileMigratorBase.key()
- 位置: L35-37
- 役割: (未記入)
- 触るとき: (未記入)

## FileMigratorBase.displayNameL10nID()
- 位置: L45-47
- 役割: (未記入)
- 触るとき: (未記入)

## FileMigratorBase.brandImage()
- 位置: L56-58
- 役割: (未記入)
- 触るとき: (未記入)

## FileMigratorBase.enabled()
- 位置: L66-68
- 役割: (未記入)
- 触るとき: (未記入)

## FileMigratorBase.progressHeaderL10nID()
- 位置: L77-79
- 役割: (未記入)
- 触るとき: (未記入)

## FileMigratorBase.successHeaderL10nID()
- 位置: L88-90
- 役割: (未記入)
- 触るとき: (未記入)

## FileMigratorBase.getFilePickerConfig()
- 位置: async L118-120
- 役割: (未記入)
- 触るとき: (未記入)

## FileMigratorBase.displayedResourceTypes()
- 位置: L132-134
- 役割: (未記入)
- 触るとき: (未記入)

## FileMigratorBase.migrate()
- 位置: async L144-146
- 役割: (未記入)
- 触るとき: (未記入)

## PasswordFileMigrator.key()
- 位置: L155-157
- 役割: (未記入)
- 触るとき: (未記入)

## PasswordFileMigrator.displayNameL10nID()
- 位置: L159-161
- 役割: (未記入)
- 触るとき: (未記入)

## PasswordFileMigrator.brandImage()
- 位置: L163-165
- 役割: (未記入)
- 触るとき: (未記入)

## PasswordFileMigrator.enabled()
- 位置: L167-169
- 役割: (未記入)
- 触るとき: (未記入)

## PasswordFileMigrator.displayedResourceTypes()
- 位置: L171-176
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.MigrationWizardConstants.DISPLAYED_FILE_RESOURCE_TYPES .PASSWORDS_FROM_FILE`

## PasswordFileMigrator.progressHeaderL10nID()
- 位置: L178-180
- 役割: (未記入)
- 触るとき: (未記入)

## PasswordFileMigrator.successHeaderL10nID()
- 位置: L182-184
- 役割: (未記入)
- 触るとき: (未記入)

## PasswordFileMigrator.getFilePickerConfig()
- 位置: async L186-207
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gFluentStrings.formatValues()`

## PasswordFileMigrator.migrate()
- 位置: async L209-253
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `console.error()`, `lazy.LoginCSVImport.importFromCSV()`, `lazy.gFluentStrings.formatValue()`, `lazy.gFluentStrings.formatValues()`
- 参照: `entry.result`, `lazy.MigrationWizardConstants.DISPLAYED_FILE_RESOURCE_TYPES .PASSWORDS_NEW`, `lazy.MigrationWizardConstants.DISPLAYED_FILE_RESOURCE_TYPES .PASSWORDS_UPDATED`
- XPCOM: `Services.prefs`

## BookmarksFileMigrator.key()
- 位置: L263-265
- 役割: (未記入)
- 触るとき: (未記入)

## BookmarksFileMigrator.displayNameL10nID()
- 位置: L267-269
- 役割: (未記入)
- 触るとき: (未記入)

## BookmarksFileMigrator.brandImage()
- 位置: L271-273
- 役割: (未記入)
- 触るとき: (未記入)

## BookmarksFileMigrator.enabled()
- 位置: L275-280
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## BookmarksFileMigrator.displayedResourceTypes()
- 位置: L282-287
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `lazy.MigrationWizardConstants.DISPLAYED_FILE_RESOURCE_TYPES .BOOKMARKS_FROM_FILE`

## BookmarksFileMigrator.progressHeaderL10nID()
- 位置: L289-291
- 役割: (未記入)
- 触るとき: (未記入)

## BookmarksFileMigrator.successHeaderL10nID()
- 位置: L293-295
- 役割: (未記入)
- 触るとき: (未記入)

## BookmarksFileMigrator.getFilePickerConfig()
- 位置: async L297-318
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.gFluentStrings.formatValues()`

## BookmarksFileMigrator.migrate()
- 位置: async L320-354
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.error()`, `filePath.toLowerCase()`, `lazy.gFluentStrings.formatValue()`, `pathCheck.endsWith()`
- 条件付き依存: `if (pathCheck.endsWith("html"))` → `lazy.BookmarkHTMLUtils.importFromFile()`
- 条件付き依存: `if (!(pathCheck.endsWith("html")))` → `pathCheck.endsWith()`
- 条件付き依存: `if (pathCheck.endsWith("json") || pathCheck.endsWith("jsonlz4"))` → `lazy.BookmarkJSONUtils.importFromFile()`
- 参照: `lazy.MigrationWizardConstants.DISPLAYED_FILE_RESOURCE_TYPES .BOOKMARKS_FROM_FILE`
