<template>
  <div class="row" :class="{ 'd-none': !show_tweet }">
    <div class="d-flex p-3 my-2 border rounded-3">
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
        <div
          class="card-body py-1"
          data-bs-toggle="modal"
          :data-bs-target="`#${main_tweet_modal_id}`"
          @click="get_tweet_replies"
        >
          <p class="card-text">{{ content }}</p>
        </div>
        <div
          class="card-footer text-muted d-flex justify-content-around border-0 bg-white"
        >
          <div>
            <i
              class="bi bi-chat interactions"
              data-bs-toggle="modal"
              :data-bs-target="`#${reply_modal_id}`"
            ></i
            ><span class="badge text-muted">{{ reply_count }}</span>
          </div>
          <div>
            <i
              @click="like_tweet"
              class="bi interactions"
              :class="{ 'bi-heart': !is_liked, 'bi-heart-fill': is_liked }"
            ></i
            ><span class="badge text-muted">{{ like_count }}</span>
          </div>
          <div>
            <i
              @click="dislike_tweet"
              class="bi interactions"
              :class="{
                'bi-hand-thumbs-down': !is_disliked,
                'bi-hand-thumbs-down-fill': is_disliked,
              }"
            ></i
            ><span class="badge text-muted">{{ dislike_count }}</span>
          </div>
          <div>
            <i class="bi bi-arrow-repeat interactions"></i
            ><span class="badge text-muted">{{ repost_count }}</span>
          </div>
          <div>
            <i
              class="interactions"
              data-bs-toggle="modal"
              :data-bs-target="`#delete-${unique_id}`"
              :class="{ 'bi bi-trash': is_owner }"
            ></i>
          </div>
        </div>
      </div>

      <!-- Delete tweet modal -->
      <div
        class="modal"
        :id="`delete-${unique_id}`"
        data-bs-backdrop="static"
        data-bs-keyboard="false"
        tabindex="-1"
        aria-labelledby="staticBackdropLabel"
        aria-hidden="true"
      >
        <div class="modal-dialog modal-dialog-centered modal-sm">
          <div class="modal-content">
            <div class="modal-header">
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <div class="modal-body text-center">
              <h5><strong>Delete tweet?</strong></h5>
            </div>
            <div class="modal-footer d-flex justify-content-around">
              <button
                @click="delete_tweet"
                type="button"
                class="btn btn-danger"
                data-bs-dismiss="modal"
              >
                Delete
              </button>
              <button
                type="button"
                class="btn btn-secondary"
                data-bs-dismiss="modal"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Reply Modal -->
      <div
        class="modal fade"
        :id="reply_modal_id"
        data-bs-keyboard="false"
        tabindex="-1"
        aria-labelledby="staticBackdropLabel"
        aria-hidden="true"
      >
        <div
          class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable"
        >
          <div class="modal-content">
            <div class="modal-header border border-0">
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
                :id="reply_modal_close_button_id"
              ></button>
            </div>

            <ReplyPost
              :id="this.id"
              :author="this.author"
              :content="this.content"
              :reply_count="this.reply_count"
              :repost_count="this.repost_count"
              :like_count="this.like_count"
              :dislike_count="this.dislike_count"
              :created_at="this.created_at"
              @update_reply_count="update_reply_counts"
            />
          </div>
        </div>
      </div>

      <!-- Main tweet modal -->

      <div
        class="modal fade"
        :id="main_tweet_modal_id"
        data-bs-keyboard="false"
        tabindex="-1"
        aria-labelledby="staticBackdropLabel"
        aria-hidden="true"
      >
        <div class="modal-dialog modal-lg modal-dialog-scrollable">
          <div class="modal-content">
            <div class="modal-header border border-0">
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <div class="modal-body">
              
              <TwitterPostt
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
            </div>
            
          </div>
        </div>
      </div>
      <!-- <div
        class="modal fade"
        id="exampleModal"
        tabindex="-1"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h1 class="modal-title fs-5" id="exampleModalLabel">
                Modal title
              </h1>
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <div class="modal-body">...</div>
            <div class="modal-footer">
              <button
                type="button"
                class="btn btn-secondary"
                data-bs-dismiss="modal"
              >
                Close
              </button>
              <button type="button" class="btn btn-primary">
                Save changes
              </button>
            </div>
          </div>
        </div>
      </div> -->
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ReplyPost from "./ReplyPost.vue";
//import TweetReplies from "./TweetReplies.vue";
import TwitterPostt from "./TwitterPostt.vue";

let uid = 0;

export default {
  name: "TwitterPost",
  components: {
    ReplyPost,
    //TweetReplies,
    TwitterPostt,
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
    liked_tweet: Boolean,
    disliked_tweet: Boolean,
    owner: String,
    show_tweet: Boolean,
  },
  data() {
    return {
      is_liked: false,
      is_disliked: false,
      is_owner: false,
      unique_id: null,
      reply_modal_id: "",
      reply_modal_close_button_id: "",
      main_tweet_modal_id: "",
      delete_tweet_id: "",
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
    like_tweet() {
      axios({
        method: "patch",
        url: `http://localhost:8000/tweets/like/${this.id}`,
      })
        .then((response) => {
          this.is_liked = response.data.is_liked;
          if (this.is_liked) {
            this.is_disliked = false;
          }
          this.$emit("update:like_count", response.data.like_count);
          this.$emit("update:dislike_count", response.data.dislike_count);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    dislike_tweet() {
      axios({
        method: "patch",
        url: `http://localhost:8000/tweets/dislike/${this.id}`,
      })
        .then((response) => {
          this.is_disliked = response.data.is_disliked;
          if (this.is_disliked) {
            this.is_liked = false;
          }
          this.$emit("update:like_count", response.data.like_count);
          this.$emit("update:dislike_count", response.data.dislike_count);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    delete_tweet() {
      axios({
        method: "delete",
        url: `http://localhost:8000/tweets/delete/${this.id}`,
      })
        .then(() => {
          this.$emit("update:show_tweet", false);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    update_reply_counts(n) {
      this.$emit("update:reply_count", n);
    },

    get_tweet_replies() {
      axios({
        method: "get",
        url: `http://localhost:8000/tweets/reply/${this.id}/`,
      })
        .then((response) => {
          this.replies = response.data;
          console.log(this.replies);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.is_liked = this.liked_tweet;
    this.is_disliked = this.disliked_tweet;
    this.is_owner = this.owner == this.author.username;

    uid++;

    (this.reply_modal_id = `reply-${uid}`),
      (this.reply_modal_close_button_id = `reply-button-${uid}`),
      (this.main_tweet_modal_id = `tweet-body-modal-${uid}`);
    this.delete_tweet_id = `delete-tweet-${uid}`;
    this.unique_id = uid;
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

i.interactions {
  cursor: pointer;
}

i.bi-heart-fill {
  color: blue;
}

i.bi-hand-thumbs-down-fill {
  color: rgb(255, 0, 55);
}
</style>
