import time
import json

fd = open("record.json", 'r')
js = fd.read()
fd.close()

ui_pr = []
ui_qn = []
sale = ''
sub_t = 0
record = json.loads(js)
more = True

print('--------------------Menu--------------------')
for key in record.keys():
    print(key, " : ", record[key]['Name'], '|', record[key]['Price'], "|", record[key]['Qn'])
print('--------------------------------------------')
ui_name = str(input("Enter your name    : "))
ui_mail = str(input("Enter Mail ID      : "))
ui_ph = str(input("Enter Phone No     : "))
j = 0
while (more == True):
    ui_pr.append(str(input('Enter product Id : ')))
    ui_qn.append(int(input('Enter Quantity   : ')))
    if (record[ui_pr[j]]['Qn'] < ui_qn[j]):
        print("Sorry we don't have enough quantity")
        print("We are having", record[ui_pr[j]]["Qn"], 'more left')
        ch = input('If you still want to buy press Y/y: ')
        if (ch == 'Y' or ch == "y"):
            ui_qn.pop()
            ui_qn.append(record[ui_pr[j]]["Qn"])
        else:
            ui_pr.pop()
            ui_qn.pop()
    m = input('Do you want more press Y/y : ')
    j = j + 1
    if (m == 'Y' or m == 'y'):
        more = True
    else:
        more = False

        print('--------------------------------------------')
print('                  BILL                      \n')
for i in range(len(ui_pr)):
    record[ui_pr[i]]["Qn"] = record[ui_pr[i]]["Qn"] - ui_qn[i]
    print('Name                       : ', record[ui_pr[i]]['Name'])
    print('Price                      : ', record[ui_pr[i]]['Price'], 'Rs')
    print('Quantity                   : ', ui_qn[i])
    print('                           : ', record[ui_pr[i]]['Price'] * ui_qn[i], "\n")
    sub_t = sub_t + int(record[ui_pr[i]]['Price']) * ui_qn[i]

print('--------------------------------------------')
print('Sub Total                      : ', sub_t, 'Rs\n')

if (sub_t > 5000):
    print("Less Discount 10%              : ", sub_t * 10 / 100)
    print("Taxable amount                 : ", sub_t - (sub_t * 10 / 100), "\n")
    sub_t = sub_t - (sub_t * 10 / 100)
print('cgst 6%                        : ', sub_t * 6 / 100)
gst = 2 * sub_t * 9 / 100
print('sgst 6%                        : ', sub_t * 6 / 100)
print('Total                          : ', sub_t + gst)
print('--------------------------------------------')

# +","+ui_pr+","+record[ui_pr]["Name"]+","+str(ui_qn)+","+str(record[ui_pr]["Price"])+","+time.ctime()+"\n"
sale_temp = ui_name + "," + ui_mail + "," + ui_ph + ',' + str(sub_t + gst)
for i in range(len(ui_pr)):
    sale = sale + ',' + ui_pr[i] + "," + record[ui_pr[i]]["Name"] + "," + str(ui_qn[i]) + "," + str(
        record[ui_pr[i]]["Price"]) + "," + time.ctime()

sale = sale_temp + sale + '\n'
js = json.dumps(record)
fd = open("record.json", 'w')
fd.write(js)
fd.close()

fd = open('Sales_json.txt', 'a')
fd.write(sale)
fd.close()

print('')
print("---------------------------------------------")
print("  Thanks for your order, Inventory Updated!  ")
print("---------------------------------------------")
input('Press any button to exit')