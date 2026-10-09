# browser/components/tabbrowser/SmartTabGrouping.sys.mjs

source: browser/components/tabbrowser/SmartTabGrouping.sys.mjs
source-hash: c9964090c0be60ae084494a6125cc72878a606b4
lines: 2064

## <module>
- 役割: タブのタイトル埋め込みで類似タブの提案・クラスタリング・グループ名生成を行う Smart Tab Grouping の管理クラス、結果クラス、設定定数をまとめる。
- 呼び出し先: `XPCOMUtils.declareLazy()`

## getBestAnchorClusterInfo()
- 位置: L197-208
- 役割: クラスタ群のうち基準(既存グループ)のタブを最も多く含むものの番号と、その含有数を返す。
- 触るとき: 既存グループを軸にクラスタリングする際の基準クラスタの選び方を調べるとき。
- 呼び出し先: `Math.max()`, `anchorItemSet.has()`, `g.reduce()`, `groupIndices.map()`, `numItemsList.indexOf()`

## isSearchTab()
- 位置: L218-238
- 役割: タブが検索 UI 由来の検索結果ページで、検索語以外の URL 部分が元のままかを判定する。
- 触るとき: 検索ページ1枚だけのグループ名を、タイトルから決める特例の条件を調べるとき。
- 呼び出し先: `curURL.substring()`, `linkedBrowser.getAttribute()`, `searchURL.indexOf()`, `searchURL.substring()`

## SmartTabGroupingManager.constructor()
- 位置: L246-257
- 役割: 設定を複製または受け取り、設定の pref があればクラスタリング手法と凝集型の閾値を上書きする。
- 触るとき: pref や Nimbus によるクラスタリング設定の上書きを調べるとき。
- 呼び出し先: `structuredClone()`, `super()`

## SmartTabGroupingManager.id()
- 位置: L264-266
- 役割: この機能の識別子 smart-tab-grouping を返す静的ゲッター。
- 触るとき: AI 機能として登録される ID を参照・変更するとき。

## SmartTabGroupingManager.hasDistinctEnabledState()
- 位置: L274-279
- 役割: 常に true を返し、利用可能とは別に手動の有効化操作が要る機能だと示す。
- 触るとき: AI 設定画面で本機能の有効状態の扱いを調べるとき。

## SmartTabGroupingManager.canRunOnDevice()
- 位置: L286-289
- 役割: ハードウェア制約が無いとして常に true を返す。
- 触るとき: 端末条件による機能の可否判定を足したいとき。

## SmartTabGroupingManager.enable()
- 位置: async L296-300
- 役割: enabled、userEnabled、optin の3つの pref を true にして機能を有効にする。
- 触るとき: 有効化時に変わる pref の組み合わせを調べるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`
- XPCOM: `Services.prefs`

## SmartTabGroupingManager.block()
- 位置: async L307-317
- 役割: 3つの pref を false にし、関連モデルを削除して機能を無効化する。
- 触るとき: 機能をブロックしたときの pref 更新とモデル削除の流れを調べるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`, `SmartTabGroupingManager.deleteSmartTabModels()`
- XPCOM: `Services.prefs`

## SmartTabGroupingManager.isEnabled()
- 位置: L324-334
- 役割: 機械学習全体の有効設定と本機能の3つの pref がすべて true のときだけ true を返す。
- 触るとき: 機能が有効と判定される条件、またはUIが出ない原因を調べるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## SmartTabGroupingManager.isAllowed()
- 位置: L341-343
- 役割: アプリのロケールが英語(en)で始まる場合に true を返す。
- 触るとき: 対応言語の範囲を広げる、または非英語で出ない理由を調べるとき。
- 呼び出し先: `Services.locale.appLocaleAsBCP47.startsWith()`
- XPCOM: `Services.locale`

## SmartTabGroupingManager.makeAvailable()
- 位置: async L350-359
- 役割: enabled と userEnabled を true、optin を false にして利用可能状態へ戻し、ローカルモデルを削除する。
- 触るとき: ブロックから利用可能へ戻す際の pref とモデル削除の挙動を調べるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`, `SmartTabGroupingManager.deleteSmartTabModels()`
- XPCOM: `Services.prefs`

## SmartTabGroupingManager.isBlocked()
- 位置: L366-371
- 役割: enabled または userEnabled のどちらかが false なら true を返す。
- 触るとき: ブロック状態の判定条件を調べるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`

