# Plant Disease Detection System

This repository contains the necessary files for setting up a plant disease detection system using deep learning and simulation scripts for testing the system both with and without drone assistance.

## Files Description

1. **Plant disease detector Model.ipynb**: A Jupyter notebook that details the creation and training of a machine learning model for plant disease detection.
2. **Plant disease model final.pth**: The trained model file that can be loaded to predict plant diseases.
3. **simulate plant disease detector drone.py**: A Python script that simulates a drone-based system for detecting plant diseases in real time.
4. **simulate plant disease detector without drone.py**: A Python script for simulating plant disease detection without the use of a drone.

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Jupyter Notebook or JupyterLab
- Required Python libraries: torch, torchvision, numpy, matplotlib (for both notebook and scripts)
- PyTorch (ensure compatibility with the `.pth` model file)

### Setup

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/Plant-Disease-Detection-System.git
   ```

2. Navigate to the cloned directory:
   ```bash
   cd Plant-Disease-Detection-System
   ```

3. Install the required Python libraries:
   ```bash
   pip install torch torchvision numpy matplotlib
   ```

### Running the Tools

#### Plant Disease Detector Notebook
To use the notebook:
1. Launch Jupyter Notebook or JupyterLab:
   ```bash
   jupyter notebook
   ```
   or
   ```bash
   jupyter lab
   ```

2. Open the `Plant disease detector Model.ipynb` file from the Jupyter interface and run the cells to see the model training process and usage.

#### Simulation Scripts
- To run the drone-based simulation:
   ```bash
   python simulate plant disease detector drone.py
   ```

- To run the simulation without a drone:
   ```bash
   python simulate plant disease detector without drone.py
   ```

### Using the Trained Model
To use the trained model in your projects:
   ```python
   import torch
   model = torch.load('Plant disease model final.pth')
   model.eval()  # Set the model to evaluation mode
   ```

## Contributing
Contributions to improve the models or scripts are welcome. Please read `CONTRIBUTING.md` for guidelines on how to make a contribution.

## Acknowledgments
- Thanks to the team and all contributors who have helped develop and refine these detection systems.
