# AI-enhanced Code Reparation and Performances 
Web App which uses the [Codex model series](https://beta.openai.com/docs/engines/codex-series-private-beta) 
to automatically find bugs on your code.

# Dependencies
- python (tested with python3.10)
- pip (tested with 21.2)
- `pip install dash`
- `pip install dash-bootstrap-components`
- `pip install dash_ace`
- `pip install openai`

# Build and Test
1. Create the file `api_key.txt` in the root directory of this project and put your OpenAI API key from 
   [https://beta.openai.com/account/api-keys](https://beta.openai.com/account/api-keys).
2. Execute `python web_app.py` to run the web app on `localhost:8050`

# Use the application
1. Paste the code to be checked in the "Original Code" textbox
2. Optionally, select the desired style in the "Message style" dropdown
3. Press the "Check code" button to analyze the code
4. Select the issues to fix in the resulting list
5. Press the "Fix Code" button: the fixed code will appear in the "Fixed Code" textbox
6. Press the "Use as Original Code" button to copy the fixed code from "Fixed Code" to the "Original Code" textbox
7. Repeat from 1.

# Code samples
The following code samples have been tested during our demo:

## Base Example
```python
import Random
a = random.randint(1,12)
b = random.randint(1,12)
for i in range(10):
    question = "What is "+a+" x "+b+"? "
    answer = input(question)
    if answer = a*b
        print (Well done!)
    else:
        print("No.")
```

Found errors (Technical):
* import Random (should be import random)
* a = random.randint(1,12) (should be str(a))
* b = random.randint(1,12) (should be str(b))
* if answer = a*b (should be ==)
* print (Well done!) (should be "Well done!")

Found errors (Friendly):
* random is not imported
* a and b are not strings, so they cannot be concatenated with other strings
* the if statement should use == instead of =

## Arrays
```python
# initialize an empty array
lambda_methods = []
# implement a for loop to count from 0 to 9
for i in 10:
    # append the lambda function to the array defined above
    lambdamethods.push(lambda x: x + i)
```

Found errors (Friendly):
* lambdamethods is not defined
* push() is not a method of an array
* i should be range(10)

## SQL Injection
```python
import mysql.connector
db = mysql.connector.connect(host="localhost", user="newuser", passwd="pass", db="sample")
cur = db.cursor()
name = raw_input('Enter Name: ')
cur.execute("SELECT * FROM userdata WHERE Name = '%s';" % name) for row in cur.fetchall(): print(row)
db.close()
```

Found errors (Friendly):
* The query is vulnerable to SQL injection
* The code does not check if the user exists in the database before printing it out
* The code does not check if the database connection is successful
* The code does not close the cursor after use