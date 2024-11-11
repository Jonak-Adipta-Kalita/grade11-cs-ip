# This script generates random lists
import random

l = []
def main():
    for i in range(5):
        l.append(random.randint(1, 100))

    print(l)

if __name__ == "__main__":
    main()
# end main