# nsIMediaManagerService (dom/media/nsIMediaManager.idl)

source: dom/media/nsIMediaManager.idl
source-hash: 68334b2e6af22c3b6d030ee992cbecf9fdc28845

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/actors/WebRTCChild.sys.mjs`](../../browser/actors/WebRTCChild.sys.mjs.md), [`browser/base/content/browser-sitePermissionPanel.js`](../../browser/base/content/browser-sitePermissionPanel.js.md), [`browser/modules/webrtcUI.sys.mjs`](../../browser/modules/webrtcUI.sys.mjs.md)

## メソッド / 属性
- `readonly attribute nsIArray activeMediaCaptureWindows`: (未記入)
- `const unsigned short STATE_NOCAPTURE`: (未記入)
- `const unsigned short STATE_CAPTURE_ENABLED`: (未記入)
- `const unsigned short STATE_CAPTURE_DISABLED`: (未記入)
- `void mediaCaptureWindowState(nsIDOMWindow aWindow, unsigned short aCamera, unsigned short aMicrophone, unsigned short aScreenShare, unsigned short aWindowShare, unsigned short aBrowserShare, Array<nsIMediaDevice> devices)`: (未記入)
- `void sanitizeDeviceIds(long long sinceWhen)`: (未記入)
