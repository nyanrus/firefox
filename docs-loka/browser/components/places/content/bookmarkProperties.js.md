# browser/components/places/content/bookmarkProperties.js

source: browser/components/places/content/bookmarkProperties.js
source-hash: c16b1d8239147c220376beabc4e16eff10fc8638
lines: 519

## <module>
- 役割: ブックマークのプロパティダイアログ。window.arguments[0] の add/edit 指定に従い、項目の新規作成または既存項目の編集を行う。
- 呼び出し先: `BookmarkPropertiesPanel.onDialogLoad()`, `BookmarkPropertiesPanel.onDialogLoad() .catch()`, `BookmarkPropertiesPanel.onDialogLoad() .catch(ex => console.error(`Failed to initialize dialog: ${ex}`)) .then()`, `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyScriptGetter()`, `console.error()`, `document.addEventListener()`, `window.sizeToContent()`

## _strings()
- 位置: L82-87
- 役割: ダイアログ用の文字列バンドル (stringBundle 要素) を遅延取得して返す。
- 触るとき: ダイアログの表示文字列を追加・差し替えるとき、または文字列 ID が見つからない不具合を調べるとき。
- 条件付き依存: `if (!this.__strings)` → `document.getElementById()`
- 参照: `this.__strings`

## BPP__getAcceptLabel()
- 位置: L106-108
- 役割: 確定ボタンのラベルを dialogAcceptLabelSaveItem から取得して返す。
- 触るとき: 確定ボタンの文言を追加や変更するとき、追加と編集で異なるラベルを出し分けたいとき。
- 呼び出し先: `this._strings.getString()`

## BPP__getDialogTitle()
- 位置: L115-139
- 役割: action と itemType の組み合わせから、ダイアログのタイトル文字列を選んで返す。フォルダー追加でURIListがあれば複数追加用のタイトルになる。
- 触るとき: ブックマーク追加・フォルダー追加・編集のどのタイトルが出るかを変えるとき、タイトルが想定と違う原因を調べるとき。
- 条件付き依存: `if (this._itemType == BOOKMARK_ITEM)` → `this._strings.getString()`
- 条件付き依存: `if (this._URIs.length)` → `this._strings.getString()`
- 条件付き依存: `if (this._action == ACTION_ADD)` → `this._strings.getString()`
- 条件付き依存: `if (this._itemType === BOOKMARK_ITEM)` → `this._strings.getString()`
- 条件付き依存: `if (this._action == ACTION_EDIT)` → `this._strings.getString()`
- 参照: `this._URIs.length`, `this._action`, `this._itemType`

## _determineItemInfo()
- 位置: async L144-219
- 役割: window.arguments[0] を読み、add なら type・title・挿入先・URI やキーワードを設定し、edit なら node からタイトルと種別を決める。
- 触るとき: ダイアログに渡す引数の項目を追加・変更するとき、add 時の既定タイトルや既定の挿入先 (defaultParentGuid) を変えたいとき。
- 条件付き依存: `if (typeof this._title != "string")` → `PlacesUtils.history.fetch()`
- 条件付き依存: `if (!("uri" in dialogInfo))` → `Services.io.newURI()`
- 条件付き依存: `if (!("uri" in dialogInfo))` → `this._strings.getString()`
- 条件付き依存: `if ("URIList" in dialogInfo)` → `this._strings.getString()`
- 条件付き依存: `if (!("URIList" in dialogInfo))` → `this._strings.getString()`
- 条件付き依存: `if (!(this._action == ACTION_ADD))` → `PlacesUtils.nodeIsFolderOrShortcut()`
- 条件付き依存: `if (!(PlacesUtils.nodeIsFolderOrShortcut(this._node)))` → `PlacesUtils.nodeIsURI()`
- 参照: `Ci.nsIURI`, `PlacesUIUtils.defaultParentGuid`, `dialogInfo.URIList`, `dialogInfo.action`, `dialogInfo.charSet`, `dialogInfo.defaultInsertionPoint`, `dialogInfo.hiddenRows`, `dialogInfo.keyword`, `dialogInfo.node`, `dialogInfo.postData`, `dialogInfo.title`, `dialogInfo.type`, `dialogInfo.uri`, `this._URIs`, `this._action`, `this._charSet`, `this._defaultInsertionPoint`, `this._dummyItem`, `this._hiddenRows`, `this._isAddKeywordDialog`, `this._itemType`, `this._keyword`, `this._node`, `this._node.title`, `this._postData`, `this._title`, `this._uri`, `this._uri.spec`, `window.arguments`
- XPCOM: [`nsIURI`](../../../../docshell/base/nsIDocShell.idl.md) / `Services.io`

