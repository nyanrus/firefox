# browser/components/places/content/placesContextMenu.js

source: browser/components/places/content/placesContextMenu.js
source-hash: b353f722d55d62708c8da51c08833cacdb55783f
lines: 44

## <module>
- 役割: places のコンテキストメニューのイベントを PlacesUIUtils の各関数へ配線する(DOMContentLoaded 後に一度だけ実行)
- 呼び出し先: `PlacesUIUtils.createContainerTabMenu()`, `PlacesUIUtils.openInContainerTab()`, `PlacesUIUtils.openSelectionInTabs()`, `PlacesUIUtils.placesContextHiding()`, `PlacesUIUtils.placesContextShowing()`, `PlacesUIUtils.shareBookmarkFolder()`, `containerPopup.addEventListener()`, `document.addEventListener()`, `document.getElementById()`, `placesContext.addEventListener()`
