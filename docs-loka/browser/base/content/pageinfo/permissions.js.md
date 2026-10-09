# browser/base/content/pageinfo/permissions.js

source: browser/base/content/pageinfo/permissions.js
source-hash: a4a5bd39ce8645e35bef5f87d88516f146942e59
lines: 246

## <module>
- 役割: ページ情報ダイアログの「権限」タブを作るスクリプト。SitePermissions から表示対象の権限を表示名順に集め、サイトごとの権限行を生成・更新する。
- 呼び出し先: `ChromeUtils.importESModule()`, `EXCLUDE_PERMS.includes()`, `SitePermissions.getPermissionLabel()`, `SitePermissions.listPermissions()`, `SitePermissions.listPermissions() .filter()`, `firstLabel.localeCompare()`

## observe()
- 位置: L31-41
- 役割: perm-changed 通知を受け、変更された権限が現在のページのプリンシパルに当たり表示対象なら、その行を initRow で更新する。
- 触るとき: 権限を別タブや設定画面で変えたときにページ情報の表示が追従しない場合を調べるとき。
- 条件付き依存: `if (aTopic == "perm-changed")` → `aSubject.QueryInterface()`
- 条件付き依存: `if (aTopic == "perm-changed")` → `permission.matches()`
- 条件付き依存: `if (aTopic == "perm-changed")` → `gPermissions.includes()`
- 条件付き依存: `if ( permission.matches(gPermPrincipal, true) && gPermissions.includes(permission.type) )` → `initRow()`
- 参照: `Ci.nsIPermission`, `permission.type`
- XPCOM: [`nsIPermission`](../../../../netwerk/base/nsIPermission.idl.md)

## getExcludedPermissions()
- 位置: L44-46
- 役割: 権限タブに表示しない権限ID(EXCLUDE_PERMS)の配列をそのまま返す。
- 触るとき: 権限タブに出さない権限を増減させるとき、または除外対象の確認をするとき。

## onLoadPermission()
- 位置: L48-64
- 役割: 対応プリンシパルなら、ホスト名を表示し全権限の行を作って perm-changed を監視し、権限タブを表示する。非対応なら権限タブを隠す。
- 触るとき: ページ情報を開いたときに権限タブが出る条件や、初期表示の内容を変えるとき。
- 呼び出し先: `SitePermissions.isSupportedPrincipal()`, `document.getElementById()`
- 条件付き依存: `if (SitePermissions.isSupportedPrincipal(principal))` → `document.getElementById()`
- 条件付き依存: `if (SitePermissions.isSupportedPrincipal(principal))` → `initRow()`
- 条件付き依存: `if (SitePermissions.isSupportedPrincipal(principal))` → `Services.obs.addObserver()`
- 条件付き依存: `if (SitePermissions.isSupportedPrincipal(principal))` → `window.addEventListener()`
- 参照: `hostText.value`, `permTab.hidden`, `uri.displayPrePath`
- XPCOM: `Services.obs`

## onUnloadPermission()
- 位置: L66-68
- 役割: onLoadPermission で登録した perm-changed の監視を解除する。
- 触るとき: ページ情報を閉じた後も通知を受け続けるといった監視の漏れを調べるとき。
- 呼び出し先: `Services.obs.removeObserver()`
- XPCOM: `Services.obs`

