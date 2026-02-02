import wfdb
import numpy as np
import pandas as pd
from scipy.signal import find_peaks

def extract_features(record_id, label):
    record = wfdb.rdrecord(record_id, pn_dir="mitdb")
    signal = record.p_signal[:, 0]
    fs = record.fs

    duration = 30
    signal = signal[:duration * fs]

    peaks, _ = find_peaks(
        signal,
        prominence=0.6,
        distance=int(0.4 * fs)
    )

    rr = np.diff(peaks) / fs
    bpm = 60 / rr

    diff_rr = np.diff(rr)

    rmssd = np.sqrt(np.mean(diff_rr ** 2))
    sdnn = np.std(rr)
    pnn50 = np.sum(np.abs(diff_rr) > 0.05) / len(diff_rr) * 100

    return {
        "record_id": record_id,
        "mean_rr": np.mean(rr),
        "median_rr": np.median(rr),
        "std_rr": np.std(rr),
        "min_rr": np.min(rr),
        "max_rr": np.max(rr),
        "mean_bpm": np.mean(bpm),
        "std_bpm": np.std(bpm),
        "rmssd": rmssd,
        "sdnn": sdnn,
        "pnn50": pnn50,
        "label": label
    }


print("DOSYA ÇALIŞTI")

# -----------------------------
# KAYITLAR
# -----------------------------
data = []
data.append(extract_features("100", label=0))  # normal
data.append(extract_features("200", label=1))  # aritmi

df = pd.DataFrame(data)

# -----------------------------
# CSV YAZ
# -----------------------------
df.to_csv("../data/ecg_features.csv", index=False)

print("\nCSV OLUŞTURULDU:")
print(df)


