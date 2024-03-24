import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.core.os_manager import ChromeType


driver = None


@pytest.fixture(scope="class")
def setup(request, browser):
    global driver
    # setup
    if browser == "ff":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "chromium":
        driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    driver.get("https://www.yatra.com/")
    driver.implicitly_wait(60)
    driver.maximize_window()
    request.cls.driver = driver  # this driver should be available at the class level of requesting class
    yield
    driver.close()  # teardown

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         extra.append(pytest_html.extras.url("http://www.google.com/"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             report_directory = os.path.dirname(item.config.option.htmlpath)
#             file_name = str(int(round(time.time() * 1000))) + ".png"
#             # file_name = report.nodeid.replace("::", "_") + ".png"
#             destinationFile = os.path.join(report_directory, file_name)
#             driver.save_screenshot(destinationFile)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>'%file_name
#             extra.append(pytest_html.extras.html(html))
#         report.extra = extra

# def pytest_html_report_title(report):
#     report.title = "Selenium Automation Report"