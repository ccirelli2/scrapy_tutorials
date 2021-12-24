"""
Module for tutorial scrapers.


Questions:
- Does scrapy treat spiders similar to fixtures, where they automatically
get loaded and or called?
- If so, how does that affect the flow of code?
- Instead of declaring a webpage as an attribute can it be passed in as
a parameter?


CSS Syntax: Ex1

    HTML
    --------
    <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">

    Request
    --------
    quote = response.css("div.quote")

    Interpretation
    --------
    <div: is an html tag. It defines divisions or sections in an html doc.
        div is like a container.

    quote: is the value of the class element.  Html classes referred to
        objects with pre-defined styling.  So when we refer to quote, all
        quotes have a pre-defined style.


CSS Syntax: Ex2
    HTML
    ----------
    <span class="text" itemprop="text">“The world as we have.”</span>

    Request
    ----------
    quote_text = quote.css("span.text::text").get()

    Interpretation
    ----------
    <span: is the html tag used to mark up a part of a text.
"""
###############################################################################
# Import Libraries
###############################################################################
import scrapy


###############################################################################
# Scrapers
###############################################################################
class QuotesSpider(scrapy.Spider):
    """
    QuotesSpider.
    """

    # Define Attributes
    name = "quotes-spider"
    results = {'title': []}
    start_urls = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/",
    ]

    def parse(self, response):
        """
        Function to parse response.
        Spyder automatically calls Response.get as the call-back.

        :param response:
        """
        # Parse the Response Object (response.body contains the page)
        page_title = response.css('title').get()
        yield {'@@@@@@@@@@@title': page_title}
        self.results['title'].append(page_title)


if __name__ == "__main__":
    pass
