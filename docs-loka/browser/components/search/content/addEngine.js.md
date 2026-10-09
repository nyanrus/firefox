# browser/components/search/content/addEngine.js

source: browser/components/search/content/addEngine.js
source-hash: 7b22993f35df0d0e11265cf7e37d1aff64873493
lines: 589

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Promise.withResolvers()`, `initL10nCache()`, `loadedResolvers.resolve()`, `window.addEventListener()`

## EngineDialog.constructor()
- 位置: L62-87
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.addEventListener()`, `document.getElementById()`, `document.querySelector()`, `this._form.addEventListener()`, `this.onAccept.bind()`, `this.showAdvanced()`, `this.validateInput()`
- 条件付き依存: `if (e.target.localName == "input")` → `this._revealValidity()`
- 条件付き依存: `if (e.key == "Enter")` → `this._revealAllValidity()`
- 参照: `e.key`, `e.target`, `e.target.localName`, `e.target.validationMessage`, `this._alias`, `this._dialog`, `this._form`, `this._name`, `this._postData`, `this._suggestUrl`, `this._url`

## EngineDialog.showAdvanced()
- 位置: L96-102
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `this._dialog.getButton()`
- 条件付き依存: `if (resize)` → `window.resizeDialog()`
- 参照: `document.getElementById("advanced-section").hidden`, `this._dialog.getButton("extra1").hidden`

## EngineDialog.onAccept()
- 位置: L104-106
- 役割: (未記入)
- 触るとき: (未記入)

## EngineDialog.validateName()
- 位置: L108-122
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.getEngineByName()`, `this._name.value.trim()`, `this.allowedNames.includes()`, `this.setValidity()`
- 条件付き依存: `if (!name)` → `this.setValidity()`
- 条件付き依存: `if (existingEngine && !this.allowedNames.includes(name))` → `this.setValidity()`
- 参照: `this._name`

## EngineDialog.validateAlias()
- 位置: async L124-138
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.getEngineByAlias()`, `this._alias.value.trim()`, `this.allowedAliases.includes()`, `this.setValidity()`
- 条件付き依存: `if (!alias)` → `this.setValidity()`
- 条件付き依存: `if (existingEngine && !this.allowedAliases.includes(alias))` → `this.setValidity()`
- 参照: `this._alias`

## EngineDialog.validateUrlInput()
- 位置: L140-164
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `this._postData?.value.trim()`, `this._url.value.trim()`, `this.setValidity()`, `urlString.includes()`
- 条件付き依存: `if (!urlString)` → `this.setValidity()`
- 条件付き依存: `if (!url)` → `this.setValidity()`
- 条件付き依存: `if (url.protocol != "http:" && url.protocol != "https:")` → `this.setValidity()`
- 条件付き依存: `if (!urlString.includes("%s") && !postData)` → `this.setValidity()`
- 参照: `this._url`, `url.protocol`

## EngineDialog.validatePostDataInput()
- 位置: L166-173
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `postData.includes()`, `this._postData.value.trim()`, `this.setValidity()`
- 条件付き依存: `if (postData && !postData.includes("%s"))` → `this.setValidity()`
- 参照: `this._postData`

## EngineDialog.validateSuggestUrlInput()
- 位置: L175-199
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `URL.parse()`, `this._suggestUrl.value.trim()`, `this.setValidity()`, `urlString.includes()`
- 条件付き依存: `if (!urlString)` → `this.setValidity()`
- 条件付き依存: `if (!url)` → `this.setValidity()`
- 条件付き依存: `if (url.protocol != "http:" && url.protocol != "https:")` → `this.setValidity()`
- 条件付き依存: `if (!urlString.includes("%s"))` → `this.setValidity()`
- 参照: `this._suggestUrl`, `url.protocol`

