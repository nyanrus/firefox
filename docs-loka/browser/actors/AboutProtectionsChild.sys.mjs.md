# browser/actors/AboutProtectionsChild.sys.mjs

source: browser/actors/AboutProtectionsChild.sys.mjs
source-hash: 72380186712bbcdee2cd3745c5edf7ef456fb61a
lines: 18

## <module>
- 役割: about:protections のコンテンツ側アクター。ページから Glean イベントを記録できるように関数を公開する。

## AboutProtectionsChild.actorCreated()
- 位置: L8-12
- 役割: RPMRecordGleanEvent をページ側の window へ exportFunctions で登録する。
- 触るとき: about:protections のページから呼べる関数を追加・変更するときに見る。
- 呼び出し先: `super.actorCreated()`, `this.exportFunctions()`

## AboutProtectionsChild.RPMRecordGleanEvent()
- 位置: L14-16
- 役割: カテゴリ名と指標名で Glean の指標を引き、存在すれば extra 付きで record する。
- 触るとき: 保護画面の計測イベントが記録されない、またはカテゴリ名の打ち間違いを調べるときに見る。
- 呼び出し先: `Glean[category]?.[name]?.record()`
