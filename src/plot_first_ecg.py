import wfdb
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from scipy.signal import welch

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

    # --- Frequency Domain HRV ---
    if len(rr) > 4:
        rr_interp = rr - np.mean(rr)

        freqs, psd = welch(rr_interp, fs=1.0, nperseg=min(len(rr_interp), 256))

        lf_mask = (freqs >= 0.04) & (freqs < 0.15)
        lf_power = np.trapz(psd[lf_mask], freqs[lf_mask])

        hf_mask = (freqs >= 0.15) & (freqs < 0.4)
        hf_power = np.trapz(psd[hf_mask], freqs[hf_mask])

        lf_hf_ratio = lf_power / hf_power if hf_power != 0 else 0
    else:
        lf_power = 0
        hf_power = 0
        lf_hf_ratio = 0

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
        "lf_power": lf_power,
        "hf_power": hf_power,
        "lf_hf_ratio": lf_hf_ratio,
        "label": label
    }

print("DOSYA ÇALIŞTI\n")

normal_records = ["100", "101", "102", "103"]
arrhythmia_records = ["200", "201", "202", "203"]

data = []

for rec in normal_records:
    data.append(extract_features(rec, label=0))

for rec in arrhythmia_records:
    data.append(extract_features(rec, label=1))

df = pd.DataFrame(data)

df.to_csv("../data/ecg_features.csv", index=False)

print("CSV OLUŞTURULDU\n")
print(df)


