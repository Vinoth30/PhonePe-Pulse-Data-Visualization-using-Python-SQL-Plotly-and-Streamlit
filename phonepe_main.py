import pandas as pd
import os
import json
import plotly.express as px
import pymysql
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

logo=Image.open('C:/Users/muthu/Desktop/py/phonepe-logo-icon.png')
st.set_page_config(page_title='Phonepe Pulse Data',page_icon=logo,layout='wide')
st.title(':violet[ PhonePe Pulse Data Visualization ]')
Map_Trans_df=pd.read_csv('C:/Users/muthu/map_Trans.csv')

myconnection=pymysql.connect(host='127.0.0.1',user='root',password='admin',database="phonepedata",port=3306)
cur=myconnection.cursor()

# Aggregated Transactions
cur.execute("select * from aggregated_transactions;")
myconnection.commit()
table_1=cur.fetchall()
A_Trans_df=pd.DataFrame(table_1,columns=("States", "Year", "Quarter", "Transaction_Type", "Transaction_Count", "Transaction_Amount"))


# Aggregated_Users
cur.execute("select * from aggregated_users;")
myconnection.commit()
table_2=cur.fetchall()
A_Users_df=pd.DataFrame(table_2,columns=("States", "Year", "Quarter", "Brand", "Count", "Percentage"))

# Map_Transactions
cur.execute("select * from map_transactions;")
myconnection.commit()
table_3=cur.fetchall()
M_Trans_df=pd.DataFrame(table_3,columns=("States", "Year", "Quarter", "District_Name", "Transaction_Count", "Transaction_Amount"))

# Map_Users
cur.execute("select * from map_users;")
myconnection.commit()
table_4=cur.fetchall()
M_Users_df=pd.DataFrame(table_4,columns=("States", "Year", "Quarter", "District_Name", "RegisteredUsers", "AppOpens"))

# Top_Transactions
cur.execute("select * from top_transactions;")
myconnection.commit()
table_5=cur.fetchall()
T_Trans_df=pd.DataFrame(table_5,columns=("States", "Year", "Quarter", "Pincodes", "Transaction_Count", "Transaction_Amount"))

# Top_Users
cur.execute("select * from top_users;")
myconnection.commit()
table_6=cur.fetchall()
T_Users_df=pd.DataFrame(table_6,columns=("States", "Year", "Quarter", "Pincodes", "Registered_Users"))

# Streamlit

select = option_menu(menu_title=None, 
                     options = ["Phonepe","Search","Basic Queries","Geo Visualization","Overview"],
                     icons=["bar-chart","search","toggles","map","gear"],
                     default_index=2,
                     orientation="horizontal",
                     styles={"container": {"padding": "0!important", "background-color": "white","size":"cover"},
                            "icon": {"color": "black", "font-size": "20px"},
                            "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
                            "nav-link-selected": {"background-color": "#6F36AD"}})
# Phonepe Details
if select=="Phonepe":
    # st.image("")
    st.title('Overview of :violet[Phonepe]')
    col1,col2=st.columns(2)
    with col1:
        st.subheader("India's Trusted App")
        st.markdown("PhonePe  is an Indian digital payments and financial technology company.")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
        st.subheader("Mission Statement of :violet[Phonepe]")
        st.write(":violet[PhonePe's] mission is to provide equal opportunities for all Indians to accelerate their progress by unlocking the flow of money and access to services.")
        st.subheader("Features of :violet[Phonepe]")
        st.write("1. :violet[Easy UPI transactions]")
        st.write("2. :violet[Easy pay with Phone Numbers and Bank Accounts]")
        st.write("3. :violet[Bank History Check within a minute]")
        st.write("4. :violet[Credit and Debit card linking]")
        st.write("5. :violet[High Secure PIN Authorization]")
        st.subheader("Accelerate business growth with :violet[PhonePe Payment Gateway]")
        st.write("Payment solution by India's largest fintech platform")
        st.image("https://www.phonepe.com/webstatic/5730/static/ebcb964b1ddd1d87de7dfc10c6d43bb8/5707d/bs-pg-widget-image-2.png")
        st.write("Enjoy industry-best success rates and uncompromised security, Integrate with a no-code setup, developer-friendly APIs & native SDK, Handle large-scale transactions with dynamic routing ensuring 100% uptime")
        st.subheader("Get new users with :violet[PhonePe Switch]")
        st.image("https://www.phonepe.com/webstatic/5730/static/2a76181cc7c1471b3bde60ad88336be2/a384c/bs-switch-sec-web-1x.png")
        st.write("switch gives you access to over 50 Crore PhonePe users and you only pay for realised business. Setting up an app on PhonePe is cost-effective and requires minimal tech investment.")
        st.subheader("Meet your business :violet[goals faster]")
        st.image("https://www.phonepe.com/webstatic/5730/static/d22a4cde6865dd4ce6e3dd6daf2f8058/a2a87/bs-ad-web-2x.png")
        st.write("PhonePe can help you reach a wide user-base with targeted campaigns designed to meet your business needs. Let relevant consumers sample your products and services in the form of ‘reward coupons’ distributed on PhonePe, or advertise within the PhonePe app.")    
    with col2:
        st.subheader("Special Features of :violet[Phonepe]")
        st.subheader("Quick :violet[Checkout]")
        st.write("Enable customers to complete transactions without closing the website or applications")
        st.subheader("Payment :violet[Links]")
        st.write("Collect payments easily through links that you can generate & share with your customers")
        st.subheader("Guardian by :violet[phonepe]")
        st.subheader("Risk Operating System For Your Organization")
        st.image("https://www.phonepe.com/webstatic/5730/static/e06bca10588de8b65402781e0d1ebccb/19648/bs-guardian-widget-image.png")
        st.write("Our proprietary Fraud Detection and Risk Management Platform intelligently detects and prevents fraud efficiently. The automated fraud management platform consists of a suite of evolving products that minimize risk for businesses at scale.")
        st.subheader(":violet[PhonePe] Express")
        st.write("A lightning quick checkout experience built to grow your business. Amplify conversions. Reduce customer drop-offs.")
        st.image("https://www.phonepe.com/webstatic/5730/static/4e06e4b4a47c3a2c301e75f098c37d5d/63f6f/express-checkout-entryimg.png")
        st.write("With PhonePe Express Checkout, build a lightning fast shopping experience for your customers, enabling them smooth checkout without the pain of filling out long address and login forms.")
        st.subheader("Help your business :violet[go cashless]")
        st.image("https://www.phonepe.com/webstatic/5730/static/1036dc0f2904dfad21079100ad988e4d/8c758/bs-cashless-web-1x.png")
        st.write("Cash and card payments are no longer a complete solution for your customers. Join the UPI revolution and grow your sales by going cashless. PhonePe also offers exclusive value added services to all its merchant partners. You can list your store, add details and offers to your store listing, enable the PhonePe ATM and increase customer walk-ins with the PhonePe for Business app.")
        st.subheader("Smart:violet[Speaker]")
        st.image("https://www.phonepe.com/webstatic/5730/static/7930d2cf1bdcdc49ffdac6a973422d30/05d05/offline-smartspeaker-illustration-3x.png")
        st.write("Do more for your business with an all new PhonePe SmartSpeaker. Get loud and clear payment confirmations delivered instantly in up to 11 languages! So step into a smarter way that makes tracking payments easier than ever before.")
        st.subheader("Scan and :violet[Pay]")
        st.image("https://www.phonepe.com/webstatic/5730/static/45dc73a4fa6b2c039488a3fb7db12152/46878/offline-scannpay-web-1x.png")
        st.write("It’s swift, effortless and perfect for small businesses! We provide QR stickers, table-top standees and nifty hangings that your customers can use to make lightning fast payments. The money is credited to the bank account of your choice.")
        st.write(":copyright: Copyright - Using Images Owned by :violet[Phonepe]")
        
        
        
