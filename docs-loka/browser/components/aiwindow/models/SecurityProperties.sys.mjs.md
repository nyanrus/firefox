# browser/components/aiwindow/models/SecurityProperties.sys.mjs

source: browser/components/aiwindow/models/SecurityProperties.sys.mjs
source-hash: cf9aba4e80de4cd2c74a90069ec7b33c7818cd37
lines: 123

## <module>
- 役割: LLM に渡すタブやページの URL を http と https に限るためのプロトコル判定関数 isAllowedURLProtocol を定義する。

## isAllowedURLProtocol()
- 位置: L19-21
- 役割: URL を解析してプロトコルが http: か https: のときだけ true を返す。
- 触るとき: モデルに見せてよい URL の範囲を変えるとき。変更にはセキュリティレビューが要る。
- 呼び出し先: `ALLOWED_URL_PROTOCOLS.has()`, `URL.parse()`
- 参照: `URL.parse(url)?.protocol`

## SecurityProperties.privateData()
- 位置: L44-46
- 役割: コミット済みの privateData フラグを返す。
- 触るとき: 個人データを含む会話かどうかで、使えるツールを絞る判定を調べるとき。
- 参照: `this.#privateData`

## SecurityProperties.setPrivateData()
- 位置: L47-49
- 役割: privateData を次のコミットで立つよう staging に記録する。
- 触るとき: 個人データ(履歴や記憶)を扱う処理を追加して、会話にフラグを立てるとき。
- 参照: `this.#newPrivateData`

## SecurityProperties.untrustedInput()
- 位置: L52-54
- 役割: コミット済みの untrustedInput フラグを返す。
- 触るとき: Web 由来の信頼できない入力が会話に入ったかを判定する箇所を調べるとき。
- 参照: `this.#untrustedInput`

## SecurityProperties.setUntrustedInput()
- 位置: L55-57
- 役割: untrustedInput を次のコミットで立つよう staging に記録する。
- 触るとき: ページ内容などの未信頼データを取り込むツールを追加したとき。
- 参照: `this.#newUntrustedInput`

## SecurityProperties.commit()
- 位置: L64-69
- 役割: staging の 2 つのフラグを committed 側へ OR で反映し、staging を倒す。一度立ったフラグは下げられない。
- 触るとき: フラグの確定タイミングを変えるとき、または一度立ったフラグが戻らない理由を確認するとき。
- 参照: `this.#newPrivateData`, `this.#newUntrustedInput`, `this.#privateData`, `this.#untrustedInput`

## SecurityProperties.toJSON()
- 位置: L81-86
- 役割: staging を含めた現在の 2 フラグを保存用のオブジェクトにして返す。
- 触るとき: 保存される会話データに新しいフラグを足すとき。
- 参照: `this.#newPrivateData`, `this.#newUntrustedInput`, `this.#privateData`, `this.#untrustedInput`

## SecurityProperties.fromJSON()
- 位置: L100-112
- 役割: 保存された JSON から 2 フラグを復元する。null なら両方 false の既定値を返す。復元後は committed になる。
- 触るとき: 過去の会話のフラグがどう復元されるか(古い会話の移行を含む)を確認するとき。
- 参照: `obj.privateData`, `obj.untrustedInput`, `props.#privateData`, `props.#untrustedInput`

## SecurityProperties.getLogText()
- 位置: L119-121
- 役割: 2 フラグの状態を private=... untrusted=... の文字列にする。
- 触るとき: ログ出力の書式を変えるとき、または会話のフラグ状態をログで確かめるとき。
- 参照: `this.privateData`, `this.untrustedInput`
