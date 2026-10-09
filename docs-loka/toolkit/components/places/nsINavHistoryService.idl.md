# nsINavHistoryResultNode (toolkit/components/places/nsINavHistoryService.idl)

source: toolkit/components/places/nsINavHistoryService.idl
source-hash: c50ab4877647444fa2f0abb1ec74eac12d027566

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/components/places/PlacesUIUtils.sys.mjs`](../../../browser/components/places/PlacesUIUtils.sys.mjs.md), [`browser/components/places/content/bookmarkProperties.js`](../../../browser/components/places/content/bookmarkProperties.js.md), [`browser/components/places/content/browserPlacesViews.js`](../../../browser/components/places/content/browserPlacesViews.js.md), [`browser/components/places/content/controller.js`](../../../browser/components/places/content/controller.js.md), [`browser/components/places/content/editBookmark.js`](../../../browser/components/places/content/editBookmark.js.md), [`browser/components/places/content/treeView.js`](../../../browser/components/places/content/treeView.js.md)

## メソッド / 属性
- `readonly attribute nsINavHistoryContainerResultNode parent`: Indentifies the parent result node in the result set. This is null for
- `readonly attribute nsINavHistoryResult parentResult`: The history-result to which this node belongs.
- `readonly attribute AUTF8String uri`: URI of the resource in question. For visits and URLs, this is the URL of
- `readonly attribute unsigned long type`: (未記入)
- `readonly attribute AUTF8String title`: Title of the web page, or of the node's query (day, host, folder, etc)
- `readonly attribute unsigned long accessCount`: Total number of times the URI has ever been accessed. For hosts, this
- `readonly attribute PRTime time`: This is the time the user accessed the page.
- `readonly attribute AUTF8String icon`: This URI can be used as an image source URI and will give you the favicon
- `readonly attribute long indentLevel`: This is the number of levels between this node and the top of the
- `readonly attribute long bookmarkIndex`: When this item is in a bookmark folder (parent is of type folder), this is
- `readonly attribute long long itemId`: If the node is an item (bookmark, folder or a separator) this value is the
- `readonly attribute PRTime dateAdded`: If the node is an item (bookmark, folder or a separator) this value is the
- `readonly attribute PRTime lastModified`: If the node is an item (bookmark, folder or a separator) this value is the
- `readonly attribute AString tags`: For uri nodes, this is a sorted list of the tags, delimited with commans,
- `readonly attribute ACString pageGuid`: The unique ID associated with the page. It my return an empty string
- `readonly attribute ACString bookmarkGuid`: The unique ID associated with the bookmark. It returns an empty string
- `readonly attribute long long visitId`: The unique ID associated with the history visit. For node types other than
- `readonly attribute unsigned long visitType`: The transition type associated with this visit. For node types other than

# nsINavHistoryContainerResultNode (toolkit/components/places/nsINavHistoryService.idl)

source: toolkit/components/places/nsINavHistoryService.idl
source-hash: c50ab4877647444fa2f0abb1ec74eac12d027566

- 継承: nsINavHistoryResultNode
- 役割: Base class for container results. This includes all types of groupings.
- 実装: (未記入)
- 使っているJS: [`browser/components/places/content/browserPlacesViews.js`](../../../browser/components/places/content/browserPlacesViews.js.md), [`browser/components/places/content/treeView.js`](../../../browser/components/places/content/treeView.js.md)

## メソッド / 属性
- `attribute boolean containerOpen`: Set this to allow descent into the container. When closed, attempting
- `readonly attribute unsigned short state`: Indicates whether the container is closed, loading, or opened.  Loading
- `const unsigned short STATE_CLOSED`: (未記入)
- `const unsigned short STATE_LOADING`: (未記入)
- `const unsigned short STATE_OPENED`: (未記入)
- `readonly attribute boolean hasChildren`: This indicates whether this node "may" have children, and can be used
- `readonly attribute unsigned long childCount`: This gives you the children of the nodes. It is preferrable to use this
- `nsINavHistoryResultNode getChild(unsigned long aIndex)`: (未記入)
- `unsigned long getChildIndex(nsINavHistoryResultNode aNode)`: Get the index of a direct child in this container.

# nsINavHistoryQueryResultNode (toolkit/components/places/nsINavHistoryService.idl)

source: toolkit/components/places/nsINavHistoryService.idl
source-hash: c50ab4877647444fa2f0abb1ec74eac12d027566

- 継承: nsINavHistoryContainerResultNode
- 役割: Used for places queries and as a base for bookmark folders.
- 実装: (未記入)
- 使っているJS: [`browser/components/places/content/treeView.js`](../../../browser/components/places/content/treeView.js.md)

## メソッド / 属性
- `readonly attribute nsINavHistoryQuery query`: Get the query which builds this node's children.
- `readonly attribute nsINavHistoryQueryOptions queryOptions`: Get the options which group this node's children.
- `readonly attribute long long folderItemId`: For both simple folder queries and folder shortcut queries, this is set to
- `readonly attribute ACString targetFolderGuid`: For both simple folder queries and folder shortcut queries, this is set to

# nsINavHistoryResultObserver (toolkit/components/places/nsINavHistoryService.idl)

source: toolkit/components/places/nsINavHistoryService.idl
source-hash: c50ab4877647444fa2f0abb1ec74eac12d027566

- 継承: nsISupports
- 役割: Allows clients to observe what is happening to a result as it updates itself
- 実装: (未記入)
- 使っているJS: [`browser/components/places/content/browserPlacesViews.js`](../../../browser/components/places/content/browserPlacesViews.js.md), [`browser/components/places/content/places-tree.js`](../../../browser/components/places/content/places-tree.js.md)

## メソッド / 属性
- `readonly attribute boolean skipHistoryDetailsNotifications`: Whether the observer is interested into history details changes.
- `void nodeInserted(nsINavHistoryContainerResultNode aParent, nsINavHistoryResultNode aNode, unsigned long aNewIndex)`: Called when 'aItem' is inserted into 'aParent' at index 'aNewIndex'.
- `void nodeRemoved(nsINavHistoryContainerResultNode aParent, nsINavHistoryResultNode aItem, unsigned long aOldIndex)`: Called whan 'aItem' is removed from 'aParent' at 'aOldIndex'. The item
- `void nodeMoved(nsINavHistoryResultNode aNode, nsINavHistoryContainerResultNode aOldParent, unsigned long aOldIndex, nsINavHistoryContainerResultNode aNewParent, unsigned long aNewIndex)`: Called whan 'aItem' is moved from 'aOldParent' at 'aOldIndex' to
- `void nodeTitleChanged(nsINavHistoryResultNode aNode, AUTF8String aNewTitle)`: Called right after aNode's title has changed.
- `void nodeURIChanged(nsINavHistoryResultNode aNode, AUTF8String aOldURI)`: Called right after aNode's uri property has changed.
- `void nodeIconChanged(nsINavHistoryResultNode aNode)`: Called right after aNode's icon property has changed.
- `void nodeHistoryDetailsChanged(nsINavHistoryResultNode aNode, PRTime aOldVisitDate, unsigned long aOldAccessCount)`: Called right after aNode's time property or accessCount property, or both,
- `void nodeTagsChanged(nsINavHistoryResultNode aNode)`: Called when the tags set on the uri represented by aNode have changed.
- `void nodeKeywordChanged(nsINavHistoryResultNode aNode, AUTF8String aNewKeyword)`: Called right after the aNode's keyword property has changed.
- `void nodeDateAddedChanged(nsINavHistoryResultNode aNode, PRTime aNewValue)`: Called right after aNode's dateAdded property has changed.
- `void nodeLastModifiedChanged(nsINavHistoryResultNode aNode, PRTime aNewValue)`: Called right after aNode's dateModified property has changed.
- `void containerStateChanged(nsINavHistoryContainerResultNode aContainerNode, unsigned long aOldState, unsigned long aNewState)`: Called after a container changes state.
- `void invalidateContainer(nsINavHistoryContainerResultNode aContainerNode)`: Called when something significant has happened within the container. The
- `void sortingChanged(unsigned short sortingMode)`: This is called to indicate to the UI that the sort has changed to the
- `void batching(boolean aToggleMode)`: This is called to indicate that a batch operation is about to start or end.
- `attribute nsINavHistoryResult result`: Called by the result when this observer is added.

# nsINavHistoryResult (toolkit/components/places/nsINavHistoryService.idl)

source: toolkit/components/places/nsINavHistoryService.idl
source-hash: c50ab4877647444fa2f0abb1ec74eac12d027566

- 継承: nsISupports
- 役割: The result of a history/bookmark query.
- 実装: (未記入)

## メソッド / 属性
- `attribute unsigned short sortingMode`: Sorts all nodes recursively by the given parameter, one of
- `attribute boolean suppressNotifications`: Whether or not notifications on result changes are suppressed.
- `void addObserver(nsINavHistoryResultObserver aObserver, boolean aOwnsWeak)`: Adds an observer for changes done in the result.
- `void removeObserver(nsINavHistoryResultObserver aObserver)`: Removes an observer that was added by addObserver.
- `readonly attribute nsINavHistoryContainerResultNode root`: This is the root of the results. Remember that you need to open all
- `void onBeginUpdateBatch()`: Notifies you that a bunch of things are about to change, don't do any
- `void onEndUpdateBatch()`: Notifies you that we are done doing a bunch of things and you should go

# nsINavHistoryQuery (toolkit/components/places/nsINavHistoryService.idl)

source: toolkit/components/places/nsINavHistoryService.idl
source-hash: c50ab4877647444fa2f0abb1ec74eac12d027566

- 継承: nsISupports
- 役割: This object encapsulates all the query parameters you're likely to need
- 実装: (未記入)
- 使っているJS: [`browser/components/aiwindow/models/SearchBrowsingHistory.sys.mjs`](../../../browser/components/aiwindow/models/SearchBrowsingHistory.sys.mjs.md)

## メソッド / 属性
- `const unsigned long TIME_RELATIVE_EPOCH`: Time range for results (INCLUSIVE). The *TimeReference is one of the
- `const unsigned long TIME_RELATIVE_TODAY`: (未記入)
- `const unsigned long TIME_RELATIVE_NOW`: (未記入)
- `attribute PRTime beginTime`: (未記入)
- `attribute unsigned long beginTimeReference`: (未記入)
- `readonly attribute boolean hasBeginTime`: (未記入)
- `readonly attribute PRTime absoluteBeginTime`: (未記入)
- `attribute PRTime endTime`: (未記入)
- `attribute unsigned long endTimeReference`: (未記入)
- `readonly attribute boolean hasEndTime`: (未記入)
- `readonly attribute PRTime absoluteEndTime`: (未記入)
- `attribute AString searchTerms`: Text search terms.
- `readonly attribute boolean hasSearchTerms`: (未記入)
- `attribute long minVisits`: Set lower or upper limits for how many times an item has been
- `attribute long maxVisits`: (未記入)
- `void setTransitions(Array<unsigned long> transitions)`: When the set of transitions is nonempty, results are limited to pages which
- `Array<unsigned long> getTransitions()`: Get the transitions set for this query.
- `readonly attribute unsigned long transitionCount`: Get the count of the set query transitions.
- `attribute boolean domainIsHost`: This controls the meaning of 'domain', and whether it is an exact match
- `attribute AUTF8String domain`: This is the host or domain name (controlled by domainIsHost). When
- `readonly attribute boolean hasDomain`: (未記入)
- `attribute nsIURI uri`: This is a URI to match, to, for example, find out every time you visited
- `readonly attribute boolean hasUri`: (未記入)
- `attribute nsIVariant tags`: Limit results to items that are tagged with all of the given tags.  This
- `attribute boolean tagsAreNot`: If 'tagsAreNot' is true, the results are instead limited to items that
- `Array<ACString> getParents()`: Limit results to items that are in all of the given folders.
- `readonly attribute unsigned long parentCount`: (未記入)
- `void setParents(Array<ACString> aGuids)`: This is not recursive so results will be returned from the first level of
- `nsINavHistoryQuery clone()`: Creates a new query item with the same parameters of this one.

# nsINavHistoryQueryOptions (toolkit/components/places/nsINavHistoryService.idl)

source: toolkit/components/places/nsINavHistoryService.idl
source-hash: c50ab4877647444fa2f0abb1ec74eac12d027566

- 継承: nsISupports
- 役割: This object represents the global options for executing a query.
- 実装: (未記入)
- 使っているJS: [`browser/base/content/browser-places.js`](../../../browser/base/content/browser-places.js.md), [`browser/components/aiwindow/models/SearchBrowsingHistory.sys.mjs`](../../../browser/components/aiwindow/models/SearchBrowsingHistory.sys.mjs.md), [`browser/components/customizableui/CustomizableWidgets.sys.mjs`](../../../browser/components/customizableui/CustomizableWidgets.sys.mjs.md), [`browser/components/places/content/bookmarksSidebar.js`](../../../browser/components/places/content/bookmarksSidebar.js.md), [`browser/components/places/content/browserPlacesViews.js`](../../../browser/components/places/content/browserPlacesViews.js.md), [`browser/components/places/content/controller.js`](../../../browser/components/places/content/controller.js.md), [`browser/components/places/content/editBookmark.js`](../../../browser/components/places/content/editBookmark.js.md), [`browser/components/places/content/historySidebar.js`](../../../browser/components/places/content/historySidebar.js.md), [`browser/components/places/content/places-tree.js`](../../../browser/components/places/content/places-tree.js.md), [`browser/components/places/content/places.js`](../../../browser/components/places/content/places.js.md), [`browser/components/places/content/treeView.js`](../../../browser/components/places/content/treeView.js.md), [`browser/components/preferences/dialogs/selectBookmark.js`](../../../browser/components/preferences/dialogs/selectBookmark.js.md), [`browser/components/sidebar/sidebar-bookmarks.mjs`](../../../browser/components/sidebar/sidebar-bookmarks.mjs.md)

## メソッド / 属性
- `attribute unsigned short sortingMode`: The sorting mode to be used for this query.
- `attribute unsigned short resultType`: Sets the result type. One of RESULT_TYPE_* which includes how URIs are
- `attribute boolean excludeItems`: This option excludes all URIs and separators from a bookmarks query.
- `attribute boolean excludeQueries`: Set to true to exclude queries ("place:" URIs) from the query results.
- `attribute boolean expandQueries`: When set, allows items with "place:" URIs to appear as containers,
- `attribute boolean includeHidden`: Some pages in history are marked "hidden" and thus don't appear by default
- `attribute unsigned long maxResults`: This is the maximum number of results that you want. The query is executed,
- `const unsigned short QUERY_TYPE_HISTORY`: (未記入)
- `const unsigned short QUERY_TYPE_BOOKMARKS`: (未記入)
- `attribute unsigned short queryType`: The type of search to use when querying the DB; This attribute is only
- `attribute boolean asyncEnabled`: When this is true, the root container node generated by these options and
- `nsINavHistoryQueryOptions clone()`: Creates a new options item with the same parameters of this one.

# nsINavHistoryService (toolkit/components/places/nsINavHistoryService.idl)

source: toolkit/components/places/nsINavHistoryService.idl
source-hash: c50ab4877647444fa2f0abb1ec74eac12d027566

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)
- 使っているJS: [`browser/base/content/pageinfo/security.js`](../../../browser/base/content/pageinfo/security.js.md), [`browser/components/extensions/parent/ext-history.js`](../../../browser/components/extensions/parent/ext-history.js.md), [`browser/components/places/content/places.js`](../../../browser/components/places/content/places.js.md), [`browser/modules/WindowsJumpLists.sys.mjs`](../../../browser/modules/WindowsJumpLists.sys.mjs.md)

## メソッド / 属性
- `const unsigned long DATABASE_SCHEMA_VERSION`: (未記入)
- `const unsigned short DATABASE_STATUS_OK`: Set when database is coherent
- `const unsigned short DATABASE_STATUS_CREATE`: Set when database did not exist and we created a new one.
- `const unsigned short DATABASE_STATUS_CORRUPT`: Set when database was corrupt and we replaced it with a new one.
- `const unsigned short DATABASE_STATUS_UPGRADED`: Set when database schema has been upgraded.
- `const unsigned short DATABASE_STATUS_LOCKED`: Set when database couldn't be opened.
- `const unsigned short VISIT_SOURCE_ORGANIC`: Insert this value into moz_historyvisits if the visit source is organic.
- `const unsigned short VISIT_SOURCE_SPONSORED`: Insert this value into moz_historyvisits if the visit source is sponsored.
- `const unsigned short VISIT_SOURCE_BOOKMARKED`: Insert this value into moz_historyvisits if the visit source is bookmarked.
- `const unsigned short VISIT_SOURCE_SEARCHED`: Insert this value into moz_historyvisits if the visit source is searched.
- `readonly attribute unsigned short databaseStatus`: Returns the current database status
- `void markPageAsFollowedBookmark(nsIURI aURI)`: This is just like markPageAsTyped (in nsIBrowserHistory, also implemented
- `void markPageAsTyped(nsIURI aURI)`: Designates the url as having been explicitly typed in by the user.
- `void markPageAsFollowedLink(nsIURI aURI)`: Designates the url as coming from a link explicitly followed by
- `boolean canAddURI(nsIURI aURI)`: Returns true if this URI would be added to the history. You don't have to
- `nsINavHistoryQuery getNewQuery()`: This returns a new query object that you can pass to executeQuer[y/ies].
- `nsINavHistoryQueryOptions getNewQueryOptions()`: This returns a new options object that you can pass to executeQuer[y/ies]
- `nsINavHistoryResult executeQuery(nsINavHistoryQuery aQuery, nsINavHistoryQueryOptions options)`: Executes a single query.
- `void queryStringToQuery(AUTF8String aQueryString, nsINavHistoryQuery aQuery, nsINavHistoryQueryOptions options)`: Converts a query URI-like string to a query object.
- `AUTF8String queryToQueryString(nsINavHistoryQuery aQuery, nsINavHistoryQueryOptions options)`: Converts a query into an equivalent string that can be persisted. Inverse
- `readonly attribute boolean historyDisabled`: True if history is disabled. currently,
- `ACString makeGuid()`: Generate a guid.
- `long long pageFrecencyThreshold(long aVisitAgeInDays, long aNumVisits, boolean aBookmarked)`: Calculates a simplified frecency threshold score for filtering
- `unsigned long long hashURL(ACString aSpec, ACString aMode)`: Returns a 48-bit hash for a URI spec.
- `readonly attribute boolean isAlternativeFrecencyEnabled`: Whether alternative frecency is enabled. This is preferred over directly
- `attribute boolean shouldStartFrecencyRecalculation`: This is set to true when a frecency is invalidated and set back to false
- `readonly attribute mozIStorageConnection DBConnection`: The database connection used by Places.
- `mozIStoragePendingStatement asyncExecuteLegacyQuery(nsINavHistoryQuery aQuery, nsINavHistoryQueryOptions aOptions, mozIStorageStatementCallback aCallback)`: Asynchronously executes the statement created from a query.
- `readonly attribute nsIAsyncShutdownClient shutdownClient`: Hook for clients who need to perform actions during/by the end of
- `readonly attribute nsIAsyncShutdownClient connectionShutdownClient`: Hook for internal clients who need to perform actions just before the
