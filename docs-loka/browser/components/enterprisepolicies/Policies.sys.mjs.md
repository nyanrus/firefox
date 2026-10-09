# browser/components/enterprisepolicies/Policies.sys.mjs

source: browser/components/enterprisepolicies/Policies.sys.mjs
source-hash: 2098c68ce8115a7839b2dcdff22087fdab10bb1d
lines: 3955

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyServiceGetters()`

## onBeforeAddons()
- 位置: L118-127
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- 条件付き依存: `if (Cu.isInAutomation)` → `lazy.clearBlockedAboutPages()`
- 参照: `Cu.isInAutomation`
- XPCOM: `Services.obs`

## onProfileAfterChange()
- 位置: L128-134
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## onBeforeUIStartup()
- 位置: L135-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## onAllWindowsRestored()
- 位置: L142-148
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`
- XPCOM: `Services.obs`

## onBeforeAddons()
- 位置: L152-154
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `manager.setExtensionPolicies()`
- 参照: `param.Extensions`

## onBeforeAddons()
- 位置: L158-216
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (defaultItem)` → `lazy.PoliciesUtils.setDefaultPref()`
- 参照: `defaultItem.Value`, `defaultItem?.Locked`, `item.Locked`, `item.Value`, `param.Default`

## onBeforeAddons()
- 位置: L220-227
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.addObserver()`, `channel.URI.host.endsWith()`, `subject.QueryInterface()`
- 条件付き依存: `if (channel.URI.host.endsWith(".google.com"))` → `channel.setRequestHeader()`
- 参照: `Ci.nsIHttpChannel`
- XPCOM: [`nsIHttpChannel`](../../../netwerk/protocol/http/nsIHttpChannel.idl.md) / `Services.obs`

## onBeforeUIStartup()
- 位置: L231-240
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!param)` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (!param)` → `manager.disallowFeature()`

## onBeforeUIStartup()
- 位置: L244-252
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`
- 条件付き依存: `if (!(param))` → `manager.disallowFeature()`

## validate()
- 位置: L256-344
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `/^0/.test()`, `/^\d+$/.test()`, `isNaN()`, `param.split()`, `parseInt()`, `pinParts.pop()`, `pinParts.shift()`
- 条件付き依存: `if (pinParts.length < 2)` → `lazy.log.error()`
- 条件付き依存: `if (pinParts.length > 3)` → `lazy.log.error()`
- 条件付き依存: `if (trailingPinPart != "")` → `lazy.log.error()`
- 条件付き依存: `if (!pinMajorVersionStr.length)` → `lazy.log.error()`
- 条件付き依存: `if (!/^\d+$/.test(pinMajorVersionStr))` → `lazy.log.error()`
- 条件付き依存: `if (/^0/.test(pinMajorVersionStr))` → `lazy.log.error()`
- 条件付き依存: `if (isNaN(pinMajorVersionInt))` → `lazy.log.error()`
- 条件付き依存: `if (pinMajorVersionInt < earliestPinMajorVersion)` → `lazy.log.error()`
- 条件付き依存: `if (pinParts.length)` → `pinParts.shift()`
- 条件付き依存: `if (!pinMinorVersionStr.length)` → `lazy.log.error()`
- 条件付き依存: `if (pinParts.length)` → `/^\d+$/.test()`
- 条件付き依存: `if (!/^\d+$/.test(pinMinorVersionStr))` → `lazy.log.error()`
- 条件付き依存: `if (pinParts.length)` → `/^0\d/.test()`
- 条件付き依存: `if (/^0\d/.test(pinMinorVersionStr))` → `lazy.log.error()`
- 条件付き依存: `if (pinParts.length)` → `parseInt()`
- 条件付き依存: `if (pinParts.length)` → `isNaN()`
- 条件付き依存: `if (isNaN(pinMinorVersionInt))` → `lazy.log.error()`
- 条件付き依存: `if ( pinMajorVersionInt == earliestPinMajorVersion && pinMinorVersionInt < earliestPinMinorVersion )` → `lazy.log.error()`
- 参照: `pinMajorVersionStr.length`, `pinMinorVersionStr.length`, `pinParts.length`

## onBeforeAddons()
- 位置: L355-422
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("SPNEGO" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("SPNEGO" in param)` → `param.SPNEGO.join()`
- 条件付き依存: `if ("Delegated" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("Delegated" in param)` → `param.Delegated.join()`
- 条件付き依存: `if ("NTLM" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("NTLM" in param)` → `param.NTLM.join()`
- 条件付き依存: `if ("NTLM" in param.AllowNonFQDN)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("SPNEGO" in param.AllowNonFQDN)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("NTLM" in param.AllowProxies)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("SPNEGO" in param.AllowProxies)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("PrivateBrowsing" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 参照: `param.AllowNonFQDN`, `param.AllowNonFQDN.NTLM`, `param.AllowNonFQDN.SPNEGO`, `param.AllowProxies`, `param.AllowProxies.NTLM`, `param.AllowProxies.SPNEGO`, `param.Locked`, `param.PrivateBrowsing`

## onBeforeAddons()
- 位置: L426-431
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L435-440
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L444-451
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.addAllowDenyPermissions()`
- 参照: `info.allowed_origins`, `info.protocol`

## onBeforeAddons()
- 位置: L455-461
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`
- 条件付き依存: `if (!(param))` → `manager.disallowFeature()`

## onBeforeUIStartup()
- 位置: L465-469
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `lazy.blockAboutPage()`

## onBeforeUIStartup()
- 位置: L473-478
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `lazy.blockAboutPage()`
- 条件付き依存: `if (param)` → `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L482-486
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`

## onBeforeUIStartup()
- 位置: L487-495
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `lazy.blockAboutPage()`

## onBeforeUIStartup()
- 位置: L499-504
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `lazy.blockAboutPage()`
- 条件付き依存: `if (param)` → `manager.disallowFeature()`

## onAllWindowsRestored()
- 位置: L508-512
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.BookmarksPolicies.processBookmarks()`

## onBeforeUIStartup()
- 位置: L516-567
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (typeof param === "boolean")` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (serviceValue !== undefined)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (hasBackup)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (hasRestore)` → `lazy.PoliciesUtils.setDefaultPref()`
- 参照: `param.AllowBackup`, `param.AllowRestore`

