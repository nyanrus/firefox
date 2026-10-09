# nsIDialogParamBlock (toolkit/components/windowwatcher/nsIDialogParamBlock.idl)

source: toolkit/components/windowwatcher/nsIDialogParamBlock.idl
source-hash: d7901063b28d40c4e3a1d7c06ac308b57705dabe

- 継承: nsISupports
- 役割: An interface to pass strings, integers and nsISupports to a dialog
- 実装: (未記入)
- 使っているJS: [`browser/components/profiles/content/profile-selector.mjs`](../../../browser/components/profiles/content/profile-selector.mjs.md)

## メソッド / 属性
- `int32_t GetInt(int32_t inIndex)`: Get or set an integer to pass.
- `void SetInt(int32_t inIndex, int32_t inInt)`: (未記入)
- `void SetNumberStrings(int32_t inNumStrings)`: Set the maximum number of strings to pass. Default is 16.
- `wstring GetString(int32_t inIndex)`: Get or set an string to pass.
- `void SetString(int32_t inIndex, wstring inString)`: (未記入)
- `attribute nsIMutableArray objects`: A place where you can store an nsIMutableArray to pass nsISupports
