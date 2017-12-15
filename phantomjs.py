from selenium import webdriver

if __name__ == "__main__":
    driver = webdriver.PhantomJS()
    driver.set_window_size(1920, 1080)
    driver.get("http://jobs.kent.edu/cw/en-us/search/?search-keyword=chemistry")
    driver.find_element_by_id("search-keyword")
    source = driver.page_source
    if ("No jobs matched your search.") in source:
        print("No jobs found!")
    else:
        if (len(jobtitles) > 1):
            print("Information about the chemistry jobs.")
        else:
            print("Information about the chemistry job.")

    driver.quit()
