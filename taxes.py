
myAnuallySalary = input("Annually Salary: ")

TaxBracket1 = 11265 * 0.00
TaxBracket2 = (13173 - 11266) * 0.08
TaxBracket3 = (15009 - 13137) * 0.09
TaxBracket4 = (16881 - 15009) * 0.10
TaxBracket5 = (18753 - 16881) * 0.11
TaxBracket6 = (20625 - 18753) * 0.12
TaxBracket7 = (22569 - 20625) * 0.14
TaxBracket8 = (24513 - 22569) * 0.16
TaxBracket9 = (26457 - 24513) * 0.18
TaxBracket10 = (28401 - 26457) * 0.20
TaxBracket11 = (30345 - 28401) * 0.22

myAnnullyTax = TaxBracket1 + TaxBracket2 + TaxBracket3 + TaxBracket4 + TaxBracket5 + TaxBracket6 + TaxBracket7 + TaxBracket8 + TaxBracket9 + TaxBracket10 + TaxBracket11
myMonthlyIncome = (float(myAnuallySalary) - myAnnullyTax) / 12

print(myMonthlyIncome)
print(myAnnullyTax)