# browser/components/aboutlogins/content/aboutLoginsUtils.mjs

source: browser/components/aboutlogins/content/aboutLoginsUtils.mjs
source-hash: 2ecea6295031d8edbe66850ecd180df01149fd0b
lines: 79

## <module>
- 役割: about:logins の共通ヘルパーを定義する。テレメトリ送信、ダイアログ外の操作の無効化、主パスワード要求、ダイアログの shadow root 初期化を担う。
- 呼び出し先: `" ".repeat()`

## recordTelemetryEvent()
- 位置: L15-22
- 役割: AboutLoginsRecordTelemetryEvent を detail 付きで document に発行し、親側でテレメトリとして記録させる。
- 触るとき: about:logins のテレメトリ送信の経路や形式を変えるとき。
- 呼び出し先: `document.dispatchEvent()`

## setKeyboardAccessForNonDialogElements()
- 位置: L24-53
- 役割: login-item など操作対象要素の tabindex を切り替える。無効化時はフォーカス中の要素を blur し(confirmation-dialog 内は除く)、既存の tabindex を oldTabIndex に退避して -1 にする。有効化時は退避値を戻す。
- 触るとき: ダイアログ表示中にページ側へフォーカスが移る問題や、キーボード操作の範囲を変えるとき。
- 呼び出し先: `docActiveElement.closest()`, `document.querySelectorAll()`, `pageElements.forEach()`
- 条件付き依存: `if ( !enableKeyboardAccess && docActiveElement && !docActiveElement.closest("confirmation-dialog") )` → `elementToBlur.blur()`
- 条件付き依存: `if (!(el.dataset.oldTabIndex))` → `el.removeAttribute()`
- 参照: `docActiveElement?.shadowRoot?.activeElement`, `el.dataset.oldTabIndex`, `el.tabIndex`

## promptForPrimaryPassword()
- 位置: L55-63
- 役割: AboutLoginsUtils.promptForPrimaryPassword を呼び、主パスワードの入力結果を Promise で返す。
- 触るとき: 主パスワードの要求を画面からどう行うかを変えるとき。
- 呼び出し先: `window.AboutLoginsUtils.promptForPrimaryPassword()`

## initDialog()
- 位置: L72-78
- 役割: テンプレートを複製し、要素に open の shadow root を付けて l10n に接続したうえで、その shadow root を返す。
- 触るとき: ダイアログ系コンポーネントの初期化手順やテンプレートの読み込み方を変えるとき。
- 呼び出し先: `document.l10n.connectRoot()`, `document.querySelector()`, `element.attachShadow()`, `shadowRoot.appendChild()`, `template.content.cloneNode()`
