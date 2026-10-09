# browser/extensions/newtab/lib/Wallpapers/WallpaperFileNames.mjs

source: browser/extensions/newtab/lib/Wallpapers/WallpaperFileNames.mjs
source-hash: 5bfb9f11e076dee40841beb19f328cb59ce464fd
lines: 206

## <module>
- 役割: (未記入)
- 呼び出し先: `Object.values()`

## encodeBackgroundPosition()
- 位置: L54-59
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `POSITIONS.has()`, `String()`, `String(position ?? "") .toLowerCase()`, `String(position ?? "") .toLowerCase() .replace()`

## decodeBackgroundPosition()
- 位置: L61-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `POSITIONS.get()`

## buildSavedWallpaperFilename()
- 位置: L64-85
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `NUMBER_PATTERN.test()`, `SAVED_TYPES.includes()`, `String()`, `THEMES.includes()`, `UUID_PATTERN.test()`, `encodeBackgroundPosition()`

## sanitizeSavedName()
- 位置: L98-128
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `clipped.lastIndexOf()`, `clipped.slice()`, `printable .slice()`, `printable .slice(0, MAX_SAVED_NAME_LENGTH + 1) .match()`, `printable.slice()`, `savedName.replace()`, `savedName.replace(/[\u0000-\u001f\u007f]/g, "").trim()`
- 参照: `printable.length`, `sentence[0].length`

## getDetailsFilename()
- 位置: L130-131
- 役割: (未記入)
- 触るとき: (未記入)

## getThumbnailFilename()
- 位置: L133-134
- 役割: (未記入)
- 触るとき: (未記入)

## getWallpaperURL()
- 位置: L149-152
- 役割: (未記入)
- 触るとき: (未記入)

## parseWallpaperFilename()
- 位置: L161-205
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UUID_PATTERN.test()`, `filename.endsWith()`, `filename.split()`
- 条件付き依存: `if (filename.endsWith(extension))` → `filename.slice()`
- 条件付き依存: `if (parts[0] === SAVED_WALLPAPER_VERSION)` → `rest.join()`
- 条件付き依存: `if (parts[0] === SAVED_WALLPAPER_VERSION)` → `SAVED_TYPES.includes()`
- 条件付き依存: `if (parts[0] === SAVED_WALLPAPER_VERSION)` → `THEMES.includes()`
- 条件付き依存: `if (parts[0] === SAVED_WALLPAPER_VERSION)` → `POSITIONS.has()`
- 条件付き依存: `if (parts[0] === SAVED_WALLPAPER_VERSION)` → `NUMBER_PATTERN.test()`
- 条件付き依存: `if (parts[0] === SAVED_WALLPAPER_VERSION)` → `UUID_PATTERN.test()`
- 条件付き依存: `if (known)` → `decodeBackgroundPosition()`
- 条件付き依存: `if (known)` → `Number()`
- 参照: `extension.length`
