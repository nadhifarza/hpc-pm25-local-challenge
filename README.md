STUDI KASUS PRAKTIKUM HPC: Analisis Prediksi Polusi Udara (PM2.5) Berbasis Data IoT Menggunakan Skrip Batch HPC

1. Latar Belakang Masalah

Di kawasan regional Asia Tenggara, termasuk Indonesia dan Thailand, isu polusi udara akibat partikel debu halus (PM2.5) menjadi tantangan kesehatan masyarakat yang serius. Pemerintah dan peneliti sering kali kesulitan memproses data sensor IoT yang masif secara real-time dengan komputer biasa.

Dalam studi kasus ini, Anda akan bertindak sebagai Integrator IT yang bertugas mengambil data mentah dari sensor IoT, melakukan kalibrasi/pembersihan data skala besar, dan menjalankan skrip pemrosesan paralel pada lingkungan High Performance Computing (HPC) berbasis Slurm Workload Manager.

2. Skenario & Tujuan Pembelajaran

Skenario: Tim riset lingkungan menyediakan file data sensor mentah berukuran besar (sensors_raw.csv). Anda harus membuat skrip pemrosesan data berbasis Python dan skrip batch job HPC untuk mengeksekusi komputasi tersebut di superkomputer.

Tujuan:

1. Memahami alur kerja (workflow) pengiriman job ke kluster HPC menggunakan SSH dan Terminal Linux.

2. Menulis skrip Python untuk pembersihan dan analisis data sensor secara efisien.

3. Mengonfigurasi skrip batch Slurm (.sh) untuk alokasi resource node superkomputer.
