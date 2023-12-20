
# PhonePe Pulse Data Visualization using Python SQL Plotly and Streamlit

The Phonepe pulse Github repository contains a large amount of data related to
various metrics and statistics. The goal is to extract this data and process it to obtain
insights and information that can be visualized in a user-friendly manner.

* Extract data from the Phonepe pulse Github repository through scripting and clone it.
* Transform the data into a suitable format and perform any necessary cleaning and pre-processing steps.
* Insert the transformed data into a MySQL database for efficient storage and retrieval.
* Create a live geo visualization dashboard using Streamlit and Plotly in Python to display the data in an interactive and visually appealing manner.
* Fetch the data from the MySQL database to display in the dashboard.
* Provide at least 10 different dropdown options for users to select different facts and figures to display on the dashboard.

## Steps Followed
### Data Extraction:
Clone the Github using scripting to fetch the data from the
Phonepe pulse Github repository and store it in a suitable format such as CSV or JSON.  

### Data transformation:
Use a scripting language such as Python, along with
libraries such as Pandas, to manipulate and pre-process the data. This may
include cleaning the data, handling missing values, and transforming the data
into a format suitable for analysis and visualization.

### Database insertion:
Use the "mysql-connector-python" library in Python to
connect to a MySQL database and insert the transformed data using SQL commands.

### Dashboard creation:
 Use the Streamlit and Plotly libraries in Python to create
an interactive and visually appealing dashboard. Plotly's built-in geo map
functions can be used to display the data on a map and Streamlit can be used
to create a user-friendly interface with multiple dropdown options for users to
select different facts and figures to display.

### Data retrieval:
Use the "mysql-connector-python" library to connect to the
MySQL database and fetch the data into a Pandas dataframe. Use the data in
the dataframe to update the dashboard dynamically.

### 








## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`import pandas as pd`

`import os`

`import json`

`import plotly.express as px`

`import pymysql`

`from PIL import Image`

`import streamlit as st`

`from streamlit_option_menu import option_menu`

`import numpy as np`


## Tech Stack

**Client:** Python, Plotly, Streamlit, Pandas and Github Cloning

**Data Base:** MySQL

