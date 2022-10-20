from collections import defaultdict
import pickle

Book_Name=[]
Book_Genre=[]
Shelf_No=[]
Status=[]
Cost=[]

i=0
myDict1 = {}
def creation():
   ##Inputs of book
   f=open("book_details.dat",'wb')
   book_id=int(input("Enter Book ID:"))
   book_name=input("Enter Book Name:")
   book_genre=input("Enter Book Genre:")
   shelf_no=int(input("Enter Shelf No."))
   status=input("Enter Availablity:")
   cost=int(input("Enter The Price of Book:"))
   ##lists
   Book_ID=defaultdict(list)
   Book_ID["id"].append(book_id)
   Book_ID["name"].append(book_name)
   Book_ID["genre"].append(book_genre)
   Book_ID["shelf"].append(shelf_no)
   Book_ID["status"].append(status)
   Book_ID["cost"].append(cost)
  ##dictionary of book
  ## print(i)
   global i
   i=i+1
   myDict1[i]=Book_ID
   pickle.dump(myDict1,f)
   f.close()

##Customer
j=0
mydict2={}
Cust_ID = []
Cust_Name = []
Issue_Date=[]
Return_Date=[]
def creation1():
   ##inputs of customer
   a=open("BookIssuer_Details.dat",'wb')
   cust_id = int(input("Enter Customer ID:"))
   cust_name = input("Enter Customer Name:")
   issue_date=input("Enter the Issue Date:")
   return_date=input("Enter the Return Date:")
   ##lists of customer
   Cust_ID=defaultdict(list)
   Cust_ID["ID"].append(cust_id)
   Cust_ID["Name"].append(cust_name)
   Cust_ID["Issue Date"].append(issue_date)
   Cust_ID["Return Date"].append(return_date)
   ##dictionary of customer
   global j
   j=j+1
   mydict2[j]=Cust_ID
   pickle.dump(mydict2,a)
   a.close()
##display of books
def display():
   b=open("book_details.dat",'rb')
   c=pickle.load(b)
   print(c)
##display of customers
def display1():
   d=open("BookIssuer.dat",'rb')
   e=pickle.load(d)
   print(e)

##def searching():
   ## x=open("book_details.dat",'rb')
    ##y=pickle.load(x)
    ##q=input("Enter the value to be searched:")
    ##if myDict.values()==q:
      ##  print(myDict)

##menu
print("1.Creation of Book Data")
print("2.Creation of Customer Data")
print("3.Display of Book Data")
print("4.Display of Customer Data")
print("5.Quit")
while True:
   n = int(input("Enter your Choice:"))
   if n == 1:
      creation()
   elif n == 2:
      creation1()
   elif n == 3:
      display()
   elif n == 4:
      display1()
   elif n==5:
      break
##   elif n == 5:
  ##    searching()
   else:
      print("invalid choice")