## SmartTabGroupingManager.isManagedByPolicy()
- 位置: L378-380
- 役割: userEnabled の pref がロックされているかで、企業ポリシー管理下かを返す。
- 触るとき: ポリシーで固定された場合のUI表示や挙動を調べるとき。
- 呼び出し先: `Services.prefs.prefIsLocked()`
- XPCOM: `Services.prefs`

## SmartTabGroupingManager.deleteSmartTabModels()
- 位置: async L387-397
- 役割: 本機能専用のトピック生成モデルだけを ML アンインストール機能で削除する(共有の埋め込みモデルは残す)。
- 触るとき: 無効化時に削除されるモデルの範囲を変える・調べるとき。
- 呼び出し先: `lazy.MLUninstallService.uninstall()`

## SmartTabGroupingManager.isEngineClosed()
- 位置: L404-406
- 役割: エンジンが未初期化または状態が closed なら true を返す。
- 触るとき: エンジンの再作成が必要になる判定を調べるとき。

## SmartTabGroupingManager.getEmbeddingsGenerator()
- 位置: L413-418
- 役割: 共有の埋め込み生成器を初回に作って保持し、以後は同じものを返す。
- 触るとき: 埋め込みモデルの取得元や生成器の使い回しを調べるとき。
- 条件付き依存: `if (!this.embeddingsGenerator)` → `embeddingsGeneratorFactory.forGeneral()`

## SmartTabGroupingManager.initEmbeddingEngine()
- 位置: async L423-429
- 役割: 埋め込みエンジンを用意しダミー文で試し実行して初回遅延を減らす。失敗は握りつぶす。
- 触るとき: 初回提案が遅い問題やウォームアップ処理を調べるとき。
- 呼び出し先: `this.getEmbeddingsGenerator()`, `this.getEmbeddingsGenerator().embedMany()`, `this.getEmbeddingsGenerator().ensureEngine()`

## SmartTabGroupingManager.getTabsToProcess()
- 位置: L441-489
- 役割: 固定タブと URL 無しを除き、グループ内の先頭3枚の後に他のタブを足して最大300枚の処理対象を作る。
- 触るとき: 提案の対象にするタブの選別や上限を変えるとき。
- 呼び出し先: `seen.has()`, `shouldInclude()`, `tabsToProcess.slice()`
- 条件付き依存: `if (!seen.has(tab))` → `seen.add()`
- 条件付き依存: `if (!seen.has(tab))` → `tabsToProcess.push()`

## shouldInclude()
- 位置: L449-457
- 役割: ピン留めタブや現在の URL が取れないタブを除外し、それ以外を処理対象とする判定を返す。
- 触るとき: 処理対象から外すタブの条件を調べるとき。

## SmartTabGroupingManager.smartTabGroupingForGroup()
- 位置: async L498-558
- 役割: グループに追加すべきタブを、pref で選ばれた手法(k-means、最近傍、ロジスティック回帰)で探し最大10件返す。
- 触るとき: 他のタブを提案する機能の手法切り替えや件数を変える・調べるとき。
- 呼び出し先: `allTabs .map()`, `allTabs .map((t, i) => (t.group ? i : -1)) .filter()`, `c.tabs.includes()`, `clusters.clusterRepresentations.find()`, `groupTabs.includes()`, `groupTabs.some()`, `suggestedTabs.slice()`, `this.findNearestNeighbors()`, `this.findSimilarTabsLogisticRegression()`, `this.generateClusters()`, `this.generateClusters( allTabs, null, null, null, groupIndices, alreadyGroupedIndices ).then()`, `this.getTabsToProcess()`
- 条件付き依存: `if (groupTabs.includes(allTabs[i]))` → `groupIndices.push()`
- 条件付き依存: `if (targetCluster)` → `targetCluster.tabs.filter()`

## SmartTabGroupingManager.getTabsToSuggest()
- 位置: L568-584
- 役割: グループ済み、他グループ所属、除外対象 URL のタブを除いた提案候補の添字を返す。
- 触るとき: 提案から除外される URL や条件を変えるとき。
- 呼び出し先: `TAB_URLS_TO_EXCLUDE.includes()`, `allTabs .map()`, `allTabs .map((_, index) => index) .filter()`, `allTabs .map((at, index) => (TAB_URLS_TO_EXCLUDE.includes(at.url) ? index : -1)) .filter()`, `excludedTabIndices.includes()`

