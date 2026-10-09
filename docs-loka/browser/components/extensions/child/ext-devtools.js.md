# browser/components/extensions/child/ext-devtools.js

source: browser/components/extensions/child/ext-devtools.js
source-hash: afd95cf92459d075e4f6df08642a6c253f7eb4c9
lines: 14

## <module>
- 役割: devtools 名前空間の子側 API の土台を定義する。中身は空で、個別の機能は ext-devtools-* の子モジュールが足す。

## getAPI()
- 位置: L8-12
- 役割: devtools 名前空間の空のオブジェクトを返す。
- 触るとき: devtools 名前空間に共通の要素を足すとき。
