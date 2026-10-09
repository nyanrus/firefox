# browser/base/content/aboutTabCrashed.js

source: browser/base/content/aboutTabCrashed.js
source-hash: 602f7fe79f0bcb9e34d975eb7f5347132c4969bc
lines: 263

## <module>
- 役割: タブのクラッシュ時に表示される about:tabcrashed ページの制御。親プロセスとのメッセージ、クラッシュレポート欄、復元などのボタンを扱う。
- 呼び出し先: `AboutTabCrashed.init()`

## pageData()
- 位置: L31-45
- 役割: about:tabcrashed の URL のクエリから、クラッシュしたページのタイトルと URL を取り出す。結果は一度だけ計算して保持する。
- 触るとき: クラッシュしたページの情報の渡し方を変えるとき。
- 呼び出し先: `URL.replace()`, `decodeURIComponent()`, `queryString.match()`
- 参照: `document.documentURI`, `this.pageData`

## init()
- 位置: L47-51
- 役割: ページのタイトルを設定し、DOMContentLoaded の監視を始める。
- 触るとき: ページ初期化の順序を変えるとき。
- 呼び出し先: `addEventListener()`
- 参照: `document.title`, `this.pageData.title`

## receiveMessage()
- 位置: L53-68
- 役割: 親から届く UpdateCount、SetCrashReportAvailable、CrashReportSent を対応する処理へ振り分ける。
- 触るとき: 親からの新しいメッセージを追加するとき。
- 呼び出し先: `this.onCrashReportSent()`, `this.onSetCrashReportAvailable()`, `this.setMultiple()`
- 参照: `message.data.count`, `message.name`

## handleEvent()
- 位置: L70-81
- 役割: DOMContentLoaded と click のイベントを対応する処理へ振り分ける。
- 触るとき: ページが受け取るイベントを増やすとき。
- 呼び出し先: `this.onClick()`, `this.onDOMContentLoaded()`
- 参照: `event.type`

## onDOMContentLoaded()
- 位置: L83-98
- 役割: 親のメッセージを登録し、ボタンのクリックを監視し、読み込み完了を通知する。
- 触るとき: ページ読み込み完了時の処理を変えるとき。
- 呼び出し先: `RPMAddMessageListener()`, `RPMSendAsyncMessage()`, `document.dispatchEvent()`, `document.getElementById()`, `el.addEventListener()`, `this.CLICK_TARGETS.forEach()`, `this.MESSAGES.forEach()`, `this.receiveMessage.bind()`

## onClick()
- 位置: L100-122
- 役割: 閉じる、復元、すべて復元、レポート送信のクリックに応じて、親へ送るメッセージ名を決める。
- 触るとき: ボタンを追加・変更するとき。
- 呼び出し先: `this.sendMessage()`, `this.showCrashReportUI()`
- 参照: `event.target.checked`, `event.target.id`

## onSetCrashReportAvailable()
- 位置: L148-169
- 役割: クラッシュレポートの有無と設定を反映し、レポート欄の表示と自動送信の案内を切り替える。
- 触るとき: クラッシュレポートの初期表示を変えるとき。
- 呼び出し先: `document.dispatchEvent()`
- 条件付き依存: `if (data.hasReport)` → `document.documentElement.classList.add()`
- 条件付き依存: `if (data.hasReport)` → `document.getElementById()`
- 条件付き依存: `if (data.hasReport)` → `this.showCrashReportUI()`
- 条件付き依存: `if (!(data.hasReport))` → `this.showCrashReportUI()`
- 条件付き依存: `if (data.requestAutoSubmit)` → `document.getElementById()`
- 参照: `data.hasReport`, `data.includeURL`, `data.requestAutoSubmit`, `data.sendReport`, `document.getElementById("includeURL").checked`, `document.getElementById("requestAutoSubmit").hidden`, `document.getElementById("sendReport").checked`, `message.data`, `this.hasReport`

## onCrashReportSent()
- 位置: L175-178
- 役割: レポート送信後に、送信済みを示すクラスへ切り替える。
- 触るとき: 送信完了後の表示を変えるとき。
- 呼び出し先: `document.documentElement.classList.add()`, `document.documentElement.classList.remove()`

## showCrashReportUI()
- 位置: L186-189
- 役割: レポート入力欄の表示を切り替える。
- 触るとき: レポート欄の表示条件を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `options.hidden`

## setMultiple()
- 位置: L199-212
- 役割: 複数のクラッシュページが開いているかで、復元ボタンの主ボタン表示を切り替える。
- 触るとき: 複数タブのクラッシュ時の文言やボタンの強調を変えるとき。
- 呼び出し先: `document.getElementById()`, `main.setAttribute()`
- 条件付き依存: `if (hasMultiple)` → `restoreTab.classList.remove()`
- 条件付き依存: `if (!(hasMultiple))` → `restoreTab.classList.add()`

## sendMessage()
- 位置: L223-259
- 役割: 選ばれた操作と、レポート送信時の入力(コメント、URL、自動送信)をまとめて親へ送る。
- 触るとき: 親へ渡す情報の項目を増やすとき。
- 呼び出し先: `RPMSendAsyncMessage()`, `document.getElementById()`
- 条件付き依存: `if (this.hasReport)` → `document.getElementById()`
- 条件付き依存: `if (sendReport)` → `document.getElementById("comments").value.trim()`
- 条件付き依存: `if (sendReport)` → `document.getElementById()`
- 条件付き依存: `if (includeURL)` → `this.pageData.URL.trim()`
- 条件付き依存: `if (!(requestAutoSubmit.hidden))` → `document.getElementById()`
- 参照: `document.getElementById("autoSubmit").checked`, `document.getElementById("includeURL").checked`, `document.getElementById("sendReport").checked`, `requestAutoSubmit.hidden`, `this.hasReport`
