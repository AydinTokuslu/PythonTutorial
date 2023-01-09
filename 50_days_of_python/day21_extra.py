# Write a function called even_or_average that ask a user to
# input five numbers. Once the user is done, the code should
# return the largest even number in the inputted numbers. If
# there is no even number in the list, the code should return the
# average of all the five numbers.


num_list=[]
for i in range(5):
    num = int(input("Lütfen bir sayı giriniz : "))
    num_list.append(num)

def even_or_average(num_list):
    toplam=0
    even_num=[]
    for sayi in num_list:
        if sayi%2==0:
            even_num.append(sayi)
        else:
            toplam+=sayi
    if len(even_num) > 0:
        return f"Girilen sayıların en büyük çift sayısı : {max(even_num)}"
    else:
        return f"Girilen sayıların ortalaması : {toplam//5}"



print(even_or_average(num_list))



