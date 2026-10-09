# browser/extensions/webcompat/injections/js/bug1994562-shim-mstp-mstg-on-window.js

source: browser/extensions/webcompat/injections/js/bug1994562-shim-mstp-mstg-on-window.js
source-hash: adb5d406bb10abecb72daa7fb67ebbff39058cf1
lines: 270

## <module>
- 役割: (未記入)

## MediaStreamTrackProcessor()
- 位置: L32-183
- 役割: (未記入)
- 触るとき: (未記入)
- 参照: `options?.track`, `track.kind`

## start()
- 位置: L39-61
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `Promise.resolve() .then()`, `controller.close()`, `document.createElement()`, `performance.now()`, `src.canvas.getContext()`, `src.video.play()`, `track.addEventListener()`, `tracks.push()`
- 参照: `src.canvas`, `src.ctx`, `src.t1`, `src.track`, `src.video`, `src.video.onloadedmetadata`, `src.video.srcObject`, `src.video.videoHeight`, `src.video.videoWidth`

## pull()
- 位置: L62-90
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `controller.enqueue()`, `performance.now()`, `requestAnimationFrame()`, `src.ctx.drawImage()`, `track.getSettings()`
- 条件付き依存: `if (track.readyState == "ended")` → `controller.close()`
- 条件付き依存: `if (track.readyState == "ended")` → `Promise.resolve()`
- 参照: `src.canvas`, `src.t1`, `src.video`, `track.getSettings().frameRate`, `track.readyState`

## waitUntil()
- 位置: L69-78
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `performance.now()`, `requestAnimationFrame()`
- 条件付き依存: `if ( track.readyState == "ended" || performance.now() - src.t1 >= 1000 / fps )` → `r()`
- 参照: `src.t1`, `track.readyState`

## start()
- 位置: L95-130
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `Promise.resolve() .then()`, `controller.close()`, `src.ac .createMediaStreamSource()`, `src.ac .createMediaStreamSource(new MediaStream(tracks)) .connect()`, `src.ac.audioWorklet.addModule()`, `src.arrays.push()`, `src.node.port.addEventListener()`, `track.addEventListener()`, `tracks.push()`, `worklet.toString()`
- 参照: `src.ac`, `src.arrays`, `src.node`

## worklet()
- 位置: L103-113
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `registerProcessor()`

## Processor.process()
- 位置: L107-110
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.port.postMessage()`

## pull()
- 位置: L131-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `(src.node.port.onmessage = r).then()`, `Promise.resolve()`, `Promise.resolve() .then()`, `channels.reduce()`, `controller.enqueue()`, `joined.set()`, `src.arrays.shift()`, `transfer.push()`
- 条件付き依存: `if (track.readyState == "ended")` → `controller.close()`
- 条件付き依存: `if (track.readyState == "ended")` → `Promise.resolve()`
- 参照: `a.length`, `b.length`, `channels.length`, `channels[0].length`, `joined.buffer`, `src.ac.currentTime`, `src.ac.sampleRate`, `src.arrays.length`, `src.node.port.onmessage`, `track.readyState`

## loop()
- 位置: L141-151
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`
- 条件付き依存: `if (track.readyState == "ended")` → `Promise.resolve()`
- 条件付き依存: `if (!src.arrays.length)` → `new Promise( _r => (src.node.port.onmessage = _r) ).then()`
- 参照: `src.arrays.length`, `src.node.port.onmessage`, `track.readyState`

## MediaStreamTrackGenerator()
- 位置: L188-267
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (options.kind == "video")` → `document.createElement()`
- 条件付き依存: `if (options.kind == "video")` → `canvas.getContext()`
- 条件付き依存: `if (options.kind == "video")` → `canvas.captureStream().getVideoTracks()`
- 条件付き依存: `if (options.kind == "video")` → `canvas.captureStream()`
- 条件付き依存: `if (options.kind == "audio")` → `ac.createMediaStreamDestination()`
- 条件付き依存: `if (options.kind == "audio")` → `dest.stream.getAudioTracks()`
- 参照: `options.kind`, `options?.kind`, `track.writable`

## write()
- 位置: L197-202
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ctx.drawImage()`, `frame.close()`
- 参照: `canvas.height`, `canvas.width`, `frame.displayHeight`, `frame.displayWidth`

## start()
- 位置: L211-252
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `Promise.resolve()`, `Promise.resolve() .then()`, `ac.audioWorklet.addModule()`, `sink.node.connect()`, `worklet.toString()`
- 参照: `sink.arrays`, `sink.node`

## worklet()
- 位置: L215-242
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `registerProcessor()`

## Processor.constructor()
- 位置: L219-226
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `super()`
- 参照: `this.arrayOffset`, `this.arrays`, `this.emptyArray`, `this.port.onmessage`

## this.port.onmessage()
- 位置: L223-224
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.arrays.push()`

## Processor.process()
- 位置: L227-239
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if ( !this.array || this.arrayOffset >= this.array.length )` → `this.arrays.shift()`
- 参照: `output.length`, `this.array`, `this.array.length`, `this.arrayOffset`, `this.emptyArray`

## write()
- 位置: L253-262
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `audioData.close()`, `audioData.copyTo()`, `sink.node.port.postMessage()`, `transfer.push()`
- 参照: `array.buffer`, `audioData.numberOfChannels`, `audioData.numberOfFrames`
