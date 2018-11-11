# The Sieve of Eratosthenes
The sieve of eratoshthenes from around 250 BC is an algorithm for writing down all prime numbers up to a given limit as follows.  
1) List all the whole positive numbers up to the limit  
2) Remove all multiplies of 2 except 2, remove all multiplies of 3 except 3 etc...  
4) What remains is a list of primes up to the chosen limit  

## Using the algo
You can use the algo and run the unittests with Python 3.x. For running the tests from the command line, simply run `python3 utests.py`. You can also import the function (`import primes_soe`) and run the function with a freely chosen limit from there. The function will print all primes up to the limit at the command line.