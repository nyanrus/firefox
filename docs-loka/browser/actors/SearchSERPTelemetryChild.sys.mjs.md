# browser/actors/SearchSERPTelemetryChild.sys.mjs

source: browser/actors/SearchSERPTelemetryChild.sys.mjs
source-hash: f1bbe7483b51aa11343a7d75ac04580c185931c6
lines: 1804

## <module>
- 役割: 検索結果ページ(SERP)で広告リンクや広告の表示、検索エンジンの操作、ドメインを調べ、テレメトリ用の情報を親プロセスへ送る子側アクター。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `XPCOMUtils.defineLazyPreferenceGetter()`, `console.createInstance()`

## keydownEnter()
- 位置: L62-62
- 役割: キーイベントが Enter キーかを判定する条件関数。
- 触るとき: Remote Settings の条件名と対応を増やすとき。
- 参照: `event.key`

## SearchProviders.constructor()
- 位置: L75-78
- 役割: プロセスごとに一度だけ作られ、shared data の変化の監視を始める。
- 触るとき: プロバイダー情報のキャッシュの仕組みを変えるとき。
- 呼び出し先: `Services.cpmm.sharedData.addEventListener()`
- 参照: `this._searchProviderInfo`
- XPCOM: `Services.cpmm`

## SearchProviders.info()
- 位置: L87-141
- 役割: 検索プロバイダー情報を読み、広告情報を持つものに絞って正規表現を前もって作って返す。
- 触るとき: プロバイダー情報の読み込みや正規表現の扱いを変えるとき。
- 呼び出し先: `Services.cpmm.sharedData.get()`, `p.extraAdServersRegexps.map()`, `p.impressionAttributes?.map()`, `p.subframes ?.filter()`, `p.subframes ?.filter(obj => obj.inspectRegexpInSERP) .map()`
- 条件付き依存: `if (attribute.element?.regexp)` → `structuredClone()`
- 参照: `SEARCH_TELEMETRY_SHARED.PROVIDER_INFO`, `attribute.element?.regexp`, `newAttribute.element.regexp`, `obj.inspectRegexpInSERP`, `obj.regexp`, `p.adServerAttributes`, `p.searchPageRegexp`, `p.shoppingTab.regexp`, `p.shoppingTab?.inspectRegexpInSERP`, `this._searchProviderInfo`
- XPCOM: `Services.cpmm`

## SearchProviders.handleEvent()
- 位置: L148-159
- 役割: プロバイダー情報が変わったら、キャッシュを消して次回に読み直させる。
- 触るとき: 情報の更新タイミングを変えるとき。
- 呼び出し先: `event.changedKeys.includes()`
- 参照: `SEARCH_TELEMETRY_SHARED.PROVIDER_INFO`, `event.type`, `this._searchProviderInfo`

## ListenerHelper.addListeners()
- 位置: L188-217
- 役割: 要素ごとにリスナーを付け、後始末の関数を文書単位で覚えておく。既存の後始末は残す。
- 触るとき: イベント登録と後始末の仕組みを変えるとき。
- 呼び出し先: `ListenerHelper.addListener()`, `documentToEventCallbackMap.get()`, `documentToRemoveEventListenersMap.has()`, `documentToRemoveEventListenersMap.set()`, `removeListenerCallbacks.concat()`
- 条件付き依存: `if (documentToRemoveEventListenersMap.has(document))` → `documentToRemoveEventListenersMap.get()`
- 参照: `elements?.length`, `elements[0].ownerDocument`, `eventListenerParams?.length`

## ListenerHelper.addListener()
- 位置: L229-282
- 役割: アクションを決め、条件があればその条件を満たした時だけ報告するリスナーを要素に付け、後始末の関数を返す。
- 触るとき: クリックなどの報告条件や対象を変えるとき。
- 呼び出し先: `element.addEventListener()`, `element.removeEventListener()`, `removeListenerCallbacks.push()`
- 参照: `eventListenerParam.condition`

## eventCallback()
- 位置: async L249-259
- 役割: 条件関数が真の時に、アクションと対象を報告に渡す。プロファイラーの計測も行う。
- 触るとき: 条件付きイベントの報告を変えるとき。
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `condition()`
- 条件付き依存: `if (condition(event))` → `callback()`

## eventCallback()
- 位置: L269-271
- 役割: イベントが起きたら、アクションと対象を報告に渡す。
- 触るとき: イベントの報告内容を変えるとき。
- 呼び出し先: `callback()`

