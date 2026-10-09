# nsIGNOMEShellService (browser/components/shell/nsIGNOMEShellService.idl)

source: browser/components/shell/nsIGNOMEShellService.idl
source-hash: 7f75f5cdd80478aeb69d7122bf8196318d09afea

- 継承: nsIShellService
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/shell/ShellService.sys.mjs`](ShellService.sys.mjs.md)

## メソッド / 属性
- `readonly attribute boolean canSetDesktopBackground`: Used to determine whether or not to offer "Set as desktop background"
- `boolean isDefaultForScheme(AUTF8String aScheme)`: Returns true if Firefox is set as the default handler for the scheme.
- `AUTF8String getGSettingsString(AUTF8String aScheme, AUTF8String aKey)`: (未記入)
- `void setGSettingsString(AUTF8String aScheme, AUTF8String aKey, AUTF8String aValue)`: (未記入)
- `ACString getArgv0()`: Gets the command name that was used to start the browser.
- `ACString getGlibPrgname()`: Gets the program name from GLib, which is used as the default window
- `nsIGNOMEShellService_DesktopEntryStatus getDesktopEntryStatus(AUTF8String aEntryId)`: Determines whether the named desktop entry exists and is visible,
- `Promise requestInstallDynamicLauncher(AUTF8String aEntryId, nsIINIParserWriter aDesktopEntry, mozIDOMWindowProxy aWindow)`: Uses the Dynamic Launcher portal to install a desktop entry for this user.
- `Promise requestUninstallDynamicLauncher(AUTF8String aEntryId)`: Uses the Dynamic Launcher portal to remove a desktop entry for this user.
