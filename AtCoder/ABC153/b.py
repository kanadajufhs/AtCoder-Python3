def main():
    H,N = (int(x) for x in input().split())
    a = list(map(int, input().strip().split()))
    if H - sum(a) > 0:
        print('No')
    else:
        print('Yes') 

if __name__ == '__main__':
    main()