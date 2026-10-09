# browser/components/aiwindow/models/aitab/AITab.sys.mjs

source: browser/components/aiwindow/models/aitab/AITab.sys.mjs
source-hash: a2698912c7966ac6d1bd9744dd7234aeb8cd3114
lines: 1624

## <module>
- 役割: AIタブ(A2UI形式のページ)を生成する静的なサービス。参照ページの読み込み、モデル呼び出し、カタログに対する検証、URLトークンの展開と復元、既存ページの修正を担う。描画はabout:smartpageが行う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `JSON.parse()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`, `prefValue.trim()`

## AITab.loadAssets()
- 位置: async L341-345
- 役割: prefに設定があればそのカタログを、無ければパック済みのカタログを読み、検証用の環境(部品ごとの検証器)を作って返す。
- 触るとき: カタログを差し替えても反映されないとき、開発用のprefの扱いを確かめるとき。
- 呼び出し先: `AITab.#loadPackagedCatalog()`, `AITab.#makeEnv()`
- 参照: `lazy.overrideCatalog`

## AITab.buildSurface()
- 位置: L359-454
- 役割: サーフェスを検証する。IDの重複、ルートが1つのPageであること、各部品がカタログのスキーマに合うこと、ID参照が存在すること、絶対パスのバインドが解決することを確かめ、エラーを全部集める。
- 触るとき: 生成されたページが形式違反で落ちた理由を調べるとき、検証の項目を増減させるとき。
- 呼び出し先: `AITab.#checkBindings()`, `AITab.#checkBoundArrays()`, `AITab.#checkRefs()`, `AITab.#propsOf()`, `Array.isArray()`, `components.filter()`, `components.map()`, `validator.validate()`
- 条件付き依存: `if (typeof id != "string" || !id)` → `errors.push()`
- 条件付き依存: `if (!(typeof id != "string" || !id))` → `idSet.has()`
- 条件付き依存: `if (idSet.has(id))` → `errors.push()`
- 条件付き依存: `if (!(idSet.has(id)))` → `idSet.add()`
- 条件付き依存: `if (roots.length !== 1)` → `errors.push()`
- 条件付き依存: `if (roots[0].component !== ROOT_COMPONENT)` → `errors.push()`
- 条件付き依存: `if (!validator)` → `errors.push()`
- 条件付き依存: `if (!valid)` → `errors.push()`
- 参照: `c?.id`, `comp.component`, `comp.id`, `comp?.children`, `comp?.component`, `comp?.header`, `comp?.id`, `env.catalog`, `env.catalog.components`, `env.validators`, `errors.length`, `roots.length`, `roots[0].component`, `surface.dataModel`, `surface?.components`

## AITab.#loadPackagedCatalog()
- 位置: L461-471
- 役割: chrome://のカタログJSONを取得し、そのPromiseをキャッシュする。失敗したらキャッシュを消して例外を投げ直す。
- 触るとき: カタログの読み込みに失敗して生成が始まらないとき。
- 条件付き依存: `if (!AITab.#packagedCatalogPromise)` → `fetch(COMPONENT_SCHEMA_URL) .then(r => r.json()) .catch()`
- 条件付き依存: `if (!AITab.#packagedCatalogPromise)` → `fetch(COMPONENT_SCHEMA_URL) .then()`
- 条件付き依存: `if (!AITab.#packagedCatalogPromise)` → `fetch()`
- 条件付き依存: `if (!AITab.#packagedCatalogPromise)` → `r.json()`
- 参照: `AITab.#packagedCatalogPromise`

## AITab.#makeEnv()
- 位置: L482-503
- 役割: カタログの部品ごとに、共有のdefsを埋め込んだJSON Schemaの検証器を作り、部品名の一覧と一緒に返す。componentsが無ければ例外を投げる。
- 触るとき: カタログの形式を変えるとき、検証器が作れない原因を調べるとき。
- 呼び出し先: `Object.keys()`
- 参照: `catalog.$defs`, `catalog.components`, `lazy.JsonSchema.Validator`

