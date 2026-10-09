# nsIPromptService (toolkit/components/windowwatcher/nsIPromptService.idl)

source: toolkit/components/windowwatcher/nsIPromptService.idl
source-hash: 44117a64f6be0f7cd493cae05679f8d2917d37ef

- 継承: nsISupports
- 役割: This is the interface to the embeddable prompt service; the service that
- 実装: (未記入)
- 使っているJS: [`browser/components/aiwindow/ui/modules/MonitorUIUtils.sys.mjs`](../../../browser/components/aiwindow/ui/modules/MonitorUIUtils.sys.mjs.md), [`browser/components/contentanalysis/content/ContentAnalysis.sys.mjs`](../../../browser/components/contentanalysis/content/ContentAnalysis.sys.mjs.md), [`browser/components/customkeys/CustomKeysParent.sys.mjs`](../../../browser/components/customkeys/CustomKeysParent.sys.mjs.md), [`browser/components/ipprotection/IPProtectionAlertManager.sys.mjs`](../../../browser/components/ipprotection/IPProtectionAlertManager.sys.mjs.md), [`browser/components/prompts/PromptCollection.sys.mjs`](../../../browser/components/prompts/PromptCollection.sys.mjs.md)

## メソッド / 属性
- `void alert(mozIDOMWindowProxy aParent, wstring aDialogTitle, wstring aText)`: Puts up an alert dialog with an OK button.
- `void alertBC(BrowsingContext aBrowsingContext, unsigned long modalType, wstring aDialogTitle, wstring aText)`: Like alert, but with a BrowsingContext as parent.
- `Promise asyncAlert(BrowsingContext aBrowsingContext, unsigned long modalType, wstring aDialogTitle, wstring aText)`: Async version of alertBC
- `void alertCheck(mozIDOMWindowProxy aParent, wstring aDialogTitle, wstring aText, wstring aCheckMsg, boolean aCheckState)`: Puts up an alert dialog with an OK button and a labeled checkbox.
- `void alertCheckBC(BrowsingContext aBrowsingContext, unsigned long modalType, wstring aDialogTitle, wstring aText, wstring aCheckMsg, boolean aCheckState)`: Like alertCheck, but with a BrowsingContext as parent.
- `Promise asyncAlertCheck(BrowsingContext aBrowsingContext, unsigned long modalType, wstring aDialogTitle, wstring aText, wstring aCheckMsg, boolean aCheckState)`: Async version of alertCheckBC
- `boolean confirm(mozIDOMWindowProxy aParent, wstring aDialogTitle, wstring aText)`: Puts up a dialog with OK and Cancel buttons.
- `boolean confirmBC(BrowsingContext aBrowsingContext, unsigned long modalType, wstring aDialogTitle, wstring aText)`: Like confirm, but with a BrowsingContext as parent.
- `Promise asyncConfirm(BrowsingContext aBrowsingContext, unsigned long modalType, wstring aDialogTitle, wstring aText)`: Async version of confirmBC
- `boolean confirmCheck(mozIDOMWindowProxy aParent, wstring aDialogTitle, wstring aText, wstring aCheckMsg, boolean aCheckState)`: Puts up a dialog with OK and Cancel buttons and a labeled checkbox.
- `boolean confirmCheckBC(BrowsingContext aBrowsingContext, unsigned long modalType, wstring aDialogTitle, wstring aText, wstring aCheckMsg, boolean aCheckState)`: Like confirmCheck, but with a BrowsingContext as parent.
- `Promise asyncConfirmCheck(BrowsingContext aBrowsingContext, unsigned long modalType, wstring aDialogTitle, wstring aText, wstring aCheckMsg, boolean aCheckState)`: Async version of confirmCheckBC
- `const unsigned long BUTTON_POS_0`: Button Flags
- `const unsigned long BUTTON_POS_1`: (未記入)
- `const unsigned long BUTTON_POS_2`: (未記入)
- `const unsigned long BUTTON_TITLE_OK`: Button Title Flags (used to set the labels of buttons in the prompt)
- `const unsigned long BUTTON_TITLE_CANCEL`: (未記入)
- `const unsigned long BUTTON_TITLE_YES`: (未記入)
- `const unsigned long BUTTON_TITLE_NO`: (未記入)
- `const unsigned long BUTTON_TITLE_SAVE`: (未記入)
- `const unsigned long BUTTON_TITLE_DONT_SAVE`: (未記入)
- `const unsigned long BUTTON_TITLE_REVERT`: (未記入)
- `const unsigned long BUTTON_TITLE_IS_STRING`: (未記入)
- `const unsigned long BUTTON_POS_0_DEFAULT`: Button Default Flags (used to select which button is the default one)
- `const unsigned long BUTTON_POS_1_DEFAULT`: (未記入)
- `const unsigned long BUTTON_POS_2_DEFAULT`: (未記入)
- `const unsigned long BUTTON_DELAY_ENABLE`: Causes the buttons to be initially disabled.  They are enabled after a
- `const unsigned long SHOW_SPINNER`: Causes a spinner to be displayed next to the title in the dialog box.
- `const unsigned long BUTTON_NONE_ENABLE_BIT`: (未記入)
- `const unsigned long BUTTON_NONE`: BUTTON_NONE indicates that the prompt should have no buttons.  The prompt
- `const unsigned long BUTTON_POS_1_IS_SECONDARY`: Allows the extra1 button to be positioned next to the primary button.
- `const unsigned long STD_OK_CANCEL_BUTTONS`: Selects the standard set of OK/Cancel buttons.
- `const unsigned long STD_YES_NO_BUTTONS`: Selects the standard set of Yes/No buttons.
- `const unsigned long MODAL_TYPE_CONTENT`: (未記入)
- `const unsigned long MODAL_TYPE_TAB`: (未記入)
- `const unsigned long MODAL_TYPE_WINDOW`: (未記入)
- `const unsigned long MODAL_TYPE_INTERNAL_WINDOW`: (未記入)
- `int32_t confirmEx(mozIDOMWindowProxy aParent, wstring aDialogTitle, wstring aText, unsigned long aButtonFlags, wstring aButton0Title, wstring aButton1Title, wstring aButton2Title, wstring aCheckMsg, boolean aCheckState)`: Puts up a dialog with up to 3 buttons and an optional, labeled checkbox.
- `int32_t confirmExBC(BrowsingContext aBrowsingContext, unsigned long modalType, wstring aDialogTitle, wstring aText, unsigned long aButtonFlags, wstring aButton0Title, wstring aButton1Title, wstring aButton2Title, wstring aCheckMsg, boolean aCheckState)`: Like confirmEx, but with a BrowsingContext as parent.
- `Promise asyncConfirmEx(BrowsingContext aBrowsingContext, unsigned long modalType, wstring aDialogTitle, wstring aText, unsigned long aButtonFlags, wstring aButton0Title, wstring aButton1Title, wstring aButton2Title, wstring aCheckMsg, boolean aCheckState, jsval aExtraArgs)`: Async version of confirmExBC
- `boolean prompt(mozIDOMWindowProxy aParent, wstring aDialogTitle, wstring aText, wstring aValue, wstring aCheckMsg, boolean aCheckState)`: Puts up a dialog with an edit field and an optional, labeled checkbox.
- `boolean promptBC(BrowsingContext aBrowsingContext, unsigned long modalType, wstring aDialogTitle, wstring aText, wstring aValue, wstring aCheckMsg, boolean aCheckState)`: Like prompt, but with a BrowsingContext as parent.
- `Promise asyncPrompt(BrowsingContext aBrowsingContext, unsigned long modalType, wstring aDialogTitle, wstring aText, wstring aValue, wstring aCheckMsg, boolean aCheckState)`: Async version of promptBC
- `boolean promptUsernameAndPassword(mozIDOMWindowProxy aParent, wstring aDialogTitle, wstring aText, wstring aUsername, wstring aPassword)`: Puts up a dialog with an edit field and a password field.
- `boolean promptUsernameAndPasswordBC(BrowsingContext aBrowsingContext, unsigned long modalType, wstring aDialogTitle, wstring aText, wstring aUsername, wstring aPassword)`: Like promptUsernameAndPassword, but with a BrowsingContext as parent.
- `Promise asyncPromptUsernameAndPassword(BrowsingContext aBrowsingContext, unsigned long modalType, wstring aDialogTitle, wstring aText, wstring aUsername, wstring aPassword)`: Async version of promptUsernameAndPasswordBC
- `boolean promptPassword(mozIDOMWindowProxy aParent, wstring aDialogTitle, wstring aText, wstring aPassword)`: Puts up a dialog with a password field.
- `boolean promptPasswordBC(BrowsingContext aBrowsingContext, unsigned long modalType, wstring aDialogTitle, wstring aText, wstring aPassword)`: Like promptPassword, but with a BrowsingContext as parent.
- `Promise asyncPromptPassword(BrowsingContext aBrowsingContext, unsigned long modalType, wstring aDialogTitle, wstring aText, wstring aPassword)`: Async version of promptPasswordBC
- `boolean select(mozIDOMWindowProxy aParent, wstring aDialogTitle, wstring aText, Array<AString> aSelectList, long aOutSelection)`: Puts up a dialog box which has a list box of strings from which the user
- `boolean selectBC(BrowsingContext aBrowsingContext, unsigned long modalType, wstring aDialogTitle, wstring aText, Array<AString> aSelectList, long aOutSelection)`: Like select, but with a BrowsingContext as parent.
- `Promise asyncSelect(BrowsingContext aBrowsingContext, unsigned long modalType, wstring aDialogTitle, wstring aText, Array<AString> aSelectList)`: Async version of selectBC
- `boolean promptAuth(mozIDOMWindowProxy aParent, nsIChannel aChannel, uint32_t level, nsIAuthInformation authInfo)`: (未記入)
- `boolean promptAuthBC(BrowsingContext aBrowsingContext, unsigned long modalType, nsIChannel aChannel, uint32_t level, nsIAuthInformation authInfo)`: Like promptAuth, but with a BrowsingContext as parent.
- `Promise asyncPromptAuth(BrowsingContext aBrowsingContext, unsigned long modalType, nsIChannel aChannel, uint32_t level, nsIAuthInformation authInfo)`: Async version of promptAuthBC
- `Promise confirmUserPaste(WindowGlobalParent aWindow)`: Displays a contextmenu to get user confirmation for clipboard read. Only
