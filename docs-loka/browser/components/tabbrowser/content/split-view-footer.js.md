# browser/components/tabbrowser/content/split-view-footer.js

source: browser/components/tabbrowser/content/split-view-footer.js
source-hash: bec7c2621ff9294a5ab560444057600b73f1c6ae
lines: 232

## <module>
- 役割: 分割ビューの非アクティブ側パネルの隅に、ファビコンとドメインを表示する split-view-footer 要素を定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.generateQI()`, `customElements.define()`

## onLocationChange()
- 位置: L40-44
- 役割: トップレベルの URL 変更を受けて、フッターの URI 表示を更新する。
- 触るとき: フッターの表示ドメインが遷移に追従しない問題を調べるとき。
- 条件付き依存: `if (aWebProgress?.isTopLevel && aLocation)` → `this.#updateUri()`

## onSecurityChange()
- 位置: L45-51
- 役割: セキュリティ状態が安全でない、または壊れている場合を判定して insecure 表示を切り替える。
- 触るとき: フッターの警告表示の条件を変えるとき。
- 呼び出し先: `this.#toggleInsecure()`
- XPCOM: [`nsIWebProgressListener`](../../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## MozSplitViewFooter.connectedCallback()
- 位置: L68-89
- 役割: 初回接続時にマークアップを挿入し、各要素を取得して表示を更新し、イベントを登録する。
- 触るとき: フッターの構造や初期化の流れを変えるとき。
- 呼び出し先: `this.#updateSecurityElement()`, `this.#updateTabImageIconElement()`, `this.#updateUriElement()`, `this.addEventListener()`, `this.appendChild()`, `this.menuButtonElement.addEventListener()`, `this.querySelector()`

## MozSplitViewFooter.disconnectedCallback()
- 位置: L91-93
- 役割: DOM から外れたときにタブとの関連付けを解除する。
- 触るとき: フッター削除時のリスナー解除漏れを調べるとき。
- 呼び出し先: `this.#resetTab()`

## MozSplitViewFooter.handleEvent()
- 位置: L95-109
- 役割: クリックの伝播停止、メニューボタンの command での分割ビューメニュー表示、タブ属性変更の処理を振り分ける。
- 触るとき: フッターのクリックやメニューボタンの動作を変えるとき。
- 呼び出し先: `e.stopPropagation()`, `gBrowser.openSplitViewMenu()`, `this.#handleTabAttrModified()`

## MozSplitViewFooter.#handleTabAttrModified()
- 位置: L111-117
- 役割: タブの image 属性が変わったらフッターのアイコン URL を更新する。
- 触るとき: ファビコンの更新契機を調べるとき。
- 呼び出し先: `this.#updateTabImageIconSrc()`

## MozSplitViewFooter.#toggleInsecure()
- 位置: L124-132
- 役割: insecure フラグを保存し、警告とアイコンの表示を更新する。
- 触るとき: 安全でない接続時の表示切り替えを調べるとき。
- 条件付き依存: `if (this.securityElement)` → `this.#updateSecurityElement()`
- 条件付き依存: `if (this.tabImageIconElement)` → `this.#updateTabImageIconElement()`

## MozSplitViewFooter.#updateSecurityElement()
- 位置: L134-138
- 役割: http か https で、かつ insecure のときだけ警告要素を表示する。
- 触るとき: 警告を出す URL スキームの条件を変えるとき。
- 呼び出し先: `this.#uri.schemeIs()`

## MozSplitViewFooter.#updateTabImageIconSrc()
- 位置: L145-150
- 役割: アイコンの URL を保存し、要素が存在すれば反映する。
- 触るとき: ファビコン URL の受け渡しを調べるとき。
- 条件付き依存: `if (this.tabImageIconElement)` → `this.#updateTabImageIconElement()`

## MozSplitViewFooter.#updateTabImageIconElement()
- 位置: L152-160
- 役割: 安全で URL があるときだけアイコンを表示し、それ以外は隠す。
- 触るとき: ファビコンの表示・非表示の条件を変えるとき。
- 条件付き依存: `if (canShowIcon)` → `this.tabImageIconElement.setAttribute()`
- 条件付き依存: `if (!(canShowIcon))` → `this.tabImageIconElement.removeAttribute()`

## MozSplitViewFooter.#updateUri()
- 位置: L167-176
- 役割: URI を保存し、about:opentabs ならフッター自体を隠して表示と警告を更新する。
- 触るとき: フッターに表示する URI の扱いや about:opentabs での非表示を調べるとき。
- 条件付き依存: `if (this.uriElement)` → `this.#updateUriElement()`
- 条件付き依存: `if (this.securityElement)` → `this.#updateSecurityElement()`

## MozSplitViewFooter.#updateUriElement()
- 位置: L178-183
- 役割: URI を表示用に整形してテキスト要素へ設定する。
- 触るとき: ドメイン表示の書式を変えるとき。
- 呼び出し先: `BrowserUtils.formatURIForDisplay()`

## MozSplitViewFooter.setTab()
- 位置: L190-212
- 役割: 指定タブに紐付け、ファビコン・URI・セキュリティ状態を反映して進捗リスナーを登録する。
- 触るとき: フッターがどのタブを表示するかの結び付けを変えるとき。
- 呼び出し先: `tab.addEventListener()`, `tab.linkedBrowser.addProgressListener()`, `this.#resetTab()`, `this.#toggleInsecure()`, `this.#updateTabImageIconSrc()`, `this.#updateUri()`
- XPCOM: [`nsIWebProgress`](../../../../dom/interfaces/base/nsIBrowser.idl.md) / [`nsIWebProgressListener`](../../../../dom/webbrowserpersist/nsIWebBrowserPersist.idl.md)

## MozSplitViewFooter.#resetTab()
- 位置: L217-227
- 役割: 現在のタブとのイベント・進捗リスナーの関連付けを解除する。
- 触るとき: タブ切り替え時のリスナー解除を調べるとき。
- 条件付き依存: `if (this.#tab)` → `this.#tab.removeEventListener()`
- 条件付き依存: `if (this.#tab.linkedBrowser?.webProgress)` → `this.#tab.linkedBrowser.removeProgressListener()`
