# browser/base/content/browser-profiles.js

source: browser/base/content/browser-profiles.js
source-hash: 7e427737893ebcaf211b6f8d4b9bb1ea26a7f846
lines: 841

## <module>
- 役割: gProfiles オブジェクトで、アプリメニュー・FxA メニュー・メニューバーのプロファイル表示、プロファイル切り替え・作成・管理の操作を担う。

## init()
- 位置: async L6-92
- 役割: 各メソッドを bind し、プロファイル関連の DOM ノードを取得して command/click/ViewShowing リスナーを登録する。SelectableProfileService の enableChanged も購読する。
- 触るとき: プロファイル関連のメニュー項目を追加・改名したとき、またはプロファイル機能の有効/無効でメニューが出たり消えたりする挙動を追うとき。
- 呼び出し先: `PanelMultiView.getViewNode()`, `PanelMultiView.getViewNode( document, "PanelUI-fxa-menu-create-profile" ).addEventListener()`, `PanelMultiView.getViewNode( document, "PanelUI-fxa-menu-create-profile-confirm-button" ).addEventListener()`, `PanelUI.mainView.addEventListener()`, `Services.strings.createBundle()`, `fxaPanelView.addEventListener()`, `this._onFxaMenuPanelShowing()`, `this._onPanelShowing()`, `this.appMenuCreateProfileButton.addEventListener()`, `this.copyProfile.bind()`, `this.createNewProfile.bind()`, `this.fxaMenuAllProfilesPanel.addEventListener()`, `this.fxaMenuProfileButtonsContainer.addEventListener()`, `this.handleCommand.bind()`, `this.launchProfile.bind()`, `this.manageProfiles.bind()`, `this.onPopupShowing.bind()`, `this.profilesButton.addEventListener()`, `this.subview.addEventListener()`, `this.toggleProfileMenus()`, `this.toggleProfileMenus.bind()`, `this.updateView.bind()`
- 条件付き依存: `if (SelectableProfileService)` → `SelectableProfileService.on()`
- 条件付き依存: `if (SelectableProfileService)` → `window.addEventListener()`
- 条件付き依存: `if (SelectableProfileService)` → `SelectableProfileService.off()`
- 参照: `SelectableProfileService?.isEnabled`, `this.appMenuCreateProfileButton`, `this.bundle`, `this.copyProfile`, `this.createNewProfile`, `this.fxaMenuAllProfilesPanel`, `this.fxaMenuProfileButtonsContainer`, `this.fxaMenuProfilesHeaderLabel`, `this.fxaMenuProfilesSeparator`, `this.handleCommand`, `this.launchProfile`, `this.manageProfiles`, `this.onPopupShowing`, `this.profilesButton`, `this.subview`, `this.toggleProfileMenus`, `this.updateView`
- XPCOM: `Services.strings`

## listener()
- 位置: L85-85
- 役割: enableChanged イベントを受け、toggleProfileMenus に有効状態を渡す無名リスナー。
- 触るとき: プロファイル機能を設定や実験で切り替えたときにメニューの表示が追従しない場合に確認する。
- 呼び出し先: `this.toggleProfileMenus()`

## toggleProfileMenus()
- 位置: L94-97
- 役割: メニューバーの profiles-menu を、有効状態が false のとき hidden にする。
- 触るとき: プロファイル機能が無効なのにメニューバーに項目が残る、または逆に出ないといった問題を調べるとき。
- 呼び出し先: `document.getElementById()`
- 参照: `profilesMenu.hidden`

