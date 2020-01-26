def main():
    H,A = (int(x) for x in input().split())
    a = 1
    while H - A*a >0:
        a += 1
    print(a)

if __name__ == '__main__':
    main()