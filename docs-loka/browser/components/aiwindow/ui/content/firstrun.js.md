# browser/components/aiwindow/ui/content/firstrun.js

source: browser/components/aiwindow/ui/content/firstrun.js
source-hash: 5ee4e9ae1b01f4510a3507c980691f9e72e4888b
lines: 750

## <module>
- 役割: AI ウィンドウの初回起動ページで、AboutWelcome 形式のオンボーディング画面を組み立てて表示する
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `Services.prefs.getBoolPref()`, `Services.prefs.getIntPref()`

## isEuropePromotionRegion()
- 位置: L133-137
- 役割: Region.home か Region.current が EEA 加盟国なら真を返す
- 触るとき: Mistral の推奨表示をどの地域に出すかを変えるとき、テストで地域を切り替えて確認するとき
- 呼び出し先: `EEA_REGIONS.has()`
- 参照: `lazy.Region.current`, `lazy.Region.home`

## getPromotedChoiceId()
- 位置: L139-148
- 役割: Mistral 版リリースかつ EEA 地域のときだけ、ブランド名 Mistral のモデル ID を返す
- 触るとき: 推奨バッジを付けるモデルの決め方を変えるとき
- 呼び出し先: `getModelDisplayOrder()`, `getModelDisplayOrder().find()`, `isEuropePromotionRegion()`
- 参照: `(modelData[id] ?? {}).brandName`

## buildModelCards()
- 位置: L150-185
- 役割: モデルごとのカードを作り、推奨にバッジを付け、選ぶと browser.smartwindow.firstrun.modelChoice を設定する
- 触るとき: モデル選択カードの文言・アイコン・説明の出し方を変えるとき
- 呼び出し先: `getModelDisplayOrder()`, `getModelDisplayOrder().map()`
- 参照: `card.label.args`, `card.subtitle`, `cardContent.body`, `cardContent.icon`, `cardContent.label`

## getHiddenOnboardingScreenIds()
- 位置: L194-204
- 役割: Nimbus の hiddenOnboardingScreenIds からカンマ区切りの非表示画面 ID 集合を作る
- 触るとき: 実験で特定の案内画面を隠す仕組みを調べるとき、画面 ID を追加するとき
- 呼び出し先: `id.trim()`, `lazy.NimbusFeatures.smartWindow.getVariable()`, `value .split()`, `value .split(",") .map()`, `value .split(",") .map(id => id.trim()) .filter()`

## getScreens()
- 位置: L206-541
- 役割: イントロ、モデル選択、記憶設定、既定の設定の 4 画面の定義を返す(記憶と既定化はチェック項目を SET_PREF で保存)
- 触るとき: オンボーディングの文言・画面構成・チェック項目と保存先の pref を変えるとき
- 呼び出し先: `buildModelCards()`

## filterOnboardingScreens()
- 位置: L553-583
- 役割: 非表示指定の画面を除き、最後に残った画面の次へボタンを完了用の文言と完了 pref の設定に差し替える
- 触るとき: 画面を隠したときに完了ボタンが正しく動くかを確認するとき
- 呼び出し先: `NON_REMOVABLE_SCREEN_IDS.has()`, `allScreens.at()`, `allScreens.filter()`, `hiddenScreenIds.has()`, `screens.at()`
- 条件付き依存: `if ( lastVisible && lastVisible !== allScreens.at(-1) && lastVisible.content.additional_button )` → `Array.isArray()`
- 条件付き依存: `if ( lastVisible && lastVisible !== allScreens.at(-1) && lastVisible.content.additional_button )` → `actions.some()`
- 条件付き依存: `if ( Array.isArray(actions) && !actions.some( action => action.data?.pref?.name === FIRST_RUN_COMPLETE_PREF ) )` → `actions.push()`
- 参照: `action.data?.pref?.name`, `button.action?.data?.actions`, `button.label`, `lastVisible.content.additional_button`, `screen.id`

## createAIWindowConfig()
- 位置: L585-605
- 役割: 推奨モデルを既定値として保存し、非表示指定を反映した spotlight 形式のウィザード設定を作る
- 触るとき: ウィザード全体の設定(テンプレートや背景など)やモデルの既定値の決め方を変えるとき
- 呼び出し先: `filterOnboardingScreens()`, `getHiddenOnboardingScreenIds()`, `getPromotedChoiceId()`, `getScreens()`
- 条件付き依存: `if (promotedChoiceId)` → `Services.prefs.setStringPref()`
- 参照: `hiddenScreenIds.size`
- XPCOM: `Services.prefs`

## renderFirstRun()
- 位置: async L607-739
- 役割: モデル情報を読み込んで設定を作り、AW 用の関数を window に登録して aboutwelcome の bundle を読み込む
- 触るとき: 初回画面の起動順や、aboutwelcome 側に渡す関数を追加するとき
- 呼び出し先: `AWParent.didDestroy()`, `createAIWindowConfig()`, `document.body.appendChild()`, `document.createElement()`, `getAllModelsData()`, `window.addEventListener()`
- 参照: `lazy.AboutWelcomeParent`, `script.src`, `window.AWEvaluateScreenTargeting`, `window.AWFinish`, `window.AWGetFeatureConfig`, `window.AWGetInstalledAddons`, `window.AWGetSelectedTheme`, `window.AWSendEventTelemetry`, `window.AWSendToParent`

