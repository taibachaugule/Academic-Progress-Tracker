import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎓 Academic Progress Tracker")

st.write("Enter your subject details:")

# Number of subjects
n = st.number_input("Enter number of subjects", min_value=1, step=1)

subjects = []
marks = []
max_marks = []

# Dynamic input
for i in range(int(n)):
    st.subheader(f"Subject {i+1}")
    subject = st.text_input(f"Subject Name {i+1}", key=f"s{i}")
    mark = st.number_input(f"Marks {i+1}", min_value=0, key=f"m{i}")
    max_mark = st.number_input(f"Max Marks {i+1}", min_value=1, key=f"mm{i}")
    
    subjects.append(subject)
    marks.append(mark)
    max_marks.append(max_mark)

# Button
if st.button("Analyze Performance"):
    
    df = pd.DataFrame({
        "Subject": subjects,
        "Marks": marks,
        "Max_Marks": max_marks
    })
    
    # Calculate percentage
    df["Percentage"] = (df["Marks"] / df["Max_Marks"]) * 100
    
    # Grade function
    def grade(p):
        if p >= 85:
            return "A"
        elif p >= 70:
            return "B"
        elif p >= 50:
            return "C"
        else:
            return "D"
    
    df["Grade"] = df["Percentage"].apply(grade)
    
    # Show table
    st.subheader("Results")
    st.dataframe(df)
    
    # Average
    avg = df["Percentage"].mean()
    st.metric("Average Percentage", f"{avg:.2f}%")
    
    # Top & Weak subject
    top = df.loc[df["Marks"].idxmax()]
    weak = df.loc[df["Marks"].idxmin()]
    
    st.success(f"Top Subject: {top['Subject']}")
    st.error(f"Weak Subject: {weak['Subject']}")
    
    # Chart
    st.subheader("Performance Chart")
    fig, ax = plt.subplots()
    ax.bar(df["Subject"], df["Marks"])
    plt.xticks(rotation=30)
    st.pyplot(fig)