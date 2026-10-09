# browser/components/tabbrowser/SmartTabGrouping.sys.mjs

source: browser/components/tabbrowser/SmartTabGrouping.sys.mjs
source-hash: c9964090c0be60ae084494a6125cc72878a606b4
lines: 2064

## <module>
- 役割: (未記入)
- 呼び出し先: `XPCOMUtils.declareLazy()`

## getBestAnchorClusterInfo()
- 位置: L197-208
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.max()`, `anchorItemSet.has()`, `g.reduce()`, `groupIndices.map()`, `numItemsList.indexOf()`

## isSearchTab()
- 位置: L218-238
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `curURL.substring()`, `linkedBrowser.getAttribute()`, `searchURL.indexOf()`, `searchURL.substring()`

## SmartTabGroupingManager.constructor()
- 位置: L246-257
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `structuredClone()`, `super()`

## SmartTabGroupingManager.id()
- 位置: L264-266
- 役割: (未記入)
- 触るとき: (未記入)

## SmartTabGroupingManager.hasDistinctEnabledState()
- 位置: L274-279
- 役割: (未記入)
- 触るとき: (未記入)

## SmartTabGroupingManager.canRunOnDevice()
- 位置: L286-289
- 役割: (未記入)
- 触るとき: (未記入)

## SmartTabGroupingManager.enable()
- 位置: async L296-300
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## SmartTabGroupingManager.block()
- 位置: async L307-317
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `SmartTabGroupingManager.deleteSmartTabModels()`
- XPCOM: `Services.prefs`

## SmartTabGroupingManager.isEnabled()
- 位置: L324-334
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## SmartTabGroupingManager.isAllowed()
- 位置: L341-343
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.locale.appLocaleAsBCP47.startsWith()`
- XPCOM: `Services.locale`

## SmartTabGroupingManager.makeAvailable()
- 位置: async L350-359
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.setBoolPref()`, `SmartTabGroupingManager.deleteSmartTabModels()`
- XPCOM: `Services.prefs`

## SmartTabGroupingManager.isBlocked()
- 位置: L366-371
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## SmartTabGroupingManager.isManagedByPolicy()
- 位置: L378-380
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.prefIsLocked()`
- XPCOM: `Services.prefs`

## SmartTabGroupingManager.deleteSmartTabModels()
- 位置: async L387-397
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.MLUninstallService.uninstall()`

## SmartTabGroupingManager.isEngineClosed()
- 位置: L404-406
- 役割: (未記入)
- 触るとき: (未記入)

## SmartTabGroupingManager.getEmbeddingsGenerator()
- 位置: L413-418
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.embeddingsGenerator)` → `embeddingsGeneratorFactory.forGeneral()`

## SmartTabGroupingManager.initEmbeddingEngine()
- 位置: async L423-429
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getEmbeddingsGenerator()`, `this.getEmbeddingsGenerator().embedMany()`, `this.getEmbeddingsGenerator().ensureEngine()`

## SmartTabGroupingManager.getTabsToProcess()
- 位置: L441-489
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `seen.has()`, `shouldInclude()`, `tabsToProcess.slice()`
- 条件付き依存: `if (!seen.has(tab))` → `seen.add()`
- 条件付き依存: `if (!seen.has(tab))` → `tabsToProcess.push()`

## shouldInclude()
- 位置: L449-457
- 役割: (未記入)
- 触るとき: (未記入)

## SmartTabGroupingManager.smartTabGroupingForGroup()
- 位置: async L498-558
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `allTabs .map()`, `allTabs .map((t, i) => (t.group ? i : -1)) .filter()`, `c.tabs.includes()`, `clusters.clusterRepresentations.find()`, `groupTabs.includes()`, `groupTabs.some()`, `suggestedTabs.slice()`, `this.findNearestNeighbors()`, `this.findSimilarTabsLogisticRegression()`, `this.generateClusters()`, `this.generateClusters( allTabs, null, null, null, groupIndices, alreadyGroupedIndices ).then()`, `this.getTabsToProcess()`
- 条件付き依存: `if (groupTabs.includes(allTabs[i]))` → `groupIndices.push()`
- 条件付き依存: `if (targetCluster)` → `targetCluster.tabs.filter()`

## SmartTabGroupingManager.getTabsToSuggest()
- 位置: L568-584
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TAB_URLS_TO_EXCLUDE.includes()`, `allTabs .map()`, `allTabs .map((_, index) => index) .filter()`, `allTabs .map((at, index) => (TAB_URLS_TO_EXCLUDE.includes(at.url) ? index : -1)) .filter()`, `excludedTabIndices.includes()`

