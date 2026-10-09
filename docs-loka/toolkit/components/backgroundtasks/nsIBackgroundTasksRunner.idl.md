# nsIBackgroundTasksRunner (toolkit/components/backgroundtasks/nsIBackgroundTasksRunner.idl)

source: toolkit/components/backgroundtasks/nsIBackgroundTasksRunner.idl
source-hash: 896c415cf2a8924d0214ed8e1a8ecaa271d42170

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/profiles/SelectableProfileService.sys.mjs`](../../../browser/components/profiles/SelectableProfileService.sys.mjs.md)

## メソッド / 属性
- `void runInDetachedProcess(ACString aTaskName, Array<ACString> aCommandLine)`: Runs a background process in an independent detached process. Any process
- `void removeDirectoryInDetachedProcess(ACString aParentDirPath, ACString aChildDirName, ACString aSecondsToWait, ACString aOtherFoldersSuffix, ACString aMetricsId)`: Runs removeDirectory background task.
