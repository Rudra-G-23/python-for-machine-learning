"""
Why we need a decorators?

- One functions one task.
- It reduce the code reusability.
"""

import time

from rich.pretty import pprint


def cooking_work():
    start_time = time.time()

    pprint("Cooking started ...")
    time.sleep(1)
    pprint("Cooking finished ...")

    end_time = time.time()

    pprint(f"Difference: {end_time - start_time}")


cooking_work()
