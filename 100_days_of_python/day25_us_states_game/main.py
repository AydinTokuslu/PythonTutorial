import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data: # çok veri olduğunda bununla yapamayız
#         if row != "temp":  # onun yerine pandas kütüphanesi ile hızlıca yapabiliriz.
#             temperatures.append(row[1])
#     print(temperatures)

data = pandas.read_csv("weather_data.csv")
#print(data["temp"])
data_dict = data.to_dict()
#print(data_dict)  # dictionary'e çevirir.

temp_list = data["temp"].to_list()
#print(temp_list)  # list'e çeviririz., [12, 14, 15, 14, 21, 22, 24]
# avg = 0
# for i in temp_list:
#     print(i)
#     avg += i
# print(f"average temperature : {avg/len(temp_list)}") #average temperature : 17.428571428571427
# # ortalama sıcaklığı böyle uzun uzun bulmak yerine, pandas ile :
# print(data["temp"].mean())  # 17.428571428571427
# print(data["temp"].max())  # 24

# # get data in columns
# print(data["condition"])  # aynısı
# print(data.condition)  # aynısı

# get data in rows
# print(data[data.day == "Monday"])

# sıcaklığın en yüksek olduğu günü bulmak
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# #MONDAY'İN TEMPİNİ FAHRENEİGHT'A ÇEVİRMEK
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)  # 53.6

#create dataframe from scratch
data_dict = {
    "students" : ["Amy","James","Angela"],
    "scores" : [76, 56, 65]
}
data = pandas.DataFrame(data_dict)  # data frame oluştururuz
data.to_csv("new_data.csv")  # ouşturduğumuz yeni verileri yeni new_data.csv klasörünü
# oluşturup içine yazarız.
















