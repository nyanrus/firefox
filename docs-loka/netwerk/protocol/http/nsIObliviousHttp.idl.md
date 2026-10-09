# nsIObliviousHttpClientResponse (netwerk/protocol/http/nsIObliviousHttp.idl)

source: netwerk/protocol/http/nsIObliviousHttp.idl
source-hash: 7309bfdc5556818dbf5a8621eee40979c5be3d91

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `Array<octet> decapsulate(Array<octet> encResponse)`: (未記入)

# nsIObliviousHttpClientRequest (netwerk/protocol/http/nsIObliviousHttp.idl)

source: netwerk/protocol/http/nsIObliviousHttp.idl
source-hash: 7309bfdc5556818dbf5a8621eee40979c5be3d91

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute Array<octet> encRequest`: (未記入)
- `readonly attribute nsIObliviousHttpClientResponse response`: (未記入)

# nsIObliviousHttpServerResponse (netwerk/protocol/http/nsIObliviousHttp.idl)

source: netwerk/protocol/http/nsIObliviousHttp.idl
source-hash: 7309bfdc5556818dbf5a8621eee40979c5be3d91

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute Array<octet> request`: (未記入)
- `Array<octet> encapsulate(Array<octet> response)`: (未記入)

# nsIObliviousHttpServer (netwerk/protocol/http/nsIObliviousHttp.idl)

source: netwerk/protocol/http/nsIObliviousHttp.idl
source-hash: 7309bfdc5556818dbf5a8621eee40979c5be3d91

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute Array<octet> encodedConfig`: (未記入)
- `nsIObliviousHttpServerResponse decapsulate(Array<octet> encRequest)`: (未記入)

# nsIObliviousHttp (netwerk/protocol/http/nsIObliviousHttp.idl)

source: netwerk/protocol/http/nsIObliviousHttp.idl
source-hash: 7309bfdc5556818dbf5a8621eee40979c5be3d91

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `nsIObliviousHttpClientRequest encapsulateRequest(Array<octet> encodedConfig, Array<octet> request)`: (未記入)
- `nsIObliviousHttpServer server()`: (未記入)
- `Array<Array<octet>> decodeConfigList(Array<octet> encodedConfigList)`: (未記入)

# nsIObliviousHttpService (netwerk/protocol/http/nsIObliviousHttp.idl)

source: netwerk/protocol/http/nsIObliviousHttp.idl
source-hash: 7309bfdc5556818dbf5a8621eee40979c5be3d91

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/mozcachedohttp/MozCachedOHTTPProtocolHandler.sys.mjs`](../../../browser/components/mozcachedohttp/MozCachedOHTTPProtocolHandler.sys.mjs.md)

## メソッド / 属性
- `nsIChannel newChannel(nsIURI relayURI, nsIURI targetURI, Array<octet> encodedConfig)`: (未記入)
- `void getTRRSettings(nsIURI relayURI, Array<octet> encodedConfig)`: (未記入)
- `void clearTRRConfig()`: (未記入)