## SearchAdImpression.providerInfo()
- 位置: L325-344
- 役割: プロバイダーが変わった時だけ、既定のコンポーネントと上から探すコンポーネントを設定し直す。
- 触るとき: コンポーネント定義の読み込み方を変えるとき。
- 条件付き依存: `if (component.topDown)` → `this.#topDownComponents.push()`
- 参照: `component.default`, `component.topDown`, `providerInfo.telemetryId`, `this.#defaultComponent`, `this.#providerInfo`, `this.#providerInfo.components`, `this.#providerInfo?.telemetryId`, `this.#topDownComponents`

## SearchAdImpression.categorize()
- 位置: L367-463
- 役割: アンカーからの分類と文書全体からの分類を行い、コンポーネントごとの読み込み・表示・非表示の件数と、href からコンポーネントへの対応表を作る。
- 触るとき: 広告の分類結果の集計方法を変えるとき。
- 呼び出し先: `componentToVisibilityMap.has()`, `this.#categorizeAnchors()`, `this.#categorizeDocument()`, `this.#countVisibleAndHiddenAds()`, `this.#elementToAdDataMap.clear()`, `this.#elementToAdDataMap.entries()`
- 条件付き依存: `if (data.type == "incontent_searchbox")` → `ListenerHelper.addListeners()`
- 条件付き依存: `if (data.childElements.length)` → `this.#extractHref()`
- 条件付き依存: `if (href)` → `hrefToComponentMap.set()`
- 条件付き依存: `if (!(data.childElements.length))` → `this.#extractHref()`
- 条件付き依存: `if (componentToVisibilityMap.has(data.type))` → `componentToVisibilityMap.get()`
- 条件付き依存: `if (!(componentToVisibilityMap.has(data.type)))` → `componentToVisibilityMap.set()`
- 参照: `componentInfo.adsHidden`, `componentInfo.adsLoaded`, `componentInfo.adsVisible`, `count.adsHidden`, `count.adsVisible`, `data.adsLoaded`, `data.childElements`, `data.childElements.length`, `data.proxyChildElements`, `data.proxyChildElements.length`, `data.type`, `document.documentGlobal.innerHeight`, `document.documentGlobal.scrollY`, `document.documentURI`, `new URL(document.documentURI).origin`

## SearchAdImpression.detectImpressionAttributes()
- 位置: L482-541
- 役割: プロバイダーが定義した属性ごとに対象の要素が見えているかを調べ、固定値か true と false の結果を返す。
- 触るとき: インプレッション属性の判定を変えるとき。
- 呼び出し先: `Array.from()`, `Array.from(elements).filter()`, `document.querySelectorAll()`, `el.checkVisibility()`, `el.getAttribute()`, `matchedElements.filter()`, `regexp.test()`
- 条件付き依存: `if (component?.type && component.countImpressions)` → `this.#recordElementData()`
- 参照: `attribute.element`, `attribute.key`, `attributes?.length`, `component.countImpressions`, `component.type`, `component?.type`, `this.#providerInfo?.impressionAttributes`, `visibleElements.length`

## SearchAdImpression.#extractHref()
- 位置: L558-586
- 役割: 要素のデータ属性にある広告の URL を優先し、無ければ href を使って絶対 URL にして返す。http と https 以外は空を返す。
- 触るとき: 広告リンクの照合に使う URL の取り方を変えるとき。
- 呼び出し先: `URL.parse()`, `element.getAttribute()`, `regexp.test()`, `this.#providerInfo.extraAdServersRegexps.some()`
- 参照: `element.dataset`, `this.#providerInfo.adServerAttributes`, `url.href`, `url.protocol`

## SearchAdImpression.#categorizeAnchors()
- 位置: L606-644
- 役割: 広告らしいアンカーを 1 つずつ調べ、所属するコンポーネントを記録する。関連要素には操作の監視を付ける。
- 触るとき: アンカーの分類ルールを変えるとき。
- 呼び出し先: `this.#shouldInspectAnchor()`
- 条件付き依存: `if (this.#shouldInspectAnchor(anchor, origin))` → `this.#findDataForAnchor()`
- 条件付き依存: `if (this.#shouldInspectAnchor(anchor, origin))` → `lazy.logConsole.error()`
- 条件付き依存: `if (result)` → `this.#recordElementData()`
- 条件付き依存: `if (result?.relatedElements?.length)` → `ListenerHelper.addListeners()`
- 参照: `result.childElements`, `result.count`, `result.element`, `result.proxyChildElements`, `result.relatedElements`, `result.type`, `result?.relatedElements?.length`

