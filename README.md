# My Cyber Blog- Muhammad Subhan Nizal's made on 17/07/2025

**A fully automated, AI-powered cybersecurity portfolio blog—documenting daily technical activity, project work, and professional growth with zero manual effort.**

---

## 🛠 Project Overview

This project integrates your real cyber work into a living, public blog and portfolio site using:

- **ActivityWatch:** Records daily applications and activities on your PC.
- **Python Automation:** Parses logs, classifies cybersecurity activity, and summarizes key projects.
- **Ollama (Local LLM):** Generates professional, reflective blog posts using AI based on your tracked logs and project highlights.
- **MkDocs:** Converts generated content into a static website.
- **GitHub Pages:** Hosts and publishes the portfolio for public access.
- **Windows Task Scheduler:** Ensures daily, hands-off updates and deployments.

---

## 🚦 How It Works

1. **Activity Tracking**  
   ActivityWatch collects all window and application usage logs on your machine.

2. **Data Processing**  
   Python scripts:
   - Export and classify the day’s cybersecurity activities.
   - Read project highlights from a dedicated file (`projects.json`).
   - Combine these into a detailed prompt for AI.

3. **AI Blog Writing**  
   A local LLM (via Ollama) generates a professional Markdown blog post summarizing both your daily activity and major project achievements.

4. **Website Generation & Deployment**  
   - The new post is added to the blog.
   - MkDocs builds the static site.
   - GitHub Pages deploys it publicly at  
     **https://subhan1414.github.io/my-cyber-blog/**

5. **Full Automation**  
   Task Scheduler runs the entire workflow daily, requiring no manual intervention.

---

## 💡 Why This Project Matters

- **Creates a verifiable record** of your hands-on cybersecurity work and learning—ideal for your CV, job applications, and annual reviews.
- **Highlights major projects** and skills development with clear, AI-written descriptions.
- **Showcases automation with Python, local AI models, MkDocs, and CI/CD skills—all highly attractive to employers.**
- Saves time while documenting progress, building a portfolio, and networking professionally.

---

## 📂 Project Structure

my-cyber-blog/
├── mkdocs.yml # MkDocs site configuration
├── docs/ # Blog content (Markdown posts)
│ └── posts/
├── scripts/ # Python and automation scripts
│ ├── export_logs.py
│ ├── summarize_logs.py
│ └── allinone.bat
├── cyber-logs/ # Raw ActivityWatch logs, AI prompts, and generated posts
├── projects.json # Manually maintained project tracking for CV/blog


---

## 🚀 Quickstart

1. **Clone the repo and install dependencies** (Python, ActivityWatch, Ollama, MkDocs).
2. Configure `projects.json` with your project highlights.
3. Set up Windows Task Scheduler to run `scripts/allinone.bat` daily.
4. Visit your live, auto-updating blog at [your GitHub Pages URL](https://subhan1414.github.io/my-cyber-blog/).

---

## ✨ Features

- Full end-to-end automation: log collection → AI content → site update → web publishing
- Modular, customizable, and resume-ready
- Showcases practical DevOps, MLOps, cybersecurity, and writing skills

---

## 🌟 About

Created by [Subhan1414](https://github.com/Subhan1414)  
Integrates AI assistants into workflows for documentation and collaboration, focusing on automating project documentation for CVs[1].  
Uses MkDocs and GitHub Pages to create tech portfolios and blogs[2].
To find out more or to contact me: Subhan05@hotmail.co.uk
---


