# 📚 Book Recommendation System using LightFM

This project builds a hybrid book recommendation system using the LightFM library.  
It leverages collaborative and content-based filtering to suggest books to users based on ratings data.

## 📦 Dataset
- Source: [Goodbooks-10K Dataset](https://www.kaggle.com/datasets/zygmunt/goodbooks-10k)
- Files used: `books.csv`, `ratings.csv`

## 🔧 Libraries
- `pandas`, `numpy`, `matplotlib`
- `lightfm`

## 🔮 Recommendation Logic
- Trained a LightFM model using WARP loss function.
- Built a user-item interaction matrix.
- Predicted books that the user hasn't rated yet.
- Displayed top-N recommendations per user.

## 📊 Visualization
- Bar chart of top 10 most-rated books.

## 🚀 How to Run
```bash
pip install -r requirements.txt
jupyter notebook Book_Recommendation_LightFM.ipynb

✍️ Author
Hande Çarkcı

