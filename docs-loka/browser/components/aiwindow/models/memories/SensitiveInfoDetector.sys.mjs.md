# browser/components/aiwindow/models/memories/SensitiveInfoDetector.sys.mjs

source: browser/components/aiwindow/models/memories/SensitiveInfoDetector.sys.mjs
source-hash: b1153cdc708c06fd4cf93688fe9c469ba9020c52
lines: 536

## <module>
- 役割: テキストに含まれる個人情報(社会保障番号やクレジットカード、メール、電話、住所など)と、医療・金融・宗教などの機微キーワードを検出する。

## validateCreditCard()
- 位置: L411-413
- 役割: カード番号の検証をResource側のCreditCard.isValidNumberに委ねる。
- 触るとき: カード番号らしき数列の誤検出を調べるとき。
- 呼び出し先: `CreditCard.isValidNumber()`

## isPublicIPv4()
- 位置: L421-442
- 役割: IPv4の文字列を4つの0から255に分けて検証し、プライベート・ループバック・リンクローカル・0.x.x.xの範囲でなければ公開IPとしてtrueを返す。
- 触るとき: IPアドレスを機微情報として扱う範囲を変えるとき、私用の範囲の判定を見直すとき。
- 呼び出し先: `ip.split()`, `ip.split(".").map()`, `isNaN()`, `parts.some()`
- 参照: `parts.length`

## validateRoutingNumber()
- 位置: L452-464
- 役割: 9桁の銀行の経路番号を、重み3・7・1の チェックサムで検証する。
- 触るとき: 9桁の数字が口座番号として誤検出されると調べるとき。
- 呼び出し先: `/^\d{9}$/.test()`, `routingNumber.split()`, `routingNumber.split("").map()`

## SensitiveInfoDetector.constructor()
- 位置: L470-472
- 役割: 検出パターンの表(PATTERNS)をインスタンスに保持する。
- 触るとき: パターンの差し替えをテストで行うとき。
- 参照: `this.patterns`

## SensitiveInfoDetector.containsSensitiveInfo()
- 位置: L480-502
- 役割: 各パターンの正規表現でテキストを検索し、検証関数がある場合は一致した値を検証して、一つでも通ればtrueを返す。
- 触るとき: 個人情報として除外される発話を調べるとき、新しいパターンを足すとき。正規表現を毎回生成している点も性能面で見る。
- 呼び出し先: `Object.values()`, `text.match()`
- 条件付き依存: `if (pattern.validator)` → `pattern.validator()`
- 参照: `pattern.regex`, `pattern.validator`, `this.patterns`

## SensitiveInfoDetector.containsSensitiveKeywords()
- 位置: L511-534
- 役割: 小文字化した本文に機微分野のキーワードを単語境界付きで照合し、語尾のsやesの揺れも許容して、一つでも一致すればtrueを返す。
- 触るとき: 医療や金融などの話題を記憶から外す範囲を変えるとき、キーワードを増減するとき。
- 呼び出し先: `Object.values()`, `keyword.endsWith()`, `pattern.test()`, `text.toLowerCase()`
- 条件付き依存: `if (keyword.endsWith("y"))` → `keyword.slice()`
