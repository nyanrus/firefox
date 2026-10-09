# browser/extensions/webcompat/lib/ua_helpers.js

source: browser/extensions/webcompat/lib/ua_helpers.js
source-hash: c157822fdf6eb200f0d5e8395564e9b87ced7152
lines: 203

## <module>
- 役割: (未記入)

## changeBrowserVersion()
- 位置: L11-43
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `new_ver.startsWith()`, `ua.match()`, `ua.replaceAll()`, `ua?.includes()`
- 条件付き依存: `if (typeof new_ver != "string")` → `String()`
- 条件付き依存: `if (new_ver.startsWith("+") || new_ver.startsWith("-"))` → `new_ver.startsWith()`
- 条件付き依存: `if (new_ver.startsWith("+") || new_ver.startsWith("-"))` → `cur_ver.split(".").map()`
- 条件付き依存: `if (new_ver.startsWith("+") || new_ver.startsWith("-"))` → `cur_ver.split()`
- 条件付き依存: `if (new_ver.startsWith("+") || new_ver.startsWith("-"))` → `parseInt()`
- 条件付き依存: `if (new_ver.startsWith("+") || new_ver.startsWith("-"))` → `new_ver .substr(1) .split(".") .map()`
- 条件付き依存: `if (new_ver.startsWith("+") || new_ver.startsWith("-"))` → `new_ver .substr(1) .split()`
- 条件付き依存: `if (new_ver.startsWith("+") || new_ver.startsWith("-"))` → `new_ver .substr()`
- 条件付き依存: `if (new_ver.startsWith("+") || new_ver.startsWith("-"))` → `ver_segs.entries()`
- 条件付き依存: `if (new_ver.startsWith("+") || new_ver.startsWith("-"))` → `ver_segs.join()`
- 参照: `config.browser`, `config.version`

## getRunningFirefoxVersion()
- 位置: L44-46
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `navigator.userAgent.match()`

## getFxQuantumSegment()
- 位置: L47-49
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UAHelpers.getRunningFirefoxVersion()`

## getDeviceAppropriateChromeUA()
- 位置: L51-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`
- 条件付き依存: `if (config.noCache || !UAHelpers._deviceAppropriateChromeUAs[key])` → `UAHelpers.getFxQuantumSegment()`
- 条件付き依存: `if (config.noCache || !UAHelpers._deviceAppropriateChromeUAs[key])` → `userAgent.includes()`
- 条件付き依存: `if (OS === "android" || (noOSGiven && userAgent.includes("Android")))` → `userAgent.includes()`
- 条件付き依存: `if (!(OS === "android" || (noOSGiven && userAgent.includes("Android"))))` → `userAgent.includes()`
- 条件付き依存: `if (!(OS === "macOS" || (noOSGiven && userAgent.includes("Macintosh"))))` → `userAgent.includes()`
- 参照: `UAHelpers._defaultChromeVersion`, `UAHelpers._deviceAppropriateChromeUAs`, `config.noCache`, `config.noFxQuantum`, `config.ua`, `navigator.userAgent`

## addGecko()
- 位置: L104-109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UAHelpers.getRunningFirefoxVersion()`
- 参照: `navigator.userAgent`

## addChrome()
- 位置: L110-118
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `navigator.userAgent.includes()`
- 参照: `UAHelpers._defaultChromeVersion`, `navigator.userAgent`

## safari()
- 位置: L119-131
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `config.osVersion?.replace()`
- 条件付き依存: `if (config.withFirefox)` → `UAHelpers.getRunningFirefoxVersion()`
- 条件付き依存: `if (config.withFxQuantum)` → `UAHelpers.getFxQuantumSegment()`
- 参照: `config.arch`, `config.version`, `config.webkitVersion`, `config.withFirefox`, `config.withFxQuantum`

## androidHotspot2Device()
- 位置: L132-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `originalUA.replace()`

## changeFirefoxToFireFox()
- 位置: L135-137
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ua.replace()`
- 参照: `navigator.userAgent`

## windows()
- 位置: L138-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `navigator.userAgent.match()`, `ua.replace()`
- 参照: `navigator.userAgent`

## desktopUA()
- 位置: L142-144
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ua.replace()`
- 参照: `navigator.userAgent`

## addSamsungForSamsungDevices()
- 位置: L145-156
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.systemManufacturer.getManufacturer()`, `manufacturer.toLowerCase()`
- 条件付き依存: `if (manufacturer && manufacturer.toLowerCase() === "samsung")` → `ua.replace()`
- 参照: `browser.systemManufacturer`, `navigator.userAgent`

## getPrefix()
- 位置: L157-159
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `originalUA.indexOf()`, `originalUA.substr()`

## overrideWithDeviceAppropriateChromeUA()
- 位置: L160-166
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.defineProperty()`, `Object.getOwnPropertyDescriptor()`, `Object.getPrototypeOf()`, `UAHelpers.getDeviceAppropriateChromeUA()`, `exportFunction()`
- 参照: `navigator.wrappedJSObject`, `ua.get`

## capVersionTo99()
- 位置: L167-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `originalUA .replace()`, `originalUA .replace(`Firefox/${ver[1]}`, "Firefox/99.0") .replace()`, `originalUA.match()`, `parseFloat()`

## capRvTo109()
- 位置: L176-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `originalUA.match()`, `originalUA.replace()`, `parseFloat()`

## capVersionToNumber()
- 位置: L183-190
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `originalUA.match()`, `originalUA.replace()`, `parseFloat()`

## getMacOSXUA()
- 位置: L191-196
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `originalUA.replace()`

## getWindowsUA()
- 位置: L197-201
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `originalUA.match()`
