# To find Additive inverse and Multiplicative inverse of x in Zn

def main():
  add_pairs = []
  multi_pairs = []
  x = int(input("Enter the value of x: "))
  n = int(input("Enter the value of n: "))
  for a in range(0, n):
    if (a + x) % n == 0:
      add_pairs.append([a, x])
    if (a * x) % n == 1:
      multi_pairs.append([a, x])
  print("Additive Inverse Pairs: ", add_pairs)
  print("Multiplicative Inverse Pairs: ", multi_pairs)

if __name__ == "__main__":
  main()

