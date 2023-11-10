from datetime import datetime


class my_date:

    def __init__(self):
        print("maybe add some property?")

    def date_to_db(*self):
        print("FROM my classes self 0", self)
        if self[0] is None or self[0] == '' or self[0] == 0:
            form_date_to_db = datetime.now()
            print("FROM my classes self ZERO VALUES", datetime.now())
            print("FROM my classes self EXCEPT: ", datetime.strptime(datetime.now(), "%Y-%m-%d %H:%M:%S"))
        try:
            #print("FROM my classes self 1", self[0][:10], self[0][-5:])
            pars_date_to_text = self[0][:10] + ' ' + self[0][-5:] + ':00'
            print("FROM my classes TRY 1: ", pars_date_to_text)
            form_date_to_db = datetime.strptime(pars_date_to_text, "%Y-%m-%d %H:%M:%S")
            #print("FROM my classes self 2", datetime.datetime.strptime('2023-09-02 21:30', "%Y-%m-%d %H:%M"))
            #form_date_to_db = datetime.datetime.strptime(self, "%Y-%m-%d %H:%M")
            print("FROM my classes TRY 2 (form_date_to_db): ", form_date_to_db)
        except:
            print("FROM my classes except: ", form_date_to_db)
            form_date_to_db = None
            #form_date_to_db = datetime.now()

        return form_date_to_db
        print("FROM my classes self RESULT: ", form_date_to_db)


    def composite_date(*self):
        print("my_date.composite_date: ", self)
        if not self[0]:
            print("my_date.composite_date: ", "is none")
            form_date_to_db = None
        else:
            print("my_date.composite_date: ", "is not none")
            try:
                #form_date_to_db = datetime.datetime.strptime(self[0] + 'T' + self[1], "%Y-%m-%dT%H:%M")
                form_date_to_db = str(self[0] + 'T' + self[1])
            except:
                form_date_to_db = None

        return form_date_to_db
