import streamlit as st
import os
import shutil
from main import ResumeMatcher
from pdf_loader import load_resumes_from_folder
from analytics import plot_results
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Smart ATS", page_icon="🧠", layout="wide")

st.title("🧠 Smart Resume Matcher")
st.markdown("### AI-Powered Applicant Tracking System")

# --- SIDEBAR: JOB DESCRIPTION ---
with st.sidebar:
    st.header("1. Job Description")
    job_description = st.text_area(
        "Paste the Job Description here:",
        height=300,
        placeholder="e.g. We are looking for a Python Engineer with AI experience..."
    )
    
    # Clean up button
    if st.button("Clear & Reset"):
        if os.path.exists("resumes"):
            shutil.rmtree("resumes")
        os.makedirs("resumes")
        st.rerun()

# --- MAIN AREA: FILE UPLOAD ---
st.header("2. Upload Resumes")
uploaded_files = st.file_uploader(
    "Upload PDF Resumes", 
    type=["pdf"], 
    accept_multiple_files=True
)

# --- LOGIC ---
if uploaded_files and job_description:
    # 1. Save uploaded files to 'resumes' folder
    save_folder = "resumes"
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
        
    for file in uploaded_files:
        with open(os.path.join(save_folder, file.name), "wb") as f:
            f.write(file.getbuffer())
    
    st.success(f"✅ Uploaded {len(uploaded_files)} resumes.")
    
    # 2. Run the Matcher
    if st.button("Analyze Candidates 🚀"):
        with st.spinner("Analyzing resumes..."):
            # Load resumes
            candidates = load_resumes_from_folder(save_folder)
            
            # Init Model
            matcher = ResumeMatcher()
            
            # Get Results
            results = matcher.match(job_description, candidates)
            
            # --- DISPLAY RESULTS ---
            st.divider()
            st.header("3. Analysis Results")
            
            # Create Columns
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.subheader("🏆 Rankings")
                # Convert to DataFrame for a nice table
                df = pd.DataFrame(results, columns=["Candidate Name", "Match Score"])
                st.dataframe(df.style.highlight_max(axis=0), use_container_width=True)
            
            with col2:
                st.subheader("📊 Visualization")
                # We need to adapt the plot slightly for Streamlit
                # (Streamlit handles charts differently than standard Matplotlib)
                st.bar_chart(df.set_index("Candidate Name"))

elif not job_description:
    st.info("👈 Please paste a Job Description in the sidebar to start.")