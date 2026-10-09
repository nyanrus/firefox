# nsIUpdatePatch (toolkit/mozapps/update/nsIUpdateService.idl)

source: toolkit/mozapps/update/nsIUpdateService.idl
source-hash: 7dbd59c456bbac334a3279ff65902e5443420a67

- 継承: nsISupports
- 役割: An interface that describes an object representing a patch file that can
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute AString type`: The type of this patch:
- `readonly attribute AString URL`: The URL this patch was being downloaded from
- `attribute AString finalURL`: The final URL this patch was being downloaded from
- `readonly attribute unsigned long size`: The size of this file, in bytes.
- `attribute AString state`: The state of this patch
- `attribute long errorCode`: A numeric error code that conveys additional information about the state of
- `attribute boolean selected`: true if this patch is currently selected as the patch to be downloaded and
- `Element serialize(Document updates)`: Serializes this patch object into a DOM Element

# nsIUpdate (toolkit/mozapps/update/nsIUpdateService.idl)

source: toolkit/mozapps/update/nsIUpdateService.idl
source-hash: 7dbd59c456bbac334a3279ff65902e5443420a67

- 継承: nsISupports
- 役割: An interface that describes an object representing an available update to
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute AString type`: The type of update:
- `readonly attribute AString name`: The name of the update, or "<Application Name> <Update Version>"
- `readonly attribute AString displayVersion`: The string to display in the user interface for the version. If you want
- `readonly attribute AString appVersion`: The Application version of this update.
- `readonly attribute AString platformVersion`: The platform version of this update.
- `readonly attribute AString previousAppVersion`: The Application version prior to the application being updated.
- `readonly attribute AString buildID`: The Build ID of this update. Used to determine a particular build, down
- `readonly attribute AString detailsURL`: The URL to a page which offers details about the content of this
- `readonly attribute AString serviceURL`: The URL to the Update Service that supplied this update.
- `readonly attribute AString channel`: The channel used to retrieve this update from the Update Service.
- `readonly attribute boolean unsupported`: Whether the update is no longer supported on this system.
- `attribute long long promptWaitTime`: Allows overriding the default amount of time in seconds before prompting the
- `attribute boolean isCompleteUpdate`: Whether or not the update being downloaded is a complete replacement of
- `attribute long long installDate`: When the update was installed.
- `attribute AString statusText`: A message associated with this update, if any.
- `readonly attribute nsIUpdatePatch selectedPatch`: The currently selected patch for this update.
- `attribute AString state`: The state of the selected patch:
- `attribute long errorCode`: A numeric error code that conveys additional information about the state of
- `attribute boolean elevationFailure`: Whether an elevation failure has been encountered for this update.
- `readonly attribute unsigned long patchCount`: The number of patches supplied by this update.
- `nsIUpdatePatch getPatchAt(unsigned long index)`: Retrieves a patch.
- `Element serialize(Document updates)`: Serializes this update object into a DOM Element

# nsIUpdateCheckResult (toolkit/mozapps/update/nsIUpdateService.idl)

source: toolkit/mozapps/update/nsIUpdateService.idl
source-hash: 7dbd59c456bbac334a3279ff65902e5443420a67

- 継承: nsISupports
- 役割: An interface describing the result of an update check.
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute boolean checksAllowed`: True if update checks are allowed. otherwise false.
- `readonly attribute boolean succeeded`: True if the update check succeeded, otherwise false. Guaranteed to be false
- `readonly attribute jsval request`: The XMLHttpRequest handling the update check. Depending on exactly how the
- `readonly attribute Array<nsIUpdate> updates`: If `!checksAllowed`, this will always be an empty array.

# nsIUpdateCheck (toolkit/mozapps/update/nsIUpdateService.idl)

source: toolkit/mozapps/update/nsIUpdateService.idl
source-hash: 7dbd59c456bbac334a3279ff65902e5443420a67

- 継承: nsISupports
- 役割: An interface describing an update check that may still be in-progress or may
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute long id`: An id that represents a particular update check. Can be passed to
- `readonly attribute Promise result`: A promise that resolves to the results of the update check, which will be

# nsIUpdateCheckerInternal (toolkit/mozapps/update/nsIUpdateService.idl)

source: toolkit/mozapps/update/nsIUpdateService.idl
source-hash: 7dbd59c456bbac334a3279ff65902e5443420a67

