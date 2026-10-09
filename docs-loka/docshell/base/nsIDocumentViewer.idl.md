# nsIDocumentViewer (docshell/base/nsIDocumentViewer.idl)

source: docshell/base/nsIDocumentViewer.idl
source-hash: 3ac704645a41ae02459f7e5e9eb67c3069a14998

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void init(nsIWidgetPtr aParentWidget, LayoutDeviceIntRectRef aBounds, WindowGlobalChildPtr aWindowActor)`: (未記入)
- `attribute nsIDocShell container`: (未記入)
- `void loadStart(Document aDoc)`: (未記入)
- `void loadComplete(nsresult aStatus)`: (未記入)
- `readonly attribute boolean loadCompleted`: (未記入)
- `readonly attribute boolean isStopped`: (未記入)
- `boolean permitUnload(nsIDocumentViewer_PermitUnloadAction aAction)`: Overload PermitUnload method for C++ consumers with no aPermitUnloadFlags
- `readonly attribute boolean inPermitUnload`: Exposes whether we're blocked in a call to permitUnload.
- `nsIDocumentViewer_PermitUnloadResult dispatchBeforeUnload()`: Dispatches the "beforeunload" event and returns the result, as documented
- `readonly attribute boolean beforeUnloadFiring`: Exposes whether we're in the process of firing the beforeunload event.
- `void pageHide(boolean isUnload)`: (未記入)
- `void close()`: All users of a content viewer are responsible for calling both
- `void destroy()`: (未記入)
- `void stop()`: (未記入)
- `readonly attribute Document DOMDocument`: Returns the same thing as getDocument(), but for use from script
- `Document getDocument()`: Returns DOMDocument without addrefing.
- `void setDocument(Document aDocument)`: Allows setting the document.
- `void getBounds(LayoutDeviceIntRectRef aBounds)`: (未記入)
- `void setBounds(LayoutDeviceIntRectRef aBounds)`: (未記入)
- `const unsigned long eDelayResize`: The 'aFlags' argument to setBoundsWithFlags is a set of these bits.
- `void setBoundsWithFlags(LayoutDeviceIntRectRef aBounds, unsigned long aFlags)`: (未記入)
- `attribute nsIDocumentViewer previousViewer`: The previous content viewer, which has been |close|d but not
- `void move(long aX, long aY)`: (未記入)
- `void show()`: (未記入)
- `void hide()`: (未記入)
- `attribute boolean sticky`: (未記入)
- `void open()`: Attach the content viewer to its DOM window and docshell.
- `void clearHistoryEntry()`: Clears the current history entry.  This is used if we need to clear out
- `void setPageModeForTesting(boolean aPageMode, nsIPrintSettings aPrintSettings)`: Change the layout to view the document with page layout (like print preview), but
- `void setPrintSettingsForSubdocument(nsIPrintSettings aPrintSettings, RemotePrintJobChildPtr aRemotePrintJob)`: Sets the print settings for print / print-previewing a subdocument.
- `readonly attribute boolean isTabModalPromptAllowed`: Indicates when we're in a state where content shouldn't be allowed to
- `attribute boolean isHidden`: Returns whether this content viewer is in a hidden state.
- `readonly attribute PresShellPtr presShell`: (未記入)
- `readonly attribute nsPresContextPtr presContext`: (未記入)
- `void setDocumentInternal(Document aDocument, boolean aForceReuseInnerWindow)`: (未記入)
- `nsSubDocumentFramePtr findContainerFrame()`: Find the view to use as the container view for MakeWindow. Returns
- `void setNavigationTiming(nsDOMNavigationTimingPtr aTiming)`: Set collector for navigation timing data (load, unload events).
- `readonly attribute float deviceFullZoomForTest`: The actual full zoom in effect, as modified by the device context.
- `attribute boolean authorStyleDisabled`: Disable entire author style level (including HTML presentation hints),
- `void getContentSize(long maxWidth, long maxHeight, long prefWidth, long width, long height)`: Returns the preferred width and height of the content, constrained to the
- `Encoding getReloadEncodingAndSource(int32_t aSource)`: (未記入)
- `void setReloadEncodingAndSource(Encoding aEncoding, int32_t aSource)`: (未記入)
- `void forgetReloadEncoding()`: (未記入)
