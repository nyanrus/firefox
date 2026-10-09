# browser/base/content/pageinfo/pageInfo.js

source: browser/base/content/pageinfo/pageInfo.js
source-hash: 1ba2ac6861b409a4afb898220d67a0a40d220484
lines: 1330

## <module>
- 役割: ページ情報ダイアログ(pageInfo.xhtml)の本体スクリプト。一般・メディア・権限・セキュリティの各タブを読み込み、画像一覧(nsITreeView)の描画と並べ替えを担い、メディアの保存とプレビューを扱う。
- 呼び出し先: `Cc[ "@mozilla.org/netwerk/cache-storage-service;1" ].getService()`, `ChromeUtils.defineESModuleGetters()`, `getClipboardHelper()`, `window.addEventListener()`

## pageInfoTreeView()
- 位置: L17-28
- 役割: nsITreeView を模した行データのオブジェクトを作る。treeid(対象の tree 要素)と、コピー対象の列番号を保持する。
- 触るとき: 新しいツリー(メタ情報や画像一覧)をページ情報に追加するとき。
- 参照: `this.copycol`, `this.data`, `this.rows`, `this.selection`, `this.sortcol`, `this.sortdir`, `this.tree`, `this.treeid`

## rowCount()
- 位置: L31-33
- 役割: rowCount への代入を禁止し、読み取り専用として例外を投げる。
- 触るとき: ツリーに rowCount を書き込もうとして例外が出る原因を調べるとき。

## rowCount()
- 位置: L34-36
- 役割: 内部の rows の値を返す。
- 触るとき: ツリーの行数の扱いを変えるとき。
- 参照: `this.rows`

## setTree()
- 位置: L38-40
- 役割: ツリー要素の参照を保持する。
- 触るとき: ツリーとビューの接続順を変えるとき。
- 参照: `this.tree`

## getCellText()
- 位置: L42-48
- 役割: 指定の行と列のセル文字列を data から返す。値が無ければ空文字を返す。
- 触るとき: ツリーの表示文字列の内容がずれるとき、または列を追加するとき。
- 参照: `column.index`, `this.data`

## setCellValue()
- 位置: L50-50
- 役割: 空の実装で、値の書き込みは何もしない。
- 触るとき: チェックボックス等の値を編集可能にする要件が出たときに見る。

## setCellText()
- 位置: L52-54
- 役割: 指定の行と列の data の値を書き換える。
- 触るとき: ツリーの行データを表示中に差し替える処理を書くとき。
- 参照: `column.index`, `this.data`

## addRow()
- 位置: L56-62
- 役割: 行を末尾に追加してツリーに通知し、選択が無くかつ画像要素の指定が無ければ先頭行を選択する。
- 触るとき: 行が追加されたときの自動選択の挙動を変えるとき、またはメディア一覧が空から埋まるときの動きを調べるとき。
- 呼び出し先: `this.data.push()`, `this.rowCountChanged()`
- 条件付き依存: `if (this.selection.count == 0 && this.rowCount && !gImageElement)` → `this.selection.select()`
- 参照: `this.rowCount`, `this.rows`, `this.selection.count`

## addRows()
- 位置: L64-68
- 役割: 渡された配列の各行について addRow を順に呼ぶ。
- 触るとき: メタ情報タブなどにまとめて行を入れる処理を変えるとき。
- 呼び出し先: `this.addRow()`

## rowCountChanged()
- 位置: L70-72
- 役割: 行数の増減をツリー要素の rowCountChanged に伝える。
- 触るとき: 行の増減が画面に反映されないときに調べる。
- 呼び出し先: `this.tree.rowCountChanged()`

## invalidate()
- 位置: L74-76
- 役割: ツリー全体の再描画をツリー要素に依頼する。
- 触るとき: ツリーの表示が古いまま残るときに呼び出し元を確認する。
- 呼び出し先: `this.tree.invalidate()`

## clear()
- 位置: L78-84
- 役割: ツリーに全行の削除を通知し、行数と data を空にする。
- 触るとき: ページ情報の再読み込みで一覧を空にする処理を変えるとき。
- 条件付き依存: `if (this.tree)` → `this.tree.rowCountChanged()`
- 参照: `this.data`, `this.rows`, `this.tree`

## onPageMediaSort()
- 位置: L86-113
- 役割: メタ情報ツリーの列見出しがクリックされたとき、大文字小文字を区別せず並べ替え、見出しの昇順・降順の属性を更新する。
- 触るとき: メタ情報タブの並べ替え方法や見出しの表示を変えるとき。
- 呼び出し先: `col.element.removeAttribute()`, `document.getElementById()`, `gTreeUtils.sort()`, `tree.columns.getNamedColumn()`, `treecol.element.setAttribute()`
- 参照: `this.data`, `this.sortcol`, `this.sortdir`, `this.treeid`, `tree.columns`, `treecol.index`

