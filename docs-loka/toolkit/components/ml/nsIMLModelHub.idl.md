# nsIMLModelDownloadProgressCallback (toolkit/components/ml/nsIMLModelHub.idl)

source: toolkit/components/ml/nsIMLModelHub.idl
source-hash: 25f23edfa19eeaddc8e91cedf26a30ea5f905561

- 継承: nsISupports
- 役割: Callback interface for receiving progress updates during model download
- 実装: (未記入)

## メソッド / 属性
- `void onProgress(long aProgress, long long aCurrentLoaded, long long aTotalLoaded, long long aTotal)`: Called to report download progress

# nsIMLModelDownloadCompletionCallback (toolkit/components/ml/nsIMLModelHub.idl)

source: toolkit/components/ml/nsIMLModelHub.idl
source-hash: 25f23edfa19eeaddc8e91cedf26a30ea5f905561

- 継承: nsISupports
- 役割: Callback interface for receiving completion notification after model download
- 実装: (未記入)

## メソッド / 属性
- `void onSuccess(AString aModel, AString aRevision)`: Called when model download completes successfully
- `void onError(AString aError)`: Called when model download fails

# nsIMLModelHub (toolkit/components/ml/nsIMLModelHub.idl)

source: toolkit/components/ml/nsIMLModelHub.idl
source-hash: 25f23edfa19eeaddc8e91cedf26a30ea5f905561

- 継承: nsISupports
- 役割: A service for checking model availability and downloading models
- 実装: (未記入)
- 使っているJS: [`browser/modules/PermissionUI.sys.mjs`](../../../browser/modules/PermissionUI.sys.mjs.md)

## メソッド / 属性
- `Promise isModelAvailable(AUTF8String aEngineId, AUTF8String aModel, AUTF8String aRevision, AUTF8String aFilename)`: Check if a model is available (either cached or downloadable)
- `Promise isModelInstalled(AUTF8String aEngineId, AUTF8String aModel, AUTF8String aRevision, AUTF8String aFilename)`: Check if a model is already downloaded to the local cache. Unlike
- `AString downloadModel(AUTF8String aEngineId, AUTF8String aTaskName, AUTF8String aModel, AUTF8String aRevision, Array<AUTF8String> aFiles, AString aProgressToken, nsIMLModelDownloadProgressCallback aProgressCallback, nsIMLModelDownloadCompletionCallback aCompletionCallback)`: Download a model with progress and completion callbacks
- `void cancelDownload(AString aProgressToken)`: Cancel the in-progress download previously started by downloadModel()
- `Promise getModelBlob(AUTF8String aEngineId, AUTF8String aTaskName, AUTF8String aModel, AUTF8String aRevision, AUTF8String aFile)`: Get a blob for a downloaded model file
