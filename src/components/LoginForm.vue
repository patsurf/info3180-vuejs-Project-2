<template>
    <form class="form-signin">
      <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
      <label for="inputEmail" class="sr-only">Email address</label>
      <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required>
      <label for="inputPassword" class="sr-only">Password</label>
      <input type="password" id="inputPassword" class="form-control" placeholder="Password" required>
      <div class="checkbox mb-3">
        <label>
          <input type="checkbox" value="remember-me"> Remember me
        </label>
      </div>
      <button class="btn btn-lg btn-primary btn-block  bg-dark" type="submit">Sign in</button>
    </form>
</template>

<script> 
// export default{
//     data() {
//         return {
//             form: {
//                 email: '',
//                 password: ''
//             }
//         }
//     },
//     }
//     methods: {
//         let loginForm = document.getElementById('loginForm');
//         let form_data = new FormData(loginForm);
//         let self = this;

//         fetch('/api/auth/login',{
//             method: 'POST',
//             body: form_data
//             headers: {
//                 'Authorization': 'Bearer ' + localStorage.getItem('access_token')
//             }
//         })
    

//     };
// }
</script>