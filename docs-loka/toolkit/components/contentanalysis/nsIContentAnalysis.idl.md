# nsIContentAnalysisAcknowledgement (toolkit/components/contentanalysis/nsIContentAnalysis.idl)

source: toolkit/components/contentanalysis/nsIContentAnalysis.idl
source-hash: 0cf288d2a2cc7870394c0acca8f73e067862cf37

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute nsIContentAnalysisAcknowledgement_Result result`: (未記入)
- `readonly attribute nsIContentAnalysisAcknowledgement_FinalAction finalAction`: (未記入)

# nsIContentAnalysisResult (toolkit/components/contentanalysis/nsIContentAnalysis.idl)

source: toolkit/components/contentanalysis/nsIContentAnalysis.idl
source-hash: 0cf288d2a2cc7870394c0acca8f73e067862cf37

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute boolean shouldAllowContent`: (未記入)

# nsIContentAnalysisResponse (toolkit/components/contentanalysis/nsIContentAnalysis.idl)

source: toolkit/components/contentanalysis/nsIContentAnalysis.idl
source-hash: 0cf288d2a2cc7870394c0acca8f73e067862cf37

- 継承: nsIContentAnalysisResult
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/contentanalysis/content/ContentAnalysis.sys.mjs`](../../../browser/components/contentanalysis/content/ContentAnalysis.sys.mjs.md), [`browser/components/downloads/DownloadsViewUI.sys.mjs`](../../../browser/components/downloads/DownloadsViewUI.sys.mjs.md)

## メソッド / 属性
- `readonly attribute nsIContentAnalysisResponse_Action action`: (未記入)
- `readonly attribute nsIContentAnalysisResponse_CancelError cancelError`: (未記入)
- `readonly attribute ACString requestToken`: (未記入)
- `readonly attribute ACString userActionId`: (未記入)
- `readonly attribute boolean isCachedResponse`: (未記入)
- `readonly attribute boolean isSyntheticResponse`: (未記入)
- `void acknowledge(nsIContentAnalysisAcknowledgement aCaa)`: Acknowledge receipt of an analysis response.

# nsIClientDownloadResource (toolkit/components/contentanalysis/nsIContentAnalysis.idl)

source: toolkit/components/contentanalysis/nsIContentAnalysis.idl
source-hash: 0cf288d2a2cc7870394c0acca8f73e067862cf37

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute AString url`: (未記入)
- `const unsigned long DOWNLOAD_URL`: (未記入)
- `const unsigned long DOWNLOAD_REDIRECT`: (未記入)
- `const unsigned long TAB_URL`: (未記入)
- `const unsigned long TAB_REDIRECT`: (未記入)
- `const unsigned long PPAPI_DOCUMENT`: (未記入)
- `const unsigned long PPAPI_PLUGIN`: (未記入)
- `readonly attribute unsigned long type`: (未記入)

# nsIContentAnalysisRequest (toolkit/components/contentanalysis/nsIContentAnalysis.idl)

source: toolkit/components/contentanalysis/nsIContentAnalysis.idl
source-hash: 0cf288d2a2cc7870394c0acca8f73e067862cf37

- 継承: nsISupports
- 役割: A nsIContentAnalysisRequest represents a request (or multiple requests)
- 実装: (未記入)
- 使っているJS: [`browser/components/contentanalysis/content/ContentAnalysis.sys.mjs`](../../../browser/components/contentanalysis/content/ContentAnalysis.sys.mjs.md)

## メソッド / 属性
- `readonly attribute nsIContentAnalysisRequest_AnalysisType analysisType`: (未記入)
- `readonly attribute nsIContentAnalysisRequest_Reason reason`: (未記入)
- `readonly attribute nsIContentAnalysisRequest_OperationType operationTypeForDisplay`: (未記入)
- `readonly attribute AString fileNameForDisplay`: (未記入)
- `attribute DataTransfer dataTransfer`: (未記入)
- `readonly attribute nsITransferable transferable`: (未記入)
- `readonly attribute AString textContent`: (未記入)
- `readonly attribute AString filePath`: (未記入)
- `Array<octet> getPrintData()`: (未記入)
- `readonly attribute AString printerName`: (未記入)
- `readonly attribute nsIURI url`: (未記入)
- `readonly attribute ACString sha256Digest`: (未記入)
- `readonly attribute Array<nsIClientDownloadResource> resources`: (未記入)
- `readonly attribute AString email`: (未記入)
- `attribute ACString requestToken`: (未記入)
- `readonly attribute WindowGlobalParent windowGlobalParent`: (未記入)
- `attribute ACString userActionId`: (未記入)
- `attribute int64_t userActionRequestsCount`: (未記入)
- `readonly attribute WindowGlobalParent sourceWindowGlobal`: (未記入)
- `attribute uint32_t timeoutMultiplier`: (未記入)
- `attribute boolean testOnlyIgnoreCanceledAndAlwaysSubmitToAgent`: (未記入)

# nsIContentAnalysisCallback (toolkit/components/contentanalysis/nsIContentAnalysis.idl)

source: toolkit/components/contentanalysis/nsIContentAnalysis.idl
source-hash: 0cf288d2a2cc7870394c0acca8f73e067862cf37

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void contentResult(nsIContentAnalysisResult aResult)`: (未記入)
- `void error(nsresult aResult)`: (未記入)

# nsIContentAnalysisDiagnosticInfo (toolkit/components/contentanalysis/nsIContentAnalysis.idl)

source: toolkit/components/contentanalysis/nsIContentAnalysis.idl
source-hash: 0cf288d2a2cc7870394c0acca8f73e067862cf37

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute boolean connectedToAgent`: (未記入)
- `readonly attribute AString agentPath`: (未記入)
- `readonly attribute boolean failedSignatureVerification`: (未記入)
- `readonly attribute long long requestCount`: (未記入)

