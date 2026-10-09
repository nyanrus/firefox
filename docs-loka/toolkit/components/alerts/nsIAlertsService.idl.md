# nsIAlertAction (toolkit/components/alerts/nsIAlertsService.idl)

source: toolkit/components/alerts/nsIAlertsService.idl
source-hash: 0402d78ff5abf5116149f92366a0e3517924bbd4

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/aiwindow/models/agents/MonitorAgent.sys.mjs`](../../../browser/components/aiwindow/models/agents/MonitorAgent.sys.mjs.md)

## メソッド / 属性
- `readonly attribute AString action`: Returns a string identifying a user action to be displayed on the alert.
- `readonly attribute AString title`: Returns a string containing action text to be shown to the user.
- `readonly attribute AString iconURL`: Returns a string containing the URL of an icon to display with the action.
- `readonly attribute nsIURI navigate`: Returns the URI to navigate to if this action is chosen, or null if it
- `readonly attribute boolean windowsSystemActivationType`: On Windows, chrome-privileged notifications -- i.e., those with a
- `readonly attribute AString opaqueRelaunchData`: On Windows, chrome-privileged notifications -- i.e., those with a

# nsIAlertNotification (toolkit/components/alerts/nsIAlertsService.idl)

source: toolkit/components/alerts/nsIAlertsService.idl
source-hash: 0402d78ff5abf5116149f92366a0e3517924bbd4

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/asrouter/modules/ToastNotification.sys.mjs`](../../../browser/components/asrouter/modules/ToastNotification.sys.mjs.md), [`browser/extensions/newtab/lib/WebNotificationsFeed.sys.mjs`](../../../browser/extensions/newtab/lib/WebNotificationsFeed.sys.mjs.md)

## メソッド / 属性
- `void init(AString aName, AString aImageURL, AString aTitle, AString aText, boolean aTextClickable, AString aCookie, AString aDir, AString aLang, AString aData, nsIPrincipal aPrincipal, boolean aInPrivateBrowsing, boolean aRequireInteraction, boolean aSilent, Array<uint32_t> aVibrate)`: Initializes an alert notification.
- `void initWithObject(nsIAlertNotification aAlertNotification)`: Initializes an alert notification with another instance.
- `readonly attribute AString id`: The unique ID of the notification, based on the profile path and the caller
- `readonly attribute AString name`: The name of the notification given by the caller.
- `readonly attribute unsigned long long countId`: An identifier unique across notification instances within the process,
- `readonly attribute AString imageURL`: A URL identifying the image to put in the alert. The OS X backend limits
- `attribute imgIContainer image`: The actual image container to use for the alert. This should be what imageURL returns.
- `readonly attribute AString title`: The title for the alert.
- `readonly attribute AString text`: The contents of the alert.
- `readonly attribute boolean textClickable`: Controls the click behavior. If true, the alert listener will be notified
- `readonly attribute AString cookie`: An opaque cookie that will be passed to the alert listener for each
- `readonly attribute AString dir`: Bidi override for the title and contents. Valid values are "auto", "ltr",
- `readonly attribute AString lang`: Language of the title and text. Ignored if the backend doesn't support
- `readonly attribute AString data`: A Base64-encoded structured clone buffer containing data associated with
- `readonly attribute nsIPrincipal principal`: The principal of the page that created the alert. Used for IPC security
- `readonly attribute nsIURI URI`: The URI of the page that created the alert. |null| if the alert is not
- `readonly attribute boolean inPrivateBrowsing`: Controls the image loading behavior. If true, the image request will be
- `readonly attribute boolean requireInteraction`: Indicates that the notification should remain readily available until
- `readonly attribute boolean silent`: When set, indicates that no sounds or vibrations should be made.
- `readonly attribute Array<uint32_t> vibrate`: A vibration pattern to run with the display of the notification. A
- `attribute Array<nsIAlertAction> actions`: Actions available for users to choose from for interacting with
- `readonly attribute boolean actionable`: Indicates whether this alert should show the source string and action
- `readonly attribute AString source`: The host and port of the originating page, or an empty string if the alert
- `readonly attribute ACString origin`: The origin of the originating page, or an empty string if the alert is not
- `attribute AString opaqueRelaunchData`: On Windows, chrome-privileged notifications -- i.e., those with a
- `nsIAlertAction getAction(AString aName)`: Retrieves the action object by the action name or null if not.

