# Automated Clinical Tabular EDA Pipeline
Reusable Python pipeline for automated exploratory data analysis (EDA), data quality auditing, feature diagnostics, and machine-learning readiness assessment for clinical tabular datasets.

## Overview
This project automates an end-to-end EDA workflow for structured clinical datasets, transforming raw tabular data into diagnostic insights, visual analytics, and model-readiness reports.
The pipeline supports any clinical CSV dataset by specifying only:
python
dataset.csv
target_column
and automatically performs:
- Data quality auditing  
- Missingness diagnostics  
- Univariate and multivariate EDA  
- Correlation and multicollinearity assessment  
- Outlier diagnostics  
- PCA structure exploration  
- Feature importance screening  
- Automated PDF reporting  
- Model readiness assessment

## Features
### Data Quality Audit
- Missing value assessment
- Duplicate detection
- Data type profiling
- Summary statistics export

### Exploratory Data Analysis
- Distribution plots
- Target-wise boxplots
- Categorical count plots
- Correlation heatmaps

### Diagnostic Analytics
- IQR-based outlier detection
- Variance Inflation Factor (VIF)
- Missingness heatmaps
- Multicollinearity screening

### Advanced EDA
- Principal Component Analysis (PCA)
- Random Forest feature importance
- Model readiness scorecard

### Reporting
- Automated PDF EDA report
- Summary statistics CSV
- Exported figures

## Pipeline Architecture
text
Input Data
↓
Data Quality Audit
↓
Distribution Profiling
↓
Correlation + VIF Diagnostics
↓
Outlier Detection
↓
PCA Structure Analysis
↓
Feature Importance Screening
↓
Model Readiness Assessment
↓
Automated Report Generation


## Example Outputs
Generated artifacts include:
text
reports/
├── EDA_Report.pdf
└── summary_stats.csv

figures/
├── correlation.png
├── pca.png
├── feature_importance.png
└── variable_plots...

## Installation
bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels reportlab missingno

## Usage
Run on any clinical dataset:

   python
FILE="heart_disease.csv"
TARGET="target_binary"

Execute notebook or pipeline and generate automated diagnostics.
## Example Applications
Suitable for:
- Clinical risk prediction datasets  
- Epidemiological tabular data  
- Electronic health record feature exploration  
- Machine learning data readiness assessment  
- Biomedical feature diagnostics

## Methodological Components
This pipeline integrates:
- Descriptive EDA  
- Diagnostic EDA  
- Multivariate structure analysis  
- Predictive signal screening  
- Reproducible reporting

## Future Extensions
Planned additions:
- SHAP-ready diagnostics  
- Automated feature engineering checks  
- Time-series EDA extension  

## Repository Goal
This repository is designed as both:
- A reusable EDA framework  
- A portfolio demonstration of automated analytical pipeline development

## Author
Ekundayo Olorunfemi Matthew
Interests:
- Statistical Modelling  
- Explainable AI  
- Clinical Analytics
- Machine Learning
