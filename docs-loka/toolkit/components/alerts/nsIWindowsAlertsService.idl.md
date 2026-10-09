# nsIWindowsAlertNotification (toolkit/components/alerts/nsIWindowsAlertsService.idl)

source: toolkit/components/alerts/nsIWindowsAlertsService.idl
source-hash: 4ba31af293a44a09819fcd3cf766836d2a7f839c

- 継承: nsIAlertNotification
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/asrouter/modules/ToastNotification.sys.mjs`](../../../browser/components/asrouter/modules/ToastNotification.sys.mjs.md)

## メソッド / 属性
- `attribute nsIWindowsAlertNotification_ImagePlacement imagePlacement`: Enum to specify image placement we want in the notification. n.b. in the
- `attribute AString imagePathUnchecked`: An image file on disk to use in the notification. This allows callers to

# nsIWindowsAlertsService (toolkit/components/alerts/nsIWindowsAlertsService.idl)

source: toolkit/components/alerts/nsIWindowsAlertsService.idl
source-hash: 4ba31af293a44a09819fcd3cf766836d2a7f839c

- 継承: nsIAlertsService
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/BrowserContentHandler.sys.mjs`](../../../browser/components/BrowserContentHandler.sys.mjs.md), [`browser/modules/BackgroundTask_uninstall.sys.mjs`](../../../browser/modules/BackgroundTask_uninstall.sys.mjs.md)

## メソッド / 属性
- `Promise handleWindowsTag(AString aWindowsTag)`: If callbacks for the given Windows-specific tag string will be handled by
- `AString getXmlStringForWindowsAlert(nsIAlertNotification aAlert, AString aWindowsTag)`: Get the Windows-specific XML generated for the given alert.
- `void removeAllNotificationsForInstall()`: Removes all action center and snoozed notifications associated with this
