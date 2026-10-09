# nsISecondaryTileListener (browser/components/shell/nsISecondaryTile.idl)

source: browser/components/shell/nsISecondaryTile.idl
source-hash: 0048e3c40e83b4d01645e370e569cd02db7ab575

- 継承: nsISupports
- 役割: Provides functions that are called (on the main thread) when the secondary
- 実装: (未記入)
- 使っているJS: [`browser/components/shell/ShellService.sys.mjs`](ShellService.sys.mjs.md)

## メソッド / 属性
- `void succeeded(boolean accepted)`: (未記入)
- `void failed(long aHresult)`: (未記入)

# nsISecondaryTileService (browser/components/shell/nsISecondaryTile.idl)

source: browser/components/shell/nsISecondaryTile.idl
source-hash: 0048e3c40e83b4d01645e370e569cd02db7ab575

- 継承: nsISupports
- 役割: Provides an interface to Windows' secondary tile APIs.
- 実装: (未記入)
- 使っているJS: [`browser/components/shell/ShellService.sys.mjs`](ShellService.sys.mjs.md)

## メソッド / 属性
- `void requestCreateAndPin(ACString aTileId, AString aName, ACString aIconPath, Array<ACString> aArguments, nsISecondaryTileListener aListener)`: Requests to create a new secondary tile and pin it to the taskbar.
- `void requestDelete(ACString aTileId, nsISecondaryTileListener aListener)`: Requests to delete a secondary tile from the taskbar.