## textComparator()
- 位置: L95-97
- 役割: 両方を小文字にして localeCompare で比べる。null は空文字として扱う。
- 触るとき: 文字列の並べ替え順序を変えるとき。同名の関数が画像一覧にもある。
- 呼び出し先: `(a || "").toLowerCase()`, `(a || "").toLowerCase().localeCompare()`, `(b || "").toLowerCase()`

## getRowProperties()
- 位置: L115-117
- 役割: 行の属性として空文字を返す。
- 触るとき: 行ごとに CSS 状態を付けたいとき。

## getCellProperties()
- 位置: L118-120
- 役割: セルの属性として空文字を返す。
- 触るとき: セル単位の見た目を変えたいとき(画像一覧は gImageView 側で上書きしている)。

## getColumnProperties()
- 位置: L121-123
- 役割: 列の属性として空文字を返す。
- 触るとき: 列ごとの属性を付けたいとき。

## isContainer()
- 位置: L124-126
- 役割: 常に false を返し、ツリー行をコンテナにしない。
- 触るとき: 階層付きの表にする変更をするとき。

## isContainerOpen()
- 位置: L127-129
- 役割: 常に false を返す。
- 触るとき: コンテナを使う変更をするとき。

## isSeparator()
- 位置: L130-132
- 役割: 常に false を返し、区切り行を作らない。
- 触るとき: 区切り行を入れたいとき。

## isSorted()
- 位置: L133-135
- 役割: sortcol が -1 より大きいときに true を返し、並べ替え中かを示す。
- 触るとき: 並べ替え表示の状態判定を変えるとき。
- 参照: `this.sortcol`

## canDrop()
- 位置: L136-138
- 役割: 常に false を返し、ドロップを受け付けない。
- 触るとき: ツリーへのドロップ操作を許可するとき。

## drop()
- 位置: L139-141
- 役割: 常に false を返し、ドロップ処理を行わない。
- 触るとき: ドロップ処理を追加するとき。

## getParentIndex()
- 位置: L142-144
- 役割: 常に 0 を返す。
- 触るとき: 階層表示を導入するとき。

## hasNextSibling()
- 位置: L145-147
- 役割: 常に false を返す。
- 触るとき: 階層表示を導入するとき。

## getLevel()
- 位置: L148-150
- 役割: 常に 0 を返す。
- 触るとき: 階層表示を導入するとき。

## getImageSrc()
- 位置: L151-151
- 役割: 空の実装で、画像アイコンは使わない。
- 触るとき: 行にアイコンを付けるとき。

## getCellValue()
- 位置: L152-155
- 役割: 列が指定されなければ copycol を使い、そのセルの値を返す。行や列が負なら空文字を返す。コピー処理が使う。
- 触るとき: コピーされる値の列を変えるとき、またはコピー結果が空になる理由を調べるとき。
- 参照: `this.copycol`, `this.data`

## toggleOpenState()
- 位置: L156-156
- 役割: 空の実装。
- 触るとき: コンテナ開閉を実装するとき。

## cycleHeader()
- 位置: L157-157
- 役割: 空の実装。
- 触るとき: 見出しのキー操作を実装するとき。

## selectionChanged()
- 位置: L158-158
- 役割: 空の実装。選択変更時に何もしない。
- 触るとき: 選択変更に応じた処理を入れるとき。

## cycleCell()
- 位置: L159-159
- 役割: 空の実装。
- 触るとき: セルのキー操作を実装するとき。

## isEditable()
- 位置: L160-162
- 役割: 常に false を返し、セルを編集不可にする。
- 触るとき: セル編集を許可するとき。

## gImageView.getCellProperties()
- 位置: L188-205
- 役割: 画像一覧のセル属性を決める。ページ上の画像として読めない行や embed、画像でない object には broken を付け、アドレス列には ltr を付ける。
- 触るとき: 壊れた画像の表示や、アドレス欄の書字方向を変えるとき。
- 呼び出し先: `HTMLEmbedElement.isInstance()`, `HTMLObjectElement.isInstance()`, `checkProtocol()`, `item.type.startsWith()`
- 参照: `col.element.id`, `gImageView.data`

## gImageView.onPageMediaSort()
- 位置: L207-249
- 役割: 画像一覧の列見出しが押されたとき並べ替える。サイズと件数は数値として比べ、サイズは生の値の列で比べる。その他は大文字小文字を区別せず文字列で比べる。
- 触るとき: 画像一覧の並べ替え規則を変えるとき。
- 呼び出し先: `col.element.removeAttribute()`, `document.getElementById()`, `gTreeUtils.sort()`, `tree.columns.getNamedColumn()`, `treecol.element.setAttribute()`
- 参照: `this.data`, `this.sortcol`, `this.sortdir`, `this.treeid`, `tree.columns`, `treecol.index`

## numComparator()
- 位置: L214-216
- 役割: 2つの数値の差を返して数値順に並べる。
- 触るとき: 数値列の並べ替えを変えるとき。

