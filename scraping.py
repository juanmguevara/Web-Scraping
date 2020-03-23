# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

# Windows users
executable_path = {'executable_path': 'C:/Users/juanm/OneDrive/Analysis Projects/Web Scraping/chromedriver_win32/chromedriver.exe'}

def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('ul.item_list li.slide')
        #slide_elem.find("div", class_='content_title')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find("div", class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
    except AttributeError:
        return None, None

    return news_title, news_p

def featured_image(browser):

    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    
    try:
        # Find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")
    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'

    return img_url

def hemisphere_title_url(browser):

    # --Visit the mars nasa hemisphere site for Cerberus Hemisphere Enhanced--
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)
    
    # Search the HTML Code
    html = browser.html
    cerberus_soup = BeautifulSoup(html, 'html.parser')

    try:
        # **Use the HTML to find the first `h2` tag and save the text as `cerberus_title`
        cerberus_title = cerberus_soup.find("h2", class_='title').get_text()
    except AttributeError:
        return None

    # Find and click the full image button
    full_image_elem = browser.find_by_id('wide-image-toggle')
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')

    try:
        # Find the relative image url
        img_url_rel = img_soup.select_one('div.wide-image-wrapper img.wide-image').get("src")
    except AttributeError:
        return None

    # **Use the base URL to create an absolute URL
    img_url_cerberus = f'https://astrogeology.usgs.gov/{img_url_rel}'

    # --Visit the mars nasa hemisphere site for Schiaparelli Hemisphere Enhanced--
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)

    # Search the HTML Code
    html = browser.html
    Schiaparelli_soup = BeautifulSoup(html, 'html.parser')

    try:
        # **Use the HTML to find the first `h2` tag and save the text as `Schiaparelli_title`
        Schiaparelli_title = Schiaparelli_soup.find("h2", class_='title').get_text()
    except AttributeError:
        return None

    # Find and click the full image button
    full_image_elem = browser.find_by_id('wide-image-toggle')
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')

    try:
        # Find the relative image url
        img_url_rel = img_soup.select_one('div.wide-image-wrapper img.wide-image').get("src")
    except AttributeError:
        return None

    # **Use the base URL to create an absolute URL
    img_url_Schiaparelli = f'https://astrogeology.usgs.gov/{img_url_rel}'

    # --Visit the mars nasa hemisphere site for Syrtis Major Hemisphere Enhanced--
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)

    # Search the HTML Code
    html = browser.html
    Syrtis_soup = BeautifulSoup(html, 'html.parser')
    
    try:
        # **Use the HTML to find the first `h2` tag and save the text as `Syrtis_title`
        Syrtis_title = Syrtis_soup.find("h2", class_='title').get_text()
    except AttributeError:
        return None
    
    # Find and click the full image button
    full_image_elem = browser.find_by_id('wide-image-toggle')
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')

    try:
        # Find the relative image url
        img_url_rel = img_soup.select_one('div.wide-image-wrapper img.wide-image').get("src")
    except AttributeError:
        return None

    # **Use the base URL to create an absolute URL
    img_url_Syrtis = f'https://astrogeology.usgs.gov/{img_url_rel}'

    # --Visit the mars nasa hemisphere site for Valles Marineris Hemisphere Enhanced--
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)

    # Search the HTML Code
    html = browser.html
    Valles_soup = BeautifulSoup(html, 'html.parser')

    try:
        # **Use the HTML to find the first `h2` tag and save the text as `Valles_title`
        Valles_title = Valles_soup.find("h2", class_='title').get_text()
    except AttributeError:
        return None

    # Find and click the full image button
    full_image_elem = browser.find_by_id('wide-image-toggle')
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')

    try:
        # Find the relative image url
        img_url_rel = img_soup.select_one('div.wide-image-wrapper img.wide-image').get("src")
    except AttributeError:
        return None

    # **Use the base URL to create an absolute URL
    img_url_Valles = f'https://astrogeology.usgs.gov/{img_url_rel}'

    # Creating Python Dictionary for Hemisphere Data
    hemispheredict = [
        {
            "title":cerberus_title,
            "img_url":img_url_cerberus

            #"title":"kitty1",
            #"img_url":"https://live.staticflickr.com/3397/3551189653_501acccd41_b.jpg"
        },
        {
            "title":Schiaparelli_title,
            "img_url":img_url_Schiaparelli
            
            #"title":"kitty2",
            #"img_url":"https://live.staticflickr.com/3397/3551189653_501acccd41_b.jpg"
        },
        {
            "title":Syrtis_title,
            "img_url":img_url_Syrtis
            
            #"title":"kitty3",
            #"img_url":"https://live.staticflickr.com/3397/3551189653_501acccd41_b.jpg"
        },
        {
            "title":Valles_title,
            "img_url":img_url_Valles
            
            #"title":"kitty4",
            #"img_url":"https://live.staticflickr.com/3397/3551189653_501acccd41_b.jpg"
        }
    ]

    #Adding list as value
    #hemispheredict["img_url"] = [
    #    img_url_cerberus, img_url_Schiaparelli, img_url_Syrtis, img_url_Valles
    #]
    #hemispheredict["title"] = [
    #    cerberus_title, Schiaparelli_title, Syrtis_title, Valles_title
    #]    

    return hemispheredict

def mars_facts():

    try:
        # use 'read_html" to scrape the facts table into a dataframe
            df = pd.read_html('http://space-facts.com/mars/')[1]
    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html() 

def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="C:/Users/juanm/OneDrive/Analysis Projects/Web Scraping/chromedriver_win32/chromedriver.exe", headless=True)
    news_title, news_paragraph = mars_news(browser)
    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemisphere": hemisphere_title_url(browser)
    }
    return data

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())