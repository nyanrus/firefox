# browser/components/extensions/parent/ext-commands.js

source: browser/components/extensions/parent/ext-commands.js
source-hash: 4b98268ed1146cd77382c4dc099e98fe09278067
lines: 88

## <module>
- 役割: commands API を実装し、拡張のキーボードショートカットの登録・更新・リセットと onCommand・onChanged イベントを提供する。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## onCommand()
- 位置: L13-29
- 役割: command イベントを購読し、アクティブタブへアクティブタブ権限を付与したうえで commandName とタブ情報を fire する。
- 触るとき: ショートカットを押したときに拡張へ渡されるタブ情報や権限付与の挙動を変えるとき。
- 呼び出し先: `this.on()`

## listener()
- 位置: L17-21
- 役割: ショートカットのコマンド発火ごとに、現在のアクティブタブへ権限を付けて commandName と変換済みタブを送る。
- 触るとき: onCommand の発火時に拡張がアクティブタブを参照できない問題を調べるとき。
- 呼び出し先: `fire.async()`, `tabManager.addActiveTabPermission()`, `tabManager.convert()`
- 参照: `tabTracker.activeTab`

## unregister()
- 位置: L24-24
- 役割: onCommand の購読を解除する。
- 触るとき: onCommand リスナーが解除されず残るときに確認する。
- 呼び出し先: `this.off()`

## convert()
- 位置: L25-27
- 役割: 永続イベントの fire 関数を差し替え、再起動後も新しい fire に送れるようにする。
- 触るとき: 拡張がリロードされた後に onCommand が古い fire に送られる問題を調べるとき。

## onChanged()
- 位置: L30-41
- 役割: shortcutChanged を購読し、変更内容 changeInfo を fire する。
- 触るとき: ショートカット変更の通知内容を変えるとき、または onChanged が届かないときに見る。
- 呼び出し先: `this.on()`

## listener()
- 位置: L31-33
- 役割: shortcutChanged の changeInfo をそのまま fire.async に渡す。
- 触るとき: onChanged に渡る変更情報の形式を変えるとき。
- 呼び出し先: `fire.async()`

## unregister()
- 位置: L36-36
- 役割: shortcutChanged の購読を解除する。
- 触るとき: onChanged リスナーが解除されず残るときに確認する。
- 呼び出し先: `this.off()`

## convert()
- 位置: L37-39
- 役割: onChanged の fire 関数を差し替える。
- 触るとき: onChanged の fire が古いままになる問題を調べるとき。

## onUninstall()
- 位置: L44-46
- 役割: 拡張のアンインストール時に、そのコマンドの保存済みショートカットを storage から削除する。
- 触るとき: アンインストール後にショートカット設定が残る問題を調べるとき。
- 呼び出し先: `ExtensionShortcuts.removeCommandsFromStorage()`

## onManifestEntry()
- 位置: async L48-57
- 役割: ExtensionShortcuts を生成し、コマンドを読み込んで登録する。コマンド発火と変更は this.emit で上の購読へ流す。
- 触るとき: manifest の commands 定義をどう読み込んで登録するかを変えるとき。
- 呼び出し先: `shortcuts.loadCommands()`, `shortcuts.register()`
- 参照: `this.extension`, `this.extension.shortcuts`

## onCommand()
- 位置: L51-51
- 役割: ExtensionShortcuts からのコマンド発火を、command イベントとして emit に渡す。
- 触るとき: ショートカットのコマンド名が拡張側に届かない問題を調べるとき。
- 呼び出し先: `this.emit()`

## onShortcutChanged()
- 位置: L52-52
- 役割: ショートカット変更の情報を shortcutChanged イベントとして emit に渡す。
- 触るとき: ショートカット変更の通知が拡張側に届かない問題を調べるとき。
- 呼び出し先: `this.emit()`

## onShutdown()
- 位置: L59-61
- 役割: 拡張の終了時に、登録済みのショートカットを解除する。
- 触るとき: 拡張の無効化・終了後にショートカットが残る問題を調べるとき。
- 呼び出し先: `this.extension.shortcuts.unregister()`

## getAPI()
- 位置: L63-86
- 役割: browser.commands の API オブジェクトを作り、getAll・update・reset・openShortcutSettings と onCommand・onChanged の EventManager を公開する。
- 触るとき: 拡張から見える commands API のメソッド名や引数を追加・変更するとき。
- 呼び出し先: `new EventManager({ context, module: "commands", event: "onChanged", extensionApi: this, }).api()`, `new EventManager({ context, module: "commands", event: "onCommand", inputHandling: true, extensionApi: this, }).api()`

## getAll()
- 位置: L66-66
- 役割: 拡張に定義された全コマンドの一覧を ExtensionShortcuts から取得する。
- 触るとき: commands.getAll の結果に含まれる内容を調べるとき。
- 呼び出し先: `this.extension.shortcuts.allCommands()`

## update()
- 位置: L67-67
- 役割: 指定されたコマンドのショートカットを新しいキーで更新する。
- 触るとき: 拡張がショートカットを変更したときの保存や検証の挙動を見直すとき。
- 呼び出し先: `this.extension.shortcuts.updateCommand()`

## reset()
- 位置: L68-68
- 役割: 指定されたコマンドのショートカットを既定値に戻す。
- 触るとき: 拡張がショートカットを初期化できない問題を調べるとき。
- 呼び出し先: `this.extension.shortcuts.resetCommand()`

## openShortcutSettings()
- 位置: L69-70
- 役割: ブラウザのショートカット設定画面を開く。
- 触るとき: 設定画面の開き方や遷移先を変えるとき。
- 呼び出し先: `this.extension.shortcuts.openShortcutSettings()`