## textComparator()
- 位置: L223-225
- 役割: 画像一覧用の文字列比較。大文字小文字を無視して localeCompare する。
- 触るとき: 画像一覧の文字列の並べ替え順序を変えるとき。
- 呼び出し先: `(a || "").toLowerCase()`, `(a || "").toLowerCase().localeCompare()`, `(b || "").toLowerCase()`

## getClipboardHelper()
- 位置: L274-283
- 役割: クリップボードヘルパーのサービスを取得する。失敗したら null を返す。
- 触るとき: コピー機能が使えない原因を調べるとき。
- 呼び出し先: `Cc["@mozilla.org/widget/clipboardhelper;1"].getService()`
- 参照: `Ci.nsIClipboardHelper`
- XPCOM: `nsIClipboardHelper` / `@mozilla.org/widget/clipboardhelper;1`

## onLoadPageInfo()
- 位置: async L294-418
- 役割: ウィンドウ読み込み時に一度だけ動き、表示文字列を取得し、ツリーの初期化、列見出しとコマンドのイベント設定を行い、loadTab で初期タブを開き page-info-init を発火する。
- 触るとき: ページ情報の起動時の初期化順序を変えるとき、またはテストが待つ初期化イベントを調べるとき。
- 呼び出し先: `doHelpButton()`, `doSelectAllMedia()`, `document .getElementById()`, `document .getElementById("metatree") .controllers.appendController()`, `document .querySelector()`, `document .querySelector("#imagetree > treecols") .addEventListener()`, `document .querySelector("#metatree > treecols") .addEventListener()`, `document.addEventListener()`, `document.getElementById()`, `document.l10n.formatValues()`, `event.target.id.slice()`, `gImageView.onPageMediaSort()`, `gMetaView.onPageMediaSort()`, `imageTree.controllers.appendController()`, `imagetree.addEventListener()`, `loadTab()`, `onBeginLinkDrag()`, `saveMedia()`, `security.clearSiteData()`, `security.viewCert()`, `security.viewPasswords()`, `security.viewQWAC()`, `showTab()`, `window.close()`, `window.dispatchEvent()`
- 参照: `MEDIA_STRINGS.audio`, `MEDIA_STRINGS.cursor`, `MEDIA_STRINGS.embed`, `MEDIA_STRINGS.img`, `MEDIA_STRINGS.input`, `MEDIA_STRINGS.link`, `MEDIA_STRINGS.object`, `MEDIA_STRINGS.video`, `event.target.id`, `imageTree.view`, `window.arguments`, `window.arguments.length`

## loadPageInfo()
- 位置: async L422-450
- 役割: PageInfo アクターからページの情報を取り、一般・権限・セキュリティを構成したあと、フレームの browsingContext を順にたどってメディア情報を addImage で一覧に追加する。
- 触るとき: フレームを含むページのメディア収集の範囲や順序を変えるとき。
- 呼び出し先: `actor.sendQuery()`, `addImage()`, `browsingContext.currentWindowGlobal.getActor()`, `contextsToVisit.pop()`, `contextsToVisit.push()`, `global.getActor()`, `onNonMediaPageInfoLoad()`, `selectImage()`, `subframeActor.sendQuery()`
- 参照: `browser.browsingContext`, `contextsToVisit.length`, `currContext.children`, `currContext.currentWindowGlobal`, `mediaResult.mediaItems`, `window.opener.gBrowser.selectedBrowser`

## createPreviewBrowserElement()
- 位置: L453-474
- 役割: メディアプレビュー用のリモート browser 要素を作り、既存の mediaBrowser と差し替える。remoteType、ブラウジングコンテキストのグループ、userContextId を引き継ぐ。
- 触るとき: プレビューが別プロセスや別コンテナで動くべき条件を変えるとき。
- 呼び出し先: `document.createXULElement()`, `document.getElementById()`, `document.getElementById("mediaBrowser").replaceWith()`, `previewBrowser.setAttribute()`
- 条件付き依存: `if (userContextId)` → `previewBrowser.setAttribute()`
- 参照: `browser.browsingContext.group.id`, `browser.remoteType`, `docInfo.principal.originAttributes`

## onNonMediaPageInfoLoad()
- 位置: async L480-519
- 役割: メディア以外のタブを読み込む。タイトル、プレビュー browser、一般タブを設定し、エラーページでは browser の URI と principal に置き換えて、権限タブとセキュリティタブを読み込む。
- 触るとき: エラーページのときに見る URI を変えるとき、または一般・権限・セキュリティの読み込み順を変えるとき。
- 呼び出し先: `Services.io.newURI()`, `createPreviewBrowserElement()`, `document .getElementById()`, `document .getElementById("main-window") .setAttribute()`, `document.l10n.setAttributes()`, `makeGeneralTab()`, `onLoadPermission()`, `securityOnLoad()`, `uri.spec.startsWith()`
- 条件付き依存: `if ( uri.spec.startsWith("about:neterror") || uri.spec.startsWith("about:certerror") || uri.spec.startsWith("about:httpsonlyerror") )` → `Services.scriptSecurityManager.createContentPrincipal()`
- 参照: `browser.contentPrincipal.originAttributes`, `browser.currentURI`, `browsingContext.top.embedderElement`, `docInfo.documentURIObject.spec`, `docInfo.location`, `docInfo.principal`, `document.documentElement`, `pageInfoData.metaViewRows`, `windowInfo.isTopWindow`
- XPCOM: `Services.io` / `Services.scriptSecurityManager`

