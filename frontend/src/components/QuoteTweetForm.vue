

<template>

  <div class="d-flex p-3 my-2 border-0 rounded-3">
    <div class="flex-shrink-0">
      <ProfilePic :profile_pic_url="profile_pic" :username="username" />
    </div>

    <div class="card ms-1 w-100 border-0">
      <div class="card-header border-0 px-2 bg-white">
        <form @submit.prevent="quote_tweet">
          <div class="d-flex justify-content-between">
            <div>
              <span class="fw-bold">
                {{ display_name }} <i class="bi bi-patch-check-fill"></i></span>
              <span> &#183; </span>
              <span class="text-muted"> @{{ username }} </span>
            </div>
            <div>
              <button type="submit" class="btn btn-primary repost-btn">
                Repost
              </button>
            </div>
          </div>
          <textarea class="form-control bg-transparent border-0 mt-1 p-2 w-100" minlength="1" maxlength="280"
            id="exampleFormControlTextarea1" placeholder="Add comment" rows="2" v-model="repost" required></textarea>
        </form>
      </div>
      <div class="card-body py-1">
        <SimpleTweetCard :key="id" :id="id" :content="content" :author="author" :created_at="created_at" />
      </div>
      <div class="card-footer text-muted d-flex justify-content-around border-0 bg-white">
      </div>
    </div>
  </div>

</template>








<script>
import axios from "axios";
import SimpleTweetCard from "./SimpleTweetCard"
import ProfilePic from "./ProfilePic.vue";

export default {
  name: "QuoteTweetForm",
  components: {
    SimpleTweetCard,
    ProfilePic
  },
  props: {
    id: Number,
    author: {},
    content: String,
    created_at: String,
  },
  data() {
    return {
      username: this.$store.state.username,
      display_name: this.$store.state.display_name,
      profile_pic: this.$store.state.profile_pic,
      repost: "",
    };
  },
  methods: {
    quote_tweet() {
      axios({
        method: "post",
        url: `/tweets/${this.id}/quote/`,
        data: { 'content': this.repost },
      })
        .then(() => {
          this.repost = "";
          this.$emit("quoted-tweet")
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

.bi-patch-check-fill {
  color: blue;
  font-size: 1rem;
}

.profile-pic {
  width: 30px;
  height: 30px;
  border-radius: 50%;
}

.repost-btn {
  --bs-btn-padding-y: .25rem;
  --bs-btn-padding-x: .5rem;
  --bs-btn-font-size: .75rem;
  background-color: blue;
}
</style>