# MySQL Connection    
myconnection=pymysql.connect(host='127.0.0.1',user='root',password='admin',database="phonepedata",port=3306)
cur=myconnection.cursor()

# Basic Queries tab
if select == "Basic Queries":
    st.title("Basic :violet[Queries]")
    st.subheader("Choose Query from the dropdown box for know more about Phonepe Datas")
    options=["--Select--",
                "1. Top 10 states based on year and Transaction amount",
                "2. Least 10 states based on year and Transaction amount",
                "3. Top 10 mobile brands based on percentage of transaction",
                "4. Least 10 mobile brands based on percentage of transaction",
                "5. Top 10 Registered Users based on states and Districts",
                "6. Least 10 Registered Users based on states and Districts",
                "7. Top 10 Districts based on states and Transaction Amount",
                "8. Least 10 Districts based on states and Transaction Amount",
                "9. Top 50 transactions_type based on states and Transaction_Amount",
                "10.Least 10 transactions_type based on states and Transaction_Amount"]
    select_1=st.selectbox("Select the Query",options)
        
    if select_1=="1. Top 10 states based on year and Transaction amount":
            query_1='''SELECT States, Transaction_Amount, Year, Quarter
                        FROM (
                            SELECT States,Transaction_Amount,Year,Quarter,ROW_NUMBER() OVER (PARTITION BY States ORDER BY Transaction_Amount DESC) AS row_num
                            FROM top_transactions
                        ) ranked_transactions
                        WHERE row_num = 1
                        ORDER BY Transaction_Amount DESC
                        LIMIT 10;'''
            cur.execute(query_1)
            myconnection.commit()
            q1=cur.fetchall()
            df=pd.DataFrame(q1,columns=['States','Transaction_Amount', 'Year', 'Quarter'])
            col1,col2=st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.subheader("1. Top 10 states based on year and Transaction amount")
                selected_chart = st.selectbox("select the Year",("","Bar Chart","Area Chart"))
                fig=px.bar(df,x="States",y="Transaction_Amount")
                tab1,tab2=st.tabs(["Streamlit theme (default)","Plotly native theme"])
                with tab1:
                    if selected_chart=="Bar Chart":
                        st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                    else:
                        st.area_chart(df,x="States",y="Transaction_Amount")
                with tab2:
                    st.plotly_chart(fig,theme=None,use_container_width=True)
                    
    elif select_1=="2. Least 10 states based on year and Transaction amount":
            query_2='''SELECT States, Transaction_Amount, Year, Quarter
                        FROM (
                            SELECT States,Transaction_Amount,Year,Quarter,ROW_NUMBER() OVER (PARTITION BY States ORDER BY Transaction_Amount DESC) AS row_num
                            FROM top_transactions
                        ) ranked_transactions
                        WHERE row_num = 1
                        ORDER BY Transaction_Amount ASC
                        LIMIT 10;'''
            cur.execute(query_2)
            myconnection.commit()
            q2=cur.fetchall()
            df=pd.DataFrame(q2,columns=['States','Transaction_Amount', 'Year', 'Quarter'])
            col1,col2=st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.subheader("2. Least 10 states based on year and Transaction amount")
                fig=px.bar(df,x="States",y="Transaction_Amount")
                tab1,tab2=st.tabs(["Streamlit theme (default)","Plotly native theme"])
                with tab1:
                    st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                with tab2:
                    st.plotly_chart(fig,theme=None,use_container_width=True)
                    
    elif select_1=="3. Top 10 mobile brands based on percentage of transaction":
            query_3='''SELECT Brand, Percentage * 100 AS Modified_Percentage
                        FROM aggregated_users
                        ORDER BY Modified_Percentage DESC
                        LIMIT 30;'''
            cur.execute(query_3)
            myconnection.commit()
            q3=cur.fetchall()
            df=pd.DataFrame(q3,columns=["Brand","Modified_Percentage"])
            col1,col2=st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.subheader("3. Top 10 mobile brands based on percentage of transaction")
                fig=px.bar(df,x="Brand",y="Modified_Percentage")
                tab1,tab2=st.tabs(["Streamlit theme (default)","Plotly native theme"])
                with tab1:
                    st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                with tab2:
                    st.plotly_chart(fig,theme=None,use_container_width=True)
                    
    elif select_1=="4. Least 10 mobile brands based on percentage of transaction":
            query_4='''SELECT Brand, Percentage * 100 AS Modified_Percentage
                        FROM aggregated_users
                        ORDER BY Modified_Percentage ASC
                        LIMIT 10;'''
            cur.execute(query_4)
            myconnection.commit()
            q4=cur.fetchall()
            df=pd.DataFrame(q4,columns=["Brand","Modified_Percentage"])
            col1,col2=st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.subheader("4. Least 10 mobile brands based on percentage of transaction")
                fig=px.bar(df,x="Brand",y="Modified_Percentage")
                tab1,tab2=st.tabs(["Streamlit theme (default)","Plotly native theme"])
                with tab1:
                    st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                with tab2:
                    st.plotly_chart(fig,theme=None,use_container_width=True)
                    
                    
                    
                    
    elif select_1=="5. Top 10 Registered Users based on states and Districts":
            query_5='''SELECT States, Pincodes, MAX(Registered_Users) AS RegisteredUsers
                        FROM top_users
                        GROUP BY States, Pincodes
                        ORDER BY RegisteredUsers DESC
                        LIMIT 10;'''
            cur.execute(query_5)
            myconnection.commit()
            q5=cur.fetchall()
            df=pd.DataFrame(q5,columns=["States","Pincodes","RegisteredUsers"])
            col1,col2=st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.subheader("5. Top 10 Registered Users based on states and Districts")
                fig=px.bar(df,x="States",y="RegisteredUsers")
                tab1,tab2=st.tabs(["Streamlit theme (default)","Plotly native theme"])
                with tab1:
                    st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                with tab2:
                    st.plotly_chart(fig,theme=None,use_container_width=True)
                    
                    
                    
    elif select_1=="6. Least 10 Registered Users based on states and Districts":
            query_6='''SELECT States, Pincodes, MAX(Registered_Users) AS RegisteredUsers
                        FROM top_users
                        GROUP BY States, Pincodes
                        ORDER BY RegisteredUsers ASC
                        LIMIT 10;'''
            cur.execute(query_6)
            myconnection.commit()
            q6=cur.fetchall()
            df=pd.DataFrame(q6,columns=["States","Pincodes","RegisteredUsers"])
            col1,col2=st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.subheader("6. Least 10 Registered Users based on states and Districts")
                fig=px.bar(df,x="States",y="RegisteredUsers")
                tab1,tab2=st.tabs(["Streamlit theme (default)","Plotly native theme"])
                with tab1:
                    st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                with tab2:
                    st.plotly_chart(fig,theme=None,use_container_width=True)
                    
                    
                    
    elif select_1=="7. Top 10 Districts based on states and Transaction Amount":
            query_7='''SELECT States, District_Name, SUM(Transaction_Amount) AS TransactionAmount
                        FROM map_transactions
                        GROUP BY States, District_Name
                        ORDER BY TransactionAmount DESC
                        LIMIT 10;'''
            cur.execute(query_7)
            myconnection.commit()
            q7=cur.fetchall()
            df=pd.DataFrame(q7,columns=["States","District_Name","TransactionAmount"])
            col1,col2=st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.subheader("7. Top 10 Districts based on states and Transaction Amount")
                fig=px.bar(df,x="District_Name",y="TransactionAmount")
                tab1,tab2=st.tabs(["Streamlit theme (default)","Plotly native theme"])
                with tab1:
                    st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                with tab2:
                    st.plotly_chart(fig,theme=None,use_container_width=True)
                    
                    
                    
    elif select_1=="8. Least 10 Districts based on states and Transaction Amount":
            query_8='''SELECT States, District_Name, SUM(Transaction_Amount) AS TransactionAmount
                        FROM map_transactions
                        GROUP BY States, District_Name
                        ORDER BY TransactionAmount ASC
                        LIMIT 10'''
            cur.execute(query_8)
            myconnection.commit()
            q8=cur.fetchall()
            df=pd.DataFrame(q8,columns=["States","District_Name","TransactionAmount"])
            col1,col2=st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.subheader("8. Least 10 Districts based on states and Transaction Amount")
                fig=px.bar(df,x="District_Name",y="TransactionAmount")
                tab1,tab2=st.tabs(["Streamlit theme (default)","Plotly native theme"])
                with tab1:
                    st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                with tab2:
                    st.plotly_chart(fig,theme=None,use_container_width=True)
                    
                    
                    
    elif select_1=="9. Top 50 transactions_type based on states and Transaction_Amount":
            query_9='''SELECT DISTINCT States,Transaction_Type,sum(Transaction_Amount) as TransactionAmount FROM aggregated_transactions 
                        GROUP BY States,Transaction_Type 
                        ORDER BY TransactionAmount DESC 
                        LIMIT 50'''
            cur.execute(query_9)
            myconnection.commit()
            q9=cur.fetchall()
            df=pd.DataFrame(q9,columns=["States","Transaction_Type","TransactionAmount"])
            col1,col2=st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.subheader("8. Least 50 Districts based on states and Transaction Amount")
                fig=px.bar(df,x="States",y="Transaction_Type")
                tab1,tab2=st.tabs(["Streamlit theme (default)","Plotly native theme"])
                with tab1:
                    st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                with tab2:
                    st.plotly_chart(fig,theme=None,use_container_width=True)
                    
                    
                    
    elif select_1=="10.Least 10 transactions_type based on states and Transaction_Amount":
            query_10='''SELECT DISTINCT States,Transaction_Type,sum(Transaction_Amount) as TransactionAmount FROM aggregated_transactions 
                        GROUP BY States,Transaction_Type 
                        ORDER BY TransactionAmount ASC 
                        LIMIT 10'''
            cur.execute(query_10)
            myconnection.commit()
            q10=cur.fetchall()
            df=pd.DataFrame(q10,columns=["States","Transaction_Type","TransactionAmount"])
            col1,col2=st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.subheader("8. Least 10 Districts based on states and Transaction Amount")
                fig=px.bar(df,x="States",y="Transaction_Type")
                tab1,tab2=st.tabs(["Streamlit theme (default)","Plotly native theme"])
                with tab1:
                    st.plotly_chart(fig,theme="streamlit",use_container_width=True)
                with tab2:
                    st.plotly_chart(fig,theme=None,use_container_width=True)
                    