## resetPageInfo()
- 位置: L521-535
- 役割: メタ情報と画像一覧を空にし、メディアタブを隠して loadTab で作り直す。
- 触るとき: ページ情報を開いたままページの内容が変わったときの再構築を変えるとき。
- 呼び出し先: `document.getElementById()`, `gImageView.clear()`, `gMetaView.clear()`, `loadTab()`
- 参照: `mediaTab.hidden`

## doHelpButton()
- 位置: L537-548
- 役割: 選択中のパネルの id を見てヘルプの項目(一般、メディア、権限、セキュリティ)を決め、ヘルプリンクを開く。
- 触るとき: パネルごとのヘルプの対応を追加・変更するとき。
- 呼び出し先: `document.getElementById()`, `openHelpLink()`
- 参照: `deck.selectedPanel.id`

## showTab()
- 位置: L550-554
- 役割: id に Panel を付けた要素を mainDeck の選択パネルにする。
- 触るとき: タブの切り替え先のパネル名を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `deck.selectedPanel`

## loadTab()
- 位置: async L556-588
- 役割: 初回だけ partitionKey 付きのディスクキャッシュを作り、loadPageInfo でページ情報を読んだあと、args.initialTab(無ければ一般タブ)を選んで doCommand で表示する。
- 触るとき: ページ情報を開くときの初期タブの決め方や、キャッシュの作り方を変えるとき。
- 呼び出し先: `document.getElementById()`, `loadPageInfo()`, `radioGroup.focus()`, `radioGroup.selectedItem.doCommand()`
- 条件付き依存: `if (!diskStorage)` → `getOaWithPartitionKey()`
- 条件付き依存: `if (!diskStorage)` → `Services.loadContextInfo.custom()`
- 条件付き依存: `if (!diskStorage)` → `cacheService.diskCacheStorage()`
- 参照: `args?.browser`, `args?.browsingContext`, `args?.imageElement`, `args?.initialTab`, `radioGroup.selectedItem`
- XPCOM: `Services.loadContextInfo`

## openCacheEntry()
- 位置: L590-605
- 役割: 指定 URL のキャッシュエントリを読み取り専用で開き、ENTRY_WANTED で cb にエントリを渡す。エントリが無い場合は cb に null が渡る。
- 触るとき: キャッシュからサイズや種類を読む処理を追加するとき、または読めない原因を調べるとき。
- 呼び出し先: `Services.io.newURI()`, `diskStorage.asyncOpenURI()`
- 参照: `nsICacheStorage.OPEN_READONLY`
- XPCOM: `Services.io`

## onCacheEntryCheck()
- 位置: L592-594
- 役割: キャッシュを開くときの確認コールバック。常に ENTRY_WANTED を返し、既存のエントリを使うよう伝える。
- 触るとき: キャッシュ読み取りで新規作成や再取得をさせたくなったときに、この戻り値を変える。
- 参照: `Ci.nsICacheEntryOpenCallback.ENTRY_WANTED`
- XPCOM: [`nsICacheEntryOpenCallback`](../../../../netwerk/cache2/nsICacheEntryOpenCallback.idl.md)

## onCacheEntryAvailable()
- 位置: L595-597
- 役割: キャッシュエントリが用意できたとき、受け取った cb にそのエントリを渡す。
- 触るとき: キャッシュの読み取り結果を呼び出し側に返す経路を変えるとき。
- 呼び出し先: `cb()`

## makeGeneralTab()
- 位置: async L607-678
- 役割: 一般タブの欄を埋める。タイトル、URL、参照元、互換モード、MIME、文字コード、メタ情報の件数と行、更新日時、キャッシュからのサイズを順に設定する。
- 触るとき: 一般タブに表示する項目を増減するとき、または項目が空になる条件を調べるとき。
- 呼び出し先: `document.getElementById()`, `document.l10n.formatValue()`, `document.l10n.setAttributes()`, `formatDate()`, `openCacheEntry()`, `setItemValue()`, `url.replace()`
- 条件付き依存: `if (docInfo.title)` → `document.getElementById()`
- 条件付き依存: `if (!(docInfo.title))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(docInfo.title))` → `document.getElementById()`
- 条件付き依存: `if (!(!length))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(!length))` → `document.getElementById()`
- 条件付き依存: `if (!(!length))` → `gMetaView.addRows()`
- 条件付き依存: `if (!(!length))` → `metaGroup.style.removeProperty()`
- 条件付き依存: `if (cacheEntry)` → `formatNumber()`
- 条件付き依存: `if (cacheEntry)` → `Math.round()`
- 条件付き依存: `if (cacheEntry)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (cacheEntry)` → `document.getElementById()`
- 条件付き依存: `if (!(cacheEntry))` → `setItemValue()`
- 参照: `cacheEntry.dataSize`, `docInfo.characterSet`, `docInfo.compatMode`, `docInfo.contentType`, `docInfo.lastModified`, `docInfo.location`, `docInfo.referrer`, `docInfo.title`, `document.getElementById("encodingtext").value`, `document.getElementById("metatree").view`, `document.getElementById("modifiedtext").value`, `document.getElementById("titletext").value`, `metaGroup.style.visibility`, `metaViewRows.length`

