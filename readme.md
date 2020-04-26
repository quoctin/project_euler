### 1. Multiples of 3 and 5

---

>If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

>Find the sum of all the multiples of 3 or 5 below 1000.

---

Sum of multiple of `x` from `x` to `nx`:

`x + 2x + 3x + ... + nx = x(1+2+3+...+n) = xn(n+1)/2`

Sum of multiples of 3 from 3 to 999

- `x = 3, nx = 999 => n = 333 => 3*333*334/2 = 166833`

Sum of multiple of 5 from 5 to 995: 

- `x = 5, nx = 995 => n = 199 => 5*199*200/2 = 99500`

Sum of multiples of 3 and 5:

- `x = 3*5, nx = 990 => n = 66 => 3*5*66*67/2 = 33165`

---

>Answer: 233168

---

### 2. Even Fibonacci numbers

---

>Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

>`1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

>By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

---

I couldn't find a solution without coding. So, my accepted solution is [sum\_even\_fibo](src/sum_even_fibo.py).

---

>Answer: 4613732

---

### 3. Largest prime factor

---

> The prime factors of 13195 are 5, 7, 13 and 29.

> What is the largest prime factor of the number 600851475143?

---

I use trial division, i.e. simply divide the input number by prime factors. Checking prime divisor is unnecessary because the smallest divisor is `2` and all multiples of `2` are then masked out. The next remaining divisor `3` is for sure a prime and so on. My less-than-1s solution is [largest\_prime\_factor](src/largest_prime_factor.py).

---

>Answer: 6857

---

### 4. Largest palindrome product

---

>A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

>Find the largest palindrome made from the product of two 3-digit numbers.

---

Denote two 3-digit numbers as: `x3x2x1` and `y3y2y1`. Their product P is 

`P = (100x3 + 10x2 + x1)(100y3 + 10y2 + y1)`

`= 10000x3y3 + 1000x3y2 + 100x3y1 + 1000x2y3 + 100x2y2 + 10x2y1 + 100x1y3 + 10x1y2 + x1y1`

We want to maximize this product, so probably we want this number to have 6 digits and to start with 9. The only option is starting with 8 and the remainder will add up. It means `x3y3 = 81 or x3 = y3 = 9`.

`10000x3y3 = 810000`

To have 1 remainder, the digit add to 1 must be 9 and the addition results in 0.

Now `P = 90****`

The summation `1000x3y2 + 100x3y1 + 1000x2y3 + 100x2y2 + 10x2y1 + 100x1y3 + 10x1y2 + x1y1` is a 5-digit number starting with 9 only if `1000(x3y2 + x2y3)` has 5 digits and `x3y2 + x2y3 >= 90 or y2 + x2 >= 10`.

To make this product palindromic, `x1y1` must end in 9. We have three options: `x1 = y1 = 3`, or `x1 = y1 = 7` or `x1 = 9, y1 = 1`. If `x1 = y1 = 7`, we have no option for the 2nd digit to be zero which is equal to the 5th digit. There are two options for the 2nd digit to be zero


+ `3x2 + 3y2 = *0`

+ and `9x2 + y2 = *0`

The solution for `3x2 + 3y2 = *0` is that `x2 = 1, y2 = 9`, while `x2 = y2 >= 5` is the solution of `9x2 + y2 = *0`. 

We carry out maximum six trials and then find that `x2 = 1, y2 = 9` is the only solution that makes P palindrome.

---

>Answer: 906609

---

### 5. Smallest multiple

---

>2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

>What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

---

Least Common Multiple(lcm)
Greatest Common Divisor(gcd)

`lcm(a, b) = |a*b| / gcd(a, b)`

`lcm(a, b, c) = lcm(lcm(a, b), c)`

and so on.

---

>Answer: 232792560

---

### 6. Sum square difference

---
>The sum of the squares of the first ten natural numbers is,

>`1^2 + 2^2 +...+ 10^2 = 385`

>The square of the sum of the first ten natural numbers is,

>`(1 + 2 +...+ 10)^2 = 552 = 3025`

>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is `3025 − 385 = 2640`

>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

---

Square of sum `(1 + 2 + ... + N)^2 = N^2(N + 1)^2 / 4`

Sum of square `(1^2 + 2^2 + ... + N^2) = N(N+1)(2N+1) / 6`

--- 

>Answer: 25164150

---

## 7. 10001st prime

---

>By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

>What is the 10001st prime number?

---

My less-than-1s solution is [nth\_prime](src/nth_prime.py).

--- 

>Answer: 104743

---

## 8. Largest product in a series

---

>The four adjacent digits in the 1000-digit number that have the greatest product are `9 × 9 × 8 × 9 = 5832`.


>
```73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
```


>Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

---


In my [solution](src/largest_adjacent_product.py), I scan over 13-digit numbers and omit ones containing `'0'` because any number times `0` becomes `0`.


--- 

>Answer: 23514624000

---

## 9. Largest product in a series

---

>A Pythagorean triplet is a set of three natural numbers, `a < b < c`, for which,

>`a^2 + b^2 = c^2`

>For example, `32 + 42 = 9 + 16 = 25 = 52`.

>There exists exactly one Pythagorean triplet for which `a + b + c = 1000`.
Find the product `abc`.

---

I derived `a` and `b` in terms of `c`. My [solution](assets/pdf/p9.pdf) is searching `c` in `[1, 999]` to find unique solution for `a` and `b`.

## 10. Summation of primes

---

>The sum of the primes below 10 is `2 + 3 + 5 + 7 = 17`.

>Find the sum of all the primes below two million.

---

[Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) is used in [my implementation](src/sum_primes.py). It tooks around 2s.

---

>Answer: 142913828922

---

## 11. Largest product in a grid

---

>In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

>![](/assets/png/11.png)

>The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

>What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

---

My [solution](src/largest_product_grid.py) is framing a sub matrix 4x4 at each element and check right, down, diagonal, inverse of diagonal.


## 12. Highly divisible triangular number

---

>The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be `1 + 2 + 3 + 4 + 5 + 6 + 7 = 28`. The first ten terms would be:

>`1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...`

>Let us list the factors of the first seven triangle numbers:

```
 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
```

>We can see that 28 is the first triangle number to have over five divisors.

>What is the value of the first triangle number to have over five hundred divisors?

---
Any positive integer has a unique prime factorization as p1^e1 * p2^e2 * ... * pn^en, where pi is a prime number. The number of divisors would be (e1+1) * (e2+1) * ... * (en+1).

The N-th triangular number have the form of N*(N+1)/2 = N(N+1)*2^-1. Therefore, to compute prime factorization of (N)-th triangular number, we need to compute prime factorization of N and N+1. To compute prime factorization of (N+1)-th triangular number, we can reuse solution of N+1 and only need to solve for N+2, so on and so forth.

My [solution](src/highly_divisible_triangular.py) is less than 1s.


