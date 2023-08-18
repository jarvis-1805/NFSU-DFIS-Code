# To perform Modular Arithmetic properties
# (a+b) mod n = [(a mod n) + (b mod n)] mod n
# (a-b) mod n = [(a mod n) - (b mod n)] mod n
# (axb) mod n = [(a mod n) x (b mod n)] mod n
# (a^n) mod b = [(a mod b) ^ n] mod b

def main():
  while True:
    print("\n========== MENU ==========")
    print("1. (a+b) mod n")
    print("2. (a-b) mod n")
    print("3. (axb) mod n")
    print("4. (a^n) mod b")
    print("0. Exit\n")

    choice = int(input("Enter your choice: "))

    if choice == 0:
      break
    
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    n = int(input("Enter the value of n: "))
    
    if choice == 1:
      result = ((a % n) + (b % n)) % n
    elif choice == 2:
      result = ((a % n) - (b % n)) % n
    elif choice == 3:
      result = ((a % n) * (b % n)) % n
    elif choice == 4:
      result = ((a % b) ** n) % b
    else:
      print("Wrong Choice! Try Again!!!")
    print("Result: ", result)

if __name__ == "__main__":
  main()

