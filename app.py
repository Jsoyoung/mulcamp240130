# -*- coding:utf-8 -*-

import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

@st.cache_data

def load_data2():
    prior = pd.read_csv("sample_prior.csv")
    return prior

def load_data3():
    products = pd.read_csv("sample_products.csv")
    return products

def main():
    st.title(":cake:Instacart:doughnut:")
    prior = load_data2()
    products = load_data3()

    st.header('Order Count by Product')
    product_id = pd.merge(prior, products, on='product_id', how='inner')
    grouped_name = product_id.groupby('product_name')['order_id'].nunique().reset_index()
    st.dataframe(grouped_name.sort_values(by='order_id', ascending=False), use_container_width=True, hide_index=True)

    grouped20 = grouped_name.sort_values(by='order_id', ascending=False).head(20)


    show_plot = st.checkbox("상위 20개 차트로 보기")
    st.write(show_plot)

    fig, ax = plt.subplots(figsize=(35,20))
    sns.barplot(x='order_id', y='product_name', data=grouped20,ax=ax, palette="viridis")
    sns.set(font_scale=4)
    plt.xlabel("Order Count")
    plt.ylabel("Product")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    if show_plot:
        st.pyplot(fig)
    else:
        st.write("닫힘")
    

if __name__ == "__main__":
    main()