# 🏢 B2B Account Segmentation & Retention Analysis

**Data analyst at B2B SaaS company analyzing 10k accounts to optimize retention and Customer Success efforts.** Built K-Means segmentation, Random Forest churn model (**AUC 0.852**), and segment-specific playbooks improving simulated **NRR from 96% → 103%**.

![Churn by Segment](visuals/churn_by_segment.png)

## 🎯 Business Problem
Leadership needs to understand:
- Which **account segments** exist (size, engagement, spend)?
- Which segments have **high/low retention** and expansion potential?
- **What factors predict churn** at account level?
- **Playbooks/actions** per segment?

**Key Metrics**: Logo Churn, GRR (Gross Retention), NRR (Net Revenue Retention)

## 📊 Dataset
- **Churn_Modelling.csv** (Kaggle, 10k accounts): [Link](https://www.kaggle.com/datasets/shivan118/churn-modeling-dataset)
- **Reframed as B2B accounts**:
  | Original | B2B Interpretation |
  |----------|-------------------|
  | Balance | ACV proxy |
  | Tenure | Relationship length |
  | NumOfProducts | Modules used |
  | Exited | Account churned |

## 🛠️ Methodology (4 Notebooks)

1. **[01_eda_account_overview.ipynb](notebooks/01_eda_account_overview.ipynb)**  
   Data cleaning + B2B features (ACV bands, tenure years).

2. **[02_account_segmentation.ipynb](notebooks/02_account_segmentation.ipynb)**  
   **K-Means (k=4)** on ACV, Tenure, Products, Activity → **4 B2B segments**.

   ![Segments Profile](visuals/segments_profile.png)

3. **[03_retention_by_segment.ipynb](notebooks/03_retention_by_segment.ipynb)**  
   **Logo Churn, Revenue Churn, GRR, NRR** per segment.

4. **[04_churn_model_and_playbooks.ipynb](notebooks/04_churn_model_and_playbooks.ipynb)**  
   **Random Forest (AUC 0.852)** → feature importance + playbooks.

   ![Feature Importance](visuals/feature_importance.png)

## 🔍 Key Findings

- **Segment 1** (Small/At-Risk): **35% logo churn**, low ACV → onboarding priority.
- **Segment 2** (Growth): **NRR 110%** → upsell focus.
- **Top churn drivers**: **Tenure, Age, NumOfProducts** (model insights).
- **Playbooks lift portfolio NRR 96% → 103%**.

| Segment | Logo Churn | Revenue Churn | GRR | **Action** |
|---------|------------|---------------|-----|------------|
| 0: Enterprise | Low | Low | **90%** | QBRs + CSM |
| 1: At-Risk | **35%** | High | 75% | Onboarding |
| 2: Growth | Medium | Low | **110% NRR** | Upsells |
| 3: Risky | Medium | **20%** | 85% | Discounts |

## 💼 Business Impact
- **Resume bullet**: "B2B account segmentation + churn model (AUC 0.85); playbooks → simulated NRR 96→103%"
- **CS teams gain**: Prioritized segments, risk scores, actionable playbooks.

## 🚀 Setup & Run
```bash
# Clone repo
git clone <your-repo-url>

# Install dependencies
pip install -r requirements.txt  # Or use b2b-env/

# Run notebooks sequentially
jupyter notebook notebooks/
