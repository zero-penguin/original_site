import { createApp } from 'vue'
import App from './App.vue'
import router from './VueRouter/index'

createApp(App)
    .use(router)
    .mount('#app')