- 継承: nsISupports
- 役割: An interface into the internals of the update checker. These should only be
- 実装: (未記入)

## メソッド / 属性
- `nsIUpdateCheck checkForUpdates(long checkType)`: This is identical to the corresponding function in `nsIUpdateChecker`, but

# nsIUpdateChecker (toolkit/mozapps/update/nsIUpdateService.idl)

source: toolkit/mozapps/update/nsIUpdateService.idl
source-hash: 7dbd59c456bbac334a3279ff65902e5443420a67

- 継承: nsISupports
- 役割: An interface describing an object that knows how to check for updates. It can
- 実装: (未記入)
- 使っているJS: [`browser/components/asrouter/modules/ASRouterTargeting.sys.mjs`](../../../browser/components/asrouter/modules/ASRouterTargeting.sys.mjs.md)

## メソッド / 属性
- `const long BACKGROUND_CHECK`: Enumerated constants. See the `checkType` parameter of `checkForUpdates`
- `const long FOREGROUND_CHECK`: (未記入)
- `nsIUpdateCheck checkForUpdates(long checkType)`: Checks for available updates.
- `Promise getUpdateURL(long checkType)`: Gets the update URL.
- `void stopCheck(long id)`: Ends a pending update check. Has no effect if the id is invalid or the
- `void stopAllChecks()`: Ends all pending update checks.
- `readonly attribute nsIUpdateCheckerInternal internal`: See nsIUpdateCheckerInternal for details.

# nsIApplicationUpdateServiceInternal (toolkit/mozapps/update/nsIUpdateService.idl)

source: toolkit/mozapps/update/nsIUpdateService.idl
source-hash: 7dbd59c456bbac334a3279ff65902e5443420a67

- 継承: nsISupports
- 役割: An interface into the internals of the update service. These should only be
- 実装: (未記入)

## メソッド / 属性
- `Promise init(boolean force)`: To initialize the update system, use the init method on
- `Promise downloadUpdate(nsIUpdate update)`: These are identical to the corresponding functions in
- `Promise stopDownload()`: (未記入)

# nsIApplicationUpdateService (toolkit/mozapps/update/nsIUpdateService.idl)

source: toolkit/mozapps/update/nsIUpdateService.idl
source-hash: 7dbd59c456bbac334a3279ff65902e5443420a67

- 継承: nsISupports
- 役割: An interface describing a global application service that handles performing
- 実装: (未記入)
- 使っているJS: [`browser/base/content/aboutDialog-appUpdater.js`](../../../browser/base/content/aboutDialog-appUpdater.js.md), [`browser/components/BrowserGlue.sys.mjs`](../../../browser/components/BrowserGlue.sys.mjs.md), [`browser/components/asrouter/modules/ASRouterTargeting.sys.mjs`](../../../browser/components/asrouter/modules/ASRouterTargeting.sys.mjs.md), [`browser/components/preferences/config/about-firefox.mjs`](../../../browser/components/preferences/config/about-firefox.mjs.md), [`browser/components/preferences/preferences.js`](../../../browser/components/preferences/preferences.js.md), [`browser/components/urlbar/QuickActionsLoaderDefault.sys.mjs`](../../../browser/components/urlbar/QuickActionsLoaderDefault.sys.mjs.md)

