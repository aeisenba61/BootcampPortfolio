from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
from selenium import webdriver

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:/Users/aeise/Chrome/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

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
    html = requests.get(url)

    soup = BeautifulSoup(html.text, 'html.parser')

    td1 = []
    td2 = []

    for tr in soup.find_all('tr'):	
        td1.append(tr.find_all('td')[0].text.replace('\n',''))
        td2.append(tr.find_all('td')[1].text.replace('\n',''))
        
    df = pd.DataFrame(
        {'column_name': td1,
         'stat': td2
        })

    mars_html = df.to_html


    ##print(df.to_string(index = False))
    #print("Step 4", df.to_string(index = False))

# Mars Hemispheres
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # Retrieve page with the requests module
    html = requests.get(url)

    soup = BeautifulSoup(html.text, 'html.parser')
    results = soup.find_all('h3')
    titles = []
    for result in results:
        titles.append(result.text)
    #print(titles)

    title = []
    hemi_img_url = []

    for x in titles:
        browser.visit(url)
        browser.click_link_by_partial_text(x)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        results = soup.find('div', class_= "downloads")
        title.append(x)
        hemi_img_url.append(results.ul.li.a['href'])

    mars_dict = dict(zip(title, hemi_img_url))
    #print(mars_dict)
    #print("Step 5",title, " ", hemi_img_url)

#Create dictionary called scraper

    scrape_mars = {
        'news_title' : news_title,
        'news_p' : news_p,
        'featured_image_url' : featured_image_url,
        'mars_weather' : mars_weather,
        'mars_html' : mars_html,
        'hemisphere' : mars_dict
        }

    return scrape_mars


