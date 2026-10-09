# nsIAutoCompleteController (toolkit/components/autocomplete/nsIAutoCompleteController.idl)

source: toolkit/components/autocomplete/nsIAutoCompleteController.idl
source-hash: 148e704b4c83b62a0a3483a4c083a4b370fc9303

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `const unsigned short STATUS_NONE`: (未記入)
- `const unsigned short STATUS_SEARCHING`: (未記入)
- `const unsigned short STATUS_COMPLETE_NO_MATCH`: (未記入)
- `const unsigned short STATUS_COMPLETE_MATCH`: (未記入)
- `attribute nsIAutoCompleteInput input`: (未記入)
- `readonly attribute unsigned short searchStatus`: (未記入)
- `readonly attribute unsigned long matchCount`: (未記入)
- `void startSearch(AString searchString)`: (未記入)
- `void stopSearch()`: (未記入)
- `boolean handleText()`: (未記入)
- `boolean handleEnter(boolean aIsPopupSelection, Event aEvent)`: (未記入)
- `boolean handleEscape()`: (未記入)
- `void handleStartComposition()`: (未記入)
- `void handleEndComposition()`: (未記入)
- `void handleTab()`: (未記入)
- `boolean handleKeyNavigation(unsigned long key)`: (未記入)
- `boolean handleDelete()`: (未記入)
- `AString getValueAt(long index)`: (未記入)
- `AString getLabelAt(long index)`: (未記入)
- `AString getCommentAt(long index)`: (未記入)
- `AString getStyleAt(long index)`: (未記入)
- `AString getImageAt(long index)`: (未記入)
- `AString getFinalCompleteValueAt(long index)`: (未記入)
- `attribute AString searchString`: (未記入)
- `void setInitiallySelectedIndex(long index)`: (未記入)
- `void resetInternalState()`: (未記入)
