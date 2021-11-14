import justpy as jp


# Every justpy object have main object known as
# TODO : QUASAR PAGE
# that is a web page
# may contain different elements

# Why called Quasar page because
# it is a JS framework that is used by python to render pages


def app():
    qp = jp.QuasarPage()
    h1 = jp.QDiv(a=qp, text="This is div", classes="text-h3")
    styled_div = jp.QDiv(a=qp, text="This is styled div", classes="text-h4 text-center shadow-4")
    print(h1)
    return qp


jp.justpy(app)
