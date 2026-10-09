# browser/components/enterprisepolicies/helpers/ProxyPolicies.sys.mjs

source: browser/components/enterprisepolicies/helpers/ProxyPolicies.sys.mjs
source-hash: a08094ab4e2dcd6ecff890b8ffaebb7b5b028d8a
lines: 149

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`

## reportFailure()
- 位置: L59-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PolicyFailures.report()`, `lazy.log.error()`

## configureProxySettings()
- 位置: L65-147
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (param.Mode)` → `setPref()`
- 条件付き依存: `if (param.Mode)` → `PROXY_TYPES_MAP.get()`
- 条件付き依存: `if (param.AutoConfigURL)` → `setPref()`
- 条件付き依存: `if (param.UseProxyForDNS !== undefined)` → `setPref()`
- 条件付き依存: `if (param.AutoLogin !== undefined)` → `setPref()`
- 条件付き依存: `if (param.SOCKSVersion != 4 && param.SOCKSVersion != 5)` → `lazy.log.error()`
- 条件付き依存: `if (!(param.SOCKSVersion != 4 && param.SOCKSVersion != 5))` → `setPref()`
- 条件付き依存: `if (param.Passthrough !== undefined)` → `setPref()`
- 条件付き依存: `if (param.UseHTTPProxyForAllProtocols !== undefined)` → `setPref()`
- 条件付き依存: `if (param.FTPProxy)` → `lazy.log.warn()`
- 条件付き依存: `if (param.HTTPProxy)` → `setProxyHostAndPort()`
- 条件付き依存: `if (param.SSLProxy)` → `setProxyHostAndPort()`
- 条件付き依存: `if (param.SOCKSProxy)` → `setProxyHostAndPort()`
- 条件付き依存: `if (param.Locked)` → `Services.prefs.lockPref()`
- 参照: `param.AutoConfigURL`, `param.AutoConfigURL.href`, `param.AutoLogin`, `param.FTPProxy`, `param.HTTPProxy`, `param.Locked`, `param.Mode`, `param.Passthrough`, `param.SOCKSProxy`, `param.SOCKSVersion`, `param.SSLProxy`, `param.UseHTTPProxyForAllProtocols`, `param.UseProxyForDNS`
- XPCOM: `Services.prefs`

## setProxyHostAndPort()
- 位置: L106-119
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `setPref()`
- 条件付き依存: `if (!url)` → `reportFailure()`
- 条件付き依存: `if (url.port)` → `setPref()`
- 条件付き依存: `if (url.port)` → `Number()`
- 参照: `url.hostname`, `url.port`
