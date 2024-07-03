from seleniumwire import webdriver

urls = []
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

page = "https://starrailstation.com/en/achievements"
driver.get(page)

for request in driver.requests:
    if request.response:
        # print(request.url, request.response.status_code, request.response.headers['Content-Type'])
        urls.append([page, request.url, request.response.status_code, request.response.headers['Content-Type']])
        if request.url.startswith("https://starrailstation.com/api/v1/data/") and \
                request.response.headers['Content-Type'] == "application/json":
            print(request.url)
driver.quit()