## onDialogLoad()
- 位置: async L225-251
- 役割: dialogaccept/cancel/unload のリスナーを登録し、確定ボタンを無効化してから項目情報とタイトル・アイコンを決め、_initDialog を呼ぶ。
- 触るとき: ダイアログ起動時の初期化順序を変えるとき、初期化の途中で確定ボタンが有効になってしまう問題を調べるとき。
- 呼び出し先: `JSON.stringify()`, `document .getElementById()`, `document .getElementById("bookmarkpropertiesdialog") .getButton()`, `document.addEventListener()`, `document.documentElement.setAttribute()`, `this._determineItemInfo()`, `this._getDialogTitle()`, `this._getIconUrl()`, `this._initDialog()`, `this.onDialogAccept()`, `this.onDialogCancel()`, `this.onDialogUnload()`, `window.addEventListener()`
- 条件付き依存: `if (iconUrl)` → `document.documentElement.style.setProperty()`
- 参照: `acceptButton.disabled`, `document.title`

## _getIconUrl()
- 位置: L253-261
- 役割: ダイアログ上部に出すアイコンの URL を返す。編集中のブックマークは node.icon、それ以外は bookmark-hollow.svg。
- 触るとき: ダイアログのアイコン表示を変えるとき、編集対象のブックマークでアイコンが出ないときに調べるとき。
- 参照: `this._action`, `this._itemType`, `window.arguments`, `window.arguments[0]?.node?.icon`

## _initDialog()
- 位置: async L267-353
- 役割: 行の表示変化に合わせてダイアログをリサイズする監視を仕掛け、編集または新規作成のパネルを初期化して、最後に確定ボタンの有効状態を決める。
- 触るとき: ダイアログの行表示やリサイズの挙動を変えるとき、新規追加で確定ボタンが無効のまま残る問題を調べるとき。
- 呼び出し先: `document .getElementById()`, `document .getElementById("bookmarkpropertiesdialog") .getButton()`, `gEditItemOverlay.initPanel()`, `target.classList.contains()`, `target.hasAttribute()`, `this._element()`, `this._getAcceptLabel()`, `this._mutationObserver.observe()`, `this._promiseNewItem()`
- 条件付き依存: `if (hidden)` → `this._mutationObserver._heightsById.get()`
- 条件付き依存: `if (hidden)` → `window.resizeBy()`
- 条件付き依存: `if (!(hidden))` → `target.getBoundingClientRect()`
- 条件付き依存: `if (!(hidden))` → `this._mutationObserver._heightsById.set()`
- 条件付き依存: `if (!(hidden))` → `window.resizeBy()`
- 条件付き依存: `if (target.classList.contains("hideable") && hidden != wasHidden)` → `window.sizeToContent()`
- 条件付き依存: `if (this._itemType == BOOKMARK_ITEM)` → `this._inputIsValid()`
- 条件付き依存: `if (this._itemType == BOOKMARK_ITEM)` → `this._element("locationField").addEventListener()`
- 条件付き依存: `if (this._itemType == BOOKMARK_ITEM)` → `this._element()`
- 条件付き依存: `if (this._isAddKeywordDialog)` → `this._element("keywordField").addEventListener()`
- 条件付き依存: `if (this._isAddKeywordDialog)` → `this._element()`
- 参照: `acceptButton.disabled`, `acceptButton.label`, `gEditItemOverlay.readOnly`, `locationField.value`, `target.getBoundingClientRect().height`, `target.id`, `this._action`, `this._hiddenRows`, `this._isAddKeywordDialog`, `this._itemType`, `this._mutationObserver`, `this._mutationObserver._heightsById`, `this._node`, `this._node.children?.length`, `this._postData`

## BPP_handleEvent()
- 位置: L356-371
- 役割: location・keyword 欄の input イベントを受け、入力が有効な URI かどうかで確定ボタンの有効状態を切り替える。
- 触るとき: URL やキーワードの入力検証で確定ボタンの状態がおかしいとき、入力欄の判定条件を変えるとき。
- 条件付き依存: `if ( target.id == "editBMPanel_locationField" || target.id == "editBMPanel_keywordField" )` → `document .getElementById("bookmarkpropertiesdialog") .getButton()`
- 条件付き依存: `if ( target.id == "editBMPanel_locationField" || target.id == "editBMPanel_keywordField" )` → `document .getElementById()`
- 条件付き依存: `if ( target.id == "editBMPanel_locationField" || target.id == "editBMPanel_keywordField" )` → `this._inputIsValid()`
- 参照: `aEvent.target`, `aEvent.type`, `document .getElementById("bookmarkpropertiesdialog") .getButton("accept").disabled`, `target.id`

## BPP__element()
- 位置: L376-378
- 役割: editBMPanel_ を前置した ID で DOM 要素を取得する。
- 触るとき: ダイアログ内の入力欄を新たに参照するとき、editBMPanel_ 接頭辞の ID が見つからないときに確認するとき。
- 呼び出し先: `document.getElementById()`

