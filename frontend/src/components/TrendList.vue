<template>
    <div class="vh-100">
        <form class="card mt-4 mb-3">
            <div class="input-group">
                <input type="text" class="form-control" placeholder="Search">
            </div>
        </form>
        <div class="list-group border border-1 ">
            <div class="list-group-item fw-bold fs-5">What's happening</div>
            <a v-for="(trend, key) in trends" :key="key" href="#" class="list-group-item list-group-item-action">
                <h6 class="fw-bold mb-0">{{ trend.phrase }}</h6>
                <small class="text-muted">{{ trend.hits }} posts</small>
            </a>
        </div>
    </div>
</template>



<script>
import axios from 'axios';

export default {
    name: 'TrendList',
    components: {},
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