import os
import json

# Lokasi folder utama di Drive D:
base_dir = "D:/MuaroJambi_Project"

# Daftar semua folder final, sudah mencakup semua derivatif LiDAR
folders = [
    # Proposal & catatan
    "01_Proposal/Notes",

    # Data
    "02_Data/LiDAR_Raw",
    "02_Data/DEM/DTM",
    "02_Data/DEM/DSM",
    "02_Data/LRM/LRM_10m",
    "02_Data/LRM/LRM_30m",
    "02_Data/LRM/LRM_60m",
    "02_Data/LRM/TPI",
    "02_Data/LRM/TRI",
    "02_Data/LRM/Curvature",
    "02_Data/Hydrology/FlowDirection",
    "02_Data/Hydrology/FlowAccumulation",
    "02_Data/Hydrology/Watershed",
    "02_Data/Hydrology/Kanal",
    "02_Data/Hydrology/Reservoir",
    "02_Data/Vegetation/NDVI",
    "02_Data/Vegetation/CanopyHeight",
    "02_Data/Other_Sensor",

    # Skrip & notebook
    "03_Scripts/ArcPy",
    "03_Scripts/Python",
    "03_Scripts/Notebooks",

    # Referensi & literatur
    "04_References/Jurnal",
    "04_References/Konferensi",
    "04_References/Grey_Literature",
    "04_References/Bibliography",

    # Hasil analisis
    "05_Results/Maps",
    "05_Results/Figures",
    "05_Results/Tables",
    "05_Results/Reports",

    # Fieldwork
    "06_Fieldwork/Photos",
    "06_Fieldwork/GPS_Data",
    "06_Fieldwork/Notes",

    # Meeting / komunikasi
    "07_Meeting/BalaiArkeologi",
    "07_Meeting/UniversitasJambi",
    "07_Meeting/ResearchGate",

    # Dokumen
    "08_Docs",

    # Backup
    "09_Backup/LiDAR",
    "09_Backup/DEM",
    "09_Backup/Scripts"
]

# Buat semua folder
for folder in folders:
    path = os.path.join(base_dir, folder)
    os.makedirs(path, exist_ok=True)

# Buat README.txt dan Instructions.txt
readme_path = os.path.join(base_dir, "08_Docs", "README.txt")
instructions_path = os.path.join(base_dir, "08_Docs", "Instructions.txt")

with open(readme_path, "w") as f:
    f.write("Folder proyek Muaro Jambi untuk penelitian kanal kuno.\n"
            "Struktur sudah mencakup semua derivatif LiDAR dan analisis hidrologi, LRM, TPI, TRI, Curvature, kanal, reservoir, vegetasi, serta output peta, grafik, tabel, dan laporan.\n")

with open(instructions_path, "w") as f:
    f.write("Petunjuk penggunaan:\n"
            "- Simpan data LiDAR di 02_Data/LiDAR_Raw\n"
            "- Simpan DEM, LRM, dan derivatif lain sesuai folder masing-masing\n"
            "- Skrip Python/ArcPy di 03_Scripts\n"
            "- Hasil analisis di 05_Results\n"
            "- Backup data penting di 09_Backup\n")

# Skeleton skrip ArcPy
arcpy_script_path = os.path.join(base_dir, "03_Scripts/ArcPy/process_arcpy.py")
arcpy_script = """# Skeleton ArcPy Script: Kanal Kuno Muaro Jambi
import arcpy
from arcpy.sa import *

arcpy.env.overwriteOutput = True

# Load DEM
dem = arcpy.Raster("D:/MuaroJambi_Project/02_Data/DEM/DTM/DTM_1m.tif")

# Fungsi LRM sederhana
def create_lrm(dem, radius, out_name):
    smooth = FocalStatistics(dem, NbrCircle(radius, "MAP"), "MEAN")
    lrm = dem - smooth
    lrm.save(out_name)
    return lrm

# Contoh penggunaan
lrm10 = create_lrm(dem, 10, "D:/MuaroJambi_Project/02_Data/LRM/LRM_10m/LRM_10m.tif")
print("LRM 10m selesai dibuat")
"""
with open(arcpy_script_path, "w") as f:
    f.write(arcpy_script)

# Skeleton notebook
notebook_path = os.path.join(base_dir, "03_Scripts/Notebooks/analysis_notebook.ipynb")
notebook_content = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Analisis Kanal Muara Jambi\n",
    "Notebook skeleton untuk analisis LRM, TPI, TRI, Curvature, kanal, hidrologi, dan derivatif LiDAR"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import arcpy\n",
    "from arcpy.sa import *\n",
    "print('Notebook siap untuk analisis LRM, TPI, TRI, Curvature, kanal, dan hidrologi')"
   ]
  }
 ],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}

with open(notebook_path, "w") as f:
    json.dump(notebook_content, f)

print(f"Struktur folder final lengkap dengan skeleton skrip dan notebook berhasil dibuat di {base_dir}!")
