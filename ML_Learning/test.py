category_mappings = {
    'Gender': {'M': 0, 'F': 1},
    'Married': {'Y': 1, 'N': 0},
    'Job': {'Y': 1, 'N': 0}
}

client_age = int(input("How old is the client? "))
client_gender = input("Is the client male(m) or female (f)? ").lower()
client_salary = int(input("How much does the client earn each month (in $)? "))
client_job = input("Is the client currently employed (y / n)? ").lower()
client_married = input("Is the client currently married (y/n)? ").lower()
client_children = int(input("How many children does the client have? "))

# Make a decision
client_data = [[client_age, category_mappings['Gender'].get(client_gender, 0), client_salary,
                category_mappings['Job'].get(client_job, 0),
            category_mappings['Married'].get(client_married, 0), client_children]]
print(client_data)