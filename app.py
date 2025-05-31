
import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Başlık
st.title("📚 Kitap Tavsiye Sistemi (LightFM)")

# Model ve veri kümesini yükle
@st.cache_resource
def load_model():
    with open("lightfm_book_model.pkl", "rb") as f:
        bundle = pickle.load(f)
    return bundle["model"], bundle["dataset"]

@st.cache_data
def load_books():
    return pd.read_csv("books.csv")

model, dataset = load_model()
books = load_books()

# Kullanıcıdan ID al
user_id = st.number_input("Kullanıcı ID girin:", min_value=0, step=1)

# Öneri üret
if st.button("📖 Kitapları Öner"):
    try:
        n_users, n_items = dataset.interactions_shape()
        scores = model.predict(user_ids=user_id, item_ids=np.arange(n_items))
        top_items = np.argsort(-scores)[:5]

        st.subheader("✅ Önerilen Kitaplar:")
        recommended_books = books[books['book_id'].isin(dataset.mapping()[2].keys())]
        reverse_item_map = {v: k for k, v in dataset.mapping()[2].items()}

        for i in top_items:
            book_id = reverse_item_map.get(i)
            book_info = books[books['book_id'] == book_id]
            if not book_info.empty:
                title = book_info['original_title'].values[0]
                author = book_info['authors'].values[0]
                st.markdown(f"**📘 {title}** by *{author}*")
    except Exception as e:
        st.error(f"Hata oluştu: {e}")
