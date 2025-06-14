# 📚 Automated Book Publication Workflow

This project demonstrates an end-to-end system that automates the publication workflow of book content from the web. The system performs intelligent scraping, AI-driven content rewriting ("spinning"), supports human-in-the-loop iterations, and stores content versions using ChromaDB, with intelligent retrieval powered by a reinforcement learning-based search algorithm.

> 🔍 **Sample Target:**  
> https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1

---

## 📌 Objectives

- Fetch content from Wikisource
- Capture screenshots of each chapter
- Apply AI "spinning" and refinement using LLMs (e.g., Gemini, GPT-4)
- Enable human iterations for writer/reviewer/editor roles
- Maintain versioned content with ChromaDB
- Retrieve finalized versions via RL-powered semantic search

---

## 🛠️ Tech Stack

| Component | Tool |
|----------|------|
| Scraping & Screenshots | Playwright (Python) |
| AI Writing | Gemini / GPT-4 |
| Human-in-the-loop Editing | Custom Prompt Chains |
| Versioning | ChromaDB |
| Retrieval | RL-based semantic search (e.g., bandit + cosine similarity) |
