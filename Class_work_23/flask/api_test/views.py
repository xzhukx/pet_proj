from flask import render_template, send_from_directory

from app import app

# <div class="col-sm-4 sm-margin-b-2">
#                         <!-- Pricing -->
#                         <div class="pricing pricing-active">
#                             <div class="margin-b-30">
#                                 <i class="pricing-icon icon-badge"></i>
#                                 <h3>Professional <span> - $</span> 149</h3>
#                                 <p>Lorem ipsum dolor amet consectetur ut consequat siad esqudiat dolor</p>
#                             </div>
#                             <ul class="list-unstyled pricing-list margin-b-50">
#                                 <li class="pricing-list-item">Basic Features</li>
#                                 <li class="pricing-list-item">Up to 100 products</li>
#                                 <li class="pricing-list-item">100 Users Panels</li>
#                             </ul>
#                             <a href="pricing.html" class="btn-theme btn-theme-sm btn-default-bg text-uppercase">Choose</a>
#                         </div>
#                         <!-- End Pricing -->
#                     </div>
#                     <div class="col-sm-4">
#                         <!-- Pricing -->
#                         <div class="pricing">
#                             <div class="margin-b-30">
#                                 <i class="pricing-icon icon-shield"></i>
#                                 <h3>Advanced <span> - $</span> 249</h3>
#                                 <p>Lorem ipsum dolor amet consectetur ut consequat siad esqudiat dolor</p>
#                             </div>
#                             <ul class="list-unstyled pricing-list margin-b-50">
#                                 <li class="pricing-list-item">Extended Features</li>
#                                 <li class="pricing-list-item">Unlimited products</li>
#                                 <li class="pricing-list-item">Unlimited Users Panels</li>
#                             </ul>
#                             <a href="pricing.html" class="btn-theme btn-theme-sm btn-default-bg text-uppercase">Choose</a>
#                         </div>
#                         <!-- End Pricing -->
#                     </div>


@app.route('/')
def re():
    # return 'Hi'
    # TODO get models params

    products = [
        {
            'name': 'Starter Kit',
            'price': 490,
            'description': 'Lorem ipsum dolor amet consectetur ut consequat siad esqudiat dolor',
            'items': ['Extended Features', 'Unlimited products', 'Unlimited Users Panels'],
            'icon': 'pricing-icon icon-shield'
         },
        {
            'name': 'Starter Kit',
            'price': 490,
            'description': 'Lorem ipsum dolor amet consectetur ut consequat siad esqudiat dolor',
            'items': ['Extended Features', 'Unlimited products', 'Unlimited Users Panels'],
            'icon': 'pricing-icon icon-shield'
        }
        ,
        {
            'name': 'Starter 2134234 234 23Kit',
            'price': 4213123,
            'description': 'Lorem ipsum dolor amet consectetur ut consequat siad esqudiat dolor',
            'items': ['Extended Features', 'Unl3214213 423imited products', 'Unlimited Users Panels'],
            'icon': 'pricing-icon2341234 icon-shield'
        }

    ]

    return render_template('index.html', name='aaa', products=products)


@app.route('/pricing')
def rer():
    # return 'Hi'
    return render_template('pricing.html')


@app.route('/about')
def rere():
    # return 'Hi'
    return render_template('about.html')


@app.route('/faq')
def rerer():
    # return 'Hi'
    return render_template('faq.html')


@app.route('/contact')
def rerere():
    # return 'Hi'
    return render_template('contact.html')


@app.route('/products')
def rererer():
    # return 'Hi'
    return render_template('products.html')


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('./templates/js', path)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('./templates/img', path)


@app.route('/vendor/<path:path>')
def send_vendor(path):
    return send_from_directory('./templates/vendor', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('./templates/css', path)
