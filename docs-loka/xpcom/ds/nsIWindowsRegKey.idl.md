# nsIWindowsRegKey (xpcom/ds/nsIWindowsRegKey.idl)

source: xpcom/ds/nsIWindowsRegKey.idl
source-hash: cb7884c88aa735e7c971097baf9228dbbf4aab4b

- 継承: nsISupports
- 役割: This interface is designed to provide scriptable access to the Windows
- 実装: (未記入)
- 使っているJS: [`browser/components/ReinstallCheck.sys.mjs`](../../browser/components/ReinstallCheck.sys.mjs.md), [`browser/components/installerprefs/InstallerPrefs.sys.mjs`](../../browser/components/installerprefs/InstallerPrefs.sys.mjs.md), [`browser/components/migration/MSMigrationUtils.sys.mjs`](../../browser/components/migration/MSMigrationUtils.sys.mjs.md), [`browser/components/shell/CustomIconManager.sys.mjs`](../../browser/components/shell/CustomIconManager.sys.mjs.md), [`browser/components/shell/StartupOSIntegration.sys.mjs`](../../browser/components/shell/StartupOSIntegration.sys.mjs.md), [`browser/modules/FirefoxBridgeExtensionUtils.sys.mjs`](../../browser/modules/FirefoxBridgeExtensionUtils.sys.mjs.md)

## メソッド / 属性
- `const unsigned long ROOT_KEY_CLASSES_ROOT`: Root keys.  The values for these keys correspond to the values from
- `const unsigned long ROOT_KEY_CURRENT_USER`: (未記入)
- `const unsigned long ROOT_KEY_LOCAL_MACHINE`: (未記入)
- `const unsigned long ACCESS_BASIC`: Values for the mode parameter passed to the open and create methods.
- `const unsigned long ACCESS_QUERY_VALUE`: (未記入)
- `const unsigned long ACCESS_SET_VALUE`: (未記入)
- `const unsigned long ACCESS_CREATE_SUB_KEY`: (未記入)
- `const unsigned long ACCESS_ENUMERATE_SUB_KEYS`: (未記入)
- `const unsigned long ACCESS_NOTIFY`: (未記入)
- `const unsigned long ACCESS_READ`: (未記入)
- `const unsigned long ACCESS_WRITE`: (未記入)
- `const unsigned long ACCESS_ALL`: (未記入)
- `const unsigned long WOW64_32`: (未記入)
- `const unsigned long WOW64_64`: (未記入)
- `const unsigned long TYPE_NONE`: Values for the type of a registry value.  The numeric values of these
- `const unsigned long TYPE_STRING`: (未記入)
- `const unsigned long TYPE_BINARY`: (未記入)
- `const unsigned long TYPE_INT`: (未記入)
- `const unsigned long TYPE_INT64`: (未記入)
- `void close()`: This method closes the key.  If the key is already closed, then this
- `void open(unsigned long rootKey, AString relPath, unsigned long mode)`: This method opens an existing key.  This method fails if the key
- `void create(unsigned long rootKey, AString relPath, unsigned long mode)`: This method opens an existing key or creates a new key.
- `nsIWindowsRegKey openChild(AString relPath, unsigned long mode)`: This method opens a subkey relative to this key.  This method fails if the
- `nsIWindowsRegKey createChild(AString relPath, unsigned long mode)`: This method opens or creates a subkey relative to this key.
- `readonly attribute unsigned long childCount`: This attribute returns the number of child keys.
- `AString getChildName(unsigned long index)`: This method returns the name of the n'th child key.
- `boolean hasChild(AString name)`: This method checks to see if the key has a child by the given name.
- `readonly attribute unsigned long valueCount`: This attribute returns the number of values under this key.
- `AString getValueName(unsigned long index)`: This method returns the name of the n'th value under this key.
- `boolean hasValue(AString name)`: This method checks to see if the key has a value by the given name.
- `void removeChild(AString relPath)`: This method removes a child key and all of its values.  This method will
- `void removeValue(AString name)`: This method removes the value with the given name.
- `unsigned long getValueType(AString name)`: This method returns the type of the value with the given name.  The return
- `AString readStringValue(AString name)`: This method reads the string contents of the named value as a Unicode
- `unsigned long readIntValue(AString name)`: This method reads the integer contents of the named value.
- `unsigned long long readInt64Value(AString name)`: This method reads the 64-bit integer contents of the named value.
- `ACString readBinaryValue(AString name)`: This method reads the binary contents of the named value under this key.
- `void writeStringValue(AString name, AString data)`: This method writes the unicode string contents of the named value.  The
- `void writeIntValue(AString name, unsigned long data)`: This method writes the integer contents of the named value.  The value
- `void writeInt64Value(AString name, unsigned long long data)`: This method writes the 64-bit integer contents of the named value.  The
- `void writeBinaryValue(AString name, ACString data)`: This method writes the binary contents of the named value.  The value will
