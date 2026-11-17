# Project Report
**Author**: Petter Gustafsson (pg22jw)   
**Course**: Advanced Information Visualization and Applications (4DT912)

* Project report: Add a dataset section describing the dataset, its source (check), domain (check), size (check),
attributes (check), and relevant characteristics (??).   
* Include a brief justification explaining why the dataset is suitable for projection
visualization.

## Dataset (Task 1)

The [**Students' Dropout and Academic Success**](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success) dataset originates from the educational domain and provides insights into students' academic performance, dropout and graduation outcomes, demographics, and educational and socio-economic backgrounds. The dataset was supported by the SATDAP – Capacitação da Administração Pública program and is available through the [**UCI Machine Learning Repository**](https://archive.ics.uci.edu/), where it was originally used to develop and evaluate a classification model for predicting student dropout and academic success.

The dataset comprises more than 4,000 students, each described by 37 attributes, with no missing values. It follows a tabular structure in which each row represents an individual student and each column represents a student attribute. These attributes cover various aspects of students' backgrounds and academic circumstances, including marital status, course enrolment, attendance-related information, educational qualifications, nationality, parental education levels, and academic grades. The attributes encompass several data types, including numerical, nominal, ordinal, and binary variables.




### Justification of suitability (Task 1)

The dataset is suitable for projection for several reasons, the major being the existence of many (>10) numerical dimensions, including admission grades and varying curricular units, which cannot be represented in three dimensions or lower. Further, the many nominal features allows us to encode the points in the reduced space based on these values, making the potential analyses multivariate.

* DR may provide insigths regarding if students are grouped based on target categories. 

# Disclosures

- AI has been used to improve grammar and semantics in the text.