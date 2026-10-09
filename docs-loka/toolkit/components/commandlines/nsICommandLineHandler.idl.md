# nsICommandLineHandler (toolkit/components/commandlines/nsICommandLineHandler.idl)

source: toolkit/components/commandlines/nsICommandLineHandler.idl
source-hash: 7868af5ef4f995a7378554691061739a24d2f061

- 継承: nsISupports
- 役割: Handles arguments on the command line of an XUL application.
- 実装: (未記入)
- 使っているJS: [`browser/components/profiles/SelectableProfileService.sys.mjs`](../../../browser/components/profiles/SelectableProfileService.sys.mjs.md), [`browser/components/shell/WindowsSetDefaultAppCmdHandler.sys.mjs`](../../../browser/components/shell/WindowsSetDefaultAppCmdHandler.sys.mjs.md), [`browser/components/taskbartabs/TaskbarTabsCmd.sys.mjs`](../../../browser/components/taskbartabs/TaskbarTabsCmd.sys.mjs.md)

## メソッド / 属性
- `void handle(nsICommandLine aCommandLine)`: Process a command line. If this handler finds arguments that it
- `readonly attribute AUTF8String helpInfo`: When the app is launched with the --help argument, this attribute
