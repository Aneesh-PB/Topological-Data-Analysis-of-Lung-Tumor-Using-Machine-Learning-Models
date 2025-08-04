# 🧠 Lung Tumor Classification using Topological Data Analysis

This project applies **Topological Data Analysis (TDA)** — particularly **persistent homology** — to classify lung CT scan images as **normal**, **benign**, or **malignant**. We extract entropy-based features from both images and point clouds, and compare their classification performance using various machine learning and deep learning models. The top-performing approach achieved **97.67% accuracy** using entropy values from point clouds with a KNN classifier.

---

## 📁 Project Structure

### 🔸 Input / Output Data

- `Images/` — Original lung CT scan images.  
- `Point Cloud/` — Sample point clouds (CSV) generated from 50 CT images.  
  - 🔗 **[Full Point Cloud Output (Google Drive)](https://drive.google.com/drive/folders/1ErLNUTKSsGUZ3lCcm0lBb-FAz8pHRwTa?usp=drive_link)**  
- `Persistence/` — Persistence diagrams computed from the point clouds.  

### 🔸 Core Notebooks and Scripts

| File | Description |
|------|-------------|
| `Point cloud generation.ipynb` | Generates point cloud representations from CT scan images. |
| `Persistence diagram generation code/` | Scripts to generate persistence diagrams from point clouds. |
| `Classification Using Entropy Values from Images.ipynb` | Classifies images based on entropy computed from raw pixel intensities. |
| `Classification using Entropy Values Generated from point cloud code/` | Subfolders (`500`, `800`, `1000`, etc.) for different point cloud sizes. Each contains:<br>- Scripts to compute entropy features (`Entropy/` subfolder)<br>- Notebook for classification using these features |
| `point cloud entropy plot.ipynb` | Visualizes entropy patterns per class across image intensities. |
| `Average points per layer.ipynb` | Analyzes average point count across layers in 3D point clouds. |
| `Classification using Image features.ipynb` | Classifies CT images using extracted pixel-based features. |
| `CNN.ipynb` | CNN model to classify CT images directly from pixel data. |
| `ML Using entropy final.ipynb` | Summarizes ML models trained on entropy features from both images and point clouds. |

---

### 📊 Comparison of Model Performance

This plot compares accuracy and F1-scores across all methods used.

![Performance Comparison](Output%20Images/Performance_metrics_all_models_(with%20heading).png)

---

## ✅ Key Findings

- **Entropy from Point Clouds + KNN**: ✅ **97.67% accuracy**
- **Entropy from Images + KNN**: ✅ **95.91% accuracy**
- Outperformed deep learning (CNN) and basic image feature-based models in multiple cases
- Entropy-based features are highly discriminative for lung tumor classification

---

## 🛠 Installation

Install dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 📜 License

This project is licensed under the [MIT License](LICENSE).  

---

## 🙏 Acknowledgements

We would like to extend our gratitude to the open-source community and the developers of the following tools and libraries that made this project possible:

- **Ripser**, **Persim**, and **Tadasets** for enabling Topological Data Analysis in Python.
- **Scikit-learn**, **XGBoost**, and **TensorFlow** for their powerful machine learning frameworks.
- **Pillow**, **Scipy**, and **Matplotlib** for essential image processing and visualization tools.

This project represents a fusion of concepts from **topology**, **image processing**, and **machine learning**, applied toward advancing research in **medical diagnostics**.

