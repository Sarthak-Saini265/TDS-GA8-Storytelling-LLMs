# Git Setup Instructions

This guide will help you create a GitHub repository and Pull Request for this project.

## Prerequisites
- GitHub account
- Git installed on your system

## Step-by-Step Instructions

### 1. Initialize Git Repository

```bash
# Navigate to your project folder
cd "x:\IITM\TDS\GA8\LLM Storytelling"

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: CAC Analysis with LLM-assisted data storytelling

- Added comprehensive data analysis script (analysis.py)
- Created 4 publication-quality visualizations
- Developed detailed data story in README.md
- Average CAC: 229.12, Target: 150
- Solution: Optimize digital marketing channels
- Student: 23f2005347@ds.study.iitm.ac.in"
```

### 2. Create GitHub Repository

1. Go to https://github.com and sign in
2. Click the "+" icon in top right → "New repository"
3. Repository name: `financial-services-cac-analysis`
4. Description: "Customer Acquisition Cost Analysis - Data Storytelling with LLMs"
5. Choose "Public" (required for PR submission)
6. DO NOT initialize with README (we already have one)
7. Click "Create repository"

### 3. Connect Local Repository to GitHub

```bash
# Add remote origin (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/financial-services-cac-analysis.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

### 4. Create a Pull Request

#### Option A: Using GitHub Web Interface (Recommended)

1. Go to your repository on GitHub
2. Click "Pull requests" tab
3. Click "New pull request"
4. Click "compare across forks" (or "Create a pull request from a fork")
5. Or simply click "Create pull request" if you created a branch

#### Option B: Using a Feature Branch (Better Practice)

```bash
# Create a new branch for your changes
git checkout -b feature/cac-analysis

# Push the branch
git push -u origin feature/cac-analysis

# Go to GitHub - it will show a banner to create PR
# Click "Compare & pull request"
```

### 5. Create the Pull Request

When creating the PR, use this template:

**Title:**
```
CAC Analysis: Data Storytelling with LLM Assistance
```

**Description:**
```
## Summary
Comprehensive analysis of Customer Acquisition Cost (CAC) for Q1-Q4 2024, demonstrating LLM-assisted data storytelling techniques.

## Key Findings
- **Average CAC:** $229.12 (verified)
- **Industry Target:** $150
- **Gap:** $79.12 (52.7% above target)
- **Trend:** Increasing (Q4 spike to $233.27)

## Solution
**Optimize digital marketing channels** to reduce CAC and reach industry benchmark.

## Deliverables
✅ Python analysis script with comprehensive visualizations  
✅ 4 publication-quality charts  
✅ Detailed data story with business insights  
✅ ROI analysis and implementation roadmap  
✅ Student email: 23f2005347@ds.study.iitm.ac.in  

## LLM Assistance
This project was developed using LLM tools (ChatGPT/Claude Code) for:
- Code generation (analysis.py)
- Data visualization design
- Data storytelling structure
- Business insights formulation

## Files Changed
- `README.md` - Comprehensive data story
- `analysis.py` - Analysis script
- `data/cac_data.csv` - Source data
- `requirements.txt` - Dependencies

## Testing
Run the analysis:
```bash
pip install -r requirements.txt
python analysis.py
```

Generates visualizations confirming average CAC of $229.12.

---
**Student:** 23f2005347@ds.study.iitm.ac.in  
**Course:** Data Storytelling with LLMs (GA8)  
**Date:** December 7, 2025
```

### 6. Submit PR URL

Once created, copy the PR URL (it will look like):
```
https://github.com/YOUR_USERNAME/financial-services-cac-analysis/pull/1
```

Submit this URL for your assignment!

## Verification Checklist

Before submitting, verify:

- ✅ README.md contains the correct average: **229.12**
- ✅ Email address (23f2005347@ds.study.iitm.ac.in) is present
- ✅ Solution mentions "optimize digital marketing channels"
- ✅ Data visualizations are included
- ✅ Analysis script runs successfully
- ✅ PR description is comprehensive
- ✅ Repository is public
- ✅ All commits show LLM assistance

## Running the Analysis

To verify the analysis works:

```bash
# Install dependencies
pip install -r requirements.txt

# Run analysis
python analysis.py

# Check output
dir visualizations
```

Should create:
- `cac_trend_analysis.png`
- `cac_gap_analysis.png`
- `cac_dashboard.png`
- `cac_optimization_projection.png`
- `analysis_summary.txt`

## Troubleshooting

### Git not recognized
Install Git from: https://git-scm.com/download/win

### Authentication issues
Use personal access token instead of password:
1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Use token as password when pushing

### Push rejected
```bash
git pull origin main --rebase
git push origin main
```

## Alternative: Using GitHub Desktop

If you prefer a GUI:

1. Download GitHub Desktop: https://desktop.github.com/
2. File → Add Local Repository → Select your folder
3. Publish repository to GitHub
4. Create Pull Request from the app

---

**Need Help?**
Contact: 23f2005347@ds.study.iitm.ac.in

Good luck with your submission! 🚀
