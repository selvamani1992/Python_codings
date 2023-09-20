# Class for library management

class library:
  def __init__(self,data):
    self.bookList = data
  def showBooks(self): 
    for i in self.bookList: 
      print(i)

  def lendBook(self,bookName,student_name): 
    if bookName in self.bookList:
      self.bookList.remove(bookName)
      student_name.addbook(bookName)
      print("Thank you, your req is fulfilled") 
    else:
      print("Book is not available")
  def returnBook(self, bookName,student_name):
    if student_name.removeBook(bookName):
      self.bookList.append(bookName)
      print("Book returned successfully")
    else:
      print("Book not found in your list")

# Class for Student management

class student:
  objects = {}   #creating a dictionary to store student name as key and object name as value, this I will use late part for selecting object by run time input


  def __init__(self,Name,ID):
    self.name = Name
    self.id = ID
    self.books_taken = []
    self.objects[ID] = self

  def student_details(self):
    print("Name: ",self.name)
    print("ID No.: ",self.id)
    print("Books take:")
    self.showStudentBooks()

  def addbook(self, bookName):
    self.books_taken.append(bookName)

  def showStudentBooks(self):
    if len(self.books_taken) == 0:
      print("No books taken by the student")
    else:
      print("Books taken by the Student:")
      for book in self.books_taken:
        print(book)

  def removeBook(self, bookName):
    if bookName in self.books_taken:
      self.books_taken.remove(bookName)
      return True
    else:
      return False

# creating object for library and student classes
lib_A = library(["b1","b2","b3","b4","b5","b6","b7","b4","b4","b7"]) 
Student1 = student('selva','id001')
Student2 = student('mani','id002')

#IO section
id = input("Please enter Student ID:")
student_info = student.objects[id]
while True:
  print("\nselect the options from below") 
  print("\n1-Show list of books in Library\n2-Lend a book\n3-Show books which are taken by you\n4- Return a book\n5-Exit") 
  option = int(input()) 
  if option ==1: 
    lib_A.showBooks()
  elif option ==2: 
    requestedBook = input("Enter Book Name ")
    lib_A.lendBook(requestedBook,student_info) 
  elif option ==3: 
    student_info.student_details()
  elif option ==4:
    returningBook = input("Enter Book Name ")
    lib_A.returnBook(returningBook,student_info)
  elif option ==5:
    break
  else:
    Print("Select a valid Option")
