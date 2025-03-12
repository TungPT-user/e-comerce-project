import matplotlib as plt 
import seaborn as sns
import pandas as pd

# matplotlib control atributes of the figure (controlling atributes of the figure) and generate plots 
# seaborn generate plots using data (we get varity of func and much-much data better plots) 
# 
# data can divide to 2 options: categories (gender, city) and continous(income, total changes)  
# 
# categorical usually use bar chart, count-plot 
# continous usually use histogram, displot (distribution), boxplot


df = pd.read_csv("C:\\Users\\ptung\\Desktop\\nhật ký Python-data\\pandas-tutorial\\day-01\\city-gdp.csv")
print(df.head(10))


sns.barplot(x='provice', y='GRDP\n(billion VND)', data=df)
plt.show()


myName = 't'
myName