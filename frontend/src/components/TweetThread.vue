<template>
  <div class="col-9 mt-4 w-100 text-start">
    <TweetDetail :tweet_id="tweet_id" />
    <TweetReplies :tweet_id="tweet_id" />
  </div>
</template>

<script>
import TweetDetail from "./TweetDetail.vue";
import TweetReplies from "./TweetReplies.vue";

export default {
  name: "TweetThread",
  components: {
    TweetDetail,
    TweetReplies
  },
  props: {
    tweet_id: Number
  },
  data() {
    return {
    };
  },
  methods: {
  },

};
</script>

<style>
.main {
  max-width: 1200px;
}
</style>
