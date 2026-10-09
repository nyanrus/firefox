# browser/modules/FilterAdult.sys.mjs

source: browser/modules/FilterAdult.sys.mjs
source-hash: e72ccd3f030f9c69e08c9702b51ad2e8a32a3e5e
lines: 69

## <module>
- 役割: 新規タブ等のリンクから成人向けサイトを除外するフィルターを提供する。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`

## _FilterAdult.constructor()
- 位置: L20-22
- 役割: Rust 製の判定コンポーネントを初期化して保持する。
- 触るとき: 判定に使うリストの読み込みや初期化の順序を変えるとき。
- 呼び出し先: `FilterAdultComponent.init()`
- 参照: `this.#comp`

## _FilterAdult.filter()
- 位置: L32-45
- 役割: リンク配列から成人向けベースドメインのリンクを除いた配列を返す。
- 触るとき: 新規タブのリンク一覧で成人向けサイトが混ざる、または消えすぎる報告を調べるとき。機能が無効ならそのまま返す。URL が解析できないリンクは残す。
- 呼び出し先: `Services.eTLD.getBaseDomain()`, `Services.io.newURI()`, `links.filter()`, `this.#comp.contains()`
- 参照: `lazy.gFilterAdultEnabled`
- XPCOM: `Services.eTLD` / `Services.io`

## _FilterAdult.isAdultUrl()
- 位置: L55-65
- 役割: 単一 URL のベースドメインが成人向けかを真偽値で返す。
- 触るとき: 個々の URL を成人向けとして扱うか判断する箇所の挙動を確かめるとき。無効時と解析失敗時は false を返す。
- 呼び出し先: `Services.eTLD.getBaseDomain()`, `Services.io.newURI()`, `this.#comp.contains()`
- 参照: `lazy.gFilterAdultEnabled`
- XPCOM: `Services.eTLD` / `Services.io`
