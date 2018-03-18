import execjs
def get_vl5x(cook_dic):
    f = open("./js/hand_cookie.js", 'r', encoding='UTF-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    ctx = execjs.compile(htmlstr)
    vl5x= ctx.call('getKey',cook_dic.get('vjkl5'))
    return vl5x

def get_guid():
    f = open("./js/create_guid.js", 'r', encoding='UTF-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    ctx = execjs.compile(htmlstr)
    guid= ctx.call('guid')
    return guid


if __name__ == '__main__':
    print(get_js({"vjkl5":"8b98549269dff0f29620122185ab91686ef4e198"}))