## SearchAdImpression.#categorizeDocument()
- 位置: L653-730
- 役割: トップダウン型のコンポーネントについて、親と子の要素を文書から探し、監視を付けるか記録する。
- 触るとき: 文書全体からの検出を変えるとき。
- 呼び出し先: `document.querySelectorAll()`
- 条件付き依存: `if (eventListeners?.length)` → `ListenerHelper.addListeners()`
- 条件付き依存: `if (component.included.related?.selector)` → `parent.querySelectorAll()`
- 条件付き依存: `if (relatedElements.length)` → `ListenerHelper.addListeners()`
- 条件付き依存: `if (component.included.children)` → `parent.querySelectorAll()`
- 条件付き依存: `if (child.eventListeners)` → `Array.from()`
- 条件付き依存: `if (child.eventListeners)` → `ListenerHelper.addListeners()`
- 条件付き依存: `if (!child.skipCount)` → `this.#recordElementData()`
- 条件付き依存: `if (!child.skipCount)` → `Array.from()`
- 条件付き依存: `if (!component.included.parent.skipCount)` → `this.#recordElementData()`
- 参照: `child.eventListeners`, `child.selector`, `child.skipCount`, `child.type`, `childElements.length`, `component.included.children`, `component.included.parent.eventListeners`, `component.included.parent.selector`, `component.included.parent.skipCount`, `component.included.related.selector`, `component.included.related?.selector`, `component.included?.parent`, `component.topDown`, `component.type`, `eventListeners?.length`, `parents.length`, `relatedElements.length`, `this.#topDownComponents`

## SearchAdImpression.#shouldInspectAnchor()
- 位置: L740-767
- 役割: href かデータ属性が広告サーバーの正規表現に合うかで、そのアンカーを調べる対象にするか決める。
- 触るとき: 調べる対象のアンカーを絞る条件を変えるとき。
- 呼び出し先: `anchor.getAttribute()`, `href.startsWith()`, `regexp.test()`, `regexps.some()`
- 参照: `anchor.dataset`, `this.#providerInfo.adServerAttributes`, `this.#providerInfo.extraAdServersRegexps`

## SearchAdImpression.#findDataForAnchor()
- 位置: L814-925
- 役割: アンカーの親をコンポーネントごとに探し、子要素の有無で数え方を決めて、コンポーネント・要素・件数を返す。どれにも当たらなければ既定のコンポーネントにする。
- 触るとき: 広告の所属判定や数え方を変えるとき。
- 呼び出し先: `anchor.closest()`, `this.#elementToAdDataMap.has()`
- 条件付き依存: `if (component.included.related?.selector)` → `parent.querySelectorAll()`
- 条件付き依存: `if (child.countChildren)` → `parent.querySelectorAll()`
- 条件付き依存: `if (proxyChildElements.length)` → `Array.from()`
- 条件付き依存: `if (!(child.countChildren))` → `parent.querySelector()`
- 参照: `child.countChildren`, `child.selector`, `child.skipCount`, `child.type`, `component.default`, `component.excluded.parent.selector`, `component.excluded?.parent?.selector`, `component.included`, `component.included.children`, `component.included.parent`, `component.included.parent.selector`, `component.included.parent.skipCount`, `component.included.related.selector`, `component.included.related?.selector`, `component.topDown`, `component.type`, `proxyChildElements.length`, `this.#defaultComponent.type`, `this.#providerInfo.components`

## SearchAdImpression.#countVisibleAndHiddenAds()
- 位置: L957-1060
- 役割: 要素と子要素が見えているかを判定し、見えている広告数と隠れている広告数を数える。
- 触るとき: 表示と非表示の判定基準を変えるとき。
- 呼び出し先: `VisibilityHelper.childElementWasVisibleHorizontally()`, `VisibilityHelper.elementWasVisibleVertically()`, `child.checkVisibility()`, `child.documentGlobal.windowUtils.getBoundsWithoutFlushing()`, `element.checkVisibility()`, `element.documentGlobal.windowUtils.getBoundsWithoutFlushing()`
- 条件付き依存: `if ( !element.checkVisibility({ visibilityProperty: true, opacityProperty: true, }) )` → `Glean.serp.adsBlockedCount.hidden_parent.add()`
- 条件付き依存: `if ( elementRect.bottom < 0 && innerWindowHeight + scrollY + elementRect.bottom < 0 )` → `Glean.serp.adsBlockedCount.beyond_viewport.add()`
- 条件付き依存: `if (!childElements?.length)` → `VisibilityHelper.elementWasVisibleVertically()`
- 条件付き依存: `if ( !child.checkVisibility({ visibilityProperty: true, opacityProperty: true, }) )` → `Glean.serp.adsBlockedCount.hidden_child.add()`
- 参照: `childElements?.length`, `elementRect.bottom`

