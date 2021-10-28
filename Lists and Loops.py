# #Exercise 1
# wordList = ['mix', 'xyz', 'apple', 'xanadu',"rovio"]
# # xwordList = []
# # noxwordList = []
# # newList = []
# #
# # for item in wordList:
# #     if "x" in item[0]:
# #         xwordList.append(item)
# #     else:
# #         noxwordList.append(item)
# #
# # xwordList.sort()
# # noxwordList.sort()
# #
# # print(xwordList)
# # print(noxwordList)
# # newList += xwordList + noxwordList
# # print(newList)


# # Exercise 2
# wordList = ["xxx", "aaa", "r5t6yy", "g","wow"]
#
# lenList = []
#
# for item in wordList:
#     if len(item) >= 2 and item[0] == item[-1]:
#         print(item)

# # Excercise 3
# password = "password"
#
# count = 3
#
# while count > 0:
#     question = input("Type the correct password to access the terminal, you have 3 attempts :")
#     if question == password:
#         print("Access to terminal granted")
#     elif question != password and count > 1:
#         print("Try again")
#         count -= 1
#     else:
#         print("You lost,access to terminal denied")
#         break