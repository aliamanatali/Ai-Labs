class Book:
  def __init__(self, iban, name, author, issued):
    self.iban = iban
    self.name = name
    self.author = author
    self.issued = issued

  def issue_book(book_objects):
    ib = input("Enter Iban Number of book you want to issue: ")
    for items in book_objects:
      if(items.iban==ib):
        if(items.issued=="0"):
          print("The book is availiable and has been issued.")
          items.issued="1"
        elif(items.issued=="1"):
          print("The book has already been issued. ")
      else:
          print("Invalid IBAN Number")
  def return_book():
    ib = input("Enter Iban Number of book you want to return: ")
    for items in book_objects:
      if(items.iban==ib):
        if(items.issued=="0"):
          print("This book has not been issued.")
        elif(items.issued=="1"):
          print("The book has been returned")
          items.issued="0"
      else:
          print("Invalid IBAN Number")
def add_book(book_objects):
  ib = input("Enter Iban Number : ")
  nme = input("Enter Book Name : ")
  auth = input("Enter Author's Name :")
  obj=Book(ib,nme,auth,"0")
  book_objects.append(obj)
  
# def search_book():
# def show_book():

