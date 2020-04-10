<template>
<div :class = "custom">
  <b>Trending tweets now:</b>
  <p>#Alonetogether</p>
  <p>#CoronaTime!</p>
  <p>#zoombombmyclassplease</p>
  <p>#itstheendoftheworldasweknowitandifeelfine</p>
</div>
</template>
<script>

  export default {
    name: 'twitter-card',
    props: {
      custom: {
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
