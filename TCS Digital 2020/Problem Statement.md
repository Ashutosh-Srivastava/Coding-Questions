# Sexy Primes

In mathematics, Sexy Primes are prime numbers that differ from each other by six. 
For example, the numbers 5 and 11 are both sexy primes, because they differ by 6. 
If p + 2 or p + 4 (where p is the lower prime) is also prime.

They can be grouped as:
- Sexy prime pairs : It is of the form (p, p + 6), where p and p + 6 are prime numbers.
  Eg. (11, 17) is a sexy prime pairs.

- Sexy prime triplets : Triplets of primes (p, p + 6, p + 12) such that p + 18 is 
                        composite are called sexy prime triplets.
  Eg. (7, 13, 19) is a Sexy prime triplets.

- Sexy prime quadruplets : Sexy prime quadruplets (p, p + 6, p + 12, p + 18) can only 
                           begin with primes ending in a 1 in their decimal representation 
                           (except for the quadruplet with p = 5).
  Eg. (41, 47, 53, 59) is a Sexy prime quadruplets.

- Sexy prime quintuplets : In an arithmetic progression of five terms with common difference 
                           6, one of the terms must be divisible by 5, because the two numbers 
                           are relatively prime. Thus, the only sexy prime quintuplet is 
                           (5, 11, 17, 23, 29); no longer sequence of sexy primes is possible.

Given a range of the form [L, R].The task is to print all the sexy prime pairs in the range.

Examples:

### Input : 
  L = 6, R = 59
### Output : 
  (7, 13) (11, 17) (13, 19) (17, 23) (23, 29) (31, 37) (37, 43) (41, 47) (47, 53) (53, 59) 

### Input : 
  L = 1, R = 19
### Output : 
  (5, 11) (7, 13) (11, 17) (13, 19)
