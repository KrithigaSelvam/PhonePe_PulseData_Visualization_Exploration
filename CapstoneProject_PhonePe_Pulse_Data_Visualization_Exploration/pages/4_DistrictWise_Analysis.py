import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px
from plotly.colors import n_colors


##  Establish MySQL Connection Thread
mydb = mysql.connector.connect( host="localhost", user="root", password="",database="project_phonepe")
mycursor = mydb.cursor(buffered=True)

st.set_page_config(layout="wide")

mappings={1:'Q1', 2: 'Q2', 3: 'Q3', 4: 'Q4',}

#*************************  Title for the Page    *******************************************

st.title("District Level - Analysis")
st.write("Phonepe has provided District Level data for 723 districts as follows")
st.write("Transaction count for each quarter from 2018 to 2023")
st.write("Transaction amount for each quarter from 2018 to 2023")
st.write("Total number of registered users at the end of each quarter from 2018 to 2023")
st.write("Number of times app was opened from 2nd quarter of 2019 to 2023")
st.write("")
st.write("")
st.write("##### Following visuals are based on the above data provided")
st.write("")
st.write("")

#*************************  State, Year, Quarter wise Bar Chart & Pie Chart *******************************************

col1, col2, col3 = st.columns(3)

with col1:
   option1_1=st.selectbox("Choose a State",
                        ['Andaman & Nicobar','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh',
                         'Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana',
                         'Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh',
                         'Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland',
                         'Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura',
                         'Uttarakhand','Uttar Pradesh','West Bengal'],
                        placeholder='Andaman & Nicobar')

with col2:
   option1_2=st.selectbox("Choose a Year",
                        ['2018','2019','2020','2021','2022','2023'],
                        placeholder='2023')

with col3:
   option1_3=int(st.selectbox("Choose a Quarter",
                        ['1','2','3','4'],
                        placeholder='1'))

input1=[option1_1,option1_2,option1_3]
st.write("#### Data Visuals for all Districts of ",option1_1,"- Year ",option1_2,"Quarter ",option1_3)

query1 = '''select State,Year,Quarter,District,Transaction_Count
            from project_phonepe.map_transaction 
            where State = %s and Year = %s and Quarter = %s
            order by Transaction_Count
            '''
mycursor.execute(query1,input1)
mydb.commit()
out=mycursor.fetchall()
df1=pd.DataFrame(out,columns=["State","Year","Quarter","District","Number of Transactions"])
fig1 = px.bar(df1,x="District", y="Number of Transactions")
fig1.update_traces(marker_color="#008000")

st.write("###### Bar Chart representing Number of Transactions for each district")
st.plotly_chart(fig1, use_container_width=True, sharing="streamlit", theme="streamlit")


query2 = '''select State,Year,Quarter,District,Transaction_Amount
            from project_phonepe.map_transaction 
            where State = %s and Year = %s and Quarter = %s
            order by Transaction_Amount
            '''
mycursor.execute(query2,input1)
mydb.commit()
out=mycursor.fetchall()
df2=pd.DataFrame(out,columns=["State","Year","Quarter","District","Amount of Transaction in Rs."])
fig2 = px.bar(df2,x="District", y="Amount of Transaction in Rs.")
fig2.update_traces(marker_color="#0000cc")

st.write("###### Bar Chart representing Amount of Transaction for each district")
st.plotly_chart(fig2, use_container_width=True, sharing="streamlit", theme="streamlit")



query3 = '''select State,Year,Quarter,District,Registered_Users
            from project_phonepe.map_users 
            where State = %s and Year = %s and Quarter = %s
            order by Registered_Users
            '''
mycursor.execute(query3,input1)
mydb.commit()
out=mycursor.fetchall()
df3=pd.DataFrame(out,columns=["State","Year","Quarter","District","Number of Registered Users"])
fig3 = px.bar(df3,x="District", y="Number of Registered Users")
fig3.update_traces(marker_color="#cc0044")

st.write("###### Bar Chart representing Number of Registered Users for each district")
st.plotly_chart(fig3, use_container_width=True, sharing="streamlit", theme="streamlit")



query4 = '''select State,Year,Quarter,District,App_Opens
            from project_phonepe.map_users 
            where State = %s and Year = %s and Quarter = %s
            order by App_Opens
            '''
mycursor.execute(query4,input1)
mydb.commit()
out=mycursor.fetchall()
if (int(option1_2)>2019) or (int(option1_3)==2019 and int(option1_3)>1):
   df4=pd.DataFrame(out,columns=["State","Year","Quarter","District","Number of Times App Opened"])
   fig4 = px.bar(df4,x="District", y="Number of Times App Opened")
   fig4.update_traces(marker_color="#804000")

   st.write("###### Bar Chart representing Number of Times App Opened for each district")
   st.plotly_chart(fig4, use_container_width=True, sharing="streamlit", theme="streamlit")
else:
   st.warning("App Opened Data not available for this quarter")


#****************************  Trend Lines for Districts in each state *********************************
st.write("")
st.write("#### Data Visuals for all Districts of a State")
option2=st.selectbox("Choose the State",
                        ['Andaman & Nicobar','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh',
                         'Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana',
                         'Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh',
                         'Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland',
                         'Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura',
                         'Uttarakhand','Uttar Pradesh','West Bengal'],
                        placeholder='Andaman & Nicobar')

input2=[option2]
query5 = '''select Year,District,sum(Transaction_Count)
            from project_phonepe.map_transaction 
            where State = %s
            group by Year,District
            order by Year
            '''
mycursor.execute(query5,input2)
mydb.commit()
out=mycursor.fetchall()
df5=pd.DataFrame(out,columns=["Year","District","Total Number of Transactions"])

fig5 = px.line(df5,x="Year", y="Total Number of Transactions", color="District")
st.write('###### District Trends Based on Number of Transactions')
st.plotly_chart(fig5, use_container_width=True, sharing="streamlit", theme="streamlit")



query6 = '''select Year,District,sum(Transaction_Amount)
            from project_phonepe.map_transaction 
            where State = %s
            group by Year,District
            order by Year
            '''
mycursor.execute(query6,input2)
mydb.commit()
out=mycursor.fetchall()
df6=pd.DataFrame(out,columns=["Year","District","Total Amount of Transactions in Rs."])

fig6 = px.line(df6,x="Year", y="Total Amount of Transactions in Rs.", color="District")
st.write('###### District Trends Based on Total Amount of Transactions')
st.plotly_chart(fig6, use_container_width=True, sharing="streamlit", theme="streamlit")



query7 = '''select Year,District,Registered_Users
            from project_phonepe.map_users 
            where State = %s and Quarter = '4'
            order by Year
            '''
mycursor.execute(query7,input2)
mydb.commit()
out=mycursor.fetchall()
df7=pd.DataFrame(out,columns=["Year","District","Number of Registered Users"])

fig7 = px.line(df7,x="Year", y="Number of Registered Users", color="District")
st.write('###### District Trends Based on Number of Registered Users')
st.plotly_chart(fig7, use_container_width=True, sharing="streamlit", theme="streamlit")

###############################
#***************** Key Insights **************************************
st.header("Key Insights")
st.write('''Though the charts show a great disparity in transactions and users between districts,
         it is only relative''')
st.write('''The general trend is that both transactions and registered users have been growing 
         year-on-year in almost all districts''')
st.write('''Interesting, Tier2 and Tier3 cities show a very steady increase in growth compared to large/metro
         cities which show higher fluctuations over the years''')
st.write('''In conclusion - the digital payments growth of UPI is all inclusive and is not concentrated
         in a few large states/districts''')
