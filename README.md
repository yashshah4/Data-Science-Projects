# Data-Science-projects
A collection of interesting Data Science Projects that highlight the foundational understanding of SQL, Python and it's libraries 

## MACHINE LEARNING PROJECTS

1. Supervised Machine Learning Project - Classifying handwritten digits into its class using KNN 

Skills tested: Pandas, Matplotlib, SciKit learn, Machine Learning, K-Nearest Neighbors classifier

Project description :In this project we work with the Scikit learn's in-built digits dataset which is a dataset of handwritten images rendered into pixels and then stored in an array. We use the image data to classify it into ten different classes from 0-9 based on the image. We also show how to choose the neighbors such that the model accuracy is the highest. 

2. Supervised Machine Learning Project - Predicting credit card approval using logistic regression classification model

Skills tested: Pandas, Supervised Learning with scikit-learn, Machine Learning, Logistic regression, grid search parameter tuning method

Project description :Commercial banks receive a lot of applications for credit cards. Many of them get rejected for many reasons, like high loan balances, low income levels, or too many inquiries on an individual's credit report, for example. Manually analyzing these applications is mundane, error-prone, and time-consuming (and time is money!). Luckily, this task can be automated with the power of machine learning and pretty much every commercial bank does so nowadays. In this project, we will build an automatic credit card approval predictor using machine learning techniques, just like the real banks do.
The dataset used in this project is the Credit Card Approval dataset from the UCI Machine Learning Repository.

3. Unsupervised Machine Learning Project - Customer segmentation using app behaviour for a marketing app

Skills tested: Pandas, Numpy, Unsupervised Learning with scikit-learn, Machine Learning, Elbow method, k-means clustering, Funnel visualisation using Plotly

Project description :Here we have the data from a marketing app that creates a drive to store solution by showing advertising brochures to users. Based on a combination of user activity & preference, users are sent different kinds of push notifications. The data tells us if a particular user received a notification and if they opened it. We use k-means clustering to segment the users into low, mid and high value customers and propose individual trageting strategies for each segment. Moreover, basic EDA coupled with the segmentation helps us recognise interesting patterns in user behaviour over several weeks and helps us define key initiatives to utilise the user trends to improve business growth.

4. Computer Vision Project - Bees image loading and preprocessing to create a data pipeline

Skills tested - Numpy, Pandas, Images module from Pillow library, data visualization, image transformation, kernel density estimation, Ipython display

The question at hand is: can a machine identify a bee as a honey bee or a bumble bee? These bees have different behaviors and appearances, but given the variety of backgrounds, positions, and image resolutions it can be a challenge for machines to tell them apart.Being able to identify bee species from images is a task that ultimately would allow researchers to more quickly and effectively collect field data. Pollinating bees have critical roles in both ecology and agriculture, and diseases like colony collapse disorder threaten these species. Identifying different species of bees in the wild means that we can better understand the prevalence and growth of these important insects. This notebook walks through loading and processing images. After loading and processing these images, they will be ready for building models that can automatically detect honeybees and bumblebees.

5. Computer Vision Project - Object detection in images using computer vision and tensorflow

Skills tested - cvlib, openCV, pandas, matplotlib

In this notebook we write a simple program that reads and image from the chosen directory and processes it for object detection using the openCV and cvlib modules of python. The program detects basic objects like bus, car, truck, person, apple, etc. We are using a pre-trained model to detect basic objects instead of training a model ourselves.

6. Natural Language Processing Project - Amazon product review web scraping and sentiment analysis

Skills tested - Pandas, TextBlob, WordCloud, EDA, matplotlib, NLP

In this notebook we scrape the amazon.com website for apple watch product reviews and star rating. We first create a word cloud that highlights the keywords used most frequently in the reviews and then we further assess the sentiment of each review. Our aim is to find the reviews where the star rating and the overall sentiment of the comments do no match because these are typically the reviews where people provide relevant information about the pros and cons of the product that could be a make/break the deal for a prospective buyer. The word cloud combined with the sentiment analysis provides a good indication about what factors generally influence the customer purchasing behaviour.

## DATA ANALYSIS PROJECTS

1. Analysing international debt statistics

Skills tested: Foundational understanding of SQL queries

