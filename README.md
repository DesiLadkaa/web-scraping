web-scraping/
│
├── .venv/                     # Local virtual environment (not Git)
├── .python-version            # Python version
├── .gitignore                 # Files Git should ignore
├── README.md                  # Project documentation
├── pyproject.toml             # Project metadata and dependencies
├── uv.lock                    # Exact dependency versions
│
├── src/
│   └── web_scraping_lab/
│       ├── __init__.py
│       │
│       ├── fetchers/           # Download webpages
│       ├── parsers/            # Parse HTML
│       ├── extractors/         # Extract useful information
│       ├── crawlers/           # Discover and crawl URLs
│       ├── pipelines/          # Coordinate processing
│       ├── storage/            # Save extracted data
│       └── agents/             # AI agent integration (later)
│
├── tests/                      # Automated tests
│
├── examples/                   # Small runnable examples
│
├── notebooks/                  # Experiments and exploration
│
├── data/
│   ├── raw/                    # Original downloaded content
│   └── processed/              # Cleaned and extracted data
│
├── docs/                       # Architecture and engineering notes
│
└── scripts/                    # Maintenance and utility scripts


# Web Scraping Lab

A practical Python engineering project exploring modern web scraping,
large-scale web data extraction, and AI-powered web research systems.

## Objectives

- Understand HTTP and website architecture.
- Build HTTP-based web scrapers.
- Parse HTML and extract structured information.
- Build website crawlers.
- Handle JavaScript-rendered websites.
- Explore scalable crawling and data pipelines.
- Prepare web content for RAG and LLM applications.
- Integrate web capabilities with MCP and AI agents.

## Technology Stack

- Python 3.11
- uv
- HTTPX
- BeautifulSoup4
- lxml
- pytest
- Ruff

Additional technologies will be introduced as the project evolves.

## Setup

Install dependencies:

    uv sync

Run the application:

    uv run web-scraping-lab

Run tests:

    uv run pytest

Check code quality:

    uv run ruff check .

Format code:

    uv run ruff format .

## Project Structure

Application source code lives in `src/web_scraping_lab/`.

- fetchers: HTTP and browser retrieval
- parsers: HTML parsing
- extractors: Structured information extraction
- crawlers: URL discovery and crawling
- pipelines: Data processing workflows
- storage: Data persistence
- agents: AI agent integration

## Learning Progress

- [X] Initial project setup
- [ ] HTTP fundamentals
- [ ] Basic web scraping
- [ ] HTML parsing
- [ ] Structured extraction
- [ ] Web crawling
- [ ] Browser automation
- [ ] Modern scraping infrastructure
- [ ] AI-ready data pipelines
- [ ] MCP web tools
- [ ] AI research agent
