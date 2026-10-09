# nsIPrivateBrowsingChannel (netwerk/base/nsIPrivateBrowsingChannel.idl)

source: netwerk/base/nsIPrivateBrowsingChannel.idl
source-hash: 196feffd58c8f42aa5bcad9c5fa4918f2e2fd1f5

- 継承: nsISupports
- 役割: This interface is implemented by channels which support overriding the
- 実装: (未記入)
- 使っているJS: [`browser/base/content/nsContextMenu.sys.mjs`](../../browser/base/content/nsContextMenu.sys.mjs.md), [`browser/modules/WindowsPreviewPerTab.sys.mjs`](../../browser/modules/WindowsPreviewPerTab.sys.mjs.md)

## メソッド / 属性
- `void setPrivate(boolean aPrivate)`: Determine whether the channel is tied to a private browsing window.
- `readonly attribute boolean isChannelPrivate`: States whether the channel is in private browsing mode. This may either
- `boolean isPrivateModeOverriden(boolean aValue)`: (未記入)
