<template>
  <div class="col-9">
    <TweetForm @new-post="get_timeline"/>
    <TwitterPost />
    <!-- <TwitterPost
      v-for="tweet in tweets"
      :key="tweet.tweet.id"
      :id="tweet.tweet.id"
      :content="tweet.tweet.content"
      :author="tweet.tweet.author"
      :created_at="tweet.tweet.created_at"
      :reply_count="tweet.reply_count"
      :like_count="tweet.like_count"
      :dislike_count="tweet.dislike_count"
      :repost_count="tweet.repost_count"
      
    /> -->
  </div>
</template>

<script>
import axios from "axios";
import TweetForm from "./TweetForm.vue";
import TwitterPost from "./TwitterPost.vue";

export default {
  name: "TimeLine",
  components: {
    TweetForm,
    TwitterPost,
  },
  data() {
    return {
      tweets: [
        {
          id: 1,
          content: "",
          reply_count: 0,
          like_count: 0,
          dislike_count: 0,
          repost_count: 0,
          author: {},
          referenced_tweet: {},
          tweet_type: "",
          created_at: "",
        },
      ],
    };
  },
  methods: {
    get_timeline() {
      axios({
        method: "get",
        url: "http://localhost:8000/tweets/timeline/",
      })
        .then((response) => {
          this.tweets = response.data;
          console.log(response.data)
        })
        .catch((error) => {
          console.log(error);
        });
    },

    get_replies_count(tweet_id) {
      axios({
        method: "get",
        url: `http://localhost:8000/tweets/${tweet_id}/reply-count/`,
      })
        .then((response) => {
          this.tweets.reply_count = response.data.reply_count;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    get_repost_count(tweet_id) {
      axios({
        method: "get",
        url: `http://localhost:8000/tweets/${tweet_id}/repost-count/`,
      })
        .then((response) => {
          this.tweets.repost_count = response.data.repost_count;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    get_like_count(tweet_id) {
      axios({
        method: "get",
        url: `http://localhost:8000/tweets/${tweet_id}/like-count/`,
      })
        .then((response) => {
          this.tweets.like_count = response.data.like_count;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    get_dislike_count(tweet_id) {
      axios({
        method: "get",
        url: `http://localhost:8000/tweets/${tweet_id}/dislike-count/`,
      })
        .then((response) => {
          this.tweets.dislike_count = response.data.dislike_count;
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
