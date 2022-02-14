import textwrap
from turtle import towards
from scripts.zplv import Scraper
from scripts.zplv import Progress
import datetime as dt
from pandas import errors as PandasErrors
####
####  CA SA MODIFICI PENTRU ANUL URMATOR MODIFICA IN scripts/zplv.py LINIILE 35, 36, 38, 51, 57 SI 63
####

output = open("output.txt", "w", encoding="utf-8")
try:
    inc_azi = Scraper().get_incidenta(dt.date.today())
    inc_ieri = Scraper().get_incidenta(dt.date.today() - dt.timedelta(days=1))
except PandasErrors.EmptyDataError: 
    output.write("!!! S-A BUSIT SCRAPERUL")
    inc_azi, inc_ieri = 0, 0

if dt.date.today() > dt.date(2022, 6, 10):
    output.write("\nE vacanta de vara!\n Asteapta sa inceapa anul scolar ca sa updatez programul si stai la curent cu http://github.com/Robyfied/zplv")
elif inc_azi is None:
    output.write("INCA NU A APARUT INCIDENTA AZI (sau s-a stricat scraperul)")
else:
    dif = round(inc_azi - inc_ieri, 2)
    if dif < 0:
        dif_print = str(dif) + "↓"
    elif dif > 0:
        dif_print = "+" + str(dif) + "↑"
    else:
        dif_print = "+0.0"

    if Progress().days_until_vacation() == 0:
        output.write(textwrap.dedent(f"""
            [{dt.date.today().strftime("%d.%m.%Y")}]    
            // ziua {Progress().school_days(dt.date.today())} de scoala//
                            
            Vacanta placuta !
            * Incidenta azi: {inc_azi} ({dif_print})

            Anul scolar: {Progress().progress_bar(dt.date.today())}
        """))
    if dif < 0:
        text = f"""
                [{dt.date.today().strftime("%d.%m.%Y")}]    
                // ziua {Progress().school_days(dt.date.today())} de scoala//
                                
                {Progress().days_until_vacation()} zile pana la vacanta ({Progress().schooldays_until_vacation()} zile de scoala)
                * Incidenta azi: {inc_azi} ({dif_print})

                Anul scolar: {Progress().progress_bar(dt.date.today())}
                """
        output.write(textwrap.dedent(text))
output.close()