## onBeforeAddons()
- 位置: L571-576
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L580-706
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("ImportEnterpriseRoots" in param)` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (platform == "win")` → `Services.dirsvc.get()`
- 条件付き依存: `if (platform == "macosx" || platform == "linux")` → `Services.dirsvc.get()`
- 条件付き依存: `if ("Install" in param)` → `dirs.unshift()`
- 条件付き依存: `if ("Install" in param)` → `Services.dirsvc.get()`
- 条件付き依存: `if ("Install" in param)` → `Cc["@mozilla.org/file/local;1"].createInstance()`
- 条件付き依存: `if ("Install" in param)` → `certfile.initWithPath()`
- 条件付き依存: `if ("Install" in param)` → `dir.clone()`
- 条件付き依存: `if ("Install" in param)` → `certfile.append()`
- 条件付き依存: `if ("Install" in param)` → `certfile.exists()`
- 条件付き依存: `if ("Install" in param)` → `File.createFromNsIFile()`
- 条件付き依存: `if ("Install" in param)` → `lazy.reportFailure()`
- 条件付き依存: `if ("Install" in param)` → `reader.readAsBinaryString()`
- 参照: `AppConstants.platform`, `Ci.nsIFile`, `Services.dirsvc.get("DefProfLRt", Ci.nsIFile).parent.parent`, `Services.dirsvc.get("XREUSysExt", Ci.nsIFile).parent`, `param.ImportEnterpriseRoots`, `param.Install`, `reader.onloadend`
- XPCOM: [`nsIFile`](../shell/nsIShellService.idl.md) / `@mozilla.org/file/local;1` / `Services.dirsvc`

## reader.onloadend()
- 位置: L636-696
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `certFile.charCodeAt()`, `certFileArray.push()`, `lazy.gCertDB.constructX509()`, `lazy.gCertDB.constructX509FromBase64()`, `lazy.log.debug()`, `lazy.pemToBase64()`, `lazy.reportFailure()`
- 条件付き依存: `if (reader.readyState != reader.DONE)` → `lazy.reportFailure()`
- 条件付き依存: `if (cert)` → `lazy.gCertDB.isCertTrusted()`
- 条件付き依存: `if (cert)` → `lazy.gCertDB.addCert()`
- 条件付き依存: `if (cert)` → `lazy.gCertDB.addCertFromBase64()`
- 条件付き依存: `if (cert)` → `lazy.pemToBase64()`
- 条件付き依存: `if (cert)` → `lazy.reportFailure()`
- 参照: `Ci.nsIX509Cert.CA_CERT`, `Ci.nsIX509CertDB.TRUSTED_SSL`, `certFile.length`, `certfile.path`, `reader.DONE`, `reader.readyState`, `reader.result`
- XPCOM: [`nsIX509Cert`](../../../netwerk/base/nsITLSServerSocket.idl.md) / `nsIX509CertDB`

## onBeforeUIStartup()
- 位置: L710-739
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (typeof param === "boolean")` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (typeof param === "boolean")` → `Object.values()`
- 条件付き依存: `if (member in param)` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (param.Exceptions)` → `lazy.addAllowDenyPermissions()`
- 参照: `param.Exceptions`

## onBeforeAddons()
- 位置: L743-745
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L753-926
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`, `lazy.PoliciesUtils.setPrefIfPresentAndLock()`
- 条件付き依存: `if ("AgentTimeout" in param)` → `Number.isInteger()`
- 条件付き依存: `if (!Number.isInteger(param.AgentTimeout))` → `lazy.log.error()`
- 条件付き依存: `if (!(!Number.isInteger(param.AgentTimeout)))` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (!("AgentTimeout" in param))` → `Services.prefs.lockPref()`
- 条件付き依存: `if (pref[0] in param)` → `Number.isInteger()`
- 条件付き依存: `if ( !Number.isInteger(param[pref[0]]) || param[pref[0]] < 0 || param[pref[0]] > 2 )` → `lazy.log.error()`
- 条件付き依存: `if ( !Number.isInteger(param[pref[0]]) || param[pref[0]] < 0 || param[pref[0]] > 2 )` → `Services.prefs.lockPref()`
- 条件付き依存: `if (!( !Number.isInteger(param[pref[0]]) || param[pref[0]] < 0 || param[pref[0]] > 2 ))` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (!(pref[0] in param))` → `Services.prefs.lockPref()`
- 条件付き依存: `if (pref[0] in param)` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if ("InterceptionPoints" in param)` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (!("InterceptionPoints" in param))` → `Services.prefs.lockPref()`
- 条件付き依存: `if ("Enabled" in param)` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if ("Enabled" in param)` → `Cc["@mozilla.org/contentanalysis;1"].getService()`
- 条件付き依存: `if (!("Enabled" in param))` → `Services.prefs.lockPref()`
- 参照: `Ci.nsIContentAnalysis`, `ca.isSetByEnterprisePolicy`, `param.AgentTimeout`, `param.Enabled`, `param.InterceptionPoints`, `param.InterceptionPoints[pref[0]].Enabled`, `param.InterceptionPoints[pref[0]].PlainTextOnly`
- XPCOM: [`nsIContentAnalysis`](../../../toolkit/components/contentanalysis/nsIContentAnalysis.idl.md) / `@mozilla.org/contentanalysis;1` → `mozilla::contentanalysis::ContentAnalysis` (toolkit/components/contentanalysis/components.conf) / `Services.prefs`

## onBeforeUIStartup()
- 位置: L930-1054
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getDefaultBranch()`, `defaultPref.getIntPref()`, `lazy.PoliciesUtils.setDefaultPref()`, `lazy.addAllowDenyPermissions()`, `manager.getActivePolicies()`
- 条件付き依存: `if ( param.Allow?.length && !manager.getActivePolicies()?.SanitizeOnShutdown?.Exceptions?.length )` → `lazy.log.warn()`
- 条件付き依存: `if ( param.Allow?.length && !manager.getActivePolicies()?.SanitizeOnShutdown?.Exceptions?.length )` → `lazy.addAllowDenyPermissions()`
- 条件付き依存: `if (param.AllowSession)` → `lazy.addPolicyPermission()`
- 条件付き依存: `if (param.AllowSession)` → `lazy.reportFailure()`
- 条件付き依存: `if (param.Block)` → `param.Block.map(url => url.hostname) .sort() .join()`
- 条件付き依存: `if (param.Block)` → `param.Block.map(url => url.hostname) .sort()`
- 条件付き依存: `if (param.Block)` → `param.Block.map()`
- 条件付き依存: `if (param.Block)` → `lazy.runOncePerModification()`
- 条件付き依存: `if (param.Block)` → `Services.cookies.removeCookiesWithOriginAttributes()`
- 条件付き依存: `if (param.ExpireAtSessionEnd != undefined)` → `lazy.log.error()`
- 参照: `Ci.nsICookiePermission.ACCESS_SESSION`, `Ci.nsICookieService.BEHAVIOR_ACCEPT`, `Ci.nsICookieService.BEHAVIOR_LIMIT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_PARTITION_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT`, `Ci.nsICookieService.BEHAVIOR_REJECT_FOREIGN`, `Ci.nsICookieService.BEHAVIOR_REJECT_TRACKER`, `blocked.hostname`, `manager.getActivePolicies()?.SanitizeOnShutdown?.Exceptions?.length`, `origin.href`, `param.AcceptThirdParty`, `param.Allow`, `param.Allow?.length`, `param.AllowSession`, `param.Behavior`, `param.BehaviorPrivateBrowsing`, `param.Block`, `param.Default`, `param.ExpireAtSessionEnd`, `param.Locked`, `param.RejectTracker`, `url.hostname`
- XPCOM: [`nsICookiePermission`](../../../netwerk/cookie/nsICookiePermission.idl.md) / [`nsICookieService`](../../../netwerk/cookie/nsICookieService.idl.md) / `Services.cookies` / `Services.prefs`

