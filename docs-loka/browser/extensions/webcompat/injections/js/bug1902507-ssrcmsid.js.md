# browser/extensions/webcompat/injections/js/bug1902507-ssrcmsid.js

source: browser/extensions/webcompat/injections/js/bug1902507-ssrcmsid.js
source-hash: b9e9d586a695ed27df22ea4739b227ab2277b672
lines: 137

## <module>
- 役割: (未記入)

## addSsrcMsidLines()
- 位置: L23-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `sdp.split()`, `section.match()`, `section.replace()`
- 参照: `parts.length`, `sdp.length`

## createOffer()
- 位置: async L62-70
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `nativeCreateOffer.apply()`
- 条件付き依存: `if (description && typeof description.sdp == "string")` → `addSsrcMsidLines()`
- 参照: `description.sdp`

## createAnswer()
- 位置: async L74-82
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `nativeCreateAnswer.apply()`
- 条件付き依存: `if (description && typeof description.sdp == "string")` → `addSsrcMsidLines()`
- 参照: `description.sdp`

## get()
- 位置: L104-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `nativeLocalDescription.get.call()`
- 条件付き依存: `if (desc && typeof desc.sdp == "string")` → `addSsrcMsidLines()`
- 参照: `desc.sdp`, `desc.type`

## get()
- 位置: L126-132
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `nativeRemoteDescription.get.call()`
- 条件付き依存: `if (desc && typeof desc.sdp == "string")` → `addSsrcMsidLines()`
- 参照: `desc.sdp`, `desc.type`
