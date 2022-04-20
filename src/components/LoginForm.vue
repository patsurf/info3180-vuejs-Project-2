<template>
    <form class="form-signin">
      <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
      <label for="email" class="sr-only">Email address</label>
      <input type="email" id="email" name="email" class="form-control" placeholder="Email address" required>
      <label for="password" class="sr-only">Password</label>
      <input type="password" name="password" id="inputPassword" class="form-control" placeholder="Password" required>
      <div class="checkbox mb-3">
        <label>
          <input type="checkbox" name="remember-me" value="remember-me"> Remember me
        </label>
      </div>
      <button class="btn btn-lg btn-primary btn-block  bg-dark" type="submit">Sign in</button>
    </form>
</template>

<script> 
export default{
  data() {
      return {
        email: '',
        password: ''
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
          'X-CSRFToken': self.csrfToken
        }
      })
       .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            // display a success message
            self.message = data.message;
            console.log(data);
            if(data.errors.length > 0) {
                self.errorFlask = data.errors;
            }
        })
        
        .catch(function (error) {
            // display an error message

            // Having issues here
            self.errorFlask = error.errors;
            console.log(error);
        });
    },

    getCsrfToken(){
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