# nsIAlertCallbacks (toolkit/components/alerts/nsIAlertsService.idl)

source: toolkit/components/alerts/nsIAlertsService.idl
source-hash: 0402d78ff5abf5116149f92366a0e3517924bbd4

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void onAlertShow()`: (未記入)
- `void onAlertClick(nsIAlertAction aAction)`: (未記入)
- `void onAlertDismissedFromForeground()`: (未記入)
- `void onAlertClosed()`: (未記入)
- `void onAlertFinished()`: (未記入)
- `void onAlertSettings()`: (未記入)
- `void onAlertDisable()`: (未記入)

# nsIAlertsService (toolkit/components/alerts/nsIAlertsService.idl)

source: toolkit/components/alerts/nsIAlertsService.idl
source-hash: 0402d78ff5abf5116149f92366a0e3517924bbd4

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/AccountsGlue.sys.mjs`](../../../browser/components/AccountsGlue.sys.mjs.md), [`browser/components/BrowserContentHandler.sys.mjs`](../../../browser/components/BrowserContentHandler.sys.mjs.md), [`browser/components/aiwindow/models/agents/MonitorAgent.sys.mjs`](../../../browser/components/aiwindow/models/agents/MonitorAgent.sys.mjs.md), [`browser/components/asrouter/modules/ToastNotification.sys.mjs`](../../../browser/components/asrouter/modules/ToastNotification.sys.mjs.md), [`browser/components/preferences/config/permissions-data.mjs`](../../../browser/components/preferences/config/permissions-data.mjs.md), [`browser/components/screenshots/ScreenshotsUtils.sys.mjs`](../../../browser/components/screenshots/ScreenshotsUtils.sys.mjs.md), [`browser/extensions/newtab/lib/WebNotificationsFeed.sys.mjs`](../../../browser/extensions/newtab/lib/WebNotificationsFeed.sys.mjs.md), [`browser/extensions/newtab/lib/Widgets/TimerFeed.sys.mjs`](../../../browser/extensions/newtab/lib/Widgets/TimerFeed.sys.mjs.md), [`browser/modules/BackgroundTask_uninstall.sys.mjs`](../../../browser/modules/BackgroundTask_uninstall.sys.mjs.md), [`browser/modules/webrtcUI.sys.mjs`](../../../browser/modules/webrtcUI.sys.mjs.md)

## メソッド / 属性
- `void showAlert(nsIAlertNotification aAlert, nsIObserver aAlertListener)`: Initializes and shows an |nsIAlertNotification| with the given parameters.
- `void showAlertWithCallbacks(nsIAlertNotification aAlert, nsIAlertCallbacks aAlertCallbacks)`: (未記入)
- `void closeAlert(AString aName, boolean aContextClosed)`: Close alerts created by the service.
- `Array<AString> getHistory()`: Returns identifiers of notifications that exist in OS notification center.
- `void teardown()`: Clean up all resources used to listen to alerts.
- `void pbmTeardown()`: Close all alerts opened for Private Browsing Mode.
- `boolean isFullscreen()`: Returns whether full-screen mode is enabled.

# nsIAlertsDoNotDisturb (toolkit/components/alerts/nsIAlertsService.idl)

source: toolkit/components/alerts/nsIAlertsService.idl
source-hash: 0402d78ff5abf5116149f92366a0e3517924bbd4

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/preferences/config/permissions-data.mjs`](../../../browser/components/preferences/config/permissions-data.mjs.md), [`browser/modules/webrtcUI.sys.mjs`](../../../browser/modules/webrtcUI.sys.mjs.md)

## メソッド / 属性
- `attribute boolean manualDoNotDisturb`: Toggles a manual Do Not Disturb mode for the service to reduce the amount
- `attribute boolean suppressForScreenSharing`: Toggles a mode for the service to suppress all notifications from
