## Introduction









## Exploratory Data Analysis









## Research Question 1:




















## Research Question 2: How do aspects in the personal profile indicated by gender, education, marital status, and age in this dataset individually determine the number of months for payment delay?

###### There are four sub-questions that can be addressed to explore the research question.
###  1. Which category in the sex group affects the length of payment delay the most?

![Gender proportion](images/final_plots_Remy/final_plot1.png)


- The categorical plot above shows each gender’s proportion in each month’s repayment status. Female clients have a larger proportion than male clients in the “-2”, “-1”, and “0” ranges which means they pay back on time. And male clients have a slightly larger proportion than female clients in delaying more than three months or above and sometimes leading the whole percentage.

### 2. How is the feature of the education level affect the length of payment delay?

![Education level proportion](images/final_plots_Remy/final_plot2.png)

- The categorical plot above shows each education level’s proportion in each month’s repayment status. Samples with graduate school education levels have slightly larger percentages in duly or early payments, and samples with university education levels dominate the portion of delayed payments.

### 3. Which marital status caused payment delay the most?

![Marital Proportion](images/final_plots_Remy/final_plot3.png)

- The categorical plot above shows each marital status’s proportion in each month’s repayment status. The proportion is close to equal in the early payments and still needs more data to determine which marital status has a larger portion in delayed payments.


### 4. How will age determine the length of payment delay?

![Distribution of age](images/final_plots_Remy/final_plot4.png)

- The joint plot above demonstrates the distribution between age and the average number of months clients used to pay back. There are three hex bins that have darker colors which means many samples concentrate at that range, the three hex bins are between ages 20 to a little bit above 30 and these samples delay more than two months for their payments.


#### As result, a sample client profiling as female, graduate school education level, whether married or single, and age not between 20 to 30 can be considered a creditable client because this group tends to pay back their credit card early or duly, and a sample client profiling as male, university education level, whether married or single, and age between 20 to 30 can be considered as an uncreditable client since this group tends to delay their payment under the setting of this dataset. 
#### The full analysis notebook including the code and the data can be found [here]( https://github.com/ubco-W2022T2-data301/project-group-group27/blob/main/analysis/analysis_Remy.ipynb).


## Research Question 3: As a client, what is the best way to have the minimum negative influence on your own credit depending on your own conditions?

###### There are four sub-questions that can be addressed to explore the research question.
###  1. How does the default payment influence the given credit ?
![R1PLOT](images/final_plots_Shirley/Q1.png)

- the bar and boxen plot shows the higher the credit they have, the less likely they will have the default payment. the line plot shows that the chance is decreasing by increasing the credit. 

###  2. How does sex,education, marriage and age influence the given credit ?
![R2PLOT](images/final_plots_Shirley/Q2(1).png)
![R2PLOT2](images/final_plots_Shirley/Q2(2).png)
![R2PLOT3](images/final_plots_Shirley/Q2(3).png)
![R2PLOT4](images/final_plots_Shirley/Q2(4).png)
![R2PLOT5](images/final_plots_Shirley/Q2(5).png)
![R2PLOT6](images/final_plots_Shirley/Q2(6).png)

- the plots for the sex vs. given credit shows that gender doesn't influence the given credit a lot, but female generally has sliently higher given credit than male. 
- the plots for the education vs. given credit shows that graduate school has the highest given credit, highschool has the lowest credit and the other three has around the same credit. the changes are strongly dependent on the education level. 
- the plots for marriage vs. given credit shows people who married and single has roughly same amount of credit, but all higher than the others and unknown. 
- the plots for age(percentage) vs. given credit shows young people tend to want to have more credits,and can usully get it too. But the people who actually can have more credits are the people who is later middle ages. Chances are increaing by the ages from middle ages to late middle ages, but decrease from late middle age to old age. 

###  3. How does sex,education, marriage and age influence the repayment status?
![R3PLOT](images/final_plots_Shirley/Q3(1).png)
![R3PLOT2](images/final_plots_Shirley/Q3(2).png)
![R3PLOT3](images/final_plots_Shirley/Q3(3).png)
![R3PLOT4](images/final_plots_Shirley/Q3(4).png)
![R3PLOT5](images/final_plots_Shirley/Q3(5).png)

- As the repayment status all shown in negative if it is late, so it means the higher the point on the graph, the later the payment happens. 
- Sex: women tend to pay more ontime/ ealier than men from all plots through several months disorvery. 
- education: people who in graduate school, unknown and others seems to perform better in repayment status, in which the graduate school is the best,but people who are in university and highschool seems doing worse than the other three, with little difference with each other. 
- marriage: people who is belongs to other group seems to has the worst repayment status through plots. But people seems to have a more stable repayment status when they are married and single, when the unknow group sometimes seems perform better but not that stable.
- age: it seems like majority of the people won't influence by the age group, but the people has more extreme performance which means more diverse of their action when they become older through plots.  

###  4. How does the amount of bill statements influence the repayment status ?
- the topay(which is caculated by the billpay with the repay status) demostrate the stress of return for the future. Through the changes and comparasion between each topay by looking at the plots, it clealy shows that the more people borrow, the longer people return, the more stress people will have. As topay is increasing through time. 

#### In conclusion through combination of all my research quesions, the best way to minimize the negative influence depends on your own condition is consider gender wise, people don't need to worry too much as they seems they can control themselves when they borrow, but male should pay more attention than female, education wise if you are in university or highschool you should focus more. marriage wise people who are not single or married should be more careful, and age wise if people are getting older they should plan from younger ages. Also, the less you borrow, the more chances you will have a better credit. Last, people should be careful about when they decide to return the money they lack, the ealier the better. 






















## Conclusion 







