# name1 = input("Enter Name1 : ")
# name2 = input("Enter Name2 : ")

# ammount_of_consonants_in_name1 = 0
# ammount_of_consonants_in_name2 = 0


# for char in name1:
#     if char in "qzwsxdcrfvtgbyhnjmklp":
#         ammount_of_consonants_in_name1 += 1
# for char in name2:
#     if char in "qzwsxdcrfvtgbyhnjmklp":
#         ammount_of_consonants_in_name2 += 1


# if ammount_of_consonants_in_name1 > ammount_of_consonants_in_name2:
#     print("Ammount Of Consonants In Name 1 Is more Than Name 2 And It Contains {} Consonants.".format(ammount_of_consonants_in_name1))
# elif ammount_of_consonants_in_name1 > ammount_of_consonants_in_name2:
#     print("Ammount Of Consonants In Name 2 Is More Than Name 1 And It Contains {} Consonants.".format(ammount_of_consonants_in_name1))
# else:
#     print("Ammount Of Consonants In Name 1 And Name 2 Match.")



print()
print()


print("<<<<< Welcome, Count Any Letters In Your Sentance >>>>>")
print()
my_sentance = input("Enter Your Sentance : ")

ammount_of_consonants_in_my_sentance = 0
for char in my_sentance:
    if char in "qzwsxdcrfvtgbyhnjmklp":
        ammount_of_consonants_in_my_sentance += 1
print()
print(" The Ammount Of Consonats In Your Sentance is : " + str(ammount_of_consonants_in_my_sentance))
print()




