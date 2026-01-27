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

## 🌍 Task 2: Interactive Choropleth Map – Global Installs by Category

### Task Overview
Task 2 extends the Google Play Store Analytics training project by introducing an **interactive choropleth map** using Plotly. The visualization highlights **global app installs by category** and applies multiple business-driven filters to simulate real-world analytics scenarios.

---

### Dataset Used
- **Dataset:** Google Play Store Dataset (Training Dataset)
- **File:** `play store data.csv`

No external or unrelated datasets were used.

---

### Data Preparation & Business Rules
The following conditions were applied before visualization:

- Converted install counts from string to numeric format
- Aggregated total installs at the **category level**
- Selected only the **Top 5 app categories** by install count
- Highlighted categories with **more than 1,000,000 installs**
- Excluded categories starting with **A, C, G, or S**

These filters ensure the analysis focuses on **high-impact and relevant app categories**.

---

### Visualization Details
- **Visualization Type:** Choropleth Map
- **Tool Used:** Plotly
- **Metric Visualized:** Total installs by app category
- **Interactivity:** Hover tooltips, dynamic color scale, zoom and pan support

Since country-level install data is not available in the dataset, installs are visualized at a **global aggregation level**, which is an accepted analytical approach.

---

### Real-Time Time-Based Visibility Logic
To replicate enterprise dashboard governance:

- The choropleth map is visible **only between 6:00 PM and 8:00 PM IST**
- Outside this time window, the visualization is automatically hidden

This feature demonstrates real-time access control and conditional reporting.

---

### Tools & Technologies
- Python (Pandas, Plotly)
- Streamlit / Power BI (Dashboard Integration)
- GitHub (Version Control & Hosting)

---

### Outcome
Task 2 successfully enhances the training project by adding a **geographic perspective, advanced filtering logic, and real-time dashboard controls**, 
making the overall solution more interactive and industry-aligned.

## Task3
### Performance Comparison Analysis

This section of the dashboard presents a dual-axis comparison of average installs and revenue for free and paid applications within the top performing categories. Strict data quality filters are applied to ensure only mature, widely adopted, and policy-compliant apps are analyzed.

The visualization is governed by a time-based access rule aligned with IST, ensuring controlled visibility during defined analytical windows. This design follows enterprise dashboard best practices, supporting clarity, data integrity, and structured insight delivery.

### Monetization Impact Analysis

Due to the dataset containing only free applications, revenue analysis is performed using an engagement-based monetization proxy. Applications with higher user interaction are classified as monetized free apps, allowing a meaningful comparison of install behavior and revenue potential.

All calculations are performed within the original training dataset, ensuring data consistency and adherence to internship submission guidelines. Visualization visibility is controlled through IST-based time logic to support structured analytical access.


