# To find all pairs of Additive inverse and Multiplicative inverse in Zn

def main():
  add_pairs = []
  multi_pairs = []
  n = int(input("Enter the value of n: "))
  for a in range(0, n):
    for b in range(0, n):
      if (a + b) % n == 0:
        if [b, a] not in add_pairs:
          add_pairs.append([a, b])
      if (a * b) % n == 1:
        if [b, a] not in multi_pairs:
          multi_pairs.append([a, b])
  print("Additive Inverse Pairs: ", add_pairs)
  print("Multiplicative Inverse Pairs: ", multi_pairs)

if __name__ == "__main__":
  main()

