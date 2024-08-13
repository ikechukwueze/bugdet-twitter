import { createApp } from 'vue'
import App from './App.vue'
import router from "./router";
import store from "./store"
import axios from 'axios'

//createApp(App).mount('#app')

axios.defaults.baseURL = 'http://localhost:8000'
//axios.defaults.baseURL = `${process.env.VUE_APP_BASEURL}:${process.env.VUE_APP_BASEURL_PORT}`
// axios.defaults.baseURL = process.env.VUE_APP_BASEURL

createApp(App).use(store).use(router, axios).mount("#app")