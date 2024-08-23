<template>
  <div class="row" :class="{ 'd-none': is_deleted }">
    <div class="d-flex p-3 my-2 border rounded-3">

      <div class="flex-shrink-0">
        <ProfilePic :profile_pic_url="author.profile_pic" :username="username" />
      </div>


      <div class="card ms-1 w-100 border-0">
        <div class="card-header border-0 bg-white">
          <div class="d-flex justify-content-between">
            <div>
              <span class="fw-bold">
                {{ author.display_name }} <i class="bi bi-patch-check-fill"></i></span>
              <span> &#183; </span>
              <span class="text-muted"> @{{ author.username }} </span>
            </div>
            <div>
              <span><small>{{ created_at }}</small></span>
            </div>
          </div>
        </div>
        <div class="card-body py-1" @click="push_to_tweet_thread">
          <template v-if="tweet_type === 'REPLY'">
            <template v-if="referenced_tweet">
              <p class="card-text text-muted text-sm">
                Replying to @{{ referenced_tweet.author.username }}
              </p>
            </template>
            <template v-else>
              <p class="card-text text-muted text-sm">
                Replying to <i>a deleted tweet</i>
              </p>
            </template>
          </template>
          <p class="card-text">{{ content }}</p>
          <template v-if="tweet_type === 'QUOTE'">
            <template v-if="referenced_tweet">
              <SimpleTweetCard :key="referenced_tweet.id" :id="referenced_tweet.id" :content="referenced_tweet.content"
                :author="referenced_tweet.author" :created_at="referenced_tweet.created_at" />
            </template>
            <template v-else>
              <DeletedTweetCard />
            </template>
          </template>
        </div>
        <div class="card-footer text-muted d-flex justify-content-around border-0 bg-white">
          <div>
            <i class="bi bi-chat interactions" data-bs-toggle="modal" :data-bs-target="`#${reply_modal_id}`"></i>
            <span class="badge text-muted">{{ reply_count }}</span>
          </div>
          <div>
            <i @click="like_tweet" class="bi interactions"
              :class="{ 'bi-heart': !is_liked, 'bi-heart-fill': is_liked }">
            </i><span class="badge text-muted">{{ like_count }}</span>
          </div>
          <div>
            <i @click="dislike_tweet" class="bi interactions" :class="{
              'bi-hand-thumbs-down': !is_disliked,
              'bi-hand-thumbs-down-fill': is_disliked,
            }"></i><span class="badge text-muted">{{ dislike_count }}</span>
          </div>
          <div>
            <i class="bi interactions" data-bs-toggle="modal" :data-bs-target="`#${quote_modal_id}`"
              :class="{ 'bi-chat-quote': !is_quoted, 'bi-chat-quote-fill': is_quoted }"></i><span
              class="badge text-muted">{{
                quote_count }}</span>
          </div>
          <div>
            <i @click="retweet_tweet" class="bi interactions"
              :class="{ 'bi-repeat': !is_retweeted, 'bi-repeat text-primary text-bold': is_retweeted }"></i><span
              class="badge text-muted">{{ retweet_count }}</span>
          </div>
          <div>
            <i class="interactions" data-bs-toggle="modal" :data-bs-target="`#delete-${unique_id}`"
              :class="{ 'bi bi-trash': is_owner }"></i>
          </div>
        </div>
      </div>

      <!-- Delete tweet modal -->
      <div class="modal" :id="`delete-${unique_id}`" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
        aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-sm">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body text-center">
              <h5><strong>Delete tweet?</strong></h5>
            </div>
            <div class="modal-footer d-flex justify-content-around">
              <button @click="delete_tweet" type="button" class="btn btn-danger" data-bs-dismiss="modal">
                Delete
              </button>
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                Close
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Reply Modal -->
      <div class="modal fade" :id="reply_modal_id" data-bs-keyboard="false" tabindex="-1"
        aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable">
          <div class="modal-content">
            <div class="modal-header border border-0">
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"
                :id="reply_modal_close_button_id"></button>
            </div>
            <div class="mx-4">
              <SimpleTweetCard :key="id" :id="id" :content="content" :author="author" :created_at="created_at" />
              <ReplyTweetForm :id="id" :author="author" @replied-tweet="replied_tweet" />
            </div>
          </div>
        </div>
      </div>


      <!-- Quote Modal -->
      <div class="modal fade" :id="quote_modal_id" data-bs-keyboard="false" tabindex="-1"
        aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable">
          <div class="modal-content">
            <div class="modal-header border border-0">
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"
                :id="quote_modal_close_button_id"></button>
            </div>
            <div class="mx-4">
              <QuoteTweetForm @quoted-tweet="quoted_tweet" :key="id" :id="id" :content="content" :author="author"
                :created_at="created_at" />
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import axios from "axios";
import SimpleTweetCard from "./SimpleTweetCard"
import ReplyTweetForm from "./ReplyTweetForm.vue"
import QuoteTweetForm from "./QuoteTweetForm.vue"
import DeletedTweetCard from "./DeletedTweetCard.vue";
import ProfilePic from "./ProfilePic.vue";
import router from "@/router";

let uid = 0;

