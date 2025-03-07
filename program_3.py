#Elijah Budd
#3/5/2025
# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data:
    # year, name of state, and population.
    # Store all of this information in a list of lists.  For example it might be stored like this:
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]
    all_entered_values = []

    while True:
        year = int(input("Enter a year: "))
        name_state = input("Enter state name: ")
        population = int(input("Enter a population: "))

        all_entered_values.append([year, name_state, population])

        more_data = input("Do you have more data? (y/n): ")
        if more_data == "y":
            continue
        elif more_data == "n":
            break
        else:
            break

    # Now have the user enter a year.
    find_year = int(input("Enter a year to calculate the total population of that year: "))

    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
    sum_population_for_year(all_entered_values, find_year)

def sum_population_for_year(all_entered_values, year_to_sum):


# Loop through and sum the populations for the appropriate year.
# e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
# or 3,421,988 if they entered 2011 for the year to sum.
    total_population = 0

    for entry in all_entered_values:
        if entry[0] == year_to_sum:
            total_population += entry[2]

# print the totalled population
    print("The total population for that year is", total_population)

# Call the main function.
if __name__ == '__main__':
    main()

TestRun:
Enter a year: 2005
Enter state name: minnesota
Enter a population: 5000
Do you have more data? (y/n): y
Enter a year: 2005
Enter state name: Utah
Enter a population: 3000
Do you have more data? (y/n): y
Enter a year: 2004
Enter state name: California
Enter a population: 10000
Do you have more data? (y/n): n
Enter a year to calculate the total population of that year: 2005
The total population for that year is 8000