## addImage()
- 位置: async L680-748
- 役割: 画像1件を一覧に加える。URL と種類と代替文字列が同じものは件数だけ増やし、新規のものは行を追加して、キャッシュからサイズを非同期に入れる。最初の1件でメディアタブを表示する。
- 触るとき: 画像の重複判定や件数の集計、メディアタブの表示条件を変えるとき。
- 呼び出し先: `gImageHash.hasOwnProperty()`, `gImageHash[url].hasOwnProperty()`, `gImageHash[url][type].hasOwnProperty()`
- 条件付き依存: `if (!gImageHash[url][type].hasOwnProperty(alt))` → `gImageView.addRow()`
- 条件付き依存: `if (!gImageHash[url][type].hasOwnProperty(alt))` → `openCacheEntry()`
- 条件付き依存: `if (value != -1)` → `Number()`
- 条件付き依存: `if (value != -1)` → `Math.round()`
- 条件付き依存: `if (value != -1)` → `document.l10n .formatValue("media-file-size", { size: kbSize }) .then()`
- 条件付き依存: `if (value != -1)` → `document.l10n .formatValue()`
- 条件付き依存: `if (value != -1)` → `gImageView.tree.invalidateRow()`
- 条件付き依存: `if (value != -1)` → `gImageView.data.indexOf()`
- 条件付き依存: `if (gImageView.data.length == 1)` → `document.getElementById()`
- 参照: `cacheEntry.dataSize`, `document.getElementById("mediaTab").hidden`, `element.height`, `element.imageText`, `element.width`, `gImageElement.currentSrc`, `gImageElement.height`, `gImageElement.imageText`, `gImageElement.width`, `gImageView.data`, `gImageView.data.length`

## onBeginLinkDrag()
- 位置: L751-776
- 役割: 画像一覧の行をドラッグしたとき、URL と説明を dataTransfer の text/x-moz-url、text/url-list、text/plain に入れる。
- 触るとき: 画像をドラッグしたときに渡すデータの形式を変えるとき。
- 呼び出し先: `dt.setData()`, `tree.getRowAt()`, `tree.view.getCellText()`
- 参照: `event.clientX`, `event.clientY`, `event.dataTransfer`, `event.originalTarget.localName`, `event.target`, `tree.columns`, `tree.localName`, `tree.parentNode`

## getSelectedRows()
- 位置: L779-793
- 役割: tree の選択範囲をすべて回り、選択された行番号の配列を返す。
- 触るとき: 選択行を扱う処理(保存やプレビュー)の対象範囲を調べるとき。
- 呼び出し先: `rowArray.push()`, `tree.view.selection.getRangeAt()`, `tree.view.selection.getRangeCount()`
- 参照: `end.value`, `start.value`

## getSelectedRow()
- 位置: L795-798
- 役割: 選択行が1つだけならその行番号を返し、そうでなければ -1 を返す。
- 触るとき: 1行選択を前提にした処理の条件を変えるとき。
- 呼び出し先: `getSelectedRows()`
- 参照: `rows.length`

## selectSaveFolder()
- 位置: async L800-824
- 役割: フォルダー選択のファイルピッカーを開き、結果を aCallback に渡す。初期フォルダーは browser.download.dir を使う。
- 触るとき: 複数の画像を保存する先の選び方を変えるとき。
- 呼び出し先: `Cc["@mozilla.org/filepicker;1"].createInstance()`, `Services.prefs.getComplexValue()`, `document.l10n.formatValue()`, `fp.appendFilters()`, `fp.init()`, `fp.open()`
- 参照: `fp.displayDirectory`, `nsIFilePicker.filterAll`, `nsIFilePicker.modeGetFolder`, `window.browsingContext`
- XPCOM: `@mozilla.org/filepicker;1` / `Services.prefs`

## fpCallback_done()
- 位置: L804-810
- 役割: ファイルピッカーの結果が OK ならそのフォルダーを、キャンセルなら null を aCallback に渡す。
- 触るとき: フォルダー選択のキャンセル時の挙動を変えるとき。
- 条件付き依存: `if (aResult == nsIFilePicker.returnOK)` → `aCallback()`
- 条件付き依存: `if (aResult == nsIFilePicker.returnOK)` → `fp.file.QueryInterface()`
- 条件付き依存: `if (!(aResult == nsIFilePicker.returnOK))` → `aCallback()`
- 参照: `nsIFilePicker.returnOK`

