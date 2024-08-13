<template>
    <div class="container-fluid h-100 d-flex justify-content-center bg-dark">
      <main class="w-100 m-auto text-center text-white">
          <h1 class="fw-bolder" style="font-size: 90px">4O4</h1>
          <h1>The page you're looking for does not exist.</h1>
          <router-link class="btn btn-primary text-white" :to="{name: 'HomePage'}">Go Home</router-link>
      </main>
    </div>
  </template>
  
  
  <script>
  export default {
      name: 'LostPup'
  }
  </script>