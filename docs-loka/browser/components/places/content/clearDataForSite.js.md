# browser/components/places/content/clearDataForSite.js

source: browser/components/places/content/clearDataForSite.js
source-hash: 671a46ccc026690c1b43c73795b8fcbb08b1a064
lines: 38

## <module>
- 役割: サイトのデータ削除ダイアログ。window.arguments の値を表示し、受諾で ForgetAboutSite によりホストのデータを削除、キャンセルで何もせず閉じる。
- 呼び出し先: `ChromeUtils.defineESModuleGetters()`, `document.addEventListener()`, `document.getElementById()`, `document.l10n.setArgs()`, `e.preventDefault()`, `lazy.ForgetAboutSite.removeDataFromBaseDomain()`, `lazy.ForgetAboutSite.removeDataFromBaseDomain(retVals.host).catch()`, `window.close()`
