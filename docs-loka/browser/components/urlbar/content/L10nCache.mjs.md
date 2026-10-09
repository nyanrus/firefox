# browser/components/urlbar/content/L10nCache.mjs

source: browser/components/urlbar/content/L10nCache.mjs
source-hash: 964d2058502dfdba8c2567107a513de6ee818ca8
lines: 431

## <module>
- 役割: urlbar の UI 文字列を同期的に取り出すための L10nCache(Fluent 文字列の値と属性をメモリに保持する)を定義する。

## L10nCache.constructor()
- 位置: L88-90
- 役割: Localization を受け取り、省略時は document.l10n を使うように設定する。
- 触るとき: テストで別の Localization を差し込む、または文字列を取得する先の document を変えるときに見る。
- 参照: `document.l10n`, `this.l10n`

## L10nCache.get()
- 位置: L105-107
- 役割: ID と args の組み合わせに対応するキャッシュ済みメッセージを返す。無ければ null。
- 触るとき: 文字列がポップインする(遅れて出る)原因が、キャッシュに無いことかを確かめるときに見る。
- 呼び出し先: `this.#argsKey()`, `this.#messagesByArgsById.get()`, `this.#messagesByArgsById.get(id)?.get()`

## L10nCache.add()
- 位置: async L120-142
- 役割: formatMessages で文字列を取得し、値と属性(name と value の配列を辞書へ変換)を #update でキャッシュに入れる。結果が無ければ console.error を出して終わる。
- 触るとき: 新しい文字列をキャッシュ対象にするとき、または formatMessages が想定外の値を返す問題を調べるときに見る。
- 呼び出し先: `this.#update()`, `this.l10n.formatMessages()`
- 条件付き依存: `if (!messages?.[0])` → `console.error()`
- 条件付き依存: `if (messages[0].attributes)` → `messages[0].attributes.reduce()`
- 参照: `a.name`, `a.value`, `message.attributes`, `messages[0].attributes`, `messages[0].value`

## L10nCache.ensure()
- 位置: async L157-164
- 役割: キャッシュにあれば最も新しい位置へ移し、無ければ add で取得する。
- 触るとき: 同じ文字列を繰り返し使う箇所で、Fluent への問い合わせを増やしたくないときに見る。
- 呼び出し先: `this.get()`
- 条件付き依存: `if (message)` → `this.#update()`
- 条件付き依存: `if (!(message))` → `this.add()`

## L10nCache.ensureAll()
- 位置: async L172-178
- 役割: 渡された複数の要素について ensure を並行に呼び、全部終わるまで待つ。
- 触るとき: 起動時などにまとめて文字列を温めたいときに見る。
- 呼び出し先: `Promise.all()`, `promises.push()`, `this.ensure()`

## L10nCache.delete()
- 位置: L191-199
- 役割: 指定の ID と args のキャッシュ項目を削除する。ID の項目が空になれば ID ごと削除する。
- 触るとき: 特定の文字列だけ古いキャッシュを捨てたいときに見る。
- 呼び出し先: `this.#messagesByArgsById.get()`
- 条件付き依存: `if (messagesByArgs)` → `messagesByArgs.delete()`
- 条件付き依存: `if (messagesByArgs)` → `this.#argsKey()`
- 条件付き依存: `if (!messagesByArgs.size)` → `this.#messagesByArgsById.delete()`
- 参照: `messagesByArgs.size`

## L10nCache.clear()
- 位置: L204-206
- 役割: 全ての ID のキャッシュを空にする。
- 触るとき: ロケールの変更などで全キャッシュを作り直す必要があるときに見る。
- 呼び出し先: `this.#messagesByArgsById.clear()`

## L10nCache.size()
- 位置: L211-215
- 役割: 全 ID の合計キャッシュ件数を返す。
- 触るとき: キャッシュがどれだけ溜まっているかをテストや計測で確かめるときに見る。
- 呼び出し先: `this.#messagesByArgsById .values()`, `this.#messagesByArgsById .values() .reduce()`
- 参照: `messagesByArg.size`

## L10nCache.setElementL10n()
- 位置: L259-330
- 役割: キャッシュにあれば同期的に要素の属性と本文を設定する。無ければ document.l10n.setAttributes で非同期に設定する。parseMarkup のときは許可したタグだけ setHTML で入れる。最後に ensure で次回のためにキャッシュする。
- 触るとき: 要素の文字列がポップインする、または markup が想定どおりに入らないときに見る。argsHighlights による強調もここで扱う。
- 呼び出し先: `element.ownerDocument.l10n.setAttributes()`, `this.ensure()`, `this.get()`
- 条件付き依存: `if (message.attributes)` → `Object.entries()`
- 条件付き依存: `if (message.attributes)` → `element.setAttribute()`
- 条件付き依存: `if (!(!parseMarkup))` → `element.setHTML()`
- 条件付き依存: `if (!message && !attribute && argsHighlights)` → `element.ownerDocument.createElement()`
- 条件付き依存: `if (!message && !attribute && argsHighlights)` → `UrlbarShared.addTextContentWithHighlights()`
- 条件付き依存: `if (attribute)` → `element.setAttribute()`
- 条件付き依存: `if (!(attribute))` → `element.removeAttribute()`
- 参照: `element.textContent`, `message.attributes`, `message.value`, `span.innerHTML`

## L10nCache.removeElementL10n()
- 位置: L342-351
- 役割: setElementL10n で設定した本文または属性と、data-l10n-id と data-l10n-args を取り除く。
- 触るとき: 要素を再利用する前に、前回の文字列が残らないようにしたいときに見る。
- 呼び出し先: `element.removeAttribute()`
- 条件付き依存: `if (attribute)` → `element.removeAttribute()`
- 参照: `element.textContent`

## L10nCache.#update()
- 位置: L384-409
- 役割: ID ごとの Map で該当 args の項目を最新位置へ入れ直す。件数が MAX_ENTRIES_PER_ID に達していれば最も古い項目を捨てる。
- 触るとき: キャッシュの追い出し方や保持件数(既定 5)を変えるときに見る。
- 呼び出し先: `messagesByArgs.delete()`, `messagesByArgs.set()`, `this.#argsKey()`, `this.#messagesByArgsById.get()`
- 条件付き依存: `if (!messagesByArgs)` → `this.#messagesByArgsById.set()`
- 条件付き依存: `if (messagesByArgs.size == this.#maxEntriesPerId)` → `messagesByArgs.delete()`
- 条件付き依存: `if (messagesByArgs.size == this.#maxEntriesPerId)` → `messagesByArgs.keys().next()`
- 条件付き依存: `if (messagesByArgs.size == this.#maxEntriesPerId)` → `messagesByArgs.keys()`
- 参照: `messagesByArgs.keys().next().value`, `messagesByArgs.size`, `this.#maxEntriesPerId`

## L10nCache.#argsKey()
- 位置: L420-429
- 役割: args の値を key 順に並べて JSON 化し、キャッシュ用のキーを作る。
- 触るとき: 引数の違いで別の文字列として扱われない、または同じ文字列が重複して入るときに見る。
- 呼び出し先: `JSON.stringify()`, `Object.entries()`, `Object.entries(args ?? []) .sort()`, `Object.entries(args ?? []) .sort(([key1], [key2]) => key1.localeCompare(key2)) .map()`, `key1.localeCompare()`
