# browser/components/aiwindow/ui/components/agent-monitor-item/agent-monitor-item.mjs

source: browser/components/aiwindow/ui/components/agent-monitor-item/agent-monitor-item.mjs
source-hash: 223c886c6932be24279037724735ec77bf5734fe
lines: 1190

## <module>
- 役割: モニターカード(agent-monitor-item)の要素定義。作成フォームと表示カードの2モードを描画し、操作はカスタムイベントとしてホストへ渡す。
- 呼び出し先: `Array.from()`, `Math.floor()`, `Object.freeze()`, `String()`, `String(hour24).padStart()`, `String(minute).padStart()`, `customElements.define()`, `timeDate.setHours()`, `timeDate.toLocaleTimeString()`

## nextTimeOption()
- 位置: L87-97
- 役割: 現在時刻を30分刻みの次の時刻に切り上げ、HH:MM の文字列で返す。最後の枠を過ぎたら0時に戻す。
- 触るとき: 作成フォームの初期時刻がずれるとき、または時刻の刻みを変えるときに見る。
- 呼び出し先: `Math.ceil()`, `now.getHours()`, `now.getMinutes()`
- 参照: `TIME_OPTIONS.length`, `TIME_OPTIONS[0].value`, `TIME_OPTIONS[slot].value`

## AgentMonitorItem.constructor()
- 位置: L202-222
- 役割: プロパティの初期値を設定する。既定の時刻は nextTimeOption で決め、欄のエラーと名前の下書きは空にする。
- 触るとき: 新しいプロパティを足すとき、または作成フォームを開いた直後の初期表示を変えるときに見る。
- 呼び出し先: `nextTimeOption()`, `super()`
- 参照: `SCHEDULE_TYPES.DAILY`, `this.#draftName`, `this.agent`, `this.alertDescription`, `this.canResume`, `this.checkFrequency`, `this.draft`, `this.editing`, `this.expanded`, `this.fieldErrors`, `this.maxWatchUrls`, `this.mode`, `this.pageUrls`, `this.pendingUrl`, `this.pendingUrlError`, `this.scheduleTime`, `this.scheduleWeekday`, `this.selfContained`, `this.showLastResult`

## AgentMonitorItem.willUpdate()
- 位置: L227-235
- 役割: agent が変わったら #seedFromAgent で入力値を作り直す。agent か draft が変わったら #applyDraft で下書きを重ねる。
- 触るとき: カードの更新で入力内容が巻き戻る、または下書きが反映されないときに見る。
- 呼び出し先: `changed.has()`
- 条件付き依存: `if (changed.has("agent"))` → `this.#seedFromAgent()`
- 条件付き依存: `if (changed.has("agent") || changed.has("draft"))` → `this.#applyDraft()`

## AgentMonitorItem.disconnectedCallback()
- 位置: L237-242
- 役割: 保留中の下書き保存があれば先に送ってから、親の切断処理に進む。
- 触るとき: カードが外れたときに入力中の内容が失われるとき、または保存のタイミングを変えるときに見る。
- 呼び出し先: `super.disconnectedCallback()`
- 条件付き依存: `if (this.#draftPersistTimer)` → `this.#flushDraft()`
- 参照: `this.#draftPersistTimer`

## AgentMonitorItem.#seedFromAgent()
- 位置: L244-275
- 役割: agent の監視 URL(無ければ url)、条件、展開状態、スケジュールから入力値を作る。名前の下書きと各エラーは消す。
- 触るとき: モニターの編集を開いたときに値が正しく入らないとき、または agent の項目を足すときに見る。
- 呼び出し先: `seededUrls.filter()`, `u?.trim()`
- 条件付き依存: `if (schedule)` → `Number()`
- 参照: `schedule.frequency`, `schedule.time`, `schedule.weekday`, `this.#draftName`, `this.agent`, `this.agent?.schedule`, `this.alertDescription`, `this.checkFrequency`, `this.expanded`, `this.fieldErrors`, `this.pageUrls`, `this.pendingUrl`, `this.pendingUrlError`, `this.scheduleTime`, `this.scheduleWeekday`, `u?.trim().length`, `watchUrls?.length`

