<script>
import { RouterLink } from "vue-router";

export default{
    data() {
        return {
            check: sessionStorage.getItem('user_id')
        };
    },
    methods() {
        return {
            registerUser() {
                router.push('/register');
            },
            loginUser() {
                router.push('/login');
            },
            logoutUser() {
                sessionStorage.removeItem('user_id');
                router.push('/');
            },
            userDetails() {
              if (sessionStorage.getItem('user_id') != null) {
                router.push('/user/' + sessionStorage.getItem('user_id'));
              }
              else {
                router.push('/login');
              }
            }
        };
    },
    components: {
        RouterLink
    }
}
</script>

<template>
  <header>
     <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
      <RouterLink class="navbar-brand" to="/"><fa icon="car" /> United Auto Sales</RouterLink>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse" :key="$route.fullPath">
          <ul class="navbar-nav">
            <li class="nav-item">
              <RouterLink class="nav-link" to="/about">About</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/explore">Explore Cars</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/cars/new">Add Car</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{name: 'user-details'}" @click="userDetails()">My Profile</RouterLink>
            </li>
            <li class="nav-item mr-sm-2">
              <RouterLink class="nav-link float-end" to="/logout">Logout</RouterLink>
            </li>
          </ul>
        </div>
    </nav>
 </header> 
</template>

<style>
/* Add any component specific styles here */
  /* body {
    background-color: #fff;
  } */
  .Herotext {
    inline-size: 400px;
    position: absolute;
    top: 50%;
    transform: translate(0, -50%);
    padding: 10px;
  }
  .Herotext h1 {
    font-size: 50px;
    font-weight: bold;
    padding-bottom: 15px;
    color: #005888;
  }
  .Herotext button {
    margin-right: 50px;
  }
  .Herotext button:hover {
    background-color: #005888;
  }
  .Herotext p {
    font-size: 16px;
    color: #5e5c5c;
    padding-bottom: 15px;
  }
  #Car_logo {
    /* float: right; */
    
    right: 50%;
    transform: translate(200%, 0);
    width: 30%;
    margin-top:0px;
  }
</style>
