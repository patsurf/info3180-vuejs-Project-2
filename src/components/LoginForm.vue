<template>
    <form class="form-signin" @submit.prevent="loginUser" id="loginForm" method="POST" enctype="multipart/form-data">
      <div v-if="message" class="alert alert-success" role="alert">{{ message }}</div>
      <li v-for ="err in errorFlask " class="alert alert-danger" role="alert">{{ err }}</li>
      <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
      <label for="username" class="sr-only">Username</label>
      <input type="username" id="username" name="username" class="form-control" placeholder="Username" required>
      <label for="email" class="sr-only">Email address</label>
      <input type="email" id="email" name="email" class="form-control" placeholder="Email address" required>
      <label for="password" class="sr-only">Password</label>
      <input type="password" name="password" id="inputPassword" class="form-control" placeholder="Password" required>
      <button class="btn btn-lg btn-primary btn-block  bg-dark" type="submit">Sign in</button>
    </form>
</template>

<script>
import router from "../router";

 
export default{
  data() {
      return {
        message: '',
        token: '',
        errorFlask: []
      }
  },
  created() {
    this.getCsrfToken();
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
          "Authorization": 'Bearer ' + self.token,
          'X-CSRF-TOKEN': this.csrfToken
        }
      })
       .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            // display a success message
              console.log(data);
              self.message = data.message;
              console.log(self.message);
              self.token = data.token;
              console.log(self.token);
              sessionStorage.setItem('token', self.token);
              router.push('/');  

        }).catch(function (error) {
            // display an error message
            self.errorFlask = error.errors;
            console.log(error);
        });
    },
    getCsrfToken() {
      let self = this;
      fetch("/api/csrf-token")
          .then((response) => {
              return response.json();
          })
          .then((data) => {
              console.log(data);
              self.csrfToken = data.csrf_token;
          })
    }
  }
}
</script>