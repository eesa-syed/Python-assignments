x=lambda n: str(n)+'tsnrhtdd'[n%5*(n%100^15>4>n%10)::4]
print(x(22))