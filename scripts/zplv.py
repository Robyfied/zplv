import datetime as dt
import requests
import tabula
import os
import pandas as pd

####
#### CA SA MODIFICI PENTRU ANUL URMATOR MODIFICA LINIILE 35, 36, 38, 51, 57 SI 63
####

class Scraper:
    def get_incidenta(self, _date: dt.date):
        _csv_name = "incidenta-" + str(_date) + ".csv"
        if not os.path.isfile("./downloads/" + _csv_name):
            _pdf_name = "INCIDENTA-JUDETUL-GALATI-" + str(_date.strftime("%d.%m.%Y")) + ".pdf"
            #downloads pdf
            link = "https://gl.prefectura.mai.gov.ro/wp-content/uploads/sites/46/" + str(_date.strftime("%Y")) + "/" + str(_date.strftime("%m")) + "/" + _pdf_name
            r = requests.get(link)
            if r.status_code == 404:
                return None
            else:
                pdf = open("./downloads/" + _pdf_name, "wb")
                pdf.write(r.content)
                pdf.close()
                tabula.convert_into("./downloads/" + _pdf_name, "./downloads/" + _csv_name, output_format="csv", pages='all',  java_options="-Dfile.encoding=UTF8")
                os.remove("./downloads/" + _pdf_name)

        #returns value for MUNICIPIUL GALATI
        df = pd.read_csv("./downloads/" + _csv_name)
        df.columns = ["Judet", "Localitate", "Populatie", "Incidenta", "Cazuri Confirmate"]
        return df.Incidenta[df.Localitate == "MUNICIPIUL GALAŢI"].values[0]

class Progress:
    def school_days(self, _date: dt.date):
        _days_off = [dt.date(2021, 10, 5), dt.date(2021, 11, 30), dt.date(2021, 12, 1), dt.date(2021, 12, 23), dt.date(2021, 12, 24), dt.date(2021, 12, 27), dt.date(2021, 12, 28), dt.date(2021, 12, 29), dt.date(2021, 12, 30), dt.date(2021, 12, 31), dt.date(2022, 1, 24),  dt.date(2022, 4, 15), dt.date(2022, 4, 18), dt.date(2022, 4, 19), dt.date(2022, 4, 20), dt.date(2022, 4, 21), dt.date(2022, 4, 22), dt.date(2022, 4, 23), dt.date(2022, 4, 25), dt.date(2022, 4, 26), dt.date(2022, 4, 27), dt.date(2022, 4, 28), dt.date(2022, 4, 29), dt.date(2022, 6, 1)]
        _curr_date = dt.date(2021, 9, 13)   # first day of school
        school_days = 0
        while _curr_date <= dt.date(2022, 6, 10):   # last day of school
            school_days += 1
            if _curr_date.weekday() > 4:
                school_days -= 1
            else:
                for d in _days_off:
                    if _curr_date == d:
                        school_days -= 1
            if _curr_date == _date:
                return school_days
            _curr_date += dt.timedelta(days=1)

    def days_until_vacation(self):
        _vacation_days = [dt.date(2021, 12, 24), dt.date(2022, 4, 15), dt.date(2022, 6, 10)]
        for day in _vacation_days:
            if dt.date.today() <= day:
                return (day - dt.date.today()).days

    def schooldays_until_vacation(self):
        _vacation_days = [dt.date(2021, 12, 24), dt.date(2022, 4, 15), dt.date(2022, 6, 10)]
        for day in _vacation_days:
            if dt.date.today() <= day:
                return (self.school_days(day) - self.school_days(dt.date.today()))

    def progress_bar(self, _date: dt.date):
        perc = round(self.school_days(_date) / 171 * 100, 2)   # 171 = total school days
        bar = ""
        i = 5
        while i <= 100:
            if i <= perc:
                bar += "▰"
            else:
                bar += "▱"
            i += 5
        return (bar + " " + str(perc) + "%")
        
    





