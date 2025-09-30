def main():
    num = input("Type a number: ").strip()
    x = []

    print(f"original number {num}")
    for i in num:
        x.append(i)
    
    x.reverse()
    new = "".join(x)

    if num == new:
        return "Yes. Given number is a palindrome number"
    else:
        return "No. Given number is not a palindrome number"

print(main())