## メソッド / 属性
- `Promise init()`: Initializes the update system. It is typically not necessary to call this
- `Promise checkForBackgroundUpdates()`: Checks for available updates in the background using the listener provided
- `Promise selectUpdate(Array<nsIUpdate> updates)`: Selects the best update to install from a list of available updates.
- `void addDownloadListener(nsIRequestObserver listener)`: Adds a listener that receives progress and state information about the
- `void removeDownloadListener(nsIRequestObserver listener)`: Removes a listener that is receiving progress and state information
- `const long DOWNLOAD_SUCCESS`: The below are the possible return values for `downloadUpdate()`.
- `const long DOWNLOAD_FAILURE_CANNOT_RESUME_IN_BACKGROUND`: (未記入)
- `const long DOWNLOAD_FAILURE_GENERIC`: (未記入)
- `const long DOWNLOAD_FAILURE_CANNOT_WRITE_STATE`: (未記入)
- `Promise downloadUpdate(nsIUpdate update)`: Starts downloading the update passed. Once the update is downloaded, it
- `Promise onCheckComplete(nsIUpdateCheckResult result)`: This is the function called internally by the Application Update Service
- `Promise stopDownload()`: Stop the active update download process. This is the equivalent of
- `readonly attribute boolean disabled`: There are a few things that can disable the Firefox updater at runtime
- `readonly attribute boolean canUsuallyCheckForUpdates`: Whether or not the Update Service can usually check for updates. This is a
- `readonly attribute boolean canCheckForUpdates`: Whether or not the Update Service can check for updates right now. This is
- `readonly attribute boolean elevationRequired`: Whether or not the installation requires elevation. Currently only
- `readonly attribute boolean canUsuallyApplyUpdates`: Whether or not the Update Service can usually download and install updates.
- `readonly attribute boolean canApplyUpdates`: Whether or not the Update Service can download and install updates right now.
- `readonly attribute boolean isOtherInstanceHandlingUpdates`: Whether or not a different instance is handling updates of this
- `readonly attribute boolean canUsuallyStageUpdates`: Whether the Update Service is usually able to stage updates.
- `readonly attribute boolean canStageUpdates`: Whether the Update Service is able to stage updates right now.  On all
- `readonly attribute boolean canUsuallyUseBits`: On Windows, whether the Update Service can usually use BITS.
- `readonly attribute boolean canUseBits`: On Windows, whether the Update Service can use BITS right now.  This
- `readonly attribute boolean manualUpdateOnly`: Indicates whether or not the enterprise policy that allows only manual
- `readonly attribute boolean isAppBaseDirWritable`: Determines if the base directory is writable. If not, we assume that
- `attribute boolean onlyDownloadUpdatesThisSession`: This can be set to true to prevent updates being processed beyond starting
- `const long STATE_IDLE`: Enumerated constants describing the update states that the updater can be
- `const long STATE_DOWNLOADING`: (未記入)
- `const long STATE_STAGING`: (未記入)
- `const long STATE_PENDING`: (未記入)
- `const long STATE_SWAP`: (未記入)
- `const long STATE_DOWNLOAD_FAILED`: (未記入)
- `AString getStateName(long state)`: Gets a string describing the state (mostly intended to be make console
- `readonly attribute long currentState`: The current state of the application updater. Returns one of the enumerated
- `readonly attribute Promise stateTransition`: A Promise that resolves immediately after `currentState` changes.
- `readonly attribute nsIApplicationUpdateServiceInternal internal`: See nsIApplicationUpdateServiceInternal for details.

# nsIUpdateProcessor (toolkit/mozapps/update/nsIUpdateService.idl)

source: toolkit/mozapps/update/nsIUpdateService.idl
source-hash: 7dbd59c456bbac334a3279ff65902e5443420a67

- 継承: nsISupports
- 役割: An interface describing a component which handles the job of processing
- 実装: (未記入)

## メソッド / 属性
- `void processUpdate()`: Stages an update while the application is running.
- `boolean getServiceRegKeyExists()`: The installer writes an installation-specific registry key if the
- `long attemptAutomaticApplicationRestartWithLaunchArgs(Array<AString> argvExtra)`: Attempts to restart the application manually on program exit with the same
- `void waitForProcessExit(unsigned long pid, unsigned long timeoutMS)`: This function is meant to be used in conjunction with

# nsIUpdateSyncManager (toolkit/mozapps/update/nsIUpdateService.idl)

source: toolkit/mozapps/update/nsIUpdateService.idl
source-hash: 7dbd59c456bbac334a3279ff65902e5443420a67

- 継承: nsISupports
- 役割: Upon creation, which should happen early during startup, the sync manager
- 実装: (未記入)

## メソッド / 属性
- `boolean isOtherInstanceRunning()`: Returns whether another instance of this application is running.
- `void resetLock(nsIFile anAppFile)`: Should only be used for testing.
- `AString getUpdateLockFilePath()`: Returns the path to the lock file used for update synchronization.

# nsIUpdateMutex (toolkit/mozapps/update/nsIUpdateService.idl)

source: toolkit/mozapps/update/nsIUpdateService.idl
source-hash: 7dbd59c456bbac334a3279ff65902e5443420a67

- 継承: nsISupports
- 役割: An object interface suitable for acquiring the update mutex for the current
- 実装: (未記入)

## メソッド / 属性
- `boolean isLocked()`: Checks the current acquisition status for the current object.
- `boolean tryLock()`: Attempts to acquire the update mutex for the current installation path.
- `void unlock()`: Manually releases the update mutex for the current installation path. Does

# nsIUpdateManagerInternal (toolkit/mozapps/update/nsIUpdateService.idl)

source: toolkit/mozapps/update/nsIUpdateService.idl
source-hash: 7dbd59c456bbac334a3279ff65902e5443420a67

- 継承: nsISupports
- 役割: An interface into the internals of the update manager. These should only be
- 実装: (未記入)

## メソッド / 属性
- `Promise reload(boolean skipFiles)`: Reloads the update manager's data.
- `Array<nsIUpdate> getHistory()`: These are identical to the functions with the same name in
- `void addUpdateToHistory(nsIUpdate update)`: (未記入)
- `attribute nsIUpdate readyUpdate`: (未記入)
- `attribute nsIUpdate downloadingUpdate`: (未記入)
- `Promise refreshUpdateStatus()`: (未記入)

# nsIUpdateManager (toolkit/mozapps/update/nsIUpdateService.idl)

source: toolkit/mozapps/update/nsIUpdateService.idl
source-hash: 7dbd59c456bbac334a3279ff65902e5443420a67

- 継承: nsISupports
- 役割: An interface describing a global application service that maintains a list
- 実装: (未記入)
- 使っているJS: [`browser/components/BrowserContentHandler.sys.mjs`](../../../browser/components/BrowserContentHandler.sys.mjs.md), [`browser/components/preferences/config/about-firefox.mjs`](../../../browser/components/preferences/config/about-firefox.mjs.md), [`browser/modules/BackgroundTask_install.sys.mjs`](../../../browser/modules/BackgroundTask_install.sys.mjs.md), [`browser/modules/BackgroundTask_uninstall.sys.mjs`](../../../browser/modules/BackgroundTask_uninstall.sys.mjs.md)

## メソッド / 属性
- `Promise getHistory()`: @returns Promise<Array<nsIUpdate>>
- `Promise getReadyUpdate()`: Returns a Promise that resolves with the nsIUpdate that has been
- `Promise getDownloadingUpdate()`: Returns a Promise that resolves with the nsIUpdate that is currently
- `Promise updateInstalledAtStartup()`: Returns a Promise that resolves with the update that Firefox installed at the
- `Promise lastUpdateInstalled()`: Returns a Promise that resolves with the most recent update that has been installed,
- `Promise addUpdateToHistory(nsIUpdate update)`: Adds the specified update to the update history. The update history is
- `void saveUpdates()`: Saves all updates to disk.
- `Promise refreshUpdateStatus()`: Refresh the update status based on the information in update.status.
- `Promise elevationOptedIn()`: The user agreed to proceed with an elevated update and we are now
- `Promise cleanupDownloadingUpdate()`: These functions clean up and remove an active update without applying
- `Promise cleanupReadyUpdate()`: (未記入)
- `Promise cleanupActiveUpdates()`: (未記入)
- `Promise doInstallCleanup()`: Runs cleanup that ought to happen on a Firefox paveover install to
- `Promise doUninstallCleanup()`: Runs cleanup that ought to happen when Firefox is uninstalled to clean up
- `readonly attribute nsIUpdateManagerInternal internal`: See nsIUpdateManagerInternal for details.

# nsIApplicationUpdateServiceStub (toolkit/mozapps/update/nsIUpdateService.idl)

source: toolkit/mozapps/update/nsIUpdateService.idl
source-hash: 7dbd59c456bbac334a3279ff65902e5443420a67

- 継承: nsISupports
- 役割: A lightweight interface that we can load early in startup that gives us very
- 実装: (未記入)
- 使っているJS: [`browser/components/BrowserGlue.sys.mjs`](../../../browser/components/BrowserGlue.sys.mjs.md)

## メソッド / 属性
- `Promise init()`: This does the standard initialization of the update service stub. The
- `Promise initUpdate()`: This is identical to `nsIApplicationUpdateService.init()`.
- `readonly attribute boolean updateDisabled`: This is identical to `nsIApplicationUpdateService.disabled`.
- `readonly attribute boolean updateDisabledForTesting`: This will be `true` if update is disabled specifically because we are
