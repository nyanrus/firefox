# browser/components/search/content/addEngine.js

source: browser/components/search/content/addEngine.js
source-hash: 7b22993f35df0d0e11265cf7e37d1aff64873493
lines: 589

## <module>
- 役割: 検索エンジンの追加・編集ダイアログ(設定画面、フォームの右クリックからの追加)のスクリプト。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `Promise.withResolvers()`, `initL10nCache()`, `loadedResolvers.resolve()`, `window.addEventListener()`

## EngineDialog.constructor()
- 位置: L62-87
- 役割: フォーム要素を取得し、input で検証、フィールドを離れたときにエラー表示、Enter で全項目表示、accept と extra1 の各イベントを登録する。
- 触るとき: 入力欄を増やしたとき、またはエラーがいつ見えるかのタイミングを変えるとき。
- 呼び出し先: `document.addEventListener()`, `document.getElementById()`, `document.querySelector()`, `this._form.addEventListener()`, `this.onAccept.bind()`, `this.showAdvanced()`, `this.validateInput()`
- 条件付き依存: `if (e.target.localName == "input")` → `this._revealValidity()`
- 条件付き依存: `if (e.key == "Enter")` → `this._revealAllValidity()`
- 参照: `e.key`, `e.target`, `e.target.localName`, `e.target.validationMessage`, `this._alias`, `this._dialog`, `this._form`, `this._name`, `this._postData`, `this._suggestUrl`, `this._url`

## EngineDialog.showAdvanced()
- 位置: L96-102
- 役割: 詳細欄を表示して詳細ボタンを隠す。resize が真ならダイアログのサイズも合わせる。
- 触るとき: 詳細欄の表示条件を変えたり、読み込み前に呼んでちらつかないか確かめるとき。
- 呼び出し先: `document.getElementById()`, `this._dialog.getButton()`
- 条件付き依存: `if (resize)` → `window.resizeDialog()`
- 参照: `document.getElementById("advanced-section").hidden`, `this._dialog.getButton("extra1").hidden`

## EngineDialog.onAccept()
- 位置: L104-106
- 役割: 抽象メソッドで、呼ばれると例外を投げる。各サブクラスが保存処理を実装する。
- 触るとき: 新しいダイアログの種類を足すとき、accept 時の処理を派生クラスに書く必要がある。

## EngineDialog.validateName()
- 位置: L108-122
- 役割: 名前が空なら no-name、既存エンジンと同名で許可リストに無ければ name-exists を設定する。
- 触るとき: 検索エンジン名の入力規則やエラー文言を変えるとき。
- 呼び出し先: `lazy.SearchService.getEngineByName()`, `this._name.value.trim()`, `this.allowedNames.includes()`, `this.setValidity()`
- 条件付き依存: `if (!name)` → `this.setValidity()`
- 条件付き依存: `if (existingEngine && !this.allowedNames.includes(name))` → `this.setValidity()`
- 参照: `this._name`

## EngineDialog.validateAlias()
- 位置: async L124-138
- 役割: キーワードが空なら有効にし、既存の別エンジンと重複すれば keyword-exists を設定する。非同期で SearchService に問い合わせる。
- 触るとき: キーワードの重複判定を変えるとき、または編集時に自分のキーワードを許す仕組みを確かめるとき。
- 呼び出し先: `lazy.SearchService.getEngineByAlias()`, `this._alias.value.trim()`, `this.allowedAliases.includes()`, `this.setValidity()`
- 条件付き依存: `if (!alias)` → `this.setValidity()`
- 条件付き依存: `if (existingEngine && !this.allowedAliases.includes(alias))` → `this.setValidity()`
- 参照: `this._alias`

## EngineDialog.validateUrlInput()
- 位置: L140-164
- 役割: URL の空・不正・http(s) 以外・%s 欠落(POST データも無い場合)を順に判定し、該当するエラーを設定する。
- 触るとき: 検索 URL の入力規則を変えたり、POST データとの組み合わせ判定を見直すとき。
- 呼び出し先: `URL.parse()`, `this._postData?.value.trim()`, `this._url.value.trim()`, `this.setValidity()`, `urlString.includes()`
- 条件付き依存: `if (!urlString)` → `this.setValidity()`
- 条件付き依存: `if (!url)` → `this.setValidity()`
- 条件付き依存: `if (url.protocol != "http:" && url.protocol != "https:")` → `this.setValidity()`
- 条件付き依存: `if (!urlString.includes("%s") && !postData)` → `this.setValidity()`
- 参照: `this._url`, `url.protocol`

