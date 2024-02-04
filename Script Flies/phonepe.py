import os
import json
import pandas as pd
import streamlit as st
import plotly.express as px
import mysql.connector
import sqlalchemy
import matplotlib.pyplot as plt
from PIL import Image
from streamlit_option_menu import option_menu




# Read your CSV files
agg_insurance_df = pd.read_csv('agg_insurance.csv')
agg_transaction_df = pd.read_csv('agg_transaction.csv')
agg_user_df = pd.read_csv('agg_user.csv')
map_insurance_df = pd.read_csv('map_insurance.csv')
map_transaction_df = pd.read_csv('map_transaction.csv')
map_user_df = pd.read_csv('map_user.csv')
top_insurance_df = pd.read_csv('top_insurance.csv')
top_transaction_df = pd.read_csv('top_transaction.csv')
top_user_df = pd.read_csv('top_user.csv')

# Streamlit App
st.title(':violet[PhonePe Data Visualization]')



# Sidebar
selected_data = st.radio(':green[Fetched Data From MYSQL Database:]', ['Aggregated Insurance', 'Aggregated Transaction', 'Aggregated User',
                                                               'Map Insurance', 'Map Transaction', 'Map User',
                                                               'Top Insurance', 'Top Transaction', 'Top User'])

# Display selected data
if selected_data == 'Aggregated Insurance':
    st.header(':violet[Aggregated Insurance Data]')
    st.write(agg_insurance_df)

elif selected_data == 'Aggregated Transaction':
    st.header(':violet[Aggregated Transaction Data]')
    st.write(agg_transaction_df)  

elif selected_data == 'Aggregated User':
    st.header(':violet[Aggregated User Data]')
    st.write(agg_user_df)        

elif selected_data == 'Map Insurance':
    st.header(':violet[Map Insurance Data]')
    st.write(map_insurance_df)    

elif selected_data == 'Map Transaction':
    st.header(':violet[Map Transaction Data]')
    st.write(map_transaction_df)    

elif selected_data == 'Map User':
    st.header(':violet[Map User Data]')
    st.write(map_user_df)    

elif selected_data == 'Top Insurance':
    st.header(':violet[Top Insurance Data]')
    st.write(top_insurance_df)    

elif selected_data == 'Top Transaction':
    st.header(':violet[Top Transaction Data]')
    st.write(top_transaction_df)    

elif selected_data == 'Top User':
    st.header(':violet[Top User Data]')
    st.write(top_user_df)       


# Sidebar

with st.sidebar:
    st.title(":violet[Phonepe Pulse Data Visualization and Exploration:A User-Friendly Tool Using Streamlit and Plotly]")
    st.markdown("## Comprehensive Data Exploration:")
    st.write("- PhonePe Pulse offers a user-friendly tool for in-depth data exploration, leveraging the power of Streamlit and Plotly.")
    st.write("- Users can dynamically visualize and analyze data through interactive features, providing a comprehensive understanding of key metrics and trends.")
    st.markdown("## Streamlined User Interface:")
    st.write("- The tool ensures an intuitive and user-friendly experience, allowing individuals to navigate and interact effortlessly with data visualizations.")
    st.write("- Through Streamlit's capabilities, users can explore complex datasets seamlessly, enhancing accessibility for a diverse audience.")
    st.markdown("## Dynamic Insights with Plotly:")
    st.write("- Utilizing Plotly, PhonePe Pulse translates data into dynamic and engaging visualizations, fostering a deeper comprehension of insights.")
    st.write("- The integration of Streamlit and Plotly creates a powerful synergy, empowering users to interpret and extract valuable information from the data efficiently.")



selected_data = st.selectbox(':green[Insurance Data Based Analysis:]', ['Aggregated Insurance',
                                                                'Top Insurance'])

