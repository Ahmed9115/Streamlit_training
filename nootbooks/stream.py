# %%
import os
import streamlit as st
import pandas as pd
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 



# %%
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "Ice Cream Sales - temperatures.csv")
data = pd.read_csv(csv_path)
 
# %%
data.isna().sum()

# %%
sns.scatterplot(data['Ice Cream Profits'])

# %%
y = data['Ice Cream Profits']
x = data.drop('Ice Cream Profits' , axis = 1)

# %%
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3 , random_state=42)

# %%
lin =LinearRegression()
lin.fit(x_train,y_train)


st.header("YOUR ICE_CREAM PRICE PREDICTOR")

temprature = st.number_input("TODAY'S TEMPRATURE IN CELCIES" , value = None , placeholder= 'type a number....' , min_value=29 )

calculate = st.button("PREDICT !")

if calculate and temprature:
 price = lin.predict([[temprature]])
 st.write("the ICE_CREAM price will be: $" , price)
 if temprature >=100 :
    st.write("GO TO ANTARCTICA ❄🧊⛸")

elif calculate and  not temprature :
 
 st.write("you didn't type a number 💀")



