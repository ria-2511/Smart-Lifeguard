# Introduction 
As per WHO , Drowning is a serious and neglected public health threat claiming the lives of 372 000 people a year worldwide. More than 90% of these deaths occur in low- and middle-income countries. This death toll is almost two thirds that of malnutrition and well over half that of malaria but unlike these public health challenges, there are no broad prevention efforts that target drowning. 

Refer to the SRS Documentation of this Project using the Link below - 

https://github.com/ria-2511/Smart-Lifeguard/blob/main/404_DrowningNotFound%20(1).pdf

## Goal 
An efficient and enhanced software tool for detecting well before the person is in danger of drowning by measure of person’s heartbeat, blood pressure and oxygen concentration.

## Software Overview 
* Our software consist of a model that takes certain values such as Heart beat , Systolic Blood pressure, Diastolic Blood pressure & SP02 values as input.
* On the basis of certain threshold values it evaluate, that a person has a higher probability of drowning.
* An alert is sent to the lifeguard along with the position of the drowning victim through the GPS.

## Team Members and Their Contributions 
### (Batch COE-12 , Thapar Institute of Engineering and Technology - 2022)
* Ria Soam - Front End Web Development for the Prototype (using CSS, HTML , BootStrap , Javascript) , Machine Learning Model to check Drowning or not , SRS 
* Saurabh Kumar - Front End Web Developement For the Prototype , SRS
* Arpit Singh - Flask usage , ML Model 
* Manan Gupta - Front End Development , ML Model 



### Detection System
Used to detect people in danger of drowning through their heartbeats , systolic bp, diastolic bp and SPo2 values through a wristband which takes this live footage and transmits them to the database to be analyzed by our model. Live alerts are sent to the lifeguard for the people with irregular values and the ones who have high probability of drowning.

#### Description and Priority
* It is of High priority. benefit, penalty, cost, and risk 
#### Stimulus/Response Sequences
* Detects the heartbeat , systolic bp, diastolic bp and SPo2 values
* Alerts are sent to the lifeguard for the people with high drowning probability.

## Working of the Drowning Machine Learning Model Below 
* We couldn't find an appropriate dataset online so we created our own using a random number generator and generating values for the coloumns with their respective ranges according to the medical facts.
* Then we have split the dataset with a 20% ratio of Testing data and 80% ratio of Training data .
* We have applied SVM to Predict the values of the dataset and to classify whether they fall into the category of drowning or not. 
* Whatever values we enter into our Interface , that is transferred to our model using FLASK. And then flask further tranfers the output given by the model to the interface and the final result is displayed.

## Algorithm Definition 
The Algo we have used here is SVM. “Support Vector Machine” (SVM) is a supervised machine learning algorithm that can be used for both classification or regression challenges. However,  it is mostly used in classification problems. In the SVM algorithm, we plot each data item as a point in n-dimensional space (where n is a number of features you have) with the value of each feature being the value of a particular coordinate. Then, we perform classification by finding the hyper-plane that differentiates the two classes very well. 

<img src="https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_21.png">

In the above Image , the Hyperplane B is the best one as it divides the data Points perfectly. 

Now consider the Planes below . Here all of them divide the set perfectly. So we introduce the concept of MARGIN to choose the best plane. Here, maximizing the distances between nearest data point (either class) and hyper-plane will help us to decide the right hyper-plane. This distance is called as Margin.

<img src="https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_4.png">

Above, you can see that the margin for hyper-plane C is high as compared to both A and B. Hence, we name the right hyper-plane as C. Another lightning reason for selecting the hyper-plane with higher margin is robustness. If we select a hyper-plane having low margin then there is high chance of miss-classification.

### SVM Parameters 
#### 1. Kernel ( TO EDIT )
#### 2. Gamma 
Kernel coefficient for ‘rbf’, ‘poly’ and ‘sigmoid’. Higher the value of gamma, will try to exact fit the as per training data set i.e. generalization error and cause over-fitting problem.
Example: Let’s difference if we have gamma different gamma values like 0, 10 or 100.

svc = svm.SVC(kernel='rbf', C=1,gamma=0).fit(X, y)

<img src="https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_15.png">

#### 3. C
Penalty parameter C of the error term. It also controls the trade-off between smooth decision boundaries and classifying the training points correctly.

<img src="https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_18.png">

We should always look at the cross-validation score to have effective combination of these parameters and avoid over-fitting.

## Results 
We created a model using SVM with an overall accuracy of 91.2%.

# Bibliography 
* https://www.analyticsvidhya.com/blog/2017/09/understaing-support-vector-machine-example-code/#:~:text=%E2%80%9CSupport%20Vector%20Machine%E2%80%9D%20(SVM,mostly%20used%20in%20classification%20problems.
* https://towardsdatascience.com/support-vector-machine-introduction-to-machine-learning-algorithms-934a444fca47
* https://monkeylearn.com/blog/introduction-to-support-vector-machines-svm/https://medium.com/analytics-vidhya/everything-one-should-know-about-support-vector-machines-svm-18e6d3f96f49 
