#!/bin/python3


def get_length(element: str) -> int:
    if isinstance(element, str):
        return len(element)

# driver code
if __name__ == "__main__":
    results = {}
    elems = [
    "female cats are polyestrous",
    'A form of AIDS exists in cats.',
    'Female felines are \\superfecund'
    ]
    for elem in elems:
        length = get_length(element=elem)
        results[f"{elem}"] = length
    print(f"results are as per follows:\n{results}")
