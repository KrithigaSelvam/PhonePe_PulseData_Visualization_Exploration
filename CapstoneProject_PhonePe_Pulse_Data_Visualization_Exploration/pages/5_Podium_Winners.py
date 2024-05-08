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

st.title("Podium Winners - Top 3 of the Chart")
st.write("Phonepe has provided District/Pincode wise data as follows")
st.write("Top 10 Transaction Districts for each quarter from 2018 to 2023 for all States")
st.write("Top 10 Transaction Pincodes for each quarter from 2018 to 2023 for all States")
st.write("Top 10 Number of Registered Users Districts for each quarter from 2018 to 2023 for all States")
st.write("Top 10 Number of Registered Users Pincodes for each quarter from 2018 to 2023 for all States")
st.write("")
st.write("")
st.write("##### Following visuals are based on the above data provided")
st.write("")
st.write("")
#**********************************************************************************************

st.header('Top 3 Data for each Quarter')

col1, col2 = st.columns(2)

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

#*****************************************************************************************  DISTRICT - WISE
st.write("#### Transaction Count - Top 3 Districts of ",option1_1,"- Year ",option1_2)

#                                                                                       Transaction Count Bar Charts

query1 = '''select District,Transaction_Count
            from project_phonepe.top_transaction_district 
            where State = %s and Year = %s and Quarter = %s
            order by Transaction_Count desc limit 3
            '''

col1, col2, col3, col4 = st.columns(4)

with col1:
   quarter=1
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query1,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df1_1=pd.DataFrame(out,columns=["District","Number of Transactions"])
   fig1_1 = px.bar(df1_1,x="District", y="Number of Transactions")
   fig1_1.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)))
   fig1_1.update_traces(marker_color=['#006600','#008000', '#00b300'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 1")
   st.plotly_chart(fig1_1, use_container_width=True, sharing="streamlit", theme="streamlit")

with col2:
   quarter=2
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query1,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df1_2=pd.DataFrame(out,columns=["District","Number of Transactions"])
   fig1_2 = px.bar(df1_2,x="District", y="Number of Transactions")
   fig1_2.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)))
   fig1_2.update_traces(marker_color=['#006600','#008000', '#00b300'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 2")
   st.plotly_chart(fig1_2, use_container_width=True, sharing="streamlit", theme="streamlit")

with col3:
   quarter=3
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query1,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df1_3=pd.DataFrame(out,columns=["District","Number of Transactions"])
   fig1_3 = px.bar(df1_3,x="District", y="Number of Transactions")
   fig1_3.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)))
   fig1_3.update_traces(marker_color=['#006600','#008000', '#00b300'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 3")
   st.plotly_chart(fig1_3, use_container_width=True, sharing="streamlit", theme="streamlit")

with col4:
   quarter=4
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query1,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df1_4=pd.DataFrame(out,columns=["District","Number of Transactions"])
   fig1_4 = px.bar(df1_4,x="District", y="Number of Transactions")
   fig1_4.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)))
   fig1_4.update_traces(marker_color=['#006600','#008000', '#00b300'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 4")
   st.plotly_chart(fig1_4, use_container_width=True, sharing="streamlit", theme="streamlit")


#                                                                                        Transaction Amount Bar Charts

st.write("#### Amount of Transaction -  Top 3 Districts of ",option1_1,"- Year ",option1_2)

query2 = '''select District,Transaction_Amount
            from project_phonepe.top_transaction_district 
            where State = %s and Year = %s and Quarter = %s
            order by Transaction_Amount desc limit 3
            '''

col1, col2, col3, col4 = st.columns(4)

with col1:
   quarter=1
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query2,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df2_1=pd.DataFrame(out,columns=["District","Amount of Transaction in Rs."])
   fig2_1 = px.bar(df2_1,x="District", y="Amount of Transaction in Rs.")
   fig2_1.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)))
   fig2_1.update_traces(marker_color=['#000099','#0000cc', '#0000ff'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 1")
   st.plotly_chart(fig2_1, use_container_width=True, sharing="streamlit", theme="streamlit")

with col2:
   quarter=2
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query2,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df2_2=pd.DataFrame(out,columns=["District","Amount of Transaction in Rs."])
   fig2_2 = px.bar(df2_2,x="District", y="Amount of Transaction in Rs.")
   fig2_2.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)))
   fig2_1.update_traces(marker_color=['#000099','#0000cc', '#0000ff'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 2")
   st.plotly_chart(fig2_2, use_container_width=True, sharing="streamlit", theme="streamlit")

with col3:
   quarter=3
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query2,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df2_3=pd.DataFrame(out,columns=["District","Amount of Transaction in Rs."])
   fig2_3 = px.bar(df2_3,x="District", y="Amount of Transaction in Rs.")
   fig2_3.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)))
   fig2_3.update_traces(marker_color=['#000099','#0000cc', '#0000ff'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 3")
   st.plotly_chart(fig2_3, use_container_width=True, sharing="streamlit", theme="streamlit")

with col4:
   quarter=4
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query2,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df2_4=pd.DataFrame(out,columns=["District","Amount of Transaction in Rs."])
   fig2_4 = px.bar(df2_4,x="District", y="Amount of Transaction in Rs.")
   fig2_4.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)))
   fig2_4.update_traces(marker_color=['#000099','#0000cc', '#0000ff'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 4")
   st.plotly_chart(fig2_4, use_container_width=True, sharing="streamlit", theme="streamlit")

#                                                                                        Registered Users Bar Charts


st.write("#### Number of Registered Users -  Top 3 Districts of ",option1_1,"- Year ",option1_2)

query3 = '''select District,Registered_Users
            from project_phonepe.top_users_district 
            where State = %s and Year = %s and Quarter = %s
            order by Registered_Users desc limit 3
            '''

col1, col2, col3, col4 = st.columns(4)

with col1:
   quarter=1
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query3,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df3_1=pd.DataFrame(out,columns=["District","Number of Registered Users"])
   fig3_1 = px.bar(df3_1,x="District", y="Number of Registered Users")
   fig3_1.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)))
   fig3_1.update_traces(marker_color=['#990033','#cc0044', '#ff0055'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 1")
   st.plotly_chart(fig3_1, use_container_width=True, sharing="streamlit", theme="streamlit")

with col2:
   quarter=2
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query3,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df3_2=pd.DataFrame(out,columns=["District","Number of Registered Users"])
   fig3_2 = px.bar(df3_2,x="District", y="Number of Registered Users")
   fig3_2.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)))
   fig3_2.update_traces(marker_color=['#990033','#cc0044', '#ff0055'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 2")
   st.plotly_chart(fig3_2, use_container_width=True, sharing="streamlit", theme="streamlit")

with col3:
   quarter=3
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query3,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df3_3=pd.DataFrame(out,columns=["District","Number of Registered Users"])
   fig3_3 = px.bar(df3_3,x="District", y="Number of Registered Users")
   fig3_3.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)))
   fig3_3.update_traces(marker_color=['#990033','#cc0044', '#ff0055'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 3")
   st.plotly_chart(fig3_3, use_container_width=True, sharing="streamlit", theme="streamlit")

with col4:
   quarter=4
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query3,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df3_4=pd.DataFrame(out,columns=["District","Number of Registered Users"])
   fig3_4 = px.bar(df3_4,x="District", y="Number of Registered Users")
   fig3_4.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)))
   fig3_4.update_traces(marker_color=['#990033','#cc0044', '#ff0055'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 4")
   st.plotly_chart(fig3_4, use_container_width=True, sharing="streamlit", theme="streamlit")

#*********************************************************************************************    PINCODE - WISE

st.write("#### Transaction Count - Top 3 PINCODEs of ",option1_1,"- Year ",option1_2)

#                                                                                       Transaction Count Bar Charts

query4 = '''select Pincode,Transaction_Count
            from project_phonepe.top_transaction_pincode 
            where State = %s and Year = %s and Quarter = %s
            order by Transaction_Count desc limit 3
            '''

col1, col2, col3, col4 = st.columns(4)

with col1:
   quarter=1
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query4,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df4_1=pd.DataFrame(out,columns=["Pincode","Number of Transactions"])
   fig4_1 = px.bar(df4_1,x="Pincode", y="Number of Transactions")
   fig4_1.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)),xaxis_type='category')
   fig4_1.update_traces(marker_color=['#006600','#008000', '#00b300'])
   #fig4_1.update_layout(xaxis_type='category') 
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 1")
   st.plotly_chart(fig4_1, use_container_width=True, sharing="streamlit", theme="streamlit")

