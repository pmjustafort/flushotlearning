# **Predicting Seasonal Flu Vaccines**

## **Authors**:
Aung Si and Paul Justafort.

![image](https://github.com/pmjustafort/flushotlearning/assets/137816262/39cf3ecf-8f74-4571-aa6e-f6d4a872e4d4)



## **Overview**



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

Model performance metrics
Our analysis involved the evaluation of multiple machine-learning models using several essential performance metrics. These metrics include Test Recall, Train Recall, Test F1, Train F1, Test ROC AUC, and Train ROC AUC. Among the models, "Random Forest (New Features)" and "Tuned Random Forest (New Features)" consistently displayed the highest performance, excelling in Test Recall and achieving a strong Test F1-score. These metrics highlight the potential of these models in effectively identifying individuals likely to take the seasonal flu vaccine. Additionally, both Random Forest models demonstrated robust training data fit, as evident from their high Train ROC AUC scores. Further details and insights can be derived from these metrics to guide our ongoing analysis.


Model Comparison
In our rigorous model evaluation, we assessed the performance of various machine learning models using key metrics, including Test Recall, Train Recall, Test F1, Train F1, Test ROC AUC, and Train ROC AUC. Among these models, "Random Forest (New Features)" and "Tuned Random Forest (New Features)" consistently outperformed the others. They achieved the highest Test Recall, with scores of 0.731 and 0.729, respectively, showcasing their proficiency in correctly identifying individuals likely to take the seasonal flu vaccine. Notably, "Tuned Random Forest (New Features)" achieved the highest Test F1-score at 0.754, highlighting an impressive balance between precision and recall. A significant contributor to their exceptional performance was the incorporation of feature engineering and hyperparameter tuning, which significantly enhanced their predictive capabilities. These techniques allowed the models to capture intricate patterns within the data, resulting in improved accuracy in vaccine uptake predictions. Further analysis is underway to gain deeper insights from these high-performing models and guide our ongoing efforts.


Feature Importance
In our analysis, we conducted a thorough examination of feature importance within our best-performing model, "Tuned Random Forest (New Features)." This model exhibited exceptional predictive capabilities and understanding the importance of different features sheds light on the factors driving vaccine uptake predictions.
We discovered that several key feature categories played a significant role in the model's predictions:

	Behavioral Features: Variables related to individual behaviors, including “behavioral_avoidance”, “behavioral_face_mask”, “behavioral_wash_hands”, and “behavioral_large_gatherings”, were found to be highly influential. These features reflect proactive measures individuals take to protect themselves against the flu, thus impacting their likelihood of taking the seasonal flu vaccine.

	Opinion Features: Features such as “opinion_h1n1_vacc_effective”, “opinion_h1n1_risk”, and “opinion_seas_vacc_effective” were also prominent. These variables capture individuals' perceptions of vaccine effectiveness and the perceived risk associated with the flu, which can strongly influence their vaccine decisions.

	Doctor Recommendation: The presence of a doctor recommendation (doctor_recc_h1n1) emerged as a significant predictor. A healthcare professional's endorsement can carry substantial weight in influencing an individual's decision to take the vaccine.

	Education Level: Education, as represented by the "education" feature, was observed to have a notable impact. Higher levels of education often correlate with better health literacy and a greater understanding of the benefits of vaccination.

	H1N1 Vaccine History: Individuals' prior experience with the H1N1 vaccine (h1n1_vaccine) was found to be influential, suggesting that past vaccination behavior is a strong predictor of seasonal flu vaccine uptake.

Additionally, there is an unidentified sector of activities that appears to have a significant impact on vaccine uptake. Unfortunately, due to limitations in the available data, we are unable to identify or analyze this sector further. Understanding the nature and characteristics of this unidentified sector could provide valuable insights into vaccination behavior but remains a challenge without additional information.


## **Conclusions**

Our in-depth investigation into seasonal flu vaccine uptake prediction has yielded compelling evidence of the effectiveness of machine learning models. Through rigorous evaluation, we identified "Tuned Random Forest (New Features)" as the unequivocal leader among the models. This model consistently achieved remarkable results, boasting the highest Test Recall at 0.729 and the highest Test F1-score at 0.754, emphasizing its robust predictive capabilities. Additionally, its Test ROC AUC of 0.851 underscores its ability to effectively distinguish between vaccine takers and non-takers.
Furthermore, our analysis unveiled the pivotal roles played by specific feature categories. Features related to individual behaviors, such as behavioral_avoidance and behavioral_face_mask, were key drivers, along with opinion-based variables, such as opinion_h1n1_risk and opinion_seas_vacc_effective. The presence of doctor recommendations (doctor_recc_h1n1) and educational attainment (education) were also prominent factors, substantiating their influence on vaccination choices.
While our investigation identified an unidentified sector of activities with a substantial impact on vaccine uptake, data constraints prevented us from further dissecting this phenomenon.
In light of these findings, we conclude our analysis on a compelling note, recognizing the power of machine learning in predicting vaccine uptake and the profound influence of specific features. We anticipate that the insights derived from this study will inform evidence-based strategies to enhance public health campaigns and policies, ultimately leading to improved seasonal flu vaccine uptake rates.


## **Next Steps**

Our current analysis has offered valuable insights into predicting seasonal flu vaccine uptake. To advance our understanding and practical impact, we suggest the following next steps:

	Feature Interaction Analysis: Investigate how various features interact to influence vaccine uptake, revealing nuanced decision-making factors.

	The sector of Activities Identification: Explore alternative data sources or methods to uncover details about the unidentified sector of activities, enhancing the depth of our predictions.

	Temporal Analysis: Examine how vaccine uptake patterns change over time and identify temporal factors influencing decisions.

	Real-World Validation: Collaborate with healthcare practitioners to validate our model in real-world healthcare settings, optimizing it for practical deployment.

These steps will expand our research and contribute to a more comprehensive understanding of seasonal flu vaccine uptake, potentially informing evidence-based strategies for public health initiatives.


## Further Details



## **Repository Structure**
