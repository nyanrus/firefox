# browser/components/aboutwelcome/modules/AboutWelcomeDefaults.sys.mjs

source: browser/components/aboutwelcome/modules/AboutWelcomeDefaults.sys.mjs
source-hash: 722291c313bf2e14e09bcc97032c98f354acad49
lines: 1015

## <module>
- 役割: about:welcome の既定コンテンツ、帰属データ、アドオン情報をまとめ、ページ描画用の形へ整えるモジュール
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `Services.prefs.getBoolPref()`, `Services.sysinfo.getProperty()`

## getAddonFromRepository()
- 位置: async L813-827
- 役割: アドオン ID でリポジトリから情報を取り、https の配布元のときだけ ID、名前、URL、アイコン、種別、スクリーンショットを返す
- 触るとき: return_to_amo のアドオン案内を変えるとき。https 以外では null を返す(呼び出し元の AWPage:GET_ADDON_DETAILS は null を前提にしていない点に注意)
- 呼び出し先: `lazy.AddonRepository.getAddonsByIDs()`
- 参照: `addonInfo.icons`, `addonInfo.id`, `addonInfo.name`, `addonInfo.screenshots`, `addonInfo.sourceURI.scheme`, `addonInfo.sourceURI.spec`, `addonInfo.type`

## getAddonInfo()
- 位置: async L829-858
- 役割: 帰属の content が addons.mozilla.org のときに二重エンコードを解き、rta: 接頭辞付きならアドオン情報を取得する
- 触るとき: return_to_amo の判定条件を変えるとき
- 呼び出し先: `console.error()`, `content.includes()`, `content.startsWith()`, `decodeURIComponent()`
- 条件付き依存: `if (content.startsWith("rta:"))` → `getAddonFromRepository()`

## getAttributionContent()
- 位置: async L860-883
- 役割: 帰属データを取得し、AMO 由来ならアドオン案内を、smart_window キャンペーンなら該当 pref を立てて、帰属データを返す
- 触るとき: 帰属データからページ用の値を作る規則を変えるとき
- 呼び出し先: `lazy.AttributionCode.getAttrDataAsync()`
- 条件付き依存: `if (attribution?.source === "addons.mozilla.org")` → `getAddonInfo()`
- 条件付き依存: `if (addonInfo)` → `decodeURIComponent()`
- 条件付き依存: `if (attribution?.campaign === "smart_window")` → `Services.prefs.setBoolPref()`
- 条件付き依存: `if (attribution)` → `decodeURIComponent()`
- 参照: `attribution.ua`, `attribution?.campaign`, `attribution?.source`
- XPCOM: `Services.prefs`

## getDefaults()
- 位置: L886-888
- 役割: 既定のマルチステージ画面の定義を複製して返す
- 触るとき: 既定の画面構成を変えるとき
- 呼び出し先: `Cu.cloneInto()`

## getLocalizedUA()
- 位置: L896-909
- 役割: chrome、edge、ie のいずれかの帰属 UA を、移行ウィザードの表示名に変換する。それ以外は null
- 触るとき: インポート元のボタン文言を増やすとき
- 呼び出し先: `allowedUAs.includes()`
- 条件付き依存: `if (allowedUAs.includes(ua))` → `gSourceL10n.formatValue()`

## prepareMobileDownload()
- 位置: L911-928
- 役割: モバイルダウンロード画面で、端末へのメール送信が使えないロケールならリンクを外し文言を差し替える
- 触るとき: 端末送信非対応のロケールでの文言を変えるとき
- 呼び出し先: `content?.screens?.find()`, `lazy.BrowserUtils.sendToDeviceEmailsSupported()`
- 参照: `content?.screens?.find( screen => screen.id === "AW_MOBILE_DOWNLOAD" )?.content`, `mobileContent.cta_paragraph.action`, `mobileContent.cta_paragraph.text`, `screen.id`

## prepareContentForReact()
- 位置: async L930-1008
- 役割: 帰属 UA に応じてインポート用ボタンの文言と引数を変え、FxA が無効なら関連画面を外し、言語不一致画面の要否を決めて不要な画面を取り除く
- 触るとき: ページに渡す画面構成を最後に整える処理を変えるとき。return_to_amo とスマートウィンドウ用の背景もここで扱う
- 呼び出し先: `Services.prefs.getBoolPref()`, `prepareMobileDownload()`
- 条件付き依存: `if (content?.ua)` → `content?.screens?.find()`
- 条件付き依存: `if (content?.ua)` → `getLocalizedUA()`
- 条件付き依存: `if (!Services.prefs.getBoolPref("identity.fxaccounts.enabled", false))` → `content.screens?.find()`
- 条件付き依存: `if (content.languageMismatchEnabled)` → `content?.screens?.find()`
- 条件付き依存: `if (screen && content.appAndSystemLocaleInfo.canLiveReload)` → `addMessageArgs()`
- 条件付き依存: `if (shouldRemoveLanguageMismatchScreen)` → `lazy.ASRouterScreenUtils.removeScreens()`
- 参照: `action.data`, `content.appAndSystemLocaleInfo.canLiveReload`, `content.backdrop`, `content.languageMismatchEnabled`, `content.screens`, `content.skipFxA`, `content.ua`, `content?.campaign`, `content?.template`, `content?.ua`, `label.args`, `label.string_id`, `label?.string_id`, `s.id`, `screen.content`, `screen.content.languageSwitcher`, `screen.content?.secondary_button_top?.action?.type`, `screen.id`, `screen?.content?.primary_button?.action?.type`
- XPCOM: `Services.prefs`

## addMessageArgs()
- 位置: L986-992
- 役割: 言語不一致画面の文字列すべてに、OS とアプリの言語の表示名を引数として入れる
- 触るとき: 言語不一致画面の表示名の渡し方を変えるとき。prepareContentForReact の内部でのみ使う
- 呼び出し先: `Object.values()`
- 参照: `content.appAndSystemLocaleInfo.displayNames`, `value.args`, `value?.string_id`
