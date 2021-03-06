# Open Sublime text editor, create a new Python file, copy the following code in it and save it as 'census_app.py'.

# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


@st.cache()
def load_data():
    # Load the Adult Income dataset into DataFrame.

    df = pd.read_csv("adult.csv",
                     header=None)
    df.head()

    # Rename the column names in the DataFrame using the list given above.

    # Create the list
    column_name = ['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation',
                   'relationship', 'race', 'gender', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
                   'income']

    # Rename the columns using 'rename()'
    for i in range(df.shape[1]):
        df.rename(columns={i: column_name[i]}, inplace=True)

    # Print the first five rows of the DataFrame
    df.head()

    # Replace the invalid values ' ?' with 'np.nan'.

    df['native-country'] = df['native-country'].replace(' ?', np.nan)
    df['workclass'] = df['workclass'].replace(' ?', np.nan)
    df['occupation'] = df['occupation'].replace(' ?', np.nan)

    # Delete the rows with invalid values and the column not required

    # Delete the rows with the 'dropna()' function
    df.dropna(inplace=True)

    # Delete the column with the 'drop()' function
    df.drop(columns='fnlwgt', axis=1, inplace=True)

    return df


census_df = load_data()
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Census App")
st.sidebar.title("Menu")
if st.sidebar.checkbox("Click here to see raw data."):
    st.dataframe(census_df)
st.sidebar.subheader("Data Visualisation")
plot_list = st.sidebar.multiselect('Select plots here', options=["Income", "Gender", "hours per week vs gender", "hours per week vs income", "workclass"])

if 'Income' in plot_list:
    st.subheader("Distribution of Income Group")
    plt.figure(figsize=(12, 6))
    plt.pie(census_df['income'].value_counts(),labels=census_df['income'].value_counts().index, autopct="%1.2f%%",
            startangle=30)
    st.pyplot()
if "Gender" in plot_list:
    st.subheader("Distribution of Gender")
    plt.figure(figsize=(12, 6))
    plt.pie(census_df['gender'].value_counts(), labels=census_df['gender'].value_counts().index, autopct="%1.2f%%",
            startangle=30)
    st.pyplot()
if "hours per week vs gender" in plot_list:
    st.subheader("Hours per week vs gender")
    plt.figure(figsize=(12, 6))
    ax = sns.boxplot(x='hours-per-week', y='gender', data=census_df, orient='h', palette="Set1")
    st.pyplot()
if "hours per week vs income" in plot_list:
    st.subheader("Hours per week vs income")
    plt.figure(figsize=(12, 6))
    ax = sns.boxplot(x='hours-per-week', y='income', data=census_df, orient='h', palette="Set3")

    st.pyplot()
if "workclass" in plot_list:
    st.subheader("Work class")
    plt.figure(figsize=(12, 6))
    plt.pie(census_df['workclass'].value_counts(), labels=census_df['workclass'].value_counts().index, autopct="%1.2f%%",
            startangle=30)
    st.pyplot()


