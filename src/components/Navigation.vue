<script>
import { RouterLink } from "vue-router";

export default{
    data() {
        return {
            check: sessionStorage.getItem('user_id')
        };
    },
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
              <RouterLink class="nav-link" :to="{name: 'user-details'}" >My Profile</RouterLink>
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
   
</style>

