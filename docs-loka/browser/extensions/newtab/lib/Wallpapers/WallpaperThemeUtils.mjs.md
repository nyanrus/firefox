# browser/extensions/newtab/lib/Wallpapers/WallpaperThemeUtils.mjs

source: browser/extensions/newtab/lib/Wallpapers/WallpaperThemeUtils.mjs
source-hash: 156e7b279f2e022844981adc44d53e5ed215efe4
lines: 68

## <module>
- 役割: (未記入)

## relativeLuminance()
- 位置: L12-20
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.pow()`, `[r, g, b].map()`

## calculateTheme()
- 位置: async L29-67
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `Math.min()`, `Math.round()`, `Math.sqrt()`, `canvas.getContext()`, `ctx.drawImage()`, `ctx.getImageData()`, `win.createImageBitmap()`
- 条件付き依存: `if (alpha > 0)` → `relativeLuminance()`
- 参照: `bitmap.height`, `bitmap.width`, `win.OffscreenCanvas`
