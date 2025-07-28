"""
Multiprocessing in Python is different than Multithreading, and the difference in capabilities is VERY important
to understand.  The Python interpreter can execute multiple threads concurrently BUT, it can only service ONE
thread at any given time within the Python process.  Conversely, the Python interpreter can use Multiprocessing
to spawn many PARALLEL processes, which can execute SIMULTANEOUSLY.

So, Multiprocessing == "parallelism" and Multithreading = "concurrency".  In general, use Multiprocessing when you
have computationally heavy things to do (or which can be executed independently, in parallel), and use Multithreading
when you have IO heavy things to do (like waiting on external system for many requests) in order to handle latency.

The easiest way to begin using Multiprocessing is to import the ProcessPoolExecutor class from the concurrent.futures 
package.  Using the example below that makes use of the "with" function in Python (which handles cleanup very well), 
create a For loop that loops pool executor "maps", like this:

with ProcessPoolExecutor() as executor:
    for x in executor.map(<function_name_with_no_parenthesis>, <iterable_object_to_feed_to_func>, <extra_iterable_if_needed>):
        <"x"_contains_any_returned_results_from_function>

If you need to add an extra object or variable that is passed to the function, you can include it as the 3rd (or 4th, etc)
argument to the "executor.map()" method.  If the extra object/variable is NOT an iterable (i.e. string, integer, etc) or 
you need to pass it to the function each time, use the built-in "itertools.repeat()" method to build an iterator that 
simply always returns the object/variable.
"""
import itertools
import time
import json
from concurrent.futures import ProcessPoolExecutor, CancelledError, TimeoutError, BrokenExecutor, InvalidStateError
from concurrent.futures.process import BrokenProcessPool

def parallel_process(var1, var2):
    results = []
    for i in var2:
      print(f"Timestamp: {time.time()} - {var1} - {i} to the 10th power is: {i ** 10}")
      results.append(f"Timestamp: {time.time()} - {var1} - {i} to the 10th power is: {i ** 10}")
    return results


if __name__ == "__main__":
    print(f"Start time: {time.time()}")
    iterable_variable_1 = [
        "Process pool 1",
        "Process pool 2",
        "Process pool 3",
        "Process pool 4"
    ]
    iterable_variable_2 = [
        15,
        25,
        35,
        45
    ]
    with ProcessPoolExecutor() as executor:
        print(f"Multiprocessing start time: {time.time()}")
        results = []
        try:
            for variable in executor.map(parallel_process, iterable_variable_1, itertools.repeat(iterable_variable_2)):
                print(f"Multiprocessing loop exit time: {time.time()}")
                results.append(variable)
        except in (CancelledError, TimeoutError, BrokenExecutor, InvalidStateError, BrokenProcessPool) as e:
            print(f"Error encountered with process: {e}")
    print(json.dumps(results, indent=4))
    print(f"End time: {time.time()}")
