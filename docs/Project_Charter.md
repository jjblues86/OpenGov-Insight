# 🏛️ Project Charter: OpenGov Insight

## 1. Project Overview
**Project Name:** OpenGov Insight  
**Project Type:** Business Intelligence & Transparency Dashboard  
**Duration:** 4 months (16 weeks)  
**Project Owner:** Jerome Joof  

### Problem Statement
Citizens and journalists often lack clear, accessible information about how public funds are spent. Budget and expenditure data, while technically public, are usually fragmented or difficult to interpret. This limits transparency and reduces public trust in institutions.

**OpenGov Insight** addresses this challenge by creating an AI-powered, interactive dashboard that visualizes government spending data, highlights anomalies, and provides automated insights for accountability and better decision-making.

---

## 2. Vision & Mission
**Vision:**  
To make public spending transparent and understandable to every citizen.

**Mission:**  
Build an open, data-driven BI platform that leverages AI to uncover patterns, inefficiencies, and opportunities for improvement in government financial management.

---

## 3. Objectives
1. Design and implement a scalable ETL pipeline to collect and clean public financial data.  
2. Build a dynamic dashboard that visualizes key KPIs (budget vs. actual spend, variance, department efficiency).  
3. Integrate AI-driven anomaly detection and automated summaries to highlight potential inefficiencies.  
4. Deploy the dashboard publicly for demonstration and community feedback.  
5. Document the entire lifecycle for use as a portfolio case study and TPM discussion project.

---

## 4. Project Scope

### In Scope
- Data ingestion from open government datasets or simulated data.  
- ETL processes for cleaning and transforming data.  
- BI dashboard development (Power BI, Tableau, or Streamlit).  
- Machine learning layer for anomaly detection.  
- Automated reporting using GPT-based natural-language summaries.  
- Hosting and sharing dashboard demo.  

### Out of Scope
- Private or restricted government data access.  
- Legal auditing or official government validation.  
- Mobile application development (future phase).

---

## 5. Stakeholders & Users

| Stakeholder | Role | Interest / Benefit |
|--------------|------|--------------------|
| Citizens | End Users | Gain visibility into public spending. |
| Journalists | Investigators | Identify trends and anomalies for stories. |
| Policymakers | Decision Makers | Discover inefficiencies and improve budget allocations. |
| Jerome Joof | Creator / TPM | Build BI + AI product experience for portfolio. |

---

## 6. Deliverables
1. Clean, structured dataset stored in PostgreSQL or equivalent.  
2. Interactive BI dashboard with visual KPIs.  
3. AI insight engine generating text summaries.  
4. Public demo deployment (Streamlit / Power BI Service).  
5. Project documentation, architecture diagram, and demo video.

---

## 7. Success Metrics (SMART Goals)

| Metric | Target | Measurement Method |
|---------|---------|--------------------|
| Data completeness | ≥90% valid and clean records | Validation script |
| Dashboard usability | ≥80% positive feedback from test users | Usability survey |
| Dashboard load time | <3 seconds | Performance test |
| Anomaly detection accuracy | ≥90% correctly identified anomalies | Manual validation |
| Project completion | 100% planned features delivered by Week 16 | Final project review |

---

## 8. Risks & Mitigation

| Risk | Impact | Mitigation Strategy |
|------|---------|--------------------|
| Limited or inconsistent data availability | High | Use simulated or alternative open data sources. |
| Time constraints | Medium | Break work into weekly sprints and track progress. |
| Technical complexity (AI, ETL integration) | Medium | Start simple, iterate gradually; prioritize BI MVP first. |
| Deployment issues | Low | Use reliable hosting (Streamlit Cloud / Power BI). |

---

## 9. Assumptions
- Public or open datasets are available or can be simulated.  
- You have 10–15 hours per week to dedicate to the project.  
- The tech stack (Python, Power BI/Streamlit, PostgreSQL) is accessible.  

---

## 10. Tools & Technology Stack
- **Programming:** Python, Pandas, NumPy  
- **Data Storage:** PostgreSQL or CSV files  
- **Visualization:** Power BI / Tableau / Streamlit + Plotly  
- **AI Layer:** Scikit-learn, OpenAI GPT API  
- **Version Control:** Git + GitHub  
- **Project Management:** Notion / Trello  
- **Deployment:** Streamlit Cloud or Power BI Service  

---

## 11. Timeline Overview

| Phase | Duration | Key Milestones |
|--------|-----------|----------------|
| Discovery & Planning | Weeks 1–2 | Charter, architecture, environment |
| Data Engineering | Weeks 3–6 | ETL, schema, KPIs |
| Dashboard Development | Weeks 7–10 | BI visuals and interactivity |
| AI & Insights | Weeks 11–13 | Anomaly detection and summaries |
| Deployment & Showcase | Weeks 14–16 | Launch + documentation |

---

## 12. Approval & Sign-off
**Prepared by:**  
Jerome Joof – Project Lead  

**Date:**  
October 2025  

---

> *This document serves as the foundation for project alignment, milestone tracking, and portfolio documentation.*