if selected_data == 'Aggregated Insurance':

    # Aggregated Insurance Data
    st.header(':red[Aggregated Insurance Data]')

    st.markdown("## Overview of Aggregated Insurance Transactions:")
    st.write("- An overview of aggregated insurance transactions provides a consolidated summary of key metrics and trends within the insurance transaction dataset.")
    st.write("- Aggregating insurance transactions allows for efficient analysis, revealing patterns, anomalies, and valuable insights that might be obscured in individual transaction record.")
    st.write("- The summarized view of insurance transactions offers strategic decision support by highlighting critical information such as transaction volumes, claim amounts, and policy activities.")
    st.write("- Stakeholders can use this overview to make informed decisions regarding business strategies, customer satisfaction, and risk mitigation within the insurance domain.")               

    # Visualization using Plotly - Bar Chart
    fig_agg_insurance_bar = px.bar(
        agg_insurance_df,
        x='States',
        y='Transction_Amount',
        color='Transction_Type',
        labels={'Transction_Amount': 'Transaction Amount'},
        title='Insights on Transaction Amounts Across States by Transaction Type',
        color_discrete_map={'Transction_Type': 'Viridis'}
    )

    # Display the bar chart
    st.plotly_chart(fig_agg_insurance_bar)


    
elif selected_data == 'Top Insurance':

    # Aggregated Insurance Data
    st.header(':red[Top Insurance Data]')

    st.markdown("## Overview of Top Insurance Transactions:")
    st.write("- The overview of top insurance transactions involves the identification and emphasis on transactions with significant impact, whether in terms of policy premiums, claim amounts, or other crucial metrics.")
    st.write("- Examining the top insurance transactions provides insights into transactional patterns, trends, and anomalies, shedding light on the most influential aspects of the insurance portfolio.")
    st.write("- Understanding the characteristics of these transactions aids in strategic decision-making, risk assessment, and policy optimization.")
    st.write("- Prioritizing based on transaction significance facilitates efficient resource allocation, targeted improvements, and strategic decision-making within the insurance domain.")                 
                           

    # Visualization using Plotly - Violin Plot
    fig_top_insurance_violin = px.violin(
        top_insurance_df,
        x='States',
        y='Transction_Count',
        color='Years',
        labels={'Transction_Count': 'Transaction Count'},
        title='Distribution of Transaction Count Across States for Top Insurance',
    )

    # Display the violin plot
    st.plotly_chart(fig_top_insurance_violin)


selected_data = st.selectbox(':green[Transaction Data Based Analysis:]', ['Aggregated Transaction',
                                                                  'Top Transaction'])

if selected_data == 'Aggregated Transaction':

    # Aggregated Insurance Data
    st.header(':red[Aggregated Transaction Data]')

    st.markdown("## Overview of Aggregated Transactions:")
    st.write("- Aggregated transaction data refers to a condensed representation of individual transactions, presenting a consolidated view of key metrics.")
    st.write("- Aggregating transaction data allows for efficient analysis, revealing patterns, trends, and insights that might be obscured in individual transaction records.")
    st.write("- By condensing transaction details into meaningful summaries, stakeholders can quickly grasp the overall performance and make informed business decisions.")
                          

    # Visualization using Plotly - Bar Chart
    fig_agg_transaction_bar = px.bar(
        agg_transaction_df,
        x='States',
        y='Transction_Amount',
        color='Transction_Type',
        labels={'Transction_Amount': 'Transaction Amount'},
        title='Insights on Transaction Amounts Across States by Transaction Type',
        color_discrete_map={'Transction_Type': 'Copper'}
    )

    # Display the bar chart
    st.plotly_chart(fig_agg_transaction_bar)


elif selected_data == 'Top Transaction':

    # Aggregated Insurance Data
    st.header(':red[Top Transaction Data]')

    st.markdown("## Overview of Top Transactions:")
    st.write("- The overview of top transactions involves identifying and highlighting transactions with the highest values or significant impact.")
    st.write("- Examining the top transactions provides insights into patterns, trends, or anomalies within the dataset.")
    st.write("- Understanding the characteristics of these transactions aids in strategic decision-making and risk management.")
    st.write("- A summary of top transactions enhances visibility, allowing stakeholders to quickly grasp the most impactful aspects of financial or operational data.")      


    # Visualization using Plotly - Violin Plot
    fig_top_transaction_violin = px.violin(
        top_transaction_df,
        x='States',
        y='Transction_Count',
        color='Years',
        labels={'Transction_Count': 'Transaction Count'},
        title='Distribution of Transaction Count Across States for Top Insurance',
    )

    # Display the violin plot
    st.plotly_chart(fig_top_transaction_violin)    


