# nsIAppStartup (toolkit/components/startup/public/nsIAppStartup.idl)

source: toolkit/components/startup/public/nsIAppStartup.idl
source-hash: fbe4be69471e63d033227507273593a2ba53a6d5

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/base/content/aboutDialog-appUpdater.js`](../../../../browser/base/content/aboutDialog-appUpdater.js.md), [`browser/base/content/aboutRestartRequired.mjs`](../../../../browser/base/content/aboutRestartRequired.mjs.md), [`browser/base/content/browser-development-helpers.js`](../../../../browser/base/content/browser-development-helpers.js.md), [`browser/base/content/browser.js`](../../../../browser/base/content/browser.js.md), [`browser/components/BrowserGlue.sys.mjs`](../../../../browser/components/BrowserGlue.sys.mjs.md), [`browser/components/aiwindow/models/agents/MonitorAgent.sys.mjs`](../../../../browser/components/aiwindow/models/agents/MonitorAgent.sys.mjs.md), [`browser/components/backup/BackupService.sys.mjs`](../../../../browser/components/backup/BackupService.sys.mjs.md), [`browser/components/newtab/AboutHomeStartupCache.sys.mjs`](../../../../browser/components/newtab/AboutHomeStartupCache.sys.mjs.md), [`browser/components/newtab/AboutNewTabResourceMapping.sys.mjs`](../../../../browser/components/newtab/AboutNewTabResourceMapping.sys.mjs.md), [`browser/components/preferences/config/firefoxLabs.mjs`](../../../../browser/components/preferences/config/firefoxLabs.mjs.md), [`browser/components/preferences/config/privacy.mjs`](../../../../browser/components/preferences/config/privacy.mjs.md), [`browser/components/profiles/ProfilesParent.sys.mjs`](../../../../browser/components/profiles/ProfilesParent.sys.mjs.md), [`browser/components/shell/HeadlessShell.sys.mjs`](../../../../browser/components/shell/HeadlessShell.sys.mjs.md), [`browser/components/urlbar/QuickActionsLoaderDefault.sys.mjs`](../../../../browser/components/urlbar/QuickActionsLoaderDefault.sys.mjs.md), [`browser/components/urlbar/UrlbarProviderInterventions.sys.mjs`](../../../../browser/components/urlbar/UrlbarProviderInterventions.sys.mjs.md), [`browser/modules/ContentCrashHandlers.sys.mjs`](../../../../browser/modules/ContentCrashHandlers.sys.mjs.md)

## メソッド / 属性
- `void createHiddenWindow()`: Create the hidden window.
- `void destroyHiddenWindow()`: Destroys the hidden window. This will have no effect if the hidden window
- `void run()`: Runs an application event loop: normally the main event pump which
- `void enterLastWindowClosingSurvivalArea()`: There are situations where all application windows will be
- `void exitLastWindowClosingSurvivalArea()`: (未記入)
- `readonly attribute boolean automaticSafeModeNecessary`: Startup Crash Detection
- `void restartInSafeMode(uint32_t aQuitMode)`: Restart the application in safe mode
- `void createInstanceWithProfile(nsIToolkitProfile aProfile, Array<AString> aArgs)`: Run a new instance of this app with a specified profile
- `boolean trackStartupCrashBegin()`: If the last startup crashed then increment a counter.
- `void trackStartupCrashEnd()`: We have succesfully started without crashing. Clear flags that were
- `const uint32_t eConsiderQuit`: The following flags may be passed as the aMode parameter to the quit
- `const uint32_t eAttemptQuit`: Try to close all windows, then quit if successful.
- `const uint32_t eForceQuit`: Quit, damnit!
- `const uint32_t eRestart`: Restart the application after quitting.  The application will be
- `const uint32_t eSilently`: Only valid when combined with eRestart. Only relevant on macOS.
- `void quit(uint32_t aMode, int32_t aExitCode)`: Exit the event loop, and shut down the app.
- `void advanceShutdownPhase(nsIAppStartup_IDLShutdownPhase aPhase)`: Wrapper for shutdown notifications that informs the terminator before
- `void setImpendingShutdown()`: Set the AppShutdown::IsShutdownImpending() flag without advancing the
- `boolean isInOrBeyondShutdownPhase(nsIAppStartup_IDLShutdownPhase aPhase)`: Check if we entered or passed a specific shutdown phase.
- `void collectShutdownHangAnnotations()`: Refresh the shutdown-hang crash annotations just before a deliberate
- `readonly attribute boolean shuttingDown`: True if the application is in the process of shutting down.
- `readonly attribute boolean attemptingQuit`: True if the application is attempting to quit (Quit has been called). This
- `readonly attribute boolean startingUp`: True if the application is in the process of starting up.
- `void doneStartingUp()`: Mark the startup as completed.
- `readonly attribute boolean restarting`: True if the application is being restarted
- `readonly attribute boolean wasRestarted`: True if this is the startup following restart, i.e. if the application
- `readonly attribute boolean wasSilentlyStarted`: True if this is the startup following a silent restart, i.e. if the
- `readonly attribute int64_t secondsSinceLastOSRestart`: The number of seconds since the OS was last rebooted
- `readonly attribute boolean showedPreXULSkeletonUI`: Whether or not we showed the startup skeleton UI.
- `jsval getStartupInfo()`: Returns an object with main, process, firstPaint, sessionRestored properties.
