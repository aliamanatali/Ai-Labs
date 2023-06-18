from book import Book
import sys
f = open("books.txt", "r")

list=f.readlines()
ibanNos = []
names = []
authors = []
issue = []
for items in list:
   x = items.strip().split(",")
   iban = x[0]
   name = x[1]
   author = x[2]
   issued = x[3]
   ibanNos.append(iban)
   names.append(name)
   authors.append(author)
   issue.append(issued)

print(ibanNos)
print(names)
print(authors)
print(issue)
book_objects = []
for i in range(0,4):
   book_obj = Book(ibanNos[i], names[i], authors[i], issue[i])
   book_objects.append(book_obj)


def add_book(book_objects):
  ib = input("Enter Iban Number : ")
  nme = input("Enter Book Name : ")
  auth = input("Enter Author's Name :")
  obj=Book(ib,nme,auth,"0")
  book_objects.append(obj)
  
def search_book(book_objects):
  nam = input("Enter the Name or Author of Book : ")
  books=[]
  for items in book_objects:
    if(items.name==nam or items.author==nam):
      books.append(items)
  for items in books:
   print("Iban:" + items.iban)
   print("Name:" + items.name)
   print("Author:" + items.author)
   print("Issued:" + items.issued)   

def show_book(book_objects):
  i=1
  for items in book_objects:
    print("Book # ", i)
    print("Iban:" + items.iban)
    print("Name:" + items.name)
    print("Author:" + items.author)
    print("Issued:" + items.issued)
    print("\n")
    i=i+1

def main():
    flag = True
    while flag!=False:
        print("Select Any Number From the Following:\n")
        choice = input("1. Add a book.\n2. Search a book.\n3. Show all books present in the library.\n4. Issue a book.\n5. Return a book.\n6. Exit\nEnter your choice: ")
        if choice == "1":
            add_book(book_objects)
        elif choice == "2":
            search_book(book_objects)
        elif choice == "3":
            show_book(book_objects)
        elif choice == "4":
            Book.issue_book(book_objects)
        elif choice == "5":
            Book.return_book(book_objects)
        elif choice == "6":
            flag = False
        else:
            print("Invalid input. Please enter a valid option.")
   
   

if __name__ == "__main__":
    main()