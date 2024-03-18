Python Back-end

Asyncio is a Python library used to write concurrent code using the async/await syntax. Here's a brief overview of how to use asyncio:

Async and Await Syntax:

Asyncio uses async and await keywords to define asynchronous functions and handle asynchronous operations.
An asynchronous function is defined using the async def syntax, and asynchronous operations are awaited using the await keyword.
Executing an Async Program with asyncio:

To execute an async program with asyncio, you typically create an event loop using asyncio.get_event_loop() and run the async function with loop.run_until_complete() or loop.run_forever().
Running Concurrent Coroutines:

Asyncio allows you to run multiple coroutines concurrently using asyncio.gather() or asyncio.wait().
asyncio.gather() collects the results of multiple coroutines into a single awaitable object, while asyncio.wait() waits for multiple coroutines to complete and provides their results and exceptions as sets of futures.
Creating Asyncio Tasks:

You can create asyncio tasks using asyncio.create_task(), passing the coroutine function as an argument. This function returns a Task object representing the execution of the coroutine.
Using the Random Module:

The random module in Python can be used within asynchronous functions just like in synchronous code.
You can import the random module and use its functions to generate random numbers or shuffle sequences asynchronously.
Here's a simple example demonstrating the use of asyncio with concurrent coroutines and the random module:

import asyncio
import random

async def print_random_number():
    await asyncio.sleep(1)  # Simulate an asynchronous operation
    return random.randint(1, 100)

async def main():
    tasks = [print_random_number() for _ in range(5)]  # Create a list of coroutines
    results = await asyncio.gather(*tasks)  # Run coroutines concurrently
    print("Random numbers:", results)

if __name__ == "__main__":
    asyncio.run(main())  # Execute the async program
In this example, print_random_number() is an asynchronous function that simulates an asynchronous operation (in this case, a sleep) and returns a random number. The main() function creates a list of coroutine tasks and runs them concurrently using asyncio.gather(). Finally, the asyncio.run() function is used to execute the async program.

Tasks
0. The basics of async
mandatory
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

Use the random module.

1. Let's execute multiple coroutines at the same time with async
mandatory
Import wait_random from the previous python file that you’ve written and write an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency.

2. Measure the runtime
mandatory
From the previous file, import wait_n into 2-measure_runtime.py.

Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float.

Use the time module to measure an approximate elapsed time.

3. Tasks
mandatory
Import wait_random from 0-basic_async_syntax.

Write a function (do not create an async function, use the regular function syntax to do this) task_wait_random that takes an integer max_delay and returns a asyncio.Task.

4. Tasks
mandatory
Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called.

