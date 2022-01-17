class Node:
    def __init__(self, Roll_Number, Year, Semester, Email):
        self.Roll_Number = Roll_Number
        self.Year = Year
        self.Semester = Semester
        self.Email = Email
        self.next = None
        self.Previous = None

    def Display(self):
        print('Roll Number.:',",",self.Roll_Number,",",'Year:',self.Year,",",'Semester:',self.Semester,",",'Email:',self.Email)

    def Get_RollNumber(self):
        return self.Roll_Number

class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def Add_at_Start(self,node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.size = self.size + 1
        else:
            node.next = self.head 
            self.head.Previous = node
            self.head = node
            self.size = self.size + 1

    def Addt_at_End(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
            self.size = self.size + 1
        else:
            node.Previous = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node
            self.size = self.size + 1 
    
    def Add_Any_Position(self,Index,node):
        if Index == 0:
            self.Add_at_Start(node)
            return
        if Index == (self.size-1):
            self.Addt_at_End(node)
            return
        if Index >= self.size:
            print('Invalid Index')
            return
        if Index < 0:
            print('Invalid Index')
            return
        Temp = self.head
        store   = 0
        for i in range(Index-1):
            Temp = Temp.next
        store = Temp.next
        Temp.next = node
        node.Previous = Temp
        node.next = store
        store.Previous = node
        self.size = self.size + 1

    def Delete_Start(self):
        if self.size  == 1:
            self.head  = self.head.next
            self.size -= 1
            print('The List is Empty.')
        else:
            self.head     = self.head.next
            self.head.Previous = None
            self.size = self.size - 1
                def Delete_End(self):
            if self.size == 1:
            self.Delete_Start()
            return
        Temp = self.tail
        self.tail = self.tail.Previous
        self.tail.next = None
        Temp = None
        self.size = self.size - 1
  
    def Delete_Any_Position(self,Index):
        if Index == 0:
            if self.size == 1:
                print("This List is Empty.")
                self.Delete_Start()
                return
        if Index >= self.size:
            print('Invalid Index')
            return
        if Index <  0:
            print('Invalid Index')
            return
        if Index == (self.size-1):
            self.Delete_End()
            return
        Current = 0
        Current_Previous = 0
        Temp = self.head
        for i in range(Index):
            Temp = Temp.next
        Current = Temp.next
        Current_Previous = Temp.Previous
        Current_Previous.next = Current
        Current.Previous = Current_Previous
        self.size = self.size - 1  

    def Search_RollNumber(self):
        Temp = self.head
        Roll_Number = int(input('Enter Roll_Number to search: '))
        while Temp != None:
            if Temp.Get_RollNumber() == Roll_Number:
                print('Roll Number is Present in List.')
                break
            if Temp.Get_RollNumber() != Roll_Number:
                if Temp.next is None:
                    print('Roll Number is Present in not List')
            Temp = Temp.next
            
    def Previous_Student(self):
        Temp = self.head
        Roll_Number = int(input('Enter Roll_Number to search: '))
        while Temp != None:
            if Temp.Get_RollNumber() == Roll_Number:
                Temp.Previous.Display()
                break
            if Temp.Get_RollNumber() != Roll_Number:
                if Temp.next == None:
                    print('Roll Number is Present in not List')
            Temp = Temp.next

    def Reverse_List(self):
        Temp = self.tail
        while Temp != self.head.Previous:
            Temp.Display()
            Temp = Temp.Previous
                    
    def Display_Values(self):
        Temp = self.head
        while Temp != None:
            Temp.Display()
            Temp = Temp.next

    def Menu(self):
        print('Enter "a" to add node at start of doubly Linked List')
        print('Enter "b" to add node at any postion of doubly Linked List')
        print('Enter "c" to add node at end of doubly Linked List')
        print('Enter "d" to delete node at start of doubly Linked List')
        print('Enter "e" to delete node at any position of doubly Linked List')
        print('Enter "f" to delete node at end of doubly Linked List')
        print('Enter "g" to check the existence of student data in doubly Linked List')
        print('Enter "h" to print doubly Linked List in forward order')
        print('Enter "i" to print doubly Linked List in reverse order')
        print('Enter "j" to check the data of previous student in doubly Linked List')
        print('Enter "k"to stop the program')
        Do = input("Please Press S to start the program: ")
        while Do != "k":
            Choice = input('Please select your choice from above and enter here: ')
            if Choice == 'a':
                loop = input("enter how many time you want to insert node: ")
                for i in range(int(loop)):
                    Roll_Number = int(input('Enter Roll_Number of student:'))
                    Year = int(input('Enter Year of student:  '))
                    Semester = input('Enter Semester of student:')
                    Email = input('Enter Email of student:')
                List.Add_at_Start(Node(Roll_Number,Year,Semester,Email))
                List.Display_Values()
            if Choice == 'b':
                Roll_Number = int(input('Enter Roll_Number of student:'))
                Year = int(input('Enter Year of student:  '))
                Semester = input('Enter Semester of student:')
                Email = input('Enter Email of student:')
                Index = int(input('At what position you want to add this node:'))
                List.Add_Any_Position(Index,Node(Roll_Number,Year,Semester,Email))
                List.Display_Values()
            if Choice == 'c':
                loop = input("enter how many time you want to insert node: ")
                for i in range(int(loop)):
                    Roll_Number = int(input('Enter Roll_Number of student:'))
                    Year = int(input('Enter Year of student:  '))
                    Semester = input('Enter Semester of student:')
                    Email = input('Enter Email of student:')
                List.Addt_at_End(Node(Roll_Number,Year,Semester,Email))
                List.Display_Values()
            if Choice == 'd':
                List.Delete_Start()
                List.Display_Values()
            if Choice == 'e':
                Index = int(input('Enter Index to delete Values: '))
                List.Delete_Any_Position(Index)
                List.Display_Values()
            if Choice == 'f':
                List.Delete_End()
                List.Display_Values()
            if Choice == 'g':
                List.Search_RollNumber()
            if Choice == 'h':
                List.Display_Values()
            if Choice == 'i':
                List.Reverse_List()
            if Choice == 'j':
                List.Previous_Student()
            if Choice == 'k':
                break

List = Doubly_Linked_List()
List.Menu()