## _onPanelShowing()
- 位置: async L99-131
- 役割: アプリメニュー表示時に、プロファイルボタンのラベル・画像・テーマ色を現在のプロファイルに合わせて設定する。プロファイルが無ければ作成ボタンを出す。
- 触るとき: アプリメニューのプロファイルボタンの名前やアバターが古いまま更新されない、または作成ボタンの出し分けを変えたいとき。
- 呼び出し先: `SelectableProfileService.currentProfile.getAvatarURL()`, `SelectableProfileService.getAllProfiles()`, `profilesButton.setAttribute()`, `profilesButton.style.setProperty()`
- 参照: `SelectableProfileService.currentProfile.name`, `SelectableProfileService.currentProfile.theme`, `SelectableProfileService.initialized`, `SelectableProfileService?.isEnabled`, `profiles.length`, `profilesButton.hidden`, `this.appMenuCreateProfileButton.hidden`

## _onFxaMenuPanelShowing()
- 位置: async L133-223
- 役割: FxA メニュー表示時に、プロファイル一覧ボタンを現在のプロファイルを先頭にして最大 3 件まで作り直す。4 件以上なら「すべて表示」ボタンを追加する。
- 触るとき: FxA メニューのプロファイル一覧の並び順や件数上限、「すべて表示」の出現条件を変えるとき。
- 呼び出し先: `SelectableProfileService.getAllProfiles()`, `btn.classList.add()`, `btn.setAttribute()`, `btn.style.setProperty()`, `container.appendChild()`, `container.lastChild.remove()`, `document.createXULElement()`, `profile.getAvatarURL()`, `profiles.slice()`, `profiles.sort()`, `showProfilesSection()`
- 条件付き依存: `if (!SelectableProfileService?.isEnabled)` → `hideProfilesSection()`
- 条件付き依存: `if (!profiles.length)` → `document.createXULElement()`
- 条件付き依存: `if (!profiles.length)` → `createBtn.classList.add()`
- 条件付き依存: `if (!profiles.length)` → `createBtn.setAttribute()`
- 条件付き依存: `if (!profiles.length)` → `container.appendChild()`
- 条件付き依存: `if (!profiles.length)` → `showProfilesSection()`
- 条件付き依存: `if (profile.id === SelectableProfileService.currentProfile?.id)` → `btn.classList.add()`
- 条件付き依存: `if (profiles.length > 3)` → `document.createXULElement()`
- 条件付き依存: `if (profiles.length > 3)` → `allBtn.classList.add()`
- 条件付き依存: `if (profiles.length > 3)` → `allBtn.setAttribute()`
- 条件付き依存: `if (profiles.length > 3)` → `container.appendChild()`
- 参照: `SelectableProfileService.currentProfile?.id`, `SelectableProfileService.initialized`, `SelectableProfileService?.isEnabled`, `a.id`, `allBtn.id`, `b.id`, `container.lastChild`, `createBtn.id`, `profile.id`, `profile.name`, `profile.theme`, `profiles.length`, `this.fxaMenuProfileButtonsContainer`, `this.fxaMenuProfilesHeaderLabel`, `this.fxaMenuProfilesSeparator`

## hideProfilesSection()
- 位置: L138-142
- 役割: FxA メニューのプロファイル一覧コンテナ、見出し、区切り線を非表示にする。_onFxaMenuPanelShowing の内側の補助関数。
- 触るとき: プロファイル機能が無効のとき FxA メニューからセクションが消えない問題を追うとき。
- 参照: `container.hidden`, `headerLabel.hidden`, `separator.hidden`

## showProfilesSection()
- 位置: L144-148
- 役割: FxA メニューのプロファイル一覧コンテナ、見出し、区切り線を表示する。_onFxaMenuPanelShowing の内側の補助関数。
- 触るとき: プロファイル一覧のセクションが常に出るべきか、作成 CTA の時だけ出すべきかを変えるとき。
- 参照: `container.hidden`, `headerLabel.hidden`, `separator.hidden`

## _populateAllProfilesPanel()
- 位置: async L225-300
- 役割: 「すべてのプロファイル」サブビューの一覧を作り直す。現在のプロファイルには「使用中」表示とチェックアイコンを付け、他はラベルとアバターだけにする。
- 触るとき: すべてのプロファイル画面の項目表示や現在のプロファイルの印の付け方を変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`, `SelectableProfileService.getAllProfiles()`, `btn.classList.add()`, `btn.setAttribute()`, `btn.style.setProperty()`, `document.createXULElement()`, `list.appendChild()`, `list.lastChild.remove()`, `profiles.sort()`
- 条件付き依存: `if (profile.id === currentProfileId)` → `btn.setAttribute()`
- 条件付き依存: `if (profile.id === currentProfileId)` → `document.createXULElement()`
- 条件付き依存: `if (profile.id === currentProfileId)` → `icon.classList.add()`
- 条件付き依存: `if (profile.id === currentProfileId)` → `icon.setAttribute()`
- 条件付き依存: `if (profile.id === currentProfileId)` → `profile.getAvatarURL()`
- 条件付き依存: `if (profile.id === currentProfileId)` → `btn.appendChild()`
- 条件付き依存: `if (profile.id === currentProfileId)` → `labelVbox.classList.add()`
- 条件付き依存: `if (profile.id === currentProfileId)` → `mainLabel.setAttribute()`
- 条件付き依存: `if (profile.id === currentProfileId)` → `labelVbox.appendChild()`
- 条件付き依存: `if (profile.id === currentProfileId)` → `document.l10n.setAttributes()`
- 条件付き依存: `if (profile.id === currentProfileId)` → `currentLabel.classList.add()`
- 条件付き依存: `if (profile.id === currentProfileId)` → `checkIcon.classList.add()`
- 条件付き依存: `if (profile.id === currentProfileId)` → `checkIcon.setAttribute()`
- 条件付き依存: `if (!(profile.id === currentProfileId))` → `btn.setAttribute()`
- 条件付き依存: `if (!(profile.id === currentProfileId))` → `profile.getAvatarURL()`
- 参照: `SelectableProfileService.currentProfile?.id`, `SelectableProfileService.initialized`, `a.id`, `b.id`, `list.lastChild`, `profile.id`, `profile.name`, `profile.theme`

## onPopupShowing()
- 位置: async L305-349
- 役割: メニューバーのプロファイル一覧ポップアップを、既存の menuitem を再利用しつつ全プロファイル分更新し、不要になった項目を削除する。
- 触るとき: メニューバーのプロファイル項目が増減したり現在のプロファイルの表示がずれたりする問題を調べるとき。
- 呼び出し先: `SelectableProfileService.getAllProfiles()`, `document.getElementById()`, `existingItems.shift()`, `menuPopup.querySelectorAll()`, `menuitem.setAttribute()`, `menuitem.style.setProperty()`, `profile.getAvatarURL()`, `remaining.remove()`
- 条件付き依存: `if (isNewItem)` → `document.createXULElement()`
- 条件付き依存: `if (isNewItem)` → `menuitem.classList.add()`
- 条件付き依存: `if (isNewItem)` → `menuitem.setAttribute()`
- 条件付き依存: `if (profile.id === currentProfile.id)` → `menuitem.classList.add()`
- 条件付き依存: `if (profile.id === currentProfile.id)` → `menuitem.setAttribute()`
- 条件付き依存: `if (profile.id === currentProfile.id)` → `JSON.stringify()`
- 条件付き依存: `if (!(profile.id === currentProfile.id))` → `menuitem.classList.remove()`
- 条件付き依存: `if (!(profile.id === currentProfile.id))` → `menuitem.removeAttribute()`
- 条件付き依存: `if (!(profile.id === currentProfile.id))` → `menuitem.setAttribute()`
- 条件付き依存: `if (isNewItem)` → `menuPopup.insertBefore()`
- 参照: `SelectableProfileService.currentProfile`, `currentProfile.id`, `profile.id`, `profile.name`, `profile.theme`

## manageProfiles()
- 位置: L351-359
- 役割: データストアを準備してから about:profilemanager を開く。
- 触るとき: プロファイル管理画面を開く経路を追加したり、開く前の準備処理を変えたりするとき。
- 呼び出し先: `SelectableProfileService.maybeSetupDataStore()`, `SelectableProfileService.maybeSetupDataStore().then()`, `toOpenWindowByType()`

## copyProfile()
- 位置: L361-367
- 役割: FxA サブビューで選ばれたプロファイル、なければ現在のプロファイルを、データストア準備後にコピーする。
- 触るとき: プロファイルのコピー操作の対象がずれる問題や、コピー前の準備処理を変えるとき。
- 呼び出し先: `SelectableProfileService.maybeSetupDataStore()`, `SelectableProfileService.maybeSetupDataStore().then()`, `profile.copyProfile()`
- 参照: `SelectableProfileService.currentProfile`, `this._subViewProfile`

## createNewProfile()
- 位置: L369-371
- 役割: 新規プロファイル作成を SelectableProfileService に依頼する。source は呼び出し元の識別子として渡す。
- 触るとき: 作成操作の呼び出し元ごとの計測や、作成時に渡す引数を変えたいとき。
- 呼び出し先: `SelectableProfileService.createNewProfile()`

## updateView()
- 位置: L373-384
- 役割: プロファイルのサブビューを作り直してから表示する。キーボード操作で開いたかどうかを維持する。
- 触るとき: アプリメニューからプロファイル画面を開いたときのフォーカスやキーボード操作の挙動を調べるとき。
- 呼び出し先: `PanelUI.showSubView()`, `PanelView.forNode()`, `target.closest()`, `this.populateSubView()`
- 参照: `panelView._doingKeyboardActivation`, `panelView?._doingKeyboardActivation`

## updateFxAView()
- 位置: async L386-393
- 役割: FxA 一覧で押された profileid のプロファイルを取得し、そのプロファイル向けのサブビューを開く。
- 触るとき: FxA メニューの別プロファイルの詳細画面が違うプロファイルを表示するといった問題を調べるとき。
- 呼び出し先: `PanelUI.showSubView()`, `SelectableProfileService.getProfile()`, `parseInt()`, `target.getAttribute()`, `this.populateSubView()`
- 参照: `this._subViewProfile`

## launchProfile()
- 位置: L395-401
- 役割: 押された要素の profileid からプロファイルを取得し、その別インスタンスを起動する。
- 触るとき: プロファイルの起動経路を変えたり、起動時の引数を追加したりするとき。
- 呼び出し先: `SelectableProfileService.getProfile()`, `SelectableProfileService.getProfile( aEvent.target.getAttribute("profileid") ).then()`, `SelectableProfileService.launchInstance()`, `aEvent.target.getAttribute()`

## openTabsInProfile()
- 位置: async L403-411
- 役割: 選択されたタブ群の URL を、指定プロファイルのインスタンスで開くために launchInstance へ渡す。
- 触るとき: タブを別プロファイルへ移動する機能で、どの URL が渡るかを確認または変更するとき。
- 呼び出し先: `SelectableProfileService.getProfile()`, `SelectableProfileService.launchInstance()`, `aEvent.target.getAttribute()`, `tabsToOpen.map()`
- 参照: `tab.linkedBrowser.currentURI.spec`

## handleCommand()
- 位置: async L413-561
- 役割: プロファイル関連の command/click を target の id で振り分ける。FxA とアプリメニューの操作、メニューバーの操作、プロファイル項目のクリックで起動を行い、各操作の telemetry も送る。
- 触るとき: プロファイル関連の新しいボタンを追加するとき、またはどの操作が telemetry や起動に繋がるかを確認するとき。
- 呼び出し先: `PanelUI.showSubView()`, `String()`, `aEvent.stopPropagation()`, `aEvent.target.blur()`, `aEvent.target.classList.contains()`, `aEvent.target.closest()`, `aEvent.target.closest("panelview").panelMultiView.goBack()`, `aEvent.target.getAttribute()`, `aEvent.target.hasAttribute()`, `gSync.emitFxaToolbarTelemetry()`, `openTrustedLinkIn()`, `this._populateAllProfilesPanel()`, `this.copyProfile()`, `this.createNewProfile()`, `this.launchProfile()`, `this.manageProfiles()`, `this.openTabsInProfile()`, `this.updateView()`
- 条件付き依存: `if ( aEvent.target.classList.contains("profile-item") && aEvent.target.classList.contains("subviewbutton-nav") )` → `aEvent.stopPropagation()`
- 条件付き依存: `if ( aEvent.target.classList.contains("profile-item") && aEvent.target.classList.contains("subviewbutton-nav") )` → `gSync.emitFxaToolbarTelemetry()`
- 条件付き依存: `if ( aEvent.target.classList.contains("profile-item") && aEvent.target.classList.contains("subviewbutton-nav") )` → `this.updateFxAView()`
- 条件付き依存: `if ( aEvent.target.classList.contains("profile-item") && aEvent.target.hasAttribute("profileid") && aEvent.target.getAttribute("profileid") !== String(Selectable...)` → `gSync.emitFxaToolbarTelemetry()`
- 条件付き依存: `if ( aEvent.target.classList.contains("profile-item") && aEvent.target.hasAttribute("profileid") && aEvent.target.getAttribute("profileid") !== String(Selectable...)` → `aEvent.target.closest()`
- 条件付き依存: `if ( aEvent.target.classList.contains("profile-item") && aEvent.target.hasAttribute("profileid") && aEvent.target.getAttribute("profileid") !== String(Selectable...)` → `this.launchProfile()`
- 参照: `SelectableProfileService.currentProfile?.id`, `TabContextMenu.contextTab`, `TabContextMenu.contextTab.multiselected`, `aEvent.sourceEvent`, `aEvent.target`, `aEvent.target.id`, `gBrowser.selectedTabs`

## populateSubView()
- 位置: async L571-791
- 役割: プロファイル用サブビューの見出し、テーマ色、編集・コピー・管理・作成のボタン、他プロファイルの一覧を組み立て直す。displayProfile が null なら現在のプロファイル向けの画面になる。
- 触るとき: プロファイルのサブビューのボタン並びや他プロファイル一覧の表示条件を変えるとき。
- 呼び出し先: `PanelMultiView.getViewNode()`, `backButton.setAttribute()`, `subview.querySelector()`, `this.bundle.GetStringFromName()`
- 条件付き依存: `if (SelectableProfileService.initialized)` → `SelectableProfileService.getAllProfiles()`
- 条件付き依存: `if (!editThisProfileButton)` → `document.createXULElement()`
- 条件付き依存: `if (!editThisProfileButton)` → `editThisProfileButton.classList.add()`
- 条件付き依存: `if (!editThisProfileButton)` → `editThisProfileButton.setAttribute()`
- 条件付き依存: `if (!footerSeparator)` → `document.createXULElement()`
- 条件付き依存: `if (!createProfileButton)` → `document.createXULElement()`
- 条件付き依存: `if (!createProfileButton)` → `createProfileButton.classList.add()`
- 条件付き依存: `if (!createProfileButton)` → `createProfileButton.setAttribute()`
- 条件付き依存: `if (!copyProfileButton)` → `document.createXULElement()`
- 条件付き依存: `if (!copyProfileButton)` → `copyProfileButton.classList.add()`
- 条件付き依存: `if (!copyProfileButton)` → `copyProfileButton.setAttribute()`
- 条件付き依存: `if (!manageProfilesButton)` → `document.createXULElement()`
- 条件付き依存: `if (!manageProfilesButton)` → `manageProfilesButton.classList.add()`
- 条件付き依存: `if (!manageProfilesButton)` → `manageProfilesButton.setAttribute()`
- 条件付き依存: `if (targetProfile)` → `subview.style.setProperty()`
- 条件付き依存: `if (targetProfile)` → `PanelMultiView.getViewNode()`
- 条件付き依存: `if (targetProfile)` → `currentProfileCard.style.setProperty()`
- 条件付き依存: `if (targetProfile)` → `targetProfile.getAvatarURL()`
- 条件付き依存: `if (!(targetProfile))` → `profilesHeader.removeAttribute()`
- 条件付き依存: `if (showProfileInfo)` → `subview.appendChild()`
- 条件付き依存: `if (showProfileInfo)` → `subview.querySelectorAll()`
- 条件付き依存: `if (showProfileInfo)` → `item.remove()`
- 条件付き依存: `if (showProfileInfo)` → `PanelMultiView.getViewNode( document, "profiles-subview-list-start-separator" )?.remove()`
- 条件付き依存: `if (showProfileInfo)` → `PanelMultiView.getViewNode()`
- 条件付き依存: `if (showProfileInfo)` → `PanelMultiView.getViewNode( document, "profiles-subview-list-header" )?.remove()`
- 条件付き依存: `if (showProfileInfo)` → `PanelMultiView.getViewNode(document, "profiles-subview-list")?.remove()`
- 条件付き依存: `if (displayProfile === null)` → `document.createXULElement()`
- 条件付き依存: `if (displayProfile === null)` → `subview.appendChild()`
- 条件付き依存: `if (displayProfile === null)` → `profilesListHeader.classList.add()`
- 条件付き依存: `if (displayProfile === null)` → `profilesListHeader.setAttribute()`
- 条件付き依存: `if (displayProfile === null)` → `btn.classList.add()`
- 条件付き依存: `if (displayProfile === null)` → `btn.setAttribute()`
- 条件付き依存: `if (displayProfile === null)` → `btn.style.setProperty()`
- 条件付き依存: `if (displayProfile === null)` → `profile.getAvatarURL()`
- 条件付き依存: `if (displayProfile === null)` → `profilesList.appendChild()`
- 条件付き依存: `if (!(showProfileInfo))` → `subview.insertBefore()`
- 参照: `SelectableProfileService.currentProfile`, `SelectableProfileService.initialized`, `backButton.style.fill`, `copyProfileButton.id`, `createProfileButton.id`, `currentProfileCard.hidden`, `editThisProfileButton.hidden`, `editThisProfileButton.id`, `footerSeparator.hidden`, `footerSeparator.id`, `headerSeparator.hidden`, `headerText.textContent`, `manageProfilesButton.id`, `profile.id`, `profile.name`, `profile.theme`, `profileIconEl.style.listStyleImage`, `profiles.length`, `profilesHeader.nextElementSibling`, `profilesHeader.style.backgroundColor`, `profilesHeader.style.color`, `profilesList.hidden`, `profilesList.id`, `profilesListHeader.hidden`, `profilesListHeader.id`, `profilesListStartSeparator.id`, `subviewBody.hidden`, `targetProfile.name`, `targetProfile.theme`, `targetProfile?.id`

## populateMoveTabMenu()
- 位置: async L793-839
- 役割: タブのメニューに、現在のプロファイル以外の各プロファイル向けの「移動」項目を作るか再利用して並べる。
- 触るとき: タブのコンテキストメニューのプロファイル移動項目が重複したり並びが崩れたりする問題を調べるとき。
- 呼び出し先: `JSON.stringify()`, `SelectableProfileService.getAllProfiles()`, `anchor.after()`, `document.getElementById()`, `existingItems.shift()`, `menuPopup.querySelectorAll()`, `menuitem.setAttribute()`, `remaining.remove()`
- 条件付き依存: `if (!menuitem)` → `document.createXULElement()`
- 条件付き依存: `if (!menuitem)` → `menuitem.setAttribute()`
- 参照: `SelectableProfileService.currentProfile`, `SelectableProfileService.initialized`, `currentProfile.id`, `menuitem.disabled`, `profile.id`, `profile.name`, `profiles.length`, `separator.hidden`
