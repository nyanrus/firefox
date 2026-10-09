# browser/components/urlbar/SmartbarMentionsPanelSearch.sys.mjs

source: browser/components/urlbar/SmartbarMentionsPanelSearch.sys.mjs
source-hash: b8b9a1deb627502a16735575815e88d565cd56bf
lines: 218

## <module>
- 役割: スマートバーのメンションパネル用に、開いているタブと最近閉じたタブを検索する SmartbarMentionsPanelSearch を定義するモジュール。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## isExcludedMentionUrl()
- 位置: L37-47
- 役割: 空の URL、初期ページ、about:aichatcontent を候補から除外すべきかを判定する。URL が解析できなければ除外しない。
- 触るとき: メンション候補に出てほしくないページが出る、または出るべきページが消えるとき。
- 呼び出し先: `ADDITIONAL_EXCLUDED_MENTION_URLS.has()`, `Services.io.newURI()`, `browserWindow.isInitialPage()`
- XPCOM: `Services.io`

## SmartbarMentionsPanelSearch.constructor()
- 位置: L78-81
- 役割: ウィンドウを保持し、開いているタブと最近閉じたタブの一覧を作る。
- 触るとき: メンション候補の元データがいつ読まれるか(生成時点で固定されるか)を確かめるとき。
- 呼び出し先: `this.#getOpenAndClosedTabs()`
- 参照: `this.#browserWindow`, `this.#tabs`

## SmartbarMentionsPanelSearch.startQuery()
- 位置: L89-93
- 役割: 入力で絞り込んだタブを最終アクセス時刻の新しい順に並べて返す。
- 触るとき: メンション候補の並び順を変えたいとき、入力に対する絞り込み結果を確かめるとき。
- 呼び出し先: `this.#filterTabs()`, `this.#filterTabs(searchString).sort()`
- 参照: `a.timestamp`, `b.timestamp`

## SmartbarMentionsPanelSearch.getTabGroups()
- 位置: L102-106
- 役割: ウィンドウ内のタブグループを TabManagementService から読み取り専用で返す。
- 触るとき: メンションパネルにタブグループを出す、または空のグループを消す条件を調べるとき。
- 呼び出し先: `lazy.tabManagementService.getTabGroups()`
- 参照: `this.#browserWindow`

## SmartbarMentionsPanelSearch.#filterTabs()
- 位置: L108-141
- 役割: 入力を最大長で切り詰めてトークン化し、タイトルと正規化した URL を連結した文字列に全トークンが含まれるタブだけを残す。
- 触るとき: 入力に対して候補が思わぬ形で消える、あるいは一致判定の対象文字列を変えたいとき。
- 呼び出し先: ``${tab.title} ${normalizedUrl}` .substring()`, ``${tab.title} ${normalizedUrl}` .substring(0, lazy.UrlbarShared.MAX_TEXT_LENGTH) .toLowerCase()`, `lazy.UrlbarTokenizer.tokenize()`, `searchString.substring()`, `searchText.includes()`, `this.#normalizeUrl()`, `this.#tabs.filter()`, `token.value.toLowerCase()`, `tokens.every()`, `truncatedSearch.trim()`
- 参照: `lazy.UrlbarShared.MAX_TEXT_LENGTH`, `tab.title`, `tab.url`, `this.#tabs`, `tokens.length`

## SmartbarMentionsPanelSearch.#getOpenAndClosedTabs()
- 位置: L143-201
- 役割: 開いているタブを gBrowser から、最近閉じたタブを SessionStore から集め、除外対象を外して種別付きの一覧にする。閉じたタブの読み取りで例外が出ても console.error に記録して続ける。
- 触るとき: タブの取得元、タイトルや画像(icon)の決め方、閉じたタブの扱いを変えるとき、候補が欠けるときの原因を探すとき。
- 呼び出し先: `console.error()`, `isExcludedMentionUrl()`, `lazy.SessionStore.getClosedTabDataForWindow()`, `lazy.UrlbarShared.getIconForUrl()`, `results.push()`, `tab.image.startsWith()`
- 参照: `MENTION_TYPE.TAB_OPEN`, `MENTION_TYPE.TAB_RECENTLY_CLOSED`, `browserWindow.gBrowser.tabs`, `closedTab.closedAt`, `closedTab.state`, `entry.title`, `entry.url`, `state.entries`, `state.entries.length`, `state.index`, `tab.image`, `tab.label`, `tab.lastAccessed`, `tab.linkedBrowser?.currentURI?.spec`

## SmartbarMentionsPanelSearch.#normalizeUrl()
- 位置: L203-216
- 役割: http/https の接頭辞やスラッシュ、空のクエリ・ハッシュを取り除いた形の URL を返す。失敗したら元の URL を返す。
- 触るとき: URL の一致判定で http と https の違いや末尾のスラッシュで候補が漏れるとき、正規化の規則を変えたいとき。
- 呼び出し先: `lazy.UrlbarShared.stripPrefixAndTrim()`
