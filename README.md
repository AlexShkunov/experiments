# Data experiments
Collection of applications for different platforms

## Data
#### deliveryData_2.csv
Package delivery data. Use for Linear regression, to forecast delivery days based on weight of a package
**Columns**
- date - dd/mm/yyyy - Order date
- weight - Integer - package's weight (kg)
- distance - Integer - delivery distance (km)
- days - Integer - amount of days the package was under delivery

#### personalBudget.csv
Personal budgeting history. Sample use is to forecast coinfidence (binary classification), of whether budgeting targets will be met in the given month
**Columns**
- period - mm/yyyy - Budgeting period
- month_num - Integer - Numeric representation of the month
- take_home_pay - Float - After-tax pay
- necessities - Float - percentage of the income spent on rent & bills
- flexible - Float - percentage of the income spent on discretionary (e.g ice cream)
- savings - Float - percentage of the income spent on saving goals (loan-extra-payment, investements)
- debt_load - Float - coeficient describing total relative (to annual income) debt-amount
- extra_flex - Boolean - Extra flexible spendings (e.g. travel)

## Apps

