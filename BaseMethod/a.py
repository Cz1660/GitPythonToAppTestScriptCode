
a = 10
b = 2000
c='x'


try:
    print(c)
    try:
        assert not a == 100
        print(22222222222222)
    except Exception as e:
        print(b)
except Exception as e:
    print(a)


# a = "2222ddd"
# b = "sssss"
# print("%s_%s" % a,b)