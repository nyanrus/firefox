# nsITabUnloader (xpcom/base/nsIAvailableMemoryWatcherBase.idl)

source: xpcom/base/nsIAvailableMemoryWatcherBase.idl
source-hash: 9f547d2f8da749d863a17d1cf157b42b338ed5ca

- 継承: nsISupports
- 役割: nsITabUnloader: interface to represent TabUnloader
- 実装: (未記入)

## メソッド / 属性
- `void unloadTabAsync()`: (未記入)

# nsIAvailableMemoryWatcherBase (xpcom/base/nsIAvailableMemoryWatcherBase.idl)

source: xpcom/base/nsIAvailableMemoryWatcherBase.idl
source-hash: 9f547d2f8da749d863a17d1cf157b42b338ed5ca

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/tabbrowser/TabUnloader.sys.mjs`](../../browser/components/tabbrowser/TabUnloader.sys.mjs.md)

## メソッド / 属性
- `void registerTabUnloader(nsITabUnloader aTabUnloader)`: (未記入)
- `void onUnloadAttemptCompleted(nsresult aResult)`: (未記入)
