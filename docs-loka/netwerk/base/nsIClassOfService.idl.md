# nsIClassOfService (netwerk/base/nsIClassOfService.idl)

source: netwerk/base/nsIClassOfService.idl
source-hash: 84c19374f7eede256783fc0caebf0b340fcf6292

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/modules/FaviconLoader.sys.mjs`](../../browser/modules/FaviconLoader.sys.mjs.md)

## メソッド / 属性
- `attribute unsigned long classFlags`: (未記入)
- `attribute boolean incremental`: (未記入)
- `void clearClassFlags(unsigned long flags)`: (未記入)
- `void addClassFlags(unsigned long flags)`: (未記入)
- `void setClassOfService(ClassOfService s)`: (未記入)
- `attribute nsIClassOfService_FetchPriority fetchPriority`: (未記入)
- `void setFetchPriorityDOM(FetchPriorityDOM aPriority)`: (未記入)
- `const unsigned long Leader`: (未記入)
- `const unsigned long Follower`: (未記入)
- `const unsigned long Speculative`: (未記入)
- `const unsigned long Background`: (未記入)
- `const unsigned long Unblocked`: (未記入)
- `const unsigned long Throttleable`: (未記入)
- `const unsigned long UrgentStart`: (未記入)
- `const unsigned long DontThrottle`: (未記入)
- `const unsigned long Tail`: (未記入)
- `const unsigned long TailAllowed`: (未記入)
- `const unsigned long TailForbidden`: (未記入)