## SmartTabGroupingManager.findNearestNeighbors()
- 位置: async L596-669
- 役割: グループ内タブとの最大コサイン類似度が閾値を超えた候補を、類似度順に返す。
- 触るとき: 最近傍方式の閾値や、グループ名を埋め込みに加える挙動を調べるとき。再帰の条件(要確認)。
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
- 役割: 各候補埋め込みについて、基準埋め込みとのコサイン類似度の平均を返す。
- 触るとき: ロジスティック回帰でグループ名との類似度を出す部分を調べるとき。
- 呼び出し先: `averageSimilarities.push()`, `cosSim()`

## SmartTabGroupingManager.getMaxSimilarity()
- 位置: L696-709
- 役割: 各候補埋め込みについて、基準埋め込みとのコサイン類似度の最大値を返す。
- 触るとき: ロジスティック回帰のタイトル類似度特徴の計算を調べるとき。
- 呼び出し先: `cosSim()`, `maxSimilarities.push()`

## SmartTabGroupingManager.getBaseDomain()
- 位置: L717-748
- 役割: URL から www を除いた基準ドメインを取り出し、失敗時は空文字またはホスト名を返す。
- 触るとき: ドメイン一致の判定がずれる、localhost や IP の扱いを調べるとき。
- 呼び出し先: `Services.eTLD .getBaseDomain()`, `Services.eTLD .getBaseDomain(Services.io.newURI(url.toLowerCase()), 1) .replace()`, `Services.io.newURI()`, `hostname.toLowerCase()`, `url.toLowerCase()`
- XPCOM: `Services.eTLD` / `Services.io`

## SmartTabGroupingManager.getDomainMatchFractions()
- 位置: L758-777
- 役割: 各候補について、基準タブのうち同じ基準ドメインを持つものの割合を返す。
- 触るとき: ドメイン類似度の特徴量の計算を調べるとき。
- 呼び出し先: `SmartTabGroupingManager.getBaseDomain()`, `anchorTabsPrep.map()`, `candidateTabsPrep.map()`

## SmartTabGroupingManager.sigmoid()
- 位置: L785-787
- 役割: 入力にシグモイド関数を適用して確率値にする。
- 触るとき: ロジスティック回帰の出力計算を確認するとき。
- 呼び出し先: `Math.exp()`

## SmartTabGroupingManager.calculateProbability()
- 位置: L798-813
- 役割: グループ名・タイトル・ドメインの類似度に重みと切片を掛けて足し、シグモイドで確率にする。
- 触るとき: ロジスティック回帰の式や重みの使い方を調べるとき。
- 呼び出し先: `this.sigmoid()`

## SmartTabGroupingManager.calculateAllProbabilities()
- 位置: L823-851
- 役割: コサイン類似度を0から1へ変換し、グループ名の有無で重みを選んで全候補の確率を計算する。
- 触るとき: 重みセットの切り替えや類似度の正規化を調べるとき。
- 呼び出し先: `Array.isArray()`, `probabilities.push()`, `this.calculateProbability()`

## SmartTabGroupingManager.findSimilarTabsLogisticRegression()
- 位置: async L861-936
- 役割: タイトル・グループ名・ドメインの類似度から候補の確率を出し、閾値以上を確率の高い順に返す。
- 触るとき: ロジスティック回帰方式の提案精度や閾値を調整するとき。
- 呼び出し先: `SmartTabGroupingManager.preprocessText()`, `anchorTabsPrep .concat()`, `anchorTabsPrep .concat(candidateTabsPrep) .map()`, `candidateIndices.map()`, `candidateTabsData // combine candidate tabs with corresponding probabilities .map()`, `groupedIndices .map()`, `groupedIndices .map(gi => tabData[gi]) .slice()`, `this._generateEmbeddings()`, `this._prepareTabData()`, `this.calculateAllProbabilities()`, `this.getDomainMatchFractions()`, `this.getMaxSimilarity()`, `this.getTabsToSuggest()`, `titleEmbeddings.slice()`
- 条件付き依存: `if (groupLabel)` → `this._generateEmbeddings()`
- 条件付き依存: `if (groupLabel)` → `this.getAverageSimilarity()`
- 条件付き依存: `if (groupLabel)` → `titleEmbeddings.slice()`

