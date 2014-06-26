from urlparse import urlparse

def main(request, response):
    try:
        code = int(request.GET.first("code", 302))
        location = request.GET.first("location", request.url_parts.path +"?followed")

        allowed_links = ["http://example.not", "mailto:someone@example.org", "http://example.not", "foobar:someone@example.org"]
        if location not in allowed_links:
            local_parsed = urlparse(location)
            request_parsed = urlparse(request.url)
            if local_parsed.hostname != None and local_parsed.hostname != request_parsed.hostname and local_parsed.hostname != ("www2." + request_parsed.hostname):
                return "illegal redirect url"

        if request.url.endswith("?followed"):
            return [("Content:Type", "text/plain")], "MAGIC HAPPENED"
        else:
            return (code, "WEBSRT MARKETING"), [("Location", location)], "TEST"
    except Exception,ex:
        return "error"
