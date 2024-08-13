<template>
  <div class="row">
    <div class="d-flex p-3 my-2 border rounded-3">
      <div class="flex-shrink-0">
        <img class="rounded-circle profile-pic" :src="this.$store.state.profile_pic" />
      </div>
      <div class="card ms-0 w-100 border-0">
        <div class="card-header border-0 bg-white">
          <div class="d-flex justify-content-between">
            <div>
              Replying to
              <span class="fw-bold">
                @{{ author.username }}
              </span>
            </div>
            <div>
              <span><small>{{ created_at }}</small></span>
            </div>
          </div>
        </div>
        <div class="card-body py-1 px-0">
          <form @submit.prevent="reply_tweet">
            <div class="card-body py-1 bg-transparent">
              <textarea class="form-control bg-transparent border-1" minlength="1" maxlength="280s"
                id="exampleFormControlTextarea1" placeholder="Post your reply" rows="3" v-model="content"
                required></textarea>
            </div>
            <div class="card-footer text-muted d-flex justify-content-end border-0 bg-white">
              <button class="btn btn-sm" type="submit" style="background-color: blue; color: white">
                Reply
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>



<script>
import axios from "axios";

export default {
  name: "ReplyTweetForm",
  props: {
    id: Number,
    author: {
      username: String
    }
  },
  data() {
    return {
      content: "",
    };
  },
  methods: {
    reply_tweet() {
      axios({
        method: "post",
        url: `/tweets/${this.id}/reply/`,
        data: { content: this.content },
      })
        .then(() => {
          this.content = "";
          this.$emit("replied-tweet")
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.form-control {
  resize: none;
}

.tweet-faorm {
  background-color: blue
}

.profile-pic {
  width: 30px;
  height: 30px;
  border-radius: 50%;
}
</style>
