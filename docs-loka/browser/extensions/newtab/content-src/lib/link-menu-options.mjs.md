# browser/extensions/newtab/content-src/lib/link-menu-options.mjs

source: browser/extensions/newtab/content-src/lib/link-menu-options.mjs
source-hash: e453805c799de829f928750d441b83106092a3ec
lines: 628

## <module>
- 役割: (未記入)

## _OpenInPrivateWindow()
- 位置: L10-22
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToMain()`
- 参照: `at.OPEN_PRIVATE_WINDOW`, `site.referrer`, `site.url`

## Separator()
- 位置: L30-30
- 役割: (未記入)
- 触るとき: (未記入)

## EmptyItem()
- 位置: L31-31
- 役割: (未記入)
- 触るとき: (未記入)

## ShowPrivacyInfo()
- 位置: L32-39
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `at.SHOW_PRIVACY_INFO`

## AboutSponsored()
- 位置: L40-53
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(site.label || site.hostname).toLocaleLowerCase()`, `ac.AlsoToMain()`
- 参照: `at.ABOUT_SPONSORED_TOP_SITES`, `site.block_key`, `site.hostname`, `site.label`, `site.sponsored_position`, `site.sponsored_tile_id`

## RemoveBookmark()
- 位置: L54-62
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.AlsoToMain()`
- 参照: `at.DELETE_BOOKMARK_BY_ID`, `site.bookmarkGuid`

## AddBookmark()
- 位置: L63-71
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.AlsoToMain()`
- 参照: `at.BOOKMARK_URL`, `site.title`, `site.type`, `site.url`

## OpenInNewWindow()
- 位置: L72-103
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.AlsoToMain()`
- 参照: `at.OPEN_NEW_WINDOW`, `site.card_type`, `site.corpus_item_id`, `site.flight_id`, `site.format`, `site.is_section_followed`, `site.received_rank`, `site.recommended_at`, `site.referrer`, `site.scheduled_corpus_item_id`, `site.section`, `site.section_position`, `site.sponsored_tile_id`, `site.tile_id`, `site.topic`, `site.type`, `site.typedBonus`, `site.url`

## BlockUrl()
- 位置: L109-111
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LinkMenuOptions.BlockUrls()`

## BlockUrls()
- 位置: L113-158
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `( site.label || site.hostname )?.toLocaleLowerCase()`, `ac.AlsoToMain()`, `tiles.map()`
- 参照: `at.BLOCK_URL`, `site.block_key`, `site.card_type`, `site.corpus_item_id`, `site.flight_id`, `site.format`, `site.hostname`, `site.is_section_followed`, `site.label`, `site.open_url`, `site.original_url`, `site.pocket_id`, `site.received_rank`, `site.recommended_at`, `site.scheduled_corpus_item_id`, `site.section`, `site.section_position`, `site.shim`, `site.shim.delete`, `site.sponsored_position`, `site.sponsored_tile_id`, `site.tile_id`, `site.type`, `site.url`

## BlockAdUrl()
- 位置: L161-169
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.AlsoToMain()`
- 参照: `at.BLOCK_URL`

## WebExtDismiss()
- 位置: L173-182
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.WebExtEvent()`
- 参照: `at.WEBEXT_DISMISS`, `site.url`

## DeleteUrl()
- 位置: L183-223
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Object.assign()`, `ac.AlsoToMain()`, `ac.UserEvent()`
- 参照: `at.DELETE_HISTORY_URL`, `at.DIALOG_CLOSE`, `at.DIALOG_OPEN`, `site.bookmarkGuid`, `site.original_url`, `site.pocket_id`, `site.url`

## ShowFile()
- 位置: L224-231
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToMain()`
- 参照: `at.SHOW_DOWNLOAD_FILE`, `site.url`

## OpenFile()
- 位置: L232-239
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToMain()`
- 参照: `at.OPEN_DOWNLOAD_FILE`, `site.url`

## CopyDownloadLink()
- 位置: L240-247
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToMain()`
- 参照: `at.COPY_DOWNLOAD_LINK`, `site.url`

