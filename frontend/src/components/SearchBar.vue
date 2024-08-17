<template>
    <form @submit.prevent="search" class="input-group mt-4 mb-3">
        <input v-model="search_query" type="text" class="form-control" :placeholder="placeholder    "
            aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" type="button" id="button-addon2"><span><i class="bi bi-search"></i></span></button>
    </form>
</template>



<script>
import axios from 'axios';

export default {
    name: 'SearchBar',
    components: {
    },
    props: {
        placeholder: {
            type: String,
            default: 'Search'
        },
    },
    data() {
        return {
            search_query: '',
            tweets: [],
        };
    },
    methods: {
        search() {
            axios({
                method: "get",
                url: `/trends/?limit=100`,
            })
                .then((response) => {
                    this.tweets = response.data.results;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },

}
</script>

<style>
.list-group-item {
    border: 0px;
}

.trend-topic {
    margin-bottom: 0px;
}

.list-group-item {
    text-align: left
}
</style>