# Search tab 
if select =="Search":
    st.title("Explore the different options for :violet[Phonepe Visualizations]")
    Topic = ["","District","Registered users","Top Transactions","Transaction Type"]
    choice = st.selectbox("Search by",Topic)
    
# Creating Functions for transaction type
     
    def trans_type(type):
        query=(f'''select distinct States,year,Quarter,Transaction_Type,Transaction_Amount from aggregated_transactions
                    where Transaction_Type='{type}'
                    order by States,Quarter,Year''')
        cur.execute(query)
        myconnection.commit()
        q=cur.fetchall()
        df=pd.DataFrame(q,columns=['States','Year', 'Quarter', 'Transaction_Type', 'Transaction_Amount'])
        return df
    def trans_type_year(year,type):
        query=(f'''select distinct states,year,quarter,Transaction_Type,Transaction_Amount from aggregated_transactions
                    where Transaction_Type='{type}' and year='{year}'
                    order by states,quarter,year''')
        cur.execute(query)
        myconnection.commit()
        q=cur.fetchall()
        df=pd.DataFrame(q,columns=['States','Year', 'Quarter', 'Transaction_Type', 'Transaction_Amount'])
        return df
    def trans_type_quarter(type,year,quarter):
        query=(f'''select distinct states,year,quarter,Transaction_Type,Transaction_Amount from aggregated_transactions
               where Transaction_Type='{type}' and year='{year}' and quarter='{quarter}'
               order by states,year,quarter''')
        cur.execute(query)
        myconnection.commit()
        q=cur.fetchall()
        df=pd.DataFrame(q,columns=['States','Year', 'Quarter', 'Transaction_Type', 'Transaction_Amount'])
        return df
       
    
    if choice == "Transaction Type":
        select = st.selectbox('SELECT VIEW', ['Tabular view', 'Plotly View'], 0)
        if select == "Tabular view":
            col1,col2,col3=st.columns(3)
            with col1:
                st.subheader("Select type of Transaction")
                Transaction_Type=st.selectbox("Search by",["Peer-to-peer payments","Merchant payments", "Financial Services","Recharge & bill payments", "Others"],0)
            with col2:
                st.subheader("Select Year")
                transaction_year=st.selectbox("Year",["", "2018", "2019", "2020", "2021", "2022","2023"], 0)
            with col3:
                st.subheader("Select Quarter")
                transaction_Quarter=st.selectbox("Quarter",["1","2","3","4"],0)
            if Transaction_Type:
                col1,col2,col3=st.columns(3)
                with col1:
                    st.subheader(f"Table View of {Transaction_Type}") 
                    st.write(trans_type(Transaction_Type))   
            if Transaction_Type and transaction_year:
                with col2:
                    st.subheader(f"in {transaction_year}") 
                    st.write(trans_type_year(transaction_year,Transaction_Type))
            if Transaction_Type and transaction_year and transaction_Quarter:
                with col3:
                    st.subheader(f"in {transaction_Quarter}")
                    st.write(trans_type_quarter(Transaction_Type,transaction_year,transaction_Quarter))
        else:
            col1,col2,col3=st.columns(3)
            with col1:
                st.subheader("Select Transaction Type")
                Transaction_Type=st.selectbox("Search by",["Peer-to-peer payments","Merchant payments", "Financial Services","Recharge & bill payments", "Others"],0)
                if Transaction_Type:
                    df=trans_type(Transaction_Type)
                    fig=px.bar(df,x="States",y="Transaction_Amount",title=f"Visualization of {Transaction_Type}",color="Year")
                    st.plotly_chart(fig,theme=None,use_container_width=True)
            with col2:
                st.subheader("Select the Year")
                transaction_year=st.selectbox("Year",["", "2018", "2019", "2020", "2021", "2022","2023"], 0)
                if transaction_year:
                    df=trans_type_year(transaction_year,Transaction_Type)
                    fig=px.bar(df,x="States",y="Transaction_Amount",title=f"Visualization of {Transaction_Type} in {transaction_year}",color="Quarter")
                    st.plotly_chart(fig,theme=None,use_container_width=True)
            with col3:
                col1,col2,col3=st.columns(3)
                with col1:
                    st.subheader("Select Quarter")
                    transaction_Quarter=st.selectbox("Quarter",["1","2","3","4"],0)
                    if transaction_Quarter:
                        df=trans_type_quarter(Transaction_Type,transaction_year,transaction_Quarter)
                        fig=px.bar(df,x="States",y="Transaction_Amount",title=f"Visualization of {Transaction_Type} of {transaction_year} in {transaction_Quarter}",color="States")
                        st.plotly_chart(fig,theme=None,use_container_width=True)
                        
                        
