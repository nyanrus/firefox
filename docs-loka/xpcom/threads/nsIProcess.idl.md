# nsIProcess (xpcom/threads/nsIProcess.idl)

source: xpcom/threads/nsIProcess.idl
source-hash: c15ded7a2fdd7810db883e9300ee7e2442a07961

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/profiles/SelectableProfileService.sys.mjs`](../../browser/components/profiles/SelectableProfileService.sys.mjs.md), [`browser/tools/mozscreenshots/mozscreenshots/extension/Screenshot.sys.mjs`](../../browser/tools/mozscreenshots/mozscreenshots/extension/Screenshot.sys.mjs.md), [`browser/tools/mozscreenshots/mozscreenshots/extension/TestRunner.sys.mjs`](../../browser/tools/mozscreenshots/mozscreenshots/extension/TestRunner.sys.mjs.md)

## メソッド / 属性
- `void init(nsIFile executable)`: Initialises the process with an executable to be run. Call the run method
- `void kill()`: Kills the running process. After exiting the process will either have
- `void run(boolean blocking, string args, unsigned long count)`: Executes the file this object was initialized with
- `void runAsync(string args, unsigned long count, nsIObserver observer, boolean holdWeak)`: Executes the file this object was initialized with optionally calling
- `void runw(boolean blocking, wstring args, unsigned long count)`: Executes the file this object was initialized with
- `void runwAsync(wstring args, unsigned long count, nsIObserver observer, boolean holdWeak)`: Executes the file this object was initialized with optionally calling
- `attribute boolean startHidden`: When set to true the process will not open a new window when started and
- `attribute boolean noShell`: When set to true the process will be launched directly without using the
- `readonly attribute unsigned long pid`: The process identifier of the currently running process. This will only
- `readonly attribute long exitValue`: The exit value of the process. This is only valid after the process has
- `readonly attribute boolean isRunning`: Returns whether the process is currently running or not.
