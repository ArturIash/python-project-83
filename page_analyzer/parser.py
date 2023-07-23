def get_data_from_html(html_content) -> tuple:
    h1 = html_content.h1.get_text() if html_content.h1 else ""
    title = html_content.title.get_text() if html_content.title else ""
    description = html_content.find("meta", {"name": "description"})
    description_content = description["content"] if description else ""

    return h1, title, description_content