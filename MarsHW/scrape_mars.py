from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
from selenium import webdriver

def scrape():

# NASA Mars News

    ## URL of NASA news
    url = 'https://mars.nasa.gov/news/'

    # Retrieve page with the requests module
    html = requests.get(url)

    ## Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html.text, 'html.parser')
    results = soup.find_all('div', class_= "slide")[0]

    news_p_list = []
    news_title_list = []
    for div in soup.find_all('div', class_= "slide"):
        news_p_list.append(div.find('div', attrs={'class': 'rollover_description_inner'}).text)
        news_title_list.append(div.find('div', attrs={'class': 'content_title'}).text)
        
    news_title_list = [w.replace('\n', '') for w in news_title_list]
    news_p_list = [w.replace('\n', '') for w in news_p_list]
    news_title = news_title_list[0]
    news_p = news_p_list[0]
    #print("Step 1:", news_title, " ", news_p)

# JPL Mars Space Images - Featured Image
    executable_path = {"executable_path": "C:/Users/aeise/Chrome/chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)
    pic_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(pic_url)

    #  Click & pull new page html
    browser.click_link_by_partial_text('FULL IMAGE')
    pic_html = browser.html

    # Parse new html
    soup = BeautifulSoup(pic_html, 'html.parser')

    # Image URL`
    partial = soup.find('a', class_ = 'button fancybox')['data-fancybox-href']
    featured_image_url = "https://www.jpl.nasa.gov" + partial

    browser.quit()
    #print("Step 2:", featured_image_url)

# Mars Weather

    ## URL of NASA tweets
    url = 'https://twitter.com/marswxreport?lang=en'

    # Retrieve page with the requests module
    html = requests.get(url)

    soup = BeautifulSoup(html.text, 'html.parser')
    results = soup.find_all('div', class_= "stream")

    for result in results:
        if result.ol.li.div['data-name'] == "Mars Weather":
            mars_weather = (result.p.text)

    #print("Step 3:", mars_weather)

# Mars Facts
    ## URL of Mars facts
    url = 'https://space-facts.com/mars/'

    ## Retrieve page with the requests module
    fact_url = "https://space-facts.com/mars/"

    # Get df
    df = pd.read_html(fact_url)
    df = pd.DataFrame(df[0]).set_index(0)

    # Convert table to HTML string
    mars_html = df.to_html(header = False).replace('\n  ','').replace('<table border="1" class="dataframe">','').replace('</table','').replace('\n>','')

    #print("Step 4", df.to_string(index = False))
#Mars Hemispheres
    executable_path = {"executable_path": "C:/Users/aeise/Chrome/chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # Retrieve page with the requests module
    html = requests.get(url)

    soup = BeautifulSoup(html.text, 'html.parser')
    results = soup.find_all('h3')
    titles = []
    for result in results:
        titles.append(result.text)
    # print(titles)


    mars_list = []

    for x in titles:
        mars_dict = {}
        browser.visit(url)
        browser.click_link_by_partial_text(x)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        results = soup.find('div', class_= "downloads")
        mars_dict['title'] = x
        mars_dict['hemi_img_url'] = results.ul.li.a['href']
        mars_list.append(mars_dict)

    browser.quit()


    #print(mars_list)
    #print("Step 5",title, " ", hemi_img_url)

#Create dictionary called scraper

    scrape_mars = {}
    scrape_mars['news_title'] = news_title
    scrape_mars['news_p'] = news_p
    scrape_mars['featured_image_url'] = featured_image_url
    scrape_mars['mars_weather'] = mars_weather
    scrape_mars['mars_html'] = mars_html
    scrape_mars['hemisphere'] = mars_list

    return scrape_mars