## AgentMonitorItem.#applyDraft()
- 位置: L280-315
- 役割: 下書きがあれば、編集中なら編集表示と展開を戻し、名前、条件、URL、保留中の URL、スケジュールを下書きの値で上書きする。
- 触るとき: 途中の編集が再表示で消えるとき、または下書きに新しい項目を足すときに見る。
- 条件付き依存: `if (schedule?.weekday !== undefined)` → `Number()`
- 参照: `schedule.frequency`, `schedule.time`, `schedule.weekday`, `schedule?.frequency`, `schedule?.time`, `schedule?.weekday`, `this.#draftName`, `this.alertDescription`, `this.checkFrequency`, `this.draft`, `this.editing`, `this.expanded`, `this.pageUrls`, `this.pendingUrl`, `this.scheduleTime`, `this.scheduleWeekday`

## AgentMonitorItem.#persistDraft()
- 位置: L323-336
- 役割: 作成中か編集中のときだけ下書きをホストへ送る。debounce を指定すると 250ms まとめて送り、指定しなければすぐ送る。
- 触るとき: 入力内容がホストに保存されないとき、または保存の回数が多すぎるときに見る。
- 呼び出し先: `setTimeout()`, `this.#clearDraftTimer()`, `this.#flushDraft()`
- 条件付き依存: `if (!debounce)` → `this.#flushDraft()`
- 参照: `this.#draftPersistTimer`, `this.editing`, `this.mode`

## AgentMonitorItem.#flushDraft()
- 位置: L338-354
- 役割: 現在の入力値を draft-change イベントの draft として送る。
- 触るとき: 下書きに項目を足すとき、または送られる内容が古いときに見る。
- 呼び出し先: `this.#clearDraftTimer()`, `this.#dispatch()`
- 参照: `this.#monitorName`, `this.alertDescription`, `this.checkFrequency`, `this.editing`, `this.pageUrls`, `this.pendingUrl`, `this.scheduleTime`, `this.scheduleWeekday`

## AgentMonitorItem.#discardDraft()
- 位置: L356-359
- 役割: draft-change で draft に null を入れて送り、ホスト側の下書きを消す。
- 触るとき: キャンセルや保存の後に下書きが残るときに見る。
- 呼び出し先: `this.#clearDraftTimer()`, `this.#dispatch()`

## AgentMonitorItem.#clearDraftTimer()
- 位置: L361-366
- 役割: 保留中の下書き保存タイマーを止める。
- 触るとき: 保存が後から走って古い下書きが戻るときに見る。
- 条件付き依存: `if (this.#draftPersistTimer)` → `clearTimeout()`
- 参照: `this.#draftPersistTimer`

## AgentMonitorItem.#dispatch()
- 位置: L368-372
- 役割: bubbles と composed を付けた CustomEvent を発火する。
- 触るとき: ホストに届くイベント名や detail の形を変えるときに見る。
- 呼び出し先: `this.dispatchEvent()`

## AgentMonitorItem.#monitorName()
- 位置: L374-376
- 役割: 名前の下書きがあればそれを、無ければ agent の monitorName を返す。
- 触るとき: 名前欄の値が保存されないとき、または agent の名前が反映されないときに見る。
- 参照: `this.#draftName`, `this.agent?.monitorName`

## AgentMonitorItem.focusName()
- 位置: L378-380
- 役割: 名前の入力欄にフォーカスを移す。
- 触るとき: 作成直後に名前欄へフォーカスが行かないときに見る。
- 呼び出し先: `this.shadowRoot?.querySelector()`, `this.shadowRoot?.querySelector(".monitor-name-input")?.focus()`

