# Mutex

Inherits: RefCounted < Object

A binary Semaphore for synchronization of multiple Threads.

## Description

A synchronization mutex (mutual exclusion). This is used to synchronize
multiple Threads, and is equivalent to a binary Semaphore. It guarantees that
only one thread can access a critical section at a time.

This is a reentrant mutex, meaning that it can be locked multiple times by one
thread, provided it also unlocks it as many times.

Warning: Mutexes must be used carefully to avoid deadlocks.

Warning: To ensure proper cleanup without crashes or deadlocks, the following
conditions must be met:

  * When a Mutex's reference count reaches zero and it is therefore destroyed, no threads (including the one on which the destruction will happen) must have it locked.

  * When a Thread's reference count reaches zero and it is therefore destroyed, it must not have any mutex locked.

## Tutorials

  * Using multiple threads

  * Thread-safe APIs

## Methods

void | lock()  
---|---  
bool | try_lock()  
void | unlock()  
  
## Method Descriptions

void lock()

Locks this Mutex, blocks until it is unlocked by the current owner.

Note: This function returns without blocking if the thread already has
ownership of the mutex.

bool try_lock()

Tries locking this Mutex, but does not block. Returns `true` on success,
`false` otherwise.

Note: This function returns `true` if the thread already has ownership of the
mutex.

void unlock()

Unlocks this Mutex, leaving it to other threads.

Note: If a thread called lock() or try_lock() multiple times while already
having ownership of the mutex, it must also call unlock() the same number of
times in order to unlock it correctly.

Warning: Calling unlock() more times that lock() on a given thread, thus
ending up trying to unlock a non-locked mutex, is wrong and may causes crashes
or deadlocks.

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.

  *[void]: No return value.