## SmartTabGroupingManager.terminateProcess()
- 位置: L942-945
- 役割: 進行中の処理を止める予定だが、現状は実装が無く何もしない(TODO)。
- 触るとき: パネルを閉じたときの処理中断を実装するとき。

## SmartTabGroupingManager.setClusteringMethod()
- 位置: L952-957
- 役割: クラスタリング手法を設定し、未対応の名前なら例外を投げる。
- 触るとき: テストや実験で手法を切り替える方法を調べるとき。

## SmartTabGroupingManager.setAnchorMethod()
- 位置: L964-969
- 役割: 既存グループを軸にする方式(DRIFT か FIXED)を設定し、未対応なら例外を投げる。
- 触るとき: 基準クラスタの扱い方を切り替えるとき。

## SmartTabGroupingManager.setSilBoost()
- 位置: L971-973
- 役割: グループ済みクラスタのシルエット係数に掛ける重みを設定に保存する。
- 触るとき: k-means の評価での基準クラスタの重みを調整するとき。

## SmartTabGroupingManager.setDimensionReductionMethod()
- 位置: L980-985
- 役割: 埋め込みの次元削減手法を設定し、未対応の名前なら例外を投げる(現状は対応手法が無い)。
- 触るとき: 次元削減を導入するとき。

## SmartTabGroupingManager.setDataTitleKey()
- 位置: L993-995
- 役割: 埋め込みやクラスタリングで使うタイトルのキー名を設定する。
- 触るとき: タブ以外のテストデータを使って評価するとき。

## SmartTabGroupingManager.log()
- 位置: L1003-1003
- 役割: ログ出力用だが本体は空で何もしない。
- 触るとき: デバッグログを出せるようにしたいとき。

## SmartTabGroupingManager._prepareTabData()
- 位置: async L1013-1036
- 役割: タブ一覧から埋め込み用テキスト(タイトル、任意で説明)、タイトル、説明、URL を持つ配列を作る。
- 触るとき: 埋め込みに渡すテキストの組み立てや URL の取得元を変えるとき。
- 呼び出し先: `structuredData.push()`

## SmartTabGroupingManager.getUpdatedInitData()
- 位置: L1045-1054
- 役割: トピック生成の場合に限り、pref で指定されたモデルのリビジョンを初期化データに入れて返す。
- 触るとき: モデルのリビジョンを pref や Nimbus で固定する挙動を調べるとき。

## SmartTabGroupingManager._createMLEngine()
- 位置: async L1063-1094
- 役割: 設定から初期化データを作って ML エンジンを生成し、実際に使われたバックエンドを記録して返す。
- 触るとき: エンジン生成時のパラメータやバックエンド記録を調べるとき。
- 呼び出し先: `SmartTabGroupingManager.getUpdatedInitData()`, `createEngine()`

## SmartTabGroupingManager._generateEmbeddings()
- 位置: async L1103-1109
- 役割: 文字列の一覧を共有の埋め込み生成器でベクトル化して返す(空なら空配列)。
- 触るとき: 埋め込みの生成経路を調べるとき。
- 呼び出し先: `this.getEmbeddingsGenerator()`, `this.getEmbeddingsGenerator().embedMany()`

## SmartTabGroupingManager._clusterEmbeddings()
- 位置: L1122-1241
- 役割: k-means で複数の k と試行を比べ、シルエット係数が最良の結果を選び、基準タブを考慮して返す。
- 触るとき: k-means 方式の k の探索、基準タブの扱い、評価の重みを調べるとき。
- 呼び出し先: `Error()`, `kmeansPlusPlus()`, `silScores.reduce()`, `silhouetteCoefficients()`, `tempResult.getCentroidInertia()`
- 条件付き依存: `if (!k)` → `Math.min()`
- 条件付き依存: `if (!k)` → `Math.floor()`
- 条件付き依存: `if (!k)` → `Math.log()`
- 条件付き依存: `if (anchorIndices && !freezeAnchorsInZeroCluster)` → `getBestAnchorClusterInfo()`
- 条件付き依存: `if (anchorIndices)` → `result.setAnchorClusterIndex()`
- 条件付き依存: `if (!freezeAnchorsInZeroCluster)` → `result.adjustClusterForAnchors()`

