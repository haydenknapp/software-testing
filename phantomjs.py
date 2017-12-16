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
        columns = []
        rows = []
        startPos = 0
        while(source.find("</tr>", startPos) > -1):
            rows.append(source[source.find("<tr>", startPos):source.find("</tr>", startPos)])
            startPos = source.find("</tr>", startPos) + 5

        for i in range(1, int(len(rows) / 2)):
            startPos = 0
            while(rows[i].find("</td>", startPos) > -1):
                add = rows[i][rows[i].find("<td>", startPos) + 7:rows[i].find("</td>", startPos) - 2]
                if len(add) > 2:
                    columns.append(add)
                startPos = rows[i].find("</td>", startPos) + 5 

        for i in range(len(columns)):
            print(i, ": ", columns[i])

        if (len(rows) > 1):
            print("Information about the chemistry jobs.")
        else:
            print("Information about the chemistry job.")

    driver.quit()
