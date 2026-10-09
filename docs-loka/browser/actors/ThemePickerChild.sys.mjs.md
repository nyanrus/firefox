# browser/actors/ThemePickerChild.sys.mjs

source: browser/actors/ThemePickerChild.sys.mjs
source-hash: bad3e0fe5e49e0d7cb15114a3a90cb4cff9d5ed2
lines: 128

## <module>
- 役割: テーマ選択 UI のコンテンツページと親プロセスの間を仲介する子側アクター。設定変更の通知や操作要求を扱う。

## ThemePickerChild.actorCreated()
- 位置: L16-21
- 役割: OS の配色変更と、テーマ関連の 3 つの pref の変化を監視し始める。
- 触るとき: 変化を検知する対象を増やすとき。
- 呼び出し先: `Services.obs.addObserver()`, `Services.prefs.addObserver()`
- 参照: `this.lookAndFeelChanged`, `this.prefChanged`
- XPCOM: `Services.obs` / `Services.prefs`

## ThemePickerChild.didDestroy()
- 位置: L23-31
- 役割: actorCreated で登録した監視を解除する。
- 触るとき: アクター破棄時の後始末を変えるとき。
- 呼び出し先: `Services.obs.removeObserver()`, `Services.prefs.removeObserver()`
- 参照: `this.lookAndFeelChanged`, `this.prefChanged`
- XPCOM: `Services.obs` / `Services.prefs`

## ThemePickerChild.lookAndFeelChanged()
- 位置: L33-44
- 役割: コンテンツ由来の配色が暗いかで dark か light を決め、ThemePickerDeviceAppearanceUpdated を発火する。
- 触るとき: デバイスの外観をページへ渡す内容を変えるとき。
- 呼び出し先: `Cu.cloneInto()`, `this.contentWindow.dispatchEvent()`
- 参照: `Services.appinfo .contentThemeDerivedColorSchemeIsDark`, `this.contentWindow`, `this.contentWindow.CustomEvent`
- XPCOM: `Services.appinfo`

## ThemePickerChild.prefChanged()
- 位置: async L46-64
- 役割: 変わった pref に応じて親へ状態を問い合わせ、結果を対応するイベントでページへ送る。
- 触るとき: 設定変更をページへ反映する仕組みを変えるとき。
- 呼び出し先: `this.dispatchToWindow()`, `this.sendQuery()`

## ThemePickerChild.handleEvent()
- 位置: async L66-107
- 役割: ページの要求イベントを親への問い合わせに変換し、結果をページへ返す。表示時はテレメトリを記録する。
- 触るとき: ページからの操作の受け口を追加・変更するとき。
- 呼び出し先: `Glean.themePicker.shown.record()`, `this.dispatchToWidget()`, `this.dispatchToWindow()`, `this.sendQuery()`
- 参照: `event.composedTarget`, `event.detail`, `event.type`

## ThemePickerChild.dispatchToWidget()
- 位置: L109-118
- 役割: 要求元の要素に、バブルと composed 付きのイベントを発火させる。
- 触るとき: 初期状態を要素単位で返す経路を変えるとき。
- 呼び出し先: `Cu.cloneInto()`, `target.dispatchEvent()`
- 参照: `target.documentGlobal`, `win.CustomEvent`

## ThemePickerChild.dispatchToWindow()
- 位置: L120-126
- 役割: コンテンツウィンドウに詳細付きのイベントを発火させる。
- 触るとき: ページへの通知の形を変えるとき。
- 呼び出し先: `Cu.cloneInto()`, `this.contentWindow.dispatchEvent()`
- 参照: `this.contentWindow`, `this.contentWindow.CustomEvent`
