# nsILocalFileWin (xpcom/io/nsILocalFileWin.idl)

source: xpcom/io/nsILocalFileWin.idl
source-hash: cb3d1d1e49af8c77d08c3b95d47c5e14b140feae

- 継承: nsIFile
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/preferences/config/downloads.mjs`](../../browser/components/preferences/config/downloads.mjs.md)

## メソッド / 属性
- `void initWithCommandLine(AString aCommandLine)`: initWithCommandLine
- `AString getVersionInfoField(string aField)`: getVersionInfoValue
- `readonly attribute AString canonicalPath`: The canonical path of the file, which avoids short/long
- `attribute boolean readOnly`: Get or set whether this file is marked read-only.
- `attribute boolean useDOSDevicePathSyntax`: Setting this to true will prepend the prefix "\\?\" to all parsed file
- `PRFileDescStar openNSPRFileDescShareDelete(long flags, long mode)`: Identical to nsIFile::openNSPRFileDesc except it also uses the
- `unsigned long getWindowsFileAttributes()`: Return the Windows-specific file attributes of this file.
- `void setWindowsFileAttributes(unsigned long aSetAttrs, unsigned long aClearAttrs)`: Set or clear the Windows specific file attributes of this file.