## AgentMonitorItem.#optionIcon()
- 位置: L392-394
- 役割: selfContained のときだけアイコンを返し、それ以外は nothing を返す。埋め込み時はネイティブの select を使うため、アイコンを外す。
- 触るとき: パネル内で選択肢の表示が崩れるとき、または選択肢にアイコンを出したいときに見る。
- 参照: `this.selfContained`

## AgentMonitorItem.#validateForm()
- 位置: L398-421
- 役割: 保留中の URL を先に追加してから、作成モードの名前、条件、監視ページを検査する。失敗した欄のキーを順に返す。URL のエラーがあれば pages を加える。
- 触るとき: 送信時の検査や必須項目を変えるとき、または送信時にフォーカスが違う欄へ行くときに見る。
- 呼び出し先: `["name", "condition", "pages"].filter()`, `invalid.includes()`, `this.#monitorName.trim()`, `this.alertDescription?.trim()`, `this.pendingUrl.trim()`
- 条件付き依存: `if (this.pendingUrl.trim())` → `this.#addUrl()`
- 条件付き依存: `if (this.pendingUrlError && !invalid.includes("pages"))` → `invalid.push()`
- 参照: `errors.condition`, `errors.name`, `errors.pages`, `this.fieldErrors`, `this.mode`, `this.pageUrls.length`, `this.pendingUrlError`

## AgentMonitorItem.#clearFieldError()
- 位置: L423-427
- 役割: 指定した欄のエラーを消す。
- 触るとき: 入力したのに欄のエラー表示が消えないときに見る。
- 参照: `this.fieldErrors`

## AgentMonitorItem.#focusField()
- 位置: L429-436
- 役割: 欄のキー(name、condition、pages)に対応する入力欄にフォーカスを移す。
- 触るとき: 送信エラー時のフォーカス先を変えるときに見る。
- 呼び出し先: `this.shadowRoot.querySelector()`, `this.shadowRoot.querySelector(selector)?.focus()`

## AgentMonitorItem.#onNameInput()
- 位置: L438-443
- 役割: 名前の下書きを更新し、名前欄のエラーを消す。入力中は保存をまとめ、変更の確定時はすぐ保存する。
- 触るとき: 名前欄の入力が保存されないとき、または保存のまとめ方を変えるときに見る。
- 呼び出し先: `this.#clearFieldError()`, `this.#persistDraft()`
- 参照: `event.target.value`, `event.type`, `this.#draftName`

## AgentMonitorItem.#onCardClick()
- 位置: L445-450
- 役割: クリックされた先がボタンでなければ、展開の切り替えを行う。
- 触るとき: カードのクリックで展開しない、またはボタンの押下が展開に伝わるときに見る。
- 呼び出し先: `e.target.closest()`, `this.#onToggle()`

## AgentMonitorItem.#onToggle()
- 位置: L452-455
- 役割: 展開状態を反転し、toggle イベントを送る。
- 触るとき: 展開の切り替えがホストに伝わらないときに見る。
- 呼び出し先: `this.#dispatch()`
- 参照: `this.expanded`

## AgentMonitorItem.#onEditToggle()
- 位置: L457-467
- 役割: 編集状態を反転する。編集を開いたときは下書きを保存し、閉じたときは下書きを捨てる。edit-toggle イベントを送る。
- 触るとき: 編集の開始と終了で入力内容が残る、または消えるときに見る。
- 呼び出し先: `this.#dispatch()`
- 条件付き依存: `if (this.editing)` → `this.#persistDraft()`
- 条件付き依存: `if (!(this.editing))` → `this.#discardDraft()`
- 参照: `this.editing`

## AgentMonitorItem.#onConditionInput()
- 位置: L469-473
- 役割: 条件の値を更新し、条件欄のエラーを消して下書きを保存する。入力中はまとめ、変更の確定時はすぐ保存する。
- 触るとき: 条件欄の入力が保存されないとき、または条件のエラーが消えないときに見る。
- 呼び出し先: `this.#clearFieldError()`, `this.#persistDraft()`
- 参照: `event.target.value`, `event.type`, `this.alertDescription`

