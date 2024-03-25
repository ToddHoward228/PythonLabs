def f2(n):
    if(n == 1):
        return 1;
    else: 
        return (2 * n - 1) * f2(n - 1)
