# Credit Scoring : Explanatory Data Analysis 

import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
#Import trainig data 
data= pd.read_csv('D:\Training50.csv', index_col=0)
print(data.head())

# Exploring data 
data.describe()
data.dtypes

# Check missing values

import numpy as np
np.isnan(data) # works only on floats 

pd.isnull(data) # only check
 # to count missing values
np.count_nonzero(pd.isnull(data))
# => we have zero missing values

def num_missing(x):
  return sum(x.isnull())

#Applying per column:
print "Missing values per column:"
print data.apply(num_missing, axis=0) #axis=0 defines that function is to be applied on each column

#Applying per row:
print "\nMissing values per row:"
print data.apply(num_missing, axis=1).head() #axis=1 defines that function is to be applied on each row

# To solve the problem of missing values :
# We can use 'fillna()' It is used for updating missing values with the overall mean/mode/median of the column
# First  we import a function to determine the mode
# CODE : from scipy.stats import mode
# CODE : mode(data['variable'])
# mode can be an erray as there can be multiple values with high frequency .We take the first one by default always using :
#CODE :mode(data['variable']).mode[0]
#Impute the values :
# CODE : data['variable'].fillna(mode(data['variable']).mode[0] , inplace=True)




# Visualize missing values

import missingno as msno
import matplotlib.pyplot as plt
#%matplotlib inline
msno.matrix(data)



# Data Visualization
                                 

   #Packages needed
                                 
import matplotlib as pl
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns

import warnings # current version of seaborn generates a bunch of warnings that we'll ignore
warnings.filterwarnings("ignore")

                                  # Continuous variables
      #Histogam
sns.distplot(data['Age..years.'], bins=20)
sns.distplot(data['Duration.of.Credit..month.'], bins=20)
sns.distplot(data['Credit.Amount'], bins=20)

      #Boxplot

c=sns.boxplot(x="Age..years.", data=data)
c=sns.stripplot(x="Credit.Amount", data=data, jitter=True,edgecolor="gray")
b=sns.boxplot(x="Duration.of.Credit..month.", data=data)
b=sns.stripplot(x="Duration.of.Credit..month.", data=data, jitter=True,edgecolor="gray")
a=sns.boxplot(x="Credit.Amount", data=data)
a=sns.stripplot(x="Credit.Amount", data=data, jitter=True,edgecolor="gray")

       # Plot  Creditability = f( continuous variables )
sns.jointplot(x="Age..years.", y="Creditability", data=data, size=5)
sns.jointplot(x="Duration.of.Credit..month.", y="Creditability", data=data, size=5)
sns.jointplot(x="Credit.Amount", y="Creditability", data=data, size=5)

   

                                # Categorical variables

       #Countplot 
sns.countplot(y="Account.Balance",data =data , palette ="Greens_d") 
sns.countplot(y="Payment.Status.of.Previous.Credit ",data =data , palette ="Greens_d") 
sns.countplot(y="Purpose",data =data , palette ="Greens_d")
sns.countplot(y="Value.Savings.Stocks ",data =data , palette ="Greens_d")
sns.countplot(y="Length.of.current.employment",data =data , palette ="Greens_d")
sns.countplot(y="Instalment.per.cent ",data =data , palette ="Greens_d")
sns.countplot(y="Sex...Marital.Status ",data =data , palette ="Greens_d")
sns.countplot(y="Guarantors ",data =data , palette ="Greens_d")
sns.countplot(y="Duration.in.Current.address",data =data , palette ="Greens_d")
sns.countplot(y="Most.valuable.available.asset",data =data , palette ="Greens_d")
sns.countplot(y="Concurrent.Credits",data =data , palette ="Greens_d") 
sns.countplot(y="Type.of.apartment",data =data , palette ="Greens_d")
sns.countplot(y="No.of.Credits.at.this.Bank",data =data , palette ="Greens_d")
sns.countplot(y="Occupation",data =data , palette ="Greens_d") 
sns.countplot(y="No.of.dependents ",data =data , palette ="Greens_d")
sns.countplot(y="Telephone",data =data , palette ="Greens_d")
sns.countplot(y="Foreign.Worker",data =data , palette ="Greens_d")

      # Plot  Creditability = f( categorical variables )

sns.barplot(x="Account.Balance",y="Creditability" , data=data)
sns.barplot(x="Payment.Status.of.Previous.Credit",y="Creditability" , data=data)
sns.barplot(x="Purpose",y="Creditability" , data=data)
sns.barplot(x="Value.Savings.Stocks",y="Creditability" , data=data)
sns.barplot(x="Length.of.current.employment",y="Creditability" , data=data)
sns.barplot(x="Instalment.per.cent",y="Creditability" , data=data)
sns.barplot(x="Sex...Marital.Status",y="Creditability" , data=data)
sns.barplot(x="Guarantors",y="Creditability" , data=data)
sns.barplot(x="Duration.in.Current.address",y="Creditability" , data=data)
sns.barplot(x="Most.valuable.available.asset",y="Creditability" , data=data)
sns.barplot(x="Concurrent.Credits",y="Creditability" , data=data)
sns.barplot(x="Type.of.apartment",y="Creditability" , data=data)
sns.barplot(x="No.of.Credits.at.this.Bank",y="Creditability" , data=data)
sns.barplot(x="Occupation",y="Creditability" , data=data)
sns.barplot(x="No.of.dependents",y="Creditability" , data=data)
sns.barplot(x="Telephone",y="Creditability" , data=data)
sns.barplot(x="Foreign.Worker",y="Creditability" , data=data)






                                 





                                 