## SmartTabGroupingManager.findNearestNeighbors()
- 位置: async L596-669
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.min()`, `closestTabs.map()`, `closestTabs.sort()`, `cosSim()`, `this._prepareTabData()`, `this.getTabsToSuggest()`
- 条件付き依存: `if (precomputedEmbeddings.length === 0)` → `this._generateEmbeddings()`
- 条件付き依存: `if (precomputedEmbeddings.length === 0)` → `tabData.map()`
- 条件付き依存: `if (precomputedEmbeddings.length === 0)` → `SmartTabGroupingManager.preprocessText()`
- 条件付き依存: `if (precomputedEmbeddings.length === 0)` → `groupedIndices.includes()`
- 条件付き依存: `if (groupLabel && groupedIndices.includes(index))` → `groupLabel.slice()`
- 条件付き依存: `if (closestScore > thresholdMills / 1000)` → `closestTabs.push()`
- 条件付き依存: `if (closestScore > thresholdMills / 1000)` → `similarTabsIndices.push()`
- 条件付き依存: `if (groupedIndices.length === 1 && !!closestTabs.length && depth === 1)` → `this.findNearestNeighbors()`
- 条件付き依存: `if (groupedIndices.length === 1 && !!closestTabs.length && depth === 1)` → `alreadyGroupedIndices.concat()`
- 条件付き依存: `if (groupedIndices.length === 1 && !!closestTabs.length && depth === 1)` → `closestTabs.concat()`

## SmartTabGroupingManager.getAverageSimilarity()
- 位置: L677-687
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `averageSimilarities.push()`, `cosSim()`

## SmartTabGroupingManager.getMaxSimilarity()
- 位置: L696-709
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cosSim()`, `maxSimilarities.push()`

## SmartTabGroupingManager.getBaseDomain()
- 位置: L717-748
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.eTLD .getBaseDomain()`, `Services.eTLD .getBaseDomain(Services.io.newURI(url.toLowerCase()), 1) .replace()`, `Services.io.newURI()`, `hostname.toLowerCase()`, `url.toLowerCase()`
- XPCOM: `Services.eTLD` / `Services.io`

## SmartTabGroupingManager.getDomainMatchFractions()
- 位置: L758-777
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SmartTabGroupingManager.getBaseDomain()`, `anchorTabsPrep.map()`, `candidateTabsPrep.map()`

## SmartTabGroupingManager.sigmoid()
- 位置: L785-787
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.exp()`

## SmartTabGroupingManager.calculateProbability()
- 位置: L798-813
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.sigmoid()`

## SmartTabGroupingManager.calculateAllProbabilities()
- 位置: L823-851
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.isArray()`, `probabilities.push()`, `this.calculateProbability()`

## SmartTabGroupingManager.findSimilarTabsLogisticRegression()
- 位置: async L861-936
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SmartTabGroupingManager.preprocessText()`, `anchorTabsPrep .concat()`, `anchorTabsPrep .concat(candidateTabsPrep) .map()`, `candidateIndices.map()`, `candidateTabsData // combine candidate tabs with corresponding probabilities .map()`, `groupedIndices .map()`, `groupedIndices .map(gi => tabData[gi]) .slice()`, `this._generateEmbeddings()`, `this._prepareTabData()`, `this.calculateAllProbabilities()`, `this.getDomainMatchFractions()`, `this.getMaxSimilarity()`, `this.getTabsToSuggest()`, `titleEmbeddings.slice()`
- 条件付き依存: `if (groupLabel)` → `this._generateEmbeddings()`
- 条件付き依存: `if (groupLabel)` → `this.getAverageSimilarity()`
- 条件付き依存: `if (groupLabel)` → `titleEmbeddings.slice()`

