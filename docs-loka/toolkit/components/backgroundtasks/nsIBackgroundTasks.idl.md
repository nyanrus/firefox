# nsIBackgroundTasks (toolkit/components/backgroundtasks/nsIBackgroundTasks.idl)

source: toolkit/components/backgroundtasks/nsIBackgroundTasks.idl
source-hash: 96054b236c29aab65ff3c8e181b1ae55d86c9a99

- 継承: nsISupports
- 役割: Determine if this instance is running background task mode and
- 実装: (未記入)
- 使っているJS: [`browser/components/asrouter/modules/ASRouterTargeting.sys.mjs`](../../../browser/components/asrouter/modules/ASRouterTargeting.sys.mjs.md), [`browser/components/shell/ShellService.sys.mjs`](../../../browser/components/shell/ShellService.sys.mjs.md)

## メソッド / 属性
- `readonly attribute boolean isBackgroundTaskMode`: True if and only if this invocation is running in background task mode.
- `AString backgroundTaskName()`: A non-empty task name if this invocation is running in background
- `void overrideBackgroundTaskNameForTesting(AString taskName)`: Should only be used for testing.
