from datetime import datetime

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect

from requests import auth

from apps.todo_list.models import TodoList, Category
from apps.main.my_classes import my_date


from django.contrib import auth

def todo_list(request: render) -> JsonResponse:
    get_auth = auth.get_user(request).username
    #get_user_id = auth.get_user(request).id
    #print("request ------------->", auth.get_user(request).username)

    #print("request ------------->", request.POST)
    #====== insert data ======
    if request.method == 'POST':
        QueryDict = request.POST
        myDict = dict(QueryDict)
        print("myDict: -------------> ", myDict)
        #print("deadline ", my_date.date_to_db(myDict['deadline'][0]))
        now_raw = datetime.now()

        #print("DATATATAATTAAT: ", myDict['due_date'][0][:10], myDict['due_date'][0][-5:])

        #print("WTF: ", datetime.strptime('2023-09-02 21:30', "%Y-%m-%d %H:%M"))
        Chacnged_date = my_date.date_to_db
        print("nnnnnnnnnnnnnnnnnnn000  ", myDict['due_date'])
        print("DATATATAATTAAT: ", Chacnged_date(myDict['due_date'][0]))
        Result_of_fuck_with_date=Chacnged_date(myDict['due_date'][0])
        print('Result_of_fuck_with_date: ', Result_of_fuck_with_date)

        batch = TodoList(
            title=myDict['title'][0],
            content=myDict['content'][0],
            #created=str(now_raw.date()) + 'T' + str(now_raw.time())[:5],
            due_date=Result_of_fuck_with_date
            #due_date=datetime.strptime('2023-09-02', "%Y-%m-%d")
            #category='test insert'

        )
        print("batch: -------------> ", batch)
        TodoList.save(batch)
        print("database entry is correct -------------> ")
        return redirect('task_manager')

    data = {
        'get_auth': get_auth
    }


    return render(request, 'todo_list/todo_index.html', data)