## AgentMonitorItem.#onPresetClick()
- 位置: L475-479
- 役割: プリセットの文言を条件に設定し、条件欄のエラーを消して下書きをすぐ保存する。
- 触るとき: プリセットを押しても条件に反映されないときに見る。
- 呼び出し先: `this.#clearFieldError()`, `this.#persistDraft()`
- 参照: `this.alertDescription`

## AgentMonitorItem.#normalizeUrl()
- 位置: L484-497
- 役割: 空白を除き、スキームが無ければ https を付けて解析する。http か https でホストがあるものだけ正規化した href を返し、それ以外は空文字を返す。
- 触るとき: 受理する URL の条件を変えるとき、またはスキーム無しの入力が通らないときに見る。
- 呼び出し先: `url.trim()`, `value.includes()`
- 参照: `new URL(candidate).href`

## AgentMonitorItem.#isSameUrl()
- 位置: L501-507
- 役割: 両方を URL として解析し、href が一致すれば同じページとみなす。解析できなければ文字列の一致で判断する。
- 触るとき: 重複ページの判定が甘い、または厳しすぎるときに見る。
- 参照: `new URL(a).href`, `new URL(b).href`

## AgentMonitorItem.#validateAndNormalizeURL()
- 位置: L510-520
- 役割: URL を正規化し、結果が空なら無効 URL のエラー ID を、有効なら正規化した URL を返す。
- 触るとき: URL のエラー文言の種類を変えるときに見る。
- 呼び出し先: `this.#normalizeUrl()`

## AgentMonitorItem.#addUrl()
- 位置: L522-549
- 役割: 保留中の URL を正規化し、無効、重複、上限超過のいずれかならエラーを出す。問題がなければ監視ページに加え、保留欄とエラーを消して下書きを保存する。
- 触るとき: ページの追加が拒否される条件を変えるとき、または追加したのに表示されないときに見る。
- 呼び出し先: `this.#clearFieldError()`, `this.#isSameUrl()`, `this.#persistDraft()`, `this.#validateAndNormalizeURL()`, `this.pageUrls.some()`, `this.pendingUrl.trim()`
- 参照: `this.maxWatchUrls`, `this.pageUrls`, `this.pageUrls.length`, `this.pendingUrl`, `this.pendingUrlError`

## AgentMonitorItem.#removeUrl()
- 位置: L551-554
- 役割: 指定した URL を監視ページから外し、下書きを保存する。
- 触るとき: ページを外しても保存されないときに見る。
- 呼び出し先: `this.#persistDraft()`, `this.pageUrls.filter()`
- 参照: `this.pageUrls`

## AgentMonitorItem.#displayUrl()
- 位置: L556-562
- 役割: URL のホスト名を返す。解析できなければ元の文字列を返す。
- 触るとき: チップの表示名が長すぎる、または崩れるときに見る。
- 参照: `new URL(url).hostname`

## AgentMonitorItem.#onPendingUrlInput()
- 位置: L564-570
- 役割: 保留中の URL を更新し、URL のエラーを消して下書きをまとめて保存する。
- 触るとき: URL 入力欄の入力が保存されないとき、またはエラーが消えないときに見る。
- 呼び出し先: `this.#persistDraft()`
- 参照: `event.target.value`, `this.pendingUrl`, `this.pendingUrlError`

## AgentMonitorItem.#onPendingUrlKeydown()
- 位置: L572-578
- 役割: Enter の既定動作を止めて、保留中の URL を追加する。
- 触るとき: Enter で追加されない、またはフォームが送信されてしまうときに見る。
- 呼び出し先: `event.preventDefault()`, `this.#addUrl()`
- 参照: `event.key`

