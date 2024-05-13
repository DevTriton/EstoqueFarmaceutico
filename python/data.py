from datetime import datetime

data=input("digite a data Ex: 14/11/2023")
data = datetime.strptime(data, "%d/%m/%Y")
databr=data.strftime("%d/%m/%Y")
print(databr)

hoje=datetime.now()

if data<hoje:
    print("joga")
else:
    print("fodase")    