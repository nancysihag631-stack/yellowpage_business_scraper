# 🕷️ YellowPages Adaptive Scraper (2026-Proof) 🚀

An advanced, resilient web scraping tool built with **Streamlit**, **Playwright**, and **BeautifulSoup4**. This application is engineered to bypass modern bot protection (like Cloudflare challenge screens) and uses an adaptive, multi-selector fallback strategy to consistently extract business leads even if structural HTML layouts change.

---

## ✨ Key Features

*   **🛡️ Anti-Bot Protection Bypass:** Integrates a headless Playwright browser configured with a realistic desktop User-Agent, custom viewport layouts, and direct request headers to mimic legitimate human traffic.
*   **🎯 Adaptive Selector Engine:** Uses a prioritized sequence of modern CSS selectors (`data-` attributes, structural classes, and fallback positional layouts) to automatically detect business listings.
*   **⚡ Built-in Caching:** Implements Streamlit's `@st.cache_data` with a 30-minute Time-To-Live (TTL) to avoid redundant network requests, optimize execution speeds, and reduce ban risks.
*   **📊 Lead Scoring & Quality Metrics:** Automatically calculates a data confidence score (up to 100%) based on data density (Name, Phone, and External Website matches).
*   **💾 Multi-Tiered Exports:** Generates immediate CSV download matrices split between overall harvested targets and filtered 100% "Premium" data rows.

---

## 🛠️ System Architecture

```text
├── yellowpages_scraper_2026.py   # Complete application file (Backend Scraper + Streamlit View)
└── requirements.txt              # Execution dependencies
