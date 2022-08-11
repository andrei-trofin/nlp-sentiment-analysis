<h1 style="text-align: center"> NLP Sentiment Analysis 🧠</h1>

## Business Case

This project has been created by going through the tutorial at https://www.youtube.com/watch?v=VyDmQggfsZ0
and adapting it to fit my work style.

In this project written sentences are analyzed and classified as being negative, positive or in-between.
This type of application is useful for any type of app to improve its marketing.
For example, we can monitor the good and bad reviews in an A/B test environment
and modify our product accordingly.

There emotions in this dataset range from 0 = negative, to 4 = positive, while 2
= neutral. The dataset was downloaded from [kaggle](https://www.kaggle.com/datasets/kazanova/sentiment140).


## Table of Contents
<details open>
<summary>Show/Hide</summary>

1. [File/Folder descriptions](#1-filefolder-descriptions)
2. [Data preparation](#2-data-preparation)
3. [EDA and clustering](#3-eda-and-clustering)
    * [3.1 Exploratory data analysis](#31-exploratory-data-analysis)
    * [3.2 Clustering](#32-clustering)
4. [Web application](#4-web-application)
5. [What did I learn?](#5-what-did-i-learn)
6. [Conclusion](#6-conclusion)

    * [5.2 Future improvements](#52-future-improvements)
</details>

## 1. File/Folder descriptions

<details open>
<summary>Show/Hide</summary>

* **data**: folder in which all data is stored
    * Economy.xlsx: excel formatted data about economy of countries from https://data.worldbank.org/


* **notebooks**: where the jupyter notebooks and adjacent python scripts are stored
  * **1. Data Preprocessing.ipynb**: notebook used for preprocessing all data about countries
  * **python-scripts**: folder which contains python scripts used in notebooks and tests for functions where possible
    * **development**: folder in which all python scripts reside
      * **preprocessing_functions.py**: script containing functions used in notebooks
    * **test**: folder containing test modules
      * **test_preprocessing_functions.py**: unit test module for functions in preprocessing_functions.py

* **research.txt**: text file I used to quickly find the most important factors for choosing a country where to move to


</details>


## 2. Data preparation

<details open>
<summary>Show/Hide</summary>


<p align="center">
  <img src="images/world-happiness.png" width=700/>
</p>
<br>
<br>



</details>


## 3. EDA and clustering

<details open>
<summary>Show/Hide</summary>



</details>


### 3.1 Exploratory data analysis

<details open>
<summary>Show/Hide</summary>



<p align="center">
  <img src="./images/correlation.png" width="800"/>
</p>
<br>
<br>

</details>


### 3.2 Clustering

<details open>
<summary>Show/Hide</summary>



<p align="center">
  <img src="./images/PCA.png" width="500"/>
</p>
<br>
<br>



</details>


## 4. Web application

<details open>
<summary>Show/Hide</summary>


<p align="center">
  <img src="./images/webapp-1.png" width="700"/>
</p>
<br>
<br>

<p align="center">
  <img src="./images/webapp-2.png" width="700"/>
</p>
<br>
<br>



Steps to follow if you want to run the application on your machine:

1. Pull this repository from git
2. Make sure you have python and pip installed
3. Install streamlit and numpy using pip
4. Go to the client directory of this project, open a command line and type
"streamlit run app.py"
5. The web app should be accessible now at http://localhost:8501 or the provided link in your console

</details>



### 5 What did I learn?

<details open>
<summary>Show/Hide</summary>


</details>

## 6. Conclusion

<details open>
<summary>Show/Hide</summary>


</details>
