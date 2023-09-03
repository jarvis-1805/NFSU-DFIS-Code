alpha_space = "abcdefghijklmnopqrstuvwxyz"

def encrypt():
  cipher_text = ""
  plain_char = ""
  file_path = input("Enter the file name/path: ")
  key = int(input("Enter the key: "))
  with open(file_path) as file:
    for plain_char in file.read():
      plain_char = plain_char.lower()
      if plain_char in alpha_space:

        for i in range(0, len(alpha_space)):
          if plain_char == alpha_space[i]:
            index = i
            break

        cipher_char = alpha_space[(index + key) % 26]
      else:
        cipher_char = plain_char
      cipher_text += cipher_char
  
  print("Cipher Text: ", cipher_text)


def decrypt():
  plain_text = ""
  cipher_char = ""
  file_path = input("Enter the file name/path: ")
  key = int(input("Enter the key: "))
  with open(file_path) as file:
    for cipher_char in file.read():
      cipher_char = cipher_char.lower()
      if cipher_char in alpha_space:

        for i in range(0, len(alpha_space)):
          if cipher_char == alpha_space[i]:
            index = i
            break

        plain_char = alpha_space[(index - key) % 26]
      else:
        plain_char = cipher_char
      plain_text += plain_char
  
  print("Plain Text: ", plain_text)

def main():
  while True:
    print("========== MENU ==========")
    print("1. Encryption")
    print("2. Decryption")
    print("0. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 0:
      break

    if choice == 1:
      encrypt()
    elif choice == 2:
      decrypt()
    else:
      print("Wrong choice! Try Again!!!")

if __name__ == "__main__":
  main()

