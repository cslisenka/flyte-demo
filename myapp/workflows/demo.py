from flytekit import task, workflow
from typing import Tuple


@task
def multiply_task(a: int, b: int) -> int:
    return a * b


@task
def sum_task(a: int, b: int) -> int:
    return b + a


@workflow
def sum_workflow(a: int, b: int) -> int:
    result = sum_task(a=a, b=b)
    return result


@workflow
def multiply_and_sum_workflow(a: int, b: int) -> Tuple[int, int]:
    sum = sum_workflow(a=a, b=b)
    multiply = multiply_task(a=a, b=b)
    return sum, multiply


if __name__ == "__main__":
    print(f"Running multiply_and_sum_workflow(a=10, b=15) {multiply_and_sum_workflow(a=10, b=15)}")
