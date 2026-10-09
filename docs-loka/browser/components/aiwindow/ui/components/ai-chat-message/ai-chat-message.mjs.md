# browser/components/aiwindow/ui/components/ai-chat-message/ai-chat-message.mjs

source: browser/components/aiwindow/ui/components/ai-chat-message/ai-chat-message.mjs
source-hash: 74c13e6e882e5c1c34fd069647065f77e3024c95
lines: 848

## <module>
- 役割: ユーザーとアシスタントの 1 メッセージを描画する ai-chat-message 要素を定義する。Markdown、履歴グリッド、リンクの扱いを担う。
- 呼び出し先: `Object.values()`, `customElements.define()`, `this.#chatMessageSanitizer.allowAttribute()`, `this.#chatMessageSanitizer.allowElement()`

## AIChatMessage.constructor()
- 位置: L100-126
- 役割: seenUrls と historyResults を空の Set・Map、conversationId を空文字で初期化する。
- 触るとき: 履歴結果や既出 URL の初期状態を変えるとき、または既定値のまま描画が崩れるときに見る。
- 呼び出し先: `super()`
- 参照: `this.conversationId`, `this.historyResults`, `this.seenUrls`

## AIChatMessage.connectedCallback()
- 位置: L128-131
- 役割: 親の connectedCallback の後、リンクのクリック監視を設定する。
- 触るとき: リンククリックが開けない、または二重に開く不具合を調べるときに見る。
- 呼び出し先: `super.connectedCallback()`, `this.#initLinkNavigationListener()`

## AIChatMessage.#initLinkNavigationListener()
- 位置: L133-158
- 役割: シャドウルート内の a をクリックされたら既定動作を止め、AIChatContent:OpenLink を修飾キー付きで発火する。
- 触るとき: リンクを新しいタブで開く条件や、クリックの detail を変えるときに見る。
- 呼び出し先: `this.shadowRoot.addEventListener()`
- 条件付き依存: `if (target.tagName === "A" && target.href)` → `event.preventDefault()`
- 条件付き依存: `if (target.tagName === "A" && target.href)` → `this.dispatchEvent()`
- 参照: `event.altKey`, `event.button`, `event.ctrlKey`, `event.metaKey`, `event.shiftKey`, `event.target`, `target.href`, `target.parentElement`, `target.tagName`, `this.shadowRoot`

## AIChatMessage.willUpdate()
- 位置: L165-184
- 役割: 既出 URL、会話 ID、完了状態、履歴結果が変わったら、リンクの展開をやり直す必要があると記録する。
- 触るとき: 既出 URL が変わってもリンクの表示が古いままのときに、この再計算条件を確認する。
- 呼び出し先: `changed.has()`, `this.#urlsUnfurledInMessage.intersection()`
- 参照: `this.#unfurledUrlsNeedUpdating`, `this.#urlsUnfurledInMessage.intersection(this.seenUrls).size`, `this.seenUrls`

## AIChatMessage.updated()
- 位置: L186-202
- 役割: アシスタントの完了時に本文のテキストを集め、ai-chat-message:complete を発火する。
- 触るとき: 完了通知の本文の取り方を変えるとき、または完了通知が届かないときに見る。
- 呼び出し先: `changed.has()`
- 条件付き依存: `if (changed.has("complete") && this.complete && this.role === "assistant")` → `this.shadowRoot?.querySelector()`
- 条件付き依存: `if (changed.has("complete") && this.complete && this.role === "assistant")` → `(messageEl.innerText || messageEl.textContent || "") .replace(/\s+/g, " ") .trim()`
- 条件付き依存: `if (changed.has("complete") && this.complete && this.role === "assistant")` → `(messageEl.innerText || messageEl.textContent || "") .replace()`
- 条件付き依存: `if (changed.has("complete") && this.complete && this.role === "assistant")` → `this.dispatchEvent()`
- 参照: `messageEl.innerText`, `messageEl.textContent`, `this.complete`, `this.messageId`, `this.role`

## AIChatMessage.#getIconSrc()
- 位置: L204-210
- 役割: リンク先があれば page-icon: 形式の URL、無ければ既定のファビコンを返す。
- 触るとき: メンション chip のアイコン取得元を変えるとき、または CSP の page-icon ルールに影響するとき見る。