## onDialogUnload()
- 位置: L380-389
- 役割: リサイズ用の MutationObserver を切断し、location・keyword 欄の input リスナーを外す。
- 触るとき: ダイアログを閉じたときのクリーンアップを増やすとき、閉じた後も監視やリスナーが残るような不具合を調べるとき。
- 呼び出し先: `this._element()`, `this._element("keywordField").removeEventListener()`, `this._element("locationField").removeEventListener()`, `this._mutationObserver.disconnect()`
- 参照: `this._mutationObserver`

## onDialogAccept()
- 位置: L391-403
- 役割: フォーカス中の要素を blur して変更を確定させ、bookmarkState を引数に載せたうえで gEditItemOverlay を終了し、作成・編集された guid を bookmarkGuid に入れる。
- 触るとき: 確定時に呼び出し元へ返す値 (bookmarkState や bookmarkGuid) を変えるとき、確定時の未保存変更が反映されない問題を調べるとき。
- 呼び出し先: `document.commandDispatcher.focusedElement?.blur()`, `gEditItemOverlay.uninitPanel()`
- 参照: `gEditItemOverlay._bookmarkState`, `this._node.bookmarkGuid`, `window.arguments`, `window.arguments[0].bookmarkGuid`, `window.arguments[0].bookmarkState`

## onDialogCancel()
- 位置: L405-409
- 役割: キャンセル時に gEditItemOverlay を終了する。途中の変更がトランザクションとして残らないよう、先に uninit する。
- 触るとき: キャンセル時の後始末を変えるとき、キャンセル後に余計な変更が保存されてしまう不具合を調べるとき。
- 呼び出し先: `gEditItemOverlay.uninitPanel()`

## BPP__inputIsValid()
- 位置: L416-431
- 役割: ブックマークなら location 欄が有効な URI か、キーワード追加ならキーワードが空でないかを確かめ、両方満たすと true を返す。
- 触るとき: 確定ボタンを有効にする入力条件を変えるとき、キーワード追加ダイアログで空のキーワードが通ってしまう問題を調べるとき。
- 呼び出し先: `this._containsValidURI()`, `this._element()`
- 参照: `this._element("keywordField").value.length`, `this._isAddKeywordDialog`, `this._itemType`

## BPP__containsValidURI()
- 位置: L442-451
- 役割: 指定 ID の入力欄の値を Services.uriFixup.getFixupURIInfo に渡し、例外なく通れば true を返す。空値や例外は false。
- 触るとき: URL の有効性判定を変えるとき、有効な URL が無効扱いされる原因を調べるとき。
- 呼び出し先: `this._element()`
- 条件付き依存: `if (value)` → `Services.uriFixup.getFixupURIInfo()`
- 参照: `this._element(aTextboxID).value`
- XPCOM: `Services.uriFixup`

## _getInsertionPointDetails()
- 位置: async L461-466
- 役割: 既定の挿入点から、挿入位置 (getIndex の結果) と親の guid を配列で返す。
- 触るとき: 新規項目の挿入位置や親フォルダーの決め方を変えるとき。JSDoc の戻り値の説明は実際の順序 (index, guid) と異なるので注意。
- 呼び出し先: `this._defaultInsertionPoint.getIndex()`
- 参照: `this._defaultInsertionPoint.guid`

## _promiseNewItem()
- 位置: async L468-509
- 役割: 新規項目の情報を組み立てる。ブックマークなら URL・キーワード・POST データを、フォルダーなら URIList を子として持たせ、未保存の仮ノードをフリーズして返す。
- 触るとき: 新規追加ダイアログで作られる項目の内容 (URL、キーワード、フォルダー内の子) を変えるとき、追加直後にノードの情報がずれる問題を調べるとき。
- 呼び出し先: `Object.freeze()`, `this._getInsertionPointDetails()`
- 条件付き依存: `if (this._charSet)` → `PlacesUIUtils.setCharsetForPage(this._uri, this._charSet, window).catch()`
- 条件付き依存: `if (this._charSet)` → `PlacesUIUtils.setCharsetForPage()`
- 条件付き依存: `if (this._itemType == BOOKMARK_FOLDER)` → `this._URIs.map()`
- 参照: `Ci.nsINavHistoryResultNode.RESULT_TYPE_FOLDER`, `Ci.nsINavHistoryResultNode.RESULT_TYPE_URI`, `PlacesUtils.bookmarks.unsavedGuid`, `console.error`, `info.children`, `info.keyword`, `info.postData`, `info.url`, `item.title`, `item.uri`, `this._charSet`, `this._itemType`, `this._keyword`, `this._postData`, `this._title`, `this._uri`, `this._uri.spec`
- XPCOM: [`nsINavHistoryResultNode`](../../../../toolkit/components/places/nsINavHistoryService.idl.md)
