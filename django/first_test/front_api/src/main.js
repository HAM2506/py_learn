// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import FastClick from 'fastclick'
import VueRouter from 'vue-router'
import App from './App'
import axios from 'axios'
import routers from './router/index'
import './assets/css/common.css'
import filters from './filter/filter.js'

Vue.use(VueRouter)

const routes = routers.routes

Vue.prototype.$ajax = axios

//loop all filter
Object.keys(filters.filterObj).forEach((key) => {
  Vue.filter(key, filters.filterObj[key])
});

const router = new VueRouter({
  routes
})

FastClick.attach(document.body)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  router,
  render: h => h(App)
}).$mount('#app-box')
