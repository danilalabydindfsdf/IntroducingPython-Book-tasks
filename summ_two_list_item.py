def main():
    nb = int(input())
    list_digits = [int(input()) for _ in range(nb)]
    print([list_digits[i] + list_digits[i + 1] for i in range(len(list_digits) - 1)])


if __name__ == '__main__':
    main()
