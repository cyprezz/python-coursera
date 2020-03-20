def main(a, b):
    assert type(a) == int
    assert a>0
    assert type(b) == int
    assert b>0
    while b != 0:
        r = a % b
        b = a
        a = r
    return a

if __name__ == "__main__":
    print(main(5, -5))