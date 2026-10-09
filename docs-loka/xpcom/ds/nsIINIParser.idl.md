# nsIINIParser (xpcom/ds/nsIINIParser.idl)

source: xpcom/ds/nsIINIParser.idl
source-hash: 6b300c64bceeb3bab025863182df287aa99feb2d

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void initFromString(AUTF8String aData, boolean aContainedErrors)`: Initializes an INI file from string data
- `nsIUTF8StringEnumerator getSections()`: Enumerates the [section]s available in the INI file.
- `nsIUTF8StringEnumerator getKeys(AUTF8String aSection)`: Enumerates the keys available within a section.
- `AUTF8String getString(AUTF8String aSection, AUTF8String aKey)`: Get the value of a string for a particular section and key.

# nsIINIParserWriter (xpcom/ds/nsIINIParser.idl)

source: xpcom/ds/nsIINIParser.idl
source-hash: 6b300c64bceeb3bab025863182df287aa99feb2d

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/shell/ShellService.sys.mjs`](../../browser/components/shell/ShellService.sys.mjs.md)

## メソッド / 属性
- `void setString(AUTF8String aSection, AUTF8String aKey, AUTF8String aValue)`: Set the value of a string for a particular section and key.
- `void deleteString(AUTF8String aSection, AUTF8String aKey)`: Deletes a string within a particular section.
- `void writeFile(nsIFile aINIFile)`: Write to the INI file.
- `AUTF8String writeToString()`: Return the formatted INI file contents

# nsIINIParserFactory (xpcom/ds/nsIINIParser.idl)

source: xpcom/ds/nsIINIParser.idl
source-hash: 6b300c64bceeb3bab025863182df287aa99feb2d

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/distribution.sys.mjs`](../../browser/components/distribution.sys.mjs.md), [`browser/components/profiles/SelectableProfileService.sys.mjs`](../../browser/components/profiles/SelectableProfileService.sys.mjs.md), [`browser/components/shell/ShellService.sys.mjs`](../../browser/components/shell/ShellService.sys.mjs.md)

## メソッド / 属性
- `nsIINIParser createINIParser(nsIFile aINIFile, boolean aContainedErrors)`: Create an iniparser instance from a local file.
