# nsIFocusManager (dom/interfaces/base/nsIFocusManager.idl)

source: dom/interfaces/base/nsIFocusManager.idl
source-hash: 33b7f04f48cae484351fd32ee0c42b4293e84bdd

- 継承: nsISupports
- 役割: The focus manager deals with all focus related behaviour. Only one element
- 実装: (未記入)
- 使っているJS: [`browser/components/tabbrowser/content/browser-ctrlTab.js`](../../../browser/components/tabbrowser/content/browser-ctrlTab.js.md)

## メソッド / 属性
- `readonly attribute mozIDOMWindowProxy activeWindow`: The most active (frontmost) window, or null if no window that is part of
- `readonly attribute BrowsingContext activeBrowsingContext`: In the parent process: The BrowsingContext corresponding to activeWindow.
- `readonly attribute BrowsingContext activeContentBrowsingContext`: Parent-process only: The chrome process notion of content's active
- `attribute mozIDOMWindowProxy focusedWindow`: The child window within the activeWindow that is focused. This will
- `readonly attribute BrowsingContext focusedContentBrowsingContext`: Parent-process only: The content BrowsingContext that currently has focus,
- `readonly attribute Element focusedElement`: The element that is currently focused. This will always be an element
- `uint32_t getLastFocusMethod(mozIDOMWindowProxy window)`: Returns the method that was used to focus the element in window. This
- `void setFocus(Element aElement, unsigned long aFlags)`: Changes the focused element reference within the window containing
- `Element moveFocus(mozIDOMWindowProxy aWindow, Element aStartElement, unsigned long aType, unsigned long aFlags)`: Move the focus to another element. If aStartElement is specified, then
- `void clearFocus(mozIDOMWindowProxy aWindow)`: Clears the focused element within aWindow. If the current focusedWindow
- `Element getFocusedElementForWindow(mozIDOMWindowProxy aWindow, boolean aDeep, mozIDOMWindowProxy aFocusedWindow)`: Returns the currently focused element within aWindow. If aWindow is equal
- `void moveCaretToFocus(mozIDOMWindowProxy aWindow)`: Moves the selection caret within aWindow to the current focus.
- `boolean elementIsFocusable(Element aElement, unsigned long aFlags)`: Check if given element (or potentially a descendant, see setFocus) is
- `const unsigned long FLAG_RAISE`: (未記入)
- `const unsigned long FLAG_NOSCROLL`: Do not scroll the element to focus into view.
- `const unsigned long FLAG_NOSWITCHFRAME`: If attempting to change focus in a window that is not focused, do not
- `const unsigned long FLAG_NOPARENTFRAME`: This flag is only used when passed to moveFocus. If set, focus is never
- `const unsigned long FLAG_NONSYSTEMCALLER`: This flag is used for window and element focus operations to signal
- `const unsigned long FLAG_BYMOUSE`: Focus is changing due to a mouse operation, for instance the mouse was
- `const unsigned long FLAG_BYKEY`: Focus is changing due to a key operation, for instance pressing the tab
- `const unsigned long FLAG_BYMOVEFOCUS`: Focus is changing due to a call to MoveFocus. This flag will be implied
- `const unsigned long FLAG_NOSHOWRING`: Do not show a ring around the element to focus, if this is not a text
- `const unsigned long FLAG_SHOWRING`: Always show the focus ring or other indicator of focus, regardless of
- `const unsigned long FLAG_BYTOUCH`: Focus is changing due to a touch operation that generated a mouse event.
- `const unsigned long FLAG_BYJS`: Focus is changing due to a JS focus() call or similar operation.
- `const unsigned long FLAG_BYLONGPRESS`: Focus is changing due to a long press operation by touch or mouse.
- `const unsigned long METHOD_MASK`: Mask with all the focus methods.
- `const unsigned long METHODANDRING_MASK`: Mask with all the focus methods, plus the SHOW / NOSHOWRING flags.
- `const unsigned long MOVEFOCUS_FORWARD`: move focus forward one element, used when pressing TAB
- `const unsigned long MOVEFOCUS_BACKWARD`: move focus backward one element, used when pressing Shift+TAB
- `const unsigned long MOVEFOCUS_FORWARDDOC`: move focus forward to the next frame document, used when pressing F6
- `const unsigned long MOVEFOCUS_BACKWARDDOC`: move focus forward to the previous frame document, used when pressing Shift+F6
- `const unsigned long MOVEFOCUS_FIRST`: move focus to the first focusable element
- `const unsigned long MOVEFOCUS_LAST`: move focus to the last focusable element
- `const unsigned long MOVEFOCUS_ROOT`: move focus to the root element in the document
- `const unsigned long MOVEFOCUS_CARET`: move focus to a link at the position of the caret. This is a special value used to
- `const unsigned long MOVEFOCUS_FIRSTDOC`: move focus to the first focusable document
- `const unsigned long MOVEFOCUS_LASTDOC`: move focus to the last focusable document
