import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { createStore } from 'vuex'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(fas)

// Create Vuex store
const store = createStore({
    state(){
        return{
            token: sessionStorage.getItem('token') || null,
            user_id: sessionStorage.getItem('user_id') || null,
            auth: sessionStorage.getItem('auth') || false,
            check: '',
        }
  
    },
    mutations:{
      check(state, auth){
         state.check= auth
      },
  
  
  },
  
  });
  
  router.beforeEach((to, from, next) => {
      console.log('State: ', store.state.check)
      if(to.path === '/new-car' && store.state.check === ''){
        next('/login')
      }else if(to.path === '/explore' && store.state.check === ''){
        next('/login')
      }
      else{
        next()
      }
      if(to.path === '/logout' && store.state.check === true){
        console.log("was loggged out");
        sessionStorage.setItem('token', null );
        sessionStorage.setItem('user_id', null );
        sessionStorage.setItem('auth', false );
        store.commit('check', false);
        console.log(store.state.check)
        window.location.reload();
        next('/');
  
  
      }
      
    });

const app = createApp(App)
.component('fa', FontAwesomeIcon)

app.use(router)
app.use(store)

app.mount('#app')

export default store
