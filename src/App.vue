<script>
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
import Navigation from "@/components/Navigation.vue";

export default{
    components:{
      Navigation,
      AppHeader,
      AppFooter,
    },created(){
      this.if_reload();
    },
    computed: {
      //Second navigation bar
       getConditionallyRenderedNavbar() {
         console.log('Session Storage Auth: ', sessionStorage.getItem('auth')); 
          if(sessionStorage.getItem('auth') == 'true'){
            return Navigation;
          }
          else{
            return AppHeader;
          }
       }
    },
    methods: {
      if_reload(){
        if(sessionStorage.getItem('user_id') !== 'null'){
          this.$store.commit('check', true);
        }
      }
    },
}
</script>

<template>
  <keep-alive>
    <component :is="getConditionallyRenderedNavbar"/>
  </keep-alive>

  <main>
    <RouterView />
  </main>

  <!-- <AppFooter></AppFooter> -->
</template>


<style>
  body {
    padding-top: 75px;
    font-family: Roboto, sans-serif;
  }
</style>