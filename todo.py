import sys
import os.path
from datetime import datetime
def addItem(item):
    if(os.path.isfile("todo.txt")):
        with open("todo.txt","r") as f:
            todoitems = f.read()
        with open("todo.txt","w") as f:
            f.write(item+'\n'+todoitems)
    else:
        with open("todo.txt","w") as f:
            f.write(item)
    print("Added todo: \"{}\"".format(item))

def ls():
    if(os.path.isfile("todo.txt")):
        with open("todo.txt","r") as f:
            todoItems = f.readlines()
        count = len(todoItems)
        insertItem = ''
        for item in todoItems:
            insertItem = '[{}] {}'.format(count,item)
            sys.stdout.buffer.write(insertItem.encode('utf8'))
            count-=1
        print('\n')
    else:
        print("There are no pending todos!")

def delItem(number):
    if(os.path.isfile("todo.txt")):
        with open("todo.txt","r") as f:
            todoItem = f.readlines()
        if int(number) < 1 or int(number) > len(todoItem):
            print("Error: todo #{} does not exist. Nothing deleted.".format(number))
        else:
            with open("todo.txt", "w") as f:
                count = len(todoItem)
                for item in todoItem:
                    if count != int(number):
                        f.write(item)
                    count-=1
    print("Deleted todo #{}".format(number))

def done(number):
    doneItem = ''
    if(os.path.isfile("todo.txt")):
        with open("todo.txt","r") as f:
            todoItem = f.readlines()
        if int(number) < 1 or int(number) > len(todoItem):
            print("Error: todo #{} does not exist.".format(number))
            pass
        else:
            with open("todo.txt", "w") as f:
                count = len(todoItem)
                for item in todoItem:
                    if count != int(number):
                        f.write(item)
                    else:
                        doneItem = item
                    count-=1
            if(os.path.isfile("done.txt")):
                with open("done.txt","r") as f:
                    todoitems = f.read()
                with open("done.txt","w") as f:
                    f.write("x "+datetime.today().strftime("%Y-%m-%d")+" "+doneItem+todoitems)
            else:
                with open("done.txt","w") as f:
                    f.write(doneItem)
            print("Marked todo #{} as done.".format(number))

def help():
    print("""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics""")


def report():
    if os.path.isfile("todo.txt"):
        with open("todo.txt","r") as f:
            todoItems = f.readlines()
        todoCount = len(todoItems)
    else:
        todoCount = 0
    if os.path.isfile("done.txt"):
        with open("done.txt","r") as f:
            doneItems = f.readlines()
        doneCount = len(doneItems)
    else:
        doneCount = 0
    print(datetime.today().strftime("%Y-%m-%d") + " Pending : {} Completed : {}".format(todoCount,doneCount),end='' )


def main():
    if len(sys.argv)==1:
        help()
    elif sys.argv[1] == 'add':
        if(len(sys.argv)>2):
            addItem(sys.argv[2])
        else:
            print("Error: Missing todo string. Nothing added!")
    elif sys.argv[1] == 'ls':
        ls()
    elif sys.argv[1] == 'del':
        if(len(sys.argv)>2):
            delItem(sys.argv[2])
        else:
            print("Error: Missing NUMBER for deleting todo.")
    elif sys.argv[1] == 'done':
        if len(sys.argv)>2:
            done(sys.argv[2])
        else:
            print("Error: Missing NUMBER for marking todo as done.",end='')
    elif sys.argv[1] == 'help':
        help() 
    elif sys.argv[1] == 'report':
        report()
    else:
    	print("Option not available. Use 'help' to see usage",end='')

if __name__ == "__main__":
    main()