## SmartTabGroupingManager.terminateProcess()
- 位置: L942-945
- 役割: (未記入)
- 触るとき: (未記入)

## SmartTabGroupingManager.setClusteringMethod()
- 位置: L952-957
- 役割: (未記入)
- 触るとき: (未記入)

## SmartTabGroupingManager.setAnchorMethod()
- 位置: L964-969
- 役割: (未記入)
- 触るとき: (未記入)

## SmartTabGroupingManager.setSilBoost()
- 位置: L971-973
- 役割: (未記入)
- 触るとき: (未記入)

## SmartTabGroupingManager.setDimensionReductionMethod()
- 位置: L980-985
- 役割: (未記入)
- 触るとき: (未記入)

## SmartTabGroupingManager.setDataTitleKey()
- 位置: L993-995
- 役割: (未記入)
- 触るとき: (未記入)

## SmartTabGroupingManager.log()
- 位置: L1003-1003
- 役割: (未記入)
- 触るとき: (未記入)

## SmartTabGroupingManager._prepareTabData()
- 位置: async L1013-1036
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `structuredData.push()`

## SmartTabGroupingManager.getUpdatedInitData()
- 位置: L1045-1054
- 役割: (未記入)
- 触るとき: (未記入)

## SmartTabGroupingManager._createMLEngine()
- 位置: async L1063-1094
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `SmartTabGroupingManager.getUpdatedInitData()`, `createEngine()`

## SmartTabGroupingManager._generateEmbeddings()
- 位置: async L1103-1109
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getEmbeddingsGenerator()`, `this.getEmbeddingsGenerator().embedMany()`

## SmartTabGroupingManager._clusterEmbeddings()
- 位置: L1122-1241
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Error()`, `kmeansPlusPlus()`, `silScores.reduce()`, `silhouetteCoefficients()`, `tempResult.getCentroidInertia()`
- 条件付き依存: `if (!k)` → `Math.min()`
- 条件付き依存: `if (!k)` → `Math.floor()`
- 条件付き依存: `if (!k)` → `Math.log()`
- 条件付き依存: `if (anchorIndices && !freezeAnchorsInZeroCluster)` → `getBestAnchorClusterInfo()`
- 条件付き依存: `if (anchorIndices)` → `result.setAnchorClusterIndex()`
- 条件付き依存: `if (!freezeAnchorsInZeroCluster)` → `result.adjustClusterForAnchors()`

## SmartTabGroupingManager.getPredictedLabelForGroup()
- 位置: async L1250-1263
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.createStaticCluster()`, `this.generateGroupLabels()`

## SmartTabGroupingManager._clusterEmbeddingsHAC()
- 位置: L1274-1285
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `agglomerativeClusterCosine()`

## SmartTabGroupingManager.generateClusters()
- 位置: async L1298-1351
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `bestResultCluster?.clusterRepresentations.forEach()`, `curResult.getCentroidInertia()`, `rep.getCohesion()`, `this._clusterEmbeddings()`, `this._clusterEmbeddingsHAC()`, `this._prepareTabData()`
- 条件付き依存: `if (!(precomputedEmbeddings))` → `this._generateEmbeddings()`
- 条件付き依存: `if (!(precomputedEmbeddings))` → `structuredData.map()`
- 条件付き依存: `if (!(precomputedEmbeddings))` → `SmartTabGroupingManager.preprocessText()`

## SmartTabGroupingManager.createStaticCluster()
- 位置: L1359-1369
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Array.from()`

## SmartTabGroupingManager.preloadAllModels()
- 位置: async L1378-1429
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.all()`, `mutliProgressAggregator?.aggregateCallback.bind()`, `this._createMLEngine()`, `this.initEmbeddingEngine()`

## progressCallback()
- 位置: L1389-1411
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.abs()`
- 条件付き依存: `if ( Math.abs(previousProgress - progress) > UPDATE_THRESHOLD_PERCENTAGE )` → `progressCallback()`