## saveMedia()
- 位置: L826-949
- 役割: 選択が1件なら internalSave で1つの画像・動画・音声を保存する。複数件ならフォルダーを選んで各項目を saveAnImage で保存し、2件目以降は 200ms の遅延を入れる。
- 触るとき: 画像・メディアの保存先や保存時の種類、ダウンロード重複を防ぐ遅延を変えるとき。
- 呼び出し先: `Components.Constructor()`, `document.getElementById()`, `getSelectedRows()`
- 条件付き依存: `if (url)` → `HTMLVideoElement.isInstance()`
- 条件付き依存: `if (!(HTMLVideoElement.isInstance(item)))` → `HTMLAudioElement.isInstance()`
- 条件付き依存: `if (url)` → `Services.io.newURI()`
- 条件付き依存: `if (url)` → `E10SUtils.deserializeCookieJarSettings()`
- 条件付き依存: `if (url)` → `internalSave()`
- 条件付き依存: `if (!(rowArray.length == 1))` → `selectSaveFolder()`
- 条件付き依存: `if (aDirectory)` → `aDirectory.clone()`
- 条件付き依存: `if (aDirectory)` → `Services.io.newURI()`
- 条件付き依存: `if (aDirectory)` → `uri.QueryInterface()`
- 条件付き依存: `if (aDirectory)` → `dir.append()`
- 条件付き依存: `if (aDirectory)` → `decodeURIComponent()`
- 条件付き依存: `if (i == 0)` → `saveAnImage()`
- 条件付き依存: `if (i == 0)` → `Services.io.newURI()`
- 条件付き依存: `if (!(i == 0))` → `setTimeout()`
- 条件付き依存: `if (!(i == 0))` → `Services.io.newURI()`
- 参照: `Ci.nsIReferrerInfo.EMPTY`, `Ci.nsIURL`, `gDocInfo.cookieJarSettings`, `gDocInfo.isContentWindowPrivate`, `gDocInfo.principal`, `gImageView.data`, `item.baseURI`, `item.mimeType`, `rowArray.length`, `uri.fileName`
- XPCOM: [`nsIReferrerInfo`](../../../../docshell/shistory/nsISHEntry.idl.md) / [`nsIURL`](../../../../netwerk/base/nsIURL.idl.md) / `Services.io`

## saveAnImage()
- 位置: L880-909
- 役割: 1件の画像を選んだフォルダーに保存する。一意なファイルを作ってから、リファラーと Cookie 設定を付けて internalSave を呼ぶ。
- 触るとき: 複数保存時のファイル名や保存時のリファラーを変えるとき。
- 呼び出し先: `E10SUtils.deserializeCookieJarSettings()`, `internalSave()`, `uniqueFile()`
- 参照: `Ci.nsIReferrerInfo.EMPTY`, `aChosenData.file`, `gDocInfo.cookieJarSettings`, `gDocInfo.isContentWindowPrivate`, `gDocInfo.principal`
- XPCOM: [`nsIReferrerInfo`](../../../../docshell/shistory/nsISHEntry.idl.md)

