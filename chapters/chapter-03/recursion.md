## Recursion

#### Chapter Three - R. Notes

* Some developers believe that using loops is better for performance, but recursion can improve developer productivity. 

* Recursion is divided into two parts: **Base Case** and **Recursive Case**.

* The Base Case represents the end of the recursion; in other words, you have found what you wanted, so the function stops calling itself. 

* The Recursive Case is the opposite: since you haven't found what you wanted, the function calls itself again.

```python
def fat(x):
    if x == 1:
        return 1  # Base case
    else:
        return x * fat(x - 1)  # Recursive case
```