## AIChatMessage.#replaceWebsiteMentions()
- 位置: L239-283
- 役割: mention:? 形式の a 要素を ai-website-chip に差し替える。タブグループかサイトかを判定する。
- 触るとき: メンションの書式や chip の属性を変えるとき、または @ メンションが普通のリンクのまま残るときに見る。
- 呼び出し先: `a.replaceWith()`, `href.startsWith()`, `href.substring()`, `params.get()`, `root.ownerDocument.createElement()`, `root.querySelectorAll()`
- 条件付き依存: `if (!(isTabGroup))` → `this.#getIconSrc()`
- 参照: `MENTION_PREFIX.length`, `a.textContent`, `chip.href`, `chip.iconSrc`, `chip.isTabGroup`, `chip.label`, `chip.tabGroupColor`, `chip.type`, `linkHref.length`

## AIChatMessage.#unfurlUnseenLinks()
- 位置: L296-351
- 役割: 既出でない http/https リンクは本文を注釈付きで出し、許可されない scheme の href は削除する。
- 触るとき: 未確認 URL の表示（注釈やリンクの扱い）を変えるとき、またはリンクが勝手に開く問題を調べるときに見る。
- 呼び出し先: `URL.parse()`, `isSettingsURL()`, `isSmartPageURL()`, `root.querySelectorAll()`, `this.seenUrls.has()`
- 条件付き依存: `if ( !parsed || (parsed.protocol !== "http:" && parsed.protocol !== "https:") )` → `anchor.removeAttribute()`
- 条件付き依存: `if (!this.seenUrls.has(anchor.href))` → `this.#urlsUnfurledInMessage.add()`
- 条件付き依存: `if (!this.seenUrls.has(anchor.href))` → `URL.parse()`
- 条件付き依存: `if (!this.seenUrls.has(anchor.href))` → `textContent.trim()`
- 条件付き依存: `if (!this.seenUrls.has(anchor.href))` → `doc.createElement()`
- 条件付き依存: `if (!this.seenUrls.has(anchor.href))` → `disclosure.append()`
- 条件付き依存: `if (!this.seenUrls.has(anchor.href))` → `anchor.replaceWith()`
- 参照: `anchor.href`, `anchor.ownerDocument`, `label.className`, `label.textContent`, `link.href`, `link.textContent`, `parsed.protocol`, `this.#urlsUnfurledInMessage`

## AIChatMessage.#isHistoryItem()
- 位置: L353-356
- 役割: リスト項目の最初のリンクが historyResults に含まれるかを判定する。
- 触るとき: 履歴結果の判定条件を変えるとき、または履歴リストがグリッドにならないときに見る。
- 呼び出し先: `li.querySelector()`, `this.historyResults.has()`
- 参照: `link.href`

## AIChatMessage.#replaceHistoryResults()
- 位置: L370-413
- 役割: 全項目が履歴 URL の一覧はグリッドに置き換え、それ以外は隠さず表示する。ストリーミング中は途中の項目を判定しない。
- 触るとき: 履歴一覧の表示切り替えのタイミングを変えるとき、またはリストが生の箇条書きで一瞬見えるときに見る。
- 呼び出し先: `Array.from()`, `items.some()`, `list.querySelectorAll()`, `lists.forEach()`, `root.querySelectorAll()`, `this.#isHistoryItem()`
- 条件付き依存: `if (this.complete)` → `items.every()`
- 条件付き依存: `if (this.complete)` → `this.#isHistoryItem()`
- 条件付き依存: `if (items.every(item => this.#isHistoryItem(item)))` → `items.map()`
- 条件付き依存: `if (items.every(item => this.#isHistoryItem(item)))` → `this.historyResults.get()`
- 条件付き依存: `if (items.every(item => this.#isHistoryItem(item)))` → `li.querySelector()`
- 条件付き依存: `if (items.every(item => this.#isHistoryItem(item)))` → `list.replaceWith()`
- 条件付き依存: `if (items.every(item => this.#isHistoryItem(item)))` → `this.#getHistoryListGrid()`
- 参照: `allListItems.length`, `items.length`, `li.querySelector("a[href]").href`, `list.style.display`, `this.complete`, `this.historyResults?.size`

