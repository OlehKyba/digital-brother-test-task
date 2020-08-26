from typing import List


def multiply(result_list: List[int], x: int):
    """Function to multiply x with large number stored in list. Result is stored in result_list."""
    carry = 0
    for i in range(len(result_list)):
        # Calculate res + previous carry
        res = carry + result_list[i] * x
        result_list[i] = res % 10
        carry = res // 10

    while carry != 0:
        result_list.append(carry % 10)
        carry //= 10


def sum_of_factorial_digits(n: int) -> int:
    """
    Algorithm:
        1) Create a list to store factorial digits and initialize it with 1.
        2) One by one multiply numbers from 1 to n to the list.
        3) Sum all the elements in vector and return the sum.
    """
    result_vector = [1]

    for i in range(1, n + 1):
        multiply(result_vector, i)

    return sum(result_vector)


def quick_test():
    print("Sum of the digits in the number 100!: ", sum_of_factorial_digits(100))


if __name__ == "__main__":
    quick_test()
    try:
        n = int(input("Count sum of the digits in the factorial of: "))
        print(sum_of_factorial_digits(n))
    except ValueError:
        print("Incorrect input!")
