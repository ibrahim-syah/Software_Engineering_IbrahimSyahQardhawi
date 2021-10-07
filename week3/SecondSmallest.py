def main():
    nOfNumber = 5
    nums = set()
    for _ in range(nOfNumber):
        nums.add(input("Input number:"))
    nums = sorted(nums)
    print(nums)
    print("Second smallest is {}".format(list(nums)[1]))

if __name__=="__main__":
    main()
