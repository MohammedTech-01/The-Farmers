# Streamlit Plant Health Dashboard

This repository contains the necessary files for setting up a Streamlit web application that visualizes plant health data in Saudi Arabia, along with the associated datasets.

## Files Description

1. **requirements.txt**: A list of Python libraries needed to run the Streamlit application.
2. **streamlit_app_with_css.py**: The main Python script for the Streamlit application that includes custom CSS for styling.
3. **Adjusted_Saudi_Arabia_Plant_Dataset.csv**: A dataset adjusted for specific analysis related to plant health in Saudi Arabia.
4. **Detailed_Plant_Health_Saudi_Arabia.csv**: A comprehensive dataset containing detailed records of plant health across various regions in Saudi Arabia.

## Getting Started

### Prerequisites
Ensure you have Python 3.8+ installed on your system. The application relies on several Python libraries listed in `requirements.txt`.

### Setup

1. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Execute the following command in your terminal to start the Streamlit application:
   ```bash
   streamlit run streamlit_app_with_css.py
   ```

The application will launch in your web browser, where you can interact with the visualizations and data analysis.

### Data Analysis

The CSV files can be used to analyze plant health trends and insights:
- **Adjusted_Saudi_Arabia_Plant_Dataset.csv**
- **Detailed_Plant_Health_Saudi_Arabia.csv**

These files can be imported into Python scripts or Jupyter notebooks for further analysis:
   ```python
   import pandas as pd
   data = pd.read_csv('Adjusted_Saudi_Arabia_Plant_Dataset.csv')
   print(data.head())
   ```

## Contributing
Contributions to improve the application or datasets are welcome. Please read `CONTRIBUTING.md` for guidelines on how to make a contribution.

## Acknowledgments
- Thanks to the team and all contributors who have helped develop and refine this dashboard and the datasets.
