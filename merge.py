import streamlit as st 
import pandas as pd

st.title('Merge Files')

uploaded_file = st.file_uploader("Choose a file (GMV & Gross) ")
if uploaded_file is not None:
    
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)
    # df = st.write(dataframe)
    st.dataframe(df)
    st.write("Number count of row " ,len(df))
    
st.write("Choose more file to merge columns with the first file")
second_file = st.file_uploader("Choose a second file (allocation table)", key="second_file")
if second_file is not None:
    
    # Can be used wherever a "file-like" object is accepted:
    df2 = pd.read_csv(second_file)
    # df = st.write(dataframe)
    st.dataframe(df2)
    st.write("Number count of row " ,len(df2))
    
    merge = df.merge(df2, on=['Date','City','Service'],how = 'left')
    merge_1 = st.dataframe(merge)
    merge_1

third_file = st.file_uploader("Choose a third file (booking with assistance)", key="third_file")
if third_file is not None:
    
    # Can be used wherever a "file-like" object is accepted:
    df3 = pd.read_csv(third_file)
    # df = st.write(dataframe)
    st.dataframe(df3)
    st.write("Number count of row " ,len(df2))
    
    merge = merge_1.merge(df3, on=['Date','City','Service'],how = 'left')
    merge_2 = st.dataframe(merge)
    merge_2
    
forth_file = st.file_uploader("Choose a file (tran_user)", key="forth_file")
if third_file is not None:
    
    # Can be used wherever a "file-like" object is accepted:
    df3 = pd.read_csv(third_file)
    # df = st.write(dataframe)
    st.dataframe(df3)
    st.write("Number count of row " ,len(df3))
    
    merge = merge_2.merge(df2, on=['Date','City','Service'],how = 'left')
    merge_3 = st.dataframe(merge)
    merge_3
    
fifth_file = st.file_uploader("Choose a file (new_user)", key="fifth_file")
if fifth_file is not None:
    
    # Can be used wherever a "file-like" object is accepted:
    df4 = pd.read_csv(third_file)
    # df = st.write(dataframe)
    st.dataframe(df4)
    st.write("Number count of row " ,len(df2))
    
    merge_4 = merge_3.merge(df4, on=['Date','City','Service'],how = 'left')
    merge_4 = st.dataframe(merge)
    merge_4
# if st.button("Download"):
#     merge_df.to_csv('merge.csv', index=False)  
    
        
        # # Create input fields for new column names
        # new_names = {}
        # for col in df.columns:
        #     new_name = st.text_input(f"New name for '{col}':", value=col)
        #     new_names[col] = new_name
        
        # # Rename columns if user clicks the button
        # if st.button("Apply new column names"):
        #     for col in df.columns:
        #         df.rename(columns=new_names, inplace=True)
        #         st.write("Updated DataFrame:")
        #         st.write(df)