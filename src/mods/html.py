from playwright.sync_api import sync_playwright

class Module:

    @staticmethod
    def render(_, html: str) -> bytes:
        "render html as bytes"

        for tag in ("html", "head", "body"):
            assert f"</{tag}>" in html, f"missing tag: </{tag}>"

        with sync_playwright() as p, p.chromium.launch() as b:

            (page := b.new_page()).set_content(html)
            return page.screenshot()