from selenium import webdriver
from bs4 import BeautifulSoup

if __name__ == "__main__":
    driver = webdriver.PhantomJS()
    driver.set_window_size(1920, 1080)
    driver.get("http://jobs.kent.edu/cw/en-us/search/?search-keyword=chemistry")
    driver.find_element_by_id("search-keyword")
    source = driver.page_source
    if ("No jobs matched your search.") in source:
        print("No jobs found!")
    else:
        soup = BeautifulSoup(source, "html.parser")
        jobtitles = soup.find_all("b")
        jobinfo = soup.find_all("<td>")
        if (len(jobtitles) > 1):
            print("Information about the chemistry jobs.")
        else:
            print("Information about the chemistry job.")

    curindex = 0
    for i in range(int(len(jobtitles) / 2)):
        jobtitles[i] = str(jobtitles[i])
        print(jobtitles[i][jobtitles[i].index("\">") + 2:jobtitles[i].index("</a>")])
    for i in range(len(jobinfo)):
        print(jobinfo[i])
    driver.quit()
