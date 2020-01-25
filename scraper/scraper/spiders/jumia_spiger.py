import scrapy


class JumiaSpider(scrapy.Spider):
    name = "jumia"

    start_urls = [
        'some jumia url',
    ]

    def parse(self, response):
        for product in response.css('div.product'):
            yield {
                'name': product.css('span.text::text').get(),
                'price': product.css('small.price::text').get(),
                'link': product.css('a.link::text').get(),
            }
