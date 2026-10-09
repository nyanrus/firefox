# browser/components/aboutlogins/content/utils/keypress.mjs

source: browser/components/aboutlogins/content/utils/keypress.mjs
source-hash: 13a97964c07fa2619ee5bc3c092dc6a93251d42c
lines: 43

## <module>
- 役割: キーの組み合わせ(例: ctrl+k)を判定してコールバックを呼ぶ、キー操作の補助を定義する

## useKeyEvent()
- 位置: L8-39
- 役割: 組み合わせ文字列を解析し、指定の対象に keydown などのリスナーを付け、外すための関数を返す
- 触るとき: 新しいショートカットの判定方法や対象イベントを変えるとき
- 呼び出し先: `keyCombination.split()`, `part.toLowerCase()`, `parts.map()`, `target.addEventListener()`, `target.removeEventListener()`

## handleKeyEvent()
- 位置: L13-32
- 役割: 修飾キーの押下状態が組み合わせと一致し、かつ event.code が対象キーに一致したとき、必要なら既定動作を止めてコールバックを呼ぶ
- 触るとき: ショートカットが反応しない、または誤反応する問題を調べるとき。文字は event.key ではなく event.code で判定する(Option+N などで文字が変わるため)
- 呼び出し先: ``key${actualKey}`.toLowerCase()`, `actualKey.toLowerCase()`, `event.code.toLowerCase()`, `keys.find()`, `keys.includes()`, `modifiers.every()`, `modifiers.includes()`
- 条件付き依存: `if (options?.preventDefault)` → `event.preventDefault()`
- 条件付き依存: `if (isModifierCorrect && isKeyCorrect)` → `callback()`
- 参照: `options?.preventDefault`

## handleKeyPress()
- 位置: L41-42
- 役割: withSimpleController を使い、ホストの接続中だけキー判定を有効にするコントローラを作る
- 触るとき: コンポーネントにショートカットを付けるとき
- 呼び出し先: `useKeyEvent()`, `withSimpleController()`
