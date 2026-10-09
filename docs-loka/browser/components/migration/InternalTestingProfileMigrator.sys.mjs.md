# browser/components/migration/InternalTestingProfileMigrator.sys.mjs

source: browser/components/migration/InternalTestingProfileMigrator.sys.mjs
source-hash: 0158f185d8b4a81df6acbbd0856d73fa27e16f1e
lines: 78

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## InternalTestingProfileMigrator.key()
- 位置: L19-21
- 役割: (未記入)
- 触るとき: (未記入)

## InternalTestingProfileMigrator.displayNameL10nID()
- 位置: L23-25
- 役割: (未記入)
- 触るとき: (未記入)

## InternalTestingProfileMigrator.sourceID()
- 位置: L27-29
- 役割: (未記入)
- 触るとき: (未記入)

## InternalTestingProfileMigrator.getSourceProfiles()
- 位置: L31-33
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`
- 参照: `InternalTestingProfileMigrator.testProfile`

## InternalTestingProfileMigrator.getResources()
- 位置: L37-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.values()`, `Object.values(lazy.MigrationUtils.resourceTypes).map()`
- 参照: `InternalTestingProfileMigrator.testProfile.id`, `aProfile.id`, `lazy.MigrationUtils.resourceTypes`

## migrate()
- 位置: L49-59
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (type == lazy.MigrationUtils.resourceTypes.EXTENSIONS)` → `callback()`
- 条件付き依存: `if (!(type == lazy.MigrationUtils.resourceTypes.EXTENSIONS))` → `callback()`
- 参照: `MigrationWizardConstants.PROGRESS_VALUE.SUCCESS`, `lazy.MigrationUtils.resourceTypes.EXTENSIONS`

## InternalTestingProfileMigrator.flushResourceCache()
- 位置: L70-72
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this._resourcesByProfile`

## InternalTestingProfileMigrator.testProfile()
- 位置: L74-76
- 役割: (未記入)
- 触るとき: (未記入)