selected_data = st.selectbox(':green[User Data Based Analysis:]', ['Aggregated User',
                                                               'Top User'])
    


if selected_data == 'Aggregated User':

    # Aggregated User Data
    st.header(':red[Aggregated User Data]')

    st.markdown("## Overview of Aggregated User:")
    st.write("- An overview of aggregated user data with brands involves consolidating information about user interactions, preferences, or behaviors specific to different brands.")
    st.write("- Analyzing aggregated user data by brands reveals patterns and trends related to brand loyalty, user engagement, and interactions with specific products or services.")
    st.write("- The overview empowers decision-makers to strategically manage brands by identifying strengths, weaknesses, and opportunities based on user interactions.")
    st.write("- This information aids in tailoring brand experiences, improving customer satisfaction, and aligning business strategies with user preferences.")
                                        
    # Visualization using Plotly - Bar Chart
    fig_agg_user_bar = px.bar(
    agg_user_df,
    x='States',
    y='Transction_Count',  # Correct column name here
    color='Brands',
    labels={'Transction_Count': 'Transaction Count'},
    title='Insights on Transaction Counts Across States by Brands',
    color_discrete_map={'Brands': 'gold'}
    )

    # Display the bar chart
    st.plotly_chart(fig_agg_user_bar)



elif selected_data == 'Top User':

    # Top User Data
    st.header(':red[Top User Data]')

    st.markdown("## Overview of Top User:")
    st.write("- An overview of top users involves identifying and spotlighting users with significant value, often determined by factors such as engagement, activity, or contribution.")
    st.write("- Examining top users provides insights into their behavior patterns, preferences, and interactions within a platform or service.")
    st.write("- The overview empowers decision-makers to strategically manage user relationships by identifying key demographics, preferences, and trends among top users.")
    st.write("- This information supports personalized marketing initiatives, targeted user engagement, and the optimization of products or services to meet the needs of the most valuable user segment.")

                            

    # Visualization using Plotly - Violin Plot
    fig_top_user_violin = px.violin(
    top_user_df,
    x='States',
    y='RegisteredUsers',  # Correct column name here
    color='Years',
    labels={'RegisteredUsers': 'Registered Users'},
    title='Distribution of Registered Users Across States for Top Users',
    )

    # Display the violin plot
    st.plotly_chart(fig_top_user_violin)
  

selected_data = st.selectbox('GeoInsights: Mapping Insurance, Transaction, and User Data', ['Geo Visualzation'
                                                               ])
mydb = mysql.connector.connect(
            host="localhost",
            user="paart",
            password="2352",
            database="Phonepe_data",
            port="3306"
        )


# Creating a cursor to execute SQL queries
    
