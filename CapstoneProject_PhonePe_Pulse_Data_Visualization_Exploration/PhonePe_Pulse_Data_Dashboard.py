import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px
from plotly.colors import n_colors
#import plotly.graph_objs as go
#from plotly.offline import iplot, init_notebook_mode


#       STREAMLIT THEME
#[theme]
primaryColor="#4b58ff"
backgroundColor="#eccd98"
secondaryBackgroundColor="#e8cef3"
textColor="#6d058c"


st.set_page_config(layout="wide")

##  Establish MySQL Connection Thread
mydb = mysql.connector.connect( host="localhost", user="root", password="",database="project_phonepe")
mycursor = mydb.cursor(buffered=True)

mappings={1:'Q1', 2: 'Q2', 3: 'Q3', 4: 'Q4'}

st.image('phonepe_new1.png')

st.header("Introduction")
st.write(r"As of March 2024, India accounts for 46% of all the digital payments in the world.")
st.write(r"UPI Transactions account for 80% of all digital payments in India")
st.write(r"PhonePe, essentially an UPI app, accounts for 48% of UPI market share")
st.write('''PhonePe Pulse - Provides the data for the past 6 years PhonePe UPI app transactions, which helps us 
         in analysing the digital payments trend in India''')



#****************   Overall Transactions Trend Line
query1 = '''select Year,sum(Transaction_Count), sum(Transaction_Amount)
            from project_phonepe.aggregate_transaction 
            group by Year
            '''

mycursor.execute(query1)
mydb.commit()
out=mycursor.fetchall()
df1=pd.DataFrame(out,columns=["Year","Number of Transactions","Amount of Transaction in Rs."])

st.header(' INDIA - Digital Transactions Analysis')

col1,col2=st.columns(2)
with col1:
   fig1_1 = px.line(df1,x="Year", y="Number of Transactions")
   st.write('###### Trend Based on Transaction Volume')
   st.plotly_chart(fig1_1, use_container_width=True, sharing="streamlit", theme="streamlit")
with col2:
   fig1_2 = px.line(df1,x="Year", y="Amount of Transaction in Rs.")
   st.write('###### Trend Based on Amount of Transaction(in Rs.)')
   st.plotly_chart(fig1_2, use_container_width=True, sharing="streamlit", theme="streamlit")

#**********************  Transaction Data Maps ***************************************************

color_palette=["#E3FF33","#FFF633","#FFE333","#FFD133","#FFB833","#FFA833","#FF9933","#FF8A33","#FF7433",
 "#FF6433","#FF4233","#FF3349","#FF3355","#FF3361","#FF3371","#FF337A","#FF3386",
 "#FF3393","#FF339C","#FF33A5","#FF33BE","#FF33CA","#FF33D4","#FF33E0","#FF33E9","#FF33F6",
 "#FF33FF","#F033FF","#DD33FF","#CA33FF","#AF33FF","#9633FF","#8633FF","#7433FF","#5E33FF",
 "#3346FF"]


option2=st.selectbox("Choose a Year to Get Map with State-wise Details",
                        ['2018','2019','2020','2021','2022','2023'],
                        placeholder='2023')

input2=[option2]

query2_1 = '''select State,sum(Transaction_Count), sum(Transaction_Amount)
            from project_phonepe.aggregate_transaction
            where Year = %s
            group by State
            order by sum(Transaction_Count)
            '''

mycursor.execute(query2_1,input2)
mydb.commit()
out=mycursor.fetchall()
df2_1=pd.DataFrame(out,columns=["State","Total Transaction Count","Total Transaction Amount"])

fig2_1 = px.choropleth(
    df2_1,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State',
    color='Total Transaction Count',
    color_discrete_sequence=color_palette
    #color_discrete_sequence= px.colors.sequential.Plasma_r                                        ### works fine
    #color_discrete_sequence=n_colors('rgb(0, 0, 255)', 'rgb(255, 0, 0)', 36, colortype = 'rgb')   ### works fine
)

fig2_1.update_geos(fitbounds="locations", visible=False)
st.write('##### Map - State wise Total Number of Transactions for the Year',option2)
st.plotly_chart(fig2_1, use_container_width=True, sharing="streamlit", theme="streamlit")

