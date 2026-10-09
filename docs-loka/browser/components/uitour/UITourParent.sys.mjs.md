# browser/components/uitour/UITourParent.sys.mjs

source: browser/components/uitour/UITourParent.sys.mjs
source-hash: 61506d358db6727f32447b42580b05580ecee553
lines: 23

## <module>
- 役割: (未記入)

## UITourParent.receiveMessage()
- 位置: L9-21
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `UITourUtils.ensureTrustedOrigin()`
- 条件付き依存: `if (this.manager.rootFrameLoader)` → `UITour.onPageEvent()`
- 参照: `message.data`, `message.name`, `this.manager`, `this.manager.rootFrameLoader`, `this.manager.rootFrameLoader.ownerElement`
