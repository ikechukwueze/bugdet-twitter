<template>
  <div class="col-9">
    <TweetForm @new-post="get_timeline"/>
    <SimpleTweetCard
      v-for="tweet in tweets"
      :key="tweet.id"
      :id="tweet.id"
      :content="tweet.content"
      :author="tweet.author"
      :created_at="tweet.created_at"
      :owner="tweet.owner"
    />
  </div>
</template>

<script>
import axios from "axios";
import TweetForm from "./TweetForm.vue";
// import TweetCard from "./TweetCard.vue";
import SimpleTweetCard from "./SimpleTweetCard.vue";


export default {
  name: "TimeLine",
  components: {
    TweetForm,
    SimpleTweetCard,

  },
  data() {
    return {
      tweets: [
        {
          id: 23,
          content: "",
          author: {},
          referenced_tweet: {},
          tweet_type: "",
          created_at: "",
          owner: ""
        },
      ],
    };
  },
  methods: {
    get_timeline() {
      axios({
        method: "get",
        url: "http://localhost:8000/timeline/home/",
      })
        .then((response) => {
          this.tweets = response.data;
          console.log(this.tweets)
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