## AITab.#checkRefs()
- 位置: L515-537
- 役割: header、childrenの参照(単独のID、ID配列、テンプレート)が、存在するIDを指しているか確かめ、無い参照をエラーとして積む。
- 触るとき: ID参照の欠落エラーの原因を追うとき、参照の形を増やすとき。
- 条件付き依存: `if (typeof value == "string")` → `idSet.has()`
- 条件付き依存: `if (!idSet.has(value))` → `errors.push()`
- 条件付き依存: `if (!(typeof value == "string"))` → `Array.isArray()`
- 条件付き依存: `if (Array.isArray(value))` → `AITab.#checkRefs()`
- 条件付き依存: `if ( typeof value == "object" && typeof value.componentId == "string" )` → `idSet.has()`
- 条件付き依存: `if (!idSet.has(value.componentId))` → `errors.push()`
- 参照: `value.componentId`

## AITab.#checkBindings()
- 位置: L550-575
- 役割: プロパティを再帰的に歩き、/で始まる{path}の値がデータモデルで解決しなければエラーにする。相対パスはテンプレート内の値なので検査しない。
- 触るとき: データバインドが見つからないというエラーの原因を調べるとき。
- 呼び出し先: `AITab.#checkBindings()`, `Array.isArray()`, `Object.keys()`, `Object.values()`
- 条件付き依存: `if (Array.isArray(value))` → `AITab.#checkBindings()`
- 条件付き依存: `if (keys.length === 1 && typeof value.path == "string")` → `value.path.startsWith()`
- 条件付き依存: `if (keys.length === 1 && typeof value.path == "string")` → `AITab.#resolvePath()`
- 条件付き依存: `if ( value.path.startsWith("/") && AITab.#resolvePath(dataModel, value.path) === undefined )` → `errors.push()`
- 参照: `keys.length`, `value.path`

## AITab.#propsOf()
- 位置: L584-589
- 役割: 部品からidとcomponentを除いたプロパティだけを複製して返す。
- 触るとき: 部品のプロパティを検証器に渡す形を変えるとき。
- 参照: `props.component`, `props.id`

## AITab.#resolvePath()
- 位置: L600-610
- 役割: /で始まるJSONポインタを先頭から順にたどり、途中で値が無ければundefinedを返す。~1と~0の展開も行う。
- 触るとき: データモデルのパスが解決しない、または逆に解決しすぎるとき。
- 呼び出し先: `pointer.slice()`, `pointer.slice(1).split()`, `seg.replace()`, `seg.replace(/~1/g, "/").replace()`

## AITab.#isBinding()
- 位置: L619-627
- 役割: 値が、文字列のpathだけを持つオブジェクト(データバインディング)かを判定する。
- 触るとき: バインディングの形の判定基準を変えるとき。
- 呼び出し先: `Array.isArray()`, `Object.keys()`
- 参照: `Object.keys(v).length`, `v.path`

## AITab.#resolveDef()
- 位置: L636-642
- 役割: { $ref: '#/$defs/X' }なら共有defsのXを返す。それ以外はそのまま返す。並んでいる他のキーは捨てる。
- 触るとき: カタログの$refが解決しないとき、参照の書き方を変えるとき。
- 条件付き依存: `if (schema && typeof schema.$ref == "string")` → `schema.$ref.replace()`
- 参照: `catalog.$defs`, `schema.$ref`

## AITab.#itemValidator()
- 位置: L652-665
- 役割: 配列の要素のスキーマから検証器を作る。同じスキーマの検証器は、同じ検証の中でキャッシュから再利用する。
- 触るとき: 配列要素の検証が遅い、または要素のエラーが出ないとき。
- 呼び出し先: `JSON.stringify()`, `cache.getOrInsertComputed()`
- 参照: `catalog.$defs`, `lazy.JsonSchema.Validator`

