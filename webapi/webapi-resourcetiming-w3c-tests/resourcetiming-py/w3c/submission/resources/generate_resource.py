import os


def main(request, response):
    try:
        get_type = request.GET.first("types")

        status = 200
        body = ""
        content_type = "text/plain"

        def file_get_contents(path):
            file_object = open(
                os.path.split(
                    os.path.realpath(__file__))[0] +
                os.path.sep +
                path)
            try:
                content = file_object.read()
            finally:
                file_object.close()
            return content

        def audio():
            body = file_get_contents("silence.wav")
            content_type = "audio/wav"

        def css():
            body = file_get_contents("gray_bg.css")
            content_type = "text/css"

        def font():
            body = file_get_contents("Ahem.ttf")
            content_type = "application/octet-stream"

        def iframe():
            body = file_get_contents("blank_page_green.htm")
            content_type = "text/html"

        def image():
            body = file_get_contents("1x1-blue.png")
            content_type = "image/png"

        def script():
            body = file_get_contents("empty_script.js")
            content_type = "text/javascript"

        operator = {
            "audio": audio,
            "css": css,
            "font": font,
            "iframe": iframe,
            "image": image,
            "script": script}

        if get_type in operator:
            operator.get(get_type)()
        else:
            status = 404

        headers = [("Content-Type", content_type)]

        if "cacheable" in request.headers:
            headers.append(("Etag", 7))
        else:
            headers.append(("Cache-control", "no-cache"))

        return status, headers, body
    except Exception as ex:
        return "error"
