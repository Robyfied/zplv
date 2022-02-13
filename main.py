from turtle import towards
from scripts.zplv import Scraper
from scripts.zplv import ProgressBar
import datetime
####
####  CA SA MODIFICI PENTRU ANUL URMATOR SCHIMBA IN scripts/zplv.py LINIILE 39, 40, 43 SI 56
####

_ = ProgressBar()
print(_.progress_bar(datetime.date.today()))
# inc_azi = Scraper().get_incidenta(datetime.date.today())
# inc_ieri = Scraper().get_incidenta(datetime.date.today() - datetime.timedelta(days = 1))
# output = open("output.txt", "w")
# if inc_azi is None:
#     print("plm coaie nu a aparut incidenta azi")
#     #TODO: sa afiseze "nu a aparut incidenta" in output.txt
# else:
#     print("Incidenta azi: ", inc_azi, "(+", f"{(inc_azi - inc_ieri):.2f}", ")")
