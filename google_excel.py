import gspread
import time



se=gspread.service_account(filename='data-collection.json')
sh=se.open("DHT11_Monitoring")

wks=sh.worksheet('Sheet1')

def read_value(worksheet):
    values=worksheet.get_all_values()
    col=f"H"+str(len(values))
    print(col)
    worksheet.update(col,"Done")
    return values[-1][0:8]
list = []
while True:
    # print(read_value(wks))
    list.append(read_value(wks))
    val= list[-1]
    print(val)
    time.sleep(5)

    