## SearchAdImpression.#recordElementData()
- 位置: L1087-1105
- 役割: 要素ごとに種類と読み込み数を一度だけ記録する。既に記録があれば子要素を追加する。
- 触るとき: 要素単位の記録方法を変えるとき。
- 呼び出し先: `this.#elementToAdDataMap.has()`
- 条件付き依存: `if (this.#elementToAdDataMap.has(element))` → `this.#elementToAdDataMap.get()`
- 条件付き依存: `if (childElements.length)` → `recordedValues.childElements.concat()`
- 条件付き依存: `if (!(this.#elementToAdDataMap.has(element)))` → `this.#elementToAdDataMap.set()`
- 参照: `childElements.length`, `recordedValues.childElements`

## VisibilityHelper.elementWasVisibleVertically()
- 位置: L1122-1124
- 役割: 要素の上端から閾値分の高さが、ウィンドウの高さ以内にあるかを返す。上方向にあるものは見えていたとみなす。
- 触るとき: 縦方向の表示判定を変えるとき。
- 参照: `rect.height`, `rect.top`

## VisibilityHelper.childElementWasVisibleHorizontally()
- 位置: L1139-1144
- 役割: 子要素の左端から閾値分の幅が、親の右端以内にあるかを返す。左側にあるものは見えていたとみなす。
- 触るとき: 横方向の表示判定を変えるとき。
- 参照: `childRect.left`, `childRect.width`, `parentRect.left`, `parentRect.width`

## DomainExtractor.extractDomainsFromDocument()
- 位置: L1185-1236
- 役割: 抽出設定ごとに href、データ属性、テキストのいずれかでドメインを集め、上限まで集合にして返す。
- 触るとき: ドメイン抽出の対象や方法を変えるとき。
- 呼び出し先: `document.querySelectorAll()`, `this.#fromElementsConvertHrefsIntoDomains()`, `this.#fromElementsRetrieveDataAttributeValues()`, `this.#fromElementsRetrieveTextContent()`
- 参照: `document.documentURI`, `elements.length`, `extractorInfo.method`, `extractorInfo.options?.dataAttributeKey`, `extractorInfo.options?.queryParamKey`, `extractorInfo.options?.queryParamValueIsHref`, `extractorInfo.selectors`, `extractorInfos?.length`, `new URL(document.documentURI).origin`

## DomainExtractor.#fromElementsConvertHrefsIntoDomains()
- 位置: L1258-1302
- 役割: href の URL からホスト名を取る。クエリの指定があれば、その値をドメインとして使う。
- 触るとき: href からのドメインの取り方を変えるとき。
- 呼び出し先: `URL.parse()`, `element.getAttribute()`, `this.#exceedsThreshold()`
- 条件付き依存: `if (queryParam)` → `url.searchParams.get()`
- 条件付き依存: `if (queryParamValueIsHref)` → `URL.parse()`
- 条件付き依存: `if (queryParamValueIsHref)` → `this.#processDomain()`
- 条件付き依存: `if (queryParam)` → `extractedDomains.has()`
- 条件付き依存: `if (paramValue && !extractedDomains.has(paramValue))` → `extractedDomains.add()`
- 条件付き依存: `if (url.hostname)` → `this.#processDomain()`
- 条件付き依存: `if (url.hostname)` → `extractedDomains.has()`
- 条件付き依存: `if (processedHostname && !extractedDomains.has(processedHostname))` → `extractedDomains.add()`
- 参照: `URL.parse(paramValue)?.hostname`, `extractedDomains.size`, `url.hostname`, `url.protocol`

