<template>
  <a :href="'/profile/' + username">
    <img class="rounded-circle profile-pic" :style="profile_pic_style" :src="profile_pic_url" />
  </a>
</template>

<script>
export default {
  name: "ProfilePic",
  components: {
  },
  props: {
    username: String,
    profile_pic_url: String,
    pic_width: {
      type: Number,
      default: 40
    },
    pic_height: {
      type: Number,
      default: 40
    }
  },
  data() {
    return {
      profile_pic_style: {
        width: `${this.pic_width}px`,
        height: `${this.pic_height}px`,
      }
    };
  },

};
</script>

<style scoped>
.bi-patch-check-fill {
  color: blue;
  font-size: 1rem;
}

.profile-pic {
  /* width: 30px;
  height: 30px; */
  border-radius: 50%;
}
</style>