## receive()
- 位置: L613-618
- 役割: 名前付きの AWPage メッセージを AboutWelcomeParent へ中継する関数を作る
- 触るとき: コンテンツ側からの通知がどう親に届くかを追うとき
- 呼び出し先: `AWParent.onContentMessage()`
- 参照: `topChromeWindow.gBrowser.selectedBrowser`

## window.AWGetFeatureConfig()
- 位置: L620-620
- 役割: 作成済みのウィザード設定をそのまま返す
- 触るとき: 画面設定の受け渡しを調べるとき

## window.AWEvaluateScreenTargeting()
- 位置: L621-621
- 役割: ターゲティング評価を行わず、渡された画面をそのまま返す
- 触るとき: 画面の出し分けを将来ターゲティングで行うときの起点を探すとき

## window.AWGetSelectedTheme()
- 位置: L622-622
- 役割: テーマ選択は空のオブジェクトを返す(テーマ指定なし)
- 触るとき: テーマの扱いを追加するとき

## window.AWGetInstalledAddons()
- 位置: L623-623
- 役割: インストール済みアドオンとして空配列を返す
- 触るとき: アドオン情報を画面に出すよう変えるとき

## window.AWSendToParent()
- 位置: L624-624
- 役割: 名前と data を受けて receive 経由で親に送る
- 触るとき: コンテンツからのアクション(画面遷移など)が親に届かない問題を調べるとき
- 呼び出し先: `receive()`, `receive(name)()`

## window.AWSendEventTelemetry()
- 位置: L626-690
- 役割: IMPRESSION とボタン操作、チェック項目の選択を Glean の onboarding 系指標に記録する
- 触るとき: オンボーディングの計測項目を追加・修正するとき、指標が記録されない原因を調べるとき
- 呼び出し先: `Array.isArray()`, `Glean.smartWindow.onboardingScreenImpression.record()`, `["model_1", "model_2", "model_3"].includes()`, `message_id.includes()`
- 条件付き依存: `if (["model_1", "model_2", "model_3"].includes(source))` → `Glean.smartWindow.onboardingModelSelected.record()`
- 条件付き依存: `if (["model_1", "model_2", "model_3"].includes(source))` → `source.split()`
- 条件付き依存: `if (!(["model_1", "model_2", "model_3"].includes(source)))` → `message_id.includes()`
- 条件付き依存: `if ( source === "primary_button" && message_id.includes("AI_WINDOW_CHOOSE_MODEL") )` → `Services.prefs.getStringPref()`
- 条件付き依存: `if ( source === "primary_button" && message_id.includes("AI_WINDOW_CHOOSE_MODEL") )` → `Glean.smartWindow.onboardingModelNavigate.record()`
- 条件付き依存: `if (!( source === "primary_button" && message_id.includes("AI_WINDOW_CHOOSE_MODEL") ))` → `message_id.includes()`
- 条件付き依存: `if ( source === "primary_button" && (message_id.includes("AI_WINDOW_MEMORIES") || message_id.includes("AI_WINDOW_SET_DEFAULT")) )` → `Glean.smartWindow.onboardingBackNavigate.record()`
- 条件付き依存: `if ( message_id.includes("AI_WINDOW_MEMORIES") && Array.isArray(source) )` → `Glean.smartWindow.onboardingMemoriesSettings.record()`
- 条件付き依存: `if ( message_id.includes("AI_WINDOW_MEMORIES") && Array.isArray(source) )` → `source.join()`
- 条件付き依存: `if ( message_id.includes("AI_WINDOW_MEMORIES") && Array.isArray(source) )` → `Glean.smartWindow.onboardingMemoriesNavigate.record()`
- 条件付き依存: `if (!( message_id.includes("AI_WINDOW_MEMORIES") && Array.isArray(source) ))` → `message_id.includes()`
- 条件付き依存: `if (!( message_id.includes("AI_WINDOW_MEMORIES") && Array.isArray(source) ))` → `Array.isArray()`
- 条件付き依存: `if ( message_id.includes("AI_WINDOW_SET_DEFAULT") && Array.isArray(source) )` → `Glean.smartWindow.onboardingSetdefaultSettings.record()`
- 条件付き依存: `if ( message_id.includes("AI_WINDOW_SET_DEFAULT") && Array.isArray(source) )` → `source.join()`
- 条件付き依存: `if ( message_id.includes("AI_WINDOW_SET_DEFAULT") && Array.isArray(source) )` → `Glean.smartWindow.onboardingSetdefaultNavigate.record()`
- XPCOM: `Services.prefs`

## window.AWFinish()
- 位置: L692-726
- 役割: 説明ページを新しいタブで開き、チェック状態を pref から読んで onboardingComplete を記録し、新規タブ URL へ移動する
- 触るとき: 完了時の遷移先や完了計測の中身を変えるとき
- 呼び出し先: `Glean.smartWindow.onboardingComplete.record()`, `Services.prefs.getBoolPref()`, `Services.prefs.getStringPref()`, `memories.join()`, `window.AWSendToParent()`
- 条件付き依存: `if (Services.prefs.getBoolPref(MEMORIES_FROM_CONVERSATION_PREF, false))` → `memories.push()`
- 条件付き依存: `if (Services.prefs.getBoolPref(MEMORIES_FROM_HISTORY_PREF, false))` → `memories.push()`
- 参照: `lazy.AIWindow.newTabURL`, `window.location.href`
- XPCOM: `Services.prefs`
