citylist = ["Miami", "Weston", "Ft Lauderdale", "Sunrise"]

removecity = "Weston1"
if removecity in citylist:
    citylist.remove(removecity)
else:
    print(f"{removecity} is not found in the list.")


print(citylist)


