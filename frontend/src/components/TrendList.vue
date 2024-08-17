<template>
    <div class="vh-100">
        <SearchBar />
        <div class="list-group border border-1 ">
            <div class="list-group-item fw-bold fs-5">What's happening</div>
            <template v-for="(trend, key) in trends" :key="key">
                <RouterLink :to="{ name: 'TrendFeedPage', params: { trend_term: trend.phrase } }"
                    class="list-group-item list-group-item-action">
                    <h6 class="fw-bold mb-0">{{ trend.phrase }}</h6>
                    <small class="text-muted">{{ trend.hits }} posts</small>
                </RouterLink>
            </template>
        </div>
    </div>
</template>



<script>
import axios from 'axios';
import SearchBar from './SearchBar.vue';

export default {
    name: 'TrendList',
    components: {
        SearchBar
    },
    props: {
        limit: {
            type: Number,
            default: 3
        }
    },
    methods: {
        get_trends(limit) {
            axios({
                method: "get",
                url: `/trends/?limit=${limit}`,
            })
                .then((response) => {
                    this.trends = response.data.results;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
    data() {
        return {
            trends: [],
        };
    },
    created() {
        this.get_trends(this.limit)
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