## AITab.#checkBoundArrays()
- 位置: L683-742
- 役割: スキーマが配列、またはバインディングとの選択肢を持つとき、データモデル上の配列を解決し、各要素を要素のスキーマで検証する。プロパティの中も再帰的に調べる。
- 触るとき: データモデルの配列の要素が検証で落ちる、または見逃されるとき。
- 呼び出し先: `AITab.#resolveDef()`, `Array.isArray()`
- 条件付き依存: `if (Array.isArray(schema.oneOf))` → `schema.oneOf.find()`
- 条件付き依存: `if (Array.isArray(schema.oneOf))` → `AITab.#isBinding()`
- 条件付き依存: `if (arrayBranch && AITab.#isBinding(value))` → `value.path.startsWith()`
- 条件付き依存: `if (arrayBranch && AITab.#isBinding(value))` → `AITab.#resolvePath()`
- 条件付き依存: `if (arrayBranch && AITab.#isBinding(value))` → `Array.isArray()`
- 条件付き依存: `if (!Array.isArray(arr))` → `errors.push()`
- 条件付き依存: `if (arrayBranch && AITab.#isBinding(value))` → `AITab.#itemValidator()`
- 条件付き依存: `if (arrayBranch && AITab.#isBinding(value))` → `arr.forEach()`
- 条件付き依存: `if (arrayBranch && AITab.#isBinding(value))` → `iv.validate()`
- 条件付き依存: `if (!valid)` → `errors.push()`
- 条件付き依存: `if (props && typeof value == "object" && !Array.isArray(value))` → `Object.entries()`
- 条件付き依存: `if (k in value)` → `AITab.#checkBoundArrays()`
- 参照: `arrayBranch.items`, `s.items`, `s.type`, `schema.oneOf`, `schema.properties`, `value.path`

## AITab.buildViewerURL()
- 位置: L752-754
- 役割: スラッグからabout:smartpage?page=スラッグのURLを作る。ページの中身はURLに含めない。
- 触るとき: AIタブを開くURLの形式を変えるとき。Toolsのcreate系の処理から使われる。

## AITab.generateAITab()
- 位置: async L788-933
- 役割: URL、直接渡された内容、修正対象の既存ページのいずれかから材料を集め、モデルで構造化されたサーフェスを作って検証する。ツール会話を保存し、ファビコンを埋め、タイトルとメタデータを決めて返す。失敗や中断は文字列のerrorで返す。
- 触るとき: AIタブの生成がどこで止まるかを追うとき、ページのIDやタイトル、出典の決まり方を変えるとき。Toolsのcreateの処理から呼ばれる。
- 呼び出し先: `AITab.#capped()`, `AITab.#collectSources()`, `AITab.#generateStructuredSurface()`, `AITab.#hydrateFavicons()`, `AITab.#mergeSources()`, `AITab.#slugify()`, `AITab.#titleFromSurface()`, `Array.isArray()`, `Date.now()`, `lazy.console.error()`, `lazy.l10n.formatValueSync()`, `modifySlug.trim()`, `rawContent.trim()`, `toolConversation .save()`, `toolConversation .save() .catch()`, `toolConversation.addSeenUrls()`, `toolConversation.addSerpUrlsForAnonymousFetch()`, `toolConversation.securityProperties.commit()`, `toolConversation.securityProperties.setPrivateData()`, `toolConversation.securityProperties.setUntrustedInput()`, `urlList.filter()`, `urlList.filter(url => typeof url == "string").slice()`
- 条件付き依存: `if (slug)` → `AITab.#loadPageToModify()`
- 条件付き依存: `if (prior)` → `AITab.#capped()`
- 参照: `conversation?.seenUrls`, `conversation?.serpUrlsForAnonymousFetch`, `prior.error`, `prior.page.slug`, `prior?.conversation`, `prior?.page.context?.creationPrompt`, `prior?.page.context?.urlsUsed`, `prior?.page.title`, `signal?.aborted`, `sources.error`, `structured.conversation`, `structured.error`, `structured.surface`, `toolConversation.id`, `toolConversation.updatedDate`, `urls.length`, `urlsUsed[0].title`

## AITab.#capped()
- 位置: L943-947
- 役割: モデルが渡した自由記述を文字列にして前後の空白を削り、1500字で切る。
- 触るとき: 焦点や修正指示の長さの上限を変えるとき。
- 呼び出し先: `text.trim()`, `text.trim().slice()`

## AITab.#collectSources()
- 位置: async L964-1040
- 役割: 各URLの本文をget_page_contentで取り、読めるものが一つも無ければエラーにする。タブごとに予算(1万字)を等分して本文を切り、og:imageと見出しを付け、直接渡された内容も別の節として加える。
- 触るとき: 生成に使われる本文が欠ける、または切れすぎるとき。予算の大きさを変えるとき。
- 呼び出し先: `AITab.#getPageImage()`, `Math.floor()`, `headLines.join()`, `lazy.GetPageContent.getTabWithURL()`, `lazy.GetPageContent.isContentAllowed()`, `sourceParts.join()`, `sourceParts.push()`, `text.slice()`, `urls.entries()`, `urlsUsed.push()`
- 条件付き依存: `if (urls.length)` → `lazy.GetPageContent.getPageContent()`
- 条件付き依存: `if (urls.length)` → `contents.some()`
- 条件付き依存: `if (imageUrl)` → `headLines.push()`
- 条件付き依存: `if (rawText)` → `sourceParts.push()`
- 条件付き依存: `if (rawText)` → `rawText.slice()`
- 参照: `contents[index]?.content`, `result.ok`, `signal?.aborted`, `tab?.label`, `text.length`, `urls.length`

