def main(request, response):
    mime = request.GET.first("mime", "text/event-stream")
    message = request.GET.first("message", "data: data")
    newline = "" if request.GET.first("newline", None) == "none" else "\n\n"

    headers = [("Content-Type", mime)]
    body = message + newline + "\n"

    # XSS filter
    body = body.replace("&", "&amp;") # Must be done first!
    body = body.replace("<", "&lt;")
    body = body.replace(">", "&gt;")
    body = body.replace('"', "&quot;")
    body = body.replace("'", "&#x27;")
    body = body.replace("/", "&#x2f;")

    return headers, body
