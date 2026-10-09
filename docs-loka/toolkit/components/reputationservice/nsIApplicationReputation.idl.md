# nsIApplicationReputationService (toolkit/components/reputationservice/nsIApplicationReputation.idl)

source: toolkit/components/reputationservice/nsIApplicationReputation.idl
source-hash: 231e45f00baf04bf446389913a8efe1a9ff3f6f6

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/downloads/DownloadsViewUI.sys.mjs`](../../../browser/components/downloads/DownloadsViewUI.sys.mjs.md)

## メソッド / 属性
- `const unsigned long VERDICT_SAFE`: Indicates the reason for the application reputation block.
- `const unsigned long VERDICT_DANGEROUS`: (未記入)
- `const unsigned long VERDICT_UNCOMMON`: (未記入)
- `const unsigned long VERDICT_POTENTIALLY_UNWANTED`: (未記入)
- `const unsigned long VERDICT_DANGEROUS_HOST`: (未記入)
- `void queryReputation(nsIApplicationReputationQuery aQuery, nsIApplicationReputationCallback aCallback)`: Start querying the application reputation service.
- `boolean isBinary(AUTF8String aFilename)`: Check if a file with this name should be treated as a binary executable,
- `boolean isExecutable(AUTF8String aFilename)`: Check if a file with this name should be treated as an executable,

# nsIApplicationReputationQuery (toolkit/components/reputationservice/nsIApplicationReputation.idl)

source: toolkit/components/reputationservice/nsIApplicationReputation.idl
source-hash: 231e45f00baf04bf446389913a8efe1a9ff3f6f6

- 継承: nsISupports
- 役割: A single-use, write-once interface for recording the metadata of the
- 実装: (未記入)

## メソッド / 属性
- `readonly attribute nsIURI sourceURI`: (未記入)
- `readonly attribute nsIReferrerInfo referrerInfo`: (未記入)
- `readonly attribute AUTF8String suggestedFileName`: (未記入)
- `readonly attribute unsigned long fileSize`: (未記入)
- `readonly attribute ACString sha256Hash`: (未記入)
- `readonly attribute Array<Array<Array<uint8_t>>> signatureInfo`: (未記入)
- `readonly attribute nsIArray redirects`: (未記入)

# nsIApplicationReputationCallback (toolkit/components/reputationservice/nsIApplicationReputation.idl)

source: toolkit/components/reputationservice/nsIApplicationReputation.idl
source-hash: 231e45f00baf04bf446389913a8efe1a9ff3f6f6

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void onComplete(boolean aShouldBlock, nsresult aStatus, unsigned long aVerdict)`: Callback for the result of the application reputation query.
