# browser/components/aiwindow/models/SecurityProperties.sys.mjs

source: browser/components/aiwindow/models/SecurityProperties.sys.mjs
source-hash: cf9aba4e80de4cd2c74a90069ec7b33c7818cd37
lines: 123

## <module>
- 役割: (未記入)

## isAllowedURLProtocol()
- 位置: L19-21
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ALLOWED_URL_PROTOCOLS.has()`, `URL.parse()`
- 参照: `URL.parse(url)?.protocol`

## SecurityProperties.privateData()
- 位置: L44-46
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#privateData`

## SecurityProperties.setPrivateData()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#newPrivateData`

## SecurityProperties.untrustedInput()
- 位置: L52-54
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#untrustedInput`

## SecurityProperties.setUntrustedInput()
- 位置: L55-57
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#newUntrustedInput`

## SecurityProperties.commit()
- 位置: L64-69
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#newPrivateData`, `this.#newUntrustedInput`, `this.#privateData`, `this.#untrustedInput`

## SecurityProperties.toJSON()
- 位置: L81-86
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#newPrivateData`, `this.#newUntrustedInput`, `this.#privateData`, `this.#untrustedInput`

## SecurityProperties.fromJSON()
- 位置: L100-112
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `obj.privateData`, `obj.untrustedInput`, `props.#privateData`, `props.#untrustedInput`

## SecurityProperties.getLogText()
- 位置: L119-121
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.privateData`, `this.untrustedInput`
