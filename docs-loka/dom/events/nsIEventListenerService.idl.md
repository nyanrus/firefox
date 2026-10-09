# nsIEventListenerChange (dom/events/nsIEventListenerService.idl)

source: dom/events/nsIEventListenerService.idl
source-hash: 18c33e5f56926251893a5e0b409a2dd4e67b0511

- 継承: nsISupports
- 役割: Contains an event target along with a count of event listener changes
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute EventTarget target`: (未記入)
- `readonly attribute uint32_t countOfEventListenerChangesAffectingAccessibility`: (未記入)

# nsIListenerChangeListener (dom/events/nsIEventListenerService.idl)

source: dom/events/nsIEventListenerService.idl
source-hash: 18c33e5f56926251893a5e0b409a2dd4e67b0511

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void listenersChanged(nsIArray aEventListenerChanges)`: (未記入)

# nsIEventListenerInfo (dom/events/nsIEventListenerService.idl)

source: dom/events/nsIEventListenerService.idl
source-hash: 18c33e5f56926251893a5e0b409a2dd4e67b0511

- 継承: nsISupports
- 役割: An instance of this interface describes how an event listener
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute AString type`: The type of the event for which the listener was added.
- `readonly attribute boolean capturing`: (未記入)
- `readonly attribute boolean allowsUntrusted`: (未記入)
- `readonly attribute boolean inSystemEventGroup`: (未記入)
- `attribute boolean enabled`: Changing the enabled state works only with listeners implemented in
- `readonly attribute jsval listenerObject`: The underlying JS object of the event listener, if this listener
- `AString toSource()`: Tries to serialize event listener to a string.

# nsIEventListenerService (dom/events/nsIEventListenerService.idl)

source: dom/events/nsIEventListenerService.idl
source-hash: 18c33e5f56926251893a5e0b409a2dd4e67b0511

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `Array<nsIEventListenerInfo> getListenerInfoFor(EventTarget aEventTarget)`: Returns an array of nsIEventListenerInfo objects.
- `boolean hasListenersFor(EventTarget aEventTarget, AString aType)`: Returns true if a event target has any listener for the given type.
- `void addListenerForAllEvents(EventTarget target, jsval listener, boolean aUseCapture, boolean aWantsUntrusted, boolean aSystemEventGroup)`: (未記入)
- `void removeListenerForAllEvents(EventTarget target, jsval listener, boolean aUseCapture, boolean aSystemEventGroup)`: (未記入)
- `void addListenerChangeListener(nsIListenerChangeListener aListener)`: (未記入)
- `void removeListenerChangeListener(nsIListenerChangeListener aListener)`: (未記入)
