Python Back-End

To write an asynchronous generator in Python, you can use the async def syntax to define an asynchronous function that contains yield statements. Here's a basic example:


import asyncio

async def async_generator():
    for i in range(5):
        await asyncio.sleep(1)  # Simulate an asynchronous operation
        yield i
In this example, async_generator() is an asynchronous generator that yields values asynchronously. Each time the yield statement is encountered, the execution of the generator function is paused, allowing other code to run until the generator is resumed.

To use async comprehensions with asynchronous generators, you can use the async for syntax. Here's an example:

async def main():
    async for value in async_generator():
        print(value)

asyncio.run(main())
This main() function asynchronously iterates over the values produced by the async_generator() using the async for syntax.

When type-annotating asynchronous generators, you can use the AsyncGenerator type from the typing module. Here's an example:


from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[int, None]:
    for i in range(5):
        yield i
In this example, AsyncGenerator[int, None] specifies that the asynchronous generator yields integers (int) and doesn't return a final result (None). You can adjust the type annotations according to the types of values yielded by your asynchronous generator.



Tasks
0. Async Generator
mandatory
Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.


1. Async Comprehensions
mandatory
Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.

2. Run time for four parallel comprehensions
mandatory
Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.