## SmartTabGroupingManager.getPredictedLabelForGroup()
- 位置: async L1250-1263
- 役割: グループのタブと他のタブから静的クラスタを作り、モデルでグループ名を予測して返す(失敗時は空文字)。
- 触るとき: グループ名の提案が空になる、またはエラー時の理由コードを調べるとき。
- 呼び出し先: `this.createStaticCluster()`, `this.generateGroupLabels()`

## SmartTabGroupingManager._clusterEmbeddingsHAC()
- 位置: L1274-1285
- 役割: 凝集型(平均連結、コサイン)クラスタリングを閾値で実行し、結果オブジェクトにして返す。
- 触るとき: 凝集型クラスタリングの閾値や挙動を調べるとき。
- 呼び出し先: `agglomerativeClusterCosine()`

## SmartTabGroupingManager.generateClusters()
- 位置: async L1298-1351
- 役割: タブの埋め込みを用意し、設定された手法でクラスタリングして、各クラスタに凝集度を付けて返す。
- 触るとき: 自動グループ分けの全体の流れや手法の選択を調べるとき。
- 呼び出し先: `bestResultCluster?.clusterRepresentations.forEach()`, `curResult.getCentroidInertia()`, `rep.getCohesion()`, `this._clusterEmbeddings()`, `this._clusterEmbeddingsHAC()`, `this._prepareTabData()`
- 条件付き依存: `if (!(precomputedEmbeddings))` → `this._generateEmbeddings()`
- 条件付き依存: `if (!(precomputedEmbeddings))` → `structuredData.map()`
- 条件付き依存: `if (!(precomputedEmbeddings))` → `SmartTabGroupingManager.preprocessText()`

## SmartTabGroupingManager.createStaticCluster()
- 位置: L1359-1369
- 役割: 与えられたタブ全部を1つのクラスタとする結果を作る(タブが無ければ null)。
- 触るとき: グループ名生成の入力となる単一クラスタの作り方を調べるとき。
- 呼び出し先: `Array.from()`

## SmartTabGroupingManager.preloadAllModels()
- 位置: async L1378-1429
- 役割: トピック生成エンジンの作成と埋め込みエンジンの準備を並行して行い、ダウンロード進捗を間引いて通知する。
- 触るとき: モデルの事前ダウンロードと進捗表示の挙動を調べるとき。
- 呼び出し先: `Promise.all()`, `mutliProgressAggregator?.aggregateCallback.bind()`, `this._createMLEngine()`, `this.initEmbeddingEngine()`

## progressCallback()
- 位置: L1389-1411
- 役割: ダウンロードの進捗を補正し、変化が閾値を超えたときだけ呼び出し元へ割合を通知する。
- 触るとき: 進捗表示が飛ぶ、または更新頻度を変えたいとき。
- 呼び出し先: `Math.abs()`
- 条件付き依存: `if ( Math.abs(previousProgress - progress) > UPDATE_THRESHOLD_PERCENTAGE )` → `progressCallback()`

## SmartTabGroupingManager.createModelInput()
- 位置: L1437-1442
- 役割: キーワードとタイトル群から、トピック生成モデルへ渡す入力文字列を組み立てる。
- 触るとき: トピック生成モデルへのプロンプト形式を変えるとき。
- 呼び出し先: `documents.join()`, `keywords.join()`
- 条件付き依存: `if (!keywords || keywords.length === 0)` → `documents.join()`

## SmartTabGroupingManager.cutAtDuplicateWords()
- 位置: L1452-1473
- 役割: 句の中で語が重複(単純な複数形の s を除く)した位置で句を切り詰める。
- 触るとき: 生成されたグループ名に同じ語が繰り返される問題を調べるとき。
- 呼び出し先: `phrase.split()`, `wordList[i].toLowerCase()`, `wordsSet.add()`, `wordsSet.has()`
- 条件付き依存: `if (baseWord.length > 3)` → `baseWord.slice()`
- 条件付き依存: `if (baseWord.slice(-1) === "s")` → `baseWord.slice()`
- 条件付き依存: `if (wordsSet.has(baseWord))` → `wordList.slice(0, i).join()`
- 条件付き依存: `if (wordsSet.has(baseWord))` → `wordList.slice()`

