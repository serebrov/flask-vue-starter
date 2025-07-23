import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './registerServiceWorker'

import PrimeVue from 'primevue/config'

// PrimeVue components
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import Textarea from 'primevue/textarea'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import Card from 'primevue/card'
import Menubar from 'primevue/menubar'
import Message from 'primevue/message'

// PrimeVue styles
import 'primevue/resources/themes/lara-light-blue/theme.css'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'

const app = createApp(App)

app.use(router)
app.use(PrimeVue)

// Register PrimeVue components globally
app.component('Button', Button)
app.component('InputText', InputText)
app.component('Textarea', Textarea)
app.component('DataTable', DataTable)
app.component('Column', Column)
app.component('Card', Card)
app.component('Menubar', Menubar)
app.component('Message', Message)

app.mount('#app')