## SmartTabGroupingManager.createModelInput()
- 位置: L1437-1442
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `documents.join()`, `keywords.join()`
- 条件付き依存: `if (!keywords || keywords.length === 0)` → `documents.join()`

## SmartTabGroupingManager.cutAtDuplicateWords()
- 位置: L1452-1473
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `phrase.split()`, `wordList[i].toLowerCase()`, `wordsSet.add()`, `wordsSet.has()`
- 条件付き依存: `if (baseWord.length > 3)` → `baseWord.slice()`
- 条件付き依存: `if (baseWord.slice(-1) === "s")` → `baseWord.slice()`
- 条件付き依存: `if (wordsSet.has(baseWord))` → `wordList.slice(0, i).join()`
- 条件付き依存: `if (wordsSet.has(baseWord))` → `wordList.slice()`

## SmartTabGroupingManager.preprocessText()
- 位置: L1482-1510
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `splitText.slice()`, `splitText.slice(0, -1).join()`, `text.split()`
- 条件付き依存: `if (hasEnoughInfo && isPotentialDomainInfo)` → `splitText .slice(0, -1) // everything except the last element .map(t => t.trim()) .filter()`
- 条件付き依存: `if (hasEnoughInfo && isPotentialDomainInfo)` → `splitText .slice(0, -1) // everything except the last element .map()`
- 条件付き依存: `if (hasEnoughInfo && isPotentialDomainInfo)` → `splitText .slice()`
- 条件付き依存: `if (hasEnoughInfo && isPotentialDomainInfo)` → `t.trim()`

## SmartTabGroupingManager.processTopicModelResult()
- 位置: L1517-1527
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(topic || "").trim()`, `LABELS_TO_EXCLUDE.includes()`, `SmartTabGroupingManager.cutAtDuplicateWords()`, `basicResult.toLowerCase()`

## SmartTabGroupingManager.generateGroupLabels()
- 位置: async L1539-1589
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Services.prefs.getBoolPref()`, `SmartTabGroupingManager.isEngineClosed()`, `genLabelResults.forEach()`, `groupingResult.getRepresentativeDocsAndKeywords()`, `otherGroupingResult.getRepresentativeDocuments()`, `this.createModelInput()`, `this.processTopicModelResult()`, `this.topicEngine.run()`
- 条件付き依存: `if ( searchTopicSpecialCase && groupingResult.clusterRepresentations.length == 1 && groupingResult.clusterRepresentations[0].isSingleTabSearch )` → `groupingResult.clusterRepresentations[0].setSingleTabSearchLabel()`
- 条件付き依存: `if (SmartTabGroupingManager.isEngineClosed(this.topicEngine))` → `this._createMLEngine()`
- XPCOM: `Services.prefs`

## SmartTabGroupingManager.getLabelReason()
- 位置: L1591-1593
- 役割: (未記入)
- 触るとき: (未記入)

## SmartTabGroupingManager.handleLabelTelemetry()
- 位置: async L1605-1630
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.tabgroup.smartTabTopic.record()`, `lazy.NLP.levenshtein()`, `this.getEngineConfigs()`, `this.getLabelReason()`

## SmartTabGroupingManager.handleSuggestTelemetry()
- 位置: async L1644-1666
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Glean.tabgroup.smartTabSuggest.record()`, `this.getEmbeddingsGenerator()`, `this.getEngineConfigs()`

## SmartTabGroupingManager.getEngineConfigs()
- 位置: async L1673-1689
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.topicEngineConfig)` → `lazy.MLEngineParent.getInferenceOptions()`
- 条件付き依存: `if (!this.embeddingEngineConfig)` → `this.getEmbeddingsGenerator()`
- 条件付き依存: `if (!this.embeddingEngineConfig)` → `lazy.MLEngineParent.getInferenceOptions()`

## SmartTabGroupingResult.constructor()
- 位置: L1704-1710
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `indices.filter()`, `this._buildClusterRepresentations()`

## SmartTabGroupingResult._buildClusterRepresentations()
- 位置: L1715-1728
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `subClusterIndices.map()`, `this.indices.map()`

## SmartTabGroupingResult.getRepresentativeDocuments()
- 位置: L1736-1744
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.documents.slice()`
- 条件付き依存: `if (!this.documents)` → `this.tabItems.map()`

