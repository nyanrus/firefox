# browser/components/downloads/content/downloadsCommands.js

source: browser/components/downloads/content/downloadsCommands.js
source-hash: fd7dfce35144a72df595739ed39880276ded2500
lines: 18

## <module>
- 役割: ダウンロードパネルのコマンド(command と commandupdate)を、DOM 読み込み後に goDoCommand と goUpdateDownloadCommands へ中継する。
- 呼び出し先: `document.addEventListener()`, `document.getElementById()`, `downloadCommands.addEventListener()`, `goDoCommand()`, `goUpdateDownloadCommands()`
