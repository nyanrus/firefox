# browser/components/attribution/AttributionCode.sys.mjs

source: browser/components/attribution/AttributionCode.sys.mjs
source-hash: 810b0b34e84271d3c5c82d922be7548d1f12703f
lines: 411

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`

## write()
- 位置: async L9-9
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.write()`

## read()
- 位置: async L10-10
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.read()`

## exists()
- 位置: async L11-11
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `IOUtils.exists()`

## msixCampaignId()
- 位置: async L71-77
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc[ "@mozilla.org/windows-package-manager;1" ].createInstance()`, `windowsPackageManager.campaignId()`
- 参照: `Ci.nsIWindowsPackageManager`
- XPCOM: [`nsIWindowsPackageManager`](../../../toolkit/system/windowsPackageManager/nsIWindowsPackageManager.idl.md) / `@mozilla.org/windows-package-manager;1` → `mozilla::toolkit::system::nsWindowsPackageManager` (toolkit/system/windowsPackageManager/components.conf)

## attributionFile()
- 位置: L84-92
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (AppConstants.platform == "win")` → `Services.dirsvc.get()`
- 条件付き依存: `if (AppConstants.platform == "win")` → `file.append()`
- 参照: `AppConstants.platform`, `Ci.nsIFile`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `Services.dirsvc`

## writeAttributionFile()
- 位置: async L99-115
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AttributionIOUtils.write()`, `IOUtils.makeDirectory()`, `Services.sysinfo.getProperty()`, `new TextEncoder().encode()`
- 条件付き依存: `if ( AppConstants.platform === "win" && Services.sysinfo.getProperty("hasWinPackageId") )` → `Services.console.logStringMessage()`
- 参照: `AppConstants.platform`, `AttributionCode.attributionFile`, `file.parent.path`, `file.path`
- XPCOM: `Services.console` / `Services.sysinfo`

## allowedCodeKeys()
- 位置: L120-122
- 役割: (未記入)
- 触るとき: (未記入)

## parseAttributionCode()
- 位置: L129-177
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ATTR_CODE_KEYS.includes()`, `Glean.browser.attributionErrors.decode_error.add()`, `code.split()`, `param.split()`
- 条件付き依存: `if (key && ATTR_CODE_KEYS.includes(key))` → `ATTR_CODE_VALUE_REGEX.test()`
- 条件付き依存: `if (!(key === "msstoresignedin"))` → `value.startsWith()`
- 条件付き依存: `if (key === "content" && value.startsWith(REFERRAL_PREFIX))` → `this.submitReferralCode()`
- 条件付き依存: `if (!(key && ATTR_CODE_KEYS.includes(key)))` → `param.startsWith()`
- 条件付き依存: `if (param.startsWith(MSCLKID_KEY_PREFIX))` → `param.substring()`
- 条件付き依存: `if (!(param.startsWith(MSCLKID_KEY_PREFIX)))` → `lazy.log.debug()`
- 参照: `MSCLKID_KEY_PREFIX.length`, `code.length`, `parsed.msclkid`

## submitReferralCode()
- 位置: L184-195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.browser.referralCode.set()`, `GleanPings.referrals.submit()`, `Services.prefs.getBoolPref()`, `Services.prefs.setBoolPref()`, `data.replace()`
- XPCOM: `Services.prefs`

## serializeAttributionData()
- 位置: L202-215
- 役割: (未記入)
- 触るとき: (未記入)

## _getMacAttrDataAsync()
- 位置: async L217-260
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `lazy.MacAttribution.getAttributionString()`, `lazy.log.debug()`, `lazy.log.warn()`
- 条件付き依存: `if (attrStr === null)` → `lazy.log.debug()`
- 条件付き依存: `if (attrStr === null)` → `Glean.browser.attributionErrors.null_error.add()`
- 条件付き依存: `if (attrStr == "")` → `lazy.log.debug()`
- 条件付き依存: `if (attrStr == "")` → `Glean.browser.attributionErrors.empty_error.add()`
- 条件付き依存: `if (!(attrStr == ""))` → `this.parseAttributionCode()`
- 条件付き依存: `if ( ex instanceof Ci.nsIException && ex.result == Cr.NS_ERROR_UNEXPECTED )` → `Glean.browser.attributionErrors.quarantine_error.add()`
- 参照: `Ci.nsIException`, `Cr.NS_ERROR_UNEXPECTED`, `ex.result`
- XPCOM: [`nsIException`](../../../xpcom/base/nsIException.idl.md)

## _getWindowsNSISAttrDataAsync()
- 位置: async L262-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `AttributionIOUtils.read()`
- 参照: `this.attributionFile.path`

## _getWindowsMSIXAttrDataAsync()
- 位置: async L266-277
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.sysinfo.getProperty()`, `encodeURIComponent()`, `encoder.encode()`, `lazy.log.debug()`, `this.msixCampaignId()`
- XPCOM: `Services.sysinfo`

## getAttrDataAsync()
- 位置: async L289-370
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `DOMException.isInstance()`, `Glean.browser.attributionErrors.read_error.add()`, `Services.sysinfo.getProperty()`, `lazy.log.debug()`
- 条件付き依存: `if (gCachedAttrData != null)` → `lazy.log.debug()`
- 条件付き依存: `if (gCachedAttrData != null)` → `JSON.stringify()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `lazy.log.debug()`
- 条件付き依存: `if (AppConstants.platform == "macosx")` → `this._getMacAttrDataAsync()`
- 条件付き依存: `if ( AppConstants.platform === "win" && Services.sysinfo.getProperty("hasWinPackageId") )` → `lazy.log.debug()`
- 条件付き依存: `if ( AppConstants.platform === "win" && Services.sysinfo.getProperty("hasWinPackageId") )` → `this._getWindowsMSIXAttrDataAsync()`
- 条件付き依存: `if (!( AppConstants.platform === "win" && Services.sysinfo.getProperty("hasWinPackageId") ))` → `lazy.log.debug()`
- 条件付き依存: `if (!( AppConstants.platform === "win" && Services.sysinfo.getProperty("hasWinPackageId") ))` → `this._getWindowsNSISAttrDataAsync()`
- 条件付き依存: `if (DOMException.isInstance(ex) && ex.name == "NotFoundError")` → `lazy.log.debug()`
- 条件付き依存: `if (DOMException.isInstance(ex) && ex.name == "NotFoundError")` → `JSON.stringify()`
- 条件付き依存: `if (bytes)` → `decoder.decode()`
- 条件付き依存: `if (bytes)` → `lazy.log.debug()`
- 条件付き依存: `if (bytes)` → `this.parseAttributionCode()`
- 条件付き依存: `if (bytes)` → `JSON.stringify()`
- 条件付き依存: `if (bytes)` → `Glean.browser.attributionErrors.decode_error.add()`
- 参照: `AppConstants.platform`, `attributionFile.path`, `ex.name`, `this.attributionFile`
- XPCOM: `Services.sysinfo`

## getCachedAttributionData()
- 位置: L379-381
- 役割: (未記入)
- 触るとき: (未記入)

## deleteFileAsync()
- 位置: async L388-399
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (AppConstants.platform == "win")` → `IOUtils.remove()`
- 参照: `AppConstants.platform`, `this.attributionFile.path`

## _clearCache()
- 位置: L405-409
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.env.exists()`
- XPCOM: `Services.env`
