<template>
    <form class="form-signin" @submit.prevent="loginUser" id="loginForm" method="POST" enctype="multipart/form-data">
      <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
      <label for="email" class="sr-only">Email address</label>
      <input type="email" id="email" name="email" class="form-control" placeholder="Email address" v-model="email" required>
      <label for="password" class="sr-only">Password</label>
      <input type="password" name="password" id="inputPassword" class="form-control" placeholder="Password" v-model="password" required>
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
      }
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
          "Authorization": 'Bearer ' + self.token
        }
      })
       .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            // display a success message
            self.message = data.message;
            console.log(data);
            let token = data.response.token;
            sessionStorage.setItem('token', token);
            self.token = token;
            alert("Login successful");
            router.push('/');
        }).catch(function (error) {
            // display an error message
            self.errorFlask = error.errors;
            console.log(error);
        });
    }
  }
}
</script>