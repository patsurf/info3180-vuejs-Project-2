<template>
    <h1 class="h3 mb-3 font-weight-normal text-center">Log in to your account</h1>
    <form class="form-signin" @submit.prevent="loginUser" id="loginForm" method="POST" enctype="multipart/form-data">
      <div v-if="message" class="alert alert-success" role="alert">{{ message }}</div>
      <li v-for ="err in errorFlask " class="alert alert-danger" role="alert">{{ err }}</li>
      <div class="form-group col-md-4">
        <label for="username" class="sr-only">Username</label>
        <input type="username" id="username" name="username" class="form-control" v-model="username" placeholder="Username" required>
      </div>
      <div class="form-group col-md-4">
        <label for="password" class="sr-only">Password</label>
        <input type="password" id="password" name="password" class="form-control" v-model="password" placeholder="Password" required> <br>
      </div> 
      <button class="btn btn-lg btn-primary" type="submit">Login</button>
    </form>
</template>

<script>
import router from "../router";
import store from '@/main.js'; 

 
export default{
  data() {
      return {
        message: '',
        csrf_token: '',
        errorFlask: [],
        username: '',
        password: ''
      }
  },
  created() {
    this.getCsrfToken();
    this.checkLogin();
  },
  methods: {
    loginUser() {
      let loginForn = document.getElementById('loginForm');
      let form_data = new FormData(loginForn);
      let self = this;

      fetch("/api/auth/login", {
        method: "POST",
        body: form_data,

        headers: {
          'X-CSRF-TOKEN': this.csrfToken
        }
      })
       .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            // display a success message
            if(data.token == ''){
              self.message = data.errmessage;
              sessionStorage.setItem('token', null);
              sessionStorage.setItem('user_id', null);
              store.commit('check', false);
              console.log('message', self.errmessage);
            }
            else{
              console.log(data);
              self.message = data.message;
              self.token = data.token;
              self.user_id = data.user_id;
              sessionStorage.setItem('token', self.token);
              sessionStorage.setItem('user_id', self.user_id);
              sessionStorage.setItem('auth', true);
              store.commit('check', true);
              router.push('/');  
            }
              console.log("message: ", self.message);
              console.log("token: ", self.token);
              console.log("user_id: ", self.user_id);
              console.log("status: ", store.state.check);

              

        }).catch(function (error) {
            // display an error message
            self.errorFlask = error.errors;
            console.log(error);
        });
    },
    getCsrfToken() {
      console.log("status: ", this.$store.state.check);
      let self = this;
      fetch("/api/csrf-token")
          .then((response) => {
              return response.json();
          })
          .then((data) => {
              console.log(data);
              self.csrfToken = data.csrf_token;
          })
    },
    checkLogin() {
      let self = this;
      if(sessionStorage.getItem('token') != null){
        self.token = sessionStorage.getItem('token');
        self.user_id = sessionStorage.getItem('user_id');
        self.message = 'You are logged in';
        store.commit('check', true);
        router.push('/');
      }
    }
  }
}
</script>