## SmartTabGroupingManager.preprocessText()
- 位置: L1482-1510
- 役割: タイトル末尾の「- サイト名」「| ニュース」などの短い区切り以降を、残りが十分あれば取り除く。
- 触るとき: タイトルからサイト名が混ざって類似度に影響する問題を調べるとき。
- 呼び出し先: `splitText.slice()`, `splitText.slice(0, -1).join()`, `text.split()`
- 条件付き依存: `if (hasEnoughInfo && isPotentialDomainInfo)` → `splitText .slice(0, -1) // everything except the last element .map(t => t.trim()) .filter()`
- 条件付き依存: `if (hasEnoughInfo && isPotentialDomainInfo)` → `splitText .slice(0, -1) // everything except the last element .map()`
- 条件付き依存: `if (hasEnoughInfo && isPotentialDomainInfo)` → `splitText .slice()`
- 条件付き依存: `if (hasEnoughInfo && isPotentialDomainInfo)` → `t.trim()`

## SmartTabGroupingManager.processTopicModelResult()
- 位置: L1517-1527
- 役割: モデルの生成文を整え、空や除外ラベルは理由を記録し、重複語を切って返す。
- 触るとき: 生成ラベルの後処理や除外ラベルの扱いを変えるとき。
- 呼び出し先: `(topic || "").trim()`, `LABELS_TO_EXCLUDE.includes()`, `SmartTabGroupingManager.cutAtDuplicateWords()`, `basicResult.toLowerCase()`