## GoToDownloadPage()
- 位置: L248-256
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToMain()`
- 参照: `at.OPEN_LINK`, `site.referrer`

## RemoveDownload()
- 位置: L257-264
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToMain()`
- 参照: `at.REMOVE_DOWNLOAD_FILE`, `site.url`

## PinTopSite()
- 位置: L265-276
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.AlsoToMain()`
- 参照: `at.TOP_SITES_PIN`

## UnpinTopSite()
- 位置: L277-285
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.AlsoToMain()`
- 参照: `at.TOP_SITES_UNPIN`, `site.url`

## EditTopSite()
- 位置: L286-294
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `at.TOP_SITES_EDIT`

## AddTopSite()
- 位置: L297-304
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `at.TOP_SITES_EDIT`

## CheckBookmark()
- 位置: L305-308
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LinkMenuOptions.AddBookmark()`, `LinkMenuOptions.RemoveBookmark()`
- 参照: `site.bookmarkGuid`

## CheckPinTopSite()
- 位置: L309-312
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LinkMenuOptions.PinTopSite()`, `LinkMenuOptions.UnpinTopSite()`
- 参照: `site.isPinned`

## OpenInPrivateWindow()
- 位置: L313-314
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LinkMenuOptions.EmptyItem()`, `_OpenInPrivateWindow()`

## SectionBlock()
- 位置: L315-383
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.AlsoToMain()`, `ac.OnlyToMain()`, `ac.OnlyToOneContent()`
- 参照: `at.BLOCK_SECTION`, `at.DIALOG_CLOSE`, `at.DIALOG_OPEN`, `at.SECTION_PERSONALIZATION_SET`, `at.SHOW_TOAST_MESSAGE`

## SectionUnfollow()
- 位置: L384-417
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(({ [sectionKey]: _sectionKey, ...remaining }) => remaining)()`, `ac.AlsoToMain()`, `ac.OnlyToMain()`, `ac.OnlyToOneContent()`
- 参照: `at.SECTION_PERSONALIZATION_SET`, `at.SHOW_TOAST_MESSAGE`, `at.UNFOLLOW_SECTION`

## ManageSponsoredContent()
- 位置: L418-422
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToMain()`
- 参照: `at.SETTINGS_OPEN`

## SectionLearnMore()
- 位置: L423-434
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToMain()`
- 参照: `at.CLICK_SECTION_LEARN_MORE`, `at.OPEN_LINK`

## OurSponsorsAndYourPrivacy()
- 位置: L436-453
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.OnlyToMain()`
- 参照: `at.OPEN_LINK`

## ReportAd()
- 位置: L454-467
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.AlsoToMain()`
- 参照: `at.REPORT_AD_OPEN`, `site.card_type`, `site.position`, `site.shim?.report`, `site.url`

## ReportContent()
- 位置: L469-486
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ac.AlsoToMain()`
- 参照: `at.REPORT_CONTENT_OPEN`, `site.card_type`, `site.corpus_item_id`, `site.scheduled_corpus_item_id`, `site.section`, `site.section_position`, `site.title`, `site.topic`, `site.url`

## getLinkMenuOptions()
- 位置: L506-627
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `LinkMenuOptions[o]()`, `propOptions .map()`
- 参照: `ac.UserEvent`, `linkMenuOptions.length`, `linkMenuOptions[0].first`, `linkMenuOptions[linkMenuOptions.length - 1].last`, `option.onClick`, `site.isDefault`, `site.searchTopSite`, `site.sponsored_position`

## option.onClick()
- 位置: L549-616
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `dispatch()`
- 条件付き依存: `if (ctrlKey || metaKey || shiftKey || button === 1)` → `Object.assign()`
- 条件付き依存: `if (toast)` → `dispatch()`
- 条件付き依存: `if (eventName)` → `Object.assign()`
- 条件付き依存: `if (eventName)` → `dispatch()`
- 条件付き依存: `if (eventName)` → `userEvent()`
- 条件付き依存: `if (impression && shouldSendImpressionStats)` → `dispatch()`
- 参照: `action.data`, `action.type`, `site.flight_id`
