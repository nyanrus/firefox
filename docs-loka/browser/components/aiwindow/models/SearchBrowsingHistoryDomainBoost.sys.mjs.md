# browser/components/aiwindow/models/SearchBrowsingHistoryDomainBoost.sys.mjs

source: browser/components/aiwindow/models/SearchBrowsingHistoryDomainBoost.sys.mjs
source-hash: 717a9816ee62f56c8d46f8c2d3a8ecaa34d79622
lines: 404

## <module>
- 役割: 一般的な分類の検索(ゲーム、映画、ニュースなど)で、タイトルや説明の埋め込みを補うためのドメイン絞り込みの簡易ヒューリスティック。
- 呼び出し先: `Object.freeze()`

## normalizeQuery()
- 位置: L231-237
- 役割: 文字列を小文字にし、英数字以外を空白に変えて連続する空白を 1 つにまとめる。
- 触るとき: カテゴリ語の一致判定の前処理を変えるとき。
- 呼び出し先: `(s || "") .toLowerCase()`, `(s || "") .toLowerCase() .replace()`, `(s || "") .toLowerCase() .replace(/[^\p{L}\p{N}]+/gu, " ") .replace()`, `(s || "") .toLowerCase() .replace(/[^\p{L}\p{N}]+/gu, " ") .replace(/\s+/g, " ") .trim()`

## matchDomains()
- 位置: L247-264
- 役割: 正規化したクエリがカテゴリの語句を単語境界つきで含めば、そのカテゴリのドメイン一覧を返す。どれも無ければ null。
- 触るとき: どの語でどのカテゴリに判定されるかを変えるとき、または一般カテゴリ検索が効かないとき。
- 呼び出し先: `normalizeQuery()`, `q.includes()`, `q.trim()`, `tt.trim()`
- 参照: `cat.domains`, `cat.terms`, `categoriesJson.categories`

## buildDomainUrlWhere()
- 位置: L273-297
- 役割: ドメインごとに https と www 付きの LIKE 条件を作り、OR で結んだ WHERE 句とパラメータを返す。
- 触るとき: ドメイン絞り込みの URL の形(サブドメインや経路の有無)を変えるとき。パス無しの URL が漏れる点に注意。
- 呼び出し先: `String()`, `String(raw).toLowerCase()`, `clauses.join()`, `clauses.push()`
- 参照: `clauses.length`

## searchByDomains()
- 位置: async L311-357
- 役割: 時間範囲とドメイン条件で moz_places を検索し、各行を buildHistoryRow で変換して返す。接続やドメインが無ければ空配列。
- 触るとき: カテゴリ検索の履歴取得条件(件数、時間範囲、並び順)を変えるとき。
- 呼び出し先: `Array.isArray()`, `buildDomainUrlWhere()`, `buildHistoryRow()`, `conn.executeCached()`, `rows.push()`
- 参照: `domains.length`

## mergeDedupe()
- 位置: L368-397
- 役割: primary の順を保ったまま secondary で補い、url(無ければ id)で重複を除いて limit 件まで返す。
- 触るとき: ドメイン検索と通常の履歴検索の結果をどの順で合わせるかを変えるとき。
- 呼び出し先: `keyOf()`, `seen.has()`
- 条件付き依存: `if (!seen.has(k))` → `seen.add()`
- 条件付き依存: `if (!seen.has(k))` → `out.push()`
- 参照: `out.length`

## keyOf()
- 位置: L372-372
- 役割: mergeDedupe 内の補助関数で、結果の url か id を重複判定のキーにする。
- 触るとき: 重複判定のキーを変えたいとき。
- 参照: `r?.id`, `r?.url`
