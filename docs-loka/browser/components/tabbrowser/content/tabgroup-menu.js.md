# browser/components/tabbrowser/content/tabgroup-menu.js

source: browser/components/tabbrowser/content/tabgroup-menu.js
source-hash: 1902d2d40887aba210d5abc1b8bd1c3326bb561f
lines: 1549

## <module>
- 役割: タブグループの作成・編集パネルを担う tabgroup-menu カスタム要素を、スクリプトの globals を漏らさないブロック内で定義する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `ChromeUtils.importESModule()`, `customElements.define()`

## MozTabbrowserTabGroupMenu.constructor()
- 位置: L362-402
- 役割: スマートタブグループ関連の pref を遅延取得として登録し、変更時にハンドラを呼ぶ。
- 触るとき: スマート機能の pref を追加・変更するとき。
- 呼び出し先: `XPCOMUtils.defineLazyPreferenceGetter()`, `super()`, `this.#onSmartTabGroupsOptInPrefChange.bind()`, `this.#onSmartTabGroupsPrefChange.bind()`

## MozTabbrowserTabGroupMenu.connectedCallback()
- 位置: L404-562
- 役割: テンプレートを挿入して各要素を取得し、ボタンのコマンドとパネルのイベントを結線する(初回のみ)。
- 触るとき: パネルのボタン動作や初期化処理を変えるとき。
- 呼び出し先: `ContentSharingUtils.handleShareTabGroup()`, `Glean.tabgroup.groupInteractions.copy_all_links.add()`, `Glean.tabgroup.smartTabEnabled.set()`, `TabMetrics.userTriggeredContext()`, `document.getElementById()`, `gBrowser.TabMetrics.userTriggeredContext()`, `gBrowser.removeTabGroup()`, `gBrowser.replaceGroupWithWindow()`, `lazy.AIWindow.createAITab()`, `this.#cancelButton.addEventListener()`, `this.#commandButtons.addNewTabInGroup.addEventListener()`, `this.#commandButtons.copyAllLinks.addEventListener()`, `this.#commandButtons.createAITab.addEventListener()`, `this.#commandButtons.deleteGroup.addEventListener()`, `this.#commandButtons.moveGroupToNewWindow.addEventListener()`, `this.#commandButtons.saveAndCloseGroup.addEventListener()`, `this.#commandButtons.shareTabGroup.addEventListener()`, `this.#commandButtons.ungroupTabs.addEventListener()`, `this.#createButton.addEventListener()`, `this.#getGroupLinks()`, `this.#handleMlTelemetry()`, `this.#handleNewTabInGroup()`, `this.#initSuggestions()`, `this.#nameField.addEventListener()`, `this.#panel.addEventListener()`, `this.#populateSwatches()`, `this.#swatchesContainer.addEventListener()`, `this.activeGroup.saveAndClose()`, `this.activeGroup.tabs.map()`, `this.activeGroup.ungroupTabs()`, `this.appendChild()`, `this.close()`, `this.initializeAttributeInheritance()`, `this.panel.addEventListener()`, `this.querySelector()`
- 条件付き依存: `if (e.target !== this.#nameField)` → `this.#nameField.blur()`
- 条件付き依存: `if (links.length)` → `BrowserUtils.copyLinks()`
- 参照: `TabMetrics.METRIC_SOURCE.TAB_GROUP_MENU`, `e.target`, `gBrowser.TabMetrics.METRIC_SOURCE.TAB_GROUP_MENU`, `links.length`, `tab.linkedBrowser.currentURI.spec`, `this.#cancelButton`, `this.#commandButtons`, `this.#createButton`, `this.#createTabGroupHeading`, `this.#defaultActions`, `this.#editTabGroupHeading`, `this.#nameContainer`, `this.#nameField`, `this.#nameField.value`, `this.#panel`, `this.#swatchesContainer`, `this.#tabGroupMain`, `this.#tabGroupPropertiesActions`, `this._initialized`, `this.activeGroup`, `this.activeGroup.label`, `this.canShowAIUserInterface`, `this.constructor.fragment`, `this.smartTabGroupsPrefEnabled`, `this.textContent`

## this.canShowAIUserInterface()
- 位置: L467-477
- 役割: グループ未所属のタブが一つでもあれば真を返す(スマート提案ボタンを出せるか)。
- 触るとき: 提案ボタンの表示条件を調べるとき。(この関数は呼び出し元が見つからず、未使用の可能性あり)
- 呼び出し先: `tabs.forEach()`
- 参照: `tab.group`

