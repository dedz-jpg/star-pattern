
---

### Código Python (patterns.py)

```python
def star_pattern(N):
    i = 1
    while i <= N:
        stars = 1
        while stars <= i:
            print("*", end="")
            stars += 1
        print()  # pula para próxima linha
        i += 1

def number_pattern(N):
    i = 1
    while i <= N:
        j = 1
        while j <= i:
            print(j, end="")
            j += 1
        print()  # pula para próxima linha
        i += 1

def main():
    N = int(input("Digite o valor de N: "))
    print("\nStar Pattern:")
    star_pattern(N)
    print("\nNumber Pattern:")
    number_pattern(N)

if __name__ == "__main__":
    main()
