from threading import Semaphore


class FizzBuzz:
    def __init__(self, n: int):
        self.done = False
        self.n = n
        self.number_sem = Semaphore(1)
        self.fizz_sem = Semaphore(0)
        self.buzz_sem = Semaphore(0)
        self.fizzbuzz_sem = Semaphore(0)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.fizz_sem.acquire()
            if self.done:
                break
            printFizz()
            self.number_sem.release()

    # printBuzz() outputs "buzz"

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.buzz_sem.acquire()
            if self.done:
                break
            printBuzz()
            self.number_sem.release()

    # printFizzBuzz() outputs "fizzbuzz"

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fizzbuzz_sem.acquire()
            if self.done:
                break
            printFizzBuzz()
            self.number_sem.release()

    # printNumber(x) outputs "x", where x is an integer.

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.number_sem.acquire()
            if i % 15 == 0:
                self.fizzbuzz_sem.release()
            elif i % 5 == 0:
                self.buzz_sem.release()
            elif i % 3 == 0:
                self.fizz_sem.release()
            else:
                printNumber(i)
                self.number_sem.release()
        self.number_sem.acquire()
        self.done = True
        self.fizz_sem.release()
        self.buzz_sem.release()
        self.fizzbuzz_sem.release()
