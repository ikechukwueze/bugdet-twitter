<template>
    <div class="container text-center">
        <div class="row align-items-start">
            <div class="col-2">
                <slot name="left-sidebar"></slot>
            </div>
            <div class="col-7 px-5">
                <slot name="main"></slot>
            </div>
            <div class="col-3">
                <slot name="right-sidebar"></slot>
            </div>
        </div>
    </div>
</template>



<script>
export default {
    name: 'ThreeColumnLayout'
}
</script>