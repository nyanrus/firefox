# nsIDOMProcessParent (dom/ipc/nsIDOMProcessParent.idl)

source: dom/ipc/nsIDOMProcessParent.idl
source-hash: 272f222671252aaad2d1a82903687c3d328f58df

- 継承: nsISupports
- 役割: Parent actor interface for a process which can host DOM content.
- 実装: (未記入)
- 使っているJS: [`browser/components/newtab/AboutHomeStartupCache.sys.mjs`](../../browser/components/newtab/AboutHomeStartupCache.sys.mjs.md)

## メソッド / 属性
- `readonly attribute unsigned long long childID`: Internal child process ID. `0` is reserved for the parent process.
- `readonly attribute long osPid`: OS ID of the process.
- `JSProcessActorParent getActor(ACString name)`: Lookup a JSProcessActorParent managed by this interface by name.
- `JSProcessActorParent getExistingActor(ACString name)`: (未記入)
- `readonly attribute boolean canSend`: Can the actor still send messages?
- `ContentParentPtr AsContentParent()`: (未記入)
- `JSActorManagerPtr AsJSActorManager()`: Cast this nsIDOMProcessParent to a JSActorManager
- `void aboutToLoadOrigin(nsIPrincipal principal)`: Called when we are about to load an origin within a content process.
- `readonly attribute ACString remoteType`: Remote type of the process.
- `boolean validatePrincipal(nsIPrincipal principal)`: (未記入)

# nsIContentParentKeepAlive (dom/ipc/nsIDOMProcessParent.idl)

source: dom/ipc/nsIDOMProcessParent.idl
source-hash: 272f222671252aaad2d1a82903687c3d328f58df

- 継承: nsISupports
- 役割: Reference counted and cycle collected interface to expose a
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute nsIDOMProcessParent domProcess`: Underlying nsIDOMProcessParent which is being kept alive.
- `void invalidateKeepAlive()`: Invalidate this nsIContentParentKeepAlive, dropping the keep alive
