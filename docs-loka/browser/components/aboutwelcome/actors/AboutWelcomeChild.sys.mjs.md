# browser/components/aboutwelcome/actors/AboutWelcomeChild.sys.mjs

source: browser/components/aboutwelcome/actors/AboutWelcomeChild.sys.mjs
source-hash: e787093bcdf019811ccc00911f2af227bd492a2a
lines: 437

## <module>
- 役割: about:welcome のコンテンツ側(JSWindowActorChild)として、ページから呼ばれる関数を export し、親プロセスへの問い合わせを中継するアクター
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.defineLazyGetter()`, `ChromeUtils.importESModule()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## AboutWelcomeChild.didDestroy()
- 位置: L35-37
- 役割: 破棄フラグを立て、以降のウィンドウアクセスを防ぐ
- 触るとき: 破棄後に非同期処理がページへ書き込んで例外になる問題を調べるとき
- 参照: `this._destroyed`

## AboutWelcomeChild.actorCreated()
- 位置: L39-41
- 役割: アクター生成時に exportFunctions を呼び、ページ側から使える関数を登録する
- 触るとき: ページに公開する関数の登録タイミングを確認するとき
- 呼び出し先: `this.exportFunctions()`

## AboutWelcomeChild.sendToPage()
- 位置: L48-55
- 役割: AboutWelcomeChromeToContent の CustomEvent を、複製した action を detail に入れて発火する
- 触るとき: 親からページへ送るイベントの形式を変えるとき
- 呼び出し先: `Cu.cloneInto()`, `lazy.log.debug()`, `win.dispatchEvent()`
- 参照: `action.type`, `this.document.defaultView`, `win.CustomEvent`

## AboutWelcomeChild.exportFunctions()
- 位置: L60-160
- 役割: AW で始まる関数群などを Cu.exportFunction で content window に defineAs 付きで公開する
- 触るとき: ページから新しい関数を呼べるようにするとき。ここに載せ忘れるとページ側で undefined になる
- 呼び出し先: `Cu.exportFunction()`, `this.AWAddScreenImpression.bind()`, `this.AWEnsureAddonInstalled.bind()`, `this.AWEnsureLangPackInstalled.bind()`, `this.AWEvaluateAttributeTargeting.bind()`, `this.AWEvaluateScreenTargeting.bind()`, `this.AWFindBackupsInWellKnownLocations.bind()`, `this.AWFinish.bind()`, `this.AWGetFeatureConfig.bind()`, `this.AWGetFxAMetricsFlowURI.bind()`, `this.AWGetInstalledAddons.bind()`, `this.AWGetSelectedTheme.bind()`, `this.AWGetUnhandledCampaignAction.bind()`, `this.AWNegotiateLangPackForLanguageMismatch.bind()`, `this.AWNewScreen.bind()`, `this.AWSelectTheme.bind()`, `this.AWSendEventTelemetry.bind()`, `this.AWSendImpressionAction.bind()`, `this.AWSendToDeviceEmailsSupported.bind()`, `this.AWSendToParent.bind()`, `this.AWSetRequestedLocales.bind()`, `this.AWWaitForMigrationClose.bind()`, `this.AWWaitForNimbus.bind()`, `this.RPMGetFormatURLPref.bind()`
- 参照: `this.contentWindow`

## AboutWelcomeChild.wrapPromise()
- 位置: L165-169
- 役割: 親からの Promise を content window の Promise に包み直し、ページ側で Promise メソッドを使えるようにする
- 触るとき: ページに返す Promise の型の扱いで問題が出たとき
- 呼び出し先: `promise.then()`
- 参照: `this.contentWindow.Promise`

## AboutWelcomeChild.sendQueryAndCloneForContent()
- 位置: L174-183
- 役割: 親への sendQuery の結果を Cu.cloneInto で content へ複製して返す
- 触るとき: 親からの戻り値のオブジェクトをページで触れるようにするとき
- 呼び出し先: `(async () => { return Cu.cloneInto( await this.sendQuery(...sendQueryArgs), this.contentWindow ); })()`, `Cu.cloneInto()`, `this.sendQuery()`, `this.wrapPromise()`
- 参照: `this.contentWindow`