## initRow()
- 位置: L70-154
- 役割: 1つの権限行を現在の状態に合わせて更新する。既定値と比べてチェックボックスとラジオを決め、cookie は別扱いにし、ポリシーやロックされた設定は無効化する。
- 触るとき: 権限の既定値判定や、ロック・ポリシーによる無効化の条件を変えるとき、行の表示がずれるときに見る。
- 呼び出し先: `Services.policies.isAllowed()`, `Services.prefs.prefIsLocked()`, `SitePermissions.getDefault()`, `SitePermissions.getForPrincipal()`, `[SitePermissions.SCOPE_POLICY, SitePermissions.SCOPE_GLOBAL].includes()`, `createRow()`, `document.getElementById()`, `setRadioState()`
- 条件付き依存: `if (aPartId == "cookie")` → `Services.perms.testPermissionFromPrincipal()`
- 条件付き依存: `if (state == SitePermissions.UNKNOWN)` → `command.setAttribute()`
- 条件付き依存: `if (state == SitePermissions.UNKNOWN)` → `document.getElementById()`
- 条件付き依存: `if (!(state == SitePermissions.UNKNOWN))` → `command.removeAttribute()`
- 条件付き依存: `if (aPartId == "cookie")` → `setRadioState()`
- 条件付き依存: `if (aPartId == "cookie")` → `Services.prefs.prefIsLocked()`
- 条件付き依存: `if (locked)` → `command.setAttribute()`
- 条件付き依存: `if (state != defaultState)` → `command.removeAttribute()`
- 条件付き依存: `if (!(state != defaultState))` → `command.setAttribute()`
- 条件付き依存: `if ( [SitePermissions.SCOPE_POLICY, SitePermissions.SCOPE_GLOBAL].includes(scope) )` → `checkbox.setAttribute()`
- 条件付き依存: `if ( [SitePermissions.SCOPE_POLICY, SitePermissions.SCOPE_GLOBAL].includes(scope) )` → `command.setAttribute()`
- 参照: `SitePermissions.SCOPE_GLOBAL`, `SitePermissions.SCOPE_POLICY`, `SitePermissions.UNKNOWN`, `checkbox.checked`, `checkbox.disabled`, `radioGroup.selectedItem`
- XPCOM: `Services.perms` / `Services.policies` / `Services.prefs`

## createRow()
- 位置: L156-215
- 役割: 1つの権限行(コマンド、ラベル、既定値チェックボックス、状態のラジオグループ)を XUL で組み立てて permList に追加する。行が既にあれば何もしない。
- 触るとき: 権限行のUIを追加・変更するとき、またはラジオの id(権限名#状態)の規則を変えるとき。
- 呼び出し先: `SitePermissions.getAvailableStates()`, `SitePermissions.getMultichoiceStateLabel()`, `SitePermissions.getPermissionLabel()`, `checkbox.addEventListener()`, `checkbox.setAttribute()`, `command.addEventListener()`, `command.setAttribute()`, `controls.appendChild()`, `controls.setAttribute()`, `document.createXULElement()`, `document.getElementById()`, `document.getElementById("pageInfoCommandSet").appendChild()`, `document.getElementById("permList").appendChild()`, `document.l10n.setAttributes()`, `label.setAttribute()`, `onCheckboxClick()`, `onRadioClick()`, `radio.setAttribute()`, `radiogroup.appendChild()`, `radiogroup.setAttribute()`, `row.appendChild()`, `row.setAttribute()`, `spacer.setAttribute()`

## onCheckboxClick()
- 位置: L217-227
- 役割: 「既定値を使用」チェックボックスの切り替えを処理する。オンなら SitePermissions.removeFromPrincipal で個別設定を消し、オフなら onRadioClick で現在の選択を保存する。
- 触るとき: 既定値に戻す操作の挙動を変えるとき。
- 呼び出し先: `document.getElementById()`
- 条件付き依存: `if (checkbox.checked)` → `SitePermissions.removeFromPrincipal()`
- 条件付き依存: `if (checkbox.checked)` → `command.setAttribute()`
- 条件付き依存: `if (!(checkbox.checked))` → `onRadioClick()`
- 条件付き依存: `if (!(checkbox.checked))` → `command.removeAttribute()`
- 参照: `checkbox.checked`

## onRadioClick()
- 位置: L229-238
- 役割: 選択中のラジオの id から状態の数値を取り出して setForPrincipal で保存する。選択がなければ既定値を保存する。
- 触るとき: 権限を変更したときに保存される値を変えるとき、またはラジオ選択が保存に反映されない不具合を調べるとき。
- 呼び出し先: `SitePermissions.setForPrincipal()`, `document.getElementById()`
- 条件付き依存: `if (radioGroup.selectedItem)` → `parseInt()`
- 条件付き依存: `if (radioGroup.selectedItem)` → `radioGroup.selectedItem.id.split()`
- 条件付き依存: `if (!(radioGroup.selectedItem))` → `SitePermissions.getDefault()`
- 参照: `radioGroup.selectedItem`

## setRadioState()
- 位置: L240-245
- 役割: 指定された状態に対応するラジオを、そのラジオグループの選択状態にする。
- 触るとき: 保存済みの権限をページ情報の表示に反映させる処理を変えるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `radio.radioGroup.selectedItem`