## DomainExtractor.#fromElementsRetrieveDataAttributeValues()
- 位置: L1319-1335
- 役割: 指定のデータ属性の値を、そのままドメインとして処理して集める。
- 触るとき: データ属性からの取り方を変えるとき。
- 呼び出し先: `extractedDomains.has()`, `this.#exceedsThreshold()`, `this.#processDomain()`
- 条件付き依存: `if (value && !extractedDomains.has(value))` → `extractedDomains.add()`
- 参照: `element.dataset`, `extractedDomains.size`

## DomainExtractor.#fromElementsRetrieveTextContent()
- 位置: L1350-1396
- 役割: テキストが URL らしければホスト名を取り、そうでなければ fixup で推定したドメインを集める。
- 触るとき: テキストからの推定を変えるとき。
- 呼び出し先: `LOOSE_URL_REGEX.test()`, `extractedDomains.has()`, `this.#exceedsThreshold()`, `this.#processDomain()`
- 条件付き依存: `if (LOOSE_URL_REGEX.test(textContent))` → `/^https?:\/\//.test()`
- 条件付き依存: `if (LOOSE_URL_REGEX.test(textContent))` → `URL.parse()`
- 条件付き依存: `if (!domain)` → `fixup()`
- 条件付き依存: `if (!(LOOSE_URL_REGEX.test(textContent)))` → `fixup()`
- 条件付き依存: `if (processedDomain && !extractedDomains.has(processedDomain))` → `extractedDomains.add()`
- 参照: `URL.parse(textContent)?.hostname`, `element.textContent`, `extractedDomains.size`

## fixup()
- 位置: L1359-1365
- 役割: テキストを小文字にし、空白と末尾のドットを除いて .com を付ける。
- 触るとき: テキストからドメインを推定する規則を変えるとき。
- 呼び出し先: `textContent .toLowerCase()`, `textContent .toLowerCase() .replaceAll()`, `textContent .toLowerCase() .replaceAll(" ", "") .replace()`, `textContent .toLowerCase() .replaceAll(" ", "") .replace(/\.$/, "") .concat()`

## DomainExtractor.#processDomain()
- 位置: L1409-1417
- 役割: プロバイダー名を含むドメインは除外し、残りはサブドメインを取り除いて返す。
- 触るとき: 除外するドメインの条件を変えるとき。
- 呼び出し先: `domain.includes()`, `domain.startsWith()`, `this.#stripDomainOfSubdomains()`

## DomainExtractor.#stripDomainOfSubdomains()
- 位置: L1427-1440
- 役割: 公開サフィックスを使い、登録可能ドメインまで切り詰める。判定できなければ空を返す。
- 触るとき: ドメインの正規化方法を変えるとき。
- 呼び出し先: `Services.eTLD.getKnownPublicSuffixFromHost()`, `domain.substring()`, `domainWithoutTLD.split()`, `domainWithoutTLD.split(".").at()`
- 参照: `domain.length`, `tld.length`
- XPCOM: `Services.eTLD`

## DomainExtractor.#exceedsThreshold()
- 位置: L1449-1451
- 役割: 集めたドメインの数が上限に達したかを返す。
- 触るとき: ドメインの上限数を変えるとき。
- 参照: `CATEGORIZATION_SETTINGS.MAX_DOMAINS_TO_CATEGORIZE`

## SearchSERPTelemetryChild._getProviderInfoForUrl()
- 位置: L1487-1489
- 役割: URL に合う検索プロバイダーの情報を探して返す。
- 触るとき: プロバイダーの判定方法を変えるとき。
- 呼び出し先: `info.searchPageRegexp.test()`, `searchProviders.info?.find()`

