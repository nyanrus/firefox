# nsISelectionController (dom/base/nsISelectionController.idl)

source: dom/base/nsISelectionController.idl
source-hash: 903558e2b89789bec56d9053ef5a960f092a701e

- 継承: nsISelectionDisplay
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/preferences/findInPage.js`](../../browser/components/preferences/findInPage.js.md), [`browser/components/urlbar/UrlbarValueFormatter.sys.mjs`](../../browser/components/urlbar/UrlbarValueFormatter.sys.mjs.md)

## メソッド / 属性
- `const short SELECTION_NONE`: (未記入)
- `const short SELECTION_NORMAL`: (未記入)
- `const short SELECTION_SPELLCHECK`: (未記入)
- `const short SELECTION_IME_RAWINPUT`: (未記入)
- `const short SELECTION_IME_SELECTEDRAWTEXT`: (未記入)
- `const short SELECTION_IME_CONVERTEDTEXT`: (未記入)
- `const short SELECTION_IME_SELECTEDCONVERTEDTEXT`: (未記入)
- `const short SELECTION_ACCESSIBILITY`: (未記入)
- `const short SELECTION_FIND`: (未記入)
- `const short SELECTION_URLSECONDARY`: (未記入)
- `const short SELECTION_URLSTRIKEOUT`: (未記入)
- `const short SELECTION_TARGET_TEXT`: (未記入)
- `const short SELECTION_HIGHLIGHT`: (未記入)
- `const short NUM_SELECTIONTYPES`: (未記入)
- `const short SELECTION_ANCHOR_REGION`: (未記入)
- `const short SELECTION_FOCUS_REGION`: (未記入)
- `const short SELECTION_WHOLE_SELECTION`: (未記入)
- `const short NUM_SELECTION_REGIONS`: (未記入)
- `const short SELECTION_OFF`: (未記入)
- `const short SELECTION_HIDDEN`: (未記入)
- `const short SELECTION_ON`: (未記入)
- `const short SELECTION_DISABLED`: (未記入)
- `const short SELECTION_ATTENTION`: (未記入)
- `void setDisplaySelection(short toggle)`: SetDisplaySelection will set the display mode for the selection. OFF,ON,DISABLED
- `short getDisplaySelection()`: GetDisplaySelection will get the display mode for the selection. OFF,ON,DISABLED
- `Selection getSelection(short type)`: GetSelection will return the selection that the presentation
- `Selection getDOMSelection(short aType)`: Return the selection object corresponding to a selection type.
- `void selectionWillTakeFocus()`: Called when the selection controller should take the focus.
- `void selectionWillLoseFocus()`: Called when the selection controller has lost the focus.
- `void scrollSelectionIntoView(short type, short region, nsISelectionController_ControllerScrollFlags flags)`: ScrollSelectionIntoView scrolls a region of the selection,
- `void repaintSelection(short type)`: RepaintSelection repaints the selection specified by aType.
- `void setCaretEnabled(boolean enabled)`: Set the caret as enabled or disabled. An enabled caret will
- `void setCaretReadOnly(boolean readOnly)`: Set the caret readonly or not. An readonly caret will
- `boolean getCaretEnabled()`: Gets the current state of the caret.
- `readonly attribute boolean caretVisible`: This is true if the caret is enabled, visible, and currently blinking.
- `void setCaretVisibilityDuringSelection(boolean visibility)`: Show the caret even in selections. By default the caret is hidden unless the
- `void characterMove(boolean forward, boolean extend)`: CharacterMove will move the selection one character forward/backward in the document.
- `void physicalMove(short direction, short amount, boolean extend)`: PhysicalMove will move the selection one "unit" in a given direction
- `const short MOVE_LEFT`: nsFrameSelection::PhysicalMove depends on the ordering of these values;
- `const short MOVE_RIGHT`: (未記入)
- `const short MOVE_UP`: (未記入)
- `const short MOVE_DOWN`: (未記入)
- `void wordMove(boolean forward, boolean extend)`: WordMove will move the selection one word forward/backward in the document.
- `void lineMove(boolean forward, boolean extend)`: LineMove will move the selection one line forward/backward in the document.
- `void intraLineMove(boolean forward, boolean extend)`: IntraLineMove will move the selection to the front of the line or end of the line
- `void paragraphMove(boolean forward, boolean extend)`: ParagraphMove will move the selection to the beginning or end of the
- `void pageMove(boolean forward, boolean extend)`: PageMove will move the selection one page forward/backward in the document.
- `void completeScroll(boolean forward)`: CompleteScroll will move page view to the top or bottom of the document
- `void completeMove(boolean forward, boolean extend)`: CompleteMove will move page view to the top or bottom of the document
- `void scrollPage(boolean forward)`: ScrollPage will scroll the page without affecting the selection.
- `void scrollLine(boolean forward)`: ScrollLine will scroll line up or down dependent on the boolean
- `void scrollCharacter(boolean right)`: ScrollCharacter will scroll right or left dependent on the boolean
