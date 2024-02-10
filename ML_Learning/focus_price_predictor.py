import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from scipy import stats
import datetime
import numpy as np
from sklearn.metrics import r2_score

#asssign instance of Standard Scaler to variable
scaler = StandardScaler()
#load dataset csv to pandas data frame 
#df= data frame
df = pd.read_csv("ML_Learning/focus.csv")

#transform data (year) to (age)
current_year = datetime.datetime.now().year
df['year'] = current_year - df['year']
df.rename(columns={'year': 'age'}, inplace = True)
#visualise data
age = df[['age']]
mileage = df[['mileage']]
price = df[['price']]
#functions for showing scatter charts
def show_age_price_scatter(age, price):
    plt.scatter(age, price)
    plt.show()

def show_mileage_price_scatter(mileage,price):
    plt.scatter(mileage, price)
    plt.show()

#scale values for multiple regression
X = df[['age', 'mileage']]
X.columns = ['age', 'mileage']
y = df[['price']]
y.columns = ['price']

scaledX = scaler.fit_transform(X)

# Create a linear regression model for multiple regression.
regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

#function to convert km to miles
def km_to_miles(km):
    miles = km * 0.621371
    return miles

#menu
while True:
    print('''
    1. Show Scatter graph age - price
    2. Show Scatter graph mileage - price
    3. Show linear coeficients
    4. Show polynominal coeficients
    5. Predict price based on mileage and age
    6. Quit
    ''')
    user_choice = int(input("Which option would you like to select? "))
    match user_choice:
        case 1: 
            show_age_price_scatter(age, price)
        case 2: 
            show_mileage_price_scatter(mileage, price)
        case 3:
            slope, intercept, r, p, std_err = stats.linregress(age['age'], price['price'])
            print(f"The R value for age - price is {r}") #result: -0.7617464424437362
            slope, intercept, r, p, std_err = stats.linregress(mileage['mileage'], price['price'])
            print(f"The R value for mileage - price is {r}") #reult: -0.7416315647759465
            print("*REMEMBER: a value of 0 means there is no corelation. a value of -1 or 1 means there is a 100 percent correlation.")
        case 4:
            mymodel = np.poly1d(np.polyfit(age['age'], price['price'], 2))
            r2_value_price_age = r2_score(price['price'], mymodel(age['age']))
            print("The R squared value for age - price is " + r2_value_price_age) #result: 0.6382572966893817
            mymodel = np.poly1d(np.polyfit(mileage['mileage'], price['price'], 2))
            r2_value_price_mileage = r2_score(price['price'], mymodel(mileage['mileage']))
            print("The R squared value for mileage - price is " + r2_value_price_mileage) #result: 0.5943442368844638
            print("*REMEMBER the R squared value ranges from 0 (no corelation) to 1 (100 percent correlation)")
        case 5:
            #user inputs values for price prediction
            user_car_age = int(input("How old is your Ford Focus in years? "))
            km_or_miles = input("Do you know the mileage in kilometres (km) or miles (m)? ").lower()
            #converts user input in km to miles for prediction
            match km_or_miles:
                case 'km':
                    km = int(input("How many kilometres are on the clock? "))
                    user_car_mileage = km_to_miles(km)
                case 'm':
                    user_car_mileage = int(input("How many miles are on the clock? "))

            user_input = np.array([[user_car_age, user_car_mileage]])

            scaled = scaler.transform(user_input)
            user_prediction = regr.predict(scaled)
            rounded_prediction = round(user_prediction[0][0], 2)
            result_string = f"Your car is worth £{rounded_prediction}"
            print(result_string)
        case 6:
            print("Goodbye!")
            break