# browser/components/asrouter/content-src/schemas/extract-test-corpus.js

source: browser/components/asrouter/content-src/schemas/extract-test-corpus.js
source-hash: 597d4119f2f82eb5cd4cb8838441021b3ee9a9b1
lines: 59

## <module>
- 役割: ASRouter のメッセージ一覧を JSON ファイルに書き出し、テストのコーパスを作る Firefox 内部スクリプト。
- 呼び出し先: `ChromeUtils.importESModule()`, `PathUtils.join()`, `Services.dirsvc.get()`, `Services.tm.spinEventLoopUntil()`, `main()`

## filter()
- 位置: L29-29
- 役割: PanelTestProvider の出力を toast_notification テンプレートだけに絞る条件。
- 触るとき: コーパスに含めるテンプレートを変えるとき。
- 参照: `message.template`

## main()
- 位置: async L34-50
- 役割: コーパスの各プロバイダからメッセージを取り出して CORPUS_DIR に JSON で書き出す。終わったら exit を立てる。
- 触るとき: コーパスのファイル名や出力先を変えるとき、またはコーパスが空になると調べるとき。
- 呼び出し先: `IOUtils.makeDirectory()`, `IOUtils.writeUTF8()`, `JSON.stringify()`, `PathUtils.join()`, `messages.filter()`, `provider.getMessages()`
- 参照: `entry.filter`
