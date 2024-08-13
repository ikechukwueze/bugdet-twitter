<template>
  <div class="col-9 mt-4 w-100 text-start">
    <TweetForm @new-post="get_timeline"/>
    <template v-for="tweet in tweets">
      <template v-if="tweet.tweet_type === 'RETWEET'">
        <RetweetCard
          :key="tweet.referenced_tweet.id"
          :id="tweet.referenced_tweet.id"
          :content="tweet.referenced_tweet.content"
          :author="tweet.referenced_tweet.author"
          :created_at="tweet.referenced_tweet.created_at"
          :retweeted_by="tweet.author.username"
        />
      </template>
      <template v-else>
        <TweetCard
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
      </template>
    </template>
  </div>
</template>

<script>
import axios from "axios";
import TweetForm from "./TweetForm.vue";
import TweetCard from "./TweetCard.vue";
import RetweetCard from "./RetweetCard.vue";


export default {
  name: "HomeTimeLine",
  components: {
    TweetForm,
    TweetCard,
    RetweetCard
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
        },
      ],
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
