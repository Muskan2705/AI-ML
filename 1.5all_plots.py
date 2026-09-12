# seaborn 

# seaborn is a python lib for creating statistical visualizations. It provides clean default
# style and color palattes making plots more attractive and easier to read. 
# Build on the top of matplotlib and pandas data structures seaborn make data visulaization easier and more consistant 

#linePlot

# show the realtionship between 2 continuous variable 





# scatter plt 

# it is used to show the realtioship between 2 numerical variable , it help to identifing pattern and corelatioship 

# import seaborn as sns 
# import matplotlib.pyplot as plt

# tips = sns.load_dataset('tips')
# sns.scatterplot(data=tips, x='total_bill', y='tip',hue='day')
# plt.show()   #hue "day" add color grouping 



#BAR PLOT 

# # barplot is used to compare numerical values across categories , it shows average values with confidence intervals

# import seaborn as sns 
# import matplotlib.pyplot as plt
# tips = sns.load_dataset('tips')
# sns.barplot(x="day", y="total_bill", hue='day',data=tips)
# plt.show()






# import seaborn as sns 
# import matplotlib.pyplot as plt

# tips = sns.load_dataset("tips")
# sns.boxplot(x="day",y='total_bill',data=tips)
# plt.show()


# histplot
# is used to visulaize the distributition of single numerical variable 

# import seaborn as sns
# import matplotlib.pyplot as plt
# tips = sns.load_dataset("tips")
# sns.histplot(tips["total_bill"],kde=True)
# plt.show()



# heatmap
# is used to visualize matrix-like data using colors. commonly used for correlationn matrices 

# import seaborn as sns
# import matplotlib.pyplot as plt
# tips = sns.load_dataset("tips")
# corr = tips.corr(numeric_only=True)
# sns.heatmap(corr,annot=True,cmap="coolwarm")
# plt.show()   # annot=True display values s=cmap control color scheme



# pairplot
# is used to plot pairwise relatioship between multiple numerical variables

import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset("iris")
sns.pairplot(iris,hue="species")
plt.show()  # hue add category distribution 