## MozTabbrowserTabGroupMenu.smartTabGroupsEnabled()
- 位置: L564-572
- 役割: 英語ロケール、pref 有効、非プライベート、ML 有効のすべてを満たすときに真を返す getter。
- 触るとき: スマートタブグループが使える条件を変えるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Services.locale.appLocaleAsBCP47.startsWith()`
- 参照: `this.documentGlobal`, `this.mlEnabled`, `this.smartTabGroupsFeatureConfigEnabled`, `this.smartTabGroupsUserEnabled`
- XPCOM: `Services.locale`

## MozTabbrowserTabGroupMenu.smartTabGroupsPrefEnabled()
- 位置: L574-580
- 役割: ユーザー設定、機能設定、オプトインがすべて有効かを返す getter。
- 触るとき: スマート機能の有効状態テレメトリを調べるとき。
- 参照: `this.smartTabGroupsFeatureConfigEnabled`, `this.smartTabGroupsOptin`, `this.smartTabGroupsUserEnabled`

## MozTabbrowserTabGroupMenu.#onSmartTabGroupsPrefChange()
- 位置: L582-596
- 役割: pref 変更時に提案 UI を初期化し、アイコンを更新してテレメトリを記録する。
- 触るとき: pref 切り替え後の UI 更新を調べるとき。
- 呼び出し先: `Glean.tabgroup.smartTab.record()`, `Glean.tabgroup.smartTabEnabled.set()`
- 条件付き依存: `if (!this.#smartTabGroupsInitiated && this.smartTabGroupsEnabled)` → `this.#initSuggestions()`
- 参照: `MozTabbrowserTabGroupMenu.AI_ICON`, `this.#smartTabGroupsInitiated`, `this.#suggestionButton.iconSrc`, `this.#suggestionsMessage.iconSrc`, `this.smartTabGroupsEnabled`, `this.smartTabGroupsPrefEnabled`

## MozTabbrowserTabGroupMenu.#onSmartTabGroupsOptInPrefChange()
- 位置: L598-603
- 役割: オプトイン pref の変更をテレメトリに記録する。
- 触るとき: オプトイン状態の記録を調べるとき。
- 呼び出し先: `Glean.tabgroup.smartTab.record()`, `Glean.tabgroup.smartTabEnabled.set()`
- 参照: `this.smartTabGroupsPrefEnabled`

## MozTabbrowserTabGroupMenu.#initSmartTabGroupsOptin()
- 位置: L605-674
- 役割: モデルのオプトイン UI を作って各イベントを結線し、コンテナに表示する。
- 触るとき: AI 機能のオプトイン流れを変えるとき。
- 呼び出し先: `Services.prefs.setBoolPref()`, `document.createElement()`, `openTrustedLinkIn()`, `this.#handleFirstDownloadAndSuggest()`, `this.#handleMLOptinTelemetry()`, `this.#setFormToDisabled()`, `this.#smartTabGroupingManager.terminateProcess()`, `this.#suggestionsOptin.addEventListener()`, `this.#suggestionsOptinContainer.appendChild()`
- 参照: `MozTabbrowserTabGroupMenu.AI_ICON`, `MozTabbrowserTabGroupMenu.State.CREATE_AI_INITIAL`, `MozTabbrowserTabGroupMenu.State.EDIT_AI_INITIAL`, `MozTabbrowserTabGroupMenu.State.OPTIN`, `this.#suggestionsOptin`, `this.#suggestionsOptin.footerMessageL10nId`, `this.#suggestionsOptin.headingIcon`, `this.#suggestionsOptin.headingL10nId`, `this.#suggestionsOptin.messageL10nId`, `this.#suggestionsOptinContainer.hidden`, `this.#suggestionsRunToken`, `this.createMode`, `this.suggestionState`
- XPCOM: `Services.prefs`

## MozTabbrowserTabGroupMenu.#initSuggestions()
- 位置: L676-765
- 役割: スマート提案が有効なとき、マネージャを生成して提案関連の要素とボタンのイベントを一度だけ設定する。
- 触るとき: タブ提案 UI の初期化や要素を変えるとき。
- 呼び出し先: `ChromeUtils.importESModule()`, `this.#cancelSuggestionsButton.addEventListener()`, `this.#createSuggestionsButton.addEventListener()`, `this.#handleLoadSuggestionsCancel()`, `this.#handleMlTelemetry()`, `this.#handleSmartSuggest()`, `this.#initSmartTabGroupsOptin()`, `this.#selectSuggestionsCheckbox.addEventListener()`, `this.#suggestionButton.addEventListener()`, `this.#suggestionsLoadCancel.addEventListener()`, `this.activeGroup.addTabs()`, `this.close()`, `this.querySelector()`
- 条件付き依存: `if (e.target.checked)` → `this.#handleSelectAll()`
- 条件付き依存: `if (!(e.target.checked))` → `this.#handleDeselectAll()`
- 参照: `MozTabbrowserTabGroupMenu.AI_ICON`, `e.target.checked`, `this.#cancelSuggestionsButton`, `this.#createSuggestionsButton`, `this.#selectSuggestionsCheckbox`, `this.#selectedSuggestedTabs`, `this.#smartTabGroupingManager`, `this.#smartTabGroupsInitiated`, `this.#suggestionButton`, `this.#suggestionButton.iconSrc`, `this.#suggestions`, `this.#suggestionsContainer`, `this.#suggestionsHeading`, `this.#suggestionsLoadActions`, `this.#suggestionsLoadCancel`, `this.#suggestionsLoading`, `this.#suggestionsMessage`, `this.#suggestionsMessage.iconSrc`, `this.#suggestionsMessageContainer`, `this.#suggestionsOptinContainer`, `this.#suggestionsRunToken`, `this.#suggestionsSeparator`, `this.smartTabGroupsEnabled`, `this.smartTabGroupsOptin`

## MozTabbrowserTabGroupMenu.#populateSwatches()
- 位置: L767-793
- 役割: 色の選択肢ごとにラジオ入力とラベルを作って配置する。
- 触るとき: グループ色の選択肢の見た目を変えるとき。
- 呼び出し先: `document.createElement()`, `label.classList.add()`, `label.setAttribute()`, `label.style.setProperty()`, `this.#clearSwatches()`, `this.#swatches.push()`, `this.#swatchesContainer.append()`
- 参照: `MozTabbrowserTabGroupMenu.COLORS`, `MozTabbrowserTabGroupMenu.MESSAGE_IDS`, `input.id`, `input.name`, `input.type`, `input.value`, `label.htmlFor`

## MozTabbrowserTabGroupMenu.#clearSwatches()
- 位置: L795-798
- 役割: 色スウォッチの要素と保持配列を空にする。
- 触るとき: スウォッチの再生成を調べるとき。
- 参照: `this.#swatches`, `this.#swatchesContainer.innerHTML`

## MozTabbrowserTabGroupMenu.createMode()
- 位置: L800-802
- 役割: 作成モードかどうかを返す getter。
- 触るとき: 作成/編集の判別を参照する箇所を調べるとき。
- 参照: `this.#createMode`

## MozTabbrowserTabGroupMenu.createMode()
- 位置: L804-817
- 役割: 作成モードを設定し、パネルのクラス、aria-labelledby、リンクコピーボタンの表示を切り替える setter。
- 触るとき: 作成モードと編集モードの見た目の違いを変えるとき。
- 呼び出し先: `this.#panel.classList.toggle()`, `this.#panel.setAttribute()`
- 参照: `this.#commandButtons.copyAllLinks.hidden`, `this.#createMode`

## MozTabbrowserTabGroupMenu.activeGroup()
- 位置: L819-821
- 役割: 編集対象のグループを返す getter。
- 触るとき: 対象グループの参照元を調べるとき。
- 参照: `this.#activeGroup`

## MozTabbrowserTabGroupMenu.activeGroup()
- 位置: L823-833
- 役割: 対象グループを設定し、名前欄と選択中の色を反映する setter。
- 触るとき: パネルを開いたときの入力欄の初期値を調べるとき。
- 呼び出し先: `this.#swatches.forEach()`
- 参照: `group.color`, `group.label`, `node.checked`, `node.value`, `this.#activeGroup`, `this.#nameField.value`

## MozTabbrowserTabGroupMenu.nextUnusedColor()
- 位置: L835-851
- 役割: 既存グループが使っていない最初の色を返し、全部使用済みならランダムに選ぶ getter。
- 触るとき: 新規グループの既定色の決め方を変えるとき。
- 呼び出し先: `MozTabbrowserTabGroupMenu.COLORS.find()`, `gBrowser.getAllTabGroups()`, `gBrowser.getAllTabGroups().forEach()`, `usedColors.includes()`, `usedColors.push()`
- 条件付き依存: `if (!color)` → `Math.floor()`
- 条件付き依存: `if (!color)` → `Math.random()`
- 参照: `MozTabbrowserTabGroupMenu.COLORS`, `MozTabbrowserTabGroupMenu.COLORS.length`, `group.color`

## MozTabbrowserTabGroupMenu.panel()
- 位置: L853-855
- 役割: 最初の子要素(パネル)を返す getter。
- 触るとき: パネル要素の取得方法を確認するとき。
- 参照: `this.children`

## MozTabbrowserTabGroupMenu.#panelPosition()
- 位置: L857-864
- 役割: 縦タブか通常か、サイドバー位置に応じたパネルの表示位置を返す getter。
- 触るとき: パネルが開く位置がずれるとき。
- 参照: `SidebarController._positionStart`, `gBrowser.tabContainer.verticalMode`

## MozTabbrowserTabGroupMenu.#initMlGroupLabel()
- 位置: async L869-884
- 役割: スマート機能が有効なら、グループのタブから ML でラベルを予測して設定する。
- 触るとき: グループ名の自動提案の動作を調べるとき。
- 呼び出し先: `gBrowser.visibleTabs.filter()`, `tabs.includes()`, `this.#setMlGroupLabel()`, `this.#smartTabGroupingManager.getPredictedLabelForGroup()`
- 参照: `t.pinned`, `this.activeGroup.tabs`, `this.activeGroup.tabs?.length`, `this.smartTabGroupsEnabled`

## MozTabbrowserTabGroupMenu.#shouldUpdateLabelWithMlLabel()
- 位置: L891-893
- 役割: 名前欄が空でパネルが閉じていないときに限り、ML ラベルで更新してよいと返す。
- 触るとき: ML ラベルがユーザー入力を上書きする条件を調べるとき。
- 参照: `this.#nameField.value`, `this.panel.state`

## MozTabbrowserTabGroupMenu.#setMlGroupLabel()
- 位置: L902-910
- 役割: 更新可能なら ML ラベルをグループと名前欄に入れて選択し、値を保持する。
- 触るとき: 自動ラベルの反映方法を変えるとき。
- 呼び出し先: `this.#nameField.select()`, `this.#shouldUpdateLabelWithMlLabel()`
- 参照: `this.#activeGroup.label`, `this.#nameField.value`, `this.#suggestedMlLabel`

## MozTabbrowserTabGroupMenu.openCreateModal()
- 位置: L912-933
- 役割: 作成モードでパネルを開き、オプトイン済みなら ML ラベル生成と埋め込みエンジン初期化を始める。
- 触るとき: グループ新規作成時のパネル表示を変えるとき。
- 呼び出し先: `this.#initMlGroupLabel()`, `this.#maybeUpdateLayoutForNova()`, `this.#panel.openPopup()`
- 条件付き依存: `if (this.smartTabGroupsEnabled)` → `this.#smartTabGroupingManager.initEmbeddingEngine()`
- 参照: `MozTabbrowserTabGroupMenu.State.CREATE_AI_INITIAL`, `MozTabbrowserTabGroupMenu.State.CREATE_STANDARD_INITIAL`, `group.firstChild`, `this.#panelPosition`, `this.activeGroup`, `this.createMode`, `this.smartTabGroupsEnabled`, `this.smartTabGroupsOptin`, `this.suggestionState`

## MozTabbrowserTabGroupMenu.mlLabel()
- 位置: L938-940
- 役割: ML 生成ラベルを設定する setter(テスト用)。
- 触るとき: テストから ML ラベルを差し込むとき。
- 参照: `this.#suggestedMlLabel`

## MozTabbrowserTabGroupMenu.mlLabel()
- 位置: L942-944
- 役割: 保持中の ML 生成ラベルを返す getter。
- 触るとき: ML ラベルの参照箇所を調べるとき。
- 参照: `this.#suggestedMlLabel`

## MozTabbrowserTabGroupMenu.hasSuggestedMlTabs()
- 位置: L949-951
- 役割: ML のタブ提案を行ったかの印を設定する setter。
- 触るとき: 提案テレメトリの条件を調べるとき。
- 参照: `this.#hasSuggestedMlTabs`

## MozTabbrowserTabGroupMenu.hasSuggestedMlTabs()
- 位置: L953-955
- 役割: ML のタブ提案を行ったかの印を返す getter。
- 触るとき: 提案テレメトリの条件を調べるとき。
- 参照: `this.#hasSuggestedMlTabs`

## MozTabbrowserTabGroupMenu.openEditModal()
- 位置: L957-979
- 役割: 編集モードでパネルを開き、新規ウィンドウ移動やリンクコピー、保存ボタンの状態を設定する。
- 触るとき: 既存グループの編集パネルの表示を変えるとき。
- 呼び出し先: `document.getElementById()`, `document.l10n.setAttributes()`, `this.#getGroupLinks()`, `this.#maybeDisableOrHideSaveButton()`, `this.#maybeUpdateLayoutForNova()`, `this.#panel.openPopup()`
- 参照: `MozTabbrowserTabGroupMenu.State.EDIT_AI_INITIAL`, `MozTabbrowserTabGroupMenu.State.EDIT_STANDARD_INITIAL`, `document.getElementById("tabGroupEditor_moveGroupToNewWindow").disabled`, `gBrowser.openTabs.length`, `group.firstChild`, `this.#commandButtons.copyAllLinks`, `this.#commandButtons.copyAllLinks.disabled`, `this.#getGroupLinks(this.activeGroup).length`, `this.#panelPosition`, `this.activeGroup`, `this.activeGroup?.tabs.length`, `this.createMode`, `this.smartTabGroupsEnabled`, `this.suggestionState`

## MozTabbrowserTabGroupMenu.#maybeUpdateLayoutForNova()
- 位置: L981-991
- 役割: Nova が有効かで色スウォッチの配置位置を切り替える。
- 触るとき: Nova 向けのレイアウト差分を調べるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- 条件付き依存: `if (isNovaEnabled)` → `this.#nameContainer.before()`
- 条件付き依存: `if (!(isNovaEnabled))` → `this.#tabGroupPropertiesActions.prepend()`
- 参照: `this.#swatchesContainer`
- XPCOM: `Services.prefs`

## MozTabbrowserTabGroupMenu.#maybeDisableOrHideSaveButton()
- 位置: L993-1015
- 役割: プライベートでは保存ボタンを隠し、それ以外はタブ状態を書き出して保存可否で無効化を決める。
- 触るとき: 保存して閉じるボタンの有効条件を調べるとき。
- 呼び出し先: `PrivateBrowsingUtils.isWindowPrivate()`, `Promise.allSettled()`, `Promise.allSettled(flushes).then()`, `TabStateFlusher.flush()`, `document.getElementById()`, `flushes.push()`, `this.activeGroup.tabs.forEach()`
- 条件付き依存: `if (this.activeGroup?.tabs)` → `SessionStore.shouldSaveTabsToGroup()`
- 参照: `saveAndCloseGroup.disabled`, `saveAndCloseGroup.hidden`, `tab.linkedBrowser`, `this.activeGroup.tabs`, `this.activeGroup?.tabs`, `this.documentGlobal`

## MozTabbrowserTabGroupMenu.close()
- 位置: L1017-1022
- 役割: 作成モードなら作成グループを残すか記録してパネルを閉じる。
- 触るとき: キャンセルと確定でのグループの扱いを調べるとき。
- 呼び出し先: `this.#panel.hidePopup()`
- 参照: `this.#keepNewlyCreatedGroup`, `this.createMode`

## MozTabbrowserTabGroupMenu.on_popupshown()
- 位置: L1024-1044
- 役割: パネル表示時に名前欄へフォーカスし、共有と AI タブのボタン表示を決める。
- 触るとき: パネルを開いた直後の初期状態を変えるとき。
- 呼び出し先: `Object.values()`, `["http", "https"].includes()`, `lazy.AIWindow.isAIWindowActiveAndEnabled()`, `this.#nameField.focus()`, `this.activeGroup?.tabs.some()`
- 参照: `ContentSharingUtils.isEnabled`, `button.label`, `button.tooltipText`, `tab.linkedBrowser.currentURI.scheme`, `this.#commandButtons`, `this.#commandButtons.createAITab.hidden`, `this.#commandButtons.shareTabGroup.hidden`, `this.#initialTabGroupName`, `this.#keepNewlyCreatedGroup`, `this.activeGroup?.label`, `this.aitabEnabled`, `this.createMode`

## MozTabbrowserTabGroupMenu.on_popuphidden()
- 位置: L1046-1075
- 役割: パネルが閉じたとき、作成の完了または取り消しを処理して状態を初期化する。
- 触るとき: 作成キャンセル時のグループ解除や後始末を調べるとき。
- 呼び出し先: `this.#smartTabGroupingManager?.terminateProcess()`
- 条件付き依存: `if (this.#keepNewlyCreatedGroup)` → `this.dispatchEvent()`
- 条件付き依存: `if ( this.smartTabGroupsEnabled && this.smartTabGroupsOptin && (this.#suggestedMlLabel !== null || this.#hasSuggestedMlTabs) )` → `this.#handleMlTelemetry()`
- 条件付き依存: `if (!(this.#keepNewlyCreatedGroup))` → `this.activeGroup.ungroupTabs()`
- 条件付き依存: `if (!(this.#keepNewlyCreatedGroup))` → `TabMetrics.userTriggeredContext()`
- 条件付き依存: `if (this.#nameField.disabled)` → `this.#setFormToDisabled()`
- 条件付き依存: `if (this.activeGroup?.label != this.#initialTabGroupName)` → `Glean.tabgroup.groupInteractions.rename.add()`
- 参照: `TabMetrics.METRIC_SOURCE.CANCEL_TAB_GROUP_CREATION`, `this.#hasSuggestedMlTabs`, `this.#initialTabGroupName`, `this.#keepNewlyCreatedGroup`, `this.#nameField.disabled`, `this.#suggestedMlLabel`, `this.activeGroup`, `this.activeGroup?.label`, `this.createMode`, `this.smartTabGroupsEnabled`, `this.smartTabGroupsOptin`

## MozTabbrowserTabGroupMenu.on_keypress()
- 位置: L1077-1098
- 役割: Escape で取り消して閉じ、Enter でボタン以外なら確定して閉じる。
- 触るとき: パネルのキー操作を変えるとき。
- 呼び出し先: `this.close()`
- 条件付き依存: `if ( event.target.localName != "toolbarbutton" && event.target.localName != "moz-button" )` → `this.close()`
- 参照: `KeyEvent.DOM_VK_ESCAPE`, `KeyEvent.DOM_VK_RETURN`, `event.defaultPrevented`, `event.keyCode`, `event.target.localName`

## MozTabbrowserTabGroupMenu.on_change()
- 位置: L1103-1111
- 役割: 色ラジオの変更をグループの色に反映してテレメトリを記録する。
- 触るとき: グループ色変更時の処理を調べるとき。
- 条件付き依存: `if (this.activeGroup)` → `Glean.tabgroup.groupInteractions.change_color.add()`
- 参照: `aEvent.target.name`, `aEvent.target.value`, `this.activeGroup`, `this.activeGroup.color`

## MozTabbrowserTabGroupMenu.#handleNewTabInGroup()
- 位置: async L1113-1128
- 役割: TabOpen を待ち受けて、グループ末尾の隣に開いた新規タブをグループに追加し、パネルを閉じる。
- 触るとき: グループ内に新規タブを開く動作を変えるとき。
- 呼び出し先: `gBrowser.addAdjacentNewTab()`, `this.activeGroup?.tabs.at()`, `window.addEventListener()`, `window.focus()`

## onTabOpened()
- 位置: async L1115-1119
- 役割: 開いたタブをアクティブなグループに追加し、パネルを閉じてリスナーを外す。
- 触るとき: 新規タブ追加後の後始末を調べるとき。
- 呼び出し先: `this.activeGroup?.addTabs()`, `this.close()`, `window.removeEventListener()`
- 参照: `aEvent.target`

## MozTabbrowserTabGroupMenu.#getGroupLinks()
- 位置: L1134-1147
- 役割: グループ内のタブから共有可能な URL とタイトルの一覧を作る。
- 触るとき: リンクのコピー対象を調べるとき。
- 呼び出し先: `BrowserUtils.getShareableURL()`
- 条件付き依存: `if (shareableURL)` → `links.push()`
- 条件付き依存: `if (shareableURL)` → `gURLBar.makeURIReadable()`
- 参照: `browser.contentTitle`, `browser.currentURI`, `gURLBar.makeURIReadable(shareableURL).displaySpec`, `group.tabs`, `tab.linkedBrowser`

## MozTabbrowserTabGroupMenu.suggestionState()
- 位置: L1152-1158
- 役割: 提案 UI の状態を更新し、変化があれば表示を描き直す setter。
- 触るとき: 提案パネルの状態遷移を調べるとき。
- 呼び出し先: `this.#renderSuggestionState()`
- 参照: `this.#suggestionState`

## MozTabbrowserTabGroupMenu.#handleLoadSuggestionsCancel()
- 位置: L1160-1166
- 役割: 提案の実行を取り消し、作成/編集に応じた初期の AI 状態に戻す。
- 触るとき: 提案読み込み中の取り消し動作を調べるとき。
- 参照: `MozTabbrowserTabGroupMenu.State.CREATE_AI_INITIAL`, `MozTabbrowserTabGroupMenu.State.EDIT_AI_INITIAL`, `this.#suggestionsRunToken`, `this.createMode`, `this.suggestionState`

## MozTabbrowserTabGroupMenu.#handleSelectAll()
- 位置: L1168-1176
- 役割: 提案チェックボックスをすべて選択し、選択済みタブを全提案にする。
- 触るとき: 提案の全選択の挙動を調べるとき。
- 呼び出し先: `document .querySelectorAll()`, `document .querySelectorAll(".tab-group-suggestion-checkbox") .forEach()`
- 参照: `checkbox.checked`, `this.#selectedSuggestedTabs`, `this.#suggestedTabs`

## MozTabbrowserTabGroupMenu.#handleDeselectAll()
- 位置: L1178-1185
- 役割: 提案チェックボックスをすべて外し、選択済みタブを空にする。
- 触るとき: 提案の全解除の挙動を調べるとき。
- 呼び出し先: `document .querySelectorAll()`, `document .querySelectorAll(".tab-group-suggestion-checkbox") .forEach()`
- 参照: `checkbox.checked`, `this.#selectedSuggestedTabs`

## MozTabbrowserTabGroupMenu.#setFormToDisabled()
- 位置: L1192-1206
- 役割: パネル内のボタン、名前欄、色入力の無効状態をまとめて切り替える。
- 触るとき: モデル取得中に操作を止める範囲を変えるとき。
- 呼び出し先: `swatches.forEach()`, `this.#swatchesContainer.querySelectorAll()`, `this.#tabGroupMain.querySelectorAll()`, `toolbarButtons.forEach()`
- 参照: `button.disabled`, `input.disabled`, `this.#nameField.disabled`

## MozTabbrowserTabGroupMenu.#handleFirstDownloadAndSuggest()
- 位置: async L1208-1238
- 役割: オプトイン後にモデルを取得して進捗を表示し、完了後にラベルとタブの提案へ進む。
- 触るとき: 初回のモデル取得とその取り消しの流れを調べるとき。
- 呼び出し先: `Date.now()`, `this.#handleMLOptinTelemetry()`, `this.#handleSmartSuggest()`, `this.#initMlGroupLabel()`, `this.#setFormToDisabled()`, `this.#smartTabGroupingManager.preloadAllModels()`
- 参照: `prog.percentage`, `this.#suggestionsOptin.headingIcon`, `this.#suggestionsOptin.headingL10nId`, `this.#suggestionsOptin.isHidden`, `this.#suggestionsOptin.isLoading`, `this.#suggestionsOptin.messageL10nId`, `this.#suggestionsOptin.progressStatus`, `this.#suggestionsRunToken`

## MozTabbrowserTabGroupMenu.#handleSmartSuggest()
- 位置: async L1240-1280
- 役割: 読み込み状態にして関連タブを取得し、結果の有無に応じた提案表示に遷移する。
- 触るとき: タブ提案の実行と結果表示を変えるとき。
- 呼び出し先: `Date.now()`, `tabs.forEach()`, `this.#createRow()`, `this.#smartTabGroupingManager.smartTabGroupingForGroup()`
- 条件付き依存: `if (!this.#createMode)` → `this.#handleMlTelemetry()`
- 参照: `MozTabbrowserTabGroupMenu.State.CREATE_AI_WITH_NO_SUGGESTIONS`, `MozTabbrowserTabGroupMenu.State.CREATE_AI_WITH_SUGGESTIONS`, `MozTabbrowserTabGroupMenu.State.EDIT_AI_WITH_NO_SUGGESTIONS`, `MozTabbrowserTabGroupMenu.State.EDIT_AI_WITH_SUGGESTIONS`, `MozTabbrowserTabGroupMenu.State.LOADING`, `gBrowser.tabs`, `tabs.length`, `this.#createMode`, `this.#hasSuggestedMlTabs`, `this.#selectedSuggestedTabs`, `this.#suggestedTabs`, `this.#suggestionsRunToken`, `this.activeGroup`, `this.suggestionState`

## MozTabbrowserTabGroupMenu.#handleMlTelemetry()
- 位置: L1287-1314
- 役割: スマート機能が有効なら、ラベルとタブ提案の利用結果を各テレメトリに送る。
- 触るとき: ML 提案の保存・取り消しの記録内容を変えるとき。
- 条件付き依存: `if (this.#suggestedMlLabel !== null)` → `this.#smartTabGroupingManager.handleLabelTelemetry()`
- 条件付き依存: `if (this.#hasSuggestedMlTabs)` → `this.#smartTabGroupingManager.handleSuggestTelemetry()`
- 参照: `gBrowser.tabs.length`, `this.#activeGroup.id`, `this.#activeGroup.tabs.length`, `this.#hasSuggestedMlTabs`, `this.#nameField.value`, `this.#selectedSuggestedTabs.length`, `this.#suggestedMlLabel`, `this.#suggestedTabs.length`, `this.smartTabGroupsEnabled`, `this.smartTabGroupsOptin`

## MozTabbrowserTabGroupMenu.#handleMLOptinTelemetry()
- 位置: L1321-1325
- 役割: オプトイン UI の段階を Glean に記録する。
- 触るとき: オプトインの計測ステップを追加するとき。
- 呼び出し先: `Glean.tabgroup.smartTabOptin.record()`

## MozTabbrowserTabGroupMenu.#createRow()
- 位置: L1327-1349
- 役割: 提案タブ一つ分のチェックボックス行を作り、選択変更を選択済み一覧に反映する。
- 触るとき: 提案リストの各行の見た目や挙動を変えるとき。
- 呼び出し先: `checkbox.addEventListener()`, `checkbox.classList.add()`, `document.createElement()`, `this.#suggestions.appendChild()`
- 条件付き依存: `if (e.target.checked)` → `this.#selectedSuggestedTabs.push()`
- 条件付き依存: `if (!(e.target.checked))` → `this.#selectedSuggestedTabs.filter()`
- 参照: `checkbox.checked`, `checkbox.iconSrc`, `checkbox.label`, `e.target.checked`, `tab.image`, `tab.label`, `this.#selectedSuggestedTabs`

## MozTabbrowserTabGroupMenu.#setElementVisibility()
- 位置: L1358-1363
- 役割: 要素が存在すれば hidden 属性を表示可否に合わせて切り替える。
- 触るとき: 表示切り替えの共通処理を確認するとき。
- 参照: `element.hidden`

## MozTabbrowserTabGroupMenu.#showDefaultTabGroupActions()
- 位置: L1365-1367
- 役割: 既定のグループ操作欄の表示を切り替える。
- 触るとき: 操作欄が出る状態を調べるとき。
- 呼び出し先: `this.#setElementVisibility()`
- 参照: `this.#defaultActions`

## MozTabbrowserTabGroupMenu.#showSmartSuggestionsContainer()
- 位置: L1369-1371
- 役割: 提案リストのコンテナの表示を切り替える。
- 触るとき: 提案リストが出る状態を調べるとき。
- 呼び出し先: `this.#setElementVisibility()`
- 参照: `this.#suggestionsContainer`

## MozTabbrowserTabGroupMenu.#showSuggestionButton()
- 位置: L1373-1375
- 役割: 提案ボタンの表示を切り替える。
- 触るとき: 提案ボタンが出る状態を調べるとき。
- 呼び出し先: `this.#setElementVisibility()`
- 参照: `this.#suggestionButton`

## MozTabbrowserTabGroupMenu.#showSuggestionMessageContainer()
- 位置: L1377-1379
- 役割: 提案メッセージ欄の表示を切り替える。
- 触るとき: 提案なしメッセージの表示状態を調べるとき。
- 呼び出し先: `this.#setElementVisibility()`
- 参照: `this.#suggestionsMessageContainer`

## MozTabbrowserTabGroupMenu.#showSuggestionsSeparator()
- 位置: L1381-1383
- 役割: 提案欄の区切り線の表示を切り替える。
- 触るとき: 区切り線の表示状態を調べるとき。
- 呼び出し先: `this.#setElementVisibility()`
- 参照: `this.#suggestionsSeparator`

## MozTabbrowserTabGroupMenu.#setLoadingState()
- 位置: L1385-1388
- 役割: 読み込み表示とその操作欄の表示をまとめて切り替える。
- 触るとき: 読み込み中表示の出し入れを調べるとき。
- 呼び出し先: `this.#setElementVisibility()`
- 参照: `this.#suggestionsLoadActions`, `this.#suggestionsLoading`

## MozTabbrowserTabGroupMenu.#setSuggestionsButtonCreateModeState()
- 位置: L1390-1396
- 役割: 提案ボタンの文言を作成用か編集用の l10n ID に切り替える。
- 触るとき: 提案ボタンの文言を変えるとき。
- 呼び出し先: `this.#suggestionButton.setAttribute()`

## MozTabbrowserTabGroupMenu.#setSuggestModeSuggestionState()
- 位置: L1404-1410
- 役割: 提案一覧だけを見せる拡張表示に切り替え、見出しと通常欄の表示を入れ替える。
- 触るとき: 提案表示時のパネル構成を変えるとき。
- 呼び出し先: `this.#panel.classList.toggle()`, `this.#setElementVisibility()`
- 参照: `this.#createTabGroupHeading`, `this.#editTabGroupHeading`, `this.#suggestionsHeading`, `this.#tabGroupPropertiesActions`

## MozTabbrowserTabGroupMenu.#resetCommonUI()
- 位置: L1412-1428
- 役割: 読み込み表示、提案一覧、選択状態、オプトイン欄を初期状態に戻す。
- 触るとき: 状態遷移時の共通リセット内容を調べるとき。
- 呼び出し先: `this.#setLoadingState()`, `this.#setSuggestModeSuggestionState()`, `this.#showSmartSuggestionsContainer()`
- 条件付き依存: `if (this.#suggestions)` → `this.#suggestions.replaceChildren()`
- 条件付き依存: `if (this.#suggestionsOptinContainer)` → `this.#suggestionsOptinContainer.replaceChildren()`
- 参照: `this.#selectSuggestionsCheckbox`, `this.#selectSuggestionsCheckbox.checkbox`, `this.#selectedSuggestedTabs`, `this.#suggestedTabs`, `this.#suggestions`, `this.#suggestionsOptinContainer`, `this.#suggestionsOptinContainer.hidden`

## MozTabbrowserTabGroupMenu.#renderSuggestionState()
- 位置: L1430-1544
- 役割: 提案 UI の状態ごとに、ボタン、メッセージ、操作欄などの表示の組み合わせを決める。
- 触るとき: 各状態でどの部品が見えるかを変えるとき。
- 呼び出し先: `this.#resetCommonUI()`, `this.#setLoadingState()`, `this.#setSuggestModeSuggestionState()`, `this.#setSuggestionsButtonCreateModeState()`, `this.#showDefaultTabGroupActions()`, `this.#showSmartSuggestionsContainer()`, `this.#showSuggestionButton()`, `this.#showSuggestionMessageContainer()`, `this.#showSuggestionsSeparator()`
- 参照: `MozTabbrowserTabGroupMenu.State .CREATE_AI_INITIAL_SUGGESTIONS_DISABLED`, `MozTabbrowserTabGroupMenu.State .EDIT_AI_INITIAL_SUGGESTIONS_DISABLED`, `MozTabbrowserTabGroupMenu.State.CREATE_AI_INITIAL`, `MozTabbrowserTabGroupMenu.State.CREATE_AI_WITH_NO_SUGGESTIONS`, `MozTabbrowserTabGroupMenu.State.CREATE_AI_WITH_SUGGESTIONS`, `MozTabbrowserTabGroupMenu.State.CREATE_STANDARD_INITIAL`, `MozTabbrowserTabGroupMenu.State.EDIT_AI_INITIAL`, `MozTabbrowserTabGroupMenu.State.EDIT_AI_WITH_NO_SUGGESTIONS`, `MozTabbrowserTabGroupMenu.State.EDIT_AI_WITH_SUGGESTIONS`, `MozTabbrowserTabGroupMenu.State.EDIT_STANDARD_INITIAL`, `MozTabbrowserTabGroupMenu.State.ERROR`, `MozTabbrowserTabGroupMenu.State.LOADING`, `MozTabbrowserTabGroupMenu.State.OPTIN`, `this.#suggestionState`
