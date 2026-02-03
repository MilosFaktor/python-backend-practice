# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "rich>=14.3.2",
# ]
# ///

# generator experiment
import time

from rich.console import Console

N = 10

console = Console()


def gen():
    for x in range(N):
        with console.status("Processing..."):
            time.sleep(1)
        print("Proccessed:", x)
        yield x


for x in gen():
    with console.status("Consuming..."):
        time.sleep(1)
    print("Consumed:", x)