cursor = mydb.cursor()
if selected_data == "Geo Visualzation":  
        Type = st.selectbox("**Type**", ("Insurance","Transactions", "Users"))
        colum1,colum2= st.columns([1,1],gap="large")
        with colum1:
            Year = st.slider("**Year**", min_value=2018, max_value=2023)
        with colum2:
            Quarter = st.slider("Quarter", min_value=1, max_value=4) 
        
        # Overall State Data - TRANSACTIONS AMOUNT - INDIA MAP - Insurance
        if Type == "Insurance": 
            select = st.radio("Select Type:",("Amount","Count"))
            if select == "Amount":
                st.markdown("## :violet[Overall Transaction Amount]")
                cursor.execute(f'''select states,sum(Transction_Count) as Total_Transactions, sum(Transaction_Amount) as Total_amount 
                from map_transaction where years = {Year} and quarter = {Quarter} 
                group by states order by states''')
                df1 = pd.DataFrame(cursor.fetchall(),columns= ['States', 'Total_Transactions', 'Total_amount'])
                df2 = pd.read_csv(r"C:/Users/paart/Visual Studio Code/map_insurance.csv")
                df1.State = df2

                fig = px.choropleth(df1, geojson=r"https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations='States',
                color='Total_amount',
                color_continuous_scale='viridis') 

                fig.update_geos(fitbounds="locations", visible=False)
                st.plotly_chart(fig, use_container_width=True)
        
         # Overall State Data - TRANSACTIONS COUNT - INDIA MAP
            if select == "Count":
                st.markdown("## :violet[Overall Transaction Count]")
                cursor.execute(f'''select states, sum(Transction_Count) as Total_Transactions, sum(Transaction_Amount) as Total_amount
                            from map_transaction where years = {Year} and quarter = {Quarter} 
                            group by states order by states''')
                df1 = pd.DataFrame(cursor.fetchall(),columns= ['States', 'Total_Transactions', 'Total_amount'])
                df2 = pd.read_csv(r"C:/Users/paart/Visual Studio Code/map_insurance.csv")
                df1.Total_Transactions = df1.Total_Transactions.astype(int)
                df1.State = df2

                fig = px.choropleth(df1, geojson=r"https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='States',
                            color='Total_Transactions',
                            color_continuous_scale='plasma')

                fig.update_geos(fitbounds="locations", visible=False)
                st.plotly_chart(fig,use_container_width=True)
        # Overall State Data - TRANSACTIONS AMOUNT - INDIA MAP 
        if Type == "Transactions": 
            select = st.radio("Select Type:",("Amount","Count"))
            if select == "Amount":
                st.markdown("## :violet[Overall Transaction Amount]")
                cursor.execute(f'''select states,sum(Transction_Count) as Total_Transactions, sum(Transaction_Amount) as Total_amount 
                from map_transaction where years = {Year} and quarter = {Quarter} 
                group by states order by states''')
                df1 = pd.DataFrame(cursor.fetchall(),columns= ['States', 'Total_Transactions', 'Total_amount'])
                df2 = pd.read_csv(r"C:/Users/paart/Visual Studio Code/map_transaction.csv")
                df1.State = df2

                fig = px.choropleth(df1, geojson=r"https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations='States',
                color='Total_amount',
                color_continuous_scale='viridis') 

                fig.update_geos(fitbounds="locations", visible=False)
                st.plotly_chart(fig, use_container_width=True)
        
         # Overall State Data - TRANSACTIONS COUNT - INDIA MAP
            if select == "Count":
                st.markdown("## :violet[Overall Transaction Count]")
                cursor.execute(f'''select states, sum(Transction_Count) as Total_Transactions, sum(Transaction_Amount) as Total_amount
                            from map_transaction where years = {Year} and quarter = {Quarter} 
                            group by states order by states''')
                df1 = pd.DataFrame(cursor.fetchall(),columns= ['States', 'Total_Transactions', 'Total_amount'])
                df2 = pd.read_csv(r"C:/Users/paart/Visual Studio Code/map_transaction.csv")
                df1.Total_Transactions = df1.Total_Transactions.astype(int)
                df1.State = df2

                fig = px.choropleth(df1, geojson=r"https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='States',
                            color='Total_Transactions',
                            color_continuous_scale='plasma')

                fig.update_geos(fitbounds="locations", visible=False)
                st.plotly_chart(fig,use_container_width=True)    

        #Overall State Data - RegisteredUser
        if Type == "Users": 
            st.markdown("## :violet[Overall State - Registered Users]")
            cursor.execute(f'''select states, sum(RegisteredUsers)
                        from map_user where years = {Year} and quarter = {Quarter} 
                        group by states order by states''')
            df1 = pd.DataFrame(cursor.fetchall(),columns= ['States', 'RegisteredUsers'])
            df2 = pd.read_csv(r"C:/Users/paart/Visual Studio Code/map_user.csv")
            df1.RegisteredUsers = df1.RegisteredUsers.astype(int)
            df1.State = df2

            fig = px.choropleth(df1, geojson=r"https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='States',
                        color='RegisteredUsers',
                        color_continuous_scale='rdpu')

            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig,use_container_width=True)        