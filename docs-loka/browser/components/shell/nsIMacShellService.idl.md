# nsIMacShellService (browser/components/shell/nsIMacShellService.idl)

source: browser/components/shell/nsIMacShellService.idl
source-hash: 0a275142177f3457e8a0159014010457001c1e4e

- 継承: nsIShellService
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/shell/ShellService.sys.mjs`](ShellService.sys.mjs.md), [`browser/components/shell/content/setDesktopBackground.js`](content/setDesktopBackground.js.md)

## メソッド / 属性
- `void showDesktopPreferences()`: Opens the desktop preferences, e.g. for after setting the background.
- `void showSecurityPreferences(ACString aPaneID)`: @param aPaneID used by macOS to identify the pane to open.
- `Array<Array<AString>> getAvailableApplicationsForProtocol(ACString protocol)`: (未記入)
- `readonly attribute boolean canSetAsDefaultHandler`: Whether setting Firefox as the default handler for a file extension or
- `Promise setAsDefaultHandlerFor(AString aFileExtensionOrProtocol)`: Set Firefox as the default handler for the given file extension (like
- `boolean isDefaultHandlerFor(AString aFileExtensionOrProtocol)`: Whether Firefox is the current default handler for the given file
- `boolean isDefaultHandlerAWebBrowserFor(AString aFileExtensionOrProtocol)`: @return true if the application currently registered as the default
- `boolean enableLaunchOnLogin()`: (未記入)
- `boolean disableLaunchOnLogin()`: (未記入)
- `boolean getLaunchOnLoginEnabled()`: (未記入)
