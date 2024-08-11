<template>
  <div class="col-9 mt-4 w-100 text-start">
    <UserDetailCard :username="username" />
    <TweetCard
      v-for="tweet in tweets"
      :key="tweet.id"
      :id="tweet.id"
      :content="tweet.content"
      :author="tweet.author"
      :created_at="tweet.created_at"
      :referenced_tweet="tweet.referenced_tweet"
      :owner="tweet.owner"
      :tweet_type="tweet.tweet_type"
      @tweet-interaction="get_timeline"
    />
  </div>
</template>

<script>
import axios from "axios";
import TweetCard from "./TweetCard.vue";
import UserDetailCard from "./UserDetailCard.vue";


export default {
  name: "TimeLine",
  components: {
    TweetCard,
    UserDetailCard
  },
  props: {
    username: String
  },
  data() {
    return {
      tweets: [
        {
          id: null,
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
    get_timeline(username) {
      axios({
        method: "get",
        url: `timeline/${username}/`,
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
    this.get_timeline(this.username);
  },
  watch: {
    username(val){
      this.get_timeline(val)
    }
  }
};
</script>

<style>
.main {
  max-width: 1200px;
}
</style>
