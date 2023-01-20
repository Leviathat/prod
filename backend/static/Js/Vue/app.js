import {createApp} from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'
import {getCookie} from "./cookie.js";
import {getToken} from "./csrf.js";

const app = createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            navbar_hidden: true,
            cart_hidden: true,
            cart: JSON.parse(getCookie('cart')),
            csrftoken: getToken('csrftoken'),
            cart_total: 0,
            cart_empty: true,
            rendered: false
        }
    },
    methods: {
        nav_reveal() {
            this.navbar_hidden = !this.navbar_hidden

        },
        cart_reveal() {
            this.cart_hidden = !this.cart_hidden
            this.navbar_hidden = true
        },
        add_to_cart(product) {
            if (this.cart === null || this.cart === undefined) {
                this.cart = {};
                document.cookie = 'cart=' + JSON.stringify(this.cart) + ";domain=;path=/"
            }
            if (this.cart[product['id']] === undefined) {
                this.cart[product['id']] = {
                    'name': product['name'],
                    'type': product['type'],
                    'brand': product['brand'],
                    'price': product['price'],
                    'sale': product['sale'],
                    'quantity': 1,
                }
            } else {
                this.cart[product['id']]['quantity'] += 1
            }
            document.cookie = 'cart=' + JSON.stringify(this.cart) + ";domain=;path=/"
            this.get_cart_total()
        },
        remove_from_cart(product_id) {
            delete this.cart[product_id]
            document.cookie = 'cart=' + JSON.stringify(this.cart) + ";domain=;path=/"
            this.get_cart_total()
        },

        get_cart_total() {
            if (this.cart != null) {

                this.cart_total = Object.entries(this.cart).reduce((counter, obj) => {
                    counter += obj[1]['quantity'];
                    return counter;
                }, 0)
            }

            this.cart_empty = this.cart_total === 0;
        },

    },
    mounted: function () {
        this.get_cart_total()
        document.onreadystatechange = () => {
            if (document.readyState == "complete"){
                this.rendered = true
            }
        }
        // this.$nextTick(function () {
        // })
    },
});
app.mount('#wrapper')