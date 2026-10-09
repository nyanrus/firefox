# browser/components/urlbar/UrlbarNewTabComponentRegistrant.sys.mjs

source: browser/components/urlbar/UrlbarNewTabComponentRegistrant.sys.mjs
source-hash: a60c6e5fc8f3bd39fba3b1ffd72a6010c4e426ad
lines: 86

## <module>
- 役割: newtabFeatureGate が有効なとき、about:newtab / about:home に <moz-urlbar> を載せる New Tab コンポーネントの登録を担うモジュール。

## UrlbarNewTabComponentRegistrant.constructor()
- 位置: L22-27
- 役割: UrlbarPrefs に自身をオブザーバーとして登録する。
- 触るとき: New Tab 側の登録が消えて urlbar が出なくなったとき、オブザーバーの寿命(弱参照で保持される点)を確かめるとき。
- 呼び出し先: `UrlbarPrefs.addObserver()`, `super()`

## UrlbarNewTabComponentRegistrant.destroy()
- 位置: L29-31
- 役割: UrlbarPrefs からオブザーバーの登録を外す。
- 触るとき: 登録解除の後に Nimbus や pref の通知が届き続けていないかを調べるとき。
- 呼び出し先: `UrlbarPrefs.removeObserver()`

## UrlbarNewTabComponentRegistrant.onNimbusChanged()
- 位置: L33-41
- 役割: newtabFeatureGate、newtabVariantA、newtabVariantB のいずれかが変わったときに updated() で再描画を促す。
- 触るとき: Nimbus の実験値を変えても New Tab の urlbar が切り替わらないとき。
- 条件付き依存: `if ( variable == FEATURE_GATE || variable == VARIANT_A || variable == VARIANT_B )` → `this.updated()`

## UrlbarNewTabComponentRegistrant.onPrefChanged()
- 位置: L43-47
- 役割: browser.nova.enabled が変わったときに updated() で再描画を促す。
- 触るとき: Nova の有効・無効を切り替えても New Tab の表示が追従しないとき。
- 条件付き依存: `if (pref == NOVA_PREF)` → `this.updated()`

## UrlbarNewTabComponentRegistrant.getComponents()
- 位置: L49-84
- 役割: feature gate が無効なら空を返す。有効なら variant-b、無ければ variant-a の属性を付けた moz-urlbar のコンポーネント定義を1件返す。
- 触るとき: New Tab に載せる urlbar の属性(sap-name、variant 属性、読み込む ftl や css)を変えるとき、ゲートの条件を確かめるとき。
- 呼び出し先: `UrlbarPrefs.get()`
- 条件付き依存: `if (!(UrlbarPrefs.get(VARIANT_B)))` → `UrlbarPrefs.get()`
- 参照: `AboutNewTabComponentRegistry.TYPES.SEARCH`
