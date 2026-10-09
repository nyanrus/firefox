# browser/extensions/pictureinpicture/lib/picture_in_picture_overrides.js

source: browser/extensions/pictureinpicture/lib/picture_in_picture_overrides.js
source-hash: 9328ce240b214e7c125ad50f1e4293677919674d
lines: 101

## <module>
- 役割: (未記入)

## PictureInPictureOverrides.constructor()
- 位置: L18-23
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.pictureInPictureChild.getPolicies()`
- 参照: `this._availableOverrides`, `this._prefEnabledOverrides`, `this.policies`, `this.pref`

## PictureInPictureOverrides._checkGlobalPref()
- 位置: async L28-39
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.aboutConfigPipPrefs.getPref()`, `browser.aboutConfigPipPrefs.getPref(this.pref).then()`
- 条件付き依存: `if (value === undefined)` → `browser.aboutConfigPipPrefs.setPref()`
- 参照: `this._enabled`, `this.pref`

## PictureInPictureOverrides._checkSpecificOverridePref()
- 位置: async L47-54
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `browser.aboutConfigPipPrefs.getPref()`
- 条件付き依存: `if (isDisabled === true)` → `this._prefEnabledOverrides.delete()`
- 条件付き依存: `if (!(isDisabled === true))` → `this._prefEnabledOverrides.add()`

## PictureInPictureOverrides.bootup()
- 位置: L59-84
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.keys()`, `Promise.all()`, `Promise.all(bootupPrefCheckPromises).then()`, `bootupPrefCheckPromises.push()`, `browser.aboutConfigPipPrefs.onPrefChange.addListener()`, `this._checkGlobalPref()`, `this._checkSpecificOverridePref()`, `this._onAvailableOverridesChanged()`
- 参照: `this._availableOverrides`, `this.pref`

## checkGlobal()
- 位置: async L60-63
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._checkGlobalPref()`, `this._onAvailableOverridesChanged()`

## checkSingle()
- 位置: async L73-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._checkSpecificOverridePref()`, `this._onAvailableOverridesChanged()`

## PictureInPictureOverrides._onAvailableOverridesChanged()
- 位置: async L89-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.entries()`, `browser.pictureInPictureParent.setOverrides()`, `this._prefEnabledOverrides.has()`
- 参照: `policies.DEFAULT`, `this._availableOverrides`, `this._enabled`, `this.policies`
