# browser/components/webrtc/content/webrtc-preview/webrtc-preview.stories.mjs

source: browser/components/webrtc/content/webrtc-preview/webrtc-preview.stories.mjs
source-hash: 710e66180c664b053536b777af63bb3f30100a5d
lines: 97

## <module>
- 役割: (未記入)
- 呼び出し先: `Template.bind()`, `getDeviceId()`, `window.MozXULElement.insertFTLIfNeeded()`

## Template()
- 位置: L31-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 条件付き依存: `if (!deviceId)` → `html()`
- 参照: `args.deviceId`, `args.mediaSource`, `args.showPreviewControlButtons`, `context?.loaded?.deviceId`

## getDeviceId()
- 位置: async L59-80
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `console.warn()`, `navigator.mediaDevices.getUserMedia()`, `stream.getTracks()`, `stream.getTracks().forEach()`, `stream.getVideoTracks()`, `track.stop()`, `videoTrack.getSettings()`
- 参照: `videoTrack.getSettings().deviceId`

## Camera.play()
- 位置: async L94-96
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `args.deviceId`, `loaded.deviceId`