## AgentMonitorItem.#onCancel()
- 位置: L580-585
- 役割: 保留中の下書き保存タイマーを止め、cancel イベントを送る。
- 触るとき: キャンセル後に古い下書きが保存されるときに見る。
- 呼び出し先: `this.#clearDraftTimer()`, `this.#dispatch()`

## AgentMonitorItem.#onSubmit()
- 位置: async L587-616
- 役割: 検査を通ったら、モード、ID、名前、条件、URL、スケジュールを submit イベントで送る。作成モードなら展開と確認を求める。編集中ならそのあと編集を終える。検査に失敗したら最初の不正な欄にフォーカスする。
- 触るとき: 保存する内容や送る項目を変えるとき、または保存後に編集を閉じる動きを確かめるときに見る。
- 呼び出し先: `this.#clearDraftTimer()`, `this.#dispatch()`, `this.#validateForm()`, `this.alertDescription.trim()`
- 条件付き依存: `if (invalidFields.length)` → `this.#focusField()`
- 条件付き依存: `if (this.editing)` → `this.#dispatch()`
- 参照: `invalidFields.length`, `this.#monitorName`, `this.agent?.id`, `this.checkFrequency`, `this.editing`, `this.mode`, `this.pageUrls`, `this.scheduleTime`, `this.scheduleWeekday`, `this.updateComplete`

## AgentMonitorItem.#renderStatusChip()
- 位置: L618-622
- 役割: monitor-status-chip を描画し、agent の状態の種類を渡す。
- 触るとき: 状態チップの表示が合わないときに見る。
- 呼び出し先: `html()`
- 参照: `this.agent?.status?.kind`

## AgentMonitorItem.#renderLastCheckedCondition()
- 位置: L624-641
- 役割: 履歴の最新項目を正規化し、その結果状態に対応する最終結果のラベルを描画する。履歴が無ければ何も描画しない。
- 触るとき: 最終結果の表示が出ない、または変更履歴の表示と食い違うときに見る。
- 呼び出し先: `html()`, `this.#transformHistoryItem()`
- 参照: `mostRecentItem.conditionMet`, `normalizedItem.resultState`, `this.agent?.history`

## AgentMonitorItem.#renderFieldError()
- 位置: L643-651
- 役割: エラーがあればその文言を表示し、無ければ nothing を返す。引数があれば JSON で渡す。
- 触るとき: エラー文言が出ない、または引数が渡らないときに見る。
- 呼び出し先: `JSON.stringify()`, `html()`
- 参照: `error.args`, `error.id`

## AgentMonitorItem.#renderConditionField()
- 位置: L653-684
- 役割: 条件のテキストエリアと、プリセットのチップ行を描画する。選択中の文言には selected を付ける。
- 触るとき: 条件欄の見た目やプリセットの並びを変えるときに見る。
- 呼び出し先: `html()`, `presets.map()`, `this.#onPresetClick()`, `this.#renderFieldError()`
- 参照: `presets.length`, `this.#onConditionInput`, `this.agent?.conditionPresets`, `this.alertDescription`, `this.fieldErrors.condition`

## AgentMonitorItem.#renderPagesField()
- 位置: L686-737
- 役割: URL 入力欄、追加ボタン、エラー、追加済みページのチップを描画する。チップの表示名は監視ページのタイトルで、無ければホスト名にする。
- 触るとき: 監視ページの入力欄や一覧の見た目を変えるときに見る。
- 呼び出し先: `JSON.stringify()`, `html()`, `this.#addUrl()`, `this.#displayUrl()`, `this.#removeUrl()`, `this.#renderFieldError()`, `this.pageUrls.map()`
- 参照: `this.#onPendingUrlInput`, `this.#onPendingUrlKeydown`, `this.agent?.watchUrlTitles`, `this.fieldErrors.pages`, `this.maxWatchUrls`, `this.pageUrls.length`, `this.pendingUrl`, `this.pendingUrlError`

