# browser/components/places/content/places-commands.js

source: browser/components/places/content/places-commands.js
source-hash: 53043c1bf79fb30f36ae0397a5a6fd141d3d3819
lines: 45

## <module>
- 役割: placesCommands 要素の command と commandupdate イベントを受け、PlacesUIUtils へ振り分ける。
- 呼び出し先: `AIWindow.isAIWindowActive()`, `PlacesCommandHook.showPlacesOrganizer()`, `PlacesUIUtils.doCommand()`, `PlacesUIUtils.updateCommands()`, `document .getElementById()`, `document .getElementById("placesCommands") .addEventListener()`, `document.getElementById()`, `document.getElementById("placesCommands").addEventListener()`
