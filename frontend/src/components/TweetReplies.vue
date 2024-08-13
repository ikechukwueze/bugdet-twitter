<template>
  <TweetCard v-for="tweet in replies" :key="tweet.id" :id="tweet.id" :content="tweet.content" :author="tweet.author"
      :created_at="tweet.created_at" :referenced_tweet="tweet.referenced_tweet"
      :tweet_type="tweet.tweet_type" />
</template>

<script>
import axios from "axios";
import TweetCard from "./TweetCard.vue";


export default {
  name: "TweetReplies",
  components: {
    TweetCard,
  },
  props: {
    tweet_id: Number
  },
  data() {
    return {
      replies: []
    };
  },
  methods: {
    get_tweet_replies(id) {
      axios({
        method: "get",
        url: `/tweets/${id}/replies/`,
      })
        .then((response) => {
          this.replies = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  async created() {
    this.get_tweet_replies(this.tweet_id)
  },
  watch: {
    tweet_id(new_id) {
      this.get_tweet_replies(new_id)
    }
  }
};
</script>

<style>
.main {
  max-width: 1200px;
}
</style>
