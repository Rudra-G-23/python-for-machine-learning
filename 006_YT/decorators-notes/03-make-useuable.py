"""
Add *args, **kwargs
"""

import time

from rich.pretty import pprint


def time_diff(base_fn):
    def enhanced_fn(*args, **kwargs):
        start_time = time.time()
        result = base_fn(*args, **kwargs)
        end_time = time.time()
        pprint(f"Difference: {end_time - start_time}")
        return result

    return enhanced_fn


@time_diff
def cooking_work(what: str):
    pprint(f"{what} Cooking started ...")
    time.sleep(1)
    pprint("Cooking finished ...")


# cooking_work = time_diff(cooking_work)
# pprint(cooking_work())

pprint(cooking_work(what="Rich"))
