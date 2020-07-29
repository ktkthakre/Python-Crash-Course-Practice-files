#list exercise 3.4

guest = ['dog','cat','horse']
print(f"Please join us to dinner Mr.{guest[0].title()}.")
print(f"Please join us to dinner Mr.{guest[1].title()}.")
print(f"Please join us to dinner Mr.{guest[2].title()}.")

#list exercise 3.5

print(f"\nOh No, Mr.{guest[2].title()} cannot join us for dinner.")
cancled = guest.pop(2)
guest.append('cow')
print(f"So, Mr.{guest[2].title()} will be joining us instead.")
print(f"Atleast Mr.{guest[0].title()} and Mr.{guest[1].title()} will be still with us")

#list exercise 3.6

print("Hey, I just found a bigger table.")
guest.insert(0, 'bird')
guest.insert(4, 'boar')
guest.append('bull')
print("\nHere are the new invites : ")
print(f"\nPlease join us to dinner Mr.{guest[0].title()}.")
print(f"Please join us to dinner Mr.{guest[1].title()}.")
print(f"Please join us to dinner Mr.{guest[2].title()}.")
print(f"Please join us to dinner Mr.{guest[3].title()}.")
print(f"Please join us to dinner Mr.{guest[4].title()}.")
print(f"Please join us to dinner Mr.{guest[5].title()}.")

#displaying number of list using len() method
print(f"{len(guest)} guests will be joining us for dinner.")

#list exercise 3.7

print("\nHoly cow, the bigger table I ordered won't be here in time.\n\tOnly two guests can be adjusted at the dinner.")

print(f"\nSorry Mr.{guest[5].title()}, for letting you down.")
guest.pop()
print(f"\nSorry Mr.{guest[4].title()}, for letting you down.")
guest.pop()
print(f"\nSorry Mr.{guest[3].title()}, for letting you down.")
guest.pop()
print(f"\nSorry Mr.{guest[2].title()}, for letting you down.")
guest.pop()

print(f"Mr.{guest[0].title()} you will still be with us.\nAnd you too Mr.{guest[1].title()}")\

del guest[1]
del guest[0]

print(guest)