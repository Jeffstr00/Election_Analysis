counties = ["Arapahoe", "Denver", "Jefferson"]
#for county in counties:
    #print(county)
counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters":422829},
                {"county":"Denver", "registered_voters":463353},
                {"county":"Jefferson", "registered_voters":432438}]

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")
