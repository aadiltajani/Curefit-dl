import urllib.request
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


##Path for downloads
path = input("Enter path to store downloads: ")



##Setting Driver and chrome to headless
options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path=r'<PATH TO CHROME DRIVER>', options=options)



links = []
filenames = []



##Getting URLs
##Range numbers denote the value of packs in the URL for specific packages, in this case, 43-47 include packages for WEIGHT LOSS
##Restricted visiting to urls of 4 and 19 because there are no packages for these values
for i in range(43, 48):

    if i in [4, 19]:

        continue

    if i < 10:

        driver.get(
            "https://www.cure.fit/cult/cultdiypack/DIYPACK00{0}?packId=DIYPACK00{0}&pageType=cultdiypack".format(i))

    else:

        driver.get(
            "https://www.cure.fit/cult/cultdiypack/DIYPACK0{0}?packId=DIYPACK0{0}&pageType=cultdiypack".format(i))



    ##Selecting a Pack from the available options one by one
    WebDriverWait(driver, 5).until(
        ec.visibility_of_element_located((By.XPATH, "//div[@class='action-button normal-button']")))

    driver.find_element_by_xpath("//div[@class='action-button normal-button']").click()  # getpack

    driver.refresh()


    ##Getting Video links
    for j in range(1, 7):

        WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, "//div[@class='img-container']")))

        videos = driver.find_elements_by_xpath("//div[@class='img-container']")

        video = videos[j]

        video.click()

        links.append(video.find_element_by_xpath("//source[@type='video/mp4']").get_attribute("src"))

        filenames.append(video.find_element_by_xpath("//div[@class='title-text']").text + video.find_element_by_xpath(
            "//div[@class='subtitle-text']").text + ".mp4")

        driver.refresh()



##Displaying current link in Download
print("displaying links...")

for i in range(len(links)):

    print("Downloading", filenames[i], links[i])

    ##Download Starts
    urllib.request.urlretrieve(links[i], path + filenames[i])



##Storing Filenames and respective links in files in root directory for reference
with open("links.txt", "w") as f:

    for link in links:

        f.writelines(link + "\n")


with open("fname.txt", "w") as f:

    for name in filenames:

        f.writelines(name + "\n")


print("Finished Downloading")
