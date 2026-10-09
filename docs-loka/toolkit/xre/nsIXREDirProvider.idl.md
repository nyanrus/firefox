# nsIXREDirProvider (toolkit/xre/nsIXREDirProvider.idl)

source: toolkit/xre/nsIXREDirProvider.idl
source-hash: ce599a83bcdf1b2779ea7fdc858920c4aa427c73

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/installerprefs/InstallerPrefs.sys.mjs`](../../browser/components/installerprefs/InstallerPrefs.sys.mjs.md), [`browser/components/protocolhandler/WebProtocolHandlerRegistrar.sys.mjs`](../../browser/components/protocolhandler/WebProtocolHandlerRegistrar.sys.mjs.md), [`browser/components/shell/ShellService.sys.mjs`](../../browser/components/shell/ShellService.sys.mjs.md)

## メソッド / 属性
- `void setUserDataDirectory(nsIFile aFile, boolean aLocal)`: Only intended to be used from xpcshell tests. Allows setting the local
- `AString getInstallHash()`: Gets the hash for the current installation directory.
