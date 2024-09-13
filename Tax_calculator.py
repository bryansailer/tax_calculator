from deductions import new_deductions

def total_income(yearly_salary, yearly_pension, yearly_disability, contribution):
    yearly_taxable_income: float = yearly_salary + yearly_pension
    
    if yearly_taxable_income < 23200:
        tax_rate = 10
    elif yearly_taxable_income < 94300:
        tax_rate = 12
    elif yearly_taxable_income < 201050:
        tax_rate = 22
    elif yearly_taxable_income < 383900:
        tax_rate = 24
    elif yearly_taxable_income < 487450:
        tax_rate = 32
    elif yearly_taxable_income < 731200:
        tax_rate = 35
    else:
        tax_rate = 37

    yearly_fed_taxes = yearly_taxable_income * (tax_rate / 100)
    yearly_state_taxes = yearly_salary * 0.0315
    yearly_local_taxes = yearly_salary * 0.0125
    yearly_SS_Med = yearly_salary * 0.0765
    yearly_401k = yearly_salary * (contribution / 100)
    yearly_deductions = yearly_fed_taxes + yearly_local_taxes + yearly_state_taxes + yearly_SS_Med + yearly_401k
    yearly_net_income: float = yearly_taxable_income - yearly_deductions
    yearly_total_income: float = yearly_net_income + yearly_disability
    
    print(f'Yearly taxable: {yearly_taxable_income:,.2f}')
    print(f'Your tax rate is: {tax_rate}%')
    print(f'Your yearly contribution to 401k: {yearly_401k:,.2f}')
    print(f'Your yearly total income: {yearly_total_income:,.2f}')
        
def main():
    yearly_salary: float = float(input('Enter yearly salary: '))
    yearly_pension: float = float(input('Enter yearly pension: '))
    yearly_disability: float = float(input('Enter yearly disability: '))
    contribution: float = float(input('What percentage do you contribute to your 401k? (%): '))
    
    
    total_income(yearly_salary, yearly_pension, yearly_disability, contribution)
    new_deductions()

if __name__ == '__main__':
    main()




    
