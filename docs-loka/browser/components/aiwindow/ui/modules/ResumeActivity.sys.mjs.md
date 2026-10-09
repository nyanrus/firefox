# browser/components/aiwindow/ui/modules/ResumeActivity.sys.mjs

source: browser/components/aiwindow/ui/modules/ResumeActivity.sys.mjs
source-hash: 40050317566d317c28284fbb8f97959b3c7d9d29
lines: 66

## <module>
- 役割: AI Window の再開(resume)セクション用に、メモリ単位の非表示状態とセクションの非表示状態をプロセス内で保持する。

## dismissMemory()
- 位置: L21-23
- 役割: 指定の resume メモリ ID をこのセッションの dismiss 集合に追加する。
- 触るとき: 利用者が再開候補を閉じたときの記録先を変えるとき。Bug 2067871 で JourneyManager に移行する際に置き換わる。
- 呼び出し先: `_dismissedResumeMemoryIds.add()`

## isMemoryDismissed()
- 位置: L29-31
- 役割: 指定 ID がこのセッションで dismiss 済みかを集合から返す。
- 触るとき: 候補一覧の描画で閉じられた項目を除外しているのに、閉じたものが再表示されるとき。
- 呼び出し先: `_dismissedResumeMemoryIds.has()`

## hideSectionForSession()
- 位置: L40-42
- 役割: 空状態のため再開セクションを隠すフラグを立て、ブラウザ再起動まで保持する。
- 触るとき: 候補が無いときにセクションを隠す条件を変えるとき。Bug 2064698 で永続化する予定。

## clearSectionHiddenForSession()
- 位置: L47-49
- 役割: セクション非表示フラグを下ろし、再び表示できる状態に戻す。
- 触るとき: 候補が利用可能になった後も空状態の非表示が残るとき、その解除経路を追う。

## isSectionHiddenForSession()
- 位置: L54-56
- 役割: 再開セクションがこのセッションで非表示になっているかを返す。
- 触るとき: AI Window の描画側でセクションを出すかどうか判断する箇所を調べるとき。

## _clearDismissedResumeMemoriesForTesting()
- 位置: L59-61
- 役割: テスト用に dismiss 済みメモリの集合を空にする。
- 触るとき: dismiss 状態がテスト間で残って結果が前後関係に依存するとき、テストの前提を揃えるために使う。
- 呼び出し先: `_dismissedResumeMemoryIds.clear()`

## _resetResumeSectionHiddenForTesting()
- 位置: L63-65
- 役割: テスト用にセクション非表示フラグを false へ戻す。
- 触るとき: 非表示フラグが残ったままテストが順序に依存して失敗するとき、初期状態に戻す箇所を確認する。
