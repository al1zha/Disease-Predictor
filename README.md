This project is a **Disease Prediction System** using machine learning models trained on symptoms data. The backend API accepts a list of symptoms and predicts the probable disease using multiple classifiers: Decision Tree, Random Forest, and Naive Bayes. The application provides predictions from each model to offer users a comparison and higher confidence in the diagnosis.

**Key Features:**

1. **Symptom Input**:
   1. The API accepts a list of symptoms from the user. Each symptom is mapped to a binary feature vector where each symptom corresponds to a feature in the dataset.
1. **Multiple Classifiers**:
- Three machine learning classifiers are used for predictions:
- **Decision Tree Classifier**.
- **Random Forest Classifier**.
- **Naive Bayes Classifier**.
- The models have been trained using a dataset that includes various symptoms and diseases.
3. **Training Data**:
   1. The system is trained on the "Training.csv" dataset where symptoms are represented as features, and the target labels are diseases.
   1. The dataset includes binary indicators for the presence of specific symptoms and maps them to the associated disease.
3. **Prediction Results**:
- The system returns the predicted disease for each classifier, allowing users to compare results from the different models.
- The predictions are based on the presence of symptoms input by the user.

**Workflow:**

1. **Data Processing**:
   1. The dataset contains symptoms as columns (features) and diseases as the target label (prognosis).
   1. Symptoms provided by the user are transformed into a binary vector (1 if the symptom is present, 0 otherwise).
1. **Model Training**:
- Three machine learning models are trained on the symptoms data:
- **Decision Tree**: A single tree used for classification.
- **Random Forest**: An ensemble of decision trees for more robust predictions.
- **Naive Bayes**: A probabilistic classifier based on Bayes' theorem.
3. **Prediction**:
- The input symptoms are matched against the trained models to predict the probable disease.
- Each model's prediction is returned in the response.

**Endpoints:**

- **GET /**: Serves the homepage (static files).
- **POST /predict**: Accepts a list of symptoms and returns the predicted disease from three different models (Decision Tree, Random Forest, and Naive Bayes).

**Input Data Structure:**

- **Symptoms**:
- sympt oms: A list of strings representing the symptoms.

**Stack:**

- **Backend**: FastAPI for API handling.
- **Machine Learning**: Scikit-learn for implementing the Decision Tree, Random Forest, and Naive Bayes classifiers.
- **Data**: A CSV file containing symptoms and associated diseases.
