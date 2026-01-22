# Google-Playstore-Analytics- Task1


## 🔹 Project Title
**Real-Time Google Play Store Analytics with Time-Based Dashboard Controls**

---

## 📌 Project Overview
This project is an enhancement of my training project **“Learn to Build Real-Time Google Play Store Data Analytics – Python”**.  
As part of the internship task, I implemented an **advanced analytical dashboard feature** that compares **average app ratings and total review counts** for the **top-performing app categories**, with **business-driven filters and real-time visibility logic**.

The goal of this task is to demonstrate:
- Data cleaning and transformation skills
- KPI-based analysis
- Interactive and conditional dashboards
- Real-time analytics concepts used in enterprise environments

---

## 📂 Dataset Used
✔ **Same dataset used during training (mandatory requirement)**  
- `googleplaystore.csv`

**Key Columns Utilized**
- `Category`
- `Rating`
- `Reviews`
- `Installs`
- `Size`
- `Last Updated`

⚠ No new or unrelated dataset was used, as per internship instructions.

---

## 🧹 Data Cleaning & Preparation
The dataset required multiple preprocessing steps to ensure accurate analysis:

### Transformations Applied
- Converted `Installs` from string format (e.g., `1,000,000+`) to numeric
- Converted `Reviews` and `Rating` to numeric values
- Cleaned `Size` column and converted all values to **MB**
- Removed invalid entries such as:
  - “Varies with device”
  - Missing ratings
- Converted `Last Updated` column to datetime format
- Extracted **Update Month** from the date

These steps ensured consistency, reliability, and professional-grade data quality.

---

## 🎯 Business Filters Applied
To meet the internship task requirements, the following filters were applied:

| Filter Condition | Purpose |
|-----------------|--------|
| Average Rating ≥ 4.0 | Focus on high-quality apps |
| App Size ≥ 10 MB | Exclude lightweight or incomplete apps |
| Last Updated = January | Analyze recently maintained apps |
| Top 10 Categories by Installs | Focus on most popular categories |

---

## 📊 KPIs & Metrics
The following KPIs were calculated:

- **Total Installs (per category)**
- **Average Rating (per category)**
- **Total Review Count (per category)**

These KPIs help assess **both popularity and user satisfaction**.

---

## 📈 Visualization Implemented
### Grouped Bar Chart
A **grouped bar chart** was used to compare:
- **Average Rating**
- **Total Review Count**

for the **Top 10 App Categories by Install Count**.

### Why Grouped Bar Chart?
- Enables **side-by-side comparison**
- Improves category-wise insight
- Ideal for comparing two related KPIs

---

## ⏰ Real-Time Time-Based Visibility Logic (Unique Feature)

### Business Rule
> The grouped bar chart should be visible **only between 3:00 PM and 5:00 PM IST**.

### Implementation Logic
- Current system time is converted to **Indian Standard Time (IST)**
- A conditional flag is generated:
  - If time ∈ 3 PM – 5 PM → Chart is visible
  - Otherwise → Chart is hidden

### Purpose
This simulates **real-world enterprise dashboards**, where reports are:
- Available during business hours
- Restricted outside defined time windows

This feature demonstrates **real-time analytics and access control concepts**.

---

## 🛠 Tools & Technologies Used
- **Python** (Pandas, Matplotlib)
- **Power BI / Streamlit** (Dashboard & Visualization)
- **GitHub** (Version control & project hosting)

---

## 📤 Project Hosting & Access
- **Dashboard Type:** Interactive & Filter-enabled
- **Hosting Platform:** Power BI Service / GitHub (Python-based)
- **Public Access:** Enabled for evaluation

📌 Screenshots of visuals and dashboard behavior are included in the repository.

---

## 📁 Repository Structure