## AITab.#loadPageToModify()
- 位置: async L1057-1088
- 役割: スラッグのページを読み、そのページが今の会話のものか確かめ、元の会話が残っていればページと元の会話を返す。どれかが欠けていればエラーにする。
- 触るとき: 修正が『この会話に該当するページが無い』で断られるとき、修正対象の選び方を変えるとき。
- 呼び出し先: `lazy.AITabStore.getBySlug()`, `lazy.console.error()`
- 条件付き依存: `if (page?.toolConvId)` → `lazy.ConversationStore.findConversationById()`
- 参照: `conversation?.id`, `page.convId`, `page.toolConvId`, `page?.toolConvId`, `priorConversation?.messageCount`

## AITab.#mergeSources()
- 位置: L1099-1108
- 役割: 以前の出典と今回の出典をURLで重ね、同じURLなら今回の方を採る。以前の出典が無ければ今回のものをそのまま返す。
- 触るとき: 修正のたびに出典が重複する、または消えるとき。
- 呼び出し先: `Array.from()`, `Array.isArray()`, `byUrl.set()`, `byUrl.values()`, `previous.map()`
- 参照: `previous.length`, `source.url`, `source?.url`

## AITab.#titleFromSurface()
- 位置: L1117-1132
- 役割: ヘッダー部品のtitleを読む。文字列ならそのまま、バインドならデータモデルの文字列を使う。どちらも無ければ空文字を返す。
- 触るとき: ページのタイトルが空になる、または期待と違うとき。
- 呼び出し先: `(surface?.components || []).find()`
- 条件付き依存: `if (title && typeof title == "object" && typeof title.path == "string")` → `title.path.startsWith()`
- 条件付き依存: `if (title && typeof title == "object" && typeof title.path == "string")` → `AITab.#resolvePath()`
- 参照: `c?.component`, `header?.title`, `surface.dataModel`, `surface?.components`, `title.path`

## AITab.#getPageImage()
- 位置: async L1141-1152
- 役割: Placesからページのプレビュー画像のURLを取る。失敗しても例外は出さず、空文字を返す。
- 触るとき: ページにプレビュー画像が付かないとき。
- 呼び出し先: `lazy.PlacesUtils.history .fetch()`, `lazy.PlacesUtils.history .fetch(url, { includeMeta: true }) .catch()`, `lazy.console.debug()`
- 参照: `pageInfo.previewImageURL.href`, `pageInfo?.previewImageURL`

## AITab.#hydrateFavicons()
- 位置: async L1171-1224
- 役割: リンクの項目(SourceLinks、Cards、Headerの references、Highlightsの sources)から、モデルが書いたfaviconを消し、hrefごとにPlacesのファビコンURLを引いて入れ直す。
- 触るとき: リンクのアイコンが表示されないとき、モデルが書いたアイコンが残るとき。
- 呼び出し先: `faviconByHref.get()`, `faviconByHref.has()`, `itemsOf()`, `linkItems.push()`
- 条件付き依存: `if (!faviconByHref.has(item.href))` → `faviconByHref.set()`
- 条件付き依存: `if (!faviconByHref.has(item.href))` → `AITab.#getFaviconURL()`
- 参照: `component.items`, `component.references?.items`, `component?.component`, `item.favicon`, `item.href`, `item?.sources?.items`, `signal?.aborted`, `surface?.components`, `surface?.dataModel`

## itemsOf()
- 位置: L1173-1185
- 役割: 値が配列ならそれを、絶対パスのバインドならデータモデルの配列を返す。どちらでもなければ空の配列を返す。
- 触るとき: ファビコンの対象項目が拾えないとき。
- 呼び出し先: `AITab.#isBinding()`, `Array.isArray()`
- 条件付き依存: `if (AITab.#isBinding(value))` → `value.path.startsWith()`
- 条件付き依存: `if (AITab.#isBinding(value))` → `AITab.#resolvePath()`
- 参照: `value.path`

