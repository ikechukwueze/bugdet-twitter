<template>
    <nav class="navbar navbar-expand-lg bg-dark bg-body-tertiary sticky-top mb-5" data-bs-theme="dark">
        <div class="container main">
            <a class="navbar-brand" href="#">Low budget twitter</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
                aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarText">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Pricing</a>
                    </li>
                </ul>
                <span class="navbar-text">
                    Sign out
                </span>
            </div>
        </div>
    </nav>
</template>




<script>
export default {
  name: 'NavBar',
  props: {
  }
}
</script>