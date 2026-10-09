# nsIToolkitProfileService (toolkit/profile/nsIToolkitProfileService.idl)

source: toolkit/profile/nsIToolkitProfileService.idl
source-hash: 3dd5cdd94af54d15525d3f44abf954003f72ea60

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/backup/BackupService.sys.mjs`](../../browser/components/backup/BackupService.sys.mjs.md), [`browser/components/defaultlaunchonlogin/DefaultLaunchOnLogin.sys.mjs`](../../browser/components/defaultlaunchonlogin/DefaultLaunchOnLogin.sys.mjs.md), [`browser/components/migration/FirefoxProfileMigrator.sys.mjs`](../../browser/components/migration/FirefoxProfileMigrator.sys.mjs.md), [`browser/components/preferences/main.js`](../../browser/components/preferences/main.js.md), [`browser/components/profiles/content/profile-selector.mjs`](../../browser/components/profiles/content/profile-selector.mjs.md), [`browser/components/shell/StartupOSIntegration.sys.mjs`](../../browser/components/shell/StartupOSIntegration.sys.mjs.md)

## メソッド / 属性
- `readonly attribute boolean isListOutdated`: Tests whether the profile lists on disk have changed since they were
- `readonly attribute boolean isFirstRun`: True if no default profile was assigned to this install at startup,
- `attribute boolean startWithLastProfile`: (未記入)
- `readonly attribute nsISimpleEnumerator profiles`: (未記入)
- `readonly attribute nsIToolkitProfile currentProfile`: The current named nsIToolkitProfile selected at startup. This may be null
- `attribute nsIToolkitProfile defaultProfile`: The default profile for this build.
- `boolean selectStartupProfile(Array<ACString> aArgv, boolean aIsResetting, AUTF8String aUpdateChannel, AUTF8String aLegacyInstallHash, nsIFile aRootDir, nsIFile aLocalDir, nsIToolkitProfile aProfile)`: Selects or creates a profile to use based on the profiles database, any
- `nsIToolkitProfile getProfileByName(AUTF8String aName)`: Get a profile by name. This is mainly for use by the -P
- `nsIToolkitProfile getProfileByDir(nsIFile aRootDir, nsIFile aLocalDir)`: Get a profile by directory. Finds a profile with the matching root directory
- `nsIToolkitProfile createProfile(nsIFile aRootDir, AUTF8String aName, AUTF8String aSource)`: Create a new profile.
- `nsIToolkitProfile createUniqueProfile(nsIFile aRootDir, AUTF8String aNamePrefix, AUTF8String aSource)`: Create a new profile with a unique name.
- `AUTF8String getProfileDescriptor(nsIFile aRootDir, boolean aIsRelative)`: Gets the profile root directory descriptor for storing in profiles.ini or
- `nsIFile getLocalDirFromRootDir(nsIFile aRootDir)`: Return the local directory for a given profile root directory.
- `readonly attribute unsigned long profileCount`: Returns the number of profiles.
- `void flush()`: Flush the profiles list file. This will fail with
- `Promise asyncFlush()`: Flushes the profiles list file on a background thread after acquiring the
- `Promise asyncFlushCurrentProfile()`: Flushes the mutable data about the current profile to disk on a
- `Promise removeProfileFilesByPath(nsIFile aRootDir, nsIFile aLocalDir, unsigned long aTimeout)`: Removes profile directories from disk. Will wait for up to aTimeout
