# browser/actors/DecoderDoctorChild.sys.mjs

source: browser/actors/DecoderDoctorChild.sys.mjs
source-hash: 30ebc07e2743d77e4e19fb1dd78d5c1659208b99
lines: 27

## <module>
- 役割: Decoder Doctor 通知のコンテンツ側アクター。デコーダーの問題通知を親へそのまま転送する。

## DecoderDoctorChild.observe()
- 位置: L23-25
- 役割: decoder-doctor-notification の JSON データを、そのまま DecoderDoctor:Notification として親へ送る。
- 触るとき: 再生問題の通知が親のインフォバーに届かないときに見る。
- 呼び出し先: `this.sendAsyncMessage()`
