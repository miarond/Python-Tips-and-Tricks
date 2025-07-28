# Python Multiprocessing

There are two primary built-in methods in Python to create "non-blocking" code - in other words, code which can execute multiple tasks at the same time, rather than performing them one at a time, in serial fashion.  These two methods are called "Multithreading" and "Multiprocessing".  Both can be a little difficult to understand for beginners and advanced coders alike; unfortunately, the best way to learn is by experimenting until you gain an understanding.

## Multithreading vs Multiprocessing

In simple terms, Multithreading provides "concurrency" while Multiprocessing provides "parallelism".  The difference is subtle, but important.  The Python interpreter can spawn multiple concurrent "threads" which can be processed independently of each other...HOWEVER, a single Python process can only service a single **thread** at a given time - though it will spread it's resources somewhat evenly across all threads.  Just not all at the same time.  Multiprocessing is different in that it allows Python to spawn multiple independent "child processes" of the Python interpreter, which can be serviced **in parallel** - one for each available processor core on the executing system.

Each method has its benefits (strengths) and drawbacks (weaknesses).  Multithreading is useful for IO intensive operations, where Python is going to be stuck waiting on Input and Output from an external source.  Multiprocessing is useful for CPU intensive operations that can be processed fully independently, like when separate calculations are taking place or when distinct datasets are being parsed or processed.

Here are some resources to help you understand the differences:

- https://www.geeksforgeeks.org/python/difference-between-multithreading-vs-multiprocessing-in-python/
- https://builtin.com/data-science/multithreading-multiprocessing
- https://docs.python.org/3/library/multiprocessing.html
- https://docs.python.org/3/library/threading.html
