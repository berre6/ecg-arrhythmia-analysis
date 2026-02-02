# ECG Arrhythmia Analysis 

This project analyzes ECG signals using real MIT-BIH Arrhythmia Database records.
It extracts heart rate variability features and applies a rule-based approach
to detect arrhythmia.

## Features Extracted
- Mean RR interval
- RR interval standard deviation
- Minimum RR
- Maximum RR
- Mean BPM
- BPM variability (STD)

## Methodology
1. Load ECG records using `wfdb`
2. Detect R-peaks using `scipy.signal.find_peaks`
3. Compute RR intervals and BPM
4. Apply rule-based decision logic for arrhythmia detection
5. Export features to CSV for further analysis

## Dataset
- Record 100: Normal
- Record 200: Arrhythmia

## Output
- Feature comparison
- Rule-based arrhythmia decision
- `ecg_features.csv` dataset

## Technologies
- Python
- NumPy
- Pandas
- SciPy
- WFDB
- Matplotlib

## Author
Berre
