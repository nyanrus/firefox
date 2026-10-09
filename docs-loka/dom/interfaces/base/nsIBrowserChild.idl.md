# nsIBrowserChild (dom/interfaces/base/nsIBrowserChild.idl)

source: dom/interfaces/base/nsIBrowserChild.idl
source-hash: 3ac63a984ad87444ddc4ff0c99229c1394a4225c

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute ContentFrameMessageManager messageManager`: (未記入)
- `void sendRequestFocus(boolean canFocus, CallerType aCallerType)`: (未記入)
- `void remoteDropLinks(Array<nsIDroppedLinkItem> links)`: (未記入)
- `Promise contentTransformsReceived()`: Resolved after content has received a PBrowser::ChildToParentMatrix.
- `readonly attribute uint64_t tabId`: (未記入)
- `void notifyNavigationFinished()`: Send a message from the BrowserChild to the BrowserParent that a
- `readonly attribute uint64_t chromeOuterWindowID`: Id of the chrome window the tab is within.
