from datetime import date
import holidays


#custome made holidays

custom_holidays = holidays.HolidayBase()
year=2020

custom_holidays.append({"{0}-{1}-{2}".format(year,1,14): "Lohri"})
custom_holidays.append({"{0}-{1}-{2}".format(year,1,26): "Republic Day"})
custom_holidays.append({"{0}-{1}-{2}".format(year,2,21): "Maha Shivaratri/Shivaratri"})
custom_holidays.append({"{0}-{1}-{2}".format(year,3,10): "Holi"})
custom_holidays.append({"{0}-{1}-{2}".format(year,4,2): "Rama Navami"})
custom_holidays.append({"{0}-{1}-{2}".format(year,4,6): "Mahavir Jayanti"})
custom_holidays.append({"{0}-{1}-{2}".format(year,4,10): "Good Friday"})
custom_holidays.append({"{0}-{1}-{2}".format(year,4,14): "Ambedkar Jayanti"})
custom_holidays.append({"{0}-{1}-{2}".format(year,5,7): "Buddha Purnima/Vesak"})
custom_holidays.append({"{0}-{1}-{2}".format(year,5,25): "Ramzan Id/Eid-ul-Fitar"})
custom_holidays.append({"{0}-{1}-{2}".format(year,8,1): "Bakr Id/Eid ul-Adha"})
custom_holidays.append({"{0}-{1}-{2}".format(year,8,12): "Janmashtami"})
custom_holidays.append({"{0}-{1}-{2}".format(year,8,15): "Independence Day"})
custom_holidays.append({"{0}-{1}-{2}".format(year,10,25): "Dussehra"})
custom_holidays.append({"{0}-{1}-{2}".format(year,10,30): "Milad un-Nabi/Id-e-Milad"})
custom_holidays.append({"{0}-{1}-{2}".format(year,11,14): "Naraka Chaturdasi"})
custom_holidays.append({"{0}-{1}-{2}".format(year,11,14): "Diwali/Deepavali"})
custom_holidays.append({"{0}-{1}-{2}".format(year,11,15): "Govardhan Puja"})
custom_holidays.append({"{0}-{1}-{2}".format(year,11,16): "Bhai Duj"})



