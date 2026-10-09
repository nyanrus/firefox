# nsITabUnloader (xpcom/base/nsIAvailableMemoryWatcherBase.idl)

source: xpcom/base/nsIAvailableMemoryWatcherBase.idl
source-hash: 9f547d2f8da749d863a17d1cf157b42b338ed5ca

- 継承: nsISupports
- 役割: nsITabUnloader: interface to represent TabUnloader
- 実装: (未記入)

## メソッド / 属性
- `void unloadTabAsync()`: 最後に使われてから最も時間が経っているタブをアンロードする。

# nsIAvailableMemoryWatcherBase (xpcom/base/nsIAvailableMemoryWatcherBase.idl)

source: xpcom/base/nsIAvailableMemoryWatcherBase.idl
source-hash: 9f547d2f8da749d863a17d1cf157b42b338ed5ca

- 継承: nsISupports
- 役割: システムのメモリ状況を監視し、メモリ不足・メモリ過多を検出したときに登録済みの TabUnloader を呼び出すためのインターフェース。
- 実装: `nsAvailableMemoryWatcherBase` (xpcom/base/AvailableMemoryWatcher.cpp)
- 使っているJS: [`browser/components/tabbrowser/TabUnloader.sys.mjs`](../../browser/components/tabbrowser/TabUnloader.sys.mjs.md)

## メソッド / 属性
- `void registerTabUnloader(nsITabUnloader aTabUnloader)`: メモリ不足時に呼び出される nsITabUnloader を登録する。
- `void onUnloadAttemptCompleted(nsresult aResult)`: タブのアンロード試行が完了したことを、結果 aResult とともに通知する。
