<template>
  <header>
     <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
      <font-awesome-icon icon="fa-solid fa-car"/>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
          <ul class="navbar-nav">
            <li class="nav-item">
              <RouterLink to="/" class="nav-link active">Supreme Auto Sales</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/about">About</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/register">Register</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/login">Login</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/cars">Explore Cars</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/cars/new">Add Car</RouterLink>
            </li>
          </ul>
        </div>
    </nav>
 </header> 
</template>

<script>
import { RouterLink } from "vue-router";
</script>

<style>
/* Add any component specific styles here */
</style>