# Creating Functions for Top Transactions

    def top_trans_state(state_1):
        query=(f'''select states,year,quarter,pincodes,transaction_count,Transaction_Amount from top_transactions
                where states='{state_1}'
                order by States,Year,Quarter''')
        cur.execute(query)
        myconnection.commit()
        q=cur.fetchall()
        df=pd.DataFrame(q,columns=["States", "Year", "Quarter", "Pincodes", "Transaction_Count", "Transaction_Amount"])
        return df
    def  top_trans_year(state_1,year_1):
        query=(f'''select states,year,quarter,pincodes,transaction_count,Transaction_Amount from top_transactions
                where states='{state_1}' and year='{year_1}'
                order by states,year,quarter''')
        cur.execute(query)
        myconnection.commit()
        q=cur.fetchall()
        df=pd.DataFrame(q,columns=["States", "Year", "Quarter", "Pincodes", "Transaction_Count", "Transaction_Amount"])
        return df
    def top_trans_quarter(state_1,quarter_1):
        query=(f'''select states,year,quarter,pincodes,transaction_count,Transaction_Amount from top_transactions
                where states='{state_1}' and quarter='{quarter_1}'
                order by states,year,quarter''')
        cur.execute(query)
        myconnection.commit()
        q=cur.fetchall()
        df=pd.DataFrame(q,columns=["States", "Year", "Quarter", "Pincodes", "Transaction_Count", "Transaction_Amount"])
        return df

    if choice=="Top Transactions":
        select = st.selectbox('SELECT VIEW', ['Tabular view', 'Plotly View'], 0)
        if select == "Tabular view":
            col1,col2,col3=st.columns(3)
            with col1:
                st.subheader("Select State")
                state_list=['', 'andaman & nicobar islands', 'andhra pradesh', 'arunachal pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra & nagar haveli & daman & diu',
                                'delhi', 'goa', 'gujarat', 'haryana', 'himachal spradesh', 'jammu & kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya pradesh',
                                'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
                                'sikkim', 'tamil nadu', 'telangana', 'tripura', 'uttar pradesh', 'uttarakhand', 'west bengal']
                top_transaction_state=st.selectbox("States",state_list,0)
            with col2:
                st.subheader("Select Year")
                top_transaction_year=st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022","2023"], 0)
            with col3:
                st.subheader("Select Quarter")
                top_transaction_quarter=st.selectbox("Quarter",["1","2","3","4"],0)
                
            if top_transaction_state:
                col,col2,col3=st.columns(3)
                with col1:
                    st.subheader(f"{top_transaction_state}") 
                    st.write(top_trans_state(top_transaction_state))
            if top_transaction_state and top_transaction_year:
                with col2:
                    st.subheader(f"{top_transaction_state}-{top_transaction_year}")
                    st.write(top_trans_year(top_transaction_state,top_transaction_year))
            if top_transaction_state and top_transaction_quarter:
                with col3:
                    st.subheader(f"{top_transaction_state}-{top_transaction_quarter}")
                    st.write(top_trans_quarter(top_transaction_state,top_transaction_quarter))
        else:
            col1,col2,col3=st.columns(3)
            with col1:
                st.subheader("Select State")
                state_list=['', 'andaman & nicobar islands', 'andhra pradesh', 'arunachal pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra & nagar haveli & daman & diu',
                                    'delhi', 'goa', 'gujarat', 'haryana', 'himachal pradesh', 'jammu & kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya pradesh',
                                    'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
                                    'sikkim', 'tamil nadu', 'telangana', 'tripura', 'uttar pradesh', 'uttarakhand', 'west bengal']
                top_transaction_state=st.selectbox("States",state_list,0)
                if top_transaction_state:
                    df=top_trans_state(top_transaction_state)
                    fig=px.bar(df,x="Year",y="Transaction_Count",title=f"Top Transactions in {top_transaction_state}",color="Quarter")
                    st.plotly_chart(fig,theme=None,use_container_width=True)
            with col2:
                st.subheader("Select Year")
                top_transaction_year=st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022","2023"], 0)
                if top_transaction_state and top_transaction_year:
                    df=top_trans_year(top_transaction_state,top_transaction_year)
                    fig=px.bar(df,x="Transaction_Amount",y="Transaction_Count",title=f"Top Transactions in {top_transaction_state}-{top_transaction_year}",color="Quarter")
                    st.plotly_chart(fig,theme=None,use_container_width=True)
            with col3:
                st.subheader("Select Quarter")
                top_transaction_quarter=st.selectbox("Quarter",["1","2","3","4"],0)
                if top_transaction_state and top_transaction_quarter:
                    df=top_trans_quarter(top_transaction_state,top_transaction_quarter)
                    fig=px.bar(df,x="Year",y="Transaction_Count",title=f"Top Transactions in {top_transaction_state}-{top_transaction_quarter}",color="Quarter")
                    st.plotly_chart(fig,theme=None,use_container_width=True)
                    
