<template>
<div :class = "custom">
  <b>Trending tweets now:</b>
  <p>#Alonetogether</p>
  <p>#CoronaTime!</p>
  <p>#zoombombmyclassplease</p>
  <p>#itstheendoftheworldasweknowitandifeelfine</p>
</div>
  <div :class = "custom">
    <div class="card text-center">

      <div class="card-body">
        <h5 class="card-title">INSERT TITLE HERE</h5>
        <p class="card-text">INSERT TWEET HERE</p>
        <a href="#" class="btn btn-primary">Link to tweet/bio?</a>
      </div>
      <div class="card-footer text-muted">
        Display how recent tweet was posted
      </div>
    </div>
  </div>
</template>
<script>

export default {
  name: 'twitter-card',
  props: {
    custom: {
      type: String,
      default: ''
    },
    ticker: {
      type: String,
      default: ''
    }
  },
  data(){
    return {
    }
  }
}
</script>
