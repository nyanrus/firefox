# nsIStreamConverterService (netwerk/streamconv/nsIStreamConverterService.idl)

source: netwerk/streamconv/nsIStreamConverterService.idl
source-hash: 6df706f10585902166c19e05ec3646bbe0b4c35b

- 継承: nsISupports
- 役割: The nsIStreamConverterService is a higher level stream converter factory
- 実装: (未記入)
- 使っているJS: [`browser/components/backup/BackupService.sys.mjs`](../../browser/components/backup/BackupService.sys.mjs.md)

## メソッド / 属性
- `boolean canConvert(string aFromType, string aToType)`: Tests whether conversion between the two specified types is possible.
- `ACString convertedType(ACString aFromType, nsIChannel aChannel)`: Returns the content type that will be returned from a converter
- `nsIInputStream convert(nsIInputStream aFromStream, string aFromType, string aToType, nsISupports aContext)`: <b>SYNCHRONOUS VERSION</b>
- `nsIStreamListener asyncConvertData(string aFromType, string aToType, nsIStreamListener aListener, nsISupports aContext)`: <b>ASYNCHRONOUS VERSION</b>