## SearchSERPTelemetryChild._checkForAdLink()
- 位置: L1495-1632
- 役割: SERP の広告リンクと広告用のサブフレームを確かめ、ページ情報を親へ送る。読み込み時のみ、広告の分類と表示の計測、ドメインの抽出を行う。
- 触るとき: SERP テレメトリの送信内容やタイミングを変えるとき。
- 呼び出し先: `doc.getElementsByTagName()`, `regexp.test()`, `regexps.some()`, `this._getProviderInfoForUrl()`, `this.sendAsyncMessage()`
- 条件付き依存: `if (!hasAds)` → `regexps.some()`
- 条件付き依存: `if (!hasAds)` → `regexp.test()`
- 条件付き依存: `if (!hasAds)` → `this.#checkForSponsoredSubframes()`
- 条件付き依存: `if ( providerInfo.components?.length && (eventType == "load" || eventType == "pageshow") )` → `this.#detectImpressionAttributes()`
- 条件付き依存: `if ( providerInfo.components?.length && (eventType == "load" || eventType == "pageshow") )` → `ChromeUtils.now()`
- 条件付き依存: `if ( providerInfo.components?.length && (eventType == "load" || eventType == "pageshow") )` → `Glean.serp.categorizationDuration.start()`
- 条件付き依存: `if ( providerInfo.components?.length && (eventType == "load" || eventType == "pageshow") )` → `documentToEventCallbackMap.set()`
- 条件付き依存: `if ( providerInfo.components?.length && (eventType == "load" || eventType == "pageshow") )` → `searchAdImpression.categorize()`
- 条件付き依存: `if ( providerInfo.components?.length && (eventType == "load" || eventType == "pageshow") )` → `Glean.serp.categorizationDuration.cancel()`
- 条件付き依存: `if ( providerInfo.components?.length && (eventType == "load" || eventType == "pageshow") )` → `this.sendAsyncMessage()`
- 条件付き依存: `if (componentToVisibilityMap && hrefToComponentMap)` → `ChromeUtils.addProfilerMarker()`
- 条件付き依存: `if (componentToVisibilityMap && hrefToComponentMap)` → `Glean.serp.categorizationDuration.stopAndAccumulate()`
- 条件付き依存: `if (componentToVisibilityMap && hrefToComponentMap)` → `this.sendAsyncMessage()`
- 条件付き依存: `if ( lazy.serpEventTelemetryCategorization && lazy.serpEventTelemetryCategorizationRegionEnabled && providerInfo.domainExtraction && (eventType == "load" || even...)` → `ChromeUtils.now()`
- 条件付き依存: `if ( lazy.serpEventTelemetryCategorization && lazy.serpEventTelemetryCategorizationRegionEnabled && providerInfo.domainExtraction && (eventType == "load" || even...)` → `domainExtractor.extractDomainsFromDocument()`
- 条件付き依存: `if ( lazy.serpEventTelemetryCategorization && lazy.serpEventTelemetryCategorizationRegionEnabled && providerInfo.domainExtraction && (eventType == "load" || even...)` → `this.sendAsyncMessage()`
- 条件付き依存: `if ( lazy.serpEventTelemetryCategorization && lazy.serpEventTelemetryCategorizationRegionEnabled && providerInfo.domainExtraction && (eventType == "load" || even...)` → `ChromeUtils.addProfilerMarker()`
- 参照: `anchor.dataset`, `anchor.href`, `doc.documentURI`, `lazy.serpEventTelemetryCategorization`, `lazy.serpEventTelemetryCategorizationRegionEnabled`, `providerInfo.adServerAttributes`, `providerInfo.components?.length`, `providerInfo.domainExtraction`, `providerInfo.domainExtraction.ads`, `providerInfo.domainExtraction.nonAds`, `providerInfo.extraAdServersRegexps`, `providerInfo.telemetryId`, `result.componentToVisibilityMap`, `result.hrefToComponentMap`, `this.contentWindow`, `this.document`

## pageActionCallback()
- 位置: L1554-1562
- 役割: 操作の報告を受け、送信があれば文書を記録し、親へ操作を送る。
- 触るとき: 操作テレメトリの内容を変えるとき。
- 呼び出し先: `this.sendAsyncMessage()`
- 条件付き依存: `if (info.action == "submitted")` → `documentToSubmitMap.set()`
- 参照: `info.action`, `info.target`

## SearchSERPTelemetryChild.#detectImpressionAttributes()
- 位置: L1643-1655
- 役割: プロバイダー情報を設定してから文書の属性を判定し、結果を返す。計測も付ける。
- 触るとき: インプレッション属性の取得経路を変えるとき。
- 呼び出し先: `ChromeUtils.addProfilerMarker()`, `ChromeUtils.now()`, `searchAdImpression.detectImpressionAttributes()`
- 参照: `searchAdImpression.providerInfo`, `this.document`

## SearchSERPTelemetryChild.#checkForSponsoredSubframes()
- 位置: L1657-1679
- 役割: 広告用の iframe のうち、見えているものがあれば真を返す。
- 触るとき: サブフレームでの広告判定を変えるとき。
- 呼び出し先: `document.querySelectorAll()`, `obj.regexp?.test()`, `providerInfo.subframes.some()`, `subframe.checkVisibility()`
- 参照: `providerInfo.subframes?.length`, `subframe.src`

