# Algona Web Scraper

## Overview
This project provides a Python script (`auto_scrape_zones.py`) designed to automatically navigate through a website with a nested structure and scrape required information, specifically zones and their descriptions. The scraped data is saved in a JSON file named `zones.json`.

## Objectives
- To create a scraper that can handle nested web structures.
- To automatically find and scrape zone information and their descriptions.
- To ensure compatibility with [Algona](https://algona.municipal.codes/) website.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Setup Instructions

### Prerequisites
Ensure you have Python 3.x installed.

### Install Required Libraries
Install the necessary Python libraries using pip:
```bash
pip install requests beautifulsoup4
```

### Script Execution
1. Download the `auto_scrape_zones.py` script to your local machine.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Python:
   ```bash
   python auto_scrape_zones.py
   ```

### Output
The script will generate a JSON file named `zones.json` in the same directory. This file contains the zones' numbers, title, and their descriptions.

## Demo Video
[media.webm](https://github.com/malikoyv/AlgonaScraper/assets/124885789/795409d7-5790-4634-b037-93b3c7623a93)

## Script Details
1. **Initialize Variables**: `zone_info` to store the scraped information, and `URL` for the website link.
2. **Set Headers**: To mimic a real browser request.
3. **Request the Homepage**: Check if the request is successful.
4. **Parse Zones Page**: Navigate to the page containing zone links.
5. **Find and Iterate Through Zone Links**: Extract and request each zone link.
6. **Scrape Zone Information**: Extract the number, title, and description for each zone.
7. **Save Data**: Use the `save_json` function to save the collected data.

### Script Execution
```python
if __name__ == "__main__":
    main()
```
This ensures the `main` function runs when the script is executed.

## Notes
- The script is currently tailored for the `https://algona.municipal.codes` website. You may need to adjust the parsing logic for other websites like Airway Heights, Albion, Anacortes, and Arlington.
- Ensure the website structure and elements (like `span` with class `name` and `article` for description) match the ones used in this script.
