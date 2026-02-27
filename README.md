# 🏢 B2B Account Segmentation & Retention Analysis

**B2B SaaS data analyst → 10k account analysis. K-Means segmentation (k=4), Random Forest churn model (AUC 0.852), playbooks targeting Segment 3's 30.3% revenue churn.**

![Churn by Segment](visuals/churn_by_segment.png)

## 🎯 Problem Statement
**"Identify account segments, predict churn, prioritize CS efforts to improve GRR/NRR."**

**Metrics Delivered**: Logo Churn, Revenue Churn, GRR, NRR

## 📊 Dataset
[Churn_Modelling.csv](https://www.kaggle.com/datasets/shivan118/churn-modeling-dataset) (10k accounts)

**B2B Reframing**:
| Column | B2B Proxy |
|--------|-----------|
| Balance | **ACV** |
| Tenure | Relationship |
| NumOfProducts | **Modules** |
| Exited | **Churn** |

## 🛠️ 4-Notebook Workflow

### 01. EDA & Features
`notebooks/01_eda_account_overview.ipynb`

### 02. K-Means Segmentation
`notebooks/02_account_segmentation.ipynb`

**Elbow → k=4 clusters** (30%/21%/27%/22% accounts)

| Segment | **Label** | Avg ACV | Churn Rate | Accounts % |
|---------|-----------|---------|------------|------------|
| **0** | Strategic Enterprise | **121k** | **0.12** | **30.1%** |
| 1 | Small Trial/At-Risk | **95k** | 0.29 | **21.0%** |
| 2 | **Growth Accounts** | **105k** | 0.29 | **21.9%** |
| **3** | High-Spend Risky | **145k** | **0.30** | **27.0%** |

### 03. Retention Metrics
`notebooks/03_retention_by_segment.ipynb`

| Segment | **Logo Churn** | **Revenue Churn** | **GRR** | ACV Share |
|---------|----------------|-------------------|---------|-----------|
| **0** | **21.0%** | **15.7%** | **84.3%** | **21%** |
| 1 | 27.5% | 25.0% | 75.0% | 21% |
| 2 | **21.4%** | 21.0% | 79.0% | **27%** |
| **3** | **30.0%** | **30.3%** | **69.7%** | **31%** |

**NRR**: Growth Segment **84.3%** (expansion simulation).

### 04. Churn Model + Playbooks
`notebooks/04_churn_model_and_playbooks.ipynb`

**Random Forest**: **AUC 0.852** (60% churn recall)

**Top 5 Predictors**:
1.Age (0.2200) ⭐

2.NumOfProducts (0.1241)

3.EstimatedSalary (0.1121)

4.CreditScore (0.1189)

5.ACV (0.0970)

![Features](visuals/feature_importance.png)

## 🎯 Retention Playbooks

| Segment | **Priority** | **CS Action** | **Target** |
|---------|--------------|---------------|------------|
| **0 Enterprise** | Protect | QBRs + CSM | GRR **84→90%** |
| **1 Trial** | Rescue | Onboarding alerts | Churn **27→20%** |
| **2 Growth** | **Expand** | Module upsells | **NRR >100%** |
| **3 Risky** ⭐ | **Urgent** | Discounts + exec | Revenue **30→20%** |

## 💼 Business Impact
**"Target Segment 3 (31% ACV, 30% churn) → portfolio GRR ~75% → 85%+"**

**Resume Bullet**:
> `B2B segmentation + RF churn model (AUC 0.85); playbooks → GRR 75→85% (10k accounts)`

## 🚀 Quick Start
```bash
git clone https://github.com/YOUR_USERNAME/b2b-account-segmentation-retention
pip install pandas scikit-learn matplotlib seaborn jupyter
jupyter notebook notebooks/