## AgentMonitorItem.#transformHistoryItem()
- 位置: L739-796
- 役割: 履歴項目を表示用に変換する。日時を整え、エラーは確認できなかった結果、条件一致は一致、不一致は不一致として扱う。タイムスタンプが無い項目は null を返す。エラーの生の文字列は表示しない。
- 触るとき: 履歴の日時、結果、説明文の表示を変えるとき、またはエラー時の表示が意図と違うときに見る。
- 呼び出し先: `date.toLocaleDateString()`, `date.toLocaleTimeString()`
- 条件付き依存: `if (item.status === "error")` → `monitorErrorL10nId()`
- 参照: `RESULT_STATES.COULD_NOT_CHECK`, `RESULT_STATES.MET`, `RESULT_STATES.NOT_MET`, `item.checkedAt`, `item.conditionMet`, `item.errorCode`, `item.resultExplanation`, `item.status`

## AgentMonitorItem.#renderHistory()
- 位置: L798-842
- 役割: 変換済みの履歴項目を、日時、結果バッジ、説明の順の行として描画する。履歴が無ければ何も描画しない。
- 触るとき: 変更履歴の一覧の並びや表示が合わないときに見る。
- 呼び出し先: `historyItems.map()`, `html()`, `this.#transformHistoryItem()`
- 条件付き依存: `if (normalizedItem.noteL10nId)` → `html()`
- 条件付き依存: `if (normalizedItem.note)` → `html()`
- 参照: `historyItems.length`, `normalizedItem.note`, `normalizedItem.noteL10nId`, `normalizedItem.resultState`, `normalizedItem.when`, `this.agent?.history`

## AgentMonitorItem.#onFrequencyChange()
- 位置: L844-847
- 役割: 頻度を選択欄の値で更新し、下書きを保存する。
- 触るとき: 頻度を変えても保存されないときに見る。
- 呼び出し先: `this.#persistDraft()`
- 参照: `event.target.value`, `this.checkFrequency`

## AgentMonitorItem.#onScheduleTimeChange()
- 位置: L849-852
- 役割: 時刻を選択欄の値で更新し、下書きを保存する。
- 触るとき: 時刻の変更が保存されないときに見る。
- 呼び出し先: `this.#persistDraft()`
- 参照: `event.target.value`, `this.scheduleTime`

## AgentMonitorItem.#onWeekdayChange()
- 位置: L854-857
- 役割: 曜日を数値にして更新し、下書きを保存する。
- 触るとき: 曜日の変更が保存されないときに見る。
- 呼び出し先: `Number()`, `this.#persistDraft()`
- 参照: `event.target.value`, `this.scheduleWeekday`

## AgentMonitorItem.#renderScheduleSummary()
- 位置: L859-904
- 役割: agent のスケジュールを、週次なら曜日と時刻、それ以外は毎日の時刻の文言で描画する。スケジュールが無ければ何も描画しない。
- 触るとき: スケジュールの要約文が合わないとき、または曜日や時刻の表示形式を変えるときに見る。
- 呼び出し先: `JSON.stringify()`, `html()`, `schedule.time.split()`, `schedule.time.split(":").map()`, `timeDate.getTime()`, `timeDate.setHours()`
- 条件付き依存: `if (fluentId)` → `html()`
- 条件付き依存: `if (fluentId)` → `JSON.stringify()`
- 条件付き依存: `if (fluentId)` → `timeDate.getTime()`
- 参照: `SCHEDULE_TYPES.WEEKLY`, `schedule.frequency`, `schedule.weekday`, `this.agent?.schedule`

