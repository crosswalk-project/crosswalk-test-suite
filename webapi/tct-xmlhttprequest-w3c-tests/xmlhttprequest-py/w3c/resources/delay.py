import time


def main(request, response):
    delay = float(request.GET.first("ms", 500))
    if delay in range(10000):
        time.sleep(delay / 1E3)
    return [("Content-type", "text/plain")], "TEST_DELAY"
