# nsIWebBrowserPersist (dom/webbrowserpersist/nsIWebBrowserPersist.idl)

source: dom/webbrowserpersist/nsIWebBrowserPersist.idl
source-hash: 8f9a5a9613372f3c35133a03671942b0cbb5e7ec

- 継承: nsICancelable
- 役割: Interface for persisting DOM documents and URIs to local or remote storage.
- 実装: (未記入)

## メソッド / 属性
- `const unsigned long PERSIST_FLAGS_NONE`: No special persistence behaviour.
- `const unsigned long PERSIST_FLAGS_FROM_CACHE`: Use cached data if present (skipping validation), else load from network
- `const unsigned long PERSIST_FLAGS_BYPASS_CACHE`: Bypass the cached data.
- `const unsigned long PERSIST_FLAGS_IGNORE_REDIRECTED_DATA`: Ignore any redirected data (usually adverts).
- `const unsigned long PERSIST_FLAGS_IGNORE_IFRAMES`: Ignore IFRAME content (usually adverts).
- `const unsigned long PERSIST_FLAGS_NO_CONVERSION`: Do not run the incoming data through a content converter e.g. to decompress it
- `const unsigned long PERSIST_FLAGS_REPLACE_EXISTING_FILES`: Replace existing files on the disk (use with due diligence!)
- `const unsigned long PERSIST_FLAGS_NO_BASE_TAG_MODIFICATIONS`: Don't modify or add base tags
- `const unsigned long PERSIST_FLAGS_FIXUP_ORIGINAL_DOM`: Make changes to original dom rather than cloning nodes
- `const unsigned long PERSIST_FLAGS_FIXUP_LINKS_TO_DESTINATION`: Fix links relative to destination location (not origin)
- `const unsigned long PERSIST_FLAGS_DONT_FIXUP_LINKS`: Don't make any adjustments to links
- `const unsigned long PERSIST_FLAGS_SERIALIZE_OUTPUT`: Force serialization of output (one file at a time; not concurrent)
- `const unsigned long PERSIST_FLAGS_DONT_CHANGE_FILENAMES`: Don't make any adjustments to filenames
- `const unsigned long PERSIST_FLAGS_FAIL_ON_BROKEN_LINKS`: Fail on broken inline links
- `const unsigned long PERSIST_FLAGS_CLEANUP_ON_FAILURE`: Automatically cleanup after a failed or cancelled operation, deleting all
- `const unsigned long PERSIST_FLAGS_AUTODETECT_APPLY_CONVERSION`: Let the WebBrowserPersist decide whether the incoming data is encoded
- `const unsigned long PERSIST_FLAGS_APPEND_TO_FILE`: Append the downloaded data to the target file.
- `const unsigned long PERSIST_FLAGS_DISABLE_HTTPS_ONLY`: Unconditionally disable HTTPS-Only and HTTPS-First upgrades
- `attribute unsigned long persistFlags`: Flags governing how data is fetched and saved from the network.
- `const unsigned long PERSIST_STATE_READY`: Persister is ready to save data
- `const unsigned long PERSIST_STATE_SAVING`: Persister is saving data
- `const unsigned long PERSIST_STATE_FINISHED`: Persister has finished saving data
- `readonly attribute unsigned long currentState`: Current state of the persister object.
- `readonly attribute nsresult result`: Value indicating the success or failure of the persist
- `attribute nsIWebProgressListener progressListener`: Callback listener for progress notifications. The object that the
- `void saveURI(nsIURI aURI, nsIPrincipal aTriggeringPrincipal, unsigned long aCacheKey, nsIReferrerInfo aReferrerInfo, nsICookieJarSettings aCookieJarSettings, nsIInputStream aPostData, string aExtraHeaders, nsISupports aFile, nsContentPolicyType aContentPolicyType, boolean aIsPrivate)`: Save the specified URI to file.
- `void saveChannel(nsIChannel aChannel, nsISupports aFile)`: Save a channel to a file. It must not be opened yet.
- `const unsigned long ENCODE_FLAGS_SELECTION_ONLY`: Output only the current selection as opposed to the whole document.
- `const unsigned long ENCODE_FLAGS_FORMATTED`: For plaintext output. Convert html to plaintext that looks like the html.
- `const unsigned long ENCODE_FLAGS_RAW`: Output without formatting or wrapping the content. This flag
- `const unsigned long ENCODE_FLAGS_BODY_ONLY`: Output only the body section, no HTML tags.
- `const unsigned long ENCODE_FLAGS_PREFORMATTED`: Wrap even if when not doing formatted output (e.g. for text fields).
- `const unsigned long ENCODE_FLAGS_WRAP`: Wrap documents at the specified column.
- `const unsigned long ENCODE_FLAGS_FORMAT_FLOWED`: For plaintext output. Output for format flowed (RFC 2646). This is used
- `const unsigned long ENCODE_FLAGS_ABSOLUTE_LINKS`: Convert links to absolute links where possible.
- `const unsigned long ENCODE_FLAGS_CR_LINEBREAKS`: Output with carriage return line breaks. May also be combined with
- `const unsigned long ENCODE_FLAGS_LF_LINEBREAKS`: Output with linefeed line breaks. May also be combined with
- `const unsigned long ENCODE_FLAGS_NOSCRIPT_CONTENT`: For plaintext output. Output the content of noscript elements.
- `const unsigned long ENCODE_FLAGS_NOFRAMES_CONTENT`: For plaintext output. Output the content of noframes elements.
- `const unsigned long ENCODE_FLAGS_ENCODE_BASIC_ENTITIES`: Encode basic entities, e.g. output &nbsp; instead of character code 0xa0.
- `const unsigned long ENCODE_FLAGS_DISALLOW_LINE_BREAKING`: Disable wrapping of long lines in output.
- `void saveDocument(nsISupports aDocument, nsISupports aFile, nsISupports aDataPath, string aOutputContentType, unsigned long aEncodingFlags, unsigned long aWrapColumn)`: Save the specified DOM document to file and optionally all linked files
- `void cancelSave()`: Cancels the current operation. The caller is responsible for cleaning up
