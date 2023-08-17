import os

def sort_file_contents():
  while True:
    print('')
    print('===== SORT FILE CONTENT MENU =====')
    print('1. Ascending Order')
    print('2. Descending Order')
    print('3. List of Numbers')
    print('4. List of Version Numbers')
    print('0. Exit')
    print('')
    
    ch = int(input('Enter your choice: '))
    print('')
    
    if (ch > 0 and ch < 5):
      file = input('Enter the file path: ')
    
    if (ch == 1):
      print('\n===== Ascending Order Sorting =====')
      os.system(f"sort {file}")
      
    elif (ch == 2):
      print('\n===== Descending Order Sorting =====')
      os.system(f"sort -r {file}")
      
    elif (ch == 3):
      print('\n===== Numbers Sorting =====')
      os.system(f"sort -n {file}")
      
    elif (ch == 4):
      print('\n===== Version Numbers Sorting =====')
      os.system(f"sort --version-sort --field-separator=. {file}")
      
    elif (ch == 0):
        print('Exiting...')
        exit()
      
    else:
      print("INVALID CHOICE\!\!! TRY AGAIN\!\!!")

def main():
  while True:
    print('')
    print('===== SORT MENU =====')
    print('1. Alphabetically')
    print('2. Size')
    print('3. Time Modified')
    print('4. File Extension')
    print('5. Sort File Contents')
    print('0. Exit')
    print('')
    
    choice = int(input('Enter your choice: '))
    print('')
    
    if (choice > 0 and choice < 6):
      path = input('Enter the path of the directory: ')

    if (choice == 1):
      print('\n===== Alphabetical Sorting =====')
      os.system(f"ls -l {path}")
      
    elif (choice == 2):
      print('\n===== Size Sorting =====')
      os.system(f"ls -lS {path}")
      
    elif (choice == 3):
      print('\n===== Time Modified Sorting =====')
      os.system(f"ls -lt {path}")
      
    elif (choice == 4):
      print('\n===== File Extension Sorting =====')
      os.system(f"ls -lX {path}")
      
    elif (choice == 5):
      sort_file_contents()
      
    elif (choice == 0):
      print('Exiting...')
      exit()
      
    else:
      print("\nINVALID CHOICE\!\!! TRY AGAIN\!\!!")

if __name__ == "__main__":
  main()

