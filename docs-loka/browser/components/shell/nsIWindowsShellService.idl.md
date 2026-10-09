# nsIInstallShortcutInfo (browser/components/shell/nsIWindowsShellService.idl)

source: browser/components/shell/nsIWindowsShellService.idl
source-hash: ee5c99c576790c21b7565588bf6ae38177eb643b

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute AString path`: (未記入)
- `readonly attribute AString location`: (未記入)

# nsIWindowsShellService (browser/components/shell/nsIWindowsShellService.idl)

source: browser/components/shell/nsIWindowsShellService.idl
source-hash: ee5c99c576790c21b7565588bf6ae38177eb643b

- 継承: nsIShellService
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/StartupTelemetry.sys.mjs`](../StartupTelemetry.sys.mjs.md), [`browser/components/profiles/SelectableProfile.sys.mjs`](../profiles/SelectableProfile.sys.mjs.md), [`browser/components/protocolhandler/WebProtocolHandlerRegistrar.sys.mjs`](../protocolhandler/WebProtocolHandlerRegistrar.sys.mjs.md), [`browser/components/shell/CustomIconManager.sys.mjs`](CustomIconManager.sys.mjs.md), [`browser/components/shell/ShellService.sys.mjs`](ShellService.sys.mjs.md), [`browser/components/shell/StartupOSIntegration.sys.mjs`](StartupOSIntegration.sys.mjs.md)

## メソッド / 属性
- `const long OPEN_WITH_SUPPRESS_OPEN`: (未記入)
- `const long OPEN_WITH_PROTOCOL_MESSAGING`: (未記入)
- `const long OPEN_WITH_OPEN_ONCE`: (未記入)
- `const long OPEN_WITH_SET_HANDLER`: (未記入)
- `const long OPEN_WITH_SET_HANDLER_WIN10`: (未記入)
- `Promise createShortcut(nsIFile aBinary, Array<AString> aArguments, AString aDescription, nsIFile aIconFile, unsigned short aIconIndex, AString aAppUserModelId, AString aShortcutFolder, AString aShortcutRelativePath)`: (未記入)
- `Promise deleteShortcut(AString aShortcutFolder, AString aShortcutRelativePath)`: (未記入)
- `Array<AString> getLaunchOnLoginShortcuts()`: (未記入)
- `Promise pinCurrentAppToStartMenu()`: (未記入)
- `Promise isCurrentAppPinnedToStartMenu()`: (未記入)
- `Promise enableLaunchOnLoginMSIX(AString aTaskId)`: (未記入)
- `Promise disableLaunchOnLoginMSIX(AString aTaskId)`: (未記入)
- `Promise getLaunchOnLoginEnabledMSIX(AString aTaskId)`: (未記入)
- `Promise pinCurrentAppToTaskbar(boolean aPrivateBrowsing, boolean aFireAndForget)`: (未記入)
- `void canPinToTaskbar()`: (未記入)
- `Promise isCurrentAppPinnedToTaskbar(AString aumid)`: (未記入)
- `Promise pinShortcutToTaskbar(AString aAppUserModelId, AString aShortcutFolder, AString aShortcutRelativePath)`: (未記入)
- `void unpinShortcutFromTaskbar(AString aShortcutFolder, AString aShortcutRelativePath)`: (未記入)
- `void launchSetDefaultAppPicker(AString aTarget, long aFlags)`: (未記入)
- `void launchModernSettingsDialogDefaultApps()`: (未記入)
- `AString classifyShortcut(AString aPath)`: (未記入)
- `Promise hasPinnableShortcut(AString aAUMID, boolean aPrivateBrowsing)`: (未記入)
- `boolean canSetDefaultBrowserUserChoice()`: (未記入)
- `boolean checkAllProgIDsExist()`: (未記入)
- `boolean checkBrowserUserChoiceHashes()`: (未記入)
- `boolean isUserChoiceProtectionDriverRunning()`: (未記入)
- `boolean canRenameUserChoiceAssociationKey(AString aAssociation)`: (未記入)
- `AString checkCurrentProcessAUMIDForTesting()`: (未記入)
- `boolean isDefaultHandlerFor(AString aFileExtensionOrProtocol)`: (未記入)
- `AString queryCurrentDefaultHandlerFor(AString aFileExtensionOrProtocol)`: (未記入)
- `Promise setShortcutsIcon(Array<AString> aShortcutPaths, AString aIconPath, unsigned short aIconResourceId)`: (未記入)
- `Promise enumerateInstallShortcuts(AString aAppUserModelId)`: (未記入)
