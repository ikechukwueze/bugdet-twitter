<template>
  <div class="col-9 mt-4 w-100 text-start">
    <TweetForm @new-post="get_timeline"/>
    <TweetList :tweets="tweets" />
  </div>
</template>

<script>
import axios from "axios";
import TweetForm from "./TweetForm.vue";
import TweetList from "./TweetList.vue";


export default {
  name: "HomeTimeLine",
  components: {
    TweetForm,
    TweetList
  },
  data() {
    return {
      tweets: [],
    };
  },
  methods: {
    get_timeline() {
      axios({
        method: "get",
        url: "/timeline/home/",
      })
        .then((response) => {
          this.tweets = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    

  },
  async created() {
    this.get_timeline();
  },
};
</script>

<style>
.main {
  max-width: 1200px;
}
</style>
