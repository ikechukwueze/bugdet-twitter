<template>
    <div class="container-fluid h-100 d-flex justify-content-center align-items-center">
      <main class="form-signin w-100 m-auto text-center">
        <form @submit.prevent="submit_login_credentials" class="">
          <div><i><img class="my-3" src="default_profile_pic.jpg" alt=""></i></div>
          <div v-show="invalid_login"><small class="text-danger">Invalid Email address or Password</small></div>
          <div class="form-floating">
            
            <input type="text" class="form-control" id="floatingInput" placeholder="name@example.com" v-model="login_credentials.username" required />
            <label for="floatingInput" class="text-secondary floating">Username</label>
          </div>
          <div class="form-floating">
            <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="login_credentials.password" required />
            <label for="floatingPassword" class="text-secondary floating">Password</label>
          </div>
  
          <div class="checkbox mb-3">
  
          </div>
          <button class="w-100 btn btn-lg btn-primary rounded-0" type="submit">
            Sign in
          </button>
        </form>
      </main>
    </div>
  </template>
  
  
  
  
  <script>
  
  import axios from "axios";
  
  
  export default {
    name: "LoginPage",
    data() {
      return {
        login_credentials: {
          username: '',
          password: ''
        },
        invalid_login: false
      }
    },
    components: {},
    methods: {
      submit_login_credentials() {
        axios({
          method: "post",
          url: '/accounts/login/',
          data: this.login_credentials
        })
          .then((response) => {
            var auth_data = JSON.stringify(response.data)
            this.$store.commit('setAuthState', auth_data)
            //this.$router.push({name: 'home'})
            location.reload()
          })
          .catch(error => {
              console.log(error)
            //this.login_credentials.email = ''
            //this.login_credentials.password = ''
            this.invalid_login = true
          })
  
      }
    }
  };
  
  </script>
  
  
  <style scoped>
  i img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
  }
  
  button {
    background-color: rgb(40, 78, 238);
  }
  
  .bd-placeholder-img {
    font-size: 1.125rem;
    text-anchor: middle;
    -webkit-user-select: none;
    -moz-user-select: none;
    user-select: none;
  }
  
  @media (min-width: 768px) {
    .bd-placeholder-img-lg {
      font-size: 3.5rem;
    }
  }
  
  .b-example-divider {
    height: 3rem;
    background-color: rgba(0, 0, 0, 0.1);
    border: solid rgba(0, 0, 0, 0.15);
    border-width: 1px 0;
    box-shadow: inset 0 0.5em 1.5em rgba(0, 0, 0, 0.1),
      inset 0 0.125em 0.5em rgba(0, 0, 0, 0.15);
  }
  
  .b-example-vr {
    flex-shrink: 0;
    width: 1.5rem;
    height: 100vh;
  }
  
  .bi {
    vertical-align: -0.125em;
    fill: currentColor;
  }
  
  .nav-scroller {
    position: relative;
    z-index: 2;
    height: 2.75rem;
    overflow-y: hidden;
  }
  
  .nav-scroller .nav {
    display: flex;
    flex-wrap: nowrap;
    padding-bottom: 1rem;
    margin-top: -1px;
    overflow-x: auto;
    text-align: center;
    white-space: nowrap;
    -webkit-overflow-scrolling: touch;
  }
  
  html,
  body {
    height: 100%;
  }
  
  body {
    display: flex;
    align-items: center;
    justify-content: center;
    padding-top: 40px;
    padding-bottom: 40px;
    background-color: #f5f5f5;
  }
  
  .form-signin {
    width: 100%;
    max-width: 330px;
    padding: 15px;
    margin: auto;
  }
  
  .form-signin .checkbox {
    font-weight: 400;
  }
  
  .form-signin .form-floating:focus-within {
    z-index: 2;
  }
  
  .form-signin input[type="email"] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
  }
  
  .form-signin input[type="password"] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }
  
  .form-floating input {
    border-radius: 0px;
    margin-bottom: 33px;
  }
  
  .form-floating {
    margin-bottom: 5px;
  }
  
  .floating {
    font-size: 10px;
    text-align: center;
  }
  </style>