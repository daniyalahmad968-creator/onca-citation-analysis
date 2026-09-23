# Ontario Court of Appeal: Citation Influence by Case Type (2015–2024)

**A data analytics project applying statistical methods to Canadian legal data**

---

## Question

Which types of Ontario Court of Appeal (ONCA) cases are most influential — measured by how often they are cited by later courts — and has that influence changed over the past decade?

## Method

**Data source:** [A2AJ (Access to Algorithmic Justice)](https://a2aj.ca), an open-source, bulk-access alternative to CanLII built for empirical legal research. The dataset (`a2aj/canadian-case-law`, `data_dir="ONCA"`) contains 24,106 total Ontario Court of Appeal decisions, each with a citation count reflecting how many later cases have cited it.

**Sampling:** Filtered to cases decided 2015–2024 (9,332 cases), then drew a random sample of 200 cases (fixed random seed for reproducibility) to keep the dataset analyzable while preserving representation across all ten years.

**Case-type classification:** The dataset has no built-in case-type label, so each case was classified into one of six categories (Criminal, Family, Employment, Contract, Tort, Estate/Trusts) or "Other" using keyword matching against the case name and judgment text (e.g., "R. v." → Criminal, "custody" → Family). This is a practical, defensible method for a project of this scope, but it is not a perfect substitute for manual legal classification — some edge cases may be mislabeled.

**Tools:**
- **SQLite / SQL** — imported the classified dataset into a relational database and ran exploratory queries (average citations by case type, by year)
- **Python (pandas, scipy)** — computed summary statistics and ran a one-way ANOVA test to check whether differences in citation counts across case types were statistically significant
- **Power BI** — built an interactive dashboard visualizing the findings

## Findings

| Case Type | Avg. Citations | n |
|---|---|---|
| Employment | 3.79 | 29 |
| Criminal | 3.12 | 113 |
| Family | 2.58 | 12 |
| Tort | 1.67 | 6 |
| Contract | 0.76 | 21 |
| Estate/Trusts | 0.50 | 12 |
| Other | 0.29 | 7 |

Employment law cases showed the highest average citation count (3.79), roughly five times higher than Contract cases (0.76). However, a one-way ANOVA test found this difference was **not statistically significant** at the conventional threshold (F = 2.05, p = 0.061, n = 200). This means that, based on this sample, we cannot confidently conclude that case type predicts citation influence — the observed pattern could plausibly be due to chance, though a p-value this close to 0.05 suggests the relationship may be real and simply undetected due to limited sample size in some categories (e.g., Tort and Estate/Trusts each had fewer than 15 cases).

Citation counts by year showed no clear directional trend from 2015–2021, fluctuating between roughly 1.6 and 3.9 average citations per year. The visible decline toward 2023–2024 is best explained by recency — newer cases have had less time to be cited by later courts — rather than a genuine drop in judicial influence.

## Limitations

- **Sample size:** 200 cases is sufficient to demonstrate the analytical pipeline but may be underpowered for smaller case-type categories.
- **Case-type classification:** keyword-based, not manually verified against legal subject-matter coding.
- **Scope:** ONCA is an appellate court; findings do not generalize to trial-level courts (e.g., Ontario Superior Court), which are not available in the A2AJ dataset due to CanLII's terms-of-service restrictions on bulk data access.
- **Recency bias:** citation counts for recent cases are mechanically lower simply because less time has passed for citations to accumulate.

## Conclusion

While Employment law appellate decisions showed the highest average citation influence in this sample, the difference across case types did not reach statistical significance — a result worth reporting honestly rather than overstating. This project demonstrates an end-to-end data analytics pipeline (data sourcing, cleaning, SQL analysis, statistical testing, and dashboard visualization) applied to a real, publicly available legal dataset, bridging quantitative analysis with legal domain interest.

**Tools used:** Python (pandas, scipy), SQL (SQLite), Power BI
**Data source:** A2AJ Canadian Legal Data (`a2aj/canadian-case-law`)
