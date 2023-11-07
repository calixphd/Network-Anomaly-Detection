# Network Anomaly Detection with MetaTune

This repository hosts the implementation of an anomaly detection system focused on network security. The system utilizes the `metatune` library to automatically select and tune machine learning models best suited for identifying potential security threats within network traffic.

## Installation

To set up the project environment, follow these steps:

```bash
git clone https://github.com/calixphd/Network-Anomaly-Detection
cd Network-Anomaly-Detection
pip install -r requirements.txt
```

Please replace `your-username` and `your-repository-name` with your actual GitHub username and repository name.

## Project Description

The anomaly detection system is developed to classify network activities into normal or potentially malicious categories. The classification process involves preprocessing network traffic data, feature scaling, dimensionality reduction, and the application of various machine learning algorithms. The `metatune` library is employed to optimize model selection and hyperparameter tuning for improved detection performance.

## Dataset

The project uses network traffic datasets, which are expected to be in CSV format:

- `train.csv`: Training dataset with labeled network traffic data.
- `test.csv`: Testing dataset for evaluating the model's performance.

These datasets should contain features indicative of network behavior and a target label for anomaly detection.

## Usage

The codebase is structured to guide users through the following process:

1. **Data Loading and Preprocessing**: Load the datasets and prepare them for analysis by handling missing values and encoding categorical features.
2. **Exploratory Data Analysis (EDA)**: Explore the data to understand the distribution of the classes (normal vs. anomalous).
3. **Feature Engineering**: Apply Principal Component Analysis (PCA) to reduce the dimensionality of the data and visualize important components.
4. **Model Selection and Hyperparameter Tuning**: Define an optimization function and use `metatune` in conjunction with Optuna to find the best model and hyperparameters.
5. **Model Training**: Train the optimal model on the entire training dataset.
6. **Performance Evaluation**: Assess the model's performance using appropriate metrics, such as the F1 score, precision, recall, and ROC AUC.
7. **Result Visualization**: Generate visual representations of performance metrics, including confusion matrices and ROC curves.
8. **Inference**: Use the trained model to predict anomalies on new, unseen network data and output the results.

## Running the Notebooks

The repository includes Jupyter notebooks that provide a step-by-step walkthrough of the anomaly detection workflow, from data preparation to model inference.

## Contributing

Contributions to enhance the anomaly detection system are welcome. Please refer to `CONTRIBUTING.md` for contribution guidelines.

## License

This project is open-sourced under the MIT License. See the `LICENSE.md` file for more details.

## Acknowledgments

- Kudos to [ches-001](https://github.com/ches-001) for the development of the `metatune` library.
- The project uses the Optuna framework to manage the model selection and hyperparameter optimization processes.
