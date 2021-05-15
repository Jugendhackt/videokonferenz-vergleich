from flask import request, Flask, render_template, make_response, url_for, redirect

class Engine():
    def __init__(self):
        return 0

    def setcookie(key, data,response = "", duration = None):
        res = make_response(response)
        res.set_cookie(key, data, duration)
        return res

    def cookie_check(name):
        if request.cookies.get(name):
            return True
        else:
            return False
    
    def cookie_content(name):
        return request.cookies.get(name)

    def cookie_delete(response = redirect("/")):
        for y in request.cookies:
            #print(y)
            res = make_response(response)
            res.set_cookie(y , "", expires=0)
            return res

            