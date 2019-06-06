
import datetime

TEMPLE_DESTROYED = 70


def shmita_year():
    now = datetime.datetime.now()
    year = now.year
    # 0. find out how many years since the temple was destroyed
    year -= TEMPLE_DESTROYED
    # 1. add one year because the temple was destroyed in year 1 in the cycle
    year += 1
    # 2. discard centuries, because each century is like 2 yovels (jubilees) - 50 years,
    # which is 7 shmitot.
    centuries_num = year / 100
    year = year % 100
    # 3. add 2 years for each discarded century, because 7 shmitot is 49, not 50,
    # so we need to add back the missing years. (According to Rabbi Yehuda)
    year += (centuries_num * 2)
    # 4. divide the single years (decades + singles) in 7 to get what year in the cycle we are in now
    shmita = year % 7
    print "In the year %d, the Shmita year is %d in the 7-year cycle" % (now.year, shmita)


shmita_year()