## AITab.#getFaviconURL()
- 位置: async L1233-1243
- 役割: PlacesからページのファビコンのURLを取る。無い場合や失敗した場合は空文字を返す。
- 触るとき: ファビコンが付かない原因を調べるとき。
- 呼び出し先: `Services.io.newURI()`, `lazy.PlacesUtils.favicons.getFaviconForPage()`, `lazy.console.debug()`
- 参照: `favicon?.uri?.spec`
- XPCOM: `Services.io`

## AITab.parsePageConfig()
- 位置: L1253-1274
- 役割: モデル出力の最初の{から最後の}までをJSONとして読む。だめなら最初のコードフェンスの中身で読み直し、両方失敗するとnullを返す。
- 触るとき: モデルの出力がJSONとして読めずに失敗するとき、出力の囲い方の扱いを広げるとき。
- 呼び出し先: `AITab.#parseJsonSpan()`, `lazy.console.error()`, `text.indexOf()`, `text.slice()`

## AITab.expandSurfaceUrlTokens()
- 位置: L1290-1331
- 役割: サーフェスの文字列にあるURLトークンを実際のURLに戻し、解決できない残りは取り除く。hrefとimageは正確に一つのトークンでなければならず、hrefが不正な項目は丸ごと落とす。深さは32までに制限する。
- 触るとき: リンクや画像が消える原因を調べるとき、モデルが与えていないURLを扱う方針を変えるとき。
- 呼び出し先: `AITab.expandSurfaceUrlTokens()`, `Array.isArray()`, `LINK_FIELDS.has()`, `Object.entries()`
- 条件付き依存: `if (typeof value == "string")` → `stripUnresolvedUrlTokens()`
- 条件付き依存: `if (typeof value == "string")` → `expandUrlTokens()`
- 条件付き依存: `if (Array.isArray(value))` → `value .map(item => AITab.expandSurfaceUrlTokens(item, urlTokenizer, recursionDepth + 1) ) .filter()`
- 条件付き依存: `if (Array.isArray(value))` → `value .map()`
- 条件付き依存: `if (Array.isArray(value))` → `AITab.expandSurfaceUrlTokens()`
- 条件付き依存: `if (LINK_FIELDS.has(key))` → `urlTokenizer.resolveExactToken()`
- 条件付き依存: `if (key == "href")` → `lazy.console.warn()`
- 参照: `urlTokenizer.tokenToUrl`

## AITab.tokenizeSurfaceUrls()
- 位置: L1345-1373
- 役割: 保存されたサーフェスのURLを、このリクエストのトークンに置き換える。修正の際に、前のターンのサーフェスをモデルに渡すために使う。
- 触るとき: 修正の文脈でURLが生のまま渡る、またはトークンがずれるとき。
- 呼び出し先: `AITab.tokenizeSurfaceUrls()`, `Array.isArray()`, `LINK_FIELDS.has()`, `Object.entries()`, `urlTokenizer.formatToken()`
- 条件付き依存: `if (typeof value == "string")` → `urlTokenizer.tokenizeText()`
- 条件付き依存: `if (Array.isArray(value))` → `value .map(item => AITab.tokenizeSurfaceUrls(item, urlTokenizer, recursionDepth + 1) ) .filter()`
- 条件付き依存: `if (Array.isArray(value))` → `value .map()`
- 条件付き依存: `if (Array.isArray(value))` → `AITab.tokenizeSurfaceUrls()`

## AITab.#tokenizedMessages()
- 位置: L1385-1399
- 役割: 会話のメッセージをChat補完形式で取り出し、アシスタントの応答はサーフェスとして読んでURLをトークン化する。それ以外の文字列もトークン化する。
- 触るとき: 修正のときにモデルへ渡る履歴の形を変えるとき。
- 呼び出し先: `AITab.parsePageConfig()`, `AITab.tokenizeSurfaceUrls()`, `JSON.stringify()`, `conversation.getMessagesInChatCompletionsFormat()`, `conversation.getMessagesInChatCompletionsFormat().map()`, `urlTokenizer.tokenizeText()`
- 参照: `message.content`, `message.role`

