# nsIDefaultAgent (toolkit/mozapps/defaultagent/nsIDefaultAgent.idl)

source: toolkit/mozapps/defaultagent/nsIDefaultAgent.idl
source-hash: 92a9f4d8627819fa8ecc5c8f29c55937131f126c

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/protocolhandler/WebProtocolHandlerRegistrar.sys.mjs`](../../../browser/components/protocolhandler/WebProtocolHandlerRegistrar.sys.mjs.md), [`browser/components/shell/ShellService.sys.mjs`](../../../browser/components/shell/ShellService.sys.mjs.md)

## メソッド / 属性
- `void registerTask(AString aUniqueToken)`: Create a Windows scheduled task that will launch this binary with the
- `void updateTask(AString aUniqueToken)`: Update an existing task registration, without changing its schedule. This
- `void unregisterTask(AString aUniqueToken)`: Removes the previously created task. The unique token argument is required
- `void uninstall(AString aUniqueToken)`: Removes the previously created task, and also removes all registry entries
- `long long secondsSinceLastAppRun()`: Returns the number of seconds since the last time the app was launched. In
- `AString getDefaultBrowser()`: Returns a string for the default browser if known, binned to known browsers.
- `AString getReplacePreviousDefaultBrowser(AString aCurrentBrowser)`: Gets and replaces the previously found default browser from the registry.
- `AString getDefaultPdfHandler()`: Returns a string for the default PDF handler if known, binned to known
- `void sendPing(AString aCurrentBrowser, AString aPreviousBrowser, AString aPdfHandler, AString aNotificationShown, AString aNotificationAction, unsigned long daysSinceLastAppLaunch, AString aIsTaskbarPinned)`: Sends a Default Agent telemetry ping.
- `void setDefaultBrowserUserChoice(AString aAumid, Array<AString> aExtraFileExtensions)`: Set the default browser and optionally additional file extensions via the
- `Promise setDefaultBrowserUserChoiceAsync(AString aAumid, Array<AString> aExtraFileExtensions)`: Set the default browser and optionally additional file extensions via the
- `void setDefaultExtensionHandlersUserChoice(AString aAumid, Array<AString> aFileExtensions)`: Sets file extensions via the UserChoice registry keys.
- `boolean agentDisabled()`: Checks if the default agent has been disabled.