Project description :It's not that we humans only take debts to manage our necessities. A country may also take debt to manage its economy. For example, infrastructure spending is one costly ingredient required for a country's citizens to lead comfortable lives. The World Bank is the organization that provides debt to countries.
In this project, we are going to analyze international debt data collected by The World Bank. The dataset contains information about the amount of debt (in USD) owed by developing countries across several categories. We are going to find the answers to questions like:
What is the total amount of debt that is owed by the countries listed in the dataset?
Which country owns the maximum amount of debt and what does that amount look like?
What is the average amount of debt owed by countries across different debt indicators?
The prerequisite for this project is Intro to SQL for Data Science.

The data used in this project is provided by The World Bank. It contains both national and regional debt statistics for several countries across the globe as recorded from 1970 to 2015.


2. Data Analysis Project - The discovery of handwash project

Skills tested: Importing & cleaning data in Python, data manipulation with Python, data visualization with python's matplotlib, foundational understanding of statistics & probability.

Project description : In 1847, the Hungarian physician Ignaz Semmelweis makes a breakthough discovery: He discovers handwashing. Contaminated hands was a major cause of childbed fever and by enforcing handwashing at his hospital he saved hundreds of lives.
In this python project we will reanalyze the medical data Semmelweis collected.

3. Data Analysis Project - GoT network analysis project

Skills tested: Network analysis in Python, foundational understanding of pandas

Project description :Jon Snow, Daenerys Targaryen, or Tyrion Lannister? Who is the most important character in Game of Thrones? Let's see what mathematics can tell us about this!
In this project, we will look at the character co-occurrence network and its evolution over the five books in R.R. Martin's hugely popular book series A Song of Ice and Fire (perhaps better known as the TV show Game of Thrones). We will look at how the importance of the characters changes over the books using different centrality measures.

4. Data Transformation Project - SEM with Python

Skills tested: Intermediate level knowledge of python, foundational understanding of data science principles

Project description :In this case study, we work for a digital marketing agency, which is approached by a massive online retailer of furniture. We are tasked with creating a prototype set of keywords for search campaigns for their sofas section. With our Python skills, we will efficiently create these keywords!
The most important task in structuring a search engine marketing account is mapping the right keywords to the right ads and making sure they send users to the right landing pages. Having figured that out is a big part of the account setup and makes the life of the account manager much easier.

5. Data Analysis Project - Exploring the Bitcoin Cryptocurrency market

Skills tested: Pandas foundation, cleaning data in python, manipulating dataframes with pandas

Project description :To better understand the growth and impact of Bitcoin and other cryptocurrencies we will, in this project, explore the market capitalization of different cryptocurrencies.
Warning: The cryptocurrency market is exceptionally volatile, and any money you put in might disappear into thin air. Never invest money you can't afford to lose.

6. Data Analysis Project - Exploring 67 years of LEGO

Skills tested: Pandas foundation, manipulating dataframes with pandas

Project description :The Rebrickable database includes data on every LEGO set that has ever been sold; the names of the sets, what bricks they contain, what color the bricks are, etc. It might be small bricks, but this is big data! In this project, we will get to explore the Rebrickable database.

## Web & App Development

1. Calculator app - Making my own calculator desktop application

Skills tested: tkinter, parser, ttk, gridlayout, pyinstaller

Project description :In this project we make our very first GUI application, a fully functional calculator that can be used to make basic calculation. Theoretically, we can add as many functions to this calculator as we want. The python script is then converted into a single executable file using python script freezing tool (pyinstaller). This helps in easily sharing the app with others and avoids the need for them to download any modules. The executable file is also found in this repo.

2. OCR app - Making an application that extracts text from pictures

Skills tested: tkinter, functions, tesseract, PIL, Image, pyperclip, filedialog, messagebox, py installer

Project description :In this project we make a new desktop app called OCR. This GUI application uses a browse button to browse and open an image file (.jpg, .jpeg & .png). If this image has text in it then the application will extract it and show it in a messagebox. Moreover, this text is also copied to the clipboard for easy access for the user of this application. The application is unfortunately too large to be added here since it has many dependencies. Therefore, only the python script has been uploaded here.

3. Building database application for PostgreSQL using Python

Skills tested: tkinter, PostgreSQL, psycopg2, SQL, canvas, frames, labels & buttons

Project description :In this project we built a destop GUI application in Python that could connect and interact with PostgreSQL database. PostgreSQL is a widely used relational database management system that is particularly famous for its scalability. While CML is generally a good option to interact and work with databases, a GUI application would reduce the entry barrier for novice users. This project builds a simple application for so that user could easily add data to the database using data entry fields, have an overview of the data in the table and search for a particular entry using the search field.