## AIChatMessage.#getHistoryListGrid()
- 位置: L423-469
- 役割: 同じ index のグリッドを再利用し、無ければ ai-chat-grid を作って資産の取得を依頼する。
- 触るとき: 履歴グリッドの作り直しや再利用の条件を変えるとき、またはグリッドが更新されないときに見る。
- 呼び出し先: `Array.from()`, `Array.from(gridItems || []).slice()`, `items.forEach()`, `items.some()`, `this.#calculateHistoryGridView()`, `this.#historyGrids.has()`, `this.#historyGrids.set()`, `this.#renderHistoryGridRow.bind()`, `this.#renderHistoryGridTile.bind()`, `this.#requestHistoryAssets()`, `this.dispatchEvent()`, `this.ownerDocument.createElement()`
- 条件付き依存: `if (this.#historyGrids.has(index))` → `this.#historyGrids.get()`
- 参照: `grid.gridItem`, `grid.items`, `grid.loading`, `grid.rowItem`, `grid.showSwitch`, `grid.view`, `historyGrid.items`, `historyGrid.loading`, `historyGrid.view`, `item.image`, `item.resultCount`, `item.resultIndex`, `item.thumbnail`, `items.length`

## AIChatMessage.#requestHistoryAssets()
- 位置: L479-501
- 役割: 新規グリッドごとに URL とサムネイルを親へ送り、サムネイルとファビコン状態の解決を依頼する。
- 触るとき: サムネイル取得の依頼内容を変えるとき、または画像が出ないときに見る。
- 呼び出し先: `items .filter()`, `items .filter(item => item?.url) .map()`, `this.dispatchEvent()`
- 参照: `item?.url`, `requestItems.length`, `this.conversationId`, `this.messageId`

## AIChatMessage.#calculateHistoryGridView()
- 位置: L512-529
- 役割: og:image が無い項目が 40%を超えると list、それ以外は grid を選び、各項目に faviconUrl を付ける。
- 触るとき: グリッドと一覧の切り替え基準を変えるとき、またはファビコンの URL を確かめるときに見る。
- 呼び出し先: `items.forEach()`, `this.#getFaviconUri()`
- 参照: `item.faviconUrl`, `item.image`, `item.url`, `items.length`

## AIChatMessage.#renderHistoryGridTile()
- 位置: L537-553
- 役割: 履歴 1 件をグリッド用の ai-chat-card で描き、クリックで itemClick を呼ぶ。
- 触るとき: グリッドのカードに出す属性を変えるとき、またはカードのクリックが記録されないときに見る。
- 呼び出し先: `html()`, `this.itemClick.bind()`
- 参照: `item.faviconUrl`, `item.hasFavicon`, `item.image`, `item.timestamp`, `item.title`, `item.url`

## AIChatMessage.#renderHistoryGridRow()
- 位置: L561-580
- 役割: 履歴 1 件を favicon、タイトル、日時の一行リンクで描き、クリックで itemClick を呼ぶ。
- 触るとき: 一覧表示の行の見た目や属性を変えるときに見る。
- 呼び出し先: `html()`, `this.#getFaviconUri()`, `this.itemClick.bind()`
- 参照: `item.timestamp`, `item.title`, `item.url`

## AIChatMessage.itemClick()
- 位置: L588-598
- 役割: AIChatContent:HistoryGridItemClick を項目付きで発火し、テレメトリに渡せるようにする。
- 触るとき: 履歴のクリック計測の内容を変えるとき、またはクリックが記録されないときに見る。
- 呼び出し先: `this.dispatchEvent()`

## AIChatMessage.#getFaviconUri()
- 位置: L608-610
- 役割: ページ URL から page-icon: 形式のファビコン URL を作る。
- 触るとき: ファビコンの URL 形式（page-icon スキーム）を変えるときに見る。

## AIChatMessage.#parseMarkdown()
- 位置: L639-648
- 役割: Markdown を HTML に変換し、チャット用の Sanitizer で安全に挿入する。失敗時は telemetry を送って再送出する。
- 触るとき: 許可するタグや属性を変えるとき、または Markdown の描画が失敗するときに見る。
- 呼び出し先: `dispatchClientError()`, `element.setHTML()`, `parseMarkdown()`
- 参照: `AIChatMessage.#chatMessageSanitizer`

