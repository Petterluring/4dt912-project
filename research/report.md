# Project Report
**Author**: Petter Gustafsson (pg22jw)   
**Course**: Advanced Information Visualization and Applications (4DT912)


Task 2
* Data and domain: Describe the dataset and its domain context. What information,
patterns, or insights might users seek?
* Analytical goal: Define the overall purpose of your visual analytics interface. What
should users be able to understand or discover by exploring the data? Identify specific,
domain-relevant analytical tasks that users should be able to perform. Explain how these
tasks contribute to the overall analytical goal.
* Design implications: Briefly discuss how these tasks could inform the choice of
projection visualization, supporting visualizations, and interactions.

## Dataset

The [**Students' Dropout and Academic Success**](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success) dataset originates from the educational domain and provides insights into students' academic performance, dropout and graduation outcomes, demographics, and educational and socio-economic backgrounds. The dataset was supported by the SATDAP – Capacitação da Administração Pública program and is available through the [**UCI Machine Learning Repository**](https://archive.ics.uci.edu/), where it was originally used to develop and evaluate a classification model for predicting student dropout and academic success.

The dataset comprises more than 4,000 students, each described by 37 attributes, with no missing values. It follows a tabular structure in which each row represents an individual student and each column represents a student attribute. These attributes cover various aspects of students' backgrounds and academic circumstances, including marital status, course enrolment, attendance-related information, educational qualifications, nationality, parental education levels, and academic grades. The attributes encompass several data types, including numerical, nominal, ordinal, and binary variables.

Some concerns include the semantics of certain attributes, including inflation and umemployment rate, and GDP. While these attributes are generally well-defined and widely understood concepts, their meaning in the context of attributes describing individual students is ambiguous. For instance, it is unclear what it means for a student to have an inflation rate of 2.8%. Consequently, any analyses involving dimensionality reduction methods that include these attributes should be interpreted with caution, as their relevance and meaning in the context of individual students are questionable. Excluding these attributes from such analyses should therefore be considered.

### Data and domain part of Task 2

* The dataset describes students' academic performance, demographics, educational, and socio-economic backgorunds etc.
* It has a target feature stating describing whether a student dropped out or graduated
* Appropriate information, patterns, or insights that users might seek could therefore be...
    * Connections between dropout/graduation rates and student attributes, such as academic performance or socio-economic background
    * Connections between admission grades and student attributes, such as parental educational levels


### Dataset characteristics

This section outlines some dataset characteristics that should be considered during future preprocessing.

Figure 1 in *Appendix* presents the correlation matrix of the numerical attributes. The matrix reveals generally weak correlations between several attributes, whereas the curricular unit attributes tend to exhibit strong correlations with one another. For instance, the number of credited curricular units in the first semester is highly correlated with that of the second semester (0.94). This is likely due to the two features having similar value distributions across semesters, as illustrated by their histograms in Figure 2 in *Appendix*. Similar patterns can be observed among the attributes describing approved and enrolled curricular unit credits across the two semesters.

These findings suggest that removing one of the semesters for certain curricular unit attributes should be considered during future preprocessing. Retaining both semesters may introduce redundant information, as the corresponding features appear to capture largely similar patterns.

### Justification of suitability

The dataset is well-suited for dimensionality reduction and projection for several reasons. Most notably, it contains numerous (>10) numerical dimensions, including admission grades and various attributes describing curricular units, making it difficult to represent the data meaningfully in three dimensions or fewer.

Furthermore, the dataset contains many categorical features that can be used to encode data points in the reduced space, enabling the exploration of patterns across multiple dimensions. For instance, colouring students based on their academic outcomes, such as dropout or graduation status, may reveal distinct clusters or groupings associated with these outcomes.

Although some numerical attributes may be excluded during preprocessing, as discussed in the previous section, the dataset still offers considerable opportunities to incorporate categorical features. Techniques such as one-hot encoding can transform these features into numerical representations, allowing them to be included in the dimensionality reduction process and potentially enriching the resulting projections.


## Analytical goal

* The overall purpose of my visualization is to allow users to explore/discover patterns of academic success accross different student attributes. 


## Design implications


# Disclosures

- AI has been used to improve grammar and semantics in this text.

# Appendix


![Correlations of numerical features](imgs/correlations.png)

![Distributions of numerical features](imgs/distributions.png)