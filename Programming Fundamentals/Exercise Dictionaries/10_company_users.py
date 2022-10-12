company_data_base = {}

while True:
    command = input()
    if command == "End":
        break
    company_name, employee_id = command.split(" -> ")
    if company_name not in company_data_base:
        company_data_base[company_name] = [employee_id]
    if employee_id not in company_data_base[company_name]:
        company_data_base[company_name].append(employee_id)

print(company_data_base)

for all_companies, all_employees in company_data_base.items():
    print(all_companies)
    for current_employee in all_employees:
        print(f"-- {current_employee}")