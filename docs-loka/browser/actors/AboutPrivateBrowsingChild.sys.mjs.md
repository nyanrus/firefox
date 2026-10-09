# browser/actors/AboutPrivateBrowsingChild.sys.mjs

source: browser/actors/AboutPrivateBrowsingChild.sys.mjs
source-hash: 7645cbb1ca12d5f067b72c1b941e063b03d58781
lines: 92

## <module>
- 役割: about:privatebrowsing のコンテンツ側アクター。ページへ関数を公開し、Nimbus の実験判定・露出記録と Glean の計測を中継する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## AboutPrivateBrowsingChild.actorCreated()
- 位置: L15-52
- 役割: about:privatebrowsing の window に、Nimbus・計測・リデザイン判定用の関数を exportFunction で登録する。
- 触るとき: ページから呼べる API を追加・削除するとき、またはページ側のスクリプトが関数を見つけられないときに見る。
- 呼び出し先: `Cu.exportFunction()`, `super.actorCreated()`, `this.PrivateBrowsingIsEnrolledInExperiment.bind()`, `this.PrivateBrowsingPromoExposureTelemetry.bind()`, `this.PrivateBrowsingRecordIntroAnimation.bind()`, `this.PrivateBrowsingRecordRedesignClick.bind()`, `this.PrivateBrowsingRedesignEnabled.bind()`, `this.PrivateBrowsingRedesignExposure.bind()`, `this.PrivateBrowsingShouldHideDefault.bind()`
- 参照: `this.contentWindow`

## AboutPrivateBrowsingChild.PrivateBrowsingIsEnrolledInExperiment()
- 位置: L54-58
- 役割: pbNewtab 機能が実験（EXPERIMENT）に参加しているかを真偽値で返す。
- 触るとき: プライベートブラウジングのページ表示を実験参加者だけ変えるときに見る。
- 呼び出し先: `lazy.NimbusFeatures.pbNewtab.getEnrollmentMetadata()`
- 参照: `lazy.EnrollmentType.EXPERIMENT`

## AboutPrivateBrowsingChild.PrivateBrowsingShouldHideDefault()
- 位置: L60-63
- 役割: pbNewtab の変数 content.hideDefault を読み、既定の表示を隠すかどうかを返す。
- 触るとき: 既定の案内や promo の表示制御を Nimbus 側の設定で切り替えるときに見る。
- 呼び出し先: `lazy.NimbusFeatures.pbNewtab.getAllVariables()`
- 参照: `config?.content?.hideDefault`

## AboutPrivateBrowsingChild.PrivateBrowsingPromoExposureTelemetry()
- 位置: L65-67
- 役割: pbNewtab の露出イベントを once: false で記録し、promo が表示されるたびに数える。
- 触るとき: promo の露出計測の回数や重複の扱いを調べるときに見る。
- 呼び出し先: `lazy.NimbusFeatures.pbNewtab.recordExposureEvent()`

## AboutPrivateBrowsingChild.PrivateBrowsingRecordRedesignClick()
- 位置: L69-71
- 役割: 引数 source を使って aboutprivatebrowsing の click 系 Glean 指標を記録する。
- 触るとき: リデザイン画面のクリック計測を追加・修正するときに見る。
- 呼び出し先: `Glean.aboutprivatebrowsing["click" + source].record()`
- 参照: `Glean.aboutprivatebrowsing`

## AboutPrivateBrowsingChild.PrivateBrowsingRecordIntroAnimation()
- 位置: L73-75
- 役割: 導入アニメーションが再生されたことを Glean の introAnimationPlayed 指標に記録する。
- 触るとき: 導入アニメーションの計測結果が合わないときに見る。
- 呼び出し先: `Glean.aboutprivatebrowsing.introAnimationPlayed.record()`

## AboutPrivateBrowsingChild.PrivateBrowsingRedesignExposure()
- 位置: L79-83
- 役割: privateWindowRedesign の露出イベントを once: true で一度だけ記録する。
- 触るとき: リデザイン実験で「加入はしたが治療を見た人」の集計が欠けるときに見る。
- 呼び出し先: `lazy.NimbusFeatures.privateWindowRedesign.recordExposureEvent()`

## AboutPrivateBrowsingChild.PrivateBrowsingRedesignEnabled()
- 位置: L85-90
- 役割: browser.privateWindowRedesign.enabled の pref を読み、リデザインが有効かを返す。
- 触るとき: プライベートウィンドウのリデザインの有効・無効条件を変えるときに見る。
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`
