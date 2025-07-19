import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from collections import Counter

# --------------- PAGE CONFIG ---------------
st.set_page_config(page_title="E-Commerce Recommendation System", layout="wide")

# --------------- TITLE & INTRO ---------------
st.title("🛒 E-Commerce Recommendation-System")
st.markdown("### Role 4: Presenting Our Work in a Webpage")

st.header("📘 Introduction")
st.markdown("""
In today's digital era, e-commerce platforms are becoming increasingly popular, offering a vast array of products to consumers worldwide. However, with the abundance of choices, it can be overwhelming for users to find products that match their preferences.

To address this challenge, implementing a recommendation system can significantly enhance the user experience by providing personalized product suggestions.

This app explores the process of building an e-commerce recommendation system using machine learning techniques including:
- ✅ Content-based filtering  
- ✅ Collaborative filtering  
- ✅ Hybrid models  
- ✅ Multi-model recommendation strategies  
""")

# --------------- ABOUT US ---------------
st.header("👥 About Us")
st.markdown("""
We are a team of passionate developers and data science interns from India.  
This project is part of our internship to demonstrate real-world machine learning skills.
""")

# --------------- PROJECT OVERVIEW ---------------
st.header("🛠️ Project Overview")
st.markdown("""
- **Project Title**: E-Commerce Product Recommendation System  
- **Team Members**: Krishna Vamsi & Team  
- **Goal**: Build a machine learning system that can predict and recommend product ratings based on input features like review count, brand, and category.  
- **Tech Stack**: Python, Pandas, Scikit-learn, XGBoost, Streamlit  
- **Dataset**: Cleaned e-commerce product data

**Roles Taken:**
1️⃣ Data Cleaning  
2️⃣ Data Visualization  
3️⃣ Model Building  
4️⃣ Web App Creation (this interface)
""")

# --------------- DATA UPLOAD ---------------
st.header("📂 View Cleaned Dataset")
file = st.file_uploader("Upload your cleaned CSV file", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    st.subheader("📊 Visual Analysis")

    # Rating Distribution
    fig1, ax1 = plt.subplots()
    sns.histplot(df['Rating'], bins=20, kde=True, ax=ax1)
    ax1.set_title("Rating Distribution")
    st.pyplot(fig1)

    # Review Count Distribution
    fig2, ax2 = plt.subplots()
    sns.histplot(df['ReviewCount'], bins=20, kde=True, ax=ax2)
    ax2.set_title("Review Count Distribution")
    st.pyplot(fig2)

    # Scatterplot: Review Count vs Rating
    fig3, ax3 = plt.subplots()
    sns.scatterplot(data=df, x='ReviewCount', y='Rating', ax=ax3)
    ax3.set_title("Review Count vs Rating")
    st.pyplot(fig3)

    # Boxplot of Rating by Brand (Top 10)
    top_brands = df['Brand'].value_counts().head(10).index
    fig4, ax4 = plt.subplots()
    sns.boxplot(data=df[df['Brand'].isin(top_brands)], x='Brand', y='Rating', ax=ax4)
    ax4.set_title("Rating by Top 10 Brands")
    st.pyplot(fig4)

    # Histogram for all numeric columns
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    for col in numeric_cols:
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax, bins=30)
        ax.set_title(f"Histogram of {col}")
        st.pyplot(fig)

    # Boxplots for numeric columns
    for col in numeric_cols:
        fig, ax = plt.subplots()
        sns.boxplot(y=df[col], ax=ax)
        ax.set_title(f"Boxplot of {col}")
        st.pyplot(fig)

    # Correlation Heatmap
    fig_corr, ax_corr = plt.subplots(figsize=(12, 8))
    sns.heatmap(df[numeric_cols].corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax_corr)
    ax_corr.set_title("Correlation Heatmap")
    st.pyplot(fig_corr)

    # Pairplot sample
    st.subheader("🔁 Pairplot of Sample Numeric Columns")
    st.pyplot(sns.pairplot(df[numeric_cols[:3]]).fig)

    # Barplot for most common categories (if Cleaned_Categories exists)
    if 'Cleaned_Categories' in df.columns:
        try:
            cat_lists = df['Cleaned_Categories'].dropna().apply(eval)
            all_cats = [item for sublist in cat_lists for item in sublist]
            common = Counter(all_cats).most_common(20)
            cat_df = pd.DataFrame(common, columns=["Category", "Count"])
            fig_cat, ax_cat = plt.subplots()
            sns.barplot(data=cat_df, x="Count", y="Category", ax=ax_cat)
            ax_cat.set_title("Top 20 Categories by Count")
            st.pyplot(fig_cat)
        except:
            st.warning("⚠️ Could not parse 'Cleaned_Categories' column. Skipping category barplot.")

# --------------- PREDICTION SECTION ---------------
st.header("🔮 Predict Product Rating")

review_count = st.number_input("Review Count", min_value=0, value=5)
brand_encoded = st.number_input("Brand Encoded", min_value=0, value=100)
categories = st.text_input("Enter Categories (comma-separated)", "beauty,face")

if st.button("Predict"):
    try:
        model = joblib.load("xgb_model.joblib")
        cat_list = [c.strip().lower() for c in categories.split(',')]
        input_dict = {'ReviewCount': review_count, 'Brand_encoded': brand_encoded}
        for cat in cat_list:
            input_dict[cat] = 1
        input_df = pd.DataFrame([input_dict])
        prediction = model.predict(input_df)[0]
        st.success(f"⭐ Predicted Rating: {round(prediction, 2)}")
    except Exception as e:
        st.error("⚠️ Could not predict. Ensure model file exists and inputs are valid.")

# --------------- CONCLUSION ---------------
st.header("✅ Conclusion")
st.markdown("""
Building an e-commerce recommendation system with machine learning offers benefits like:
- 🎯 Personalized shopping experiences  
- 📈 Higher customer satisfaction  
- 💰 Boost in sales and user engagement  

We used:
- Content-Based Filtering  
- Collaborative Filtering  
- Hybrid Approaches  
- Multi-Model ML integration  

Integrated using **Streamlit** for rapid deployment. Can be scaled with Flask, Django or hosted online!
""")

# --------------- FOOTER ---------------
st.markdown("---")
st.subheader("📌 Summary")
st.markdown("""
- ✅ Role 1: Data Cleaning & Preparation  
- ✅ Role 2: Power BI Visualization  
- ✅ Role 3: Model Building with RandomForest & XGBoost  
- ✅ Role 4: Web Presentation & Final App  
""")
st.markdown("Made with ❤️ by **Krishna Vamsi & Team**")
