<template>
  <TweetCard :key="tweet.id" :id="tweet.id" :content="tweet.content" :author="tweet.author"
    :created_at="tweet.created_at" :referenced_tweet="tweet.referenced_tweet"
    :tweet_type="tweet.tweet_type" />
  <ReplyTweetForm :id="tweet.id" :author="tweet.author" />
</template>

<script>
import axios from "axios";
import TweetCard from "./TweetCard.vue";
import ReplyTweetForm from "./ReplyTweetForm.vue";


export default {
  name: "TweetDetail",
  components: {
    TweetCard,
    ReplyTweetForm
  },
  props: {
    tweet_id: Number
  },
  data() {
    return {
      tweet: {
        id: '',
        author: {},
        content: '',
        created_at: '',
        tweet_type: '',
        referenced_tweet: null
      },
    };
  },
  methods: {
    get_tweet_detail(id) {
      axios({
        method: "get",
        url: `/tweets/${id}/detail/`,
      })
        .then((response) => {
          this.tweet = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  async created() {
    this.get_tweet_detail(this.tweet_id);
  },
  watch: {
    tweet_id(new_id) {
      this.get_tweet_detail(new_id)
    }
  }
};
</script>

<style>
.main {
  max-width: 1200px;
}
</style>
