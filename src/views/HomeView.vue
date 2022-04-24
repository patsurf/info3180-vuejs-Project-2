<template>
    <img id="Car_logo" alt="Car logo" class="logo" src="uploads\photo-1542282088-fe8426682b8f.jfif"/> 
    <div class="container">
      <!-- <img alt="Car logo" class="logo" src="uploads\photo-1542282088-fe8426682b8f.jfif"/> -->
      <div class="Herotext">
        <h1>Buy and Sell Cars Online</h1> 
        <p>United Auto Sales provides the fastest, easiest and most user friendly way to buy or sell cars online. Find a  Great Price on the Vehicle You Want</p> 
        <button type="button" class="btn btn-primary btn-lg" @click="registerUser()" id="Register">Register</button> <button class="btn btn-success btn-lg" @click="loginUser()" id="Login">Login</button>   
      </div>
      
    </div>
</template>
<script>
import router from "../router";

export default {
    data() {
        return {
        };
    },

    methods: {
        registerUser() {
            router.push('/register');
        },
        loginUser() {
            router.push('/login');
        }
    },
}
</script>

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