# nsIConsoleAPIStorage (dom/console/nsIConsoleAPIStorage.idl)

source: dom/console/nsIConsoleAPIStorage.idl
source-hash: 0736b28275a113d71f636665656fabeecd623677

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/enterprisepolicies/content/aboutPolicies.js`](../../browser/components/enterprisepolicies/content/aboutPolicies.js.md)

## メソッド / 属性
- `jsval getEvents(AString aId)`: Get the events array by inner window ID or all events from all windows.
- `void addLogEventListener(jsval aListener, nsIPrincipal aPrincipal)`: Adds a listener to be notified of log events.
- `void removeLogEventListener(jsval aListener)`: Removes a listener added with `addLogEventListener`.
- `void recordEvent(AString aId, jsval aEvent)`: Record an event associated with the given window ID.
- `void clearEvents(AString aId)`: Clear storage data for the given window.
