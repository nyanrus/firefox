# browser/actors/ThemePickerParent.sys.mjs

source: browser/actors/ThemePickerParent.sys.mjs
source-hash: 897977804305b82afee8033856936ac785b27a6e
lines: 161

## <module>
- 役割: テーマ選択 UI の状態(テーマ・外観・ネイティブテーマ)を読み書きする親側アクター。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## ThemePickerParent.getThemesManager()
- 位置: async L24-35
- 役割: インストール元ごとにテーマ一覧のマネージャーを一度だけ作って使い回す。失敗時はキャッシュを消す。
- 触るとき: テーマ一覧の取得元や再利用の仕方を変えるとき。
- 呼び出し先: `this.themesManagers.get()`
- 条件付き依存: `if (!managerPromise)` → `lazy.getThemesList({ installSource }).catch()`
- 条件付き依存: `if (!managerPromise)` → `lazy.getThemesList()`
- 条件付き依存: `if (!managerPromise)` → `this.themesManagers.delete()`
- 条件付き依存: `if (!managerPromise)` → `this.themesManagers.set()`

## ThemePickerParent.receiveMessage()
- 位置: async L37-62
- 役割: メッセージ名に応じて、初期状態・テーマ・外観・ネイティブテーマの取得や更新に振り分ける。
- 触るとき: ページから使える操作を増やすとき。
- 呼び出し先: `this.getActiveThemeId()`, `this.getAppearance()`, `this.getInitialState()`, `this.getNativeTheme()`, `this.updateAppearance()`, `this.updateNativeTheme()`, `this.updateTheme()`
- 参照: `message.data`, `message.name`

## ThemePickerParent.getInitialState()
- 位置: async L64-84
- 役割: テーマ一覧と現在のテーマ・外観・ネイティブテーマ、デバイスの外観をまとめて返す。ネイティブテーマの選択肢は Linux のみ。
- 触るとき: 初期表示の内容を変えるとき。
- 呼び出し先: `themesManager.getThemesInfo()`, `this.getActiveThemeId()`, `this.getAppearanceFromPref()`, `this.getNativeTheme()`, `this.getThemesManager()`
- 参照: `AppConstants.platform`, `Services.appinfo .contentThemeDerivedColorSchemeIsDark`
- XPCOM: `Services.appinfo`

## ThemePickerParent.updateTheme()
- 位置: async L86-90
- 役割: 指定テーマを有効にし、有効なテーマ ID を返す。
- 触るとき: テーマ切り替えの処理を変えるとき。
- 呼び出し先: `themesManager.updateThemeState()`, `this.getActiveThemeId()`, `this.getThemesManager()`

## ThemePickerParent.updateAppearance()
- 位置: async L92-111
- 役割: 外観の pref を device なら消し、light と dark なら数値で保存して、テレメトリを記録する。
- 触るとき: 外観の保存方法や記録内容を変えるとき。
- 呼び出し先: `Glean.themePicker.change.record()`, `this.getAppearance()`
- 条件付き依存: `if (appearance === "device")` → `Services.prefs.clearUserPref()`
- 条件付き依存: `if (!(appearance === "device"))` → `Services.prefs.setIntPref()`
- 参照: `result.appearance`
- XPCOM: `Services.prefs`

## ThemePickerParent.updateNativeTheme()
- 位置: async L113-125
- 役割: ネイティブテーマの pref を保存し、テレメトリを記録する。
- 触るとき: ネイティブテーマの保存を変えるとき。
- 呼び出し先: `Glean.themePicker.change.record()`, `Services.prefs.setBoolPref()`, `this.getNativeTheme()`
- 参照: `result.nativeTheme`
- XPCOM: `Services.prefs`

## ThemePickerParent.getActiveThemeId()
- 位置: L127-134
- 役割: 有効テーマの ID を pref から読む。未設定なら default-theme@mozilla.org。
- 触るとき: 現在のテーマ ID の取得方法を変えるとき。
- 呼び出し先: `Services.prefs.getStringPref()`
- XPCOM: `Services.prefs`

## ThemePickerParent.getAppearance()
- 位置: L136-138
- 役割: 外観の値を {appearance} の形で返す。
- 触るとき: 外観の取得結果の形を変えるとき。
- 呼び出し先: `this.getAppearanceFromPref()`

## ThemePickerParent.getAppearanceFromPref()
- 位置: L140-153
- 役割: 外観 pref の値を device、light、dark のいずれかに変換する。ユーザー設定がなければ device。
- 触るとき: 外観の判定条件を変えるとき。
- 呼び出し先: `Services.prefs.getIntPref()`, `Services.prefs.prefHasUserValue()`
- XPCOM: `Services.prefs`

## ThemePickerParent.getNativeTheme()
- 位置: L155-159
- 役割: ネイティブテーマの pref を読む。既定は false。
- 触るとき: ネイティブテーマの既定値を変えるとき。
- 呼び出し先: `Services.prefs.getBoolPref()`
- XPCOM: `Services.prefs`
