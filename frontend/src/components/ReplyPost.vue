<template>
  <div class="row mx-1 ">
    <div class="d-flex p-3 my-1 rounded-3">
      <div class="flex-shrink-0">
        <img class="rounded-circle profile-pic" :src="author.profile_pic" />
      </div>
      <div class="card ms-1 w-100 border-0">
        <div class="card-header border-0 bg-white">
          <div class="d-flex justify-content-between">
            <div>
              <span class="fw-bold">
                {{ author.display_name}} <i class="bi bi-patch-check-fill"></i
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
            data-bs-dismiss="modal"
          >
            Reply
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

let uid = 0;

export default {
  name: "ReplyPost",
  emits: ["update_reply_count"],
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
  },
  data() {
    return {
      reply: "",
    };
  },
  methods: {
    reply_tweet() {
      axios({
        method: "post",
        url: `http://localhost:8000/tweets/reply/${this.id}/`,
        data: {
            "content": this.reply
        },
      })
        .then((response) => {
          this.reply = "";
          this.$emit("update_reply_count", response.data.reply_count);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    uid++;
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



i.bi-heart-fill {
  color: blue;
}

i.bi-hand-thumbs-down-fill {
  color: rgb(255, 0, 55);
}
</style>