## AITab.#generateStructuredSurface()
- 位置: async L1419-1528
- 役割: カタログを読み、プロンプトを用意して、修正なら既存の会話に続け、新規なら会話を作ってモデルを1回呼ぶ。出力を読んでURLを戻し、検証が通ればアシスタントの応答として会話に記録する。修正で履歴が10万字を超えれば断る。
- 触るとき: 生成の中核で失敗するとき、履歴の上限を変えるとき、モデルへの送信内容を確かめるとき。
- 呼び出し先: `AITab.#resolvePromptSet()`, `AITab.#schemaText()`, `AITab.#tokenizedMessages()`, `AITab.buildSurface()`, `AITab.expandSurfaceUrlTokens()`, `AITab.loadAssets()`, `AITab.parsePageConfig()`, `JSON.stringify()`, `conversation.addAssistantMessage()`, `conversation.addUserMessage()`, `conversation.run()`, `conversation.setSystemMessage()`, `lazy.console.debug()`, `lazy.console.error()`, `lazy.openAIEngine.getFxAccountToken()`, `lazy.renderPrompt()`, `response?.finalOutput?.trim()`, `text.slice()`, `userParts.join()`
- 条件付き依存: `if (sourceText)` → `userParts.push()`
- 条件付き依存: `if (sourceText)` → `lazy.renderPrompt()`
- 条件付き依存: `if (modifyInstructions)` → `userParts.push()`
- 条件付き依存: `if (priorConversation)` → `JSON.stringify()`
- 条件付き依存: `if (history.length > MAX_HISTORY_CHARS)` → `lazy.console.warn()`
- 条件付き依存: `if (!parsed)` → `lazy.console.error()`
- 条件付き依存: `if (!result.ok)` → `lazy.console.error()`
- 参照: `error?.message`, `history.length`, `result.errors`, `result.ok`, `result.surface`, `signal?.aborted`, `text?.length`, `userParts.length`

## AITab.#resolvePromptSet()
- 位置: async L1543-1561
- 役割: 修正なら既存の会話にAITab用のエンジンを付け直し、新規なら会話を作る。システム用と利用者データ用の二つのプロンプトを読んで返す。
- 触るとき: プロンプトの読み込みやエンジンの付け方で生成が始まらないとき。
- 呼び出し先: `Promise.all()`, `lazy.loadPrompt()`
- 条件付き依存: `if (conversation)` → `lazy.buildEngineForFeature()`
- 条件付き依存: `if (!(conversation))` → `lazy.buildConversation()`
- 参照: `conversation.engine`, `conversation.parameters`, `lazy.MODEL_FEATURES.AITAB`

## AITab.#schemaText()
- 位置: L1573-1585
- 役割: カタログの共有defsを先頭に一度だけ、続けて部品ごとのスキーマを、インデントなしのJSON文字列として連結する。
- 触るとき: モデルに渡すスキーマの形や大きさを変えるとき。
- 呼び出し先: `JSON.stringify()`, `parts.join()`, `parts.push()`
- 条件付き依存: `if (catalog.$defs)` → `parts.push()`
- 条件付き依存: `if (catalog.$defs)` → `JSON.stringify()`
- 参照: `catalog.$defs`, `catalog.components`

## AITab.#parseJsonSpan()
- 位置: L1594-1605
- 役割: 最初の{から最後の}までをJSON.parseし、範囲が無い、または解析できない場合はnullを返す。
- 触るとき: JSONの囲いの取り方を変えるとき。
- 呼び出し先: `JSON.parse()`, `text.indexOf()`, `text.lastIndexOf()`, `text.slice()`

## AITab.#slugify()
- 位置: L1613-1622
- 役割: タイトルを小文字にし、英数字以外の連続を_に置き換え、先頭と末尾の_を削って60字で切る。英数字が無ければaitabを返す。
- 触るとき: ページのIDの形式を変えるとき、別のタイトルが同じIDになる原因を調べるとき。
- 呼び出し先: `title .toLowerCase()`, `title .toLowerCase() .replace()`, `title .toLowerCase() .replace(/[^a-z0-9]+/g, "_") .replace()`, `title .toLowerCase() .replace(/[^a-z0-9]+/g, "_") .replace(/^_+|_+$/g, "") .slice()`
