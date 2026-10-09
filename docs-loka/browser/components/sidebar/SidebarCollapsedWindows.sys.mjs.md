# browser/components/sidebar/SidebarCollapsedWindows.sys.mjs

source: browser/components/sidebar/SidebarCollapsedWindows.sys.mjs
source-hash: b381728cb5d63205a1738370b59c0cafc4301578
lines: 187

## <module>
- 役割: (未記入)
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`

## SidebarCollapsedWindowsImpl.#ensureInitialized()
- 位置: L34-57
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `ChromeUtils.generateQI()`, `Services.obs.addObserver()`, `this.#hydrate()`
- 参照: `this.#initialized`, `this.#observer`
- XPCOM: `Services.obs`

## SidebarCollapsedWindowsImpl.observe()
- 位置: L43-53
- 役割: (未記入)
- 触るとき: (未記入)
- 条件付き依存: `if (topic === "domwindowclosed")` → `self.#onWindowClosed()`
- 条件付き依存: `if (topic === "quit-application-granted")` → `Services.obs.removeObserver()`
- 参照: `self.#observer`
- XPCOM: `Services.obs`

## SidebarCollapsedWindowsImpl.#hydrate()
- 位置: L59-81
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.parse()`, `Object.entries()`, `Services.prefs.getStringPref()`, `liveIds.has()`, `this.#collectLiveWindowIds()`
- 条件付き依存: `if (liveIds.has(id) && collapsed)` → `this.#map.set()`
- 条件付き依存: `if (!(liveIds.has(id) && collapsed))` → `liveIds.has()`
- 条件付き依存: `if (trimmed)` → `this.#persist()`
- XPCOM: `Services.prefs`

## SidebarCollapsedWindowsImpl.#collectLiveWindowIds()
- 位置: L83-92
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SessionStore.getWindowId()`, `lazy.SessionStore.getWindows()`
- 条件付き依存: `if (id)` → `ids.add()`

## SidebarCollapsedWindowsImpl.#persist()
- 位置: L94-99
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `JSON.stringify()`, `Object.fromEntries()`, `Services.prefs.setStringPref()`
- 参照: `this.#map`
- XPCOM: `Services.prefs`

## SidebarCollapsedWindowsImpl.#setCollapsedById()
- 位置: L101-121
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.SessionStore.getWindowById()`, `this.#ensureInitialized()`, `this.#map.get()`, `this.#persist()`, `this.dispatchEvent()`
- 条件付き依存: `if (collapsed)` → `this.#map.set()`
- 条件付き依存: `if (!(collapsed))` → `this.#map.delete()`

## SidebarCollapsedWindowsImpl.#onWindowClosed()
- 位置: L123-146
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.SessionStore.getWindowId()`, `lazy.SessionStore.getWindows()`, `this.#map.delete()`, `this.#map.has()`, `this.#persist()`, `this.dispatchEvent()`
- 参照: `lazy.SessionStore.getWindows({ private: false }).length`

## SidebarCollapsedWindowsImpl.isCollapsed()
- 位置: L148-155
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.PrivateBrowsingUtils.isWindowPrivate()`, `lazy.SessionStore.getWindowId()`, `this.#ensureInitialized()`, `this.#map.get()`

## SidebarCollapsedWindowsImpl.collapseWindow()
- 位置: L157-165
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SessionStore.getWindowId()`
- 条件付き依存: `if (id)` → `this.#setCollapsedById()`

## SidebarCollapsedWindowsImpl.expandWindow()
- 位置: L167-175
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `lazy.SessionStore.getWindowId()`
- 条件付き依存: `if (id)` → `this.#setCollapsedById()`

## SidebarCollapsedWindowsImpl.collapseWindowById()
- 位置: L177-179
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setCollapsedById()`

## SidebarCollapsedWindowsImpl.expandWindowById()
- 位置: L181-183
- 役割: (未記入)
- 触るとき: (未記入)
- 呼び出し先: `this.#setCollapsedById()`
