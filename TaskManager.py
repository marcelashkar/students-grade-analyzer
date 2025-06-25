def creat_task(title,duration,priority):
    return {"title":title,"duration":duration,"priority":priority}
      

def insert(queue,task):
    queue.append(task)


def extract(queue):
    if queue:
        return queue.pop(0)
    return None
    
def peek(queue):
    if queue:
        return queue[0]
    return None

def is_empty(queue):
    return len(queue)==0



def complete_next_task(queue):
    if is_empty(queue):
        print("IS EMPTY")
        return
    highest = min(queue,key=lambda task:task["priority"])
    print("the highest title:",title,"priority",priority)

def sort_tasks(queue):
    return sorted(queue,key=lambda task:task['duration'])

def search_for_task(queue,title):
    sorted(queue,key=lambda task:task('title'))
    return


def binary_search(queue,title):
    low = 0
    high = len(queue) - 1
    while low <=high:
        mid = (low + high) // 2
        if queue[mid]['title'] == title:
            return queue[mid]
        elif queue[mid]['title']< title:
            low=mid+1
        else:
             high=mid - 1
    return None
                         

def main():
    queue = []
    count = int(input("Number of tasks"))
    for i in range(count):
               title = input("Enter title: ")
               duration = int(input("Enter duration: "))
               priority = int(input("Enter priority: "))
               task= creat_task(title,duration,priority)
               insert(queue,task)
    for task in queue:
        print(task)


    print("complete next task",complete_next_task(queue))

    for task in queue:
        print(task)

    print("sort task",sort_tasks(queue))
    
   
    search=input("enter your title task")
    result=search_for_task(queue,search)
    if result:
        print(result)
    else:       
             print("not found")

         
