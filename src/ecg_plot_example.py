import wfdb
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Örnek kayıt
record_id = "100"
record = wfdb.rdrecord(record_id, pn_dir="mitdb")

signal = record.p_signal[:, 0]
fs = record.fs

# İlk 10 saniye (daha temiz görünür)
signal = signal[:10 * fs]

# R-peak bul
peaks, _ = find_peaks(
    signal,
    prominence=0.6,
    distance=int(0.4 * fs)
)

# Grafik
plt.figure(figsize=(12, 4))
plt.plot(signal, label="ECG Signal")
plt.plot(peaks, signal[peaks], "ro", label="R-peaks")
plt.title(f"ECG Signal with R-peaks (Record {record_id})")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.legend()
plt.tight_layout()

# KAYDET
plt.savefig("../data/ecg_example.png", dpi=300)
plt.show()
