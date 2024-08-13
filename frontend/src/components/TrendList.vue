<template>
    <div class="vh-100">
        <form class="card mt-4 mb-3">
            <div class="input-group">
                <input type="text" class="form-control" placeholder="Search">
            </div>
        </form>
        <div class="list-group border border-1 vh-50">
            <div class="list-group-item fw-bold fs-5">What's happening</div>
            <a href="#" class="list-group-item list-group-item-action">
                <h6 class="fw-bold mb-0">London</h6>
                <small class="text-muted">10.4k posts</small>
            </a>
            <a href="#" class="list-group-item list-group-item-action">
                <h6 class="fw-bold mb-0">The Boys</h6>
                <small class="text-muted">10.4k posts</small>
            </a>
            <a href="#" class="list-group-item list-group-item-action">
                <h6 class="fw-bold mb-0">Botswana</h6>
                <small class="text-muted">10.4k posts</small>
            </a>
            <a href="#" class="list-group-item list-group-item-action">
                <h6 class="fw-bold mb-0">#ManCity</h6>
                <small class="text-muted">10.4k posts</small>
            </a>
        </div>
    </div>
</template>



<script>

export default {
    name: 'TrendList',
    components: {},
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