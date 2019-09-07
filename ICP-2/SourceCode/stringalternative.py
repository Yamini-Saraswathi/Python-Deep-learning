str = input("Enter something")


def string_alternative(s):
    p = [str[i] for i in range(len(str)) if i % 2 == 0]
    a = ""
    print(a.join(p))


string_alternative(str)
