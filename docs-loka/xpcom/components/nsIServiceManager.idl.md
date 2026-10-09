# nsIServiceManager (xpcom/components/nsIServiceManager.idl)

source: xpcom/components/nsIServiceManager.idl
source-hash: e327b49d793b3b0894e83772427e793144e826fc

- 継承: nsISupports
- 役割: The nsIServiceManager manager interface provides a means to obtain
- 実装: (未記入)
- 使っているJS: [`browser/components/StartupRecorder.sys.mjs`](../../browser/components/StartupRecorder.sys.mjs.md)

## メソッド / 属性
- `void getService(nsCIDRef aClass, nsIIDRef aIID, nsQIResult result)`: getServiceByContractID
- `void getServiceByContractID(string aContractID, nsIIDRef aIID, nsQIResult result)`: (未記入)
- `boolean isServiceInstantiated(nsCIDRef aClass, nsIIDRef aIID)`: isServiceInstantiated
- `boolean isServiceInstantiatedByContractID(string aContractID, nsIIDRef aIID)`: (未記入)
