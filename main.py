from book import Book

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

# book_obj=Book('12345','Discrete Structures','Moris','0')
Book.issue_book(book_objects)