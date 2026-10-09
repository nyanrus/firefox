# nsIHangReport (dom/ipc/nsIHangReport.idl)

source: dom/ipc/nsIHangReport.idl
source-hash: 25c3f7993fccea7a0f5eb10049cbfbb338969039

- 継承: nsISupports
- 役割: When a content process hangs, Gecko notifies "process-hang-report" observers
- 実装: (未記入)
- 使っているJS: [`browser/modules/ProcessHangMonitor.sys.mjs`](../../browser/modules/ProcessHangMonitor.sys.mjs.md)

## メソッド / 属性
- `readonly attribute Element scriptBrowser`: (未記入)
- `readonly attribute ACString scriptFileName`: (未記入)
- `readonly attribute double hangDuration`: (未記入)
- `readonly attribute AString addonId`: (未記入)
- `readonly attribute unsigned long long childID`: (未記入)
- `void userCanceled()`: (未記入)
- `void terminateScript()`: (未記入)
- `void beginStartingDebugger()`: (未記入)
- `void endStartingDebugger()`: (未記入)
- `boolean isReportForBrowserOrChildren(FrameLoader aFrameLoader)`: (未記入)
