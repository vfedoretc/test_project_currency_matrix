# Currency trading
____

Imagine EUR 1.00 in European currency buys USD 1.10 of U.S. currency, and USD 1.00 of U.S. currency buys CNY 6.00 of Chinese currency, and CNY 1.00 of Chinese currency buys EUR 0.16 of European currency. 
Therefore, a profitable risk-free trading strategy would be the following:
take EUR 1.00 and purchase USD 1.10, then
take USD 1.10 and purchase CNY 6.60 (1.10*6.00), then
take CNY 6.60 and purchase EUR1.056 (6.60*0.16)
Therefore, the strategy started with EUR 1.00 and ended with EUR 1.056, generating 5.60% risk-free profit: 1 x 1.1 x 6 x 0.16 = 1.056
The task is to determine whether any sequence of currency exchanges can yield a risk-free profit starting and ending with the same currency as per the example above.


## Input
Matrix of n currency exchange rates similar to:
| | EUR |  USD | CNY | THB |
|:---------:|:---------:|:---------:|:---------:|:---------:|
| EUR | 1.00 | 1.10 | 6.50 | 70.00 |
| USD | 0.90 | 1.00 | 6.00 | 65.00 |
| CNY | 0.16 | 0.17 | 0.14 |10.75|
| THB | 0.01 | 0.02 | 0.08 |1.00|

```
>>> python main.py <name_file>.csv
```
./currency_matrix_1.csv
```
,EUR,USD,CNY,THB
EUR,1.00,1.10,6.50,70.00
USD,0.90,1.00,6.00,65.00
CNY,0.16,0.17,1.00,10.75
THB,0.01,0.02,0.08,1.00
```

Thus the first row and the first column of the table represent the names of the currencies. The corresponding intersections represent the conversion rates between the two currencies.
Each table consists of n+1 rows and n+1 columns in the input file.

## Output
The algorithm  determine whether a sequence of exchanges exists that yields a profit greater than 1.00%. If there is more than one sequence yielding a profit of more than 1.00%, the algorithm needs to print the shortest sequence.

Input
```
.>>> python main.py currency_matrix_1.csv
```
Output
```
USD, THB, USD
```