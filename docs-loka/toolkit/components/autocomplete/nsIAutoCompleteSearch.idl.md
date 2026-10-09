# nsIAutoCompleteSearch (toolkit/components/autocomplete/nsIAutoCompleteSearch.idl)

source: toolkit/components/autocomplete/nsIAutoCompleteSearch.idl
source-hash: ca41be4a3622b4a6d065b6210e065a1f202978b5

- 継承: nsISupports
- 役割: オートコンプリートの検索プロバイダが実装する、検索の開始と停止を行うインターフェース。
- 実装: (未記入)

## メソッド / 属性
- `void startSearch(AString searchString, AString searchParam, nsIAutoCompleteResult previousResult, nsIAutoCompleteObserver listener)`: 検索文字列で検索を開始し、結果を同期または非同期に listener へ通知する (searchParam は追加パラメータ、previousResult は高速化に使う前回の結果)。
- `void stopSearch()`: 進行中のすべての検索を停止する。

# nsIAutoCompleteObserver (toolkit/components/autocomplete/nsIAutoCompleteSearch.idl)

source: toolkit/components/autocomplete/nsIAutoCompleteSearch.idl
source-hash: ca41be4a3622b4a6d065b6210e065a1f202978b5

- 継承: nsISupports
- 役割: オートコンプリート検索が完了して結果が用意できたときに通知を受けるリスナー。
- 実装: `nsAutoCompleteController` (toolkit/components/autocomplete/nsAutoCompleteController.cpp)

## メソッド / 属性
- `void onSearchResult(nsIAutoCompleteSearch search, nsIAutoCompleteResult result)`: 検索が完了して結果が用意できたときに呼ばれる (search は検索を処理したオブジェクト、result は検索結果)。
