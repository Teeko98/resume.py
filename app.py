from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# -- General Settings ---
PAGE_TITLE = "Digital Resume | Alberto Sosa"
PAGE_ICON = ":wave:"
NAME = "Alberto Sosa"
DESCRIPTION = """
Recent Computer Science Graduate looking to start my career in Software Engineering    
"""
EMAIL = "sosa.alberto98@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/teeko/"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/teeko/",
    "GitHub": "https://github.com/Teeko98"
}
PROJECTS = {
    "🗓 Appointment Scheduling Application (Java, JavaFX, JDBC, PostgreSQL)": "https://github.com/Teeko98/C195-Software-II",
    "🧾 Inventory Management System (Java, JavaFX)": "https://github.com/Teeko98/C482-Software-I",
    "🤖 Disaster Recovery Bot (AIML, CoppeliaSim, C++)": "https://github.com/Teeko98/C951-Disaster-Rescue-Bot",
    "📦 Package Delivery Simulation (Python)": "https://github.com/Teeko98/C950-Delivery-Simulation",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF, AND PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=250)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫️", EMAIL)
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        st.write(f"[{platform}]({link})")


# --- Experience and Qualifications ---
st.write("#")
st.subheader("Experience and Qualifications")
st.write("""
    - 🎓 Bachelor of Science in Computer Science.
    - 💪🏽 8 Years of working experience in both team and leadership roles.
    - 💻 Strong understanding of Object Oriented Programming and various project methodologies.
"""
)


# --- SKILLS ---
st.write("#")
st.subheader("Skills")
st.write("""
    - 👨🏽‍💻 Technologies: Java, Python, C++, C#, HTML5, CSS, JavaScript, Bash, PHP, AIML.
    - 💾 Data Storage and OS: MySQL, PostgreSQL, Windows, Mac OS, Linux.
    - 📚 Certifications: ITIL 4, CompTIA Project+, CIW Site Development Associate, MTA Software Fundamentals.
    - 💡 Soft-skills: Bilingual (Native English and Spanish), Creativity, Communication, Teamwork, Problem-Solving.
    """
)


# --- PROJECTS and ACCOMPLISHMENTS ---
st.write("#")
st.subheader("Projects and Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1 ---
st.write("🍻", "**Bartender | Three Sheets Craft Beer**")
st.write("02/2022 - 11/2022")
st.write("""
    - Poured and Served Craft Beer in the heart of Las Vegas’s Art District.
    - Assisted in planning and operating events in the Three Sheets beer garden. 
    - Maintained up to date knowledge of our ever changing menu to inform patrons of our current offerings.
"""
)

# --- JOB 2 ---
st.write("#")
st.write("☕️", "**Barista | Vesta Coffee Roasters**")
st.write("04/2021 - 04/2022")
st.write("""
    - Prepared and served 3rd wave coffee at a very high volume in downtown Las Vegas.
    - Practiced and perfected latte art techniques including: swan, phoenix, rosetta, tulip, and heart.
"""
)

# --- JOB 3 ---
st.write("#")
st.write("☕️", "**Barista | Mothership Coffee Roasters**")
st.write("03/2020 - 04/2021")
st.write("""
    - Prepared and served 3rd wave coffee at a high volume in downtown Las Vegas.
    - Assisted in operating events at Ferguson’s Downtown Las Vegas.
"""
)


# --- JOB 4 ---
st.write("#")
st.write("☕️", "**Barista | For Five Coffee Roasters**")
st.write("11/2019 - 03/2020")
st.write("""
    - Prepared specialty coffee in a very high paced environment; serving an average of 1200 customers daily in downtown Manhattan.
    - Practiced and perfected latte art techniques.
"""
)