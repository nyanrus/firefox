# nsITimerCallback (xpcom/threads/nsITimer.idl)

source: xpcom/threads/nsITimer.idl
source-hash: 9bd1691aee363839282d68042a48b9dfbb1fe645

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `void notify(nsITimer timer)`: @param aTimer the timer which has expired

# nsITimer (xpcom/threads/nsITimer.idl)

source: xpcom/threads/nsITimer.idl
source-hash: 9bd1691aee363839282d68042a48b9dfbb1fe645

- 継承: nsISupports
- 役割: nsITimer instances must be initialized by calling one of the "init" methods
- 実装: (未記入)
- 使っているJS: [`browser/components/tabbrowser/AsyncTabSwitcher.sys.mjs`](../../browser/components/tabbrowser/AsyncTabSwitcher.sys.mjs.md)

## メソッド / 属性
- `const short TYPE_ONE_SHOT`: Type of a timer that fires once only.
- `const short TYPE_REPEATING_SLACK`: After firing, a TYPE_REPEATING_SLACK timer is stopped and not restarted
- `const short TYPE_REPEATING_PRECISE`: TYPE_REPEATING_PRECISE is just a synonym for
- `const short TYPE_REPEATING_PRECISE_CAN_SKIP`: A TYPE_REPEATING_PRECISE_CAN_SKIP repeating timer aims to have constant
- `const short TYPE_REPEATING_SLACK_LOW_PRIORITY`: Same as TYPE_REPEATING_SLACK with the exception that idle events
- `const short TYPE_ONE_SHOT_LOW_PRIORITY`: Same as TYPE_ONE_SHOT with the exception that idle events won't
- `void init(nsIObserver aObserver, unsigned long aDelayInMs, unsigned long aType)`: Initialize a timer that will fire after the said delay.
- `void initWithCallback(nsITimerCallback aCallback, unsigned long aDelayInMs, unsigned long aType)`: Initialize a timer to fire after the given millisecond interval.
- `void initHighResolutionWithCallback(nsITimerCallback aCallback, TimeDuration aDelay, unsigned long aType)`: Initialize a timer to fire after the high resolution TimeDuration.
- `void cancel()`: Cancel the timer.  This method works on all types, not just on repeating
- `void initWithNamedFuncCallback(nsTimerCallbackFunc aCallback, voidPtr aClosure, unsigned long aDelay, unsigned long aType, ACString aName)`: Initialize a timer to fire after the given millisecond interval.
- `void initHighResolutionWithNamedFuncCallback(nsTimerCallbackFunc aCallback, voidPtr aClosure, TimeDuration aDelay, unsigned long aType, ACString aName)`: Initialize a timer to fire after the high resolution TimeDuration.
- `attribute unsigned long delay`: The millisecond delay of the timeout.
- `attribute unsigned long type`: The timer type - one of the above TYPE_* constants.
- `readonly attribute voidPtr closure`: The opaque pointer passed to initWithNamedFuncCallback.
- `readonly attribute nsITimerCallback callback`: The nsITimerCallback object passed to initWithCallback.
- `attribute nsIEventTarget target`: The nsIEventTarget where the callback will be dispatched. Note that this
- `readonly attribute ACString name`: (未記入)
- `readonly attribute unsigned long allowedEarlyFiringMicroseconds`: The number of microseconds this nsITimer implementation can possibly
- `size_t sizeOfIncludingThis(MallocSizeOf aMallocSizeOf)`: (未記入)

# nsITimerManager (xpcom/threads/nsITimer.idl)

source: xpcom/threads/nsITimer.idl
source-hash: 9bd1691aee363839282d68042a48b9dfbb1fe645

- 継承: nsISupports
- 役割: (未記入)
- 実装: (未記入)

## メソッド / 属性
- `Array<nsITimer> getTimers()`: Returns a read-only list of nsITimer objects, implementing only the name,