## EngineDialog.validatePostDataInput()
- 位置: L166-173
- 役割: POST データが空でなく %s を含まなければ missing-terms-post-data を設定する。
- 触るとき: POST データの入力規則を変えるとき。
- 呼び出し先: `postData.includes()`, `this._postData.value.trim()`, `this.setValidity()`
- 条件付き依存: `if (postData && !postData.includes("%s"))` → `this.setValidity()`
- 参照: `this._postData`

## EngineDialog.validateSuggestUrlInput()
- 位置: L175-199
- 役割: サジェスト URL の空・不正・http(s) 以外・%s 欠落を判定する。空なら有効扱い。
- 触るとき: サジェスト URL の入力規則を変えるとき。
- 呼び出し先: `URL.parse()`, `this._suggestUrl.value.trim()`, `this.setValidity()`, `urlString.includes()`
- 条件付き依存: `if (!urlString)` → `this.setValidity()`
- 条件付き依存: `if (!url)` → `this.setValidity()`
- 条件付き依存: `if (url.protocol != "http:" && url.protocol != "https:")` → `this.setValidity()`
- 条件付き依存: `if (!urlString.includes("%s"))` → `this.setValidity()`
- 参照: `this._suggestUrl`, `url.protocol`

## EngineDialog.validateInput()
- 位置: async L207-226
- 役割: 入力要素の id で検証関数を振り分ける。URL と POST データは互いの %s を見るため両方を検証する。
- 触るとき: 新しい入力欄を足して検証を結び付けるとき、または URL と POST データの連動を直すとき。
- 呼び出し先: `this.validateAlias()`, `this.validateName()`, `this.validatePostDataInput()`, `this.validateSuggestUrlInput()`, `this.validateUrlInput()`
- 参照: `input.id`, `this._alias.id`, `this._name.id`, `this._postData.id`, `this._suggestUrl.id`, `this._url.id`

## EngineDialog.validateAll()
- 位置: async L228-232
- 役割: フォーム内の全要素について validateInput を順に await する。
- 触るとき: ダイアログを開いた直後に全項目を検証し直す処理を変えるとき。
- 呼び出し先: `this.validateInput()`
- 参照: `this._form.elements`

## EngineDialog.setValidity()
- 位置: L244-256
- 役割: 要素の customValidity を l10nCache の文言で設定し、フォームが有効かで accept ボタンの無効状態を決める。エラー表示は行わない。
- 触るとき: accept ボタンの有効条件を変えるとき、またはエラー文言が出ないのに保存だけ止まる原因を調べるとき。
- 呼び出し先: `this._dialog.getButton()`, `this._form.checkValidity()`
- 条件付き依存: `if (l10nId)` → `inputElement.setCustomValidity()`
- 条件付き依存: `if (l10nId)` → `l10nCache.get()`
- 条件付き依存: `if (!(l10nId))` → `inputElement.setCustomValidity()`
- 参照: `this._dialog.getButton("accept").disabled`

## EngineDialog._revealAllValidity()
- 位置: L262-266
- 役割: フォーム内の全要素に対して _revealValidity を呼び、現在の検証結果を表示する。
- 触るとき: 送信を試みたときに全エラーを見せる挙動を変えるとき。
- 呼び出し先: `this._revealValidity()`
- 参照: `input.validationMessage`, `this._form.elements`

## EngineDialog._revealValidity()
- 位置: L276-294
- 役割: エラーラベルに検証メッセージを入れ、メッセージがあれば aria-invalid と aria-describedby を付け、無ければ外す。
- 触るとき: エラー表示や支援技術向けの属性の付け方を変えるとき。
- 呼び出し先: `inputElement.parentElement.querySelector()`
- 条件付き依存: `if (validationMessage)` → `inputElement.setAttribute()`
- 条件付き依存: `if (!(validationMessage))` → `inputElement.removeAttribute()`
- 参照: `errorLabel.id`, `errorLabel.textContent`

## EngineDialog.allowedNames()
- 位置: L302-304
- 役割: 既存でも使ってよい名前の一覧を返す。基底は空配列。
- 触るとき: 編集ダイアログで名前の重複判定から除外する対象を変えるとき。

## EngineDialog.allowedAliases()
- 位置: L312-314
- 役割: 既存でも使ってよいキーワードの一覧を返す。基底は空配列。
- 触るとき: 編集ダイアログでキーワードの重複判定から除外する対象を変えるとき。