export default {
  name: "TweetCard",
  components: {
    SimpleTweetCard,
    ReplyTweetForm,
    QuoteTweetForm,
    DeletedTweetCard,
    ProfilePic
  },
  props: {
    id: Number,
    author: {},
    content: String,
    created_at: String,
    referenced_tweet: null,
    tweet_type: String,
  },
  data() {
    return {
      replies: [],
      username: '',
      is_liked: false,
      is_disliked: false,
      is_quoted: false,
      is_retweeted: false,
      is_owner: false,
      is_deleted: false,
      unique_id: null,
      main_tweet_modal_id: "",
      delete_tweet_id: "",
      like_count: 0,
      dislike_count: 0,
      reply_count: 0,
      repost_count: 0,
      retweet_count: 0,
      quote_count: 0,
      reply_modal_id: "",
      reply_modal_close_button_id: "",
      quote_modal_id: "",
      quote_modal_close_button_id: "",
      owner: false
    };
  },

  methods: {

    get_reply_count() {
      axios({
        method: "get",
        url: `/tweets/${this.id}/reply-count/`,
      })
        .then((response) => {
          this.reply_count = response.data.reply_count;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    get_repost_count() {
      axios({
        method: "get",
        url: `/tweets/${this.id}/repost-count/`,
      })
        .then((response) => {
          this.repost_count = response.data.repost_count;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    get_retweet_count() {
      axios({
        method: "get",
        url: `/tweets/${this.id}/retweet-count/`,
      })
        .then((response) => {
          this.retweet_count = response.data.retweet_count;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    get_quote_count() {
      axios({
        method: "get",
        url: `/tweets/${this.id}/quote-count/`,
      })
        .then((response) => {
          this.quote_count = response.data.quote_count;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    get_like_count() {
      axios({
        method: "get",
        url: `/tweets/${this.id}/like-count/`,
      })
        .then((response) => {
          this.like_count = response.data.like_count;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    get_dislike_count() {
      axios({
        method: "get",
        url: `/tweets/${this.id}/dislike-count/`,
      })
        .then((response) => {
          this.dislike_count = response.data.dislike_count;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    like_tweet() {
      axios({
        method: "post",
        url: `/tweets/${this.id}/like/`,
      })
        .then(() => {
          this.get_like_status();
          this.get_dislike_status()
          this.get_like_count()
          this.get_dislike_count()
        })
        .catch((error) => {
          console.log(error);
        });
    },

    dislike_tweet() {
      axios({
        method: "post",
        url: `/tweets/${this.id}/dislike/`,
      })
        .then(() => {
          this.get_like_status();
          this.get_dislike_status()
          this.get_like_count()
          this.get_dislike_count()

        })
        .catch((error) => {
          console.log(error);
        });
    },

    retweet_tweet() {
      axios({
        method: "post",
        url: `/tweets/${this.id}/retweet/`,
      })
        .then(() => {
          this.get_retweet_count()
          this.get_retweet_status()
        })
        .catch((error) => {
          console.log(error);
        });
    },

    get_like_status() {
      axios({
        method: "get",
        url: `/tweets/${this.id}/like-status/`,
      })
        .then((response) => {
          this.is_liked = response.data.is_liked;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    get_dislike_status() {
      axios({
        method: "get",
        url: `/tweets/${this.id}/dislike-status/`,
      })
        .then((response) => {
          this.is_disliked = response.data.is_disliked;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    get_quote_status() {
      axios({
        method: "get",
        url: `/tweets/${this.id}/quote-status/`,
      })
        .then((response) => {
          this.is_quoted = response.data.is_quoted;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    get_retweet_status() {
      axios({
        method: "get",
        url: `/tweets/${this.id}/retweet-status/`,
      })
        .then((response) => {
          this.is_retweeted = response.data.is_retweeted;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    delete_tweet() {
      axios({
        method: "delete",
        url: `/tweets/${this.id}/delete/`,
      })
        .then(() => {
          this.is_deleted = true
        })
        .catch((error) => {
          console.log(error);
        });
    },

    quoted_tweet() {
      document.getElementById(this.quote_modal_close_button_id).click();
      this.get_quote_count()
      this.get_quote_status()
      this.$emit("tweet-interaction")
    },

    replied_tweet() {
      document.getElementById(this.reply_modal_close_button_id).click();
      this.get_reply_count()
      this.get_reply_status()
      this.$emit("tweet-interaction")
    },

    push_to_tweet_thread() {
      router.push({ name: 'ThreadPage', params: { tweet_id: this.id } })
    }

  },
  created() {

    this.get_like_count()
    this.get_dislike_count()
    this.get_reply_count()
    this.get_repost_count()
    this.get_retweet_count()
    this.get_quote_count()

    this.is_liked = this.get_like_status();
    this.is_disliked = this.get_dislike_status();
    this.is_quoted = this.get_quote_status()
    this.is_retweeted = this.get_retweet_status()

    this.is_owner = this.$store.state.username == this.author.username;
    this.username = this.author.username

    uid++;

    this.delete_tweet_id = `delete-tweet-${uid}`;

    this.reply_modal_id = `reply-${uid}`;
    this.reply_modal_close_button_id = `reply-button-${uid}`;

    this.quote_modal_id = `quote-${uid}`;
    this.quote_modal_close_button_id = `quote-button-${uid}`;

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
  width: 40px;
  height: 40px;
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

.card-body {
  cursor: pointer;
}
</style>
