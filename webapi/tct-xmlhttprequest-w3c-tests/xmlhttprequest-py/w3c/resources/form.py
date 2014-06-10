def main(request, response):
    try:
        return "id:%s;value:%s;" % (request.POST.first("id"), request.POST.first("value"))
    except Exception,ex:
        return Exception,":",ex
