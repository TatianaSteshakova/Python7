string = input("Введите строку: ")

if (len(string) < 1000):
    res = ' '.join(string.split())
    print(res)
else:
    print("False")