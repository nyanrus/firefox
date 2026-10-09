# nsIShellService (browser/components/shell/nsIShellService.idl)

source: browser/components/shell/nsIShellService.idl
source-hash: a799120521b9ed1e20229b88364f7fa26dfe62ad

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/shell/ShellService.sys.mjs`](ShellService.sys.mjs.md), [`browser/components/shell/content/setDesktopBackground.js`](content/setDesktopBackground.js.md)

## メソッド / 属性
- `boolean isDefaultBrowser(boolean aForAllTypes)`: Determines whether or not Firefox is the "Default Browser."
- `Promise isDefaultBrowserAsync(boolean aForAllTypes)`: Asynchronously determines whether or not Firefox is the "Default Browser."
- `void setDefaultBrowser(boolean aForAllUsers)`: Registers Firefox as the "Default Browser."
- `const long BACKGROUND_TILE`: Flags for positioning/sizing of the Desktop Background image.
- `const long BACKGROUND_STRETCH`: (未記入)
- `const long BACKGROUND_CENTER`: (未記入)
- `const long BACKGROUND_FILL`: (未記入)
- `const long BACKGROUND_FIT`: (未記入)
- `const long BACKGROUND_SPAN`: (未記入)
- `void setDesktopBackground(Element aElement, long aPosition, ACString aImageName)`: Sets the desktop background image using either the HTML <IMG>
- `attribute unsigned long desktopBackgroundColor`: The desktop background color, visible when no background image is