## onBeforeAddons()
- 位置: L1058-1071
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (!(param))` → `manager.disallowFeature()`
- 条件付き依存: `if (!(param))` → `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L1075-1080
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setDefaultPref()`, `lazy.replacePathVariables()`

## onBeforeAddons()
- 位置: L1084-1103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Number.isInteger()`
- 条件付き依存: `if (!Number.isInteger(param))` → `lazy.log.error()`
- 条件付き依存: `if (param == 3)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (param == 2)` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (!(param == 2))` → `lazy.log.error()`

## onBeforeAddons()
- 位置: L1107-1115
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L1119-1123
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`

## onBeforeAddons()
- 位置: L1127-1164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.getActivePolicies()`, `lazy.gMIMEService.getFromTypeAndExtension()`, `lazy.processMIMEInfo()`
- 条件付き依存: `if (!param)` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (!param)` → `lazy.runOncePerModification()`
- 条件付き依存: `if (!param)` → `lazy.gMIMEService.getFromTypeAndExtension()`
- 条件付き依存: `if (!param)` → `lazy.processMIMEInfo()`
- 参照: `policies.Handlers?.extensions?.pdf`, `policies.Handlers?.mimeTypes`
- XPCOM: `Services.policies` / `Services.prefs`

## onBeforeAddons()
- 位置: L1168-1206
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L1216-1228
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (param)` → `manager.disallowFeature()`
- 条件付き依存: `if (param)` → `lazy.blockAboutPage()`

## onBeforeAddons()
- 位置: L1232-1243
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeUIStartup()
- 位置: L1247-1251
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`

## onBeforeAddons()
- 位置: L1255-1268
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `manager.getActivePolicies()`
- 条件付き依存: `if (param)` → `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeUIStartup()
- 位置: L1272-1279
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L1283-1295
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`
- 条件付き依存: `if (param)` → `lazy.PoliciesUtils.setAndLockPref()`

## onProfileAfterChange()
- 位置: L1299-1303
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeUIStartup()
- 位置: L1307-1311
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L1315-1325
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.LaunchOnLogin.disable()`, `lazy.PoliciesUtils.setAndLockPref()`, `manager.disallowFeature()`

## onBeforeUIStartup()
- 位置: L1329-1333
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`

## onBeforeUIStartup()
- 位置: L1337-1345
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`
- 条件付き依存: `if (param)` → `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L1349-1358
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`
- 条件付き依存: `if (param)` → `lazy.blockAboutPage()`
- 条件付き依存: `if (param)` → `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeUIStartup()
- 位置: L1362-1370
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`
- 条件付き依存: `if (param)` → `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeUIStartup()
- 位置: L1374-1379
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`
- 条件付き依存: `if (param)` → `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L1383-1387
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`

## onBeforeUIStartup()
- 位置: L1391-1395
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`

## onBeforeUIStartup()
- 位置: L1399-1403
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`

## onBeforeUIStartup()
- 位置: L1407-1421
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("InvalidCertificate" in param)` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if ("SafeBrowsing" in param)` → `lazy.PoliciesUtils.setAndLockPref()`
- 参照: `param.InvalidCertificate`, `param.SafeBrowsing`

## onBeforeUIStartup()
- 位置: L1425-1429
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`

## onBeforeAddons()
- 位置: L1433-1437
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`

## onBeforeAddons()
- 位置: L1441-1461
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (param)` → `lazy.blockAboutPage()`

## onBeforeUIStartup()
- 位置: L1465-1469
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`

## onBeforeUIStartup()
- 位置: L1473-1487
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setCharPref()`, `lazy.runOncePerModification()`
- XPCOM: `Services.prefs`

## onBeforeUIStartup()
- 位置: L1491-1542
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( typeof param === "boolean" || param == "default-on" || param == "default-off" )` → `lazy.runOncePerModification()`
- 条件付き依存: `if ( typeof param === "boolean" || param == "default-on" || param == "default-off" )` → `Services.xulStore.setValue()`
- 条件付き依存: `if (!( typeof param === "boolean" || param == "default-on" || param == "default-off" ))` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (!( typeof param === "boolean" || param == "default-on" || param == "default-off" ))` → `Services.xulStore.setValue()`
- 条件付き依存: `if (!( typeof param === "boolean" || param == "default-on" || param == "default-off" ))` → `manager.disallowFeature()`
- XPCOM: `Services.xulStore`

