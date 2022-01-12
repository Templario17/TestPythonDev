def show(content=''):
    print("Content-type: text/html; charset=utf-8")
    print("")
    print(content)


def show_ajax(content=''):
    print("Content-type: text/html; Charset=utf-8")
    print("Access-Control-Allow-Origin: *")
    print("")
    print(content)
    
def show_json(content=''):
    print("Content-type: application/json; charset=utf-8")
    print("")
    print(content)
        
def redirect(url):
    print("Content-type: text/html; charset=utf-8")
    print("Location: {}".format(url))
    print("")
