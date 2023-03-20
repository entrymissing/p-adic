# p-adic

Code for dealing with p-adic distances. 

See [p-adic Wiki](https://en.wikipedia.org/wiki/P-adic_number) for an intro to p-adic numbers. I was trying to visualize what a cricle in p-adic space would look like and wasn't able to find a good lib for it.

The code is representing a rational number $x=p^n * \frac{r}{s}$ where $p$ is the p-adic base, $n$ is an integer and $r$ and $s$ are integers that are not deivisible by $p$. The p-adic distance is then defined as $|x|_p = p^{-n}$.
