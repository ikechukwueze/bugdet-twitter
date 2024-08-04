<template>
  <NavBar />
  <div class="container main">
    <div class="row">
      <TimeLine />
      <TrendList />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import NavBar from './components/NavBar.vue'
import TimeLine from './components/TimeLine.vue'
import TrendList from './components/TrendList.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    TimeLine,
    TrendList
  },
  beforeCreate() {
    axios.defaults.headers.common['Authorization'] = 'Token 974373f3650388f209d86c5492864ddf4fa74a57'
  }
}
</script>

<style>
.main {
  max-width: 1200px;
}
</style>