## SmartTabGroupingResult.getRepresentativeDocsAndKeywords()
- 位置: L1753-1766
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.getRepresentativeDocuments()`
- 条件付き依存: `if (!this.keywords)` → `this.documents.slice(0, 3).join()`
- 条件付き依存: `if (!this.keywords)` → `this.documents.slice()`
- 条件付き依存: `if (!this.keywords)` → `otherDocuments.join()`
- 条件付き依存: `if (this.documents.length > 1)` → `keywordExtractor.fitTransform()`

## SmartTabGroupingResult.setAnchorClusterIndex()
- 位置: L1768-1770
- 役割: (未記入)
- 触るとき: (未記入)

## SmartTabGroupingResult.getAnchorCluster()
- 位置: L1777-1782
- 役割: (未記入)
- 触るとき: (未記入)

## SmartTabGroupingResult.adjustClusterForAnchors()
- 位置: L1788-1806
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `anchorSet.has()`, `this._buildClusterRepresentations()`, `this.indices[i].filter()`
- 条件付き依存: `if (anchorSet.has(item))` → `this.indices[this.#anchorClusterIndex].push()`

## SmartTabGroupingResult.printClusters()
- 位置: L1811-1815
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cluster.print()`

## SmartTabGroupingResult.getCentroidInertia()
- 位置: L1822-1828
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `rep.computeTotalSquaredCentroidDistance()`, `this.clusterRepresentations.forEach()`

## SmartTabGroupingResult._flatMapItemsInClusters()
- 位置: L1836-1846
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `clusterRep.tabs.map()`, `result.concat()`, `this.clusterRepresentations.reduce()`

## SmartTabGroupingResult.getRandScore()
- 位置: L1855-1858
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `computeRandScore()`, `this._flatMapItemsInClusters()`

## SmartTabGroupingResult.getAccuracyStatsForCluster()
- 位置: L1867-1901
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `combinedItems.find()`, `combinedItems.forEach()`, `getAccuracyStats()`, `this._flatMapItemsInClusters()`

## genHexString()
- 位置: L1910-1917
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Math.floor()`, `Math.random()`, `hex.charAt()`

## EmbeddingCluster.constructor()
- 位置: L1920-1925
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `computeCentroidFrom2DArray()`

## EmbeddingCluster.computeTotalSquaredCentroidDistance()
- 位置: L1930-1939
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `euclideanDistance()`, `this.embeddings.forEach()`

## EmbeddingCluster.getCohesion()
- 位置: L1954-1978
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `cosSim()`
- 条件付き依存: `if (total > MAX_COHESION_ITEMS)` → `embeddings.push()`
- 条件付き依存: `if (total > MAX_COHESION_ITEMS)` → `Math.floor()`

## EmbeddingCluster.numItems()
- 位置: L1985-1987
- 役割: (未記入)
- 触るとき: (未記入)

## ClusterRepresentation.constructor()
- 位置: L1994-2005
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `genHexString()`, `isSearchTab()`, `super()`

## ClusterRepresentation.setSingleTabSearchLabel()
- 位置: L2013-2032
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `TITLE_DELIMETER_SET.has()`
- 条件付き依存: `if (TITLE_DELIMETER_SET.has(pageTitle[i]))` → `pageTitle.substring(0, i).trim()`
- 条件付き依存: `if (TITLE_DELIMETER_SET.has(pageTitle[i]))` → `pageTitle.substring()`
- 条件付き依存: `if (TITLE_DELIMETER_SET.has(pageTitle[i]))` → `topicString.replace()`
- 条件付き依存: `if (TITLE_DELIMETER_SET.has(pageTitle[i]))` → `t.toUpperCase()`

## ClusterRepresentation.getRepresentativeText()
- 位置: L2037-2042
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (!this.representativeText)` → `this._generateRepresentativeText()`

## ClusterRepresentation._generateRepresentativeText()
- 位置: L2051-2058
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.tabs.slice()`

## ClusterRepresentation.print()
- 位置: L2060-2062
- 役割: (未記入)
- 触るとき: (未記入)