query2_2 = '''select State,sum(Transaction_Count), sum(Transaction_Amount)
            from project_phonepe.aggregate_transaction
            where Year = %s
            group by State
            order by sum(Transaction_Amount)
            '''

mycursor.execute(query2_2,input2)
mydb.commit()
out=mycursor.fetchall()
df2_2=pd.DataFrame(out,columns=["State","Total Transaction Count","Total Transaction Amount"])

fig2_2 = px.choropleth(
    df2_2,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State',
    color='Total Transaction Amount',
    #color_discrete_sequence= px.colors.sequential.Plasma                                       ### works fine
    color_discrete_sequence=n_colors('rgb(0, 0, 255)', 'rgb(255, 0, 0)', 36, colortype = 'rgb')   ### works fine
)

fig2_2.update_geos(fitbounds="locations", visible=False)
st.write('##### Map - State wise Total Amount of Transactions(in Rs.) for the Year',option2)
st.plotly_chart(fig2_2, use_container_width=True, sharing="streamlit", theme="streamlit")

query2_3 = '''select State,(sum(Transaction_Amount)/sum(Transaction_Count)) as Average_Transaction
            from project_phonepe.aggregate_transaction
            where Year = %s
            group by State
            order by Average_Transaction
            '''

mycursor.execute(query2_3,input2)
mydb.commit()
out=mycursor.fetchall()
df2_3=pd.DataFrame(out,columns=["State","Average Amount per Transaction"])

fig2_3 = px.choropleth(
    df2_3,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State',
    color='Average Amount per Transaction',
    #color_discrete_sequence= px.colors.sequential.Plasma                                       ### works fine
    color_discrete_sequence=n_colors('rgb(0, 0, 255)', 'rgb(255, 0, 0)', 36, colortype = 'rgb')   ### works fine
)

fig2_3.update_geos(fitbounds="locations", visible=False)
st.write('##### Map - State wise Average Amount per Transactions(in Rs.) for the Year',option2)
st.plotly_chart(fig2_3, use_container_width=True, sharing="streamlit", theme="streamlit")


#***************** Sunburst Charts - Overall Transaction *****************************************

query3 = '''select Year, Quarter, sum(Transaction_Count), sum(Transaction_Amount)
            from project_phonepe.aggregate_transaction 
            group by Year,Quarter
            '''

mycursor.execute(query3)
mydb.commit()
out=mycursor.fetchall()
df3=pd.DataFrame(out,columns=["Year","Quarter","Total Transaction Count","Total Transaction Amount in Rs."])
#st.write(df)
df3['Quarter']=df3['Quarter'].replace(mappings)

fig3_1 = px.sunburst(df3,path=[ 'Year', 'Quarter','Total Transaction Count'], values='Total Transaction Count')
fig3_2 = px.sunburst(df3,path=[ 'Year', 'Quarter','Total Transaction Amount in Rs.'], 
                     values='Total Transaction Amount in Rs.')

col1,col2=st.columns(2)

with col1:
    st.write('##### Spread of Transaction Volume')
    st.plotly_chart(fig3_1, use_container_width=True, sharing="streamlit", theme="streamlit")

with col2:
    st.write('##### Spread of Amount of Transaction in Rs.')
    st.plotly_chart(fig3_2, use_container_width=True, sharing="streamlit", theme="streamlit")

#****************************************************************************************************************
#***************** Key Insights **************************************
st.header("Key Insights")
st.write('''India has been showing a sudden increase in digital transactions in the past 5 years - 
         which can be seen by the sharp increase in the trend line curve''')
st.write('''Be it Transaction Volume/Amount, the payments made in a single quarter in 2023 
         exceed the total values of transaction volume/Amount for the entire year before 2020 - 
         which can be observed from the above sunburst charts''')
st.write('''Larger/Well-Developed states account for more transactions compared to 
         smaller/under-developed states - The Maps above clearly depict this phenomenon
         with larger states occupying the colours at the end of the spectrum for higher values''')
st.write('''Interestingly - the average amount per transaction reveals a reverse trend - which 
         shows in smaller states the per transaction amount is higher and there might be large number
         of small amount transfers in larger states''')
st.write("Government promotion of Digital Payments and UPI has yielded tremendous results all over India")









   






