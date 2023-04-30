# djinni-technologies-statistics
Djinni Python technologies statistics

This application allows you to make data analysis on the open vacancies in the python section on the Djinni site. By using this, you can track what technologies are popular for that category now, and what requirements are there for different levels.


### Installation
1. To work with the project, you must have python 3.10 or higher installed.
2. Clone the forked repo
    ```
    git clone https://github.com/AnnaKabatova/djinni-technologies-statistics.git
    ```
3. Open the project folder.
4. Install all of the Python modules and packages listed in requirements.txt file to your environment
   ```
   python -m venv venv
   venv\Scripts\activate (on Windows)
   source venv/bin/activate (on macOS) 
   pip install -r requirements.txt
   ```

###  Usage

- Run scraper from directory, where is spiders directory
   ```
  cd technologies
  scrapy crawl djinni -O vacancies.csv
   ```
- Open Jupyter notebook analytics.ipynb and run