with col2:
   quarter=2
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query4,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df4_2=pd.DataFrame(out,columns=["Pincode","Number of Transactions"])
   fig4_2 = px.bar(df4_2,x="Pincode", y="Number of Transactions")
   fig4_2.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)),xaxis_type='category')
   fig4_2.update_traces(marker_color=['#006600','#008000', '#00b300'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 2")
   st.plotly_chart(fig4_2, use_container_width=True, sharing="streamlit", theme="streamlit")

with col3:
   quarter=3
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query4,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df4_3=pd.DataFrame(out,columns=["Pincode","Number of Transactions"])
   fig4_3 = px.bar(df4_3,x="Pincode", y="Number of Transactions")
   fig4_3.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)),xaxis_type='category')
   fig4_3.update_traces(marker_color=['#006600','#008000', '#00b300'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 3")
   st.plotly_chart(fig4_3, use_container_width=True, sharing="streamlit", theme="streamlit")

with col4:
   quarter=4
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query4,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df4_4=pd.DataFrame(out,columns=["Pincode","Number of Transactions"])
   fig4_4 = px.bar(df4_4,x="Pincode", y="Number of Transactions")
   fig4_4.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)),xaxis_type='category')
   fig4_4.update_traces(marker_color=['#006600','#008000', '#00b300'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 4")
   st.plotly_chart(fig4_4, use_container_width=True, sharing="streamlit", theme="streamlit")


#                                                                                        Transaction Amount Bar Charts

st.write("#### Amount of Transaction -  Top 3 PINCODEs of ",option1_1,"- Year ",option1_2)

query5 = '''select Pincode,Transaction_Amount
            from project_phonepe.top_transaction_pincode 
            where State = %s and Year = %s and Quarter = %s
            order by Transaction_Amount desc limit 3
            '''

col1, col2, col3, col4 = st.columns(4)

with col1:
   quarter=1
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query5,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df5_1=pd.DataFrame(out,columns=["Pincode","Amount of Transaction in Rs."])
   fig5_1 = px.bar(df5_1,x="Pincode", y="Amount of Transaction in Rs.")
   fig5_1.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)),xaxis_type='category')
   fig5_1.update_traces(marker_color=['#000099','#0000cc', '#0000ff'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 1")
   st.plotly_chart(fig5_1, use_container_width=True, sharing="streamlit", theme="streamlit")

with col2:
   quarter=2
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query5,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df5_2=pd.DataFrame(out,columns=["Pincode","Amount of Transaction in Rs."])
   fig5_2 = px.bar(df5_2,x="Pincode", y="Amount of Transaction in Rs.")
   fig5_2.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)),xaxis_type='category')
   fig5_2.update_traces(marker_color=['#000099','#0000cc', '#0000ff'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 2")
   st.plotly_chart(fig5_2, use_container_width=True, sharing="streamlit", theme="streamlit")

with col3:
   quarter=3
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query5,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df5_3=pd.DataFrame(out,columns=["Pincode","Amount of Transaction in Rs."])
   fig5_3 = px.bar(df5_3,x="Pincode", y="Amount of Transaction in Rs.")
   fig5_3.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)),xaxis_type='category')
   fig5_3.update_traces(marker_color=['#000099','#0000cc', '#0000ff'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 3")
   st.plotly_chart(fig5_3, use_container_width=True, sharing="streamlit", theme="streamlit")

with col4:
   quarter=4
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query5,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df5_4=pd.DataFrame(out,columns=["Pincode","Amount of Transaction in Rs."])
   fig5_4 = px.bar(df5_4,x="Pincode", y="Amount of Transaction in Rs.")
   fig5_4.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)),xaxis_type='category')
   fig5_4.update_traces(marker_color=['#000099','#0000cc', '#0000ff'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 4")
   st.plotly_chart(fig5_4, use_container_width=True, sharing="streamlit", theme="streamlit")

#                                                                                        Registered Users Bar Charts


st.write("#### Number of Registered Users -  Top 3 PINCODEs of ",option1_1,"- Year ",option1_2)

query6 = '''select Pincode,Registered_Users
            from project_phonepe.top_users_pincode 
            where State = %s and Year = %s and Quarter = %s
            order by Registered_Users desc limit 3
            '''

col1, col2, col3, col4 = st.columns(4)

with col1:
   quarter=1
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query6,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df6_1=pd.DataFrame(out,columns=["Pincode","Number of Registered Users"])
   fig6_1 = px.bar(df6_1,x="Pincode", y="Number of Registered Users")
   fig6_1.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)),xaxis_type='category')
   fig6_1.update_traces(marker_color=['#990033','#cc0044', '#ff0055'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 1")
   st.plotly_chart(fig6_1, use_container_width=True, sharing="streamlit", theme="streamlit")

with col2:
   quarter=2
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query6,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df6_2=pd.DataFrame(out,columns=["Pincode","Number of Registered Users"])
   fig6_2 = px.bar(df6_2,x="Pincode", y="Number of Registered Users")
   fig6_2.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)),xaxis_type='category')
   fig6_2.update_traces(marker_color=['#990033','#cc0044', '#ff0055'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 2")
   st.plotly_chart(fig6_2, use_container_width=True, sharing="streamlit", theme="streamlit")

with col3:
   quarter=3
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query6,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df6_3=pd.DataFrame(out,columns=["Pincode","Number of Registered Users"])
   fig6_3 = px.bar(df6_3,x="Pincode", y="Number of Registered Users")
   fig6_3.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)),xaxis_type='category')
   fig6_3.update_traces(marker_color=['#990033','#cc0044', '#ff0055'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 3")
   st.plotly_chart(fig6_3, use_container_width=True, sharing="streamlit", theme="streamlit")

with col4:
   quarter=4
   input1=[option1_1,option1_2,quarter]
   mycursor.execute(query6,input1)
   mydb.commit()
   out=mycursor.fetchall()
   df6_4=pd.DataFrame(out,columns=["Pincode","Number of Registered Users"])
   fig6_4 = px.bar(df6_4,x="Pincode", y="Number of Registered Users")
   fig6_4.update_layout(xaxis=dict(tickangle=-45,tickfont=dict(size=14)),xaxis_type='category')
   fig6_4.update_traces(marker_color=['#990033','#cc0044', '#ff0055'])
   
   #st.write("###### Bar Chart representing Number of Transactions for each district")
   st.write("###### Quarter - 4")
   st.plotly_chart(fig6_4, use_container_width=True, sharing="streamlit", theme="streamlit")