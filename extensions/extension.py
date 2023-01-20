import gi
gi.require_version('Soup', '2.4')
from gi.repository import Soup

def on_document_loaded(webpage):
    # print("document-loaded: uri =", webpage.get_uri())
    document = webpage.get_dom_document()
    # print("document-loaded: title =", document.get_title())

def set_headers(web_page, uri_request, uri_response):
    # For more documentation, head over to:
    # https://libsoup.org/libsoup-2.4/SoupMessageHeaders.html
    
    http_headers = uri_request.get_http_headers()
    # http_method = uri_request.get_http_method()
    # Soup.MessageHeaders.replace(http_headers, "Accept-Encoding", "gzip, deflate, br")
    Soup.MessageHeaders.append(http_headers, 'Task', 'Done')


def on_page_created(extension, webpage):
    # doc = webpage.get_dom_document()
    # nodes = doc.get_elements_by_tag_name('body')
    # print('Nodes:', nodes)
    webpage.connect('send-request', set_headers)
    webpage.connect("document-loaded", on_document_loaded)


def initialize(extension, arguments):
    # print("initialize: arguments =", arguments)
    extension.connect("page-created", on_page_created)
