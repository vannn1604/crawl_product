import scrapy


class SpecsSpider(scrapy.Spider):
    name = "spec"
    allowed_domains = ["www.gsmarena.com"]
    start_urls = ["https://www.gsmarena.com/makers.php3"]

    def parse(self, response):
        for a in response.xpath('//*[@id="body"]/div/div[2]/table/tr/td/a'):
            yield response.follow(
                a, callback=self.parse_brand, cb_kwargs={"brand": a.xpath("./text()").get()}
            )

    def parse_brand(self, response, brand):
        for product in response.xpath('//*[@id="review-body"]/div[1]/ul/li/a'):
            yield response.follow(
                product,
                callback=self.parse_specs,
                cb_kwargs={"name": product.xpath("./strong/span/text()").get(), "brand": brand},
            )

        for a in response.xpath('//a[@class="pages-next"]'):
            yield response.follow(a, callback=self.parse_brand, cb_kwargs={"brand": brand})

    def parse_specs(self, response, name, brand):
        specs = {}
        for i, table in enumerate(response.xpath('//*[@id="specs-list"]/table')):
            th = table.xpath("./tr[1]/th/text()").get()
            specs[th] = {}
            for j, tr in enumerate(table.xpath("./tr")):
                if i == 0 and j == 0:
                    td2 = tr.xpath("./td[2]/a/text()").get()
                else:
                    td2 = tr.xpath("./td[2]/text()").get()
                td1 = tr.xpath("./td[1]/a/text()").get()
                if not td1:
                    td1 = "Other"
                specs[th][td1] = td2

        yield {"brand": brand, "name": name, "specs": specs}


"""
        for a in response.xpath('//*[@id="user-comments"]/div[4]/div[1]/ul/li[1]/a'):
            yield response.follow(
                a,
                callback=self.parse_reviews,
                cb_kwargs={"name": name, "brand": brand, "specs": specs},
            )

    def parse_reviews(self, response, name, brand, specs):
        # for div in response.xpath('//div[@class="user-thread"]'):
        #     review = {
        #         "username": div.xpath("./ul[1]/li[1]/a/b/text()").get(),
        #         "time": div.xpath("./ul[1]/li[3]/time/text()").get(),
        #         "content": div.xpath("./p/text()").get(),
        #         "rating": div.xpath("./ul[2]/li[1]/span[2]/text()").get(),
        #         "location": div.xpath("./ul[1]/li[2]/span/text()").get(),
        #     }
        reviews = []
        reviews.append(self.parse_all_reviews(response, []))
        print(reviews, "1111111111111111111111111111111111111111111111111111111111111")
        # yield {"brand": brand, "name": name, "specs": specs, "reviews": reviews}

    # def parse_all_reviews(self, response, reviews):
    #     for div in response.xpath('//div[@class="user-thread"]'):
    #         review = {
    #             "username": div.xpath("./ul[1]/li[1]/a/b/text()").get(),
    #             "time": div.xpath("./ul[1]/li[3]/time/text()").get(),
    #             "content": div.xpath("./p/text()").get(),
    #             "rating": div.xpath("./ul[2]/li[1]/span[2]/text()").get(),
    #             "location": div.xpath("./ul[1]/li[2]/span/text()").get(),
    #         }
    #         reviews.append(review)

    #     for i, a in enumerate(response.xpath('//a[@title="Next page"]')):
    #         yield response.follow(
    #             a, callback=self.parse_all_reviews, cb_kwargs={"reviews": reviews}
    #         )
    #         i += 1
    #     yield reviews
"""