## AgentMonitorItem.#renderTimeField()
- 位置: L906-928
- 役割: 時刻の選択欄を描画する。選択肢は TIME_OPTIONS の30分刻みで、アイコンは埋め込み時に外す。
- 触るとき: 時刻の選択肢や表示を変えるときに見る。
- 呼び出し先: `TIME_OPTIONS.map()`, `html()`, `this.#optionIcon()`
- 参照: `opt.label`, `opt.value`, `this.#onScheduleTimeChange`, `this.scheduleTime`

## AgentMonitorItem.#renderScheduler()
- 位置: L930-982
- 役割: 頻度の選択欄と、週次のときだけ出る曜日の選択欄、時刻欄を並べて描画する。
- 触るとき: スケジュール入力の並びや、曜日欄を出す条件を変えるときに見る。
- 呼び出し先: `WEEKDAYS.map()`, `html()`, `this.#optionIcon()`, `this.#renderTimeField()`
- 参照: `SCHEDULE_TYPES.DAILY`, `SCHEDULE_TYPES.WEEKLY`, `day.ftlId`, `day.value`, `this.#onFrequencyChange`, `this.#onWeekdayChange`, `this.checkFrequency`, `this.scheduleWeekday`

## AgentMonitorItem.#renderCreate()
- 位置: L984-1037
- 役割: 作成モードのカードを描画する。名前、条件、監視ページ、スケジュール、必須の注記、キャンセルと作成のボタンを並べる。selfContained のときはタイトルも出す。
- 触るとき: 新規作成フォームの項目や並びを変えるときに見る。
- 呼び出し先: `html()`, `this.#renderConditionField()`, `this.#renderFieldError()`, `this.#renderPagesField()`, `this.#renderScheduler()`
- 参照: `this.#monitorName`, `this.#onCancel`, `this.#onNameInput`, `this.#onSubmit`, `this.fieldErrors.name`, `this.selfContained`

## AgentMonitorItem.#renderDisplay()
- 位置: L1039-1067
- 役割: 表示モードのカードを描画する。状態チップ、名前、必要なら最終結果、展開ボタンを並べ、展開中は #renderExpand を続ける。カード全体のクリックでも展開を切り替える。
- 触るとき: 一覧のカードの見た目や展開の操作を変えるときに見る。
- 呼び出し先: `html()`, `this.#renderExpand()`, `this.#renderLastCheckedCondition()`, `this.#renderStatusChip()`
- 参照: `agent.monitorName`, `this.#onCardClick`, `this.#onToggle`, `this.agent`, `this.expanded`, `this.showLastResult`

## AgentMonitorItem.#renderExpand()
- 位置: L1069-1176
- 役割: 展開部を描画する。編集中は条件、ページ、スケジュールの入力欄を出し、通常時は条件、ページ、スケジュールの要約と履歴を出す。編集、一時停止か再開、今すぐ確認、削除、保存かキャンセルのボタンを状況に応じて出す。
- 触るとき: 操作ボタンを増やすとき、または一時停止の再開ボタンを無効にする条件を変えるときに見る。再開は canResume が false のとき押せず、一時停止は常に押せる。
- 呼び出し先: `agent.watchUrls.map()`, `e.stopPropagation()`, `html()`, `this.#dispatch()`, `this.#displayUrl()`, `this.#renderConditionField()`, `this.#renderHistory()`, `this.#renderPagesField()`, `this.#renderScheduleSummary()`, `this.#renderScheduler()`
- 参照: `agent.condition`, `agent.id`, `agent.status?.kind`, `agent.watchUrlTitles`, `agent.watchUrls?.length`, `this.#onEditToggle`, `this.#onSubmit`, `this.agent`, `this.canResume`, `this.editing`

## AgentMonitorItem.render()
- 位置: L1178-1186
- 役割: モードに応じて作成フォームか表示カードを描画し、カード用のスタイルシートを読み込む。
- 触るとき: カード全体のスタイルの読み込みや、モードの切り替え方を変えるときに見る。
- 呼び出し先: `html()`, `this.#renderCreate()`, `this.#renderDisplay()`
- 参照: `this.mode`
