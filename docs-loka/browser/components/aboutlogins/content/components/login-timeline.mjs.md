# browser/components/aboutlogins/content/components/login-timeline.mjs

source: browser/components/aboutlogins/content/components/login-timeline.mjs
source-hash: ec4543177b7c8966b07f3947e9c0df0d15757316
lines: 80

## <module>
- 役割: ログイン詳細の作成・変更・使用の時系列を描画する login-timeline 要素を定義する
- 呼び出し先: `customElements.define()`

## Timeline.properties()
- 位置: L13-17
- 役割: 履歴配列(history)を宣言する
- 触るとき: タイムラインに渡す項目の形を変えるとき

## Timeline.constructor()
- 位置: L19-22
- 役割: 履歴を空配列で初期化する
- 触るとき: 初期表示の既定値を変えるとき
- 呼び出し先: `super()`
- 参照: `this.history`

## Timeline.render()
- 位置: L24-76
- 役割: 時刻が無い項目を除き時刻順に並べ、項目間の間隔を grid の fr 幅に変換して、点と日付と動作名を描画する
- 触るとき: 項目間の距離感や、時刻の無い項目の扱いを変えるとき。間隔は差分時間をそのまま fr に入れているため、極端な差は見た目が偏る
- 呼び出し先: `JSON.stringify()`, `classMap()`, `html()`, `styleMap()`, `this.history.filter()`, `this.history.map()`, `this.history.sort()`
- 参照: `a.time`, `b.time`, `entry.actionId`, `entry.time`, `historyPoint.time`, `this.history`, `this.history.length`, `this.history[index - 1].time`
