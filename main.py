<<<<<<< HEAD
def fibo(n):
    if n<2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

if __name__ == "__main__":
    res = fibo(5)
    print(res)
=======
# make fizzbuzz code
for i in range(1, 101):
    if i % 15 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
print("abcde")
>>>>>>> 9ac4513ec407bbc687f4fe1774c87c448f665b26
