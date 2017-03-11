# Why-Is-LCG-bad
Why is LCG considered unsafe/harmful/bad PRNG?

https://en.wikipedia.org/wiki/Linear_congruential_generator

LCG is also known as C-rand(), because stdlib.h provides PRNG that uses LCG. So LCG was widely using through C code-- or other implementations of other languages.

But, as almost of you know, LCG is not very good PRNG becuase:

1. It is biased
2. It has very short period
3. It is cryptographically dangerous
4. It is highly-uniformed

To see this visibly, we can use [Marsaglia Effect](https://en.wikipedia.org/wiki/George_Marsaglia). Which shows:

"that n-tuples with coordinates obtained from consecutive use of the generator will lie on a small number of equally spaced hyperplanes in n-dimensional space."

Max number of "a small number" is m^(1/n), where m is divisor of LCG algorithm.
So I implemented in python, with n=3(of course :D). and result is here:

![alt tag](https://raw.githubusercontent.com/g34r/Why-Is-LCG-bad/master/crand_danger.gif)

OWAH!

I cannot count exactly but I think there are 11 planes in space.

See also : [BBS](https://github.com/g34r/BBS-prng)
