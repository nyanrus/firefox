# browser/components/storybook/.storybook/l10n-pseudo.mjs

source: browser/components/storybook/.storybook/l10n-pseudo.mjs
source-hash: c92be262e9e1625e6bda6587675b602558589e46
lines: 111

## <module>
- 役割: (未記入)
- 呼び出し先: `transformString.bind()`

## transformString()
- 位置: L62-105
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ch.charCodeAt()`, `modified.join()`, `msg.split()`, `part.replace()`, `parts.map()`, `reExcluded.test()`
- 条件付き依存: `if (cc >= 97 && cc <= 122)` → `String.fromCodePoint()`
- 条件付き依存: `if (cc >= 65 && cc <= 90)` → `String.fromCodePoint()`
- 参照: `map.caps`, `map.small`, `msg.length`
