# browser/actors/BrowserProcessChild.sys.mjs

source: browser/actors/BrowserProcessChild.sys.mjs
source-hash: 1f2b7d3cadcb398d4afe6d65f114dd6e9724227c
lines: 39

## <module>
- 役割: コンテンツプロセス側のブラウザ全体アクター。about:home 起動キャッシュの入力ストリームを受け取り、WebRTC の通知を WebRTCChild へ流す。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## BrowserProcessChild.receiveMessage()
- 位置: L14-25
- 役割: AboutHomeStartupCache:InputStreams を受け、ページとスクリプトの入力ストリームを about:home キャッシュへ渡す。
- 触るとき: about:home の起動キャッシュがプロセス間で渡らない問題を調べるときに見る。
- 呼び出し先: `lazy.AboutHomeStartupCacheChild.init()`
- 参照: `message.data`, `message.name`

## BrowserProcessChild.observe()
- 位置: L27-37
- 役割: getUserMedia、PeerConnection、録音デバイスなどの通知を、WebRTCChild の observe へそのまま渡す。
- 触るとき: カメラやマイクの共有通知が子プロセス側で届かない問題を調べるときに見る。
- 呼び出し先: `lazy.WebRTCChild.observe()`
