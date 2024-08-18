<template>
    <form @submit.prevent="push_to_search" class="input-group mt-4 mb-3">
        <input v-model="search_query" type="text" class="form-control" :placeholder="placeholder" required
            aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" type="submit" id="button-addon2"><span><i class="bi bi-search"></i></span></button>
    </form>
</template>



<script>
import router from '@/router';

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
        };
    },
    methods: {
        push_to_search() {
            router.push({ name: 'SearchResultsPage', params: { search_query: this.search_query } })
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