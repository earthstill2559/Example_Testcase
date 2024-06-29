
def is_prime_list(num):
        print(num)
        if num < 0:
            num = num * -1
        if num == 1 or num == 0:
            return False
        for n in range(2, num):
            if num % n == 0:
                return False
        return True
