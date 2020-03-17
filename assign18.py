'''
Care hospital wants to know the medical speciality visited by the maximum number of patients. Assume that the patient id of the patient along with the medical speciality visited by the patient is stored in a list. The details of the medical specialities are stored in a dictionary as follows:
{
"P":"Pediatrics",
"O":"Orthopedics",
"E":"ENT
}

Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.
Also write the pytest test cases to test the program.

Note:
Assume that there is always only one medical speciality which is visited by maximum number of patients.
Perform case sensitive string comparison wherever necessary.

Sample Input	                           Expected Output
[101,P,102,O,302,P,305,P]	                  Pediatrics
[101,O,102,O,302,P,305,E,401,O,656,O]	      Orthopedics
[101,O,102,E,302,P,305,P,401,E,656,O,987,E] 	ENT

'''
#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    count_p = 0
    count_E = 0
    count_o = 0
    for i in patient_medical_speciality_list:
        if i=='P':
            count_p = count_p + 1
        elif i=='O':
            count_o = count_o + 1
        elif i=='E':
            count_E = count_E + 1
    if count_E>count_o and count_E>count_p:
        speciality = medical_speciality["E"]
    elif count_p>count_o and count_p>count_E:
        speciality = medical_speciality["P"]
    else:
        speciality = medical_speciality["O"]
    # write your logic here

    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)