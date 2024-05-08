import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px
import plotly.graph_objects as go
from plotly.colors import n_colors


##  Establish MySQL Connection Thread
mydb = mysql.connector.connect( host="localhost", user="root", password="",database="project_phonepe")
mycursor = mydb.cursor(buffered=True)

st.set_page_config(layout="wide")

st.title("Registered User-Mobile Brand - Analysis")

st.write("PhonePe Pulse provides the number of registered users of their app at the end of each quarter")
st.write("It also provides Mobile Brand-wise split up of its Registered Users till Q1 of 2022")
st.write("There is also a partially provided data for the number of times their UPI app was opened by users")

#****************   Overall Users Trend Line
query1 = '''select Year,Quarter,sum(Registered_Users)
            from project_phonepe.aggregate_users
            group by Year,Quarter
            order by Year,Quarter
            '''

mycursor.execute(query1)
mydb.commit()
out=mycursor.fetchall()
df1=pd.DataFrame(out,columns=["Year","Quarter","Number of Registered Users"])
#df1['Quarter']=df1['Quarter'].replace(mappings)
df1['Year_new']=df1['Year']-1
df1['Year-Quarter']=df1['Year_new']+(df1['Quarter']/4)

fig1 = px.line(df1,x="Year-Quarter", y="Number of Registered Users")
st.write('## INDIA - Digital Transactions - User Analysis')
st.write('###### Trend Based on Number of Registered Users')
st.plotly_chart(fig1, use_container_width=True, sharing="streamlit", theme="streamlit")

#**********************  User Data Maps ***************************************************

color_palette=["#E3FF33","#FFF633","#FFE333","#FFD133","#FFB833","#FFA833","#FF9933","#FF8A33","#FF7433",
 "#FF6433","#FF4233","#FF3349","#FF3355","#FF3361","#FF3371","#FF337A","#FF3386",
 "#FF3393","#FF339C","#FF33A5","#FF33BE","#FF33CA","#FF33D4","#FF33E0","#FF33E9","#FF33F6",
 "#FF33FF","#F033FF","#DD33FF","#CA33FF","#AF33FF","#9633FF","#8633FF","#7433FF","#5E33FF",
 "#3346FF"]


option2=st.selectbox("Choose a Year to Get Map with State-wise Details",
                        ['2018','2019','2020','2021','2022','2023'],
                        placeholder='2023')

input2=[option2,'4']

query2 = '''select State,Year,Registered_Users
            from project_phonepe.aggregate_users
            where Year=%s and Quarter=%s
            '''

mycursor.execute(query2,input2)
mydb.commit()
out=mycursor.fetchall()
df2=pd.DataFrame(out,columns=["State","Year","Number of Registered Users"])

fig2 = px.choropleth(
    df2,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State',
    color='Number of Registered Users',
    #color_discrete_sequence=color_palette
    #color_discrete_sequence= px.colors.sequential.Plasma                                     ### works fine
    #color_discrete_sequence=n_colors('rgb(0, 0, 255)', 'rgb(255, 0, 0)', 36, colortype = 'rgb')# works fine
)

fig2.update_geos(fitbounds="locations", visible=False)
st.write('##### Map - State wise Number of Registered Users for the Year',option2)
st.plotly_chart(fig2, use_container_width=True, sharing="streamlit", theme=None)


#*************************  State, Year, Quarter wise Pie Chart *******************************************
st.write("#### Brand-wise Split up of Registered Users")
col1, col2, col3 = st.columns(3)

with col1:
   option4_1=st.selectbox("Choose a State",
                  ['Andaman & Nicobar','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh',
                   'Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana',
                   'Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh',
                   'Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland',
                   'Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura',
                   'Uttarakhand','Uttar Pradesh','West Bengal'],
                  placeholder='Andaman & Nicobar')

with col2:
   option4_2=st.selectbox("Choose a Year",
                        ['2018','2019','2020','2021','2022'],
                        placeholder='2022')

with col3:
   option4_3=int(st.selectbox("Choose a Quarter",
                        ['1','2','3','4'],
                        placeholder='1'))

input4=[option4_1,option4_2,option4_3]


query4 = '''select State,Year,Quarter,Brand_Name,Brand_User_Count
            from project_phonepe.aggregate_brand_users
            where State=%s and Year=%s and Quarter=%s
            '''

mycursor.execute(query4,input4)
mydb.commit()
out=mycursor.fetchall()
if len(out)==0:
   st.warning("Brand-wise User Data Not available for entire Year 2023 and Q2,Q3,Q4 of Year 2022")
