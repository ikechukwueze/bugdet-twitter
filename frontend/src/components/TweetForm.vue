<template>
  <div class="mb-5 tweet-form">
    <div class="row border rounded p-3">
      <div class="col-1">
        <img class="rounded-circle profile-pic" :src="this.$store.state.profile_pic" alt="" />
      </div>
      <div class="col-11">
        <form @submit.prevent="post_tweet">
          <div class="card-body py-1 bg-transparent">
            <textarea
              class="form-control bg-transparent"
              minlength="1"
              maxlength="280s"
              id="exampleFormControlTextarea1"
              placeholder="What's on your mind?"
              rows="3"
              v-model="content"
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
              Post!
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";

export default {
  name: "TweetForm",
  props: {},
  data() {
    return {
      content: "",
      profile_pic: ""
    };
  },
  methods: {
    post_tweet() {
      axios({
        method: "post",
        url: "/tweets/post/",
        data: { content: this.content },
      })
        .then(() => {
          this.content = "";
          this.$emit("new-post")
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created () {
    this.profile_pic = this.$store.state.profile_pic
  }
};
</script>

<style scoped>
.form-control {
  resize: none;
}

.tweet-foarm {
  background-color:rgb(216, 216, 236)
}

.profile-pic {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}
</style>
