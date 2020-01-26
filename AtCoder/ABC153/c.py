def main():
    N,K = (int(x) for x in input().split())
    h = list(map(int, input().strip().split()))
    H = sorted(h, reverse=True)
    del H[:K]
    print(sum(H))


if __name__ == '__main__':
    main()