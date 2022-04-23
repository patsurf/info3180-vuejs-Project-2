<template>
  <header>
     <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
      <RouterLink class="navbar-brand" to="/"><fa icon="car" /> United Auto Sales</RouterLink>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse" :key="$route.fullPath">
          <ul class="navbar-nav nav">
            <li class="nav-item">
              <RouterLink class="nav-link" to="/about">About</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/register">Register</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/login">Login</RouterLink>
            </li>
          </ul>
        </div>
    </nav>
 </header> 
</template>

<script>
import { RouterLink } from "vue-router";

export default {
    data() {
        return {
             check : sessionStorage.getItem('user_id')
        };
    },
}
</script>

<style>
/* Add any component specific styles here */
.nav{
  float: right;
}
</style>