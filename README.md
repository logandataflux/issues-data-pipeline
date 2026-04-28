# Jira-Style Data Engineering Pipeline (GitHub Issues Analytics)

## Overview
This project is an end-to-end data engineering pipeline that extracts issue data from the GitHub API, transforms it into analytics-ready format, loads it into PostgreSQL, and visualizes insights using Power BI.

The goal is to simulate a **Jira-style ticket analytics system** to analyze operational performance, SLA compliance, and ticket resolution trends.

---

## Problem Statement
Organizations need visibility into:
- Ticket resolution performance
- SLA compliance
- Workload trends over time

However, raw API data is not analytics-ready and requires transformation before meaningful insights can be generated.

---

## Tech Stack
- Python
- SQL
- PostgreSQL
- GitHub REST API
- Power BI
- Pandas

---

## Architecture

GitHub API  
→ Python Extract Script  
→ Data Transformation Layer  
→ PostgreSQL Database  
→ SQL Analytics  
→ Power BI Dashboard  

---

## ETL Pipeline Steps

### 1. Extract
- Pulls issue data from GitHub API
- Uses pagination to retrieve multiple pages
- Filters out pull requests

### 2. Transform
- Converts timestamps into datetime format
- Engineers resolution time (hours)
- Creates SLA classification:
  - On Time
  - At Risk
  - Breached

### 3. Load
- Loads cleaned data into PostgreSQL
- Ensures schema consistency
- Handles duplicate records using primary key constraints

---

## Data Model

Table: `github_issues`

| Column | Type | Description |
|--------|------|-------------|
| id | BIGINT | Unique issue ID |
| title | TEXT | Issue title |
| state | TEXT | Open / Closed |
| created_at | TIMESTAMP | Issue creation time |
| updated_at | TIMESTAMP | Last update time |
| resolution_time_hours | FLOAT | Time to resolve issue |
| sla_status | TEXT | SLA classification |

---

## Key Insights

- Ticket volume analysis across issue states
- Average resolution time per issue
- SLA compliance breakdown (On Time / At Risk / Breached)
- Time-based trend analysis of issue creation

---

## Power BI Dashboard

The dataset is visualized using Power BI to provide:

- KPI Cards:
  - Total Tickets
  - SLA Breach Rate
  - Average Resolution Time

- Visuals:
  - Ticket trends over time
  - SLA status distribution
  - Issue state breakdown

---

## Business Value

This project demonstrates how raw engineering data can be transformed into actionable insights for:

- Improving team productivity
- Identifying SLA bottlenecks
- Tracking operational performance
- Supporting data-driven decision making

---

## How to Run This Project

### 1. Clone repository
```bash
git clone https://github.com/logandataflux/issues-data-pipeline.git
cd issues-data-pipeline
