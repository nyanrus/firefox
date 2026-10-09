# nsIChannel (netwerk/base/nsIChannel.idl)

source: netwerk/base/nsIChannel.idl
source-hash: b8985434483ccc45de01411abd6210c74f1d3922

- 継承: nsIRequest
- 役割: The nsIChannel interface allows clients to construct "GET" requests for
- 実装: (未記入)
- 使っているJS: [`browser/components/tabbrowser/Tabbrowser.sys.mjs`](../../browser/components/tabbrowser/Tabbrowser.sys.mjs.md)

## メソッド / 属性
- `attribute nsIURI originalURI`: The original URI used to construct the channel. This is used in
- `readonly attribute nsIURI URI`: The URI corresponding to the channel.  Its value is immutable.
- `attribute nsISupports owner`: The owner, corresponding to the entity that is responsible for this
- `attribute nsIInterfaceRequestor notificationCallbacks`: The notification callbacks for the channel.  This is set by clients, who
- `readonly attribute nsITransportSecurityInfo securityInfo`: Transport-level security information (if any) corresponding to the
- `attribute ACString contentType`: The MIME type of the channel's content if available.
- `attribute ACString contentCharset`: The character set of the channel's content if available and if applicable.
- `attribute int64_t contentLength`: The length of the data associated with the channel if available.  A value
- `nsIInputStream open()`: Synchronously open the channel.
- `void asyncOpen(nsIStreamListener aListener)`: Asynchronously open this channel.  Data is fed to the specified stream
- `readonly attribute boolean canceled`: True if the channel has been canceled.
- `const unsigned long LOAD_DOCUMENT_URI`: Channel specific load flags:
- `const unsigned long LOAD_RETARGETED_DOCUMENT_URI`: If the end consumer for this load has been retargeted after discovering
- `const unsigned long LOAD_REPLACE`: This flag is set to indicate that this channel is replacing another
- `const unsigned long LOAD_INITIAL_DOCUMENT_URI`: Set (e.g., by the docshell) to indicate whether or not the channel
- `const unsigned long LOAD_TARGETED`: Set (e.g., by the URILoader) to indicate whether or not the end consumer
- `const unsigned long LOAD_CALL_CONTENT_SNIFFERS`: If this flag is set, the channel should call the content sniffers as
- `const unsigned long LOAD_BYPASS_URL_CLASSIFIER`: This flag tells the channel to bypass URL classifier service check
- `const unsigned long LOAD_MEDIA_SNIFFER_OVERRIDES_CONTENT_TYPE`: If this flag is set, the media-type content sniffer will be allowed
- `const unsigned long LOAD_EXPLICIT_CREDENTIALS`: Set to let explicitely provided credentials be used over credentials
- `const unsigned long LOAD_BYPASS_SERVICE_WORKER`: Set to force bypass of any service worker interception of the channel.
- `attribute unsigned long contentDisposition`: Access to the type implied or stated by the Content-Disposition header
- `const unsigned long DISPOSITION_INLINE`: (未記入)
- `const unsigned long DISPOSITION_ATTACHMENT`: (未記入)
- `const unsigned long DISPOSITION_FORCE_INLINE`: (未記入)
- `attribute AString contentDispositionFilename`: Access to the filename portion of the Content-Disposition header if
- `readonly attribute ACString contentDispositionHeader`: Access to the raw Content-Disposition header if available and applicable.
- `attribute nsILoadInfo loadInfo`: The LoadInfo object contains information about a network load, why it
- `readonly attribute boolean isDocument`: Returns true if the channel is used to create a document.
- `attribute ParentProcessChannelHandle parentProcessChannelHandle`: Associate a ParentProcessChannelHandle with this channel.

# nsIIdentChannel (netwerk/base/nsIChannel.idl)

source: netwerk/base/nsIChannel.idl
source-hash: b8985434483ccc45de01411abd6210c74f1d3922

- 継承: nsIChannel
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `attribute uint64_t channelId`: Unique ID of the channel, shared between parent and child. Needed if
