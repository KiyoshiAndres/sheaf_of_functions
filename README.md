# sheaf_of_functions

k-valued functions form a module with k-scalar multiplication. 
By using this class, you can use the standard +, -, *, symbols on k-valued functions.
Note that if "f" is a k-valued function, "f * 2 = f + f" works, but "2 * f" does not since the __mul__ method extension has only been applied to "f".
