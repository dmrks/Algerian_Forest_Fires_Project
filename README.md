# AlgerianForestFires_Project

Algerian Forest Fires
In this project, you’ll examine the forests dataset that includes variables on weather and fire risk for locations in Algerian forests from two different regions. By plotting and running multiple linear regressions, you’ll explore the relationships among variables including:

temp – maximum temperature in degrees Celsius
humid – relative humidity as a percentage
region – location in Bejaia in the northeast of Algeria or Sidi Bel-abbes in the northwest of Algeria
fire – whether a fire occurred (True) or didn’t (False)
FFMC – Fine Fuel Moisture Code: measure of forest litter fuel moisture that incorporates temperature, humidity, wind, and rain
ISI – Initial Spread Index: estimates spread potential of fire
BUI – Buildup Index: estimates potential release of heat
FWI – Fire Weather Index: measure of general fire intensity potential that incorporates ISI and BUI
The dataset is a subset of data that was downloaded from the UCI Machine Learning Repository and then cleaned for analysis.


Faroudja ABID et al., Predicting Forest Fire in Algeria using Data Mining Techniques: Case Study of the Decision Tree Algorithm, International Conference on Advanced Intelligent Systems for Sustainable Development (AI2SD 2019) , 08 - 11 July , 2019, Marrakech, Morocco.


# Predicting Relative Humidity

1.
The dataset has been loaded for you as forests. Since we will be running several multiple linear regressions in this project, we want to check the multicollinearity assumption before we get started. Create a table of correlations for the quantitative variables in forests and call it corr_grid. Then plot the correlations with a heat map to look for potential collinear variables. Make sure to show, then clear the plot.

Are there any variables that should not go into a model together as predictors?


2.
Let’s explore the relationship between relative humidity (humid) and maximum temperature (temp) by creating a scatter plot with humid on the y-axis and temp on the x-axis. Color the points by region. Make sure to show, then clear the plot.

Does the relationship between humidity and temperature appear different for locations in Bejaia compared to those in Sidi Bel-abbes?

3.
Fit a multiple linear regression model predicting humidity with temperature and region as predictors. Save the fitted model as modelH and print the coefficients. Does the coefficient on temp match the relationship you expected from the plot you made in the previous step?


4.
Using the model coefficients you printed in the last step, write out the full regression equation as a comment. Then write out the regression equation for locations in Bejaia and the regression equation for Sidi Bel-abbes as additional comments. How are these equations similar and how are they different?


5.
In a comment, write an interpretation for the coefficient on temp in the full regression equation. Then, for each region’s regression equation, interpret the intercept in terms of the regression line and in the context of predicting humidity from temperature. Do the intercept interpretations make practical sense?


6.
Finally, let’s put our model back into a visualization to see if it matches our expectations. Create the same scatter plot of humidity and temperature from step 2, but this time add the two regression lines you found for each region. Make sure to show, then clear the plot.

Do these lines seem to fit the data well?



# Predicting FFMC: Interaction

7.
In this section, we will fit the first of two regression models predicting the Fine Fuel Moisture Code (FFMC), a measurement of fuel moisture that contributes to the assessment of fire risk. First, let’s explore the relationship between FFMC and temperature and see if that relationship looks different for areas that ended up experiencing a fire compared to those that didn’t. Create a scatter plot of FFMC on the y-axis and temperature on the x-axis with points colored by the binary variable for fire status. Make sure you show, then clear the plot.

Do the groups seem to have the same or different slopes?

8.
Since the groups look like they may have regression lines with different slopes, fit a model predicting FFMC with predictors temp, fire, and a term for their interaction. Save the results as resultsF and print the resulting model coefficients. What do we learn about the regression line created with these coefficients?


9.
As a comment, write the full regression equation from the coefficients you printed in the last step. Then, write an equation for each group of fire. How are the equations similar, and how are they different?


10.
Using the equations you created in the previous step, write as a comment an interpretation of the coefficient on temp for each group of fire. What does the difference in these coefficients say about the relationship between FFMC measure and temperature in areas where a fire didn’t occur compared to where one did occur?

11.
Let’s visualize our model results on the scatter plot from step 7 by adding lines to the plot for the regression equation for each group of fire. Make sure you show, then clear the plot.

Do these lines seem to fit the data better than two parallel lines (i.e., lines with the same slope)?


# Predicting FFMC: Polynomial

12.
Now, let’s try predicting FFMC from just relative humidity. First, let’s get an idea of what the relationship looks like in a scatter plot of FFMC on the y-axis and relative humidity on the x-axis. Make sure to show, then clear the plot.

Will a straight line produce the best fit here?


13.
Since we see a curve in the pattern of points on the plot, run a multiple regression model predicting FFMC with humid and humid raised to the second power (squared) as predictors. Save the results as resultsP and print the coefficients. Does it make sense to interpret the coefficient on humid as we would normally interpret coefficients on quantitative variables?


14.
In a comment, use the coefficients you found in the previous step to write the regression equation. Using the equation and the model coefficients you found in the last step, find the FFMC for the following relative humidity levels: 25%, 35%, 60%, and 70%. What do you notice about the difference in FFMC when increasing from 25% to 35% compared to increasing from 60% to 70%?


Stuck? Get a hint
15.
Using the plot from step 12 and the sample predicted values from step 14, write as a comment an interpretation of the relationship between FFMC and relative humidity. What would a straight regression line have implied about their relationship?