## NewEngineDialog.constructor()
- 位置: L321-328
- 役割: 名前・URL・キーワードのプレースホルダーを設定し、初期状態の全項目を検証する。
- 触るとき: 新規追加ダイアログのプレースホルダー文言を変えるとき。
- 呼び出し先: `document.l10n.setAttributes()`, `super()`, `this.validateAll()`
- 参照: `this._alias`, `this._name`, `this._url`

## NewEngineDialog.onAccept()
- 位置: L330-344
- 役割: URL と POST データの %s を {searchTerms} に直し、SearchService.addUserEngine でユーザーエンジンを登録する。
- 触るとき: 新規追加時に登録される項目(メソッド、サジェスト URL、キーワード)を変えるとき。
- 呼び出し先: `lazy.SearchService.addUserEngine()`, `this._alias.value.trim()`, `this._name.value.trim()`, `this._postData.value.trim()`, `this._postData.value.trim().replace()`, `this._suggestUrl.value.trim()`, `this._suggestUrl.value.trim().replace()`, `this._url.value.trim()`, `this._url.value.trim().replace()`
- 参照: `params.size`

## EditEngineDialog.constructor()
- 位置: L363-405
- 役割: 既存エンジンの名前・キーワード・URL・POST データ・サジェスト URL を入力欄に入れる。ユーザーエンジン以外は名前と URL を隠し、キーワードだけ編集可能にする。
- 触るとき: 編集画面に出す項目を変えたり、組み込みエンジンでどの項目を編集させるかを変えるとき。
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
- 役割: ユーザーエンジンなら全項目、組み込みエンジンならキーワードだけを検証する。
- 触るとき: 組み込みエンジンの編集で検証の対象を変えるとき。
- 条件付き依存: `if (this.#engine instanceof lazy.UserSearchEngine)` → `super.validateAll()`
- 条件付き依存: `if (!(this.#engine instanceof lazy.UserSearchEngine))` → `this.validateAlias()`
- 参照: `lazy.UserSearchEngine`, `this.#engine`

## EditEngineDialog.onAccept()
- 位置: L417-454
- 役割: ユーザーエンジンは名前、キーワード、変更された URL とサジェスト URL を反映し、アイコンを更新する。組み込みエンジンはキーワードだけを小文字にして保存する。
- 触るとき: 編集の保存時に反映される項目や、URL が変わったときだけ changeUrl を呼ぶ条件を変えるとき。
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
- 役割: 編集中エンジン自身のキーワードを、重複判定で許す一覧として返す。
- 触るとき: 編集時に自分のキーワードが重複扱いされないか確かめるとき。
- 参照: `this.#engine.alias`

## EditEngineDialog.allowedNames()
- 位置: L460-462
- 役割: 編集中エンジン自身の名前を、重複判定で許す一覧として返す。
- 触るとき: 編集時に自分の名前が重複扱いされないか確かめるとき。
- 参照: `this.#engine.name`

## EditEngineDialog.getSubmissionTemplate()
- 位置: L476-494
- 役割: 指定した種類の送信 URL と POST データを取り出し、searchTerms を %s に戻す。無ければ両方 null を返す。
- 触るとき: 編集画面に既存の URL を表示する仕組みを変えたり、URL の変更有無を比べる処理を調べるとき。
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
- 役割: URL・サジェスト・POST データの行を削除し、名前欄に nameTemplate を入れて検証する。
- 触るとき: フォームからの追加ダイアログに出す入力欄を変えるとき。
- 呼び出し先: `document.getElementById()`, `document.getElementById("enginePostDataRow").remove()`, `document.getElementById("engineUrlRow").remove()`, `document.getElementById("suggestUrlRow").remove()`, `super()`, `this._dialog.getButton()`, `this.validateAll()`
- 参照: `this._dialog.getButton("extra1").hidden`, `this._name.value`, `this._postData`, `this._suggestUrl`, `this._url`

## NewEngineFromFormDialog.onAccept()
- 位置: L529-536
- 役割: 入力された名前とキーワードを window.arguments[0].engineInfo に入れて呼び出し元へ返す。エンジンは登録しない。
- 触るとき: フォームからの追加で呼び出し元に返す値の形式を変えるとき。
- 呼び出し先: `this._alias.value.trim()`, `this._name.value.trim()`
- 参照: `window.arguments`, `window.arguments[0].engineInfo`

## initL10nCache()
- 位置: async L539-557
- 役割: エラー文言の id を一括で整形し、l10nCache の Map に格納する。
- 触るとき: 検証エラーの文言 id を新しく足すとき、その id をここにも加えないと文言が出ない。
- 呼び出し先: `document.l10n.formatValues()`, `errorIds.map()`, `l10nCache.set()`
- 参照: `errorIds.length`
