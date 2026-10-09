# nsIMLUtils (toolkit/components/ml/nsIMLUtils.idl)

source: toolkit/components/ml/nsIMLUtils.idl
source-hash: e6f6c9bcdd8c6012f0128a75ff819319c5d90232

- 継承: nsISupports
- 役割: (未記入)
- 実装: `mozilla::ml::MLUtils` (toolkit/components/ml/components.conf)
- contract ID: `@mozilla.org/ml-utils;1`
- 使っているJS: [`browser/components/aiwindow/ui/modules/AutoTabGroupingSuggestions.sys.mjs`](../../../browser/components/aiwindow/ui/modules/AutoTabGroupingSuggestions.sys.mjs.md), [`browser/components/genai/LinkPreview.sys.mjs`](../../../browser/components/genai/LinkPreview.sys.mjs.md)

## メソッド / 属性
- `readonly attribute unsigned long long totalPhysicalMemory`: (未記入)
- `readonly attribute unsigned long long availablePhysicalMemory`: (未記入)
- `octet getOptimalCPUConcurrency()`: Computes the optimal concurrency level for ML workloads on the CPU.
- `boolean canUseLlamaCpp()`: Checks llama.cpp is usable. This always returns true on aarch64.
