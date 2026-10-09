# nsIWeakReference (xpcom/base/nsIWeakReference.idl)

source: xpcom/base/nsIWeakReference.idl
source-hash: 7c54c078c9a910c33462295d59b8ab1e7818a74b

- 継承: nsISupports
- 役割: An instance of |nsIWeakReference| is a proxy object that cooperates with
- 実装: (未記入)

## メソッド / 属性
- `void QueryReferent(nsIIDRef uuid, nsQIResult result)`: |QueryReferent| queries the referent, if it exists, and like |QueryInterface|, produces
- `size_t sizeOfOnlyThis(MallocSizeOf aMallocSizeOf)`: (未記入)

# nsISupportsWeakReference (xpcom/base/nsIWeakReference.idl)

source: xpcom/base/nsIWeakReference.idl
source-hash: 7c54c078c9a910c33462295d59b8ab1e7818a74b

- 継承: nsISupports
- 役割: |nsISupportsWeakReference| is a factory interface which produces appropriate
- 実装: (未記入)
- 使っているJS: [`browser/components/tabbrowser/content/split-view-footer.js`](../../browser/components/tabbrowser/content/split-view-footer.js.md)

## メソッド / 属性
- `nsIWeakReference GetWeakReference()`: |GetWeakReference| produces an appropriate instance of |nsIWeakReference|.
