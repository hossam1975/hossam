from timeit import timeit
print("Execution time for 'check_if_contains_truthy()'")
print(
    timeit(
        "check_if_contains_truthy(an_iterable)",
        number=10_000_000,
        globals=globals(),
    )
)
print("Execution time for 'any()'")
print(
    timeit(
        "any(an_iterable)",
        number=10_000_000,
        globals=globals(),
    )
)