else:
   df4=pd.DataFrame(out,columns=["State","Year","Quarter","Brand_Name","Brand_User_Count"])
   
   fig4_x=list(df4["Brand_Name"])
   fig4_y=list(pd.to_numeric(df4["Brand_User_Count"]))
   fig4 = px.pie(values=fig4_y, names=fig4_x)
   st.write("###### Pie Chart for ",option4_1,"- Year ",option4_2,"Quarter ",option4_3)
   st.plotly_chart(fig4, use_container_width=True, sharing="streamlit", theme="streamlit")


#****************   State-Level Users Trend Line

option5=st.selectbox("Choose State For Trend Lines",
                  ['Andaman & Nicobar','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh',
                  'Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana',
                  'Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh',
                  'Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland',
                  'Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura',
                  'Uttarakhand','Uttar Pradesh','West Bengal'],
                  placeholder='Andaman & Nicobar')

input5=[option5]
query5_1 = '''select Year,Quarter,Registered_Users
            from project_phonepe.aggregate_users
            where State=%s
            order by Year,Quarter
            '''

mycursor.execute(query5_1,input5)
mydb.commit()
out=mycursor.fetchall()
df5_1=pd.DataFrame(out,columns=["Year","Quarter","Number of Registered Users"])
#df1['Quarter']=df1['Quarter'].replace(mappings)
df5_1['Year_new']=df5_1['Year']-1
df5_1['Year-Quarter']=df5_1['Year_new']+(df5_1['Quarter']/4)

fig5_1 = px.line(df5_1,x="Year-Quarter", y="Number of Registered Users")
#st.write('###### Trend Line Based on Total Number of Registered Users for ',option5)
#st.plotly_chart(fig5_1, use_container_width=True, sharing="streamlit", theme="streamlit")

#           Each State brand-wise trend lines
query5_2 = '''select Year,Quarter,Brand_Name,Brand_User_Count
            from project_phonepe.aggregate_brand_users
            where State=%s
            order by Year,Quarter
            '''

mycursor.execute(query5_2,input5)
mydb.commit()
out=mycursor.fetchall()
df5_2=pd.DataFrame(out,columns=["Year","Quarter","Brand Name","Brand User Count"])
df5_2['Year_new']=df5_2['Year']-1
df5_2['Year-Quarter']=df5_2['Year_new']+(df5_2['Quarter']/4)

st.write('###### Trend Line Based on Number of Brand-wise Registered Users for ',option5)
fig5_2 = px.line(df5_2,x="Year-Quarter", y="Brand User Count", color="Brand Name")
st.plotly_chart(fig5_2, use_container_width=True, sharing="streamlit", theme="streamlit")

#           State Registered Users and AppOpens bar chart
query5_31 = '''select Year,Registered_Users
            from project_phonepe.aggregate_users
            where State=%s and Quarter=4 and Year>2018
            order by Year
            '''

mycursor.execute(query5_31,input5)
mydb.commit()
out=mycursor.fetchall()
df5_31=pd.DataFrame(out,columns=["Year","Registered Users"])

query5_32 = '''select Year,sum(App_Opens)
            from project_phonepe.aggregate_users
            where State=%s and Year>2018
            group by Year
            order by Year
            '''

mycursor.execute(query5_32,input5)
mydb.commit()
out=mycursor.fetchall()
df5_32=pd.DataFrame(out,columns=["Year","App Opens"])

fig5_31= px.bar(df5_31,x="Year",y="Registered Users")
fig5_32=px.line(df5_32,x="Year",y="App Opens")

col1,col2=st.columns(2)

with col1:
   st.write('###### Number of Total Registered Users for ',option5)
   st.plotly_chart(fig5_31, use_container_width=True, sharing="streamlit", theme="streamlit")
with col2:
   st.write('###### Number of Times App Opened for ',option5)
   st.plotly_chart(fig5_32, use_container_width=True, sharing="streamlit", theme="streamlit")
   #st.write('Note: App opened data not available for 1st quarter in 2019')



#***************** Key Insights **************************************
st.header("Key Insights")
st.write('''Unlike the Steep increase in Transactions - the user numbers have been increasing steadily
          year-on-year''')
st.write('''The Bar chart reveals that User Registration has been increasing steadily both country-wise 
         and each state-wise''')
st.write('''Except for Lenovo - which discontinued smart phones production, and Huawei - which faces US 
         sanctions due to security reasons, All other Mobile Phone Brands show the same trend of 
         steady increase in the number of Registered Users over the past 6 years''')
st.write('''While registration is increasing arithmetically, the usage of the app is increasing
         exponentially for most states as witnessed by the trend line of App Opened for each state''')

