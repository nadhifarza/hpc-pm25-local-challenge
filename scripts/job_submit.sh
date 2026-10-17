#!/bin/bash
#SBATCH --job-name=PM25_Analysis_HPC
#SBATCH --output=outputs/log_%j.out
#SBATCH --error=outputs/error_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --time=00:30:00
#SBATCH --partition=compute

echo "=================================================="
echo "Job HPC Dimulai pada: $(date)"
echo "Berjalan di Node: $(hostname)"
echo "=================================================="

# Memuat modul lingkungan Python di superkomputer
module load python/3.9

# Menjalankan program utama
python3 scripts/process_pm25.py

echo "=================================================="
echo "Job HPC Selesai pada: $(date)"
echo "=================================================="