## SearchSERPTelemetryChild.#removeEventListeners()
- 位置: L1681-1689
- 役割: 文書に付けた監視をすべて外し、記録から消す。
- 触るとき: 監視の後始末を変えるとき。
- 呼び出し先: `documentToRemoveEventListenersMap.get()`
- 条件付き依存: `if (callbacks)` → `callback()`
- 条件付き依存: `if (callbacks)` → `documentToRemoveEventListenersMap.delete()`
- 参照: `this.document`

## SearchSERPTelemetryChild.handleEvent()
- 位置: L1696-1736
- 役割: SERP のときだけ、読み込みの各イベントで広告の確認を予約する。pagehide では監視を外し、予約を取り消す。
- 触るとき: 広告の確認のタイミングを変えるとき。
- 呼び出し先: `documentToRemoveEventListenersMap.get()`, `this.#cancelCheck()`, `this.#check()`, `this.#urlIsSERP()`
- 条件付き依存: `if (event.persisted)` → `this.#check()`
- 条件付き依存: `if (callbacks)` → `removeEventListenerCallback()`
- 条件付き依存: `if (callbacks)` → `documentToRemoveEventListenersMap.delete()`
- 参照: `event.persisted`, `event.type`, `this.document`

## SearchSERPTelemetryChild.receiveMessage()
- 位置: async L1738-1753
- 役割: SPA の読み込み待ち、文書の追跡の終了、送信の確認に応える。
- 触るとき: 親からの要求の種類を変えるとき。
- 呼び出し先: `Services.cpmm.sharedData.get()`, `lazy.setTimeout()`, `this.#didSubmit()`, `this.#removeDocumentFromSubmitMap()`, `this.#removeEventListeners()`, `this._checkForAdLink()`
- 参照: `SEARCH_TELEMETRY_SHARED.SPA_LOAD_TIMEOUT`, `message.name`
- XPCOM: `Services.cpmm`

## SearchSERPTelemetryChild.#didSubmit()
- 位置: L1755-1757
- 役割: 文書が送信されたかを記録から返す。
- 触るとき: 送信検出の仕組みを変えるとき。
- 呼び出し先: `documentToSubmitMap.get()`
- 参照: `this.document`

## SearchSERPTelemetryChild.#removeDocumentFromSubmitMap()
- 位置: L1759-1761
- 役割: 文書の送信記録を消す。
- 触るとき: 送信記録の寿命を変えるとき。
- 呼び出し先: `documentToSubmitMap.delete()`
- 参照: `this.document`

## SearchSERPTelemetryChild.#urlIsSERP()
- 位置: L1763-1784
- 役割: URL がプロバイダーの検索結果ページかを判定する。POST 型は URL の一致だけで判定し、それ以外は検索語のパラメータの有無で判定する。
- 触るとき: SERP の判定条件を変えるとき。
- 呼び出し先: `this._getProviderInfoForUrl()`
- 条件付き依存: `if (provider)` → `URL.fromURI()`
- 条件付き依存: `if (provider)` → `queries.get()`
- 参照: `URL.fromURI(this.document.documentURIObject).searchParams`, `provider.alwaysMatchSERP?.child`, `provider.queryParamNames`, `this.document.documentURI`, `this.document.documentURIObject`

## SearchSERPTelemetryChild.#cancelCheck()
- 位置: L1786-1790
- 役割: 予約中の確認タイマーを取り消す。
- 触るとき: 確認タイマーの管理を変えるとき。
- 条件付き依存: `if (this._waitForContentTimeout)` → `lazy.clearTimeout()`
- 参照: `this._waitForContentTimeout`

## SearchSERPTelemetryChild.#check()
- 位置: L1792-1802
- 役割: 読み込み待ちの時間を一度だけ shared data から取り、前の予約を取り消して確認を予約する。
- 触るとき: 広告の確認を遅らせる時間の決め方を変えるとき。
- 呼び出し先: `lazy.setTimeout()`, `this.#cancelCheck()`, `this._checkForAdLink()`
- 条件付き依存: `if (!this.#adTimeout)` → `Services.cpmm.sharedData.get()`
- 参照: `SEARCH_TELEMETRY_SHARED.LOAD_TIMEOUT`, `this.#adTimeout`, `this._waitForContentTimeout`
- XPCOM: `Services.cpmm`