## AIChatMessage.parseUserMarkdown()
- 位置: L656-659
- 役割: ユーザー発言を Markdown として描画し、その後にメンションを chip に変換する。
- 触るとき: ユーザー発言でメンションが効かない、または描画順を変えるときに見る。
- 呼び出し先: `this.#parseMarkdown()`, `this.#replaceWebsiteMentions()`

## AIChatMessage.#renderBlockElement()
- 位置: L668-679
- 役割: ブロック 1 つの HTML を一時 div で安全に描き、最初の要素を返す。
- 触るとき: ブロック単位の描画結果や例外の扱いを変えるとき、またはブロックが空で返るときに見る。
- 呼び出し先: `dispatchClientError()`, `scratch.setHTML()`, `this.ownerDocument.createElement()`
- 参照: `AIChatMessage.#chatMessageSanitizer`, `scratch.firstElementChild`

## AIChatMessage.#reconcileBlocks()
- 位置: L691-714
- 役割: ブロック HTML が変わったものだけ作り直し、末尾の余分な要素を削除する。作り直した数を返す。
- 触るとき: ストリーミング中に既存のブロック（表など）が作り直されて途切れるときに見る。
- 呼び出し先: `container.lastElementChild.remove()`, `this.#renderBlockElement()`
- 条件付き依存: `if (container.children[i])` → `container.replaceChild()`
- 条件付き依存: `if (!(container.children[i]))` → `container.append()`
- 参照: `container.children`, `container.children.length`, `newHtml.length`, `this.#blockHtml`

## AIChatMessage.getAssistantMessage()
- 位置: L724-788
- 役割: 翻訳 ID があれば Fluent で描き、無ければ Markdown をブロックごとに描いて履歴とリンクを処理する。同じ内容なら再計算しない。
- 触るとき: アシスタント回答の描画順やストリーミング時の更新を変えるとき、または表示が古いままのときに見る。
- 呼び出し先: `parseMarkdownBlocks()`, `parseMarkdownBlocks(this.message).map()`, `performance.measure()`, `performance.now()`, `this.#reconcileBlocks()`, `this.#replaceHistoryResults()`, `this.#unfurlUnseenLinks()`
- 条件付き依存: `if (this.messageL10n?.id)` → `this.#renderL10nMessage()`
- 条件付き依存: `if (!this.#lastMessageElement)` → `this.ownerDocument.createElement()`
- 条件付き依存: `if (!this.message)` → `messageElement.replaceChildren()`
- 条件付き依存: `if (!this.message)` → `messageElement.classList.remove()`
- 条件付き依存: `if (this.historyResults?.size)` → `messageElement.classList.add()`
- 条件付き依存: `if (!(this.historyResults?.size))` → `messageElement.classList.remove()`
- 参照: `block.html`, `blockHtml.length`, `this.#blockHtml`, `this.#lastMessage`, `this.#lastMessageElement`, `this.#lastMessageElement.className`, `this.#unfurledUrlsNeedUpdating`, `this.historyResults?.size`, `this.message`, `this.messageL10n?.id`, `this.role`

## AIChatMessage.getUserMessage()
- 位置: L797-808
- 役割: ユーザー発言を新しい div に Markdown として描画する。空なら空の div を返す。
- 触るとき: ユーザー発言の見た目や Markdown の扱いを変えるときに見る。
- 呼び出し先: `this.ownerDocument.createElement()`, `this.parseUserMarkdown()`
- 参照: `messageElement.className`, `this.message`, `this.role`

## AIChatMessage.#renderL10nMessage()
- 位置: L817-829
- 役割: 翻訳 ID と args を使い、任意のリンク付きでアシスタント文言を描画する。
- 触るとき: 翻訳で出すエラーや案内文の描画方法を変えるとき、またはリンクの href が反映されないときに見る。
- 呼び出し先: `JSON.stringify()`, `html()`
- 参照: `link.href`, `link.l10nName`, `this.messageL10n`

## AIChatMessage.render()
- 位置: L831-844
- 役割: CSS を読み込み、ユーザーかアシスタントかに応じた本文を article に入れて描画する。
- 触るとき: メッセージ全体の外側構造を変えるとき、またはユーザーとアシスタントの分岐を変えるときに見る。
- 呼び出し先: `html()`, `this.getAssistantMessage()`, `this.getUserMessage()`
- 参照: `this.role`