## onImageSelect()
- 位置: L951-974
- 役割: 画像一覧の選択数に応じて、プレビューと保存欄の表示を切り替える。1件選んだときは makePreview を呼ぶ。
- 触るとき: 選択数ごとの表示の出し分けを変えるとき。
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (count == 0)` → `tree.setAttribute()`
- 条件付き依存: `if (count > 1)` → `tree.setAttribute()`
- 条件付き依存: `if (!(count > 1))` → `tree.setAttribute()`
- 条件付き依存: `if (!(count > 1))` → `makePreview()`
- 条件付き依存: `if (!(count > 1))` → `getSelectedRows()`
- 参照: `mediaSaveBox.collapsed`, `previewBox.collapsed`, `splitter.collapsed`, `tree.view.selection.count`

## makePreview()
- 位置: L977-1189
- 役割: 選んだ画像のプレビューを作る。サイズと種類を表示し、プロトコルと権限が許せば mediaBrowser に読み込んで読み込み完了を待ち、PageInfoPreview から寸法を受けて表示する。許されない場合は壊れた画像の欄を出す。
- 触るとき: プレビューの対象範囲、寸法の表示、読み込みを許可する条件のどれかを変えるとき。
- 呼び出し先: `ChromeUtils.generateQI()`, `Services.io.newURI()`, `actor.sendQuery()`, `checkProtocol()`, `console.error()`, `document.getElementById()`, `getSelectedRows()`, `mediaBrowser.addProgressListener()`, `mediaBrowser.browsingContext.currentWindowGlobal.getActor()`, `mediaBrowser.loadURI()`, `mimeType.startsWith()`, `openCacheEntry()`, `setItemValue()`, `this.getContentTypeFromHeaders()`, `url.replace()`, `window.dispatchEvent()`
- 条件付き依存: `if (cacheEntry)` → `Math.round()`
- 条件付き依存: `if (cacheEntry)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (cacheEntry)` → `document.getElementById()`
- 条件付き依存: `if (cacheEntry)` → `formatNumber()`
- 条件付き依存: `if (!(cacheEntry))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(cacheEntry))` → `document.getElementById()`
- 条件付き依存: `if (mimeType)` → `/^image\/(.*)/i.exec()`
- 条件付き依存: `if (imageMimeType)` → `imageMimeType[1].toUpperCase()`
- 条件付き依存: `if (numFrames > 1)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(numFrames > 1))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!(imageMimeType))` → `element.setAttribute()`
- 条件付き依存: `if (!(imageMimeType))` → `element.removeAttribute()`
- 条件付き依存: `if (!(mimeType))` → `element.setAttribute()`
- 条件付き依存: `if (!(mimeType))` → `element.removeAttribute()`
- 条件付き依存: `if (isAllowed)` → `Services.scriptSecurityManager.checkLoadURIWithPrincipal()`
- 条件付き依存: `if (isAllowed)` → `Services.io.newURI()`
- 条件付き依存: `if ( (item.HTMLLinkElement || item.HTMLInputElement || item.HTMLImageElement || item.SVGImageElement || (item.HTMLObjectElement && mimeType && mimeType.startsWit...)` → `document.getElementById()`
- 条件付き依存: `if (item.HTMLVideoElement && isAllowed)` → `document.getElementById()`
- 条件付き依存: `if (item.HTMLVideoElement && isAllowed)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (item.HTMLVideoElement && isAllowed)` → `formatNumber()`
- 条件付き依存: `if (item.HTMLAudioElement && isAllowed)` → `document.getElementById()`
- 条件付き依存: `if (!(item.HTMLAudioElement && isAllowed))` → `document.getElementById()`
- 条件付き依存: `if ( data.width != data.naturalWidth || data.height != data.naturalHeight )` → `document.l10n.setAttributes()`
- 条件付き依存: `if ( data.width != data.naturalWidth || data.height != data.naturalHeight )` → `document.getElementById()`
- 条件付き依存: `if ( data.width != data.naturalWidth || data.height != data.naturalHeight )` → `formatNumber()`
- 条件付き依存: `if (!( data.width != data.naturalWidth || data.height != data.naturalHeight ))` → `document.l10n.setAttributes()`
- 条件付き依存: `if (!( data.width != data.naturalWidth || data.height != data.naturalHeight ))` → `document.getElementById()`
- 条件付き依存: `if (!( data.width != data.naturalWidth || data.height != data.naturalHeight ))` → `formatNumber()`
- 参照: `Ci.nsIWebProgress.NOTIFY_STATE_WINDOW`, `cacheEntry.dataSize`, `data.height`, `data.naturalHeight`, `data.naturalWidth`, `data.width`, `document.getElementById("brokenimagecontainer").collapsed`, `document.getElementById("theimagecontainer").collapsed`, `gDocInfo.principal`, `gImageView.data`, `item.HTMLAudioElement`, `item.HTMLImageElement`, `item.HTMLInputElement`, `item.HTMLLinkElement`, `item.HTMLObjectElement`, `item.HTMLVideoElement`, `item.SVGImageElement`, `item.SVGImageElementHeight`, `item.SVGImageElementWidth`, `item.height`, `item.imageText`, `item.longDesc`, `item.mimeType`, `item.numFrames`, `item.videoHeight`, `item.videoWidth`, `item.width`, `message.height`, `message.width`
- XPCOM: [`nsIWebProgress`](../../../../dom/interfaces/base/nsIBrowser.idl.md) / `Services.io` / `Services.scriptSecurityManager`

## onStateChange()
- 位置: L1117-1124
- 役割: 読み込みの状態変化を受け、STATE_STOP になったらリスナーを外して Promise を解決する。
- 触るとき: プレビューの読み込み完了の判定を変えるとき。
- 条件付き依存: `if (aStateFlags & Ci.nsIWebProgressListener.STATE_STOP)` → `mediaBrowser.webProgress?.removeProgressListener()`
- 条件付き依存: `if (aStateFlags & Ci.nsIWebProgressListener.STATE_STOP)` → `resolve()`
- 参照: `Ci.nsIWebProgressListener.STATE_STOP`
- XPCOM: [`nsIWebProgressListener`](../../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## getContentTypeFromHeaders()
- 位置: L1191-1199
- 役割: キャッシュの response-head から Content-Type の値を取り出す。エントリが無ければ null を返す。
- 触るとき: キャッシュから MIME 種別を取り出す方法を変えるとき。
- 呼び出し先: `/^Content-Type:\s*(.*?)\s*(?:\;|$)/im.exec()`, `cacheEntryDescriptor.getMetaDataElement()`

## setItemValue()
- 位置: L1201-1207
- 役割: 値が空なら行ごと隠し、値があれば要素に値を入れる。
- 触るとき: 一般タブやメディアタブの欄の空表示の挙動を変えるとき。
- 呼び出し先: `document.getElementById()`, `item.closest()`
- 参照: `item.closest("tr").hidden`, `item.value`

## formatNumber()
- 位置: L1209-1211
- 役割: 数値を実行環境のロケールで文字列にする。
- 触るとき: 数値の表示形式を変えるとき。
- 呼び出し先: `(+number).toLocaleString()`

## formatDate()
- 位置: L1213-1224
- 役割: 日付文字列を長い形式の日付と時刻に整形する。解釈できなければ unknown をそのまま返す。
- 触るとき: 更新日時の表示形式を変えるとき。
- 呼び出し先: `date.valueOf()`, `dateTimeFormatter.format()`
- 参照: `Services.intl.DateTimeFormat`
- XPCOM: `Services.intl`

## supportsCommand()
- 位置: L1227-1229
- 役割: cmd_copy と cmd_selectAll だけを扱うと返す。
- 触るとき: ツリーで扱うコマンドを増やすとき。

## isCommandEnabled()
- 位置: L1231-1233
- 役割: 常に true を返す。
- 触るとき: コマンドを無効にする条件を入れるとき。

## doCommand()
- 位置: L1235-1244
- 役割: cmd_copy なら doCopy を呼び、cmd_selectAll ならフォーカス中のツリーの全行を選択する。
- 触るとき: ツリーのコピーや全選択の挙動を変えるとき。
- 呼び出し先: `doCopy()`, `document.activeElement.view.selection.selectAll()`

## doCopy()
- 位置: L1247-1276
- 役割: フォーカス中のツリーで選択された行のセル値を集め、改行で連結してクリップボードに入れる。
- 触るとき: コピーされるテキストの形式を変えるとき。
- 条件付き依存: `if (elem && elem.localName == "tree")` → `selection.getRangeCount()`
- 条件付き依存: `if (elem && elem.localName == "tree")` → `selection.getRangeAt()`
- 条件付き依存: `if (elem && elem.localName == "tree")` → `view.getCellValue()`
- 条件付き依存: `if (tmp)` → `text.push()`
- 条件付き依存: `if (elem && elem.localName == "tree")` → `gClipboardHelper.copyString()`
- 条件付き依存: `if (elem && elem.localName == "tree")` → `text.join()`
- 参照: `document.commandDispatcher.focusedElement`, `elem.localName`, `elem.view`, `max.value`, `min.value`, `view.selection`

## doSelectAllMedia()
- 位置: L1278-1284
- 役割: 画像一覧の全行を選択する。
- 触るとき: 全選択ボタンの動作を変えるとき。
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (tree)` → `tree.view.selection.selectAll()`

## selectImage()
- 位置: L1286-1308
- 役割: 右クリックの「画像情報を表示」で渡された画像要素に対応する行を探して選択し、表示範囲に入れてフォーカスする。
- 触るとき: 画像情報の表示で選ばれる行の一致条件を変えるとき。
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if ( !gImageView.data[i][COL_IMAGE_BG] && gImageElement.currentSrc == gImageView.data[i][COL_IMAGE_ADDRESS] && gImageElement.width == image.width && gImageElemen...)` → `tree.view.selection.select()`
- 条件付き依存: `if ( !gImageView.data[i][COL_IMAGE_BG] && gImageElement.currentSrc == gImageView.data[i][COL_IMAGE_ADDRESS] && gImageElement.width == image.width && gImageElemen...)` → `tree.ensureRowIsVisible()`
- 条件付き依存: `if ( !gImageView.data[i][COL_IMAGE_BG] && gImageElement.currentSrc == gImageView.data[i][COL_IMAGE_ADDRESS] && gImageElement.width == image.width && gImageElemen...)` → `tree.focus()`
- 参照: `gImageElement.currentSrc`, `gImageElement.height`, `gImageElement.imageText`, `gImageElement.width`, `gImageView.data`, `image.height`, `image.imageText`, `image.width`, `tree.view.rowCount`

## checkProtocol()
- 位置: L1310-1316
- 役割: data:image、http(s)、file、about、chrome、resource の URL なら true を返す。
- 触るとき: プレビューや画像表示を許すスキームを変えるとき。
- 呼び出し先: `/^(https?|file|about|chrome|resource):/.test()`, `/^data:image\//i.test()`

## getOaWithPartitionKey()
- 位置: async L1318-1329
- 役割: コンテンツプロセスから partitionKey を取得し、ブラウザの principal の originAttributes にその値を入れて返す。
- 触るとき: キャッシュの分離キーの決め方を変えるとき。
- 呼び出し先: `actor.sendQuery()`, `browsingContext.currentWindowGlobal.getActor()`
- 参照: `browser.browsingContext`, `browser.contentPrincipal.originAttributes`, `oa.partitionKey`, `partitionKeyFromChild.partitionKey`, `window.opener.gBrowser.selectedBrowser`
