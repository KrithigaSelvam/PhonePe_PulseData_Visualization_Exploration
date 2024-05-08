import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px
#import plotly.graph_objs as go
#from plotly.offline import iplot, init_notebook_mode


##  Establish MySQL Connection Thread
mydb = mysql.connector.connect( host="localhost", user="root", password="",database="project_phonepe")
mycursor = mydb.cursor(buffered=True)

st.set_page_config(layout="wide")

mappings={1:'Q1', 2: 'Q2', 3: 'Q3', 4: 'Q4',}
#*************************  Title for the Page    *******************************************

st.title("Transaction Types - Analysis")
st.write("")
st.write("###### There are 4 major types of Money Tranfers/Transactions")
st.write("1. Recharge & Bill Payments  ==> Payments of pre-generated bills")
st.write("2. Peer-to-Peer Payments ==> Money Transfers between individual accounts")
st.write("3. Merchant Payments ==> Payments made towards purchases through merchants(like POS)")
st.write("4. Financial Services ==> Payments/Transfers made as per prior purchase/sale agreements")
st.write("###### Following analysis are based on the above categories of Transactions")
st.write("")
st.write("")

#****************   Overall Transactions Trend Line
query4 = '''select Year,Transaction_Type,sum(Transaction_Count), sum(Transaction_Amount)
            from project_phonepe.aggregate_transaction 
            group by Year, Transaction_Type
            '''

mycursor.execute(query4)
mydb.commit()
out=mycursor.fetchall()
df4=pd.DataFrame(out,columns=["Year","Transaction Type","Number of Transactions","Amount of Transaction in Rs."])

st.write('## INDIA - Digital Transaction Types Analysis')
col1,col2=st.columns(2)
with col1:
   fig4_1 = px.line(df4,x="Year", y="Number of Transactions", color="Transaction Type")
   st.write('###### Trend Based on Transaction Volume')
   st.plotly_chart(fig4_1, use_container_width=True, sharing="streamlit", theme="streamlit")
with col2:
   fig4_2 = px.line(df4,x="Year", y="Amount of Transaction in Rs.", color="Transaction Type")
   st.write('###### Trend Based on Amount of Transaction(in Rs.)')
   st.plotly_chart(fig4_2, use_container_width=True, sharing="streamlit", theme="streamlit")
#st.write(df1)


#***************** Sunburst Charts - Overall Transaction *****************************************


query3 = '''select State,Year,Transaction_Type,sum(Transaction_Count), sum(Transaction_Amount)
            from project_phonepe.aggregate_transaction 
            group by State,Year,Transaction_Type
            '''

mycursor.execute(query3)
mydb.commit()
out=mycursor.fetchall()
df3=pd.DataFrame(out,columns=["State","Year","Transaction Type","Annual Transaction Count","Annual Transaction Amount"])
#st.write(df)
#df3['Quarter']=df3['Quarter'].replace(mappings)

fig3_1 = px.sunburst(df3,path=[ 'Year','State','Transaction Type'], values='Annual Transaction Count')
fig3_2 = px.sunburst(df3,path=[ 'Year','State','Transaction Type'], values='Annual Transaction Amount')

col1,col2=st.columns(2)

with col1:
    st.write('##### Spread of Transaction Volume')
    st.plotly_chart(fig3_1, use_container_width=True, sharing="streamlit", theme="streamlit")

with col2:
    st.write('##### Spread of Amount of Transaction in Rs.')
    st.plotly_chart(fig3_2, use_container_width=True, sharing="streamlit", theme="streamlit")

#****************************************************************************************************************

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

query1 = '''select State,Year,Quarter,Transaction_Type,Transaction_Count,Transaction_Amount
            from project_phonepe.aggregate_transaction 
            where State = %s and Year = %s and Quarter = %s
            '''
mycursor.execute(query1,input1)
mydb.commit()
out=mycursor.fetchall()
df1=pd.DataFrame(out,columns=["State","Year","Quarter","Transaction Type",
                             "Number of Transactions","Amount of Transaction in Rs."])

#st.write("#### Transaction Data for ",option1_1,"- Year ",option1_2,"Quarter ",option1_3)
#st.write(df1)

fig1_x=list(df1["Transaction Type"])
fig1_y1=list(pd.to_numeric(df1["Number of Transactions"]))
fig1_y2=list(pd.to_numeric(df1["Amount of Transaction in Rs."]))

fig1_1 = px.bar(x=fig1_x, y=fig1_y1)
fig1_2 = px.bar(x=fig1_x, y=fig1_y2) 
fig1_3 = px.pie(values=fig1_y1, names=fig1_x)
fig1_4 = px.pie(values=fig1_y2, names=fig1_x)

st.write("#### Transaction Visuals for ",option1_1,"- Year ",option1_2,"Quarter ",option1_3)

col4, col5 = st.columns(2)

with col4:
   st.write("###### Number of Transactions for each Type")
   st.plotly_chart(fig1_1, use_container_width=True, sharing="streamlit", theme="streamlit")
   st.write("###### Based on Number of Transactions")
   st.plotly_chart(fig1_3, use_container_width=True, sharing="streamlit", theme="streamlit")

with col5:
   st.write("###### Amount of Transaction for each Type in Rs.")
   st.plotly_chart(fig1_2, use_container_width=True, sharing="streamlit", theme="streamlit")
   st.write("###### Based on Amount of Transaction in Rs.")
   st.plotly_chart(fig1_4, use_container_width=True, sharing="streamlit", theme="streamlit")
   


#********************   Transaction Type Trend Lines for the past few years for States ***********************
option0=st.selectbox("Select State for Trend Analysis",
                    ['Andaman & Nicobar','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh',
                     'Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana',
                     'Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh',
                     'Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland',
                     'Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura',
                     'Uttarakhand','Uttar Pradesh','West Bengal'],
                     placeholder='Andaman & Nicobar')

input0=[option0]
query0 = '''select State,Year,Transaction_Type,sum(Transaction_Count), sum(Transaction_Amount)
            from project_phonepe.aggregate_transaction 
            where State = %s
            group by Year, Transaction_Type
            '''

mycursor.execute(query0,input0)
mydb.commit()
out=mycursor.fetchall()
df0=pd.DataFrame(out,columns=["State","Year","Transaction Type","Number of Transactions","Amount of Transaction in Rs."])
st.write(df0)

#init_notebook_mode()

#fig3 = go.Figure()
#for index, row in df3.groupby('Transaction Type'):
#    fig3.add_scatter(x=row['Year'], y=row['Number of Transactions'], name=index, mode='lines')

#fig3_1=iplot(fig3)
#st.plotly_chart(fig3_1, use_container_width=True, sharing="streamlit", theme="streamlit")

fig0 = px.line(df0,x="Year", y="Number of Transactions", color="Transaction Type")
st.plotly_chart(fig0, use_container_width=True, sharing="streamlit", theme="streamlit")

#***************** Key Insights **************************************
st.header("Key Insights")
st.write("India has been showing a sudden increase in digital transactions in the past 5 years")
st.write('''Major increase of transaction volume and amount comes from individual money transfers and merchant payments
         as it can be seen from the pie charts that these 2 transaction amount to more than 80%
         in both volume and in amount in all states''')
st.write('''It can also be inferred that UPI apps' increased usage are mainly driven by increase in the 
         use of individuals''')
st.write("This shows the tremendous increase of basic financial literacy in India")
st.write("Other transaction segments are also showing a steady increase in volume and amount")