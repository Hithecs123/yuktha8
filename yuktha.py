q=[]
def enqueue():
    if len(q)==size:
        print("queue is full")
        else:
     item=input("enter the element:")
        q.append(item)
def dequeue.():
    if not q:
        print("queue is empty")
    else:
        item=q.pop(0)
        print("element removed is:",item)
def display():
    if not q:
        print("queue is empty")
   else:
        print(q)
size=int.(input("enter the size of queue:"))
while True:
    choice=int(input("1.insert 2.delete 3.display 4.quit enter your choice:"))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    else:
        break
