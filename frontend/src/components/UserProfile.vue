<template>
  <div class="col-9 mt-4 w-100 text-start">
    <UserDetailCard :username="username" />
    <div class="col-9 mt-4 w-100 text-start">
      <nav>
        <div class="nav nav-pills nav-fill" id="nav-tab" role="tablist">
          <button class="nav-link active" id="nav-posts-tab" data-bs-toggle="tab" data-bs-target="#nav-posts"
            type="button" role="tab" aria-controls="nav-posts" aria-selected="true">Posts</button>
          <button class="nav-link" id="nav-replies-tab" data-bs-toggle="tab" data-bs-target="#nav-replies" type="button"
            role="tab" aria-controls="nav-replies" aria-selected="false">Replies</button>

          <button class="nav-link" id="nav-quotes-tab" data-bs-toggle="tab" data-bs-target="#nav-quotes" type="button"
            role="tab" aria-controls="nav-quotes" aria-selected="false">Quotes</button>

          <button class="nav-link" id="nav-retweets-tab" data-bs-toggle="tab" data-bs-target="#nav-retweets"
            type="button" role="tab" aria-controls="nav-retweets" aria-selected="false">Retweets</button>

          <button class="nav-link" id="nav-likes-tab" data-bs-toggle="tab" data-bs-target="#nav-liked-tweets"
            type="button" role="tab" aria-controls="nav-likes" aria-selected="false">Likes</button>
          <button class="nav-link" id="nav-dislikes-tab" data-bs-toggle="tab" data-bs-target="#nav-disliked-tweets"
            type="button" role="tab" aria-controls="nav-dislikes" aria-selected="false">Dislikes</button>
        </div>
      </nav>
      <div class="tab-content" id="nav-tabContent">
        <div class="tab-pane fade show active" id="nav-posts" role="tabpanel" aria-labelledby="nav-posts-tab"
          tabindex="0">
          <TweetCard v-for="tweet in tweets" :key="tweet.id" :id="tweet.id" :content="tweet.content"
            :author="tweet.author" :created_at="tweet.created_at" :referenced_tweet="tweet.referenced_tweet"
            :owner="tweet.owner" :tweet_type="tweet.tweet_type" />
        </div>
        <div class="tab-pane fade" id="nav-replies" role="tabpanel" aria-labelledby="nav-replies-tab" tabindex="0">
          <TweetCard v-for="tweet in replies" :key="tweet.id" :id="tweet.id" :content="tweet.content"
            :author="tweet.author" :created_at="tweet.created_at" :referenced_tweet="tweet.referenced_tweet"
            :owner="tweet.owner" :tweet_type="tweet.tweet_type" />
        </div>

        <div class="tab-pane fade" id="nav-quotes" role="tabpanel" aria-labelledby="nav-quotes-tab" tabindex="0">
          <TweetCard v-for="tweet in quotes" :key="tweet.id" :id="tweet.id" :content="tweet.content"
            :author="tweet.author" :created_at="tweet.created_at" :referenced_tweet="tweet.referenced_tweet"
            :owner="tweet.owner" :tweet_type="tweet.tweet_type" />
        </div>

        <div class="tab-pane fade" id="nav-retweets" role="tabpanel" aria-labelledby="nav-retweets-tab" tabindex="0">
          <RetweetCard v-for="tweet in retweets" :key="tweet.referenced_tweet.id" :id="tweet.referenced_tweet.id"
            :content="tweet.referenced_tweet.content" :author="tweet.referenced_tweet.author"
            :created_at="tweet.referenced_tweet.created_at" :retweeted_by="tweet.author.username" />
        </div>

        <div class="tab-pane fade" id="nav-liked-tweets" role="tabpanel" aria-labelledby="nav-liked-tweets-tab"
          tabindex="0">
          <TweetCard v-for="tweet in liked_tweets" :key="tweet.id" :id="tweet.id" :content="tweet.content"
            :author="tweet.author" :created_at="tweet.created_at" :referenced_tweet="tweet.referenced_tweet"
            :owner="tweet.owner" :tweet_type="tweet.tweet_type" />
        </div>

        <div class="tab-pane fade" id="nav-disliked-tweets" role="tabpanel" aria-labelledby="nav-disliked-tweets-tab"
          tabindex="0">
          <TweetCard v-for="tweet in disliked_tweets" :key="tweet.id" :id="tweet.id" :content="tweet.content"
            :author="tweet.author" :created_at="tweet.created_at" :referenced_tweet="tweet.referenced_tweet"
            :owner="tweet.owner" :tweet_type="tweet.tweet_type" />
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from "axios";
import TweetCard from "./TweetCard.vue";
import UserDetailCard from "./UserDetailCard.vue";
import RetweetCard from "./RetweetCard.vue";


export default {
  name: "UserProfileVue",
  components: {
    TweetCard,
    RetweetCard,
    UserDetailCard
  },
  props: {
    username: String
  },
  data() {
    return {
      tweets: [],
      replies: [],
      quotes: [],
      retweets: [],
      liked_tweets: [],
      disliked_tweets: [],
    };
  },
  methods: {
    get_user_tweets(username) {
      axios({
        method: "get",
        url: `tweets/${username}/`,
      })
        .then((response) => {
          this.tweets = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    get_user_replies(username) {
      axios({
        method: "get",
        url: `tweets/${username}/replies`,
      })
        .then((response) => {
          this.replies = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    get_user_quotes(username) {
      axios({
        method: "get",
        url: `tweets/${username}/quotes`,
      })
        .then((response) => {
          this.quotes = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    get_user_retweets(username) {
      axios({
        method: "get",
        url: `tweets/${username}/retweets`,
      })
        .then((response) => {
          this.retweets = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    get_user_liked_tweets(username) {
      axios({
        method: "get",
        url: `tweets/${username}/liked-tweets`,
      })
        .then((response) => {
          this.liked_tweets = response.data;
          console.log(this.liked_tweets)
        })
        .catch((error) => {
          console.log(error);
        });
    },
    get_user_disliked_tweets(username) {
      axios({
        method: "get",
        url: `tweets/${username}/disliked-tweets`,
      })
        .then((response) => {
          this.disliked_tweets = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },



  },
  async created() {
    this.get_user_tweets(this.username)
    this.get_user_replies(this.username)
    this.get_user_quotes(this.username)
    this.get_user_retweets(this.username)
    this.get_user_liked_tweets(this.username)
    this.get_user_disliked_tweets(this.username)
  },
  watch: {
    username(val) {
      this.get_user_tweets(val)
      this.get_user_replies(val)
      this.get_user_quotes(val)
      this.get_user_retweets(val)
      this.get_user_liked_tweets(val)
      this.get_user_disliked_tweets(val)
    }
  }
};
</script>

<style>
.main {
  max-width: 1200px;
}
</style>
