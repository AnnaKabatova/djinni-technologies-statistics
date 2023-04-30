import scrapy

from scrapy.http import Response


def delete_double_symbols(text: list) -> str:
    if len(text) > 1:
        out = [
            list(text)[0],
        ]
        for i in range(1, len(text)):
            if text[i] == text[i - 1] and text[i] in ".,;":
                continue
            else:
                out.append(text[i])
        return "".join(out)
    return ""


def delete_empty_lines(array: list) -> list:
    out = [delete_double_symbols(element) for element in array if (element != "" and element != ",")]
    return out


def parse_detail_vacancy(response: Response) -> None:
    yield {
        "title": response.css("h1::text").get().strip(),
        "company": response.css(".job-details--title::text").get().strip(),
        "salary": response.css("h1 .public-salary-item::text").get(),
        "category": delete_empty_lines(
            [
                text.replace("\n", "").strip()
                for text in response.css(".job-additional-info--body")[0]
                .css("div::text")
                .getall()
            ]
        ),
        "publicated": delete_empty_lines(
            [
                text.replace("\n", "").strip()
                for text in response.css(".text-muted::text").getall()
            ]
        ),
        "description": delete_empty_lines(
            [
                text.replace("\n", "").strip()
                for text in response.css(".profile-page-section")[0]
                .css("div::text")
                .getall()
            ]
        ),
    }


class DjinniSpider(scrapy.Spider):
    name = "djinni"
    allowed_domains = ["djinni.co"]
    start_urls = ["http://djinni.co/jobs/?primary_keyword=Python"]

    def parse(self, response: Response, **kwargs):
        page_urls = response.css("ul.list-jobs .order-1 a::attr(href)").getall()
        for url in page_urls:
            full_url = response.urljoin(url)
            yield scrapy.Request(full_url, parse_detail_vacancy)

        next_page = response.css(".pagination li.page-item a::attr(href)").getall()[-1]
        url_next_page = response.urljoin(next_page)
        yield scrapy.Request(url_next_page, self.parse)
