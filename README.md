# **Predicting Seasonal Flu Vaccines**

## **Authors**:
Aung Si and Paul Justafort.

![5384427](https://github.com/pmjustafort/flushotlearning/assets/137816262/538874d0-d94c-4255-9ef9-d4b90c7583c5)



## **Overview**

This project aims to predict seasonal flu vaccine uptake using data from the National 2009 H1N1 Flu Survey (NHFS), conducted during the 2009 flu season where more than 26000 people were interviewed. Our goal is to develop an accurate predictive model based on specific parameters that can accurately predict whether individuals will take the seasonal flu vaccine and provide recommendations to enhance seasonal flu vaccine uptake based on the insights gained from our analysis. By doing so, we hope to contribute to improving vaccination rates and understanding vaccination behavior, ultimately supporting public health initiatives.

## **Business Problem**
Vaccines have long been a cornerstone of public health, shielding individuals and entire communities from a wide array of infectious diseases. Among these, the ongoing efforts to immunize against seasonal influenza stand out as a vital and complex undertaking. Unlike specific pandemic strains such as the 2009 H1N1 "swine flu," seasonal flu is a persistent and annually recurring challenge, necessitating vigilance and adaptation by medical professionals every year. Seasonal influenza vaccines are developed and distributed on an annual basis to combat the most common flu strains predicted to circulate during the upcoming flu season. Scientists and researchers analyze global flu trends, collecting samples and data to determine which strains are most likely to pose a threat. The composition of the seasonal flu vaccine is then tailored each year based on these predictions, making it a unique and dynamic tool in the fight against influenza.

In the United States, a coordinated effort involving the government, healthcare providers, public health organizations, and even private companies is launched each year to promote and provide seasonal flu vaccines. This expansive campaign includes public education, accessibility initiatives, and collaboration with healthcare professionals to ensure that vaccines reach as many people as possible. Guiding these efforts are robust data collection and analysis, including surveys and studies that closely monitor vaccination rates. One such resource is the National Seasonal Flu Survey, a comprehensive effort to gather information about individuals' vaccination status, as well as insights into their lives, opinions, and behaviors related to vaccination. In this analysis, we will delve into the data from this survey, applying statistical and analytical techniques to uncover patterns and trends in seasonal flu vaccination. By understanding the factors that influence people's decisions to get vaccinated, such as age, location, education, and beliefs about vaccines, we can craft targeted strategies to increase vaccination rates.

## **Data**
![image](https://github.com/pmjustafort/flushotlearning/assets/137816262/4cec3603-2fd3-425a-ba7e-f6f7fafdfd83) 


![image](https://github.com/pmjustafort/flushotlearning/assets/137816262/1ca50a0c-d008-4eb8-b0be-29b251f37c85)


The dataset utilized in this project originates from the National 2009 H1N1 Flu Survey (NHFS), conducted during the 2009-10 flu season. This telephone survey was designed to monitor influenza immunization coverage in the United States, specifically targeting individuals aged 6 months or older. A collaboration between the National Center for Immunization and Respiratory Diseases (NCIRD) and the National Center for Health Statistics (NCHS) under the Centers for Disease Control and Prevention (CDC), the NHFS collected information from October 2009 to June 2010. Its primary focus was to produce timely estimates of vaccination coverage rates for both the monovalent pH1N1 and trivalent seasonal influenza vaccines during the 2009-2010 flu season in response to the H1N1 pandemic. The CDC continues to monitor seasonal flu vaccination through other ongoing annual phone surveys, but the NHFS stands as a one-time survey created for this specific purpose.

For our exploration we're given three CSV's:
1. **Training Labels**: This one holds the binary labels we'll be training our model(s) to predict. There are two target labels, `'h1n1_vaccine'` and '`seasonal_vaccine'`— for this analysis we're only concerned with the latter. A $0$ indicates that the given respondent did not receive the respective vaccine while a $1$ indicates that the given respondent received the respective vaccine. This file shares the `'respondent_id'` column with the Training Features CSV.

2. **Training Features**: These are the features we'll be using to predict the probability of a respondent receiving a vaccine. There are 35 features and each is a response to a survey question. Features comprise various topics, such as behavioral (whether a respondent touches their face, washes their hand, etc.), opinion (whether the respondent believed the h1n1 vaccine was effective, etc.), and demographic.

3. **Testing Features**: These features relate to the respondents for whom we will be predicting the likelihood of receiving the vaccine.



## **Data Understanding**



## Results

### **Model performance metrics**
Our analysis involved the evaluation of multiple machine-learning models using several essential performance metrics. These metrics include Test Recall, Train Recall, Test F1, Train F1, Test ROC AUC, and Train ROC AUC. Among the models, "Random Forest (New Features)" and "Tuned Random Forest (New Features)" consistently displayed the highest performance, excelling in Test Recall and achieving a strong Test F1-score. These metrics highlight the potential of these models in effectively identifying individuals likely to take the seasonal flu vaccine. Additionally, both Random Forest models demonstrated robust training data fit, as evident from their high Train ROC AUC scores. Further details and insights can be derived from these metrics to guide our ongoing analysis.

![Model Recall Score Comparison](https://github.com/pmjustafort/flushotlearning/assets/137816262/f7e449fd-70d4-4234-896e-0d479a9ad62f)


### **Model Comparison**
In our comprehensive model evaluation, we rigorously assessed the performance of various machine learning models using a range of key metrics, including Test Recall, Train Recall, Test F1, Train F1, Test ROC AUC, and Train ROC AUC. Among this array of models, two consistently stood out as top performers: "Random Forest (New Features)" and "Tuned Random Forest (New Features)."
These models demonstrated exceptional predictive capabilities, particularly in correctly identifying individuals likely to take the seasonal flu vaccine. They achieved the highest Test Recall scores, with "Random Forest (New Features)" and "Tuned Random Forest (New Features)" scoring at 0.766 and 0.766, respectively. This highlights their proficiency in identifying potential vaccine takers.
Notably, "Tuned Random Forest (New Features)" attained the highest Test F1-score, reaching an impressive 0.776. This remarkable score underscores the model's ability to strike a balance between precision and recall, making it an excellent choice for our predictive task.
A significant contributing factor to the outstanding performance of these models was the meticulous application of feature engineering and hyperparameter tuning. These techniques allowed the models to capture intricate patterns within the data, resulting in improved accuracy in vaccine uptake predictions.



![Random Model  Comparison](https://github.com/pmjustafort/flushotlearning/assets/137816262/c95b4871-8bd9-4fbc-bdd0-2f5fbb6ba119)




![Random Tuned New Features (SelectedModel)](https://github.com/pmjustafort/flushotlearning/assets/137816262/c4792e57-aed6-4b33-abd1-3d178660f728)




### **Feature Importance**
In our analysis, we conducted a comprehensive examination of feature importance within our best-performing model, "Tuned Random Forest (New Features)." This model exhibited exceptional predictive capabilities, and understanding the significance of different features, grouped by category, sheds light on the factors driving vaccine uptake predictions.

![Tot Ten Features (3)](https://github.com/pmjustafort/flushotlearning/assets/137816262/ece3af69-dac9-4034-a194-73f0b82483a3)


Opinion: Several features emerged as highly influential in our model. First and foremost, "Opinion about H1N1 Vaccine's Side Effects (opinion_h1n1_sick_from_vacc)" was the most influential feature. It reflects individuals' concerns about potential side effects of the H1N1 vaccine, which strongly impact their decisions regarding seasonal flu vaccination. Following closely, "Opinion about Seasonal Vaccine's Effectiveness (opinion_seas_vacc_effective)" ranked second in importance. Individuals' belief in the vaccine's ability to protect against the flu plays a critical role in their decision to get vaccinated. Opinions about the effectiveness and risks associated with both H1N1 and seasonal vaccines ("Opinion about H1N1 Vaccine's Effectiveness" and "Opinion about Seasonal Vaccine's Risk") also significantly influenced vaccine decisions. Additionally, beliefs about the risks associated with the H1N1 vaccine ("Opinion about H1N1 Vaccine's Risk") played a notable role.

Health and Behavior:  Health Insurance Status was found to be influential, indicating that access to healthcare resources and information may affect vaccination choices. Additionally, specific age groups, such as those between 55 and 64 years old ("Age Group: 55 - 64 Years"), exhibited a noteworthy impact. Age can be a significant factor in vaccine decision-making.

Vaccine History and Doctor Recommendation:  The historical behavior of individuals played a significant role. Surprisingly, individuals' previous experience with the H1N1 vaccine ("Prior H1N1 Vaccine History: h1n1_vaccine") was a strong predictor of seasonal flu vaccine uptake. This suggests that past vaccination behavior is a robust indicator of future vaccination decisions. Furthermore, the presence of a doctor's recommendation for the H1N1 vaccine ("Doctor's Recommendation for H1N1 Vaccine: doctor_recc_h1n1") also played a vital role. Healthcare professionals' endorsements carry substantial weight in influencing individuals to take the seasonal flu vaccine.

It's worth noting that there is an unidentified sector of activities that appears to have a significant impact on vaccine uptake. Unfortunately, due to limitations in the available data, we are unable to identify or analyze this sector further. Understanding the nature and characteristics of this unidentified sector could provide valuable insights into vaccination behavior but remains a challenge without additional information.


## **Conclusions And Recommendations**

Our thorough investigation into the prediction of seasonal flu vaccine uptake has showcased the remarkable effectiveness of machine-learning models. Through rigorous evaluation, we identified "Tuned Random Forest (New Features)" as the indisputable frontrunner among the models. This model consistently delivered outstanding results, boasting the highest Test Recall at 0.729 and the highest Test F1-score at 0.754, emphasizing its robust predictive capabilities. Additionally, its Test ROC AUC of 0.851 underscores its ability to effectively distinguish between vaccine takers and non-takers.

Furthermore, our analysis has shed light on the pivotal roles played by specific feature categories. Features associated with individual behaviors, such as behavioral_avoidance and behavioral_face_mask, emerged as paramount drivers, along with opinion-based variables, notably opinion_h1n1_risk and opinion_seas_vacc_effective. The presence of doctor recommendations (doctor_recc_h1n1) and educational attainment (education) were also prominent factors, reaffirming their profound influence on vaccination decisions.

In light of these findings, we propose two key recommendations to enhance seasonal flu vaccine uptake rates:

Promote Health Literacy and Education: Our analysis underscores the significant impact of education on vaccination decisions. Public health campaigns should prioritize health literacy and education initiatives to provide individuals with accurate information about vaccine effectiveness and safety. By addressing misconceptions and increasing awareness, we can empower individuals to make informed choices regarding vaccination.

Address Cost Barriers: The cost of vaccines and associated healthcare services can be a significant barrier to vaccine uptake. Policymakers and healthcare providers should explore strategies to reduce or eliminate the financial burden of vaccination for individuals, especially for those in underserved communities. This could include subsidizing vaccine costs, expanding insurance coverage, or providing free vaccination clinics.

While our investigation identified an unidentified sector of activities with a substantial impact on vaccine uptake, data constraints prevented us from further dissecting this phenomenon. Nevertheless, our findings underscore the critical importance of understanding and leveraging these key features in designing evidence-based strategies to enhance public health campaigns and policies. We are optimistic that the insights gleaned from this study, coupled with our recommendations, will empower public health initiatives and contribute to improved seasonal flu vaccine uptake rates.


## **Next Steps**

Our current analysis has offered valuable insights into predicting seasonal flu vaccine uptake. To advance our understanding and practical impact, we suggest the following next steps:

-Feature Interaction Analysis: Investigate how various features interact to influence vaccine uptake, revealing nuanced decision-making factors.

-The sector of Activities Identification: Explore alternative data sources or methods to uncover details about the unidentified sector of activities, enhancing the depth of our predictions.

-Temporal Analysis: Examine how vaccine uptake patterns change over time and identify temporal factors influencing decisions.

-Real-World Validation: Collaborate with healthcare practitioners to validate our model in real-world healthcare settings, optimizing it for practical deployment.

These steps will expand our research and contribute to a more comprehensive understanding of seasonal flu vaccine uptake, potentially informing evidence-based strategies for public health initiatives.


## Further Details



## **Repository Structure**


