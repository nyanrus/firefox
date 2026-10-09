# nsIImageLoadingContent (dom/base/nsIImageLoadingContent.idl)

source: dom/base/nsIImageLoadingContent.idl
source-hash: 30378305c79a931a22be6e85f148ebbea775e418

- 継承: imgINotificationObserver
- 役割: This interface represents a content node that loads images.  The interface
- 実装: (未記入)
- 使っているJS: [`browser/actors/ContextMenuChild.sys.mjs`](../../browser/actors/ContextMenuChild.sys.mjs.md), [`browser/actors/PageInfoChild.sys.mjs`](../../browser/actors/PageInfoChild.sys.mjs.md)

## メソッド / 属性
- `const long UNKNOWN_REQUEST`: Request types.  Image loading content nodes attempt to do atomic
- `const long CURRENT_REQUEST`: (未記入)
- `const long PENDING_REQUEST`: (未記入)
- `void setLoadingEnabled(boolean aEnabled)`: setLoadingEnabled is used to enable and disable loading in
- `void addNativeObserver(imgINotificationObserver aObserver)`: Used to register an image decoder observer.  Typically, this will
- `void removeNativeObserver(imgINotificationObserver aObserver)`: Used to unregister an image decoder observer.
- `imgIRequest getRequest(long aRequestType)`: Accessor to get the image requests
- `void frameCreated(nsIFrame aFrame)`: Used to notify the image loading content node that a frame has been
- `void frameDestroyed(nsIFrame aFrame)`: Used to notify the image loading content node that a frame has been
- `long getRequestType(imgIRequest aRequest)`: Used to find out what type of request one is dealing with (eg
- `readonly attribute nsIURI currentURI`: Gets the URI of the current request, if available.
- `readonly attribute boolean syncDecodingHint`: Gets the sync-decoding hint set by the decoding attribute.
- `nsIStreamListener loadImageWithChannel(nsIChannel aChannel)`: loadImageWithChannel allows data from an existing channel to be
- `void onVisibilityChange(Visibility aNewVisibility, MaybeOnNonvisible aNonvisibleAction)`: Called by layout to announce when the frame associated with this content
