# browser/components/profiles/content/profile-card.mjs

source: browser/components/profiles/content/profile-card.mjs
source-hash: b219d565bb93ee2177945e58b91e431c5089dca5
lines: 197

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.importESModule()`, `customElements.define()`

## ProfileCard.firstUpdated()
- 位置: L37-42
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super.firstUpdated()`, `this.setAvatarImage()`, `this.setBackgroundImage()`

## ProfileCard.setBackgroundImage()
- 位置: L44-51
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `this.backgroundImage.style.backgroundImage`, `this.backgroundImage.style.fill`, `this.backgroundImage.style.stroke`, `this.profile.id`, `this.profile.theme`

## ProfileCard.setAvatarImage()
- 位置: async L53-58
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.profile.getAvatarURL()`
- 参照: `this.avatarImage.style.backgroundImage`, `this.avatarImage.style.fill`, `this.avatarImage.style.stroke`, `this.profile.theme`

## ProfileCard.launchProfile()
- 位置: L60-68
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`
- 参照: `this.profile`

## ProfileCard.click()
- 位置: L70-72
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleClick()`

## ProfileCard.handleClick()
- 位置: L74-76
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.launchProfile()`

## ProfileCard.handleKeyDown()
- 位置: L78-85
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( event.target === this.profileCard && (event.code === "Enter" || event.code === "Space") )` → `this.launchProfile()`
- 参照: `event.code`, `event.target`, `this.profileCard`

## ProfileCard.handleEditClick()
- 位置: L87-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `this.launchProfile()`

## ProfileCard.handleDeleteClick()
- 位置: L92-101
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `event.stopPropagation()`, `this.dispatchEvent()`
- 参照: `this.profile`

## ProfileCard.render()
- 位置: L103-141
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `html()`
- 参照: `this.handleClick`, `this.handleDeleteClick`, `this.handleEditClick`, `this.handleKeyDown`, `this.profile.name`

## NewProfileCard.createProfile()
- 位置: L150-157
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.dispatchEvent()`

## NewProfileCard.click()
- 位置: L159-161
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.handleClick()`

## NewProfileCard.handleClick()
- 位置: L163-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.createProfile()`

## NewProfileCard.handleKeyDown()
- 位置: L167-171
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (event.code === "Enter" || event.code === "Space")` → `this.createProfile()`
- 参照: `event.code`

## NewProfileCard.render()
- 位置: L173-193
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `html()`
- 参照: `this.handleClick`, `this.handleKeyDown`
