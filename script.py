#import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import codecademylib3

#load data
forests = pd.read_csv('forests.csv')

#check multicollinearity with a heatmap
matrix = forests.corr()
sns.heatmap(matrix, annot = True )
plt.show() # Show the plot
plt.clf()

#plot humidity vs temperature
sns.lmplot(x='temp', y='humid', hue='region',markers=['o', 'x'], data=forests)
plt.show() # Show the plot
plt.clf()

#model predicting humidity Intercept : 142.575801 / region[T.Sidi Bel-abbes] -7.247538 /temp -2.392547
modelH =sm.OLS.from_formula('humid ~ temp + region', data=forests).fit()
print(modelH.params)

#equations 
#y= 142.575801 -7.247538*region-2.392547*temp
#y(Bejaia)= 142.575801-2.392547 *temp
#y(Sidi Bel-abbes)= 135.3- 2.392547 *temp

#interpretations
## Coefficient on temp: For every temperature increase of one-degree Celsius, relative humidity decreases by 2.4%.

## For Bejaia equation:
#The intercept indicates that a temperature of zero degrees Celsius is associated with an average relative humidity of 142.57%.

## For Sidi Bel-abbes equation:
#The intercept indicates that a temperature of zero degrees Celsius is associated with an average relative humidity of 135.3%.

#plot regression lines
sns.lmplot(x='temp',y='humid',hue='region',data=forests, fit_reg = False)
plt.plot(forests.temp, modelH.params[0]+modelH.params[1]*0+modelH.params[2]*forests.temp, color='blue',linewidth=5, label='Bejaia')
plt.plot(forests.temp, modelH.params[0]+modelH.params[1]*1+modelH.params[2]*forests.temp, color='orange',linewidth=5, label='Sidi Bel-abbes')
plt.legend()
plt.show()
plt.clf()

#plot FFMC vs temperature
sns.lmplot(x='temp', y='FFMC', hue='fire',markers=['o', 'x'], data=forests)
plt.show() # Show the plot
plt.clf()

#model predicting FFMC with interaction = Intercept	20.072892799617442 /fire[T.True]	16.543904071067036 / temp	1.5066520148415457
modelF =sm.OLS.from_formula('FFMC ~ temp + fire + temp:fire', data=forests).fit()
print(modelF.params)

#equations
## Full equation:
#y= -8.108891 + 76.788000*fire+ 2.445159*temp -1.887219*temp:fire
## For locations without fire:
#y= -8.108891 + 2.445159*temp
## For locations with fire:
#y= 68.7 + 0.5*temp

# The regression line has an intercept 76.8 points greater and a slope 1.9 points less than those of the locations that did not end up experiencing a fire. 
# For every temperature increase of one degree Celsius, FFMC score increases by 0.5 points.


#plot regression lines
sns.lmplot(x='temp',y='FFMC',hue='fire',data=forests, fit_reg = False)
plt.plot(forests.temp, modelF.params[0]+modelF.params[1]*0+modelF.params[2]*forests.temp + modelF.params[3]*forests.temp*0, color='blue',linewidth=5, label='No Fire')
plt.plot(forests.temp, modelF.params[0]+modelF.params[1]*1+modelF.params[2]*forests.temp + modelF.params[3]*forests.temp*1, color='orange',linewidth=5, label='Fire')
plt.legend()
plt.show()
plt.clf()


#plot FFMC vs humid
sns.lmplot(x='humid', y='FFMC',data=forests)
plt.show() # Show the plot
plt.clf()

#polynomial model predicting FFMC
resultsP = sm.OLS.from_formula('FFMC ~ humid + np.power(humid,2)', data=forests).fit()
print(resultsP.params)

#regression equation
# y = 77.634041 + 0.752165*humid -0.011420*np.power(humid, 2) 

#sample predicted values
#89.30075097131991 / 89.97048469230963 /81.65244328464414/ 74.32827643752202

print(resultsP.params[0] + resultsP.params[1]*25 + resultsP.params[2]*np.power(25,2))
print(resultsP.params[0] + resultsP.params[1]*35 + resultsP.params[2]*np.power(35,2))
print(resultsP.params[0] + resultsP.params[1]*60 + resultsP.params[2]*np.power(60,2))
print(resultsP.params[0] + resultsP.params[1]*70 + resultsP.params[2]*np.power(70,2))


#interpretation of relationship

#From the plot, we see that as humidity increases FFMC slightly increases, then slightly decreases, and then decreases faster at the highest humidity percentages. These changes produce a curved rather than straight shape.

