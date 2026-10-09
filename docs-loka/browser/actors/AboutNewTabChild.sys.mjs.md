# browser/actors/AboutNewTabChild.sys.mjs

source: browser/actors/AboutNewTabChild.sys.mjs
source-hash: 88149c9a741557a58d8799cf5521531e108e09ca
lines: 178

## <module>
- 役割: about:newtab のコンテンツ側アクター。ページの初期化、描画用スクリプトの注入、可視状態に応じた通知と Nimbus の露出記録を担う。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `XPCOMUtils.defineLazyPreferenceGetter()`

## AboutNewTabChild.handleEvent()
- 位置: async L40-160
- 役割: DOM イベント（挿入・load・DOMContentLoaded・unload・可視性変化）ごとに親へ Init/Load/Unload/AboutNewTabVisible を送り、リモートレンダラー有効時はスタイルとスクリプトを読み込む。
- 触るとき: newtab の起動順序、レンダラー切り替え、ページ表示時の露出イベントや親への通知タイミングを変えるときに見る。
- 条件付き依存: `if (event.type == "DOMDocElementInserted")` → `this.sendAsyncMessage()`
- 条件付き依存: `if (event.type == "DOMDocElementInserted")` → `this.contentWindow.document.documentURI.replace()`
- 条件付き依存: `if (lazy.NEWTAB_REMOTE_RENDERER_ENABLED)` → `Cu.waiveXrays()`
- 条件付き依存: `if (event.type == "load")` → `this.sendAsyncMessage()`
- 条件付き依存: `if (lazy.NEWTAB_REMOTE_RENDERER_ENABLED)` → `this.sendQuery()`
- 条件付き依存: `if (lazy.NEWTAB_REMOTE_RENDERER_ENABLED)` → `document.createDocumentFragment()`
- 条件付き依存: `if (lazy.NEWTAB_REMOTE_RENDERER_ENABLED)` → `document.createElement()`
- 条件付き依存: `if (lazy.NEWTAB_REMOTE_RENDERER_ENABLED)` → `frag.appendChild()`
- 条件付き依存: `if (lazy.NEWTAB_REMOTE_RENDERER_ENABLED)` → `scriptTag.addEventListener()`
- 条件付き依存: `if (lazy.NEWTAB_REMOTE_RENDERER_ENABLED)` → `Cu.cloneInto()`
- 条件付き依存: `if (lazy.NEWTAB_REMOTE_RENDERER_ENABLED)` → `this.contentWindow.dispatchEvent()`
- 条件付き依存: `if (lazy.NEWTAB_REMOTE_RENDERER_ENABLED)` → `document.head.appendChild()`
- 条件付き依存: `if (!lazy.NEWTAB_SELF_LOADING)` → `Services.scriptloader.loadSubScriptWithOptions()`
- 条件付き依存: `if (event.type == "unload")` → `this.sendAsyncMessage()`
- 条件付き依存: `if (!(this.document.visibilityState != "visible"))` → `PrivateBrowsingUtils.isContentWindowPrivate()`
- 条件付き依存: `if ( !contentWindowPrivate || (contentWindowPrivate && PrivateBrowsingUtils.permanentPrivateBrowsing) )` → `this.sendAsyncMessage()`
- 条件付き依存: `if ( !contentWindowPrivate || (contentWindowPrivate && PrivateBrowsingUtils.permanentPrivateBrowsing) )` → `lazy.NimbusFeatures.newtab.recordExposureEvent()`
- 参照: `AppConstants.RELEASE_OR_BETA`, `Ci.imgIContainer.kDontAnimMode`, `Ci.imgIContainer.kNormalAnimMode`, `PrivateBrowsingUtils.permanentPrivateBrowsing`, `Services.appinfo.processID`, `event.type`, `lazy.ACTIVITY_STREAM_DEBUG`, `lazy.NEWTAB_REMOTE_RENDERER_ENABLED`, `lazy.NEWTAB_SELF_LOADING`, `scriptTag.src`, `styleTag.href`, `styleTag.rel`, `this.contentWindow`, `this.contentWindow.CustomEvent`, `this.contentWindow.document.body.firstElementChild`, `this.contentWindow.windowUtils.imageAnimationMode`, `this.document.visibilityState`, `xrayedWin.__APP_PROPS__`, `xrayedWin.__REMOTE_RENDERER__`
- XPCOM: `Services.appinfo` / `Services.scriptloader`

## AboutNewTabChild.observe()
- 位置: L162-176
- 役割: intl:l10n-sources-changed を受けて newtab の DOM を再翻訳させる（Bug 2046945 の暫定対応）。
- 触るとき: newtab の翻訳やローカライズソースの更新反映に問題が出たときに見る。
- 呼び出し先: `doc.l10n.translateRoots()`
- 参照: `doc?.l10n`, `this.document`