# nsIContentAnalysis (toolkit/components/contentanalysis/nsIContentAnalysis.idl)

source: toolkit/components/contentanalysis/nsIContentAnalysis.idl
source-hash: 0cf288d2a2cc7870394c0acca8f73e067862cf37

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/contentanalysis/content/ContentAnalysis.sys.mjs`](../../../browser/components/contentanalysis/content/ContentAnalysis.sys.mjs.md), [`browser/components/enterprisepolicies/Policies.sys.mjs`](../../../browser/components/enterprisepolicies/Policies.sys.mjs.md)

## メソッド / 属性
- `readonly attribute boolean isActive`: True if content analysis should be consulted. Must only be accessed from
- `readonly attribute boolean mightBeActive`: True if content analysis might be active, and False if content analysis
- `attribute boolean isSetByEnterprisePolicy`: True if content-analysis activation was determined by enterprise policy,
- `Promise analyzeContentRequests(Array<nsIContentAnalysisRequest> aCars, boolean aAutoAcknowledge)`: Consults content analysis server, if any, to request a permission
- `void analyzeContentRequestsCallback(Array<nsIContentAnalysisRequest> aCars, boolean aAutoAcknowledge, nsIContentAnalysisCallback callback)`: Same functionality as AnalyzeContentRequests(), but more convenient to call
- `Promise analyzeBatchContentRequest(nsIContentAnalysisRequest aCar, boolean aAutoAcknowledge)`: Same functionality as analyzeContentRequests(), but only accepts one request
- `void analyzeContentRequestPrivate(nsIContentAnalysisRequest aRequest, boolean aAutoAcknowledge, nsIContentAnalysisCallback aCallback)`: Internal helper for 'analyzeContentRequest*' methods.  This is abstracted
- `void cancelRequestsByUserAction(ACString aUserActionId)`: Cancels the request that is in progress. This may not actually cancel the request
- `void cancelAllRequestsAssociatedWithUserAction(ACString aUserActionId)`: Like cancelRequestsByUserAction but does the same for any other user
- `void respondToWarnDialog(ACString aRequestToken, boolean aAllowContent)`: Indicates that the user has responded to a WARN dialog. aAllowContent represents
- `void cancelAllRequests(boolean aForbidFutureRequests)`: Cancels all outstanding DLP requests. Used on shutdown.
- `void testOnlySetCACmdLineArg(boolean aVal)`: Test-only function that pretends that "-allow-content-analysis" was
- `Promise getDiagnosticInfo()`: Gets diagnostic information about content analysis. Returns a
- `nsIURI getURIForBrowsingContext(BrowsingContext aBrowsingContext)`: Gets the URI to use for the passed-in browsing context. This correctly
- `nsIURI getURIForDropEvent(DragEvent aEvent)`: Gets the URI to use for the passed-in drop event. This correctly
- `void setCachedResponse(nsIURI aURI, int32_t aSequenceNumber, nsIContentAnalysisResponse_Action aAction)`: Sets the cached response from analyzing the whole clipboard.
- `void getCachedResponse(nsIURI aURI, int32_t aSequenceNumber, nsIContentAnalysisResponse_Action aAction, boolean aIsValid)`: Gets the cached response from analyzing the whole clipboard.
- `void showBlockedRequestDialog(nsIContentAnalysisRequest aRequest)`: Show a dialog to indicate to the user that the given request was blocked.
- `nsIContentAnalysisResponse makeResponseForTest(nsIContentAnalysisResponse_Action aAction, ACString aToken, ACString aUserActionId)`: Make an nsIContentAnalysisResponse object.  For use in tests only.
- `void sendCancelToAgent(ACString aUserActionId)`: Send CancelRequests to agent on a background thread.
- `void forceRecreateClientForTest()`: Force the content analysis client to be recreated. For use in tests only.

# nsIContentAnalysisRule (toolkit/components/contentanalysis/nsIContentAnalysis.idl)

source: toolkit/components/contentanalysis/nsIContentAnalysis.idl
source-hash: 0cf288d2a2cc7870394c0acca8f73e067862cf37

- 継承: nsISupports
- 役割: A single Content Analysis rule passed to the built-in DLP module
- 実装: (未記入)

## メソッド / 属性
- `const octet REPORT`: (未記入)
- `const octet WARN`: (未記入)
- `const octet BLOCK`: (未記入)
- `readonly attribute AString name`: (未記入)
- `readonly attribute Array<unsigned long> operations`: (未記入)
- `readonly attribute Array<AString> domains`: (未記入)
- `readonly attribute Array<AString> contentPatterns`: (未記入)
- `readonly attribute octet verdict`: (未記入)
- `readonly attribute AString message`: (未記入)

# nsIContentAnalysisWasmRunner (toolkit/components/contentanalysis/nsIContentAnalysis.idl)

source: toolkit/components/contentanalysis/nsIContentAnalysis.idl
source-hash: 0cf288d2a2cc7870394c0acca8f73e067862cf37

- 継承: nsISupports
- 役割: Runs an in-process WebAssembly DLP module. Implemented in JS
- 実装: (未記入)

## メソッド / 属性
- `Promise analyze(Array<octet> aRequestBytes, Array<octet> aContentBytes, Array<nsIContentAnalysisRule> aRules)`: Analyze a request asynchronously.
