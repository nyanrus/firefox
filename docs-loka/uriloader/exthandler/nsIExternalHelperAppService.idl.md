# nsIExternalHelperAppService (uriloader/exthandler/nsIExternalHelperAppService.idl)

source: uriloader/exthandler/nsIExternalHelperAppService.idl
source-hash: f5c40986adad5a9354d1ef1b86e058c83064a7f6

- 継承: nsISupports
- 役割: The external helper app service is used for finding and launching
- 実装: (未記入)
- 使っているJS: [`browser/base/content/nsContextMenu.sys.mjs`](../../browser/base/content/nsContextMenu.sys.mjs.md)

## メソッド / 属性
- `nsIStreamListener doContent(ACString aMimeContentType, nsIChannel aChannel, nsIInterfaceRequestor aContentContext, boolean aForceSave, nsIInterfaceRequestor aWindowContext)`: Binds an external helper application to a stream listener. The caller
- `nsIStreamListener createListener(ACString aMimeContentType, nsIChannel aChannel, BrowsingContext aContentContext, boolean aForceSave, nsIInterfaceRequestor aWindowContext)`: Binds an external helper application to a stream listener. The caller
- `boolean applyDecodingForExtension(AUTF8String aExtension, ACString aEncodingType)`: Returns true if data from a URL with this extension combination
- `nsIFile getPreferredDownloadsDirectory()`: Returns the current downloads directory, given the current preferences. May

# nsPIExternalAppLauncher (uriloader/exthandler/nsIExternalHelperAppService.idl)

source: uriloader/exthandler/nsIExternalHelperAppService.idl
source-hash: f5c40986adad5a9354d1ef1b86e058c83064a7f6

- 継承: nsISupports
- 役割: This is a private interface shared between external app handlers and the platform specific
- 実装: (未記入)

## メソッド / 属性
- `void deleteTemporaryFileOnExit(nsIFile aTemporaryFile)`: mscott --> eventually I should move this into a new service so other
- `void deleteTemporaryPrivateFileWhenPossible(nsIFile aTemporaryFile)`: Delete a temporary file created inside private browsing mode when
- `void deletePrivateFileWhenPossible(nsIFile aPrivateFile)`: Delete a file downloaded inside private browsing mode when

# nsIHelperAppLauncher (uriloader/exthandler/nsIExternalHelperAppService.idl)

source: uriloader/exthandler/nsIExternalHelperAppService.idl
source-hash: f5c40986adad5a9354d1ef1b86e058c83064a7f6

- 継承: nsICancelable
- 役割: A helper app launcher is a small object created to handle the launching
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute nsIMIMEInfo MIMEInfo`: The mime info object associated with the content type this helper app
- `readonly attribute nsIURI source`: The source uri
- `readonly attribute AString suggestedFileName`: The suggested name for this file
- `void promptForSaveDestination()`: Saves the final destination of the file.
- `void setDownloadToLaunch(boolean aHandleInternally, nsIFile aFile)`: Tell the launcher that we will want to open the file.
- `void launchLocalFile()`: Use the MIMEInfo associated with us to open a file that is already local.
- `void saveDestinationAvailable(nsIFile aFile, boolean aDialogWasShown)`: Callback invoked by nsIHelperAppLauncherDialog::promptForSaveToFileAsync
- `void setWebProgressListener(nsIWebProgressListener2 aWebProgressListener)`: The following methods are used by the progress dialog to get or set
- `readonly attribute nsIFile targetFile`: The file we are saving to
- `readonly attribute boolean targetFileIsExecutable`: The executable-ness of the target file
- `readonly attribute PRTime timeDownloadStarted`: Time when the download started
- `readonly attribute int64_t contentLength`: The download content length, or -1 if the length is not available.
- `readonly attribute uint64_t browsingContextId`: The browsingContext ID of the launcher's source