## SmartTabGroupingManager.generateGroupLabels()
- 位置: async L1539-1589
- 役割: 検索ページ特例を試し、代表文書とキーワードからトピック生成モデルを実行して各クラスタに予測ラベルを付ける。
- 触るとき: グループ名の自動生成の流れ、入力、モデル実行を調べるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`, `SmartTabGroupingManager.isEngineClosed()`, `genLabelResults.forEach()`, `groupingResult.getRepresentativeDocsAndKeywords()`, `otherGroupingResult.getRepresentativeDocuments()`, `this.createModelInput()`, `this.processTopicModelResult()`, `this.topicEngine.run()`
- 条件付き依存: `if ( searchTopicSpecialCase && groupingResult.clusterRepresentations.length == 1 && groupingResult.clusterRepresentations[0].isSingleTabSearch )` → `groupingResult.clusterRepresentations[0].setSingleTabSearchLabel()`
- 条件付き依存: `if (SmartTabGroupingManager.isEngineClosed(this.topicEngine))` → `this._createMLEngine()`
- XPCOM: `Services.prefs`

## SmartTabGroupingManager.getLabelReason()
- 位置: L1591-1593
- 役割: 直近のラベル生成の理由コードを返し、無ければ DEFAULT を返す。
- 触るとき: ラベルが空になった理由をテレメトリで見るとき。

## SmartTabGroupingManager.handleLabelTelemetry()
- 位置: async L1605-1630
- 役割: ラベル提案の保存・キャンセル時に、ラベル長や編集距離などを Glean に記録して理由コードをリセットする。
- 触るとき: グループ名提案のテレメトリ項目を変える・調べるとき。
- 呼び出し先: `Glean.tabgroup.smartTabTopic.record()`, `lazy.NLP.levenshtein()`, `this.getEngineConfigs()`, `this.getLabelReason()`

## SmartTabGroupingManager.handleSuggestTelemetry()
- 位置: async L1644-1666
- 役割: 他タブ提案の保存・キャンセル時に、提案数や承認数などを Glean に記録する。
- 触るとき: タブ提案のテレメトリ項目を変える・調べるとき。
- 呼び出し先: `Glean.tabgroup.smartTabSuggest.record()`, `this.getEmbeddingsGenerator()`, `this.getEngineConfigs()`

## SmartTabGroupingManager.getEngineConfigs()
- 位置: async L1673-1689
- 役割: トピック生成と埋め込みの推論設定を取得して保持し、タスク名をキーにした形で返す。
- 触るとき: テレメトリに載るモデルのリビジョンの取得元を調べるとき。
- 条件付き依存: `if (!this.topicEngineConfig)` → `lazy.MLEngineParent.getInferenceOptions()`
- 条件付き依存: `if (!this.embeddingEngineConfig)` → `this.getEmbeddingsGenerator()`
- 条件付き依存: `if (!this.embeddingEngineConfig)` → `lazy.MLEngineParent.getInferenceOptions()`

## SmartTabGroupingResult.constructor()
- 位置: L1704-1710
- 役割: 添字、タブ、埋め込み、設定を保持し、空のクラスタを除いてクラスタ表現を作る。
- 触るとき: クラスタリング結果オブジェクトの構造を調べるとき。
- 呼び出し先: `indices.filter()`, `this._buildClusterRepresentations()`

## SmartTabGroupingResult._buildClusterRepresentations()
- 位置: L1715-1728
- 役割: 添字ごとにタブと埋め込みを抜き出して ClusterRepresentation の一覧を作る。
- 触るとき: クラスタ表現が再構築されるタイミングを調べるとき。
- 呼び出し先: `subClusterIndices.map()`, `this.indices.map()`

## SmartTabGroupingResult.getRepresentativeDocuments()
- 位置: L1736-1744
- 役割: タブのタイトルを代表文書として最大10件返す(初回に計算して保持)。
- 触るとき: ラベル生成に渡すタイトルの数や選び方を変えるとき。
- 呼び出し先: `this.documents.slice()`
- 条件付き依存: `if (!this.documents)` → `this.tabItems.map()`

## SmartTabGroupingResult.getRepresentativeDocsAndKeywords()
- 位置: L1753-1766
- 役割: 代表文書と、他の文書との比較で抽出したキーワードを返す(文書が1件ならキーワードは空)。
- 触るとき: ラベル生成に渡すキーワードの抽出方法を調べるとき。
- 呼び出し先: `this.getRepresentativeDocuments()`
- 条件付き依存: `if (!this.keywords)` → `this.documents.slice(0, 3).join()`
- 条件付き依存: `if (!this.keywords)` → `this.documents.slice()`
- 条件付き依存: `if (!this.keywords)` → `otherDocuments.join()`
- 条件付き依存: `if (this.documents.length > 1)` → `keywordExtractor.fitTransform()`

## SmartTabGroupingResult.setAnchorClusterIndex()
- 位置: L1768-1770
- 役割: 基準にしているクラスタの番号を保存する。
- 触るとき: 基準クラスタの管理方法を調べるとき。

## SmartTabGroupingResult.getAnchorCluster()
- 位置: L1777-1782
- 役割: 保存された番号の基準クラスタを返す(未設定なら null)。
- 触るとき: 提案結果から基準クラスタを取り出す呼び出しを調べるとき。

## SmartTabGroupingResult.adjustClusterForAnchors()
- 位置: L1788-1806
- 役割: 基準タブが他のクラスタにあれば基準クラスタへ移し、クラスタ表現を作り直す。
- 触るとき: 基準タブが別グループに分かれてしまう問題を調べるとき。
- 呼び出し先: `anchorSet.has()`, `this._buildClusterRepresentations()`, `this.indices[i].filter()`
- 条件付き依存: `if (anchorSet.has(item))` → `this.indices[this.#anchorClusterIndex].push()`

## SmartTabGroupingResult.printClusters()
- 位置: L1811-1815
- 役割: 各クラスタ表現の print を呼ぶ(print の中身は空)。
- 触るとき: デバッグ出力を整備するとき。
- 呼び出し先: `cluster.print()`

## SmartTabGroupingResult.getCentroidInertia()
- 位置: L1822-1828
- 役割: 全クラスタの重心からの二乗距離の合計(慣性)を返す。
- 触るとき: クラスタリング結果の良し悪しを比べる指標を調べるとき。
- 呼び出し先: `rep.computeTotalSquaredCentroidDistance()`, `this.clusterRepresentations.forEach()`

## SmartTabGroupingResult._flatMapItemsInClusters()
- 位置: L1836-1846
- 役割: 全クラスタのタブを1つの配列に平坦化し、各要素に所属クラスタの ID を付ける。
- 触るとき: 評価用の正解ラベルとの比較データを作る処理を調べるとき。
- 呼び出し先: `Object.assign()`, `clusterRep.tabs.map()`, `result.concat()`, `this.clusterRepresentations.reduce()`

## SmartTabGroupingResult.getRandScore()
- 位置: L1855-1858
- 役割: 正解ラベル付きデータに対するクラスタリングの Rand スコアを返す。
- 触るとき: クラスタリング精度を評価するとき。
- 呼び出し先: `computeRandScore()`, `this._flatMapItemsInClusters()`

## SmartTabGroupingResult.getAccuracyStatsForCluster()
- 位置: L1867-1901
- 役割: 指定ラベルのクラスタについて真陽性などを数え、精度指標を返す。
- 触るとき: 特定グループの精度を評価するとき。
- 呼び出し先: `combinedItems.find()`, `combinedItems.forEach()`, `getAccuracyStats()`, `this._flatMapItemsInClusters()`

## genHexString()
- 位置: L1910-1917
- 役割: 指定長のランダムな16進文字列を作る。
- 触るとき: クラスタ ID の生成方法を調べるとき。
- 呼び出し先: `Math.floor()`, `Math.random()`, `hex.charAt()`

## EmbeddingCluster.constructor()
- 位置: L1920-1925
- 役割: タブと埋め込みを保持し、重心が無ければ埋め込みから計算する。
- 触るとき: クラスタの重心の求め方を調べるとき。
- 呼び出し先: `computeCentroidFrom2DArray()`

## EmbeddingCluster.computeTotalSquaredCentroidDistance()
- 位置: L1930-1939
- 役割: 各埋め込みと重心の二乗ユークリッド距離を合計して返す(空なら0)。
- 触るとき: 慣性の計算を調べるとき。
- 呼び出し先: `euclideanDistance()`, `this.embeddings.forEach()`

## EmbeddingCluster.getCohesion()
- 位置: L1954-1978
- 役割: クラスタ内の埋め込みの平均ペア間コサイン類似度を返し、20件超は等間隔に間引いて計算する。
- 触るとき: グループの信頼度スコアや計算量の上限を調べるとき。
- 呼び出し先: `cosSim()`
- 条件付き依存: `if (total > MAX_COHESION_ITEMS)` → `embeddings.push()`
- 条件付き依存: `if (total > MAX_COHESION_ITEMS)` → `Math.floor()`

## EmbeddingCluster.numItems()
- 位置: L1985-1987
- 役割: クラスタ内のタブ数を返す。
- 触るとき: クラスタの大きさを参照する箇所を調べるとき。

## ClusterRepresentation.constructor()
- 位置: L1994-2005
- 役割: クラスタに各種ラベル欄、ID、1枚だけの検索ページかどうかのフラグを持たせて初期化する。
- 触るとき: クラスタ表現が持つ項目や ID の付与を調べるとき。
- 呼び出し先: `genHexString()`, `isSearchTab()`, `super()`

## ClusterRepresentation.setSingleTabSearchLabel()
- 位置: L2013-2032
- 役割: 検索ページ1枚のクラスタで、タイトル末尾の区切りより前を先頭大文字にしてラベルにする(長すぎると失敗)。
- 触るとき: 検索ページだけのグループ名の特例を調整するとき。
- 呼び出し先: `TITLE_DELIMETER_SET.has()`
- 条件付き依存: `if (TITLE_DELIMETER_SET.has(pageTitle[i]))` → `pageTitle.substring(0, i).trim()`
- 条件付き依存: `if (TITLE_DELIMETER_SET.has(pageTitle[i]))` → `pageTitle.substring()`
- 条件付き依存: `if (TITLE_DELIMETER_SET.has(pageTitle[i]))` → `topicString.replace()`
- 条件付き依存: `if (TITLE_DELIMETER_SET.has(pageTitle[i]))` → `t.toUpperCase()`

## ClusterRepresentation.getRepresentativeText()
- 位置: L2037-2042
- 役割: 代表テキストを未計算なら生成して返す。
- 触るとき: 代表テキストが使われる箇所を調べるとき。
- 条件付き依存: `if (!this.representativeText)` → `this._generateRepresentativeText()`

## ClusterRepresentation._generateRepresentativeText()
- 位置: L2051-2058
- 役割: 先頭3タブのタイトルを改行でつないだテキストを返す。
- 触るとき: 代表テキストの作り方を変えるとき。
- 呼び出し先: `this.tabs.slice()`

## ClusterRepresentation.print()
- 位置: L2060-2062
- 役割: デバッグ出力用だが本体は空で何もしない。
- 触るとき: クラスタのデバッグ出力を実装するとき。
