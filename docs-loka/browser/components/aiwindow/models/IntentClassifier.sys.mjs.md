# browser/components/aiwindow/models/IntentClassifier.sys.mjs

source: browser/components/aiwindow/models/IntentClassifier.sys.mjs
source-hash: 88e22f24e497c539b5c9f52224d5544fade38af2
lines: 334

## <module>
- 役割: 検索かチャットかを判定する意図分類器 IntentClassifier を定義する。固定の語句リストで即座に chat を返すほか、地域に応じた分類モデルで判定する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## normalizeTextForChatAllowlist()
- 位置: L163-174
- 役割: NFKC と小文字化の後、結合記号を取り除いて空白を整え、アクセント無しで比較できる形にする。
- 触るとき: フランス語など発音記号つきの入力を照合の対象に入れる範囲を変えるとき。
- 呼び出し先: `s .normalize()`, `s .normalize("NFKC") .toLowerCase()`, `s .normalize("NFKC") .toLowerCase() .normalize()`, `s .normalize("NFKC") .toLowerCase() .normalize("NFD") .replace()`, `s .normalize("NFKC") .toLowerCase() .normalize("NFD") .replace(/\p{M}/gu, "") .replace()`, `s .normalize("NFKC") .toLowerCase() .normalize("NFD") .replace(/\p{M}/gu, "") .replace(/\s+/g, " ") .trim()`

## tokenizeTextForChatAllowlist()
- 位置: L177-181
- 役割: 正規化した文字列を文字・数字・_ 以外で区切り、トークンの配列にする。
- 触るとき: 照合の単語区切りを変えるとき。
- 呼び出し先: `normalizeTextForChatAllowlist()`, `normalizeTextForChatAllowlist(s) .split()`, `normalizeTextForChatAllowlist(s) .split(/[^\p{L}\p{N}_]+/u) .filter()`

## buildChatAllowlist()
- 位置: L183-197
- 役割: 各語句を正規化して語数ごとに分けた Map(語数 -> 語句の集合)を作る。
- 触るとき: 許可語句の登録方法や語数による分け方を変えるとき。
- 呼び出し先: `byLen.get()`, `byLen.get(k).add()`, `byLen.has()`, `key.split()`, `tokenizeTextForChatAllowlist()`, `tokenizeTextForChatAllowlist(p).join()`
- 条件付き依存: `if (!byLen.has(k))` → `byLen.set()`
- 参照: `key.split(" ").length`

## makeIsolatedPhraseChecker()
- 位置: L200-222
- 役割: 語句から判定関数を作る。判定関数はクエリ中に語句がトークン単位で含まれるかを調べ、結果を結果キャッシュに保存する。
- 触るとき: 許可語句の一致判定の仕組みを変えるとき、またはキャッシュの挙動を確認するとき。
- 呼び出し先: `buildChatAllowlist()`

## containsIsolatedPhrase()
- 位置: L204-221
- 役割: クエリを正規化して、語数の多い順ではなく登録された語数ごとに連続するトークン列が集合に含まれるかを調べる。
- 触るとき: 「hi」のような 1 語の許可語が、別の語の一部として誤って一致していないかを確かめるとき。
- 呼び出し先: `cache.has()`, `cache.set()`, `normalizeTextForChatAllowlist()`, `qNorm.split()`, `qNorm.split(/[^\p{L}\p{N}_]+/u).filter()`, `set.has()`, `toks.slice()`, `toks.slice(i, i + k).join()`
- 条件付き依存: `if (cache.has(qNorm))` → `cache.get()`
- 条件付き依存: `if (set.has(toks.slice(i, i + k).join(" ")))` → `cache.set()`
- 参照: `toks.length`

## getIntentModelInfoForLocale()
- 位置: L230-241
- 役割: ホーム地域が FR なら英仏両対応の分類モデル、それ以外は既定の英語モデルの ID と機能 ID を返す。
- 触るとき: 地域ごとに使う意図分類モデルを増やすとき。
- 参照: `lazy.Region.home`

## getForcedChatPhrasesForModel()
- 位置: L250-255
- 役割: 英仏モデルの場合だけ、フランス語の許可語句を英語の語句の後ろに足して返す。
- 触るとき: モデルごとに強制 chat にする語句を変えるとき。

## _isForcedChat()
- 位置: L279-288
- 役割: モデル ID ごとに判定関数を 1 回だけ作り、クエリが強制 chat の語句を含むかを返す。
- 触るとき: 強制 chat の判定条件を変えるとき。1 語の許可語(hi や sup など)は、hi-fi のような別の語の中でも一致する点に注意。
- 呼び出し先: `checker()`, `this._forcedChatCheckers.get()`
- 条件付き依存: `if (!checker)` → `makeIsolatedPhraseChecker()`
- 条件付き依存: `if (!checker)` → `getForcedChatPhrasesForModel()`
- 条件付き依存: `if (!checker)` → `this._forcedChatCheckers.set()`

## getPromptIntent()
- 位置: async L296-322
- 役割: クエリの ? を除いて強制 chat を先に判定し、該当しなければ分類モデルを実行する。search と判定されかつ確信度 0.8 以上のときだけ search、それ以外は chat を返す。エラーは記録して再送出する。
- 触るとき: 検索に回す閾値や分類モデルの扱いを変えるとき、または検索されるべき問い合わせが chat に流れる原因を調べるとき。
- 呼び出し先: `console.error()`, `engine.run()`, `getIntentModelInfoForLocale()`, `resp[0].label.toLowerCase()`, `this._createEngine()`, `this._isForcedChat()`, `this._preprocessQuery()`
- 参照: `modelInfo.modelId`, `resp[0].score`

## _preprocessQuery()
- 位置: L325-332
- 役割: 文字列以外を TypeError で拒否し、文字列から ? を取り除いて前後の空白を除く。
- 触るとき: 分類に入る前の入力整形を変えるとき。
- 呼び出し先: `query.replace()`, `query.replace(/\?/g, "").trim()`
