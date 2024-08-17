<template>
  <div class="col-9 mt-4 w-100 text-start">
    <h4 v-if="tweets.length === 0">Trying search for something else.</h4>
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
import TweetCard from "./TweetCard.vue";
import RetweetCard from "./RetweetCard.vue";


export default {
  name: "SearchResults",
  components: {
    TweetCard,
    RetweetCard
  },
  props: {
    search_query: String
  },
  data() {
    return {
      tweets: [],
    };
  },
  methods: {
    get_search_results() {
      axios({
        method: "get",
        url: `/tweets?search=${this.search_query}`,
      })
        .then((response) => {
          this.tweets = response.data.result;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    

  },
  async created() {
    this.get_search_results();
  },
};
</script>

<style>
.main {
  max-width: 1200px;
}
</style>