## EngineDialog.validateInput()
- 位置: async L207-226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.validateAlias()`, `this.validateName()`, `this.validatePostDataInput()`, `this.validateSuggestUrlInput()`, `this.validateUrlInput()`
- 参照: `input.id`, `this._alias.id`, `this._name.id`, `this._postData.id`, `this._suggestUrl.id`, `this._url.id`

## EngineDialog.validateAll()
- 位置: async L228-232
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.validateInput()`
- 参照: `this._form.elements`

## EngineDialog.setValidity()
- 位置: L244-256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._dialog.getButton()`, `this._form.checkValidity()`
- 条件付き依存: `if (l10nId)` → `inputElement.setCustomValidity()`
- 条件付き依存: `if (l10nId)` → `l10nCache.get()`
- 条件付き依存: `if (!(l10nId))` → `inputElement.setCustomValidity()`
- 参照: `this._dialog.getButton("accept").disabled`

## EngineDialog._revealAllValidity()
- 位置: L262-266
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._revealValidity()`
- 参照: `input.validationMessage`, `this._form.elements`

## EngineDialog._revealValidity()
- 位置: L276-294
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `inputElement.parentElement.querySelector()`
- 条件付き依存: `if (validationMessage)` → `inputElement.setAttribute()`
- 条件付き依存: `if (!(validationMessage))` → `inputElement.removeAttribute()`
- 参照: `errorLabel.id`, `errorLabel.textContent`

## EngineDialog.allowedNames()
- 位置: L302-304
- 役割: (未記入)
- 触るとき: (未記入)

## EngineDialog.allowedAliases()
- 位置: L312-314
- 役割: (未記入)
- 触るとき: (未記入)

## NewEngineDialog.constructor()
- 位置: L321-328
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.setAttributes()`, `super()`, `this.validateAll()`
- 参照: `this._alias`, `this._name`, `this._url`

## NewEngineDialog.onAccept()
- 位置: L330-344
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SearchService.addUserEngine()`, `this._alias.value.trim()`, `this._name.value.trim()`, `this._postData.value.trim()`, `this._postData.value.trim().replace()`, `this._suggestUrl.value.trim()`, `this._suggestUrl.value.trim().replace()`, `this._url.value.trim()`, `this._url.value.trim().replace()`
- 参照: `params.size`