# Creating Functions for Registered Users
    def reg_user_state(state_2):
        query=(f'''SELECT States,Year,Quarter,District_name,RegisteredUsers FROM map_users 
            WHERE States = '{state_2}' 
            ORDER BY States,Year,Quarter,District_name''')
        cur.execute(query)
        myconnection.commit()
        q=cur.fetchall()
        df=pd.DataFrame(q,columns=["States","Year","Quarter","District_Name","RegisteredUsers"])
        return df
    def reg_user_year(state_2,year_2):
            query=(f'''SELECT States,Year,Quarter,District_name,RegisteredUsers FROM map_users 
                WHERE States = '{state_2}' and Year='{year_2}'
                ORDER BY States,Year,Quarter,District_name''')
            cur.execute(query)
            myconnection.commit()
            q=cur.fetchall()
            df=pd.DataFrame(q,columns=["States","Year","Quarter","District_Name","RegisteredUsers"])
            return df
    def reg_user_district(state_2,year_2,district_2):
            query=(f'''SELECT States,Year,Quarter,District_name,RegisteredUsers FROM map_users 
                WHERE States = '{state_2}' and Year='{year_2}' and District_Name='{district_2}'
                ORDER BY States,Year,Quarter,District_name''')
            cur.execute(query)
            myconnection.commit()
            q=cur.fetchall()
            df=pd.DataFrame(q,columns=["States","Year","Quarter","District_Name","RegisteredUsers"])
            return df

    if choice=="Registered users":
        select = st.selectbox('View', ['Tabular view', 'Plotly View'], 0)
        if select == 'Tabular view':
                col1, col2, col3 = st.columns(3)
                with col1:
                        st.subheader("Select State")
                        state_list=['', 'andaman & nicobar islands', 'andhra pradesh', 'arunachal pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra & nagar haveli & daman & diu',
                                'delhi', 'goa', 'gujarat', 'haryana', 'himachal pradesh', 'jammu & kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya pradesh',
                                'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
                                'sikkim', 'tamil nadu', 'telangana', 'tripura', 'uttar pradesh', 'uttarakhand', 'west bengal']
                        selected_state=st.selectbox("States",state_list,0)
                with col2:
                        st.subheader("Select Year")
                        selected_year=st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022","2023"], 0)
                with col3:
                        st.subheader("Select District")
                        districts=Map_Trans_df["District_Name"].unique().tolist()
                        districts.sort()
                        selected_district=st.selectbox("search by",districts)
                if selected_state:
                        st.subheader(f'{selected_state}')
                        st.write(reg_user_state(selected_state))
                if selected_state and selected_year:
                        st.subheader(f'{selected_state}-{selected_year}')
                        st.write(reg_user_year(selected_state,selected_year))
                if selected_state and selected_year and selected_district:
                        st.subheader(f'{selected_state}-{selected_year}-{selected_district}')
                        st.write(reg_user_district(selected_state,selected_year,selected_district))
        else:
                col1,col2,col3=st.columns(3)
                with col1:
                        st.subheader("Select State")
                        state_list=['', 'andaman & nicobar islands', 'andhra pradesh', 'arunachal pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra & nagar haveli & daman & diu',
                                'delhi', 'goa', 'gujarat', 'haryana', 'himachal pradesh', 'jammu & kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya pradesh',
                                'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
                                'sikkim', 'tamil nadu', 'telangana', 'tripura', 'uttar pradesh', 'uttarakhand', 'west bengal']
                        selected_state=st.selectbox("States",state_list,0)
                        if selected_state:
                                df=reg_user_state(selected_state)
                                fig=px.bar(df,x="District_Name",y="RegisteredUsers",title=f"Regitered users in {selected_state}",color="Year")
                                st.plotly_chart(fig,theme=None,use_container_width=True)
                with col2:
                        st.subheader("Select Year")
                        selected_year=st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022","2023"], 0)
                        if selected_state and selected_year:
                                df=reg_user_year(selected_state,selected_year)
                                fig=px.bar(df,x="District_Name",y="RegisteredUsers",title=f"Registered users in {selected_state}-{selected_year}")
                                st.plotly_chart(fig,theme=None,use_container_width=True)
                with col3:
                        st.subheader("Select District")
                        districts=Map_Trans_df["District_Name"].unique().tolist()
                        districts.sort()
                        selected_district=st.selectbox("search by",districts)
                        if selected_district:
                                df=reg_user_district(selected_state,selected_year,selected_district)
                                fig=px.bar(df,x="Year",y="RegisteredUsers",title=f"Registered users in {selected_state}-{selected_year}-{selected_district}")
                                st.plotly_chart(fig,theme=None,use_container_width=True)
                                