## onBeforeAddons()
- 位置: L1546-1573
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("Enabled" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("ProviderURL" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("ExcludedDomains" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("ExcludedDomains" in param)` → `param.ExcludedDomains.join()`
- 参照: `param.Enabled`, `param.Fallback`, `param.Locked`, `param.ProviderURL.href`

## onBeforeUIStartup()
- 位置: L1577-1582
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L1586-1599
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`, `lazy.replacePathVariables()`

## onAllWindowsRestored()
- 位置: L1603-1634
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param.Category)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (param.Category)` → `ChromeUtils.importESModule()`
- 条件付き依存: `if (param.Category)` → `ContentBlockingPrefs.setPrefsToCategory()`
- 条件付き依存: `if (param.Category)` → `ContentBlockingPrefs.matchCBCategory()`
- 条件付き依存: `if (param.Category == "strict" && !param.Locked)` → `Services.prefs.unlockPref()`
- 参照: `param.Category`, `param.Locked`
- XPCOM: `Services.prefs`

## onBeforeUIStartup()
- 位置: L1635-1717
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("Exceptions" in param)` → `lazy.addAllowDenyPermissions()`
- 条件付き依存: `if ("BaselineExceptions" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("ConvenienceExceptions" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (param.Value)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (!(param.Value))` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if ("Cryptomining" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("Fingerprinting" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("EmailTracking" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("SuspectedFingerprinting" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 参照: `param.BaselineExceptions`, `param.Category`, `param.ConvenienceExceptions`, `param.Cryptomining`, `param.EmailTracking`, `param.Exceptions`, `param.Fingerprinting`, `param.Locked`, `param.SuspectedFingerprinting`, `param.Value`

## onBeforeAddons()
- 位置: L1721-1729
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("Enabled" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 参照: `param.Enabled`, `param.Locked`

## onBeforeUIStartup()
- 位置: L1738-1794
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `Promise.resolve()`
- 条件付き依存: `if ("Uninstall" in param)` → `lazy.uninstallListedAddons()`
- 条件付き依存: `if ("Install" in param)` → `uninstallingPromise.then()`
- 条件付き依存: `if (uninstallListChanged)` → `lazy.clearRunOnceModification()`
- 条件付き依存: `if ("Install" in param)` → `lazy.runOncePerModification()`
- 条件付き依存: `if ("Install" in param)` → `JSON.stringify()`
- 条件付き依存: `if ("Install" in param)` → `Services.io.newFileURI()`
- 条件付き依存: `if ("Install" in param)` → `Services.io.newURI()`
- 条件付き依存: `if ("Install" in param)` → `lazy.reportFailure()`
- 条件付き依存: `if ("Install" in param)` → `lazy.installAddonFromURL()`
- 条件付き依存: `if ("Locked" in param)` → `manager.disallowFeature()`
- 参照: `lazy.FileUtils.File`, `param.Install`, `param.Locked`, `param.Uninstall`, `uri.spec`
- XPCOM: `Services.io`

## onBeforeAddons()
- 位置: L1798-1817
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.applyExtensionGuards()`, `lazy.discardAMOUpdateURLs()`, `lazy.reportFailure()`, `manager.setExtensionSettings()`
- 参照: `e.message`

## onBeforeUIStartup()
- 位置: async L1818-1999
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.getExtensionSettings()`, `addons.set()`, `addons.values()`, `blockedPerms.includes()`, `granted.permissions.filter()`, `lazy.AddonManager.getAllAddons()`, `lazy.AddonManagerPrivate.updateAddonAppDisabledStates()`, `lazy.ExtensionPermissions.get()`, `lazy.log.debug()`
- 条件付き依存: `if ( "installation_mode" in extensionSettings["*"] && extensionSettings["*"].installation_mode == "blocked" )` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if ( "installation_mode" in extensionSettings["*"] && extensionSettings["*"].installation_mode == "blocked" )` → `manager.disallowFeature()`
- 条件付き依存: `if ("restricted_domains" in extensionSettings["*"])` → `Services.prefs .getCharPref("extensions.webextensions.restrictedDomains") .split()`
- 条件付き依存: `if ("restricted_domains" in extensionSettings["*"])` → `Services.prefs .getCharPref()`
- 条件付き依存: `if ("restricted_domains" in extensionSettings["*"])` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if ("restricted_domains" in extensionSettings["*"])` → `restrictedDomains .concat(extensionSettings["*"].restricted_domains) .join()`
- 条件付き依存: `if ("restricted_domains" in extensionSettings["*"])` → `restrictedDomains .concat()`
- 条件付き依存: `if ( extensionSettings[extensionID].installation_mode == "force_installed" || extensionSettings[extensionID].installation_mode == "normal_installed" )` → `addons.get()`
- 条件付き依存: `if (extensionSettings[extensionID].install_url)` → `lazy.installAddonFromURL()`
- 条件付き依存: `if (extensionSettings[extensionID].update_url)` → `lazy.installAddonFromUpdateURL()`
- 条件付き依存: `if (!(extensionSettings[extensionID].update_url))` → `lazy.installAddonFromRepository()`
- 条件付き依存: `if ( extensionSettings[extensionID].installation_mode == "force_installed" || extensionSettings[extensionID].installation_mode == "normal_installed" )` → `manager.disallowFeature()`
- 条件付き依存: `if ( extensionSettings[extensionID].installation_mode == "force_installed" )` → `manager.disallowFeature()`
- 条件付き依存: `if ( extensionSettings[extensionID].installation_mode == "force_installed" || extensionSettings[extensionID].installation_mode == "normal_installed" )` → `allowedExtensions.push()`
- 条件付き依存: `if ( extensionSettings[extensionID].installation_mode == "allowed" )` → `allowedExtensions.push()`
- 条件付き依存: `if ( extensionSettings[extensionID].installation_mode == "blocked" )` → `addons.has()`
- 条件付き依存: `if (addons.has(extensionID))` → `lazy.AddonManager.getAddonByID()`
- 条件付き依存: `if (addons.has(extensionID))` → `addon.uninstall()`
- 条件付き依存: `if (addons.has(extensionID))` → `addons.delete()`
- 条件付き依存: `if (addons.has(extensionID))` → `lazy.log.debug()`
- 条件付き依存: `if (blockAllExtensions || allowedTypes)` → `addons.values()`
- 条件付き依存: `if (blockAllExtensions || allowedTypes)` → `allowedExtensions.includes()`
- 条件付き依存: `if (blockAllExtensions || allowedTypes)` → `allowedTypes.includes()`
- 条件付き依存: `if ( !allowedExtensions.includes(addon.id) && !(blockAllExtensions && addon.id in extensionSettings) && (blockAllExtensions || !allowedTypes.includes(addon.type)) )` → `lazy.AddonManager.getAddonByID()`
- 条件付き依存: `if ( !allowedExtensions.includes(addon.id) && !(blockAllExtensions && addon.id in extensionSettings) && (blockAllExtensions || !allowedTypes.includes(addon.type)) )` → `addonToUninstall.uninstall()`
- 条件付き依存: `if ( !allowedExtensions.includes(addon.id) && !(blockAllExtensions && addon.id in extensionSettings) && (blockAllExtensions || !allowedTypes.includes(addon.type)) )` → `addons.delete()`
- 条件付き依存: `if ( !allowedExtensions.includes(addon.id) && !(blockAllExtensions && addon.id in extensionSettings) && (blockAllExtensions || !allowedTypes.includes(addon.type)) )` → `lazy.log.debug()`
- 条件付き依存: `if (toRemove.length)` → `WebExtensionPolicy.getByID()`
- 条件付き依存: `if (toRemove.length)` → `lazy.ExtensionPermissions.remove()`
- 参照: `Services.policies.getExtensionSettings(addon.id) ?.blocked_permissions`, `WebExtensionPolicy.getByID(addon.id)?.extension`, `a.id`, `addon.id`, `addon.isBuiltin`, `addon.isSystem`, `addon.scope`, `addon.type`, `blockedPerms.length`, `extensionSettings["*"].installation_mode`, `extensionSettings["*"].restricted_domains`, `extensionSettings["*"]?.allowed_types`, `extensionSettings[extensionID].install_url`, `extensionSettings[extensionID].installation_mode`, `extensionSettings[extensionID].update_url`, `lazy.AddonManager.SCOPE_PROFILE`, `toRemove.length`
- XPCOM: `Services.policies` / `Services.prefs`

## onBeforeAddons()
- 位置: L2003-2007
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!param)` → `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L2011-2116
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("Search" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("Weather" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("TopSites" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("SponsoredTopSites" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("Highlights" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("Pocket" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("Stories" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("SponsoredPocket" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("SponsoredStories" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ( param.Locked && "SponsoredTopSites" in param && "SponsoredStories" in param )` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("Enabled" in param.Widgets)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (param.Widgets)` → `lazy.PoliciesUtils.setDefaultPref()`
- 参照: `param.Highlights`, `param.Locked`, `param.Pocket`, `param.Search`, `param.SponsoredPocket`, `param.SponsoredStories`, `param.SponsoredTopSites`, `param.Stories`, `param.TopSites`, `param.Weather`, `param.Widgets`, `param.Widgets.Blocked`, `param.Widgets.Enabled`

## onBeforeAddons()
- 位置: L2120-2146
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("WebSuggestions" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("SponsoredSuggestions" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("OnlineEnabled" in param || "ImproveSuggest" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 参照: `lazy.QuickSuggest.initPromise`, `param.ImproveSuggest`, `param.Locked`, `param.OnlineEnabled`, `param.SponsoredSuggestions`, `param.WebSuggestions`

## onBeforeAddons()
- 位置: L2150-2195
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.getActivePolicies()`
- 条件付き依存: `if (policies.AIControls)` → `lazy.log.warn()`
- 条件付き依存: `if (value !== undefined)` → `lazy.PoliciesUtils.setDefaultPref()`
- 参照: `param.Enabled`, `param.Locked`, `policies.AIControls`
- XPCOM: `Services.policies`

## onBeforeAddons()
- 位置: L2199-2204
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L2208-2267
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!mimeType)` → `lazy.reportFailure()`
- 条件付き依存: `if ("mimeTypes" in param)` → `lazy.gMIMEService.getFromTypeAndExtension()`
- 条件付き依存: `if ("mimeTypes" in param)` → `lazy.processMIMEInfo()`
- 条件付き依存: `if ("mimeTypes" in param)` → `lazy.reportFailure()`
- 条件付き依存: `if (!extension)` → `lazy.reportFailure()`
- 条件付き依存: `if ("extensions" in param)` → `lazy.gMIMEService.getFromTypeAndExtension()`
- 条件付き依存: `if ("extensions" in param)` → `lazy.processMIMEInfo()`
- 条件付き依存: `if ("extensions" in param)` → `lazy.reportFailure()`
- 条件付き依存: `if (!scheme)` → `lazy.reportFailure()`
- 条件付き依存: `if ("schemes" in param)` → `lazy.gExternalProtocolService.getProtocolHandlerInfo()`
- 条件付き依存: `if ("schemes" in param)` → `lazy.processMIMEInfo()`
- 条件付き依存: `if ("schemes" in param)` → `lazy.reportFailure()`
- 参照: `param.extensions`, `param.mimeTypes`, `param.schemes`

## onBeforeAddons()
- 位置: L2271-2275
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!param)` → `lazy.PoliciesUtils.setAndLockPref()`

## migrateLegacySyntax()
- 位置: L2282-2297
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.HomePage.parseCustomHomepageURLs()`, `param.URL.includes()`
- 参照: `param.Additional`, `param.URL`, `param?.URL`

## onBeforeUIStartup()
- 位置: L2299-2370
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param.Additional && param.Additional.length)` → `param.Additional.map(url => url.href).join()`
- 条件付き依存: `if (param.Additional && param.Additional.length)` → `param.Additional.map()`
- 条件付き依存: `if ("URL" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (param.Locked)` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (!(param.Locked))` → `lazy.clearRunOnceModification()`
- 条件付き依存: `if (param.URL != "about:blank")` → `manager.disallowFeature()`
- 条件付き依存: `if (param.StartPage)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("NewTabOnRestore" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 参照: `param.Additional`, `param.Additional.length`, `param.Locked`, `param.NewTabOnRestore`, `param.StartPage`, `param.URL`, `param.URL.href`, `url.href`

## onBeforeAddons()
- 位置: L2374-2376
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.addAllowDenyPermissions()`

## onBeforeAddons()
- 位置: L2380-2404
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`, `lazy.PoliciesUtils.setDefaultPref()`

## onBeforeUIStartup()
- 位置: L2408-2435
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("Allow" in param)` → `lazy.addAllowDenyPermissions()`
- 条件付き依存: `if ("Default" in param)` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (!param.Default)` → `manager.disallowFeature()`
- 条件付き依存: `if (!param.Default)` → `lazy.PoliciesUtils.setAndLockPref()`
- 参照: `param.Allow`, `param.Default`

## onBeforeAddons()
- 位置: L2439-2446
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!param)` → `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L2454-2459
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setDefaultPref()`

## onBeforeAddons()
- 位置: L2463-2468
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setDefaultPref()`, `param.join()`

## onBeforeAddons()
- 位置: L2472-2490
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs .getCharPref()`, `Services.prefs .getCharPref("capability.policy.policynames", "") .split()`, `lazy.PoliciesUtils.setAndLockPref()`, `param.join()`, `policyNames.join()`, `policyNames.push()`
- XPCOM: `Services.prefs`

## onBeforeAddons()
- 位置: L2494-2545
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`
- 条件付き依存: `if ("Enabled" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (param.Enabled === false)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (!(param.Enabled === false))` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("SkipDomains" in param && Array.isArray(param.SkipDomains))` → `param.SkipDomains.join()`
- 条件付き依存: `if ("SkipDomains" in param && Array.isArray(param.SkipDomains))` → `lazy.PoliciesUtils.setDefaultPref()`
- 参照: `param.BlockTrackers`, `param.EnablePrompting`, `param.Enabled`, `param.Locked`, `param.SkipDomains`

## onBeforeAddons()
- 位置: L2551-2555
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`

## onBeforeAddons()
- 位置: L2559-2564
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L2568-2574
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L2578-2580
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onProfileAfterChange()
- 位置: L2584-2588
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`

## onBeforeUIStartup()
- 位置: L2592-2598
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeUIStartup()
- 位置: L2602-2611
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.getActivePolicies()`
- 条件付き依存: `if ("OfferToSaveLogins" in policies)` → `lazy.log.error()`
- 条件付き依存: `if (!("OfferToSaveLogins" in policies))` → `lazy.PoliciesUtils.setDefaultPref()`
- XPCOM: `Services.policies`

## onProfileAfterChange()
- 位置: L2615-2619
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onProfileAfterChange()
- 位置: L2623-2630
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`, `manager.disallowFeature()`
- 参照: `param.href`

## onBeforeUIStartup()
- 位置: L2634-2647
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (!param)` → `lazy.blockAboutPage()`
- 条件付き依存: `if (!param)` → `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeUIStartup()
- 位置: L2651-2653
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.addAllowDenyPermissions()`

## onBeforeAddons()
- 位置: L2657-2667
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("Enabled" in param)` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if ("EnablePermissions" in param)` → `lazy.PoliciesUtils.setAndLockPref()`
- 参照: `param.EnablePermissions`, `param.Enabled`

## onBeforeUIStartup()
- 位置: L2671-2752
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param.Camera)` → `lazy.addAllowDenyPermissions()`
- 条件付き依存: `if (param.Camera)` → `lazy.setDefaultPermission()`
- 条件付き依存: `if (param.Microphone)` → `lazy.addAllowDenyPermissions()`
- 条件付き依存: `if (param.Microphone)` → `lazy.setDefaultPermission()`
- 条件付き依存: `if (param.Autoplay)` → `lazy.addAllowDenyPermissions()`
- 条件付き依存: `if ("Default" in param.Autoplay)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (param.Location)` → `lazy.addAllowDenyPermissions()`
- 条件付き依存: `if (param.Location)` → `lazy.setDefaultPermission()`
- 条件付き依存: `if (param.Notifications)` → `lazy.addAllowDenyPermissions()`
- 条件付き依存: `if (param.Notifications)` → `lazy.setDefaultPermission()`
- 条件付き依存: `if ("VirtualReality" in param)` → `lazy.addAllowDenyPermissions()`
- 条件付き依存: `if ("VirtualReality" in param)` → `lazy.setDefaultPermission()`
- 条件付き依存: `if ("ScreenShare" in param)` → `lazy.addAllowDenyPermissions()`
- 条件付き依存: `if ("ScreenShare" in param)` → `lazy.setDefaultPermission()`
- 参照: `param.Autoplay`, `param.Autoplay.Allow`, `param.Autoplay.Block`, `param.Autoplay.Default`, `param.Autoplay.Locked`, `param.Camera`, `param.Camera.Allow`, `param.Camera.Block`, `param.Location`, `param.Location.Allow`, `param.Location.Block`, `param.Microphone`, `param.Microphone.Allow`, `param.Microphone.Block`, `param.Notifications`, `param.Notifications.Allow`, `param.Notifications.Block`, `param.ScreenShare`, `param.ScreenShare.Allow`, `param.ScreenShare.Block`, `param.VirtualReality`, `param.VirtualReality.Allow`, `param.VirtualReality.Block`

## onBeforeAddons()
- 位置: L2756-2768
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("Enabled" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (param.Locked)` → `Services.prefs.lockPref()`
- 参照: `param.Enabled`, `param.Locked`
- XPCOM: `Services.prefs`

## onBeforeUIStartup()
- 位置: L2772-2798
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.addAllowDenyPermissions()`
- 条件付き依存: `if (param.Locked)` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (param.Default !== undefined)` → `lazy.PoliciesUtils.setDefaultPref()`
- 参照: `param.Allow`, `param.Default`, `param.Locked`

## onBeforeAddons()
- 位置: L2802-2812
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L2816-3007
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `blockedPrefs.includes()`, `preference.startsWith()`
- 条件付き依存: `if (!AppConstants.MOZ_REQUIRE_SIGNING)` → `allowedPrefixes.push()`
- 条件付き依存: `if (blockedPrefs.includes(preference))` → `lazy.reportFailure()`
- 条件付き依存: `if (preference.startsWith("security."))` → `allowedSecurityPrefs.includes()`
- 条件付き依存: `if (!allowedSecurityPrefs.includes(preference))` → `lazy.reportFailure()`
- 条件付き依存: `if (!(preference.startsWith("security.")))` → `allowedPrefixes.some()`
- 条件付き依存: `if (!(preference.startsWith("security.")))` → `preference.startsWith()`
- 条件付き依存: `if ( !allowedPrefixes.some(prefix => preference.startsWith(prefix)) )` → `lazy.reportFailure()`
- 条件付き依存: `if (typeof param[preference] != "object")` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (typeof param[preference] != "object")` → `lazy.reportFailure()`
- 条件付き依存: `if (typeof param[preference] != "object")` → `lazy.describePreferenceFailure()`
- 条件付き依存: `if (param[preference].Status == "clear")` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (!(param[preference].Status == "user"))` → `Services.prefs.getDefaultBranch()`
- 条件付き依存: `if (!(typeof param[preference] != "object"))` → `Services.prefs.prefIsLocked()`
- 条件付き依存: `if (prefWasLocked)` → `Services.prefs.unlockPref()`
- 条件付き依存: `if (!(typeof param[preference] != "object"))` → `prefBranch.setBoolPref()`
- 条件付き依存: `if (!(typeof param[preference] != "object"))` → `Number.isInteger()`
- 条件付き依存: `if (!(typeof param[preference] != "object"))` → `prefBranch.getPrefType()`
- 条件付き依存: `if (!(typeof param[preference] != "object"))` → `[0, 1].includes()`
- 条件付き依存: `if ( param[preference].Type == "number" || prefBranch.getPrefType(preference) == prefBranch.PREF_INT || ![0, 1].includes(param[preference].Value) )` → `prefBranch.setIntPref()`
- 条件付き依存: `if (!( param[preference].Type == "number" || prefBranch.getPrefType(preference) == prefBranch.PREF_INT || ![0, 1].includes(param[preference].Value) ))` → `prefBranch.setBoolPref()`
- 条件付き依存: `if (!(typeof param[preference] != "object"))` → `prefBranch.setStringPref()`
- 条件付き依存: `if (!(typeof param[preference] != "object"))` → `lazy.reportFailure()`
- 条件付き依存: `if (!(typeof param[preference] != "object"))` → `lazy.describePreferenceFailure()`
- 条件付き依存: `if (param[preference].Status == "locked" || prefWasLocked)` → `Services.prefs.lockPref()`
- 参照: `AppConstants.MOZ_REQUIRE_SIGNING`, `Services.prefs`, `param[preference].Status`, `param[preference].Type`, `param[preference].Value`, `prefBranch.PREF_INT`
- XPCOM: `Services.prefs`

## onAllWindowsRestored()
- 位置: L3011-3017
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`
- 条件付き依存: `if (!(param))` → `manager.disallowFeature()`

## onBeforeUIStartup()
- 位置: L3021-3023
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L3027-3049
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`, `lazy.blockAboutPage()`, `manager.disallowFeature()`

## onBeforeAddons()
- 位置: L3053-3058
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L3062-3070
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.ProxyPolicies.configureProxySettings()`
- 条件付き依存: `if (param.Locked)` → `manager.disallowFeature()`
- 参照: `lazy.PoliciesUtils.setDefaultPref`, `param.Locked`

## onBeforeUIStartup()
- 位置: L3074-3106
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (typeof param.RestartTimeOfDay === "object")` → `Temporal.PlainTime.from()`
- 条件付き依存: `if (typeof param.RestartTimeOfDay === "object")` → `lazy.reportFailure()`
- 参照: `param.NotificationPeriodHours`, `param.RestartTimeOfDay`, `param.RestartTimeOfDay.Hour`, `param.RestartTimeOfDay.Minute`, `restartTimeOfDay.Hour`, `restartTimeOfDay.Minute`, `timeOfDay.hour`, `timeOfDay.minute`

## onBeforeAddons()
- 位置: L3110-3126
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `JSON.stringify()`, `lazy.runOncePerModification()`
- 条件付き依存: `if (param)` → `param.split()`
- 参照: `Services.locale.requestedLocales`
- XPCOM: `Services.locale`

## onBeforeUIStartup()
- 位置: L3130-3361
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `manager.getActivePolicies()`
- 条件付き依存: `if (manager.getActivePolicies().ClearOnShutdown)` → `lazy.log.error()`
- 条件付き依存: `if (typeof param === "boolean")` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (!(typeof param === "boolean"))` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("Cache" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (!("Cache" in param))` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("Cookies" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (!("Cookies" in param))` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("Downloads" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (!("Downloads" in param))` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("FormData" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (!("FormData" in param))` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("History" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (!("History" in param))` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("Sessions" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (!("Sessions" in param))` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("SiteSettings" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("OfflineApps" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if (param.Exceptions)` → `lazy.addAllowDenyPermissions()`
- 参照: `manager.getActivePolicies().ClearOnShutdown`, `param.Cache`, `param.Cookies`, `param.Downloads`, `param.Exceptions`, `param.FormData`, `param.History`, `param.Locked`, `param.OfflineApps`, `param.Sessions`, `param.SiteSettings`

## onAllWindowsRestored()
- 位置: L3365-3381
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.runOncePerModification()`
- 条件付き依存: `if (param == "separate")` → `lazy.CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if (param == "separate")` → `lazy.CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if (param == "unified")` → `lazy.CustomizableUI.removeWidgetFromArea()`
- 参照: `lazy.CustomizableUI.AREA_NAVBAR`, `lazy.CustomizableUI.getPlacementOfWidget("urlbar-container") .position`

## onBeforeUIStartup()
- 位置: L3385-3389
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param.PreventInstalls)` → `manager.disallowFeature()`
- 参照: `param.PreventInstalls`

## onAllWindowsRestored()
- 位置: L3390-3498
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.init()`, `lazy.SearchService.init().then()`
- 条件付き依存: `if (param.Remove)` → `lazy.runOncePerModification()`
- 条件付き依存: `if (param.Remove)` → `JSON.stringify()`
- 条件付き依存: `if (param.Remove)` → `lazy.SearchService.getEngineByName()`
- 条件付き依存: `if (engine)` → `lazy.SearchService.removeEngine()`
- 条件付き依存: `if (engine)` → `lazy.reportFailure()`
- 条件付き依存: `if (param.Default)` → `lazy.runOncePerModification()`
- 条件付き依存: `if (param.Default)` → `lazy.SearchService.getEngineByName()`
- 条件付き依存: `if (param.Default)` → `lazy.reportFailure()`
- 条件付き依存: `if (defaultEngine)` → `lazy.SearchService.setDefault()`
- 条件付き依存: `if (defaultEngine)` → `lazy.reportFailure()`
- 条件付き依存: `if (param.DefaultPrivate)` → `lazy.runOncePerModification()`
- 条件付き依存: `if (param.DefaultPrivate)` → `lazy.SearchService.getEngineByName()`
- 条件付き依存: `if (param.DefaultPrivate)` → `lazy.reportFailure()`
- 条件付き依存: `if (defaultPrivateEngine)` → `lazy.SearchService.setDefaultPrivate()`
- 条件付き依存: `if (defaultPrivateEngine)` → `lazy.reportFailure()`
- 参照: `lazy.SearchService.CHANGE_REASON.ENTERPRISE`, `param.Default`, `param.DefaultPrivate`, `param.Remove`

## onBeforeAddons()
- 位置: L3502-3511
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## _onProfileAfterChangeImpl()
- 位置: async L3515-3567
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Cc["@mozilla.org/security/pkcs11moduledb;1"].getService()`, `lazy.log.debug()`, `lazy.reportFailure()`, `pkcs11db.addModule()`, `pkcs11db.listModules()`
- 条件付き依存: `if (param.Delete)` → `pkcs11db.deleteModule()`
- 参照: `Ci.nsIPKCS11ModuleDB`, `module.libName`, `param.Add`, `param.Delete`
- XPCOM: `nsIPKCS11ModuleDB` / `@mozilla.org/security/pkcs11moduledb;1`

## onProfileAfterChange()
- 位置: L3569-3578
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.obs.notifyObservers()`, `this._onProfileAfterChangeImpl()`, `this._onProfileAfterChangeImpl(manager, param).then()`
- XPCOM: `Services.obs`

## onBeforeAddons()
- 位置: L3582-3586
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `manager.disallowFeature()`

## onAllWindowsRestored()
- 位置: L3587-3603
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `lazy.CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if (!homeButtonPlacement)` → `lazy.CustomizableUI.getPlacementOfWidget()`
- 条件付き依存: `if (!homeButtonPlacement)` → `lazy.CustomizableUI.addWidgetToArea()`
- 条件付き依存: `if (!(param))` → `lazy.CustomizableUI.removeWidgetFromArea()`
- 参照: `lazy.CustomizableUI.AREA_NAVBAR`, `placement.position`

## intoMatchPattern()
- 位置: L3617-3632
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD.getBaseDomainFromHost()`, `base.startsWith()`
- 条件付き依存: `if (base.startsWith("*."))` → `base.substring()`
- 条件付き依存: `if (site != base)` → `console.warn()`
- XPCOM: `Services.eTLD`

## validate()
- 位置: L3634-3651
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `patterns.forEach()`
- 条件付き依存: `if (p != "*")` → `this.intoMatchPattern()`
- 参照: `param.Exceptions`, `param.Match`

## featuresForPolicies()
- 位置: L3653-3669
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `features.http`, `features.jit`, `features.serviceworkers`, `policies.DisableJit`, `policies.DisableServiceWorkers`, `policies.HttpsOnly`

## onMissing()
- 位置: L3673-3675
- 役割: (未記入)
- 触るとき: (未記入)

## onBeforeAddons()
- 位置: L3677-3773
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cis.getPolicyIdentities()`, `cis.removePolicyIdentity()`, `exceptions.includes()`, `exceptions.map()`, `manager.updateSitePolicies()`, `matches.includes()`, `policyContainerMap.set()`, `policyContainerMap.values()`, `sitePolicies.push()`, `this.featuresForPolicies()`
- 条件付き依存: `if (!(!matches.length || matches.includes("*")))` → `matches.map()`
- 条件付き依存: `if (!(!matches.length || matches.includes("*")))` → `matchPatterns.filter()`
- 条件付き依存: `if (!(!matches.length || matches.includes("*")))` → `exceptionPatterns.some()`
- 条件付き依存: `if ("Container" in policies.Policies)` → `policyContainerMap.get()`
- 条件付き依存: `if (!userContextId)` → `cis.createForPolicy()`
- 条件付き依存: `if (!userContextId)` → `policyContainerMap.set()`
- 条件付き依存: `if (!(!userContextId))` → `unseenContainers.delete()`
- 条件付き依存: `if (policies.Policies.Container.ephemeral)` → `ephemeralUserContextIds.add()`
- 条件付き依存: `if (hasContainerPolicy)` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (ephemeralUserContextIds.size > 0)` → `lazy.EphemeralContainerWatcher.init()`
- 条件付き依存: `if (!(ephemeralUserContextIds.size > 0))` → `lazy.EphemeralContainerWatcher.destroy()`
- 条件付き依存: `if (!(hasContainerPolicy))` → `lazy.EphemeralContainerWatcher.destroy()`
- 参照: `cis.createForPolicy(containerId).userContextId`, `ephemeralUserContextIds.size`, `exceptionPattern.pattern`, `features.container`, `identity.policyId`, `identity.userContextId`, `lazy.ContextualIdentityService`, `matchPattern.pattern`, `matchPatterns.length`, `matches.length`, `policies.Exceptions`, `policies.Match`, `policies.Policies`, `policies.Policies.Container.ephemeral`, `policies.Policies.Container.id`, `this.intoMatchPattern`

## onBeforeAddons()
- 位置: L3777-3785
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param)` → `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (param)` → `Date.now().toString()`
- 条件付き依存: `if (param)` → `Date.now()`

## onBeforeAddons()
- 位置: L3789-3806
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L3810-3827
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L3831-3836
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onProfileAfterChange()
- 位置: L3840-3842
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `manager.setSupportMenu()`

## onBeforeAddons()
- 位置: L3846-3859
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.policies.getActivePolicies()`, `lazy.PoliciesUtils.setAndLockPref()`
- 条件付き依存: `if (policies.AIControls?.Translations || policies.AIControls?.Default)` → `lazy.log.warn()`
- 参照: `policies.AIControls?.Default`, `policies.AIControls?.Translations`
- XPCOM: `Services.policies`

## onBeforeAddons()
- 位置: L3863-3916
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ("ExtensionRecommendations" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("FeatureRecommendations" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("FeatureRecommendations" in param)` → `Services.locale.acceptLanguages .split(",")[0] .trim()`
- 条件付き依存: `if ("FeatureRecommendations" in param)` → `Services.locale.acceptLanguages .split()`
- 条件付き依存: `if ("UrlbarInterventions" in param && !param.UrlbarInterventions)` → `manager.disallowFeature()`
- 条件付き依存: `if ("SkipOnboarding" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("MoreFromMozilla" in param)` → `lazy.PoliciesUtils.setDefaultPref()`
- 条件付き依存: `if ("FirefoxLabs" in param && !param.FirefoxLabs)` → `manager.disallowFeature()`
- 参照: `Services.locale.appLocaleAsBCP47`, `param.ExtensionRecommendations`, `param.FeatureRecommendations`, `param.FirefoxLabs`, `param.Locked`, `param.MoreFromMozilla`, `param.SkipOnboarding`, `param.UrlbarInterventions`, `topWebPreferredLanguage.length`
- XPCOM: `Services.locale`

## onBeforeAddons()
- 位置: L3920-3922
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L3926-3931
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeUIStartup()
- 位置: L3935-3937
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.WebsiteFilter.init()`
- 参照: `param.Block`, `param.Exceptions`

## onBeforeAddons()
- 位置: L3941-3946
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`

## onBeforeAddons()
- 位置: L3950-3952
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PoliciesUtils.setAndLockPref()`
