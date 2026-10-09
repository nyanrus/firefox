# nsIOSPermissionRequest (dom/system/nsIOSPermissionRequest.idl)

source: dom/system/nsIOSPermissionRequest.idl
source-hash: d524564add2b61a712349dbad4924f4bf6c0c751

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/actors/WebRTCParent.sys.mjs`](../../browser/actors/WebRTCParent.sys.mjs.md)

## メソッド / 属性
- `const uint16_t PERMISSION_STATE_NOTDETERMINED`: (未記入)
- `const uint16_t PERMISSION_STATE_RESTRICTED`: (未記入)
- `const uint16_t PERMISSION_STATE_DENIED`: (未記入)
- `const uint16_t PERMISSION_STATE_AUTHORIZED`: (未記入)
- `void getMediaCapturePermissionState(uint16_t aVideo, uint16_t aAudio)`: (未記入)
- `void getAudioCapturePermissionState(uint16_t aAudio)`: (未記入)
- `void getVideoCapturePermissionState(uint16_t aVideo)`: (未記入)
- `void getScreenCapturePermissionState(uint16_t aScreen)`: (未記入)
- `Promise requestVideoCapturePermission()`: (未記入)
- `Promise requestAudioCapturePermission()`: (未記入)
- `void maybeRequestScreenCapturePermission()`: (未記入)
