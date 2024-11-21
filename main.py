# Memuat modul yang dibutuhkan
from time import sleep
#from os import system as execute
import cv2
import numpy as np

# Membiarkan sistem sleep untuk menginisialisasi kamera
sleep(1.5)

# Memulai menangkap video dengan kamera
cv2.startWindowThread()
capture = cv2.VideoCapture(0)

# Mengatur pendeteksian orang dengan HOG-SVM
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#hog.setSVMDetector(cv2.HOGDescriptor_getDaimlerPeopleDetector())

# Mengatur variabel yang dibutuhkan di dalam while loop
whileLoopIterator = True # Selama bernilai True, while loop akan terus berjalan
amt = 0 # Kondisi awal jumlah orang yaitu nol

# While loop yg akan selalu berjalan
# Sampai user menginterupsi dengan menekan huruf "Q" pada keyboard
while(whileLoopIterator):
    ret,frame = capture.read() # membaca tangkapan video
    frame = cv2.resize(frame, (400, 300)) # mengatur ukuran tangkapan video

    #B, G, R = cv2.split(frame) # memecah kanal-kanal spektrum warna dari tangkapan video
    # untuk meningkatkan kecerahan dan kontras
    #B = cv2.equalizeHist(B) # mengatur kanal spektrum warna biru
    #G = cv2.equalizeHist(G) # mengatur kanal spektrum warna hijau
    #R = cv2.equalizeHist(R) # mengatur kanal spektrum warna merah
    #frame = cv2.merge((B,G,R)) # menggabungkan ketiga kanal spektrum
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # mengubah menjadi hitam putih

    # mulai mendeteksi
    # nilai di dalam tuple `winStride` dan `padding` dapat dicoba-coba (trial & error)
    humans,_ = hog.detectMultiScale(frame, winStride=(6, 6), padding=(9, 9), scale=1.02)

    # hitung jumlah orang yang saat ini terdeteksi
    currentAmt = len(humans)

    # algoritma pengaturan AC saat mendeteksi peambahan jumlah orang
    if currentAmt > amt:
        print("Jumlah orang bertambah")

        if amt == 0:
            # Jika jumlah orang sebelumnya 0 dan bertambah, nyalakan AC
            #execute("ir-ctl -d /dev/lirc0 --send=/home/pesekcuy/remote/panasonic-power-on.txt")
            print("Nyalakan AC")
        else:
            # Jika jumlah orang sebelumnya bukan 0 dan bertambah, turunkan temperatur
            #execute("ir-ctl -d /dev/lirc0 --send=/home/pesekcuy/remote/panasonic-temp-down.txt")
            print("Suhu turun")

        amt = currentAmt

    # algoritma pengaturan AC saat mendeteksi pengurangan jumlah orang
    elif currentAmt < amt:
        print("Jumlah orang berkurang")

        if currentAmt == 0:
            # Jika jumlah orang menjadi 0, matikan AC
            #execute("ir-ctl -d /dev/lirc0 --send=/home/pesekcuy/remote/panasonic-power-off.txt")
            print("Matikan AC")
        else:
            # Jika jumlah orang berkurang tapi tidak menjadi 0, naikkan temperatur
            #execute("ir-ctl -d /dev/lirc0 --send=/home/pesekcuy/remote/panasonic-temp-up.txt")
            print("Suhu naik")

        amt = currentAmt

    # memvisualisasikan pendeteksian orang dengan bingkai persegi
    humans = np.array([[x, y, x + w, y + h] for (x, y, w, h) in humans])
    for (xA, yA, xB, yB) in humans:
        # menggambar bingkai putih di sekitar orang yang terdeteksi
        cv2.rectangle(frame, (xA, yA), (xB, yB), (255, 255, 255), 2)

    cv2.imshow('frame',frame) # menampilkan tangkapan video berikut pendeteksian orang jika ada

    sleep(0.5) # membiarkan sistem sleep agar kamera tidak bekerja terlalu keras

    if cv2.waitKey(1) & 0xFF == ord('q'):
        # menekan tombol "Q" pada keyboard akan menghentikan program ini
        whileLoopIterator = False

# Mengakhiri tangkapan video dan menutup jendela visualisasi
# Dieksekusi jika while loop di atas diinterupsi
capture.release()
cv2.destroyAllWindows()
