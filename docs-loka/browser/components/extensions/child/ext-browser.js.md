# browser/components/extensions/child/ext-browser.js

source: browser/components/extensions/child/ext-browser.js
source-hash: 790b2d4bd0a4f20d4c1cb60079beb1a47bcac0c5
lines: 50

## <module>
- 役割: 拡張機能の子プロセスで使う API の子モジュールを登録する。devtools 系、menus、omnibox、tabs を、対応する名前空間とスコープに割り当てる。
- 呼び出し先: `extensions.registerModules()`
