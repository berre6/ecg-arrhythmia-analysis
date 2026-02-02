import wfdb
import numpy as np
import matplotlib.pyplot as plt

print("DOSYA ÇALIŞTI")

from scipy.signal import find_peaks

# ECG verisini yükle
record = wfdb.rdrecord('100', pn_dir='mitdb')
signal = record.p_signal[:, 0]
fs = record.fs

# R-peak bul
peaks, _ = find_peaks(signal, distance=200, prominence=0.6)

print("Bulunan peak sayısı:", len(peaks))
print("Peak indeksleri:", peaks[:10])

# RR interval hesapla (saniye)
rr_intervals = np.diff(peaks) / fs

print("RR intervals:", rr_intervals[:10])


# RR interval grafiği
plt.figure(figsize=(12, 4))
plt.plot(signal[:2000], label="ECG (ilk 2000 örnek)")
plt.plot(peaks[peaks < 2000], signal[peaks[peaks < 2000]], "ro")
plt.legend()
plt.tight_layout()
plt.show()

# Basit aritmi kontrolü
mean_rr = np.mean(rr_intervals)
std_rr = np.std(rr_intervals)

print(f"Ortalama RR: {mean_rr:.3f} s")
print(f"RR Std (düzensizlik): {std_rr:.3f} s")

if std_rr > 0.15:
    print(" Olası aritmi (RR düzensiz)")
else:
    print(" RR aralıkları düzenli")
