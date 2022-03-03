import textwrap
from scripts.zplv import Scraper
from scripts.zplv import Progress
import datetime as dt
from pandas import errors as PandasErrors
from requests import exceptions as RequestsErrors
####
####  CA SA MODIFICI PENTRU ANUL URMATOR MODIFICA IN scripts/zplv.py LINIILE 35, 36, 38, 51, 57 SI 63
####

output = open("output.txt", "w", encoding="utf-8")

try:
    inc_azi = Scraper().get_incidenta(dt.date.today())
    inc_ieri = Scraper().get_incidenta(dt.date.today() - dt.timedelta(days=1))
except PandasErrors.EmptyDataError: 
    output.write("!!! S-A BUSIT SCRAPERUL. DATA DOWNLOAD FAILED.")
    print("!!! S-A BUSIT SCRAPERUL. DATA DOWNLOAD FAILED.")
    inc_azi, inc_ieri = 0, 0
except RequestsErrors.ConnectionError:
    output.write("!!! NO INTERNET. DATA DOWNLOAD FAILED.")
    print("!!! NO INTERNET. DATA DOWNLOAD FAILED.")
    inc_azi, inc_ieri = 0, 0
if inc_azi is None:
    output.write("!!! INCA NU A APARUT INCIDENTA AZI")
    print("!!! INCA NU A APARUT INCIDENTA AZI")
    inc_azi, inc_ieri = 0, 0


if dt.date.today() > dt.date(2022, 6, 10):
    output.write("\nE vacanta de vara!\n Asteapta sa inceapa anul scolar ca sa updatez programul si stai la curent cu http://github.com/Robyfied/zplv")
else:
    dif = round(inc_azi - inc_ieri, 2)
    if dif < 0:
        dif_print = str(dif) + "↓"
    elif dif > 0:
        dif_print = "+" + str(dif) + "↑"
    else:
        dif_print = "+0.0"

    if Progress().days_until_vacation() == 0:
        text = textwrap.dedent(f"""
            [{dt.date.today().strftime("%d.%m.%Y")}]    
            // ziua {Progress().school_days(dt.date.today())} de scoala//
                            
            Vacanta placuta !
            * Incidenta azi: {inc_azi} ({dif_print})

            Anul scolar: {Progress().progress_bar(dt.date.today())}
        """)
        print(text)
        output.write(text)
    else:
        text = textwrap.dedent(f"""
                [{dt.date.today().strftime("%d.%m.%Y")}]    
                // ziua {Progress().school_days(dt.date.today())} de scoala//
                                
                {Progress().days_until_vacation()} zile pana la vacanta ({Progress().schooldays_until_vacation()} zile de scoala)
                * Incidenta azi: {inc_azi} ({dif_print})

                Anul scolar: {Progress().progress_bar(dt.date.today())}
                """)
        print(text)
        output.write(text)
output.close()
