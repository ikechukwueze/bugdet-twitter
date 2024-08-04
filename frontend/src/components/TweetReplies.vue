<!-- <template>
  <div class="row mx-1">
    <div class="d-flex p-3 my-1 rounded-3">
      <div class="flex-shrink-0">
        <img class="rounded-circle profile-pic" :src="author.profile_pic" />
      </div>
      <div class="card ms-1 w-100 border-0">
        <div class="card-header border-0 bg-white">
          <div class="d-flex justify-content-between">
            <div>
              <span class="fw-bold">
                {{ author.display_name }} <i class="bi bi-patch-check-fill"></i
              ></span>
              <span> &#183; </span>
              <span class="text-muted"> @{{ author.username }} </span>
            </div>
            <div>
              <span
                ><small>{{ created_at }}</small></span
              >
            </div>
          </div>
        </div>
        <div class="card-body py-1">
          <p class="card-text">{{ content }}</p>
        </div>
        <div
          class="card-footer text-muted d-flex justify-content-around border-0 bg-white"
        >
          <div>
            <i class="bi bi-chat"></i
            ><span class="badge text-muted">{{ reply_count }}</span>
          </div>
          <div>
            <i class="bi bi-heart"></i
            ><span class="badge text-muted">{{ like_count }}</span>
          </div>
          <div>
            <i class="bi bi-hand-thumbs-down"></i
            ><span class="badge text-muted">{{ dislike_count }}</span>
          </div>
          <div>
            <i class="bi bi-arrow-repeat"></i
            ><span class="badge text-muted">{{ repost_count }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="row p-3">
    <div class="col-1">
      <img class="rounded-circle" src="https://placehold.co/60" alt="" />
    </div>
    <div class="col-11">
      <form @submit.prevent="reply_tweet">
        <div class="card-body py-1 bg-transparent">
          <textarea
            class="form-control bg-transparent"
            minlength="1"
            maxlength="280s"
            id="exampleFormControlTextarea1"
            placeholder="Reply"
            rows="3"
            v-model="reply"
            required
          ></textarea>
        </div>
        <div
          class="card-footer text-muted d-flex justify-content-end border-0 bg-white bg-transparent"
        >
          <button
            class="btn btn-sm"
            type="submit"
            style="background-color: blue; color: white"
          >
            Reply
          </button>
        </div>
      </form>
    </div>
  </div>
  <TwitterPost
    v-for="tweet in replies"
    :key="tweet.id"
    :id="tweet.id"
    :content="tweet.content"
    :reply_count="tweet.reply_count"
    :like_count="tweet.like_count"
    :dislike_count="tweet.dislike_count"
    :repost_count="tweet.repost_count"
    :author="tweet.author"
    :created_at="tweet.created_at"
    :liked_tweet="tweet.is_liked"
    :disliked_tweet="tweet.is_disliked"
    :owner="tweet.owner"
    :show_tweet="tweet.show_tweet"
    @update:show_tweet="(n) => (tweet.show_tweet = n)"
    @update:like_count="(n) => (tweet.like_count = n)"
    @update:dislike_count="(n) => (tweet.dislike_count = n)"
    @update:reply_count="(n) => (tweet.reply_count = n)"
  />
</template> -->




<template>
  <TwitterPost
    v-for="tweet in replies"
    :key="tweet.id"
    :id="tweet.id"
    :content="tweet.content"
    :reply_count="tweet.reply_count"
    :like_count="tweet.like_count"
    :dislike_count="tweet.dislike_count"
    :repost_count="tweet.repost_count"
    :author="tweet.author"
    :created_at="tweet.created_at"
    :liked_tweet="tweet.is_liked"
    :disliked_tweet="tweet.is_disliked"
    :owner="tweet.owner"
    :show_tweet="tweet.show_tweet"
    @update:show_tweet="(n) => (tweet.show_tweet = n)"
    @update:like_count="(n) => (tweet.like_count = n)"
    @update:dislike_count="(n) => (tweet.dislike_count = n)"
    @update:reply_count="(n) => (tweet.reply_count = n)"
  />
</template>




<script>
import axios from "axios";
import TwitterPost from "./TwitterPost.vue";

let uid = 0;

export default {
  name: "TweetReplies",
  components: {
    TwitterPost,
  },
  props: {
    id: Number,
    author: {},
    content: String,
    like_count: Number,
    dislike_count: Number,
    repost_count: Number,
    reply_count: Number,
    created_at: String,
  },
  data() {
    return {
      reply: "",
      replies: [
        {
          id: 1,
          content: "",
          reply_count: 0,
          like_count: 0,
          dislike_count: 0,
          repost_count: 0,
          author: {},
          created_at: "",
          liked_tweet: null,
          disliked_tweet: null,
        },
      ],
    };
  },
  methods: {
    get_tweet_replies() {
      axios({
        method: "get",
        url: `http://localhost:8000/tweets/reply/${this.id}/`,
      })
        .then((response) => {
          this.replies = response.data;
          //console.log(this.replies)
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    uid++;
    this.unique_id = uid;
    this.get_tweet_replies();
  },
};
</script>

<style scoped>
.bi-patch-check-fill {
  color: blue;
  font-size: 1rem;
}

.profile-pic {
  width: 60px;
  height: 60px;
  border-radius: 50%;
}

i.bi-heart-fill {
  color: blue;
}

i.bi-hand-thumbs-down-fill {
  color: rgb(255, 0, 55);
}
</style>
