# local, encosing, global, built-in variables

# x = "global x"
#
# def fonk():
#     y = "local y"
#     print(y)
#
# fonk()
# print(y) local değişken olduğu için fonksiyon dışından ulaşamayız

# x = "global x"

# def outer():
# #     x = "enclosing x"
# #     print(x)
# #     def inner():
# #         x = "local x"
# #         #x = "local x"
# #         print(x) # yukarıdaki x'i kapatırsak, local x olmadığı için bir üstteki enclosing x'i yazdırır.
# #     inner()
# #
# # outer() # ilk önce "enclosing x" yazdırılır, sonra "local x" çağrıldığı için yazdırılır.
# # print(x)# en son global x çağrıldığı içim "global x" yazdırır.
# # # enclosing x
# # # local x
# # # global x

# def outer():
#     #x = "enclosing x"
#     print(x)# yukarıdaki x'i kapatırsak, enclosing x olmadığı için bir üstteki global x'i yazdırır.
#     def inner():
#         x = "local x"
#         #x = "local x"
#         print(x)
#     inner()
#
# outer() # ilk önce "enclosing x" yazdırılır, sonra "local x" çağrıldığı için yazdırılır.
# print(x)# en son global x çağrıldığı içim "global x" yazdırır.
# # global x
# # local x
# # global x

# def outer():
#     #x = "enclosing x"
#     print(x)# yukarıdaki x'i kapatırsak, enclosing x olmadığı için bir üstteki global x'i yazdırır.
#     def inner():
#         #x = "local x"
#         print(x)# yukarıdaki x'i kapatırsak, enclosing x olmadığı için bir üstteki global x'i yazdırır.
#     inner()
#
# outer() # ilk önce "enclosing x" yazdırılır, sonra "local x" çağrıldığı için yazdırılır.
# print(x)# en son global x çağrıldığı içim "global x" yazdırır.
# # global x
# global x
# global x

# x = "global x"
# def fonk():
#     global x # yukarıdaki global x'i buna atadık ve yeni değer 5 aldı
#     x = 5
# fonk()
# print(x) # 5

x = "global x"
def outer():
    x = "enclosing x"
    print(x)
    def inner():
        nonlocal x
        x = 5
    inner()
    print(x)

outer()
# enclosing x
# 5




