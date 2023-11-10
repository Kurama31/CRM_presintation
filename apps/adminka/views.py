import datetime
from pprint import pprint
from django.contrib import auth
from django.shortcuts import render, redirect
from apps.todo_list.models import Category
from django.db import connection
now = datetime.datetime.now()

def adminka(request):
    # now = datetime.datetime.now()
    get_auth = auth.get_user(request).username  # получить пользователя из реквеста
    get_user_id = auth.get_user(request).id
    latest_id = Category.objects.latest('id').id
    new_id = int(latest_id) + 1

    if request.method == 'POST':
        QueryDict = request.POST
        myDict = dict(QueryDict)
        print("myDict: -------------> ", myDict['title'][0])
        #Category.objects.raw("INSERT INTO todo_list_category(id, name) VALUES(2, 'test2')")
        #INSERT INTO todo_list_category(id, name) VALUES(1, 'test1');


    def my_custom_sql(self):
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO todo_list_category(id, name) VALUES(2, 'test2')", [self.baz])

            row = cursor.fetchone()

        return row
    #for p in Category.objects.raw('SELECT id, name FROM todo_list_category'):
    #    print("sql_test: ", p.name)
    #sql_test = Category.objects.raw("SELECT id, name FROM todo_list_category")
    #print("sql_test: ", sql_test)
    #print("sql_test type: ", type(sql_test))
    #print("sql_test: ", sql_test[0].name)
    data = {
        'get_auth': get_auth,
        'new_id': new_id,
        'error': 'Request failed successfully'
    }

    return render(request, 'admin/adminka.html', data)

