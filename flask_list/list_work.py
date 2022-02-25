

task_list=["task 1", "task 2", "task 3"]
def addTask(task):
    task_list.append(task)
    return task_list


def delete_task():
    task_list.pop()
    return task_list


def list_item():
    return task_list