## AboutWelcomeChild.AWSelectTheme()
- 位置: L185-189
- 役割: テーマ名を大文字にして AWPage:SELECT_THEME を親に問い合わせる
- 触るとき: テーマ選択の値の形式を変えるとき。親側は大文字の名前で LIGHT_WEIGHT_THEMES を引く
- 呼び出し先: `data.toUpperCase()`, `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.AWEvaluateScreenTargeting()
- 位置: L191-196
- 役割: 画面のターゲティング評価を親に依頼し、結果を content へ複製して返す
- 触るとき: 画面の表示可否の判定を変えるとき
- 呼び出し先: `this.sendQueryAndCloneForContent()`

## AboutWelcomeChild.AWEvaluateAttributeTargeting()
- 位置: L198-202
- 役割: 属性ベースのターゲティング評価を親に依頼して返す
- 触るとき: 属性ターゲティングの入力を変えるとき
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.AWAddScreenImpression()
- 位置: L204-208
- 役割: 画面の表示記録を親に依頼する
- 触るとき: 画面の表示回数の記録条件を変えるとき
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.AWSendImpressionAction()
- 位置: L210-212
- 役割: インプレッションに伴う操作の記録を親に依頼する
- 触るとき: インプレッションのアクション種別を追加するとき
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.AWFindBackupsInWellKnownLocations()
- 位置: L214-219
- 役割: 既知の場所にあるバックアップの探索を親に依頼し、結果を content へ複製して返す
- 触るとき: 移行時のバックアップ検出の経路を調べるとき
- 呼び出し先: `this.sendQueryAndCloneForContent()`

## AboutWelcomeChild.getAWContent()
- 位置: async L224-262
- 役割: 帰属データ、Nimbus の設定、既定値、既定ブラウザ・ピンの要否を集め、言語不一致時は言語情報も加えて React 用のコンテンツを組み立てる
- 触るとき: ページ初期描画に渡すデータの形を変えるとき。実験の設定値が既定値より優先される点に注意
- 呼び出し先: `Cu.cloneInto()`, `lazy.AboutWelcomeDefaults.getDefaults()`, `lazy.AboutWelcomeDefaults.prepareContentForReact()`, `lazy.log.debug()`, `this.sendQuery()`
- 条件付き依存: `if (featureConfig.languageMismatchEnabled)` → `this.sendQuery()`
- 参照: `defaults.backdrop`, `defaults.screens`, `experimentMetadata?.slug`, `featureConfig.appAndSystemLocaleInfo`, `featureConfig.backdrop`, `featureConfig.languageMismatchEnabled`, `featureConfig.needDefault`, `featureConfig.needPin`, `featureConfig.screens`, `this.contentWindow`

## AboutWelcomeChild.AWGetFeatureConfig()
- 位置: L264-266
- 役割: getAWContent の結果を Promise としてページへ返す
- 触るとき: ページの初期設定の取得経路を調べるとき
- 呼び出し先: `this.getAWContent()`, `this.wrapPromise()`

## AboutWelcomeChild.AWGetFxAMetricsFlowURI()
- 位置: L268-270
- 役割: FxA の計測フロー URI を親から取得して返す
- 触るとき: FxA 関連のリンクに付く計測パラメータを変えるとき
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.AWGetSelectedTheme()
- 位置: L272-274
- 役割: 現在選ばれているテーマの短い名前を親から取得して返す
- 触るとき: テーマ選択画面の初期値を調べるとき
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.AWSendEventTelemetry()
- 位置: L281-291
- 役割: toolbar の entrypoint があれば event_context に加えて、TELEMETRY_EVENT を親へ送る
- 触るとき: about:welcome のテレメトリ項目を変えるとき。event_context が無いと entrypoint の代入で例外になる点に注意
- 呼び出し先: `this.AWSendToParent()`
- 参照: `eventData.event_context`, `eventData.event_context.entrypoint`, `lazy.toolbarEntrypoint`

## AboutWelcomeChild.AWSendToParent()
- 位置: L300-302
- 役割: AWPage: 接頭辞付きの種別で、データを親へ送って結果を content へ複製して返す
- 触るとき: 親へのメッセージ種別を新しく追加するとき。親側の onContentMessage と対で見る
- 呼び出し先: `this.sendQueryAndCloneForContent()`

## AboutWelcomeChild.AWWaitForMigrationClose()
- 位置: L304-306
- 役割: 移行ウィザードが閉じるまで待つ Promise を親に依頼する
- 触るとき: 移行完了後に次の画面へ進むタイミングを変えるとき
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.setDidSeeFinalScreen()
- 位置: L308-318
- 役割: 最終画面を見たことを示す didSeeFinalScreen の pref を SPECIAL_ACTION の SET_PREF で true にする
- 触るとき: オンボーディング完了の判定を変えるとき。ツールバーボタンの撤去判定もこの pref を見る
- 呼び出し先: `this.AWSendToParent()`

## AboutWelcomeChild.focusUrlBar()
- 位置: L320-324
- 役割: 親に FOCUS_URLBAR の特殊アクションを送り、アドレスバーへフォーカスを移す
- 触るとき: 完了後のフォーカス先を変えるとき
- 呼び出し先: `this.AWSendToParent()`

## AboutWelcomeChild.AWFinish()
- 位置: L326-331
- 役割: 完了 pref を立て、ページを about:home へ移動し、アドレスバーへフォーカスする
- 触るとき: オンボーディング完了時の遷移先を変えるとき
- 呼び出し先: `this.focusUrlBar()`, `this.setDidSeeFinalScreen()`
- 参照: `this.contentWindow.location.href`

## AboutWelcomeChild.AWEnsureAddonInstalled()
- 位置: L333-337
- 役割: 指定のアドオンが入るまでの待ちを親に依頼して結果を返す
- 触るとき: アドオン導入を伴う画面の挙動を変えるとき
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.AWGetInstalledAddons()
- 位置: L339-343
- 役割: 有効なアドオン ID の一覧を親から取得して返す
- 触るとき: 導入済みアドオンに応じて画面を出し分けるとき
- 呼び出し先: `this.sendQueryAndCloneForContent()`, `this.wrapPromise()`

## AboutWelcomeChild.AWEnsureLangPackInstalled()
- 位置: L345-389
- 役割: 言語パックの導入を親に依頼し、完了後に Localization で言語名入りの文字列を用意して、コンテンツへ複製して返す
- 触るとき: 言語パックの導入後に表示文言が正しく切り替わらない問題を調べるとき
- 呼び出し先: `Cu.cloneInto()`, `Promise.all()`, `Promise.all(formatting).then()`, `addMessageArgsAndUseLangPack()`, `this.sendQuery()`, `this.sendQuery( "AWPage:ENSURE_LANG_PACK_INSTALLED", negotiated.langPack ).then()`, `this.wrapPromise()`
- 参照: `content.languageSwitcher`, `negotiated.langPack`, `negotiated.requestSystemLocales`, `this.contentWindow`

## addMessageArgsAndUseLangPack()
- 位置: L362-381
- 役割: string_id を持つ値に交渉済み言語名を引数として加え、useLangPack の項目は整形済みの文字列を raw として埋める
- 触るとき: 言語パック対応の文字列の扱いを変えるとき。内側の関数で、AWEnsureLangPackInstalled からだけ呼ばれる
- 呼び出し先: `Object.values()`
- 条件付き依存: `if (value.useLangPack)` → `formatting.push()`
- 条件付き依存: `if (value.useLangPack)` → `l10n.formatValue(value.string_id, value.args).then()`
- 条件付き依存: `if (value.useLangPack)` → `l10n.formatValue()`
- 参照: `negotiated.langPackDisplayName`, `value.args`, `value.raw`, `value.string_id`, `value.useLangPack`, `value?.string_id`

## AboutWelcomeChild.AWSetRequestedLocales()
- 位置: L391-396
- 役割: 要求する言語リストを親に設定させる
- 触るとき: 言語選択の反映を変えるとき
- 呼び出し先: `this.sendQueryAndCloneForContent()`

## AboutWelcomeChild.AWNegotiateLangPackForLanguageMismatch()
- 位置: L398-403
- 役割: アプリと OS の言語が違うときの言語パック交渉を親に依頼する
- 触るとき: 言語不一致画面の判定を変えるとき
- 呼び出し先: `this.sendQueryAndCloneForContent()`

## AboutWelcomeChild.AWSendToDeviceEmailsSupported()
- 位置: L405-409
- 役割: 端末へのメール送信が使えるロケールかを親に問い合わせる
- 触るとき: モバイル版ダウンロードのリンクを出すかどうかを変えるとき
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.AWNewScreen()
- 位置: L411-413
- 役割: 新しい画面に入ったことを親に通知する
- 触るとき: 画面遷移の記録を変えるとき
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.AWGetUnhandledCampaignAction()
- 位置: L415-419
- 役割: 未処理のキャンペーン動作を親から取得して複製して返す
- 触るとき: キャンペーン経由の既定ブラウザ設定などの扱いを調べるとき
- 呼び出し先: `this.sendQueryAndCloneForContent()`

## AboutWelcomeChild.AWWaitForNimbus()
- 位置: L421-423
- 役割: Nimbus の準備完了を親で待つ Promise を返す
- 触るとき: 実験設定の読み込み前に描画が始まる問題を調べるとき
- 呼び出し先: `this.sendQuery()`, `this.wrapPromise()`

## AboutWelcomeChild.RPMGetFormatURLPref()
- 位置: L425-427
- 役割: URL の書式 pref を Services.urlFormatter で解決して返す
- 触るとき: about:welcome 内の書式付き URL の作り方を変えるとき
- 呼び出し先: `Services.urlFormatter.formatURLPref()`
- XPCOM: `Services.urlFormatter`

## AboutWelcomeChild.handleEvent()
- 位置: L433-435
- 役割: 受け取ったページ側イベントの種別をログに出すだけで、処理はしない
- 触るとき: ページからのイベント受信の扱いを増やすとき。現状は記録のみ
- 呼び出し先: `lazy.log.debug()`
- 参照: `event.type`
