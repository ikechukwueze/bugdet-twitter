<template>
  <div class="row mx-1" :class="{ 'd-none': !show_tweet }">
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
    </div>
  </div>
</template>

<script>
import axios from "axios";

let uid = 0;

export default {
  name: "TwitterPostt",
  components: {
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
      delete_tweet_id: ""
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
    }

  },
  created() {
    this.is_liked = this.liked_tweet;
    this.is_disliked = this.disliked_tweet;
    this.is_owner = this.owner == this.author.username;

    uid++;
    
    this.reply_modal_id = `reply-${uid}`,
    this.reply_modal_close_button_id = `reply-button-${uid}`,
    this.main_tweet_modal_id = `tweet-body-modal-${uid}`
    this.delete_tweet_id = `delete-tweet-${uid}`
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
