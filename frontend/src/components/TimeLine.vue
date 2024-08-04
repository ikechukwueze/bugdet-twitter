<template>
  <div class="col-9">
    <TweetForm @new-post="get_timeline"/>
    <TweetCard
      v-for="tweet in tweets"
      :key="tweet.id"
      :id="tweet.id"
      :content="tweet.content"
      :author="tweet.author"
      :created_at="tweet.created_at"
      :referenced_tweet="tweet.referenced_tweet"
      :owner="tweet.owner"
    />
  </div>
</template>

<script>
import axios from "axios";
import TweetForm from "./TweetForm.vue";
import TweetCard from "./TweetCard.vue";


export default {
  name: "TimeLine",
  components: {
    TweetForm,
    TweetCard,
  },
  data() {
    return {
      tweets: [
        {
          id: 23,
          content: "",
          author: {},
          referenced_tweet: null,
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
