# nsIUpdateTimerManager (toolkit/components/timermanager/nsIUpdateTimerManager.idl)

source: toolkit/components/timermanager/nsIUpdateTimerManager.idl
source-hash: 2544944cc715b793d65b07dd1c91ca3280998ed2

- 継承: nsISupports
- 役割: An interface describing a global application service that allows long
- 実装: (未記入)
- 使っているJS: [`browser/components/urlbar/private/SuggestBackendRust.sys.mjs`](../../../browser/components/urlbar/private/SuggestBackendRust.sys.mjs.md)

## メソッド / 属性
- `void registerTimer(AString id, nsITimerCallback callback, unsigned long interval, boolean skipFirst)`: Register an interval with the timer manager. The timer manager
- `void unregisterTimer(AString id)`: Unregister an existing interval from the timer manager.
