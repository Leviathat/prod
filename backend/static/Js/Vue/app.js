import {createApp} from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'
import {getCookie} from "./cookie.js";
import {getToken} from "./csrf.js";
import {getAlert} from "./alerts.js"

const app = createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            navbar_hidden: true,
            cart: JSON.parse(getCookie('cart')),
            jwt_token: getCookie('jwt'),

            rendered: false,
            cart_hidden: true,
            alerts: [],
            fio: null,
            email: null,
            phone: null,
            city: null,
            street: null,
            house: null,

            price_range: 10000,
            filter_sold: false,

            otp_sent: false,
            otp: null,
            message: null,
            pass: null,
            pass_rep: null,


            profile_selected_nav: 1
        }
    },
    computed: {
        verified: function () {
            if (this.otp && this.otp.toString().length === 4) {
                setTimeout(() => {
                    this.otp_sent = false;
                }, 2000);
                return true
            }
        },
        cart_empty: function () {
            return this.cart_total === 0
        },
        cart_total: function () {
            if (this.cart != null) {
                return Object.entries(this.cart).reduce((counter, obj) => {
                    counter += obj[1]['quantity'];
                    return counter;
                }, 0)
            }
            return 0
        },
        cart_summary: function () {
            if (this.cart != null) {
                return Object.entries(this.cart).reduce((counter, obj) => {
                    counter += obj[1]['price'];
                    return counter;
                }, 0)
            }
            return 0
        }
    },
    methods: {
        profile_select_nav(i) {
            this.profile_selected_nav = i
        },
        // REGISTER
        send_otp() {
            if (this.phone && this.phone.toString().length === 11) {
                setTimeout(() => {
                    this.otp_sent = true
                }, 500);
            } else {
                getAlert('error', '?????????????? ???????? ????????')
            }

        },
        set_token() {
            document.cookie = 'jwt=' + this.jwt_token + ";domain=;path=/"
        },
        profile() {
            if (this.jwt_token === null) {
                window.location.href = "/login/"
            }
            else {
                axios.get('/api/user/', {
                    headers: {
                        'Authorization': 'token $jwt'.replace('$jwt', this.jwt_token)
                    }
                }).then(res => {
                    getAlert('success', 'True')
                }).catch((error) => {
                    getAlert('error', 'False')
                    if (error.response) {
                        console.log(error.response.data);
                    }
                });
                window.location.href = "/profile/"
            }
        },
        register() {
            let user = {
                "phone_number": this.phone,
                "email": this.email,
                "password": this.pass
            };
            axios.post('/api/users/', {
                "user": user
            }).then(res => {
                this.jwt_token = res.data.token
                this.set_token()
                getAlert('success', '?????????????????????? ???????????? ??????????????')
            }).catch((error) => {
                getAlert('error', '???????????????? ???????????? ?????? ??????????????????????')
                if (error.response) {
                    console.log(error.response.data);
                }
            });
        },
        login() {
            let user = {
                "email": this.email,
                "password": this.pass
            };
            axios.post('/api/users/login/', {
                "user": user
            }).then(res => {
                console.log(res)
                this.jwt_token = res.data.user.token
                getAlert('success', '???? ?????????????? ??????????')
                this.set_token()
                window.location.href = "/profile/"
            }).catch((error) => {
                getAlert('error', '???????????????? ???????????? ?????? ??????????????????????')
                if (error.response) {
                    console.log(error.response.data);
                }
            });
        },
        // NAVBAR
        nav_reveal() {
            this.navbar_hidden = !this.navbar_hidden
        },

        //CART
        cart_refresh() {
            document.cookie = 'cart=' + JSON.stringify(this.cart) + ";domain=;path=/"
        },
        cart_reveal() {
            this.cart_hidden = !this.cart_hidden
            console.log(this.cart_hidden)
            this.navbar_hidden = true
        },
        add_to_cart(product) {
            if (!product['sold']) {
                if (this.cart === null || this.cart === undefined) {
                    this.cart = {};
                    this.cart_refresh()
                }
                if (this.cart[product['id']] === undefined) {
                    this.cart[product['id']] = {
                        'name': product['name'],
                        'type': product['type'],
                        'brand': product['brand'],
                        'price': product['price'],
                        'sale': product['sale'],
                        'image_url': product['image'],
                        'quantity': 1,
                    }
                } else {
                    this.cart[product['id']]['quantity'] += 1
                }
                this.cart_refresh()
                getAlert('success', '?????????? ???????????????? ?? ??????????????')
            } else {
                getAlert('error', '???????????? ?????? ?? ??????????????')
            }
        },
        remove_from_cart(product_id) {
            delete this.cart[product_id]
            this.cart_refresh()
        },
        // ORDER
        make_order() {
            let cart = {}
            for (const [id, obj] of Object.entries(this.cart)) {
                cart[id] = obj['quantity']
            }
            axios.post('/order/', {
                cart: cart,
                email: this.email,
                phone: this.phone,
                fio: this.fio,
                city: this.city,
                street: this.street,
                house: this.house,
                summary: this.cart_summary
            }).then(res => {
                getAlert('success', '?????????? ????????????????')
                console.log(res)
                this.cart = {}
                this.cart_refresh()
                window.location.href = "/"
            }).catch((error) => {
                getAlert('error', '???????????????? ???????????? ?????? ????????????????????')
                if (error.response) {
                    console.log(error.response.data);
                }
            });
        },
    },
    mounted: function () {
        document.onreadystatechange = () => {
            if (document.readyState === "complete") {
                this.rendered = true
            }
        }
    },
});
app.mount('#wrapper')