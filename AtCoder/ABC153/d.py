def main():
    H =int(input())
    bit_list = list(bin(H))
    del bit_list[:2]
    bit_in = [s.replace('0', '1') for s in bit_list]
    mojiretu = ' '
    for x in bit_in:
        mojiretu += x
    print(int(mojiretu, 2))
if __name__ == '__main__':
    main()