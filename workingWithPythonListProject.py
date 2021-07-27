names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
#append name and cost
names.append("Priscilla")
insurance_costs.append(8320.0)
#combine names and insurance_costs to be paired
medical_records= list(zip(insurance_costs, names))
print(medical_records)

#num of medical records we have
num_medical_records= len(medical_records)
print("There are ", num_medical_records, "medical records.")
#selecting first medical record
first_medical_record= medical_records[0]
print("Here is the first medical record: ", first_medical_record)

#sorting lists
medical_records.sort()
print("Here are the medical records sorted by insurance cost: ", str(medical_records))

#cheapest medical_records
cheapest_three= medical_records[:3]
print("Here are the three cheapest insurance costs in our medical records: ", str(cheapest_three))

#most expensive medical records
priciest_three=medical_records[-3:]
print("Here are the three most expensive insurance costs in our medical records: ", str(priciest_three))

#counting elements in a list
occurrences_paul= names.count("Paul")
print("There are ",str(occurrences_paul), "individuals with the name Paul in our medical records.")

#sort the medical records alphabetically by name
new_list= list(zip(names, insurance_costs))
new_list.sort()
print("The new list is in this order: ", str(new_list))

#select medical records from index [3] to [7]
middle_five_records= new_list[3:8]
print("The middle five records are: ", middle_five_records)