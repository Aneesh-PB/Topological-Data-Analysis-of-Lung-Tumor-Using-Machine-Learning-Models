# Lung Tumor Classification using Topological Data Analysis

This project explores the use of **Topological Data Analysis (TDA)**, specifically **persistent homology**, for classifying lung CT scan images into *normal*, *benign*, and *malignant* categories. By generating persistence diagrams from both images and point clouds, and computing entropy-based features, we compare the performance of traditional ML models and CNNs. The best-performing setup — using entropy from point clouds — achieved **97.6% accuracy** with KNN.

---

## 📁 Repository Structure

### 🔹 Input & Output

- **Images/**  
  Contains input CT scan images used for analysis.

- **Point Cloud/**  
  Contains Excel/CSV files representing point clouds generated from input images.

- **Persistence/**  
  Output images of persistence diagrams computed from the point clouds.

---

### 🔹 Notebooks and Scripts

- **Point cloud generation.ipynb**  
  Generates point cloud files from the input CT scan images.

- **Persistence diagram generation.ipynb/**  
  Code to generate persistence diagrams from the point clouds.

- **Classification using entropy values from images.ipynb**  
  Classifies images based on entropy values computed directly from images.

- **Classification using Entropy Values Generated from point cloud code/**  
  Contains subfolders (`500`, `800`, `1000`, `2000`, `3000`) for different subsample sizes.  
  Each contains:
  - `.py` scripts to compute entropy values (saved in a subfolder named `Entropy`)
  - A `.ipynb` notebook to classify based on the computed entropy

- **Point cloud entropy plot.ipynb**  
  Plots entropy values across different intensity levels for each class using point cloud-based entropy features.

- **Average points per layer code.ipynb**  
  Plots the average number of points across different layers of point clouds.

- **Classification using Image features.ipynb**  
  Classifies images using features directly extracted from the images.

- **CNN new.ipynb**  
  Implements a CNN for direct classification of CT scan images.

---

## 🧪 Key Results

- **97.6% Accuracy** using KNN on entropy features from point cloud data.
- Compared performance with CNN and image-based entropy models.
- Subsampling analysis showed robust accuracy across varying point sizes.

---

## 🛠 Dependencies

- Python 3.8+
- NumPy, Pandas, scikit-learn, xgboost, scipy, skimage, optuna, shapely
- matplotlib, seaborn, plotly
- ripser, cripser, tcripser, persim (for persistent homology)
- TensorFlow/Keras (for CNN)
- Any additional dependencies are listed in each notebook.

---

## 📄 License

This project is for academic/research purposes.
---

## 🙌 Acknowledgements

Inspired by the intersection of topological data analysis and medical imaging, this project demonstrates how abstract mathematical structures can improve classification performance in healthcare datasets.