# Creating Functions for Districts
    def district_state(state_3):
        query=(f'''select States,year,Quarter,District_Name,Transaction_Count,Transaction_Amount from map_transactions 
            where states='{state_3}'
            order by states,year,quarter,District_Name''')
        cur.execute(query)
        myconnection.commit()
        q=cur.fetchall()
        df=pd.DataFrame(q,columns=['States', 'Year','Quarter', 'District_Name', 'Transaction_Count','Transaction_Amount'])
        return df
    def district_year(state_3,year_3):
        query=(f'''select States,year,Quarter,District_Name,Transaction_Count,Transaction_Amount from map_transactions 
                where states='{state_3}' and year='{year_3}'
                order by states,year,quarter,District_Name''')
        cur.execute(query)
        myconnection.commit()
        q=cur.fetchall()
        df=pd.DataFrame(q,columns=['States', 'Year','Quarter', 'District_Name', 'Transaction_Count','Transaction_Amount'])
        return df
    if choice=="District":
        select = st.selectbox('View', ['Tabular view', 'Plotly View'], 0)
        if select == 'Tabular view':
                col1,col2=st.columns(2)
                with col1:
                        st.subheader("Select State")
                        state_list=['', 'andaman & nicobar islands', 'andhra pradesh', 'arunachal pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra & nagar haveli & daman & diu',
                                    'delhi', 'goa', 'gujarat', 'haryana', 'himachal pradesh', 'jammu & kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya pradesh',
                                    'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
                                    'sikkim', 'tamil nadu', 'telangana', 'tripura', 'uttar pradesh', 'uttarakhand', 'west bengal']
                        selected_state=st.selectbox("States",state_list,0)
                with col2:
                        st.subheader("Select year")
                        selected_year=st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022","2023"], 0)
                if selected_state:
                        col1,col2=st.columns(2)
                        with col1:
                                st.subheader(f'in {selected_state}')
                                st.write(district_state(selected_state))
                if selected_state and selected_year:
                        with col2:
                                st.subheader(f'in {selected_year}')
                                st.write(district_year(selected_state,selected_year))
        else:
                col1,col2=st.columns(2)
                with col1:
                        st.subheader("Select State")
                        state_list=['', 'andaman & nicobar islands', 'andhra pradesh', 'arunachal pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra & nagar haveli & daman & diu',
                                    'delhi', 'goa', 'gujarat', 'haryana', 'himachal pradesh', 'jammu & kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya pradesh',
                                    'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
                                    'sikkim', 'tamil nadu', 'telangana', 'tripura', 'uttar pradesh', 'uttarakhand', 'west bengal']
                        selected_state=st.selectbox("States",state_list,0)
                        if selected_state:
                                df=district_state(selected_state)
                                fig=px.bar(df,x="District_Name",y="Transaction_Amount",title="Users in {selected_state}")
                                st.plotly_chart(fig,theme=None,use_container_width=True)
                with col2:
                        st.subheader("Select Year")
                        selected_year=st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022","2023"], 0)
                        if selected_state and selected_year:
                                df=district_year(selected_state,selected_year)
                                fig=px.bar(df,x="District_Name",y="Transaction_Amount",title="Users in {selected_state}-{selected_year}")
                                st.plotly_chart(fig,theme=None,use_container_width=True)
                
# Geo Visualization Tab
if select=="Geo Visualization":
    def amount():
        file_path =  "C:/Users/muthu/Downloads/states_india.geojson"
        states_json=json.load(open(file_path,'r'))
        # data= json.load(states_json.content)
        state_name=[feature["properties"]["st_nm"] for feature in states_json["features"]]
        state_name.sort()

        state_df=pd.DataFrame({"States":state_name})

        list=[]

        for year in M_Users_df["Year"].unique():
            for quarter in A_Trans_df["Quarter"].unique():
                a_trans=A_Trans_df[(A_Trans_df["Year"]==year) & (A_Trans_df["Quarter"]==quarter)]   
                a_trans_1=a_trans[["States","Transaction_Amount"]]
                a_trans_1=a_trans_1.sort_values(by="States")
                a_trans_1["Year"]=year
                a_trans_1["Quarter"]=quarter 
                list.append(a_trans_1)
        overall_df=pd.concat(list)
        fig_trans=px.choropleth(overall_df,geojson=states_json,locations="States",featureidkey="properties.st_nm",
                                color="Transaction_Amount",color_continuous_scale="Sunsetdark",range_color=(0,4000000000),hover_name="States",
                                title="Transaction Amount",animation_frame="Year",animation_group="Quarter")
        fig_trans.update_geos(fitbounds="locations",visible=True)
        fig_trans.update_layout(width=600,height=700)
        fig_trans.update_layout(title_font={"size":25})
        return st.plotly_chart(fig_trans)

    def payment():
        a_trans=A_Trans_df[["Transaction_Type","Transaction_Count"]]
        a_trans_1=a_trans.groupby("Transaction_Type")["Transaction_Count"].sum()
        df_a_trans_1=pd.DataFrame(a_trans_1).reset_index()
        fig_payment=px.bar(df_a_trans_1,x="Transaction_Type",y="Transaction_Count",title="Transaction Type and Transaction Count",
                        color_discrete_sequence=px.colors.sequential.Redor_r)
        fig_payment.update_layout(width=600,height=500)
        st.plotly_chart(fig_payment)
        
    def count():
        file_path =  "C:/Users/muthu/Downloads/states_india.geojson"
        states_json=json.load(open(file_path,'r'))
        state_name=[feature["properties"]["st_nm"] for feature in states_json["features"]]
        state_name.sort()

        state_df=pd.DataFrame({"States":state_name})

        list=[]
        
        for year in M_Users_df["Year"].unique():
            for quarter in A_Trans_df["Quarter"].unique():
                a_trans=A_Trans_df[(A_Trans_df["Year"]==year) & (A_Trans_df["Quarter"]==quarter)]   
                a_trans_1=a_trans[["States","Transaction_Count"]]
                a_trans_1=a_trans_1.sort_values(by="States")
                a_trans_1["Year"]=year
                a_trans_1["Quarter"]=quarter 
                list.append(a_trans_1)
        overall_df=pd.concat(list)
        fig_trans=px.choropleth(overall_df,geojson=states_json,locations="States",featureidkey="properties.st_nm",
                                color="Transaction_Count",color_continuous_scale="Sunsetdark",range_color=(0,4000000000),hover_name="States",
                                title="Transaction Count",animation_frame="Year",animation_group="Quarter")
        fig_trans.update_geos(fitbounds="locations",visible=True)
        fig_trans.update_layout(width=600,height=700)
        fig_trans.update_layout(title_font={"size":25})
        return st.plotly_chart(fig_trans)

    def p_amount():
        a_trans=A_Trans_df[["Transaction_Type","Transaction_Amount"]]
        a_trans_1=a_trans.groupby("Transaction_Type")["Transaction_Amount"].sum()
        df_a_trans_1=pd.DataFrame(a_trans_1).reset_index()
        fig_payment=px.bar(df_a_trans_1,x="Transaction_Type",y="Transaction_Amount",title="Transaction Type and Transaction Amount",
                        color_discrete_sequence=px.colors.sequential.Redor_r)
        fig_payment.update_layout(width=600,height=500)
        st.plotly_chart(fig_payment)
        
    def states(state):
        m_user=M_Users_df[["States","District_Name","RegisteredUsers"]]
        m_user_1=m_user.loc[(m_user["States"]==state)]
        m_user_2=m_user_1[["District_Name","RegisteredUsers"]]
        m_user_3=m_user_2.groupby("District_Name")["RegisteredUsers"].sum()
        m_user_4=pd.DataFrame(m_user_3).reset_index()
        fig_m_user= px.bar(m_user_4, x= "District_Name", y= "RegisteredUsers", title= "DISTRICTS and REGISTERED USER",
                    color_discrete_sequence=px.colors.sequential.Bluered_r)
        fig_m_user.update_layout(width= 1000, height= 500)
        return st.plotly_chart(fig_m_user)

    def transaction_year(selected_year):
        file_path =  "C:/Users/muthu/Downloads/states_india.geojson"
        states_json=json.load(open(file_path,'r'))
        state_name=[feature["properties"]["st_nm"] for feature in states_json["features"]]
        state_name.sort()
        
        year=int(selected_year)
        aty=A_Trans_df[["States","Year","Transaction_Amount"]]
        aty1=aty.loc[(A_Trans_df["Year"]==year)]
        aty2=aty1.groupby("States")["Transaction_Amount"].sum()
        aty3=pd.DataFrame(aty2).reset_index()
        
        fig_at_year=px.choropleth(aty3,geojson=states_json,locations="States",featureidkey="properties.st_nm",
                                color="Transaction_Amount",color_continuous_scale="rainbow",range_color=(0,800000000000),
                                title="Transaction_Amount and States",hover_name="States")
        
        fig_at_year.update_geos(fitbounds="locations",visible=True)
        fig_at_year.update_layout(width=600,height=700)
        fig_at_year.update_layout(title_font={"size":25})
        return st.plotly_chart(fig_at_year)

    def payment_count_year(selected_year):
        year=int(selected_year)
        a_p=A_Trans_df[["Transaction_Type","Transaction_Count"]]
        a_p1=a_p.loc[(A_Trans_df["Year"]==year)]
        a_p2=a_p1.groupby("Transaction_Type")["Transaction_Count"].sum()
        a_p3=pd.DataFrame(a_p2).reset_index()
        
        fig_apc= px.bar(a_p3,x= "Transaction_Type", y= "Transaction_Count", title= "PAYMENT COUNT and PAYMENT TYPE",
                        color_discrete_sequence=px.colors.sequential.Brwnyl_r)
        fig_apc.update_layout(width=600, height=500)
        return st.plotly_chart(fig_apc)

    def transaction_count_year(selected_year):
        file_path =  "C:/Users/muthu/Downloads/states_india.geojson"
        states_json=json.load(open(file_path,'r'))
        state_name=[feature["properties"]["st_nm"] for feature in states_json["features"]]
        state_name.sort()
        
        year=int(selected_year)
        tcy=A_Trans_df[["States","Year","Transaction_Count"]]
        tcy_1=tcy.loc[(A_Trans_df["Year"]==year)]
        tcy_2=tcy_1.groupby("States")["Transaction_Count"].sum()
        tcy_3=pd.DataFrame(tcy_2).reset_index()
        
        fig_tcy=px.choropleth(tcy_3,geojson=states_json,locations="States",featureidkey= "properties.st_nm",
                            color="Transaction_Count",color_continuous_scale="rainbow",range_color=(0,3000000000),
                            title="TRANSACTION COUNT and STATES",hover_name="States")
        fig_tcy.update_geos(fitbounds= "locations", visible= True)
        fig_tcy.update_layout(width=600, height= 700)
        fig_tcy.update_layout(title_font={"size":25})
        return st.plotly_chart(fig_tcy)

    def payment_amount(selected_year):
        year= int(selected_year)
        pay = A_Trans_df[["Year", "Transaction_Type", "Transaction_Amount"]]
        pay1= pay.loc[(A_Trans_df["Year"]==year)]
        pay2= pay1.groupby("Transaction_Type")["Transaction_Amount"].sum()
        pay3= pd.DataFrame(pay2).reset_index()

        fig_pay= px.bar(pay3, x="Transaction_Type", y= "Transaction_Amount", title= "PAYMENT TYPE and PAYMENT AMOUNT",
                        color_discrete_sequence=px.colors.sequential.Burg_r)
        fig_pay.update_layout(width=600, height=500)
        return st.plotly_chart(fig_pay)

    def reg_state_user(selected_year,state):
        year= int(selected_year)
        m_user= M_Users_df[["States", "Year", "District_Name", "RegisteredUsers"]]
        m_user1= m_user.loc[(M_Users_df["States"]==state)&(M_Users_df["Year"]==year)]
        m_user2= m_user1.groupby("District_Name")["RegisteredUsers"].sum()
        m_user3= pd.DataFrame(m_user2).reset_index()

        fig_muser= px.bar(m_user3, x= "District_Name", y="RegisteredUsers", title="DISTRICTS and REGISTERED USER",
                        color_discrete_sequence=px.colors.sequential.Cividis_r)
        fig_muser.update_layout(width= 600, height= 500)
        return st.plotly_chart(fig_muser)
        
    def reg_state_trans(selected_year,state):
        year= int(selected_year)
        m_ts= M_Users_df[["States", "Year","District_Name", "Transaction_Amount"]]
        m_ts_1= m_ts.loc[(M_Users_df["States"]==state)&(M_Users_df["Year"]==year)]
        m_ts_2= m_ts_1.groupby("District_Name")["Transaction_Amount"].sum()
        m_ts_3= pd.DataFrame(m_ts_2).reset_index()

        fig_mts= px.bar(m_ts_3, x= "District_Name", y= "Transaction_Amount", title= "DISTRICT and TRANSACTION AMOUNT",
                        color_discrete_sequence= px.colors.sequential.Darkmint_r)
        fig_mts.update_layout(width= 600, height= 500)
        return st.plotly_chart(fig_mts)

    # st.set_page_config(layout= "wide")
    st.title("Phonepe Data :violet[GEO-VISUALIZATION]")
    tab1,tab2,tab3=st.tabs(["Choropleth Visualization","Table View","Categories"])
    with tab1:
        selected_year = st.selectbox("select the Year",("All", "2018", "2019", "2020", "2021", "2022", "2023"))
        if selected_year== "All":
            col1,col2=st.columns(2)
            with col1:
                amount()
                payment()
            with col2:
                count()
                p_amount()
                
            state=st.selectbox("selecet the state",('Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
                                                    'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                                    'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa',
                                                    'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
                                                    'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep',
                                                    'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
                                                    'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan',
                                                    'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                                    'Uttarakhand', 'West Bengal'))
            
            states(state)
        else:
            col1,col2=st.columns(2)
            with col1:
                transaction_year(selected_year)
                payment_count_year(selected_year)
            with col2:
                transaction_count_year(selected_year)
                payment_amount(selected_year)
                
                state=st.selectbox("selecet the state",('Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
                                                    'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                                    'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa',
                                                    'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
                                                    'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep',
                                                    'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
                                                    'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan',
                                                    'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                                    'Uttarakhand', 'West Bengal'))
                reg_state_user(selected_year,state)
                reg_state_trans(selected_year,state)
# Overview Tab 
if select =="Overview":
    st.title("Overview of the :violet[Project]")
    st.header("Project :violet[Title:]")
    st.header(":violet[Phonepe Pulse Data Visualization and Exploration]: A User-Friendly Tool Using Streamlit and Plotly")
    
    st.subheader("Used :violet[Technologies]")
    st.write("1. Github Cloning")
    st.write("2. Python")
    st.write("3. Pandas")
    st.write("4. MySQL")
    st.write("5. MySQL connector Python")
    st.write("6. Streamlit and Plotly")
    
    st.subheader("Requirement:")
    st.write("The Phonepe pulse Github repository contains a large amount of data related to various metrics and statistics. The goal is to extract this data and process it to obtain insights and information that can be visualized in a user-friendly manner.")
    
    st.header("Process in this :violet[Project:]")
    st.header("Data :violet[Extraction:]")
    st.write("Clone the Github using scripting to fetch the data from the Phonepe pulse Github repository and store it in a suitable format such as CSV or JSON.")
    st.header("Data :violet[Transformation:]")
    st.write("Use a scripting language such as Python, along with libraries such as Pandas, to manipulate and pre-process the data. This may include cleaning the data, handling missing values, and transforming the data into a format suitable for analysis and visualization.")
    st.header(" Database :violet[Insertion:]")
    st.write("Use the mysql-connector-python library in Python to connect to a MySQL database and insert the transformed data using SQL commands.")
    st.header("Dashboard :violet[Creation:]")
    st.write("Use the Streamlit and Plotly libraries in Python to create an interactive and visually appealing dashboard. Plotly's built-in geo map functions can be used to display the data on a map and Streamlit can be used to create a user-friendly interface with multiple dropdown options for users to select different facts and figures to display.")
    st.header("Data :violet[Retrieval:]")
    st.write("Use the mysql-connector-python library to connect to the MySQL database and fetch the data into a Pandas dataframe. Use the data in the dataframe to update the dashboard dynamically.")
    st.header("Deploy:violet[ment:]")
    st.write("Ensure the solution is secure, efficient, and user-friendly. Test the solution thoroughly and deploy the dashboard publicly, making it accessible to users.")
    st.header("Result of the :violet[Project]")
    multi='''The result of this project is a live geo visualization dashboard that displays
            information and insights from the Phonepe pulse Github repository in an interactive
            and visually appealing manner. The dashboard containst 10 different
            dropdown options for users to select different facts and figures to display. The data
            can be stored in a MySQL database for efficient retrieval and the dashboard is
            dynamically updated to reflect the latest data.
            Users can able to access the dashboard from a web browser and easily navigate
            the different visualizations and facts and figures displayed. The dashboard was
            provided valuable insights and information about the data in the Phonepe pulse
            Github repository, making it a valuable tool for data analysis and decision-making.
            Overall, the result of this project is a comprehensive and user-friendly solution
            for extracting, transforming, and visualizing data from the Phonepe pulse Github
            repository.'''
    st.markdown(multi)
    st.write(":copyright: Copyright UI owned by palemravichandra")