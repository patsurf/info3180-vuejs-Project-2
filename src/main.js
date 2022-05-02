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
      if(to.path === '/cars/new' && sessionStorage.getItem('auth') === 'false'){
        next('/login')
      }else if(to.path === '/explore' && sessionStorage.getItem('auth') === 'false'){
        next('/login')
      }
      else{
        next()
      }
      if(to.path === '/logout' && sessionStorage.getItem('auth') === 'true'){
        console.log("was loggged out");
        sessionStorage.setItem('token', null );
        sessionStorage.setItem('user_id', null );
        sessionStorage.setItem('auth', false );
        store.commit('check', false);
        console.log(store.state.check)
        window.location.reload();
        next('/');
  
  
      }
      if(to.path === '/login' && sessionStorage.getItem('token') !== 'null'){
        console.log("was loggged in");
        next('/explore');
  
  
      }
      
    });


const app = createApp(App)
.component('fa', FontAwesomeIcon)

app.use(router)
app.use(store)

app.mount('#app')

export default store
