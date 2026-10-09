# nsIIDNService (netwerk/dns/nsIIDNService.idl)

source: netwerk/dns/nsIIDNService.idl
source-hash: c112ba1d357acdd0d2c623469c8051561cd02b8e

- 継承: nsISupports
- 役割: IDN (Internationalized Domain Name) support. Provides facilities
- 実装: (未記入)
- 使っているJS: [`browser/base/content/browser-siteIdentity.js`](../../browser/base/content/browser-siteIdentity.js.md), [`browser/components/preferences/config/containers.mjs`](../../browser/components/preferences/config/containers.mjs.md), [`browser/components/qrcode/qrcode-dialog.js`](../../browser/components/qrcode/qrcode-dialog.js.md), [`browser/components/urlbar/UrlbarValueFormatter.sys.mjs`](../../browser/components/urlbar/UrlbarValueFormatter.sys.mjs.md), [`browser/modules/PermissionUI.sys.mjs`](../../browser/modules/PermissionUI.sys.mjs.md)

## メソッド / 属性
- `ACString domainToASCII(AUTF8String input)`: The UTS #46 ToASCII operation as parametrized by the WHATWG URL Standard
- `ACString convertUTF8toACE(AUTF8String input)`: Legacy variant of `domainToASCII` that allows allows any ASCII character that has a glyph.
- `AUTF8String domainToDisplay(AUTF8String input)`: The UTS #46 ToUnicode operation as parametrized by the WHATWG URL Standard,
- `AUTF8String convertToDisplayIDN(AUTF8String input)`: Legacy variant of `domainToDisplay` that allows allows any ASCII character that has a glyph.
- `AUTF8String convertACEtoUTF8(ACString input)`: The UTS #46 ToUnicode operation as parametrized by the WHATWG URL Standard,