## EditEngineDialog.constructor()
- 位置: L363-405
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`, `this.getSubmissionTemplate()`, `this.validateAll()`
- 条件付き依存: `if (!(this.#engine instanceof lazy.UserSearchEngine))` → `this._name.closest()`
- 条件付き依存: `if (!(this.#engine instanceof lazy.UserSearchEngine))` → `this._url.closest()`
- 条件付き依存: `if (!(this.#engine instanceof lazy.UserSearchEngine))` → `this._dialog.getButton()`
- 条件付き依存: `if (!(this.#engine instanceof lazy.UserSearchEngine))` → `this.setValidity()`
- 条件付き依存: `if (!(this.#engine instanceof lazy.UserSearchEngine))` → `this.validateAll()`
- 条件付き依存: `if (postData || suggestUrl)` → `this.showAdvanced()`
- 参照: `engine.alias`, `engine.name`, `lazy.SearchUtils.URL_TYPE.SEARCH`, `lazy.SearchUtils.URL_TYPE.SUGGEST_JSON`, `lazy.UserSearchEngine`, `this.#engine`, `this._alias`, `this._alias.value`, `this._dialog.getButton("extra1").hidden`, `this._form.elements`, `this._name.closest(".dialogRow").hidden`, `this._name.value`, `this._postData.value`, `this._suggestUrl.value`, `this._url.closest(".dialogRow").hidden`, `this._url.value`

## EditEngineDialog.validateAll()
- 位置: async L407-415
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#engine instanceof lazy.UserSearchEngine)` → `super.validateAll()`
- 条件付き依存: `if (!(this.#engine instanceof lazy.UserSearchEngine))` → `this.validateAlias()`
- 参照: `lazy.UserSearchEngine`, `this.#engine`

## EditEngineDialog.onAccept()
- 位置: L417-454
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (this.#engine instanceof lazy.UserSearchEngine)` → `this.#engine.rename()`
- 条件付き依存: `if (this.#engine instanceof lazy.UserSearchEngine)` → `this._name.value.trim()`
- 条件付き依存: `if (this.#engine instanceof lazy.UserSearchEngine)` → `this._alias.value.trim()`
- 条件付き依存: `if (this.#engine instanceof lazy.UserSearchEngine)` → `this._url.value.trim()`
- 条件付き依存: `if (this.#engine instanceof lazy.UserSearchEngine)` → `this._postData.value.trim()`
- 条件付き依存: `if (this.#engine instanceof lazy.UserSearchEngine)` → `this.getSubmissionTemplate()`
- 条件付き依存: `if (newURL != prevURL || prevPostData != newPostData)` → `this.#engine.changeUrl()`
- 条件付き依存: `if (newURL != prevURL || prevPostData != newPostData)` → `newURL.replace()`
- 条件付き依存: `if (newURL != prevURL || prevPostData != newPostData)` → `newPostData?.replace()`
- 条件付き依存: `if (this.#engine instanceof lazy.UserSearchEngine)` → `this._suggestUrl.value.trim()`
- 条件付き依存: `if (newSuggestURL != prevSuggestUrl)` → `this.#engine.changeUrl()`
- 条件付き依存: `if (newSuggestURL != prevSuggestUrl)` → `newSuggestURL?.replace()`
- 条件付き依存: `if (this.#engine instanceof lazy.UserSearchEngine)` → `this.#engine.updateFavicon()`
- 条件付き依存: `if (!(this.#engine instanceof lazy.UserSearchEngine))` → `newAlias.trim().toLowerCase()`
- 条件付き依存: `if (!(this.#engine instanceof lazy.UserSearchEngine))` → `newAlias.trim()`
- 参照: `lazy.SearchUtils.URL_TYPE.SEARCH`, `lazy.SearchUtils.URL_TYPE.SUGGEST_JSON`, `lazy.UserSearchEngine`, `this.#engine`, `this.#engine.alias`, `this._alias.value`

## EditEngineDialog.allowedAliases()
- 位置: L456-458
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#engine.alias`

## EditEngineDialog.allowedNames()
- 位置: L460-462
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.#engine.name`

## EditEngineDialog.getSubmissionTemplate()
- 位置: L476-494
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `submission.uri.spec.replace()`, `this.#engine.getSubmission()`
- 条件付き依存: `if (submission.postData)` → `Cc["@mozilla.org/binaryinputstream;1"].createInstance()`
- 条件付き依存: `if (submission.postData)` → `binaryStream.setInputStream()`
- 条件付き依存: `if (submission.postData)` → `binaryStream .readBytes(binaryStream.available()) .replace()`
- 条件付き依存: `if (submission.postData)` → `binaryStream .readBytes()`
- 条件付き依存: `if (submission.postData)` → `binaryStream.available()`
- 参照: `Ci.nsIBinaryInputStream`, `submission.postData`, `submission.postData.data`
- XPCOM: [`nsIBinaryInputStream`](../../../../xpcom/io/nsIBinaryInputStream.idl.md) / `@mozilla.org/binaryinputstream;1`

## NewEngineFromFormDialog.constructor()
- 位置: L515-527
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.getElementById()`, `document.getElementById("enginePostDataRow").remove()`, `document.getElementById("engineUrlRow").remove()`, `document.getElementById("suggestUrlRow").remove()`, `super()`, `this._dialog.getButton()`, `this.validateAll()`
- 参照: `this._dialog.getButton("extra1").hidden`, `this._name.value`, `this._postData`, `this._suggestUrl`, `this._url`

## NewEngineFromFormDialog.onAccept()
- 位置: L529-536
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this._alias.value.trim()`, `this._name.value.trim()`
- 参照: `window.arguments`, `window.arguments[0].engineInfo`

## initL10nCache()
- 位置: async L539-557
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `document.l10n.formatValues()`, `errorIds.map()`, `l10nCache.set()`
- 参照: `errorIds.length`
