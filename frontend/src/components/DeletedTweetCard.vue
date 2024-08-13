<template>
  <div class="row">
    <div class="d-flex p-3 my-2 border rounded-3">
      <div class="card ms-1 w-100 border-0">
        <div class="card-header border-0 bg-white">

        </div>
        <div class="card-body py-1">
          <p class="card-text"><i>This tweet was deleted by the tweet author.</i></p>
        </div>
        <div class="card-footer text-muted d-flex justify-content-around border-0 bg-white">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DeletedTweetCard",
  components: {
  },
  props: {
  },
  data() {
    return {
    };
  },

  methods: {
  },

  created() {
  },
};
</script>

<style scoped>
.bi-patch-check-fill {
  color: blue;
  font-size: 1rem;
}

.profile-pic {
  width: 30px;
  height: 30px;
  border-radius: 50%;
}
</style>
