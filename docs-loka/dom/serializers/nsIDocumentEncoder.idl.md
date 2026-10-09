# nsIDocumentEncoderNodeFixup (dom/serializers/nsIDocumentEncoder.idl)

source: dom/serializers/nsIDocumentEncoder.idl
source-hash: 7313b49f4d8929032a89892377e6bbe610448059

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `Node fixupNode(Node aNode, boolean aSerializeCloneKids)`: Create a fixed up version of a node. This method is called before

# nsIDocumentEncoder (dom/serializers/nsIDocumentEncoder.idl)

source: dom/serializers/nsIDocumentEncoder.idl
source-hash: 7313b49f4d8929032a89892377e6bbe610448059

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/urlbar/content/SmartbarInput.mjs`](../../browser/components/urlbar/content/SmartbarInput.mjs.md), [`browser/components/urlbar/content/UrlbarInputBase.mjs`](../../browser/components/urlbar/content/UrlbarInputBase.mjs.md)

## メソッド / 属性
- `const unsigned long OutputSelectionOnly`: Output only the selection (as opposed to the whole document).
- `const unsigned long OutputFormatted`: Plaintext output:
- `const unsigned long OutputRaw`: Don't do prettyprinting. Don't do any wrapping that's not in the existing
- `const unsigned long OutputBodyOnly`: Do not print html head tags.
- `const unsigned long OutputPreformatted`: Output as though the content is preformatted
- `const unsigned long OutputWrap`: Wrap even if we're not doing formatted output (e.g. for text fields).
- `const unsigned long OutputFormatFlowed`: Output for format flowed (RFC 2646). This is used when converting
- `const unsigned long OutputAbsoluteLinks`: Convert links, image src, and script src to absolute URLs when possible.
- `const unsigned long OutputCRLineBreak`: LineBreak processing: if this flag is set than CR line breaks will
- `const unsigned long OutputLFLineBreak`: LineBreak processing: if this flag is set than LF line breaks will
- `const unsigned long OutputNoScriptContent`: Output the content of noscript elements (only for serializing
- `const unsigned long OutputNoFramesContent`: Output the content of noframes elements (only for serializing
- `const unsigned long OutputNoFormattingInPre`: Don't allow any formatting nodes (e.g. <br>, <b>) inside a <pre>.
- `const unsigned long OutputEncodeBasicEntities`: Encode entities when outputting to a string.
- `const unsigned long OutputPersistNBSP`: Normally &nbsp; is replaced with a space character when
- `const unsigned long OutputDontRewriteEncodingDeclaration`: Normally when serializing the whole document using the HTML or
- `const unsigned long SkipInvisibleContent`: When using the HTML or XHTML serializer, skip elements that are not
- `const unsigned long OutputFormatDelSp`: Output for delsp=yes (RFC 3676). This is used with OutputFormatFlowed
- `const unsigned long OutputDropInvisibleBreak`: Drop <br> elements considered "invisible" by the editor. OutputPreformatted
- `const unsigned long OutputIgnoreMozDirty`: Don't check for _moz_dirty attributes when deciding whether to
- `const unsigned long OutputForPlainTextClipboardCopy`: Serialize in a way that is suitable for copying a plaintext version of the
- `const unsigned long OutputRubyAnnotation`: Include ruby annotations and ruby parentheses in the output.
- `const unsigned long OutputDisallowLineBreaking`: Disallow breaking of long character strings. This is important
- `const unsigned long RequiresReinitAfterOutput`: Release reference of Document after using encodeTo* method to recycle
- `const unsigned long AllowCrossShadowBoundary`: (未記入)
- `const unsigned long MimicChromeToStringBehaviour`: Whether window.getSelection().toString() should mimic Chrome's
- `void init(Document aDocument, AString aMimeType, unsigned long aFlags)`: Initialize with a pointer to the document and the mime type.
- `void setSelection(Selection aSelection)`: If the selection is set to a non-null value, then the
- `void setRange(Range aRange)`: If the range is set to a non-null value, then the
- `void setNode(Node aNode)`: If the node is set to a non-null value, then the
- `void setContainerNode(Node aContainer)`: If the container is set to a non-null value, then its
- `void setCharset(ACString aCharset)`: Documents typically have an intrinsic character set,
- `void setWrapColumn(unsigned long aWrapColumn)`: Set a wrap column.  This may have no effect in some types of encoders.
- `readonly attribute AString mimeType`: The mime type preferred by the encoder.  This piece of api was
- `void encodeToStream(nsIOutputStream aStream)`: Encode the document and send the result to the nsIOutputStream.
- `AString encodeToString()`: Encode the document into a string.
- `AString encodeToStringWithContext(AString aContextString, AString aInfoString)`: Encode the document into a string. Stores the extra context information
- `AString encodeToStringWithMaxLength(unsigned long aMaxLength)`: Encode the document into a string of limited size.
- `void setNodeFixup(nsIDocumentEncoderNodeFixup aFixup)`: Set the fixup object associated with node persistence.
