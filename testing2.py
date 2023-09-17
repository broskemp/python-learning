# assignment 1
# -create a tuple named patient with first_name, last_name, age and the symptoms
# -print the tuple
# -write a python function that takes a tuple of patient information as an argument
# and returns a formatted string with the following information
# ("Name: Timo Virtanen, Age: 60, Symptoms: Flu")
# -use the function to print your information from the "patient" tuple.

patient = ("Timo","Virtanen",60,"Flu")
print(patient)

def format_patient_info(patient_info):
    first_name, last_name, age, symptoms = patient_info
    formatted_info = f"Name: {first_name} {last_name}, Age: {age}, Symptoms: {symptoms}"
    return formatted_info

patient_info_string = format_patient_info(patient)
print(patient_info_string)

# Create an empty list named "patient"
# append at least five different patient names to the list
# print the first three items (details) in the "patient" list
# write a function to check whether the patient is in the list
patient = []
patient.append(("Timo","Virtanen","60","Flu"))
patient.append(("Ramon","Vanker","21","Healthy"))
patient.append(("Jari","Paakkanen","72","Covid"))
patient.append(("Michael","Jackson","50","Dead"))
patient.append(("Lia","Jaakari","25","Healthy"))

print("First three patient details:")
for i, patient_details in enumerate(patient[:3], start=1):
    print(f"Patient {i}: {patient_details}")


