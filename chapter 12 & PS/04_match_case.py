def http(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "Not found"
        case _:
            return "Something's wrong with the internet "


print(http(400))
print(http(404))
print(http(418))    
print(http(200))
        