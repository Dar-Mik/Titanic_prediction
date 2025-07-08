# Titanic_prediction

My first project on a journey of becoming ML expert.

## ACTIVATION
1. clone repository
2. change the directory using "cd"
3. activate virtual environment using: python -m venv .venv.venv\Scripts\activate
4. install packages using: pip install -r requirements.txt


## PROGRESS TACKER
Here I track my progress and insights

# Day 1 - (7.7.2025)
I managed to copy the data from Kaggle. The import function was created in secondary folder in order to try importing functions from other folders. Then I downloaded and imported data into main file. I use Jupyter Notebook due to its accessibility and visual appeal.

I conducted the first part of Exploratory Data Analysis (EDA) focusing on Age, Sex, Class with respsect to Surivovrship. The data suggest that there is probably no significant difference in age when it comes to survivorship. However, there is significant difference in attributes of Sex and Class. People from higher class and females were prone to surviving. The differences are quite significant. 

Next steps:
1. Proceed with EDA focusing on remaining categories such as no. of family members on the ship
2. Creation of Binary dependent model

Main insights:
1. Need to work on my matplotlib skills - graphing

# Day 2 - (8.7.2025)
I continued in EDA. Exlpored other interesting metrics such as family size including number of silblings and parents on the board. Additionally, I looked at the cabin position on the ship based on leading letter. I concluded, that the most significant indicators for survivorship were the fare of a ticket and class indicating the wealth of a passenger, the sex of a passenger and age. I continued with the first model selection and training. I chose RandomForestCliassifier. The raw model returned the accuracy ~80%. After a try of tuning hyperparameters, I were not able to significantly increase the accuracy or other metrics. Even though, the results are satisfactory, I would like to explore other classifying models.

Next steps:
1. Discover other models such as KNN, SVM, Logistic Regression
2. Potential inclusion of other metrics in the model (currently using only 4 explanatory variables)

Main insights:
1. After the first exploration (describe, info...), split the variables into categorical and continuous --> This is easier for working with the data
2. It is beneficial to keep orignial dataset and perform EDA on it, then to create all_data dataset with custom fields and columns
3. Hyperparameters tuning and cross-validation. Especially for Random Forest, it may help to find the best fitting model, however be aware of overfitting or undefitting
4. For plotting histograms separated by categorical variable, it is better to set bin_width rather than number of bins due to imbalance of range 
