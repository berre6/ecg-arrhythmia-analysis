# ECG Arrhythmia Analysis 🫀

This project analyzes real ECG signals from the **MIT-BIH Arrhythmia Database**
to detect arrhythmia using both **rule-based methods** and a **machine learning model**.

The goal is to build an **explainable and reproducible ECG analysis pipeline**,
starting from raw signals and ending with classification results.

---

## 📊 Dataset
- Source: MIT-BIH Arrhythmia Database
- Records used:
  - Normal: 100, 101, 102, 103
  - Arrhythmia: 200, 201, 202, 203
- Signal duration: first 30 seconds
- Sampling frequency: record-dependent (MIT-BIH standard)

---

## ⚙️ Feature Extraction
Heart Rate Variability (HRV) features extracted from R–R intervals:

- Mean RR interval
- Median RR interval
- RR standard deviation (STD)
- Minimum RR
- Maximum RR
- Mean BPM
- BPM standard deviation
- RMSSD
- SDNN
- pNN50

All extracted features are saved into:

data/ecg_features.csv


---

## 🧠 Methods

### 1️⃣ Rule-Based Analysis
- R-peaks detected using `scipy.signal.find_peaks`
- RR intervals and BPM calculated
- Threshold-based logic used to analyze rhythm variability

### 2️⃣ Machine Learning
- Model: Logistic Regression
- Features: HRV features listed above
- Train/Test split: 75% / 25%
- Library: scikit-learn

⚠️ **Note:**  
Due to the small dataset size, ML results may appear overly optimistic.
The goal is demonstration and explainability, not clinical deployment.

---

## ▶️ How to Run

Install dependencies:
```bash
pip install -r requirements.txt

Generate features:
python src/plot_first_ecg.py

Train ML classifier:
python src/ml_classifier.py


---




📈 Example Output

-Extracted HRV features saved as CSV
-Classification accuracy and confusion matrix printed in terminal


🧩 Project Structure
ecg-arrhythmia-analysis/
├── data/
│   └── ecg_features.csv
├── src/
│   ├── plot_first_ecg.py
│   └── ml_classifier.py
├── requirements.txt
└── README.md


🚀 Future Work

-Increase dataset size using more MIT-BIH records
-Add advanced HRV features
-Compare multiple ML models (SVM, Random Forest)
-Time-domain and frequency-domain analysis
-Visualization of feature importance


👤 Author
Berre


---

## 🐙 FINISH COMMIT
```powershell
git add README.md
git commit -m "Improve README with methodology, ML, and future work"
git push



