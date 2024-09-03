# AgriHealth Soil Detector

This repository contains tools and datasets for analyzing soil health and providing crop recommendations.

## Files Description

1. **Car Soil Detector.py**: A Python script that uses IoT data to assess soil conditions in agricultural fields.
2. **Check soil for crop.ipynb**: A Jupyter notebook that analyzes soil data to suggest suitable crops.
3. **Crop recommendation.csv**: A dataset containing crop recommendations based on various soil parameters.

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Required Python libraries: pandas, numpy, matplotlib (for the notebook)

#### Running the deom
To run the `Demo soil detector.py` script, execute the following command in your terminal:
   ```bash
   streanlit run Demo Soil Detector.py
   ```


#### Car Soil Detector Script
To run the `Car Soil Detector.py` script, execute the following command in your terminal:
   ```bash
   python Car Soil Detector.py
   ```

#### Check Soil for Crop Notebook
To analyze soil data using the notebook:
1. Launch Jupyter Notebook or JupyterLab:
   ```bash
   jupyter notebook
   ```
   or
   ```bash
   jupyter lab
   ```

2. Open the `Check soil for crop.ipynb` file from the Jupyter interface and run the cells as per the instructions within the notebook.

### Using the Crop Recommendation Dataset
The `Crop recommendation.csv` file can be used in data analysis tools or imported in Python scripts as follows:
   ```python
   import pandas as pd
   crop_data = pd.read_csv('Crop recommendation.csv')
   print(crop_data.head())
   ```

## Contributing
Contributions to improve the tools or dataset are welcome. Please read `CONTRIBUTING.md` for guidelines on how to make a contribution.

## Acknowledgments
- Thanks to the team and all contributors who have helped